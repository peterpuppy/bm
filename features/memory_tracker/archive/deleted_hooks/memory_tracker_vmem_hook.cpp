/*-------------------------------------------------------------------------
Copyright Notice
Copyright (c)  Booming Tech All rights reserved.
-------------------------------------------------------------------------*/


#include "chaos/core/memory/tracker/memory_tracker_vmem_hook.h"
#include "chaos/core/memory/tracker/memory_tracker.h"
#include "chaos/core/memory/tracker/memory_tracker_hook_utils.h"
#include "chaos/base/logger/logger_system.h"

#include <Windows.h>
#include <Psapi.h>
#include "detours.h"

#include <atomic>
#include <array>
#include <cctype>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <intrin.h>
#include <mutex>
#include <string>

#pragma comment(lib, "Psapi.lib")

namespace Chaos
{
namespace MemTrack
{
namespace
{
    // -------- Re-entrance guard (OS TLS) --------
    // See memory_tracker_hook_utils.h for design rationale.
    using namespace Chaos::MemTrack::HookUtils;

    // -------- Real function pointers (Detours patches in install) --------
    static decltype(&::VirtualAlloc)    Real_VirtualAlloc    = ::VirtualAlloc;
    static decltype(&::VirtualAllocEx)  Real_VirtualAllocEx  = ::VirtualAllocEx;
    static decltype(&::VirtualFree)     Real_VirtualFree     = ::VirtualFree;

    // ntdll!NtAllocateVirtualMemory / NtFreeVirtualMemory.
    // These are the NT syscall stubs that ALL user-mode alloc paths eventually
    // funnel through (VirtualAlloc, D3D12 driver, V8 internals, etc.).
    // Loaded dynamically via GetProcAddress so we don't need <winternl.h>.
    // NTSTATUS == LONG; using LONG directly to avoid the header dependency.
    using PFN_NtAllocateVirtualMemory = LONG (NTAPI*)(HANDLE, PVOID*, ULONG_PTR, PSIZE_T, ULONG, ULONG);
    using PFN_NtFreeVirtualMemory     = LONG (NTAPI*)(HANDLE, PVOID*, PSIZE_T, ULONG);
    static PFN_NtAllocateVirtualMemory Real_NtAllocateVirtualMemory = nullptr;
    static PFN_NtFreeVirtualMemory     Real_NtFreeVirtualMemory     = nullptr;

    // -------- Module attribution cache --------
    // Each loaded module gets two source IDs: one for reserve tracking and
    // one for commit tracking. They live in parallel "VirtualAllocReserveFrom_<dll>"
    // and "VirtualAllocCommitFrom_<dll>" sources in the Tracker.
    struct ModuleEntry
    {
        std::uintptr_t base;
        std::uintptr_t end;
        SourceId       reserveSourceId;
        SourceId       commitSourceId;
    };
    static constexpr std::size_t kMaxModules = 256;
    static std::array<ModuleEntry, kMaxModules> s_modules {};
    static std::atomic<std::size_t> s_moduleCount {0};
    static std::mutex s_moduleRegMutex;

    static std::atomic<SourceId> s_unknownReserveSourceId {kInvalidSourceId};
    static std::atomic<SourceId> s_unknownCommitSourceId  {kInvalidSourceId};

    // -------- ptr -> size tables (separate for reserve and commit) --------
    // VirtualFree has no size param on MEM_RELEASE/DECOMMIT, so we cache the
    // size at alloc/commit time and look it up on free/decommit.
    //
    // Two tables because reserve and commit are independent dimensions:
    // - Reserve: lookup by reservation base on MEM_RELEASE
    // - Commit:  lookup by commit subblock addr on MEM_DECOMMIT
    //
    // MEM_RELEASE retires the whole reservation (and implicitly all commits
    // inside it). The commit table cannot be efficiently swept by address
    // range against a hash structure, so we accept a small leak in the
    // commit table: when a reservation is released, its committed entries
    // remain in the table. In practice, V8/DirectX/Tracy reservations live
    // for the whole process lifetime, so this leak doesn't affect steady-state
    // numbers in real diagnostic sessions.
    struct PtrSizeBucket
    {
        std::atomic<std::uintptr_t> ptr  {0};   // 0 == empty
        std::atomic<std::uint64_t>  size {0};
    };
    static constexpr std::size_t kPtrSizeTableSize = 4096;  // power of 2
    static_assert((kPtrSizeTableSize & (kPtrSizeTableSize - 1)) == 0,
                  "kPtrSizeTableSize must be power of 2");
    static std::array<PtrSizeBucket, kPtrSizeTableSize> s_reserveTable {};
    static std::array<PtrSizeBucket, kPtrSizeTableSize> s_commitTable  {};

