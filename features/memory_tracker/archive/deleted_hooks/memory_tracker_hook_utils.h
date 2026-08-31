/*-------------------------------------------------------------------------
Copyright Notice
Copyright (c)  Booming Tech All rights reserved.
-------------------------------------------------------------------------*/
#pragma once

#include <Windows.h>

// Shared TLS re-entrance guard for Detours hook implementations.
//
// Each including TU gets its own TLS slot (g_tlsIndex is static at namespace
// scope). This is intentional: heap_hook and vmem_hook are independent Detours
// transactions; two separate TLS slots avoids any cross-hook interference at
// the cost of one extra TLS slot (~8 bytes per thread).
//
// Usage:
//   #include "memory_tracker_hook_utils.h"
//   using namespace Chaos::MemTrack::HookUtils;
//   // initTls() in install function, InHookGuard on stack in hook callbacks.

namespace Chaos
{
namespace MemTrack
{
namespace HookUtils
{
    static DWORD g_tlsIndex = TLS_OUT_OF_INDEXES;

    inline bool initTls()
    {
        if (g_tlsIndex == TLS_OUT_OF_INDEXES)
        {
            g_tlsIndex = ::TlsAlloc();
        }
        return g_tlsIndex != TLS_OUT_OF_INDEXES;
    }

    inline bool inHook()
    {
        if (g_tlsIndex == TLS_OUT_OF_INDEXES) return false;
        return ::TlsGetValue(g_tlsIndex) != nullptr;
    }

    inline void setInHook(bool v)
    {
        if (g_tlsIndex == TLS_OUT_OF_INDEXES) return;
        ::TlsSetValue(g_tlsIndex, v ? reinterpret_cast<LPVOID>(1) : nullptr);
    }

    // RAII helper: marks the current thread "inside hook" for the scope duration,
    // restoring the prior state on destruction. Nesting is safe — the dtor
    // restores the outer scope's value.
    struct InHookGuard
    {
        bool prev;
        InHookGuard()  : prev(inHook()) { setInHook(true); }
        ~InHookGuard() { setInHook(prev); }
    };

} // namespace HookUtils
} // namespace MemTrack
} // namespace Chaos
