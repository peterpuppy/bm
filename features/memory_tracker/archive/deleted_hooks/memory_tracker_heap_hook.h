/*-------------------------------------------------------------------------
Copyright Notice
Copyright (c)  Booming Tech All rights reserved.
-------------------------------------------------------------------------*/
#pragma once

#include "chaos/core/macro.h"

namespace Chaos
{
namespace MemTrack
{
    // Detours-based hook for kernel32!HeapAlloc / HeapReAlloc / HeapFree.
    //
    // What it does
    // ============
    // For every HeapAlloc-family call, we capture the immediate caller's
    // return address, look up which loaded module contains that RA, and
    // route the bytes into a per-module Tracker Counter source named
    //   HeapAllocFrom_<basename>      e.g. "HeapAllocFrom_chaos_client.dll"
    //
    // This breaks down CRTHeap_BusyAllHeaps (the total HeapAlloc world) into
    // per-module attribution so we can answer "which dll is using the
    // CRT heap memory". STL-via-default-allocator instances all show up
    // under the dll that *instantiated* the template (since STL is inline,
    // there's no STL dll to attribute to).
    //
    // Why this works alongside Pool/CRTHeap
    // =====================================
    // - chaos mempool calls ::VirtualAlloc directly, not HeapAlloc -- so
    //   none of Pool/* shows up here. No double counting.
    // - All HeapAllocFrom_* counters together should ~= CRTHeap_BusyAllHeaps
    //   (modulo timing skew between the periodic HeapWalk and the live
    //   counters).
    //
    // Performance notes
    // =================
    // - Each HeapAlloc adds ~1us of overhead (RA capture + module cache
    //   lookup + atomic add). On a tick spent doing 100k allocs that's
    //   ~100ms, which is significant. Acceptable for diagnosis runs;
    //   should be turned off in shipping builds.
    // - Re-entrance is handled with a thread_local flag so allocations
    //   made by the hook itself (e.g. registerSource on a new module)
    //   don't recurse.
    //
    // Lifecycle
    // =========
    // Call install() once after Tracker is initialized; uninstall() before
    // shutdown is optional (process exit reclaims everything).
    CORE_API bool installHeapHook();
    CORE_API void uninstallHeapHook();
    CORE_API bool isHeapHookInstalled();

    // Source-name prefix used by the heap hook. dump segments by this prefix
    // to display per-module breakdown under the CRT Heap section.
    constexpr const char* kHeapAllocSourcePrefix = "HeapAllocFrom_";

} // namespace MemTrack
} // namespace Chaos
