/*-------------------------------------------------------------------------
Copyright Notice
Copyright (c)  Booming Tech All rights reserved.
-------------------------------------------------------------------------*/
#pragma once

#include "chaos/core/macro.h"

#include <cstdint>

namespace Chaos
{
namespace MemTrack
{
    using SourceId = std::uint32_t;  // matches memory_tracker.h
    // Detours-based hook for kernel32!VirtualAlloc / VirtualFree.
    //
    // What it does
    // ============
    // Captures every direct VirtualAlloc-family call and routes the bytes
    // into per-module Tracker Counter sources named:
    //   VirtualAllocFrom_<basename>     e.g. "VirtualAllocFrom_xenon_client.exe"
    //
    // This complements the HeapAlloc hook: HeapAlloc world covers default-
    // process-heap allocations (most STL, mempool's DebugAllocator route,
    // Wwise default malloc). VirtualAlloc world covers everything that
    // skips the heap manager and calls VirtualAlloc directly -- typically
    // V8 isolate heap, DirectX driver shadow buffers, Wwise streaming
    // ring buffers, and some third-party SDKs.
    //
    // Together they account for ~95%+ of process-private commit, leaving
    // only thread stacks + OS-managed page bookkeeping (~100 MB) as the
    // structural blind spot.
    //
    // Capture semantics
    // =================
    // We record alloc on MEM_RESERVE only (commits are subsets of an
    // already-reserved region; counting both would double up). VirtualFree
    // with MEM_RELEASE retires the entire reservation; MEM_DECOMMIT is
    // ignored (it doesn't release the address-space reservation).
    //
    // Because VirtualFree's size argument is 0 on MEM_RELEASE, we maintain
    // a small ptr->size lock-free hash table populated by VirtualAlloc.
    // Lookups that miss fall back to VirtualQuery on the address.
    //
    // Performance
    // ===========
    // VirtualAlloc is called orders of magnitude less than HeapAlloc
    // (game-thread VirtualAlloc rate is < 1 kHz typically), so even
    // unconditionally walking a hash table per call is cheap.
    //
    // Master switch: FeatureFlag::VirtualAllocHookActive (default ON), queried
    // per call from the cached Tracker pointer.
    CORE_API bool installVMemHook();
    CORE_API void uninstallVMemHook();
    CORE_API bool isVMemHookInstalled();

    // Source-name prefixes used by the VirtualAlloc hook. Two separate
    // dimensions are recorded:
    //
    //   VirtualAllocReserveFrom_<dll>  -- bytes reserved (address space)
    //                                     V8's 4 GB sandbox shows here. Not
    //                                     consumed memory; informational.
    //
    //   VirtualAllocCommitFrom_<dll>   -- bytes committed (real RAM/page-file)
    //                                     This *is* part of ProcessCommit.
    //                                     Used in Tracked / Coverage math.
    constexpr const char* kVMemReserveSourcePrefix = "VirtualAllocReserveFrom_";
    constexpr const char* kVMemCommitSourcePrefix  = "VirtualAllocCommitFrom_";

} // namespace MemTrack
} // namespace Chaos
