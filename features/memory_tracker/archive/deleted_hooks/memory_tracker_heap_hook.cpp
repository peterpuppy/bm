/*-------------------------------------------------------------------------
Copyright Notice
Copyright (c)  Booming Tech All rights reserved.
-------------------------------------------------------------------------*/


#include "chaos/core/memory/tracker/memory_tracker_heap_hook.h"
#include "chaos/core/memory/tracker/memory_tracker.h"
#include "chaos/core/memory/tracker/memory_tracker_hook_utils.h"
#include "chaos/base/logger/logger_system.h"

#include <Windows.h>
#include <Psapi.h>
#include "detours.h"

#include <algorithm>
#include <atomic>
#include <array>
#include <cctype>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <intrin.h>      // _ReturnAddress
#include <mutex>
#include <string>

#pragma comment(lib, "Psapi.lib")

namespace Chaos
{
namespace MemTrack
{
namespace
{
    // Re-entrance guard. See memory_tracker_hook_utils.h for design rationale
    // (OS TLS vs C++ thread_local). The shared header provides g_tlsIndex,
    // inHook(), setInHook(), and InHookGuard via namespace HookUtils.
    using namespace Chaos::MemTrack::HookUtils;

    // Set true ONLY after Detours commit completes and the Tracker singleton
    // has been fully constructed. Hook callbacks check this first to avoid
    // racing with a still-in-flight install or a not-yet-constructed Tracker.
    std::atomic<bool> s_hookEnabled {false};

    // Cached Tracker pointer. After installHeapHook() forces the magic
    // static to completion, we stash &Tracker::instance() here. Hook
    // callbacks use this raw pointer DIRECTLY -- they never call
    // Tracker::instance() themselves, so they cannot race with the magic-
    // static guard, cannot trigger recursive construction, and cannot see
    // a partially-constructed singleton.
    Tracker* s_trackerPtr = nullptr;

    // Real function pointers. Detours overwrites these in installHeapHook()
    // so calls through them go to the actual kernel32 implementation.
    static decltype(&::HeapAlloc)   Real_HeapAlloc   = ::HeapAlloc;
    static decltype(&::HeapFree)    Real_HeapFree    = ::HeapFree;
    static decltype(&::HeapReAlloc) Real_HeapReAlloc = ::HeapReAlloc;

    // Module attribution cache. Linear-search a small array (loaded module
    // count is typically <100); this is hot-path code so we can't afford a
    // hash map lookup per alloc, especially one that itself allocates.
    struct ModuleEntry
    {
        std::uintptr_t base;
        std::uintptr_t end;
        SourceId       sourceId;
    };
    static constexpr std::size_t kMaxModules = 256;
    static std::array<ModuleEntry, kMaxModules> s_modules {};
    static std::atomic<std::size_t> s_moduleCount {0};
    static std::mutex s_moduleRegMutex;

    // Source for "couldn't resolve module" -- registered lazily.
    static std::atomic<SourceId> s_unknownSourceId {kInvalidSourceId};