    inline std::size_t hashPtr(std::uintptr_t p)
    {
        // VirtualAlloc returns are page-aligned (low 12 bits zero), so
        // shift down before hashing to spread bits.
        std::uint64_t k = p >> 12;
        k = (k ^ (k >> 16)) * 0x85ebca6b;
        k = (k ^ (k >> 13)) * 0xc2b2ae35;
        k = k ^ (k >> 16);
        return static_cast<std::size_t>(k) & (kPtrSizeTableSize - 1);
    }

    void storePtrSize(std::array<PtrSizeBucket, kPtrSizeTableSize>& table,
                      std::uintptr_t ptr, std::uint64_t size)
    {
        if (ptr == 0) return;
        const std::size_t startIdx = hashPtr(ptr);
        for (std::size_t probe = 0; probe < 32; ++probe)
        {
            const std::size_t idx = (startIdx + probe) & (kPtrSizeTableSize - 1);
            std::uintptr_t cur = table[idx].ptr.load(std::memory_order_acquire);
            if (cur == ptr || cur == 0)
            {
                std::uintptr_t expected = cur;
                if (cur == 0)
                {
                    if (!table[idx].ptr.compare_exchange_strong(
                            expected, ptr,
                            std::memory_order_acq_rel, std::memory_order_acquire))
                    {
                        if (expected != ptr) continue;
                    }
                }
                table[idx].size.store(size, std::memory_order_release);
                return;
            }
        }
        // Table too contended; drop. Free path will fall back to VirtualQuery.
    }

    std::uint64_t takePtrSize(std::array<PtrSizeBucket, kPtrSizeTableSize>& table,
                              std::uintptr_t ptr)
    {
        if (ptr == 0) return 0;
        const std::size_t startIdx = hashPtr(ptr);
        for (std::size_t probe = 0; probe < 32; ++probe)
        {
            const std::size_t idx = (startIdx + probe) & (kPtrSizeTableSize - 1);
            std::uintptr_t cur = table[idx].ptr.load(std::memory_order_acquire);
            if (cur == ptr)
            {
                std::uint64_t size = table[idx].size.load(std::memory_order_relaxed);
                table[idx].ptr.store(0, std::memory_order_release);
                return size;
            }
            if (cur == 0) break;
        }
        // Lookup miss; fall back to VirtualQuery.
        MEMORY_BASIC_INFORMATION mbi {};
        if (::VirtualQuery(reinterpret_cast<LPCVOID>(ptr), &mbi, sizeof(mbi)) != 0
            && mbi.State != MEM_FREE)
        {
            return mbi.RegionSize;
        }
        return 0;
    }

    // -------- Cached Tracker --------
    Tracker* s_trackerPtr = nullptr;

    // -------- Module resolution --------
    struct ResolvedSources
    {
        SourceId reserveSid;
        SourceId commitSid;
    };

