"""Parse one call stack into its allocator and business-caller frames.

WPA prints stacks root->leaf, bottoming out in the kernel. The real allocator is
near the leaf, so we walk leaf->root and skip OS plumbing + our own VA-hook frames.
"""
import re

# OS plumbing -- never the "owner".
SYSTEM_MODULES = {
    "ntdll.dll", "kernel32.dll", "kernelbase.dll", "ntoskrnl.exe",
    "wow64.dll", "wow64cpu.dll", "wow64win.dll", "win32u.dll",
}

# MemTrack's own VA/Nt hook frames, sitting between caller and kernel.
INSTRUMENTATION_MARKERS = (
    "MemTrack", "Hook_NtAllocateVirtualMemory", "Hook_VirtualAlloc",
    "Hook_VirtualFree", "Real_NtAllocateVirtualMemory",
)

# Stack went through the heap manager (CRT/mempool heap growth, not a direct
# reservation). Needs symbols -- never matches when symbols are disabled.
HEAP_MARKERS = (
    "RtlpAllocateHeap", "RtlAllocateHeap", "RtlpAllocateHeapInternal",
    "HeapAlloc", "_aligned_malloc", "_malloc_base", "malloc",
)

# Allocator / container / new glue between the kernel and the real business
# caller. Skipped (on top of system + instrumentation) to find which engine
# code wanted the memory. Substring match.
ALLOCATOR_MARKERS = (
    "Chaos::MemoryPool::", "Chaos::PoolDefault::", "DebugAllocator::",
    "MemoryPool::internal::AllocateHelper", "AllocatorWithPool", "::OnAllocate",
    "_malloc_base", "malloc", "realloc", "_aligned_malloc", "calloc",
    "operator new", "_callnewh", "std::_Default_allocate",
    "std::vector<", "std::basic_string", "std::_Tree", "std::_Hash",
    "std::deque", "::_Resize", "::_Reallocate", "::_Emplace", "::_Buynode",
    "::_Reserve", "::_Insert_hint",
)

# Allocation passed through the engine memory pool. In the Profile build the pool
# routes through DebugAllocator->_malloc_base->CRT heap, so a pool alloc is also
# a heap path; "non-pool heap" = is_heap_path AND NOT is_mempool_path.
MEMPOOL_MARKERS = (
    "chaos_mempool.dll!", "Chaos::MemoryPool::", "Chaos::PoolDefault",
    "Chaos::PoolBase", "DebugAllocator::",
)

_FRAME_RE = re.compile(r"([\w.\-]+\.(?:dll|exe))!", re.IGNORECASE)


def attribute(stack: str):
    """One leaf->root walk returning (alloc_mod, biz_mod, biz_frame):
      alloc_mod          deepest non-system/non-instrumentation module (View 1)
      biz_mod, biz_frame deepest frame that is also not allocator glue (View 2),
                         falling back to the allocator frame.
    All '<system>' if the stack has no usable frame."""
    alloc = None
    for frame in reversed(stack.split("/")):
        m = _FRAME_RE.search(frame)
        if not m:
            continue
        mod = m.group(1).lower()
        if mod in SYSTEM_MODULES:
            continue
        if any(k in frame for k in INSTRUMENTATION_MARKERS):
            continue
        if alloc is None:
            alloc = (mod, frame.strip())
        if any(k in frame for k in ALLOCATOR_MARKERS):
            continue
        return alloc[0], mod, frame.strip()
    if alloc is not None:          # every non-system frame was allocator glue
        return alloc[0], alloc[0], alloc[1]
    return "<system>", "<system>", "<system>"


def is_heap_path(stack: str) -> bool:
    return any(m in stack for m in HEAP_MARKERS)


def is_mempool_path(stack: str) -> bool:
    return any(m in stack for m in MEMPOOL_MARKERS)


def is_default_pool(stack: str) -> bool:
    """True if routed to the catch-all DefaultPool (vs a dedicated named pool)."""
    return "Chaos::PoolDefault" in stack


def business_chain(stack: str, max_frames: int = 16):
    """Ordered non-glue frames, allocation site first (leaf->root), with
    consecutive duplicates collapsed (recursion). chain[0] is the deepest
    business frame (== attribute()'s biz_frame); the rest are its callers.
    Used by View 4 to trace a generic leaf up to a meaningful owner."""
    out = []
    for frame in reversed(stack.split("/")):
        m = _FRAME_RE.search(frame)
        if not m:
            continue
        mod = m.group(1).lower()
        if mod in SYSTEM_MODULES:
            continue
        if any(k in frame for k in INSTRUMENTATION_MARKERS):
            continue
        if any(k in frame for k in ALLOCATOR_MARKERS):
            continue
        f = frame.strip()
        if out and out[-1] == f:          # collapse recursion (addNodes x N)
            continue
        out.append(f)
        if len(out) >= max_frames:
            break
    return tuple(out)