    // Find or register a module for the given return address. Returns
    // kInvalidSourceId if module lookup fails. Sets the hook flag around
    // the registerSource path to absorb re-entrant allocations.
    SourceId resolveModule(void* returnAddress)
    {
        const auto ra = reinterpret_cast<std::uintptr_t>(returnAddress);

        // Fast path: linear scan in cached entries (lock-free read).
        const std::size_t cnt = s_moduleCount.load(std::memory_order_acquire);
        for (std::size_t i = 0; i < cnt; ++i)
        {
            const ModuleEntry& e = s_modules[i];
            if (ra >= e.base && ra < e.end) return e.sourceId;
        }

        // Slow path: lookup module + register source. Re-entrance protected.
        InHookGuard guard;
        SourceId result = kInvalidSourceId;
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
                        // Strip directory; keep "<basename>".
                        const char* basename = std::strrchr(modPath, '\\');
                        basename = basename ? basename + 1 : modPath;

                        // Register under lock; another thread may have raced
                        // to add the same module, so re-check first.
                        std::lock_guard<std::mutex> lk(s_moduleRegMutex);
                        const std::size_t cnt2 = s_moduleCount.load(std::memory_order_relaxed);
                        const std::uintptr_t modBase = reinterpret_cast<std::uintptr_t>(mi.lpBaseOfDll);
                        for (std::size_t i = 0; i < cnt2; ++i)
                        {
                            if (s_modules[i].base == modBase) return s_modules[i].sourceId;
                        }
                        if (cnt2 < kMaxModules && s_trackerPtr)
                        {
                            char sourceName[64];
                            std::snprintf(sourceName, sizeof(sourceName),
                                "%s%s", kHeapAllocSourcePrefix, basename);
                            SourceId sid = s_trackerPtr->registerSource(
                                sourceName, SourceKind::Counter);
                            if (sid != kInvalidSourceId)
                            {
                                ModuleEntry& e = s_modules[cnt2];
                                e.base     = modBase;
                                e.end      = modBase + mi.SizeOfImage;
                                e.sourceId = sid;
                                s_moduleCount.store(cnt2 + 1, std::memory_order_release);
                                result = sid;
                            }
                        }
                    }
                }
            }
        }

        // Fall back to a single "unknown" source if module lookup failed.
        if (result == kInvalidSourceId)
        {
            SourceId expected = kInvalidSourceId;
            SourceId u = s_unknownSourceId.load(std::memory_order_acquire);
            if (u == kInvalidSourceId && s_trackerPtr)
            {
                u = s_trackerPtr->registerSource(
                    "HeapAllocFrom_<unknown>", SourceKind::Counter);
                if (u != kInvalidSourceId)
                {
                    s_unknownSourceId.compare_exchange_strong(expected, u,
                        std::memory_order_acq_rel, std::memory_order_acquire);
                }
            }
            result = u;
        }

        return result;
    }

    LPVOID WINAPI Hook_HeapAlloc(HANDLE heap, DWORD flags, SIZE_T size)
    {
        LPVOID p = Real_HeapAlloc(heap, flags, size);
        if (!p || !s_hookEnabled.load(std::memory_order_acquire) || inHook()) return p;
        // Master switch: skip recording entirely when HeapHookActive is off.
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::HeapHookActive))
            return p;

        // Detours patches HeapAlloc with a jmp (not a call), so on entry the
        // stack still holds the user code's return address.
        void* ra = _ReturnAddress();

        InHookGuard guard;
        SourceId sid = resolveModule(ra);
        if (sid != kInvalidSourceId && s_trackerPtr)
        {
            s_trackerPtr->recordAlloc(sid, size, p);
        }
        return p;
    }

    BOOL WINAPI Hook_HeapFree(HANDLE heap, DWORD flags, LPVOID mem)
    {
        if (!mem || !s_hookEnabled.load(std::memory_order_acquire) || inHook())
            return Real_HeapFree(heap, flags, mem);
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::HeapHookActive))
            return Real_HeapFree(heap, flags, mem);

        // HeapSize is valid until the actual free; capture it first.
        SIZE_T size = ::HeapSize(heap, 0, mem);
        if (size == static_cast<SIZE_T>(-1)) size = 0;

        void* ra = _ReturnAddress();

        BOOL ok = Real_HeapFree(heap, flags, mem);
        if (!ok || size == 0) return ok;

        InHookGuard guard;
        // Note: we attribute the free to the *freer's* module, not the
        // *allocator's* module. In well-behaved code these match; cross-
        // module ownership transfers will produce per-module imbalance,
        // but the system-wide net is still accurate.
        SourceId sid = resolveModule(ra);
        if (sid != kInvalidSourceId && s_trackerPtr)
        {
            s_trackerPtr->recordFree(sid, size, mem);
        }
        return ok;
    }

    LPVOID WINAPI Hook_HeapReAlloc(HANDLE heap, DWORD flags, LPVOID mem, SIZE_T size)
    {
        // Capture old size BEFORE realloc may move the block.
        SIZE_T oldSize = mem ? ::HeapSize(heap, 0, mem) : 0;
        if (oldSize == static_cast<SIZE_T>(-1)) oldSize = 0;

        LPVOID p = Real_HeapReAlloc(heap, flags, mem, size);
        if (!p || !s_hookEnabled.load(std::memory_order_acquire) || inHook()) return p;
        if (s_trackerPtr &&
            !s_trackerPtr->isFeatureEnabled(FeatureFlag::HeapHookActive))
            return p;

        void* ra = _ReturnAddress();

        InHookGuard guard;
        SourceId sid = resolveModule(ra);
        if (sid != kInvalidSourceId && s_trackerPtr)
        {
            if (oldSize > 0) s_trackerPtr->recordFree(sid, oldSize, mem);
            s_trackerPtr->recordAlloc(sid, size, p);
        }
        return p;
    }

    std::atomic<bool> s_installed {false};
    std::mutex        s_installMutex;
} // anonymous namespace