    // Returns the (reserveSid, commitSid) pair for the dll containing
    // returnAddress. Populates module cache on first hit. Mempool is
    // detected and tagged so dump can subtract the overlap with Pool/*.
    ResolvedSources resolveModule(void* returnAddress)
    {
        const auto ra = reinterpret_cast<std::uintptr_t>(returnAddress);

        // Fast path: linear scan in cached entries.
        const std::size_t cnt = s_moduleCount.load(std::memory_order_acquire);
        for (std::size_t i = 0; i < cnt; ++i)
        {
            const ModuleEntry& e = s_modules[i];
            if (ra >= e.base && ra < e.end)
                return { e.reserveSourceId, e.commitSourceId };
        }

        // Slow path: register module.
        InHookGuard guard;
        ResolvedSources result { kInvalidSourceId, kInvalidSourceId };
        {
            HMODULE hMod = nullptr;
            const DWORD flags = GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS
                              | GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT;
            if (::GetModuleHandleExA(flags,
                    reinterpret_cast<LPCSTR>(returnAddress), &hMod) && hMod)
            {
                MODULEINFO mi {};
                if (::GetModuleInformation(::GetCurrentProcess(), hMod, &mi, sizeof(mi)))
                {
                    char modPath[MAX_PATH];
                    DWORD plen = ::GetModuleFileNameA(hMod, modPath, MAX_PATH);
                    if (plen > 0)
                    {
                        const char* basename = std::strrchr(modPath, '\\');
                        basename = basename ? basename + 1 : modPath;

                        std::lock_guard<std::mutex> lk(s_moduleRegMutex);
                        const std::size_t cnt2 = s_moduleCount.load(std::memory_order_relaxed);
                        const std::uintptr_t modBase = reinterpret_cast<std::uintptr_t>(mi.lpBaseOfDll);
                        for (std::size_t i = 0; i < cnt2; ++i)
                        {
                            if (s_modules[i].base == modBase)
                                return { s_modules[i].reserveSourceId, s_modules[i].commitSourceId };
                        }
                        if (cnt2 < kMaxModules && s_trackerPtr)
                        {
                            char reserveName[64];
                            char commitName[64];
                            std::snprintf(reserveName, sizeof(reserveName),
                                "%s%s", kVMemReserveSourcePrefix, basename);
                            std::snprintf(commitName, sizeof(commitName),
                                "%s%s", kVMemCommitSourcePrefix, basename);
                            SourceId rsid = s_trackerPtr->registerSource(
                                reserveName, SourceKind::Counter);
                            SourceId csid = s_trackerPtr->registerSource(
                                commitName, SourceKind::Counter);
                            if (rsid != kInvalidSourceId && csid != kInvalidSourceId)
                            {
                                ModuleEntry& e = s_modules[cnt2];
                                e.base            = modBase;
                                e.end             = modBase + mi.SizeOfImage;
                                e.reserveSourceId = rsid;
                                e.commitSourceId  = csid;
                                s_moduleCount.store(cnt2 + 1, std::memory_order_release);
                                result = { rsid, csid };
                            }
                        }
                    }
                }
            }
        }

        if (result.reserveSid == kInvalidSourceId)
        {
            SourceId ru = s_unknownReserveSourceId.load(std::memory_order_acquire);
            SourceId cu = s_unknownCommitSourceId.load(std::memory_order_acquire);
            if ((ru == kInvalidSourceId || cu == kInvalidSourceId) && s_trackerPtr)
            {
                if (ru == kInvalidSourceId)
                {
                    ru = s_trackerPtr->registerSource(
                        "VirtualAllocReserveFrom_<unknown>", SourceKind::Counter);
                    if (ru != kInvalidSourceId)
                    {
                        SourceId expected = kInvalidSourceId;
                        s_unknownReserveSourceId.compare_exchange_strong(
                            expected, ru, std::memory_order_acq_rel, std::memory_order_acquire);
                    }
                }
                if (cu == kInvalidSourceId)
                {
                    cu = s_trackerPtr->registerSource(
                        "VirtualAllocCommitFrom_<unknown>", SourceKind::Counter);
                    if (cu != kInvalidSourceId)
                    {
                        SourceId expected = kInvalidSourceId;
                        s_unknownCommitSourceId.compare_exchange_strong(
                            expected, cu, std::memory_order_acq_rel, std::memory_order_acquire);
                    }
                }
            }
            result = { ru, cu };
        }
        return result;
    }

    // -------- Hook functions --------
    LPVOID WINAPI Hook_VirtualAlloc(LPVOID lpAddress, SIZE_T dwSize,
                                    DWORD flAllocationType, DWORD flProtect)
    {
        LPVOID p = Real_VirtualAlloc(lpAddress, dwSize, flAllocationType, flProtect);
        if (!p || inHook()) return p;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::VirtualAllocHookActive))
            return p;