bool installHeapHook()
{
    if (!kMemTrackEnabled || !kHeapHookEnabled) return false;   // see memory_tracker.h
    if (s_installed.load(std::memory_order_acquire)) return true;
    std::lock_guard<std::mutex> lk(s_installMutex);
    if (s_installed.load(std::memory_order_relaxed)) return true;

    // CRITICAL: force the Tracker singleton to FULLY construct BEFORE the
    // hook is live, then cache its address so hook callbacks never need to
    // call instance() (which would race with magic-static guard during init
    // and could return a partially-constructed s_instance with m_impl=nullptr,
    // dereferencing slots[15] -> AV at offset 0x78).
    s_trackerPtr = &Tracker::instance();
    (void)s_trackerPtr->getSourceCount();   // touch a method to confirm fully constructed

    // Allocate the TLS slot BEFORE installing the hook -- otherwise the very
    // first hook callback will see g_tlsIndex == TLS_OUT_OF_INDEXES and bail
    // out without recording. Windows zero-initializes the slot for every
    // existing and future thread, so inHook() returns false everywhere
    // until an InHookGuard sets it true.
    if (!initTls()) return false;

    // Detours requires the transaction model: begin -> attach* -> commit.
    LONG err = NO_ERROR;
    if ((err = DetourTransactionBegin())  != NO_ERROR) return false;
    if ((err = DetourUpdateThread(GetCurrentThread())) != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_HeapAlloc),   reinterpret_cast<PVOID>(Hook_HeapAlloc)))   != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_HeapReAlloc), reinterpret_cast<PVOID>(Hook_HeapReAlloc))) != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourAttach(reinterpret_cast<PVOID*>(&Real_HeapFree),    reinterpret_cast<PVOID>(Hook_HeapFree)))    != NO_ERROR) { DetourTransactionAbort(); return false; }
    if ((err = DetourTransactionCommit()) != NO_ERROR) return false;

    // Hooks are now live. Mark them enabled so callbacks proceed past the
    // early bail-out.
    s_hookEnabled.store(true, std::memory_order_release);
    s_installed.store(true, std::memory_order_release);
    return true;
}

void uninstallHeapHook()
{
    if (!s_installed.load(std::memory_order_acquire)) return;
    std::lock_guard<std::mutex> lk(s_installMutex);
    if (!s_installed.load(std::memory_order_relaxed)) return;

    // Disable callbacks BEFORE detaching: any in-flight Real_HeapAlloc on
    // another thread that's about to enter our wrapper logic will see
    // s_hookEnabled == false and bail to passthrough.
    s_hookEnabled.store(false, std::memory_order_release);

    DetourTransactionBegin();
    DetourUpdateThread(GetCurrentThread());
    DetourDetach(reinterpret_cast<PVOID*>(&Real_HeapAlloc),   reinterpret_cast<PVOID>(Hook_HeapAlloc));
    DetourDetach(reinterpret_cast<PVOID*>(&Real_HeapReAlloc), reinterpret_cast<PVOID>(Hook_HeapReAlloc));
    DetourDetach(reinterpret_cast<PVOID*>(&Real_HeapFree),    reinterpret_cast<PVOID>(Hook_HeapFree));
    DetourTransactionCommit();

    s_installed.store(false, std::memory_order_release);
}

bool isHeapHookInstalled()
{
    return s_installed.load(std::memory_order_acquire);
}

} // namespace MemTrack
} // namespace Chaos