        const bool isReserve = (flAllocationType & MEM_RESERVE) != 0;
        const bool isCommit  = (flAllocationType & MEM_COMMIT)  != 0;
        if (!isReserve && !isCommit) return p;

        InHookGuard guard;
        void* ra = _ReturnAddress();

        ResolvedSources sids = resolveModule(ra);
        if (!s_trackerPtr) return p;

        // MEM_RESERVE: record under the reserve dimension.
        if (isReserve && sids.reserveSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.reserveSid, dwSize, p);
            storePtrSize(s_reserveTable, reinterpret_cast<std::uintptr_t>(p), dwSize);
        }

        // MEM_COMMIT: record under the commit dimension. Same call may
        // include both flags (one-shot reserve+commit) -- record both.
        if (isCommit && sids.commitSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.commitSid, dwSize, p);
            storePtrSize(s_commitTable, reinterpret_cast<std::uintptr_t>(p), dwSize);
        }
        return p;
    }

    BOOL WINAPI Hook_VirtualFree(LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType)
    {
        // Capture sizes BEFORE the actual free (in case lookup needs to
        // fall back to VirtualQuery, which won't work after release).
        std::uint64_t reserveSize = 0;
        std::uint64_t commitSize  = 0;
        const bool isRelease  = (dwFreeType & MEM_RELEASE)  != 0;
        const bool isDecommit = (dwFreeType & MEM_DECOMMIT) != 0;
        if (lpAddress && isRelease)
            reserveSize = takePtrSize(s_reserveTable, reinterpret_cast<std::uintptr_t>(lpAddress));
        if (lpAddress && isDecommit)
            commitSize  = takePtrSize(s_commitTable,  reinterpret_cast<std::uintptr_t>(lpAddress));

        BOOL ok = Real_VirtualFree(lpAddress, dwSize, dwFreeType);

        if (!ok || !lpAddress || inHook()) return ok;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::VirtualAllocHookActive))
            return ok;

        InHookGuard guard;
        void* ra = _ReturnAddress();
        ResolvedSources sids = resolveModule(ra);
        if (!s_trackerPtr) return ok;

        // MEM_DECOMMIT: only commit dimension changes; reservation stays.
        if (isDecommit && commitSize > 0 && sids.commitSid != kInvalidSourceId)
        {
            s_trackerPtr->recordFree(sids.commitSid, commitSize, lpAddress);
        }

        // MEM_RELEASE: retires the entire reservation. The committed bytes
        // inside it are implicitly released too, but we cannot efficiently
        // sweep the commit table by address range, so commit-side leaks a
        // little. In practice V8/DirectX/Tracy reservations live forever,
        // so this doesn't affect steady-state numbers.
        if (isRelease && reserveSize > 0 && sids.reserveSid != kInvalidSourceId)
        {
            s_trackerPtr->recordFree(sids.reserveSid, reserveSize, lpAddress);
        }
        return ok;
    }

    // -------- VirtualAlloc2 hook (Win10 1803+) --------
    // V8 sandbox and some DirectX 12 paths use VirtualAlloc2 instead of
    // the classic VirtualAlloc. Signature differs by a leading HANDLE
    // Process param. We only care about calls targeting the current
    // process (cross-process alloc doesn't show in our ProcessCommit).
    //
    // VirtualAlloc2 is in kernelbase.dll, not kernel32.dll. We load it
    // dynamically with GetProcAddress so the hook doesn't break on older
    // Windows versions where the export doesn't exist.
    using PFN_VirtualAlloc2 = LPVOID (WINAPI*)(HANDLE, PVOID, SIZE_T, ULONG, ULONG, MEM_EXTENDED_PARAMETER*, ULONG);
    static PFN_VirtualAlloc2 Real_VirtualAlloc2 = nullptr;

    LPVOID WINAPI Hook_VirtualAlloc2(HANDLE hProcess, PVOID lpAddress, SIZE_T dwSize,
                                     ULONG flAllocationType, ULONG flProtect,
                                     MEM_EXTENDED_PARAMETER* params, ULONG paramCount)
    {
        LPVOID p = Real_VirtualAlloc2(hProcess, lpAddress, dwSize, flAllocationType,
                                      flProtect, params, paramCount);
        // Cross-process alloc: not our memory, skip.
        if (hProcess != ::GetCurrentProcess()) return p;
        if (!p || inHook()) return p;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::VirtualAllocHookActive))
            return p;

        const bool isReserve = (flAllocationType & MEM_RESERVE) != 0;
        const bool isCommit  = (flAllocationType & MEM_COMMIT)  != 0;
        if (!isReserve && !isCommit) return p;

        InHookGuard guard;
        void* ra = _ReturnAddress();

        ResolvedSources sids = resolveModule(ra);
        if (!s_trackerPtr) return p;

        if (isReserve && sids.reserveSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.reserveSid, dwSize, p);
            storePtrSize(s_reserveTable, reinterpret_cast<std::uintptr_t>(p), dwSize);
        }
        if (isCommit && sids.commitSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.commitSid, dwSize, p);
            storePtrSize(s_commitTable, reinterpret_cast<std::uintptr_t>(p), dwSize);
        }
        return p;
    }

    // -------- VirtualAllocEx hook --------
    // Many libraries call VirtualAllocEx(GetCurrentProcess(), ...) instead of
    // the simpler VirtualAlloc(...). The two are different kernel32 exports;
    // hooking only VirtualAlloc leaves the Ex variant unobserved.
    // Cross-process calls (hProcess != our own) are skipped.
    LPVOID WINAPI Hook_VirtualAllocEx(HANDLE hProcess, PVOID lpAddress, SIZE_T dwSize,
                                      DWORD flAllocationType, DWORD flProtect)
    {
        LPVOID p = Real_VirtualAllocEx(hProcess, lpAddress, dwSize, flAllocationType, flProtect);
        // Cross-process alloc: not our memory.
        if (hProcess != ::GetCurrentProcess()) return p;
        if (!p || inHook()) return p;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::VirtualAllocHookActive))
            return p;

        const bool isReserve = (flAllocationType & MEM_RESERVE) != 0;
        const bool isCommit  = (flAllocationType & MEM_COMMIT)  != 0;
        if (!isReserve && !isCommit) return p;

        InHookGuard guard;
        void* ra = _ReturnAddress();

        ResolvedSources sids = resolveModule(ra);
        if (!s_trackerPtr) return p;

        if (isReserve && sids.reserveSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.reserveSid, dwSize, p);
            storePtrSize(s_reserveTable, reinterpret_cast<std::uintptr_t>(p), dwSize);
        }
        if (isCommit && sids.commitSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.commitSid, dwSize, p);
            storePtrSize(s_commitTable, reinterpret_cast<std::uintptr_t>(p), dwSize);
        }
        return p;
    }

    // -------- ntdll!NtAllocateVirtualMemory hook --------
    // Catches D3D12 driver, V8 internals, and anything that bypasses
    // kernel32 to call the NT syscall stub directly. This is the common
    // funnel for all user-mode VirtualAlloc-family calls.
    //
    // NTSTATUS >= 0 means success. We save BaseAddress and RegionSize BEFORE
    // calling the real function since they are in/out parameters.
    LONG NTAPI Hook_NtAllocateVirtualMemory(
        HANDLE hProcess, PVOID* pBaseAddress, ULONG_PTR ZeroBits,
        PSIZE_T pRegionSize, ULONG flAllocationType, ULONG flProtect)
    {
        // Save before: in/out params will be overwritten by real call.
        const SIZE_T reqSize = pRegionSize ? *pRegionSize : 0;

        LONG st = Real_NtAllocateVirtualMemory(
            hProcess, pBaseAddress, ZeroBits, pRegionSize,
            flAllocationType, flProtect);

        if (st < 0 || !pBaseAddress || !(*pBaseAddress) || inHook()) return st;
        if (hProcess != ::GetCurrentProcess()) return st;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::VirtualAllocHookActive))
            return st;

        const bool isReserve = (flAllocationType & MEM_RESERVE) != 0;
        const bool isCommit  = (flAllocationType & MEM_COMMIT)  != 0;
        if (!isReserve && !isCommit) return st;

        LPVOID allocated = *pBaseAddress;
        SIZE_T actualSize = pRegionSize ? *pRegionSize : reqSize;
        if (actualSize == 0) actualSize = reqSize;

        InHookGuard guard;
        void* ra = _ReturnAddress();

        ResolvedSources sids = resolveModule(ra);
        if (!s_trackerPtr) return st;

        if (isReserve && sids.reserveSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.reserveSid, actualSize, allocated);
            storePtrSize(s_reserveTable, reinterpret_cast<std::uintptr_t>(allocated), actualSize);
        }
        if (isCommit && sids.commitSid != kInvalidSourceId)
        {
            s_trackerPtr->recordAlloc(sids.commitSid, actualSize, allocated);
            storePtrSize(s_commitTable, reinterpret_cast<std::uintptr_t>(allocated), actualSize);
        }
        return st;
    }

    LONG NTAPI Hook_NtFreeVirtualMemory(
        HANDLE hProcess, PVOID* pBaseAddress, PSIZE_T pRegionSize, ULONG dwFreeType)
    {
        // Save before.
        PVOID freeAddr = pBaseAddress ? *pBaseAddress : nullptr;
        const bool isRelease  = (dwFreeType & MEM_RELEASE)  != 0;
        const bool isDecommit = (dwFreeType & MEM_DECOMMIT) != 0;
        std::uint64_t reserveSize = 0;
        std::uint64_t commitSize  = 0;
        if (freeAddr && isRelease)
            reserveSize = takePtrSize(s_reserveTable, reinterpret_cast<std::uintptr_t>(freeAddr));
        if (freeAddr && isDecommit)
            commitSize  = takePtrSize(s_commitTable,  reinterpret_cast<std::uintptr_t>(freeAddr));

        LONG st = Real_NtFreeVirtualMemory(
            hProcess, pBaseAddress, pRegionSize, dwFreeType);

        if (st < 0 || !freeAddr || inHook()) return st;
        if (hProcess != ::GetCurrentProcess()) return st;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::VirtualAllocHookActive))
            return st;

        InHookGuard guard;
        void* ra = _ReturnAddress();
        ResolvedSources sids = resolveModule(ra);
        if (!s_trackerPtr) return st;

        if (isDecommit && commitSize > 0 && sids.commitSid != kInvalidSourceId)
            s_trackerPtr->recordFree(sids.commitSid, commitSize, freeAddr);
        if (isRelease && reserveSize > 0 && sids.reserveSid != kInvalidSourceId)
            s_trackerPtr->recordFree(sids.reserveSid, reserveSize, freeAddr);
        return st;
    }

    // -------- Install state --------
    std::atomic<bool> s_installed    {false};
    std::atomic<bool> s_hookEnabled  {false};
    std::mutex        s_installMutex;
} // anonymous namespace

bool installVMemHook()
{
    if (!kMemTrackEnabled) return false;   // master switch (memory_tracker.h)
    if (s_installed.load(std::memory_order_acquire)) return true;
    std::lock_guard<std::mutex> lk(s_installMutex);
    if (s_installed.load(std::memory_order_relaxed)) return true;

    // Force Tracker singleton to fully construct first; cache pointer.
    s_trackerPtr = &Tracker::instance();
    (void)s_trackerPtr->getSourceCount();

    if (!initTls()) return false;

    // NtAllocateVirtualMemory / NtFreeVirtualMemory live in ntdll.dll.
    // These are the NT syscall stubs -- the common funnel for ALL user-mode
    // alloc paths (VirtualAlloc, D3D12 driver, V8 internals, etc.).
    HMODULE ntdll = ::GetModuleHandleA("ntdll.dll");
    if (ntdll)
    {
        Real_NtAllocateVirtualMemory = reinterpret_cast<PFN_NtAllocateVirtualMemory>(
            ::GetProcAddress(ntdll, "NtAllocateVirtualMemory"));
        Real_NtFreeVirtualMemory     = reinterpret_cast<PFN_NtFreeVirtualMemory>(
            ::GetProcAddress(ntdll, "NtFreeVirtualMemory"));
    }

    // VirtualAlloc2 is in kernelbase.dll, available Win10 1803+. Load it
    // dynamically so the hook doesn't break on older Windows or console OSes
    // where the export may not exist. If not found, VirtualAlloc2 simply
    // isn't hooked -- the classic VirtualAlloc/Free hook still works.
    HMODULE kbase = ::GetModuleHandleA("KernelBase.dll");
    if (kbase)
    {
        Real_VirtualAlloc2 = reinterpret_cast<PFN_VirtualAlloc2>(
            ::GetProcAddress(kbase, "VirtualAlloc2"));
        // Fallback: some builds alias it in kernel32
        if (!Real_VirtualAlloc2)
        {
            HMODULE k32 = ::GetModuleHandleA("kernel32.dll");
            if (k32)
                Real_VirtualAlloc2 = reinterpret_cast<PFN_VirtualAlloc2>(
                    ::GetProcAddress(k32, "VirtualAlloc2"));
        }
    }

    LONG err = NO_ERROR;
    if ((err = DetourTransactionBegin())  != NO_ERROR) return false;
    if ((err = DetourUpdateThread(GetCurrentThread())) != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_VirtualAlloc),   reinterpret_cast<PVOID>(Hook_VirtualAlloc)))   != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_VirtualAllocEx), reinterpret_cast<PVOID>(Hook_VirtualAllocEx))) != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_VirtualFree),    reinterpret_cast<PVOID>(Hook_VirtualFree)))    != NO_ERROR) { DetourTransactionAbort(); return false; }
    if (Real_VirtualAlloc2)
    {
        if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_VirtualAlloc2), reinterpret_cast<PVOID>(Hook_VirtualAlloc2))) != NO_ERROR) { DetourTransactionAbort(); return false; }
    }
    if (Real_NtAllocateVirtualMemory)
    {
        if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_NtAllocateVirtualMemory), reinterpret_cast<PVOID>(Hook_NtAllocateVirtualMemory))) != NO_ERROR) { DetourTransactionAbort(); return false; }
    }
    if (Real_NtFreeVirtualMemory)
    {
        if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_NtFreeVirtualMemory), reinterpret_cast<PVOID>(Hook_NtFreeVirtualMemory))) != NO_ERROR) { DetourTransactionAbort(); return false; }
    }
    if ((err = DetourTransactionCommit()) != NO_ERROR) return false;

    s_hookEnabled.store(true, std::memory_order_release);
    s_installed.store(true, std::memory_order_release);
    return true;
}

void uninstallVMemHook()
{
    if (!s_installed.load(std::memory_order_acquire)) return;
    std::lock_guard<std::mutex> lk(s_installMutex);
    if (!s_installed.load(std::memory_order_relaxed)) return;

    s_hookEnabled.store(false, std::memory_order_release);

    DetourTransactionBegin();
    DetourUpdateThread(GetCurrentThread());
    DetourDetach(reinterpret_cast<PVOID*>(&Real_VirtualAlloc),   reinterpret_cast<PVOID>(Hook_VirtualAlloc));
    DetourDetach(reinterpret_cast<PVOID*>(&Real_VirtualAllocEx), reinterpret_cast<PVOID>(Hook_VirtualAllocEx));
    DetourDetach(reinterpret_cast<PVOID*>(&Real_VirtualFree),    reinterpret_cast<PVOID>(Hook_VirtualFree));
    if (Real_VirtualAlloc2)
        DetourDetach(reinterpret_cast<PVOID*>(&Real_VirtualAlloc2), reinterpret_cast<PVOID>(Hook_VirtualAlloc2));
    if (Real_NtAllocateVirtualMemory)
        DetourDetach(reinterpret_cast<PVOID*>(&Real_NtAllocateVirtualMemory), reinterpret_cast<PVOID>(Hook_NtAllocateVirtualMemory));
    if (Real_NtFreeVirtualMemory)
        DetourDetach(reinterpret_cast<PVOID*>(&Real_NtFreeVirtualMemory), reinterpret_cast<PVOID>(Hook_NtFreeVirtualMemory));
    DetourTransactionCommit();

    s_installed.store(false, std::memory_order_release);
}

bool isVMemHookInstalled()
{
    return s_installed.load(std::memory_order_acquire);
}

} // namespace MemTrack
} // namespace Chaos
