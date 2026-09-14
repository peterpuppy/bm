# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/slvrwlockrdlockdestroyed.html

# Exception Reason Codes

## System Software and Compiler Runtime (SYSTEM)

## CPU Exceptions

## GPU exceptions

## AMM exceptions

## APR Exceptions

## Dynamic Libraries (PRX)

# PRX\_RUNTIME\_ERROR

Fatal error of the dynamic library runtime

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_PRX_RUNTIME_ERROR       0xa0020103
```

## Description

This exception reason code is signaled when a fatal error occurs in the system software's dynamic library runtime and the process has to be terminated. Additional information may be output to the process TTY.

If a fatal error occurs for a thread creation or a PRX/main module load, there may not be enough memory for allocating the memory area declared to the PRX/main module that is being loaded.

# PRX\_SCE\_MODULE\_LOAD\_ERROR

Failure to load PRX in sce\_module

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_PRX_SCE_MODULE_LOAD_ERROR       0xa0020102
```

## Description

This exception reason code is signaled when loading of libc.prx (PRX of the C and C++ standard libraries) from the /app0/sce\_module directory fails.

The loading of libc.prx fails due to one of the following reasons:

1. /app0/sce\_module/libc.prx does not exist
2. /app0/sce\_module/libc.prx exists, but there is a problem with the file format (including when the libc.prx placed in the directory is not for PlayStation®5)
3. /app0/sce\_module/libc.prx exists, but the libc.prx placed in the directory is included in an SDK whose version differs from the SDK that was used to build the program
4. Mirroring of libc.prx failed when using a workspace (For information about workspaces, refer to [Workspaces Overview](../Workspaces-Overview/__document_toc.html))

In the cases of [1](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_zfz_5lt_42c), [2](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_dyh_vlt_42c), and [3](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_twq_vlt_42c), the problem can be resolved by copying the target/sce\_module/libc.prx that is included in the SDK used to build the program to /app0/sce\_module.

This exception occurs when a library required for process start by the system fails to load. SDK library calls by the application cannot cause this exception to occur. Therefore, when explicitly loading a PRX in sce\_module with `sceSysmoduleLoadModule()`, this exception will not occur due to load failure.

## Notes

The occurrence of this exception can be avoided during development by using one of the following debug settings.

* Set "★Debug Settings" > "System" > "Use Default PRX Runtime Library" to "On":

  effective for all the above cases [1](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_zfz_5lt_42c), [2](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_dyh_vlt_42c), [3](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_twq_vlt_42c), and [4](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_mgl_2mt_42c).
* Set "★Debug Settings" > "System" > "Ignore PRX SDK Version Check" to "On":

  effective for the above case [3](prxscemoduleloaderror.html#kernel-reference_19_6_5__li_twq_vlt_42c).

For details about these debug settings, refer to [Sysmodule Library Overview - Package Installation - PRX File Placement During Development](../Sysmodule-Overview/ps5-prx-file-placement-during-development.html) and [Sysmodule Library Overview - Package Installation - Version Checking PRX Files](../Sysmodule-Overview/ps5-version-checking-prx-files.html).

# PRX\_TLS\_ALLOC\_ERROR

Failure to allocate TLS area

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_PRX_TLS_ALLOC_ERROR       0xa0020106
```

## Description

This exception reason code is signaled when a dynamic library runtime failed to allocate a TLS area. Additional information may be output to the process TTY.

## Notes

* This exception will also be signaled for failure to allocate a main module TLS area.
* When replacing the memory management functions of the C/C++ standard libraries, this exception will also be signaled if the start address of the TLS area allocated by the replaced function is not aligned to 32 bytes or more. For details, refer to `user_malloc_for_tls()` of [Memory Management Function Replacements of the C and C++ Standard Libraries: Reference](../Malloc_Replace-Reference/__document_toc.html).
* Because TLS is used internally in the C++ runtime, this exception may also be signaled for failure to allocate a non-TLS area.

## Standard Libraries (LIBC)

# LIBC\_ABORT

Termination due to `abort()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_ABORT       0xa002000b
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `abort()` function.

# LIBC\_ASSERT

`assert()` failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_ASSERT       0xa0020007
```

## Description

This exception reason code is signaled when a process terminates due to an `assert()` macro failure.

# LIBC\_EXIT\_FAIL

Termination due to `exit()` (non-0)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_EXIT_FAIL       0xa0020004
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `exit()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_FAIL` suffix indicates that a non-0 value was passed to `exit()`. When attempting to terminate with a 0 value, `LIBC_EXIT_SUCCESS` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_EXIT\_SUCCESS

Termination due to `exit()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_EXIT_SUCCESS       0xa0020003
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `exit()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_SUCCESS` suffix indicates that a 0 value was passed to `exit()`. When attempting to terminate with a non-0 value, `LIBC_EXIT_FAIL` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_FAILED\_TO\_CREATE\_HEAP

Standard library heap creation failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_FAILED_TO_CREATE_HEAP       0xa002000e
```

## Description

This exception reason code is signaled when standard heap creation fails.

Check the `sceLibcHeapSize` setting value. For the setting of `sceLibcHeapSize`, refer to the explanation on `malloc()` in the [C and C++ Standard Libraries: Overview and Reference](../C_and_Cpp_standard_libraries/__document_toc.html) document.

# LIBC\_FAILED\_TO\_MALLOC\_INIT

Memory management function initialization failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_FAILED_TO_MALLOC_INIT       0xa0020013
```

## Description

This exception reason code is signaled when standard library memory management function initialization fails.

If memory management function replacement was performed, make sure that initialization has terminated normally.

# LIBC\_FAILED\_TO\_REPLACE\_MALLOC

C memory management function replacement failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_FAILED_TO_REPLACE_MALLOC       0xa0020010
```

## Description

This exception reason code is signaled when C memory management function replacement fails.

Confirm that all functions required for replacement are linked.

# LIBC\_FAILED\_TO\_REPLACE\_NEW

C++ memory management function replacement failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_FAILED_TO_REPLACE_NEW       0xa0020011
```

## Description

This exception reason code is signaled when C++ memory management function replacement fails.

Confirm that all functions required for replacement are linked.

# LIBC\_FAILED\_TO\_REPLACE\_TLS\_MALLOC

TLS memory management function replacement failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_FAILED_TO_REPLACE_TLS_MALLOC       0xa0020012
```

## Description

This exception reason code is signaled when TLS memory management function replacement fails.

Confirm that all functions required for replacement are linked.

# LIBC\_FAILED\_TO\_TLS\_MALLOC\_INIT

TLS memory management function initialization failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_FAILED_TO_TLS_MALLOC_INIT       0xa0020014
```

## Description

This exception reason code is signaled when initialization of a replaced TLS memory management function fails.

# LIBC\_INTERNAL\_\*

SDK library internal errors

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_RETURN_MAIN_SUCCESS       0xa0020081
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_RETURN_MAIN_FAIL       0xa0020082
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_EXIT_SUCCESS       0xa0020083
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_EXIT_FAIL       0xa0020084
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL__EXIT_SUCCESS       0xa0020085
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL__EXIT_FAIL       0xa0020086
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_ASSERT       0xa0020087
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_TERMINATE       0xa0020088
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_UNEXPECTED       0xa0020089
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_PURE_VIRTUAL       0xa002008a
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_ABORT       0xa002008b
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_QUICK_EXIT_SUCCESS       0xa002008c
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_QUICK_EXIT_FAIL       0xa002008d
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_FAILED_TO_CREATE_SYSTEM_MEMORY       0xa002008f
#define SCE_KERNEL_STOP_CODE_LIBC_INTERNAL_CONSTRAINT_HANDLER       0xa0020095
```

## Description

`LIBC_INTERNAL_*` exception reason codes indicate SDK library internal errors.

Note that some functions provided in SDK libraries omit argument checks for improved efficiency; therefore, there is a possibility of internal errors occurring when an invalid argument is assigned. In addition, internal errors may occur due to reasons such as heap corruption.

SDK libraries may output additional information to the TTY immediately before process termination due to an internal error.

## Notes

The exceptions that occur are subsets of standard library exceptions. For example, `LIBC_INTERNAL_ABORT` indicates that an SDK library attempted to terminate a process with `abort()` and is equivalent to `LIBC_ABORT`.

# LIBC\_PURE\_VIRTUAL

Pure virtual function call

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_PURE_VIRTUAL       0xa002000a
```

## Description

This exception reason code is signaled when a pure virtual function call is detected and a process terminates.

# LIBC\_QUICK\_EXIT\_FAIL

Termination due to `quick_exit()` (non-0)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_QUICK_EXIT_FAIL       0xa002000d
```

## Description

This exception reason code is signaled when attempting to terminate a process with a `quick_exit()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_FAIL` suffix indicates that a non-0 value was passed to `quick_exit()`. When attempting to terminate with a 0 value, `LIBC_QUICK_EXIT_SUCCESS` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_QUICK\_EXIT\_SUCCESS

Termination due to `quick_exit()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_QUICK_EXIT_SUCCESS       0xa002000c
```

## Description

This exception reason code is signaled when attempting to terminate a process with a `quick_exit()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_SUCCESS` suffix indicates that a 0 value was passed to `quick_exit()`. When attempting to terminate with a non-0 value, `LIBC_QUICK_EXIT_FAIL` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_RETURN\_MAIN\_FAIL

Termination due to return from `main()` (non-0)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_RETURN_MAIN_FAIL       0xa0020002
```

## Description

This exception reason code is signaled when attempting to terminate a process with a return from a `main()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_FAIL` suffix indicates that termination is attempted with `main()` by returning a non-0 value. When attempting to terminate with a 0 value, `LIBC_RETURN_MAIN_SUCCESS` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_RETURN\_MAIN\_SUCCESS

Termination due to return from `main()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_RETURN_MAIN_SUCCESS       0xa0020001
```

## Description

This exception reason code is signaled when attempting to terminate a process with a return from a `main()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_SUCCESS` suffix indicates that termination is attempted with `main()` by returning a 0 value. When attempting to terminate with a non-0 value, `LIBC_RETURN_MAIN_FAIL` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_TERMINATE

Termination due to `terminate()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_TERMINATE       0xa0020008
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `std::terminate()` function.

# LIBC\_UNEXPECTED

Termination due to `unexpected()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC_UNEXPECTED       0xa0020009
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `std::unexpected()` function.

# LIBC\_\_EXIT\_FAIL

Termination due to `_Exit()` (non-0)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC__EXIT_FAIL       0xa0020006
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `_Exit()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_FAIL` suffix indicates that a non-0 value was passed to `_Exit()`. When attempting to terminate with a 0 value, `LIBC__EXIT_SUCCESS` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# LIBC\_\_EXIT\_SUCCESS

Termination due to `_Exit()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_LIBC__EXIT_SUCCESS       0xa0020005
```

## Description

This exception reason code is signaled when attempting to terminate a process with an `_Exit()` function. When the Release Check Mode is set to Development Mode or Assist Mode, the process will terminate without an exception being signaled.

The `_SUCCESS` suffix indicates that a 0 value was passed to `_Exit()`. When attempting to terminate with a non-0 value, `LIBC__EXIT_FAIL` will be signaled.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

## SLV (System Library Verification) Exceptions

# SLV\_BARRIER\_DESTROY\_DESTROYED

`scePthreadBarrierDestroy()`: Destruction of a destroyed barrier

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_BARRIER_DESTROY_DESTROYED       0xa0ff832e
```

## Description

This exception reason code is signaled when `scePthreadBarrierDestroy()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the barrier specified for `scePthreadBarrierDestroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_BARRIER\_DESTROY\_IN\_USE

`scePthreadBarrierDestroy()`: Destruction of a barrier being used by some thread

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_BARRIER_DESTROY_IN_USE       0xa0ff8330
```

## Description

This exception reason code is signaled when `scePthreadBarrierDestroy()` returns the `SCE_KERNEL_ERROR_EBUSY` error in a state where the SLV for the process is enabled and set to "Abort".

The barrier specified for `scePthreadBarrierDestroy()` is currently being used by some thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_BARRIER\_WAIT\_DESTROYED

`scePthreadBarrierWait()`: Wait for a destroyed barrier

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_BARRIER_WAIT_DESTROYED       0xa0ff8332
```

## Description

This exception reason code is signaled when `scePthreadBarrierWait()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the barrier specified for `scePthreadBarrierWait()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_CLOSE\_NOT\_PERMITTED\_FD

`sceKernelClose()`: Closing of an unpermitted file descriptor

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_CLOSE_NOT_PERMITTED_FD       0xa0ff8307
```

## Description

This exception reason code is signaled when `sceKernelClose()` returns the `SCE_KERNEL_ERROR_EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

## Notes

Closing `stdin(0)`, `stdout(1)`, or `stderr(2)` is prohibited for applications.

# SLV\_COND\_BROADCAST\_DESTROYED

`scePthreadCondBroadcast()`: Broadcast to a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_BROADCAST_DESTROYED       0xa0ff8310
```

## Description

This exception reason code is signaled when `scePthreadCondBroadcast()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `scePthreadCondBroadcast()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_COND\_DESTROY\_DESTROYED

`scePthreadCondDestroy()`: Destruction of a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_DESTROY_DESTROYED       0xa0ff8312
```

## Description

This exception reason code is signaled when `scePthreadCondDestroy()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `scePthreadCondDestroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_COND\_SIGNALTO\_DESTROYED

`scePthreadCondSignalto()`: Signal to a destroyed condition variable (specified thread)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_SIGNALTO_DESTROYED       0xa0ff8316
```

## Description

This exception reason code is signaled when `scePthreadCondSignalto()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `scePthreadCondSignalto()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_COND\_SIGNAL\_DESTROYED

`scePthreadCondSignal()`: Signal to a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_SIGNAL_DESTROYED       0xa0ff8314
```

## Description

This exception reason code is signaled when `scePthreadCondSignal()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `scePthreadCondSignal()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_COND\_TIMEDWAIT\_DESTROYED

`scePthreadCondTimedwait()`: Wait for a destroyed condition variable (with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_TIMEDWAIT_DESTROYED       0xa0ff8317
```

## Description

This exception reason code is signaled when `scePthreadCondTimedwait()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `scePthreadCondTimedwait()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_COND\_TIMEDWAIT\_MUTEX\_NOT\_OWNED

`scePthreadCondTimedwait()`: Wait for a condition variable with a mutex that is not locked by the calling thread specified (with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_TIMEDWAIT_MUTEX_NOT_OWNED       0xa0ff8318
```

## Description

This exception reason code is signaled when `scePthreadCondTimedwait()` returns the `SCE_KERNEL_ERROR_EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `scePthreadCondTimedwait()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_COND\_WAIT\_DESTROYED

`scePthreadCondWait()`: Wait for a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_WAIT_DESTROYED       0xa0ff831a
```

## Description

This exception reason code is signaled when `scePthreadCondWait()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `scePthreadCondWait()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_COND\_WAIT\_MUTEX\_NOT\_OWNED

`scePthreadCondWait()`:Wait for a condition variable with a mutex that is not locked by the calling thread specified

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_COND_WAIT_MUTEX_NOT_OWNED       0xa0ff831c
```

## Description

This exception reason code is signaled when `scePthreadCondWait()` returns the `SCE_KERNEL_ERROR_EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `scePthreadCondWait()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_CREATE\_THREAD\_NO\_RESOURCE

`scePthreadCreate()`: Failed to create thread because of insufficient resources

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_CREATE_THREAD_NO_RESOURCE       0xa0ff8338
```

## Description

This exception reason code is signaled when `scePthreadCreate()` returns the error `SCE_KERNEL_ERROR_EAGAIN` in a state where the SLV for the process is enabled and set to "Abort".

This exception is signaled when the ceiling for memory resources allocated in the thread runtime library has been reached and an attempt is made to create another thread. A typical case in which this exception occurs is when `scePthreadJoin()` is not called and numerous threads with uncollected resources exist within a process.

The maximum amount of thread resources that can be in any one process is enough for 512 threads.

# SLV\_MUTEX\_DESTROY\_DESTROYED

`scePthreadMutexDestroy()`: Destruction of a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_DESTROY_DESTROYED       0xa0ff8309
```

## Description

This exception reason code is signaled when `scePthreadMutexDestroy()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `scePthreadMutexDestroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_MUTEX\_DESTROY\_LOCKED

`scePthreadMutexDestroy()`: Destruction of a locked mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_DESTROY_LOCKED       0xa0ff8303
```

## Description

This exception reason code is signaled when `scePthreadMutexDestroy()` returns the `SCE_KERNEL_ERROR_EBUSY` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `scePthreadMutexDestroy()` is locked by some thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_MUTEX\_LOCK\_DESTROYED

`scePthreadMutexLock()`: Locking of a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_LOCK_DESTROYED       0xa0ff8305
```

## Description

This exception reason code is signaled when `scePthreadMutexLock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `scePthreadMutexLock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

When the specified mutex has a priority protection attribute, this exception will also be signaled when the priority value of the calling thread is higher than the ceiling value.

# SLV\_MUTEX\_TIMEDLOCK\_DESTROYED

`scePthreadMutexTimedlock()`: Locking of a destroyed mutex (with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_TIMEDLOCK_DESTROYED       0xa0ff830b
```

## Description

This exception reason code is signaled when `scePthreadMutexTimedlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `scePthreadMutexTimedlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

When the specified mutex has a priority protection attribute, this exception will also be signaled when the priority value of the calling thread is higher than the ceiling value.

# SLV\_MUTEX\_TRYLOCK\_DESTROYED

`scePthreadMutexTrylock()`: Attempting to lock a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_TRYLOCK_DESTROYED       0xa0ff830c
```

## Description

This exception reason code is signaled when `scePthreadMutexTrylock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `scePthreadMutexTrylock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

When the specified mutex has a priority protection attribute, this exception will also be signaled when the priority value of the calling thread is higher than the ceiling value.

# SLV\_MUTEX\_UNLOCK\_DESTROYED

`scePthreadMutexUnlock()`: Unlocking of a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_UNLOCK_DESTROYED       0xa0ff830e
```

## Description

This exception reason code is signaled when `scePthreadMutexUnlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `scePthreadMutexUnlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_MUTEX\_UNLOCK\_NOT\_OWNED

`scePthreadMutexUnlock()`: Unlocking of a mutex that is not locked by the calling thread

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_MUTEX_UNLOCK_NOT_OWNED       0xa0ff8301
```

## Description

This exception reason code is signaled when `scePthreadMutexUnlock()` returns the `SCE_KERNEL_ERROR_EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `scePthreadMutexUnlock()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_BARRIER\_DESTROY\_DESTROYED

`pthread_barrier_destroy()`: Destruction of a destroyed barrier

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_BARRIER_DESTROY_DESTROYED       0xa0ff832f
```

## Description

This exception reason code is signaled when `pthread_barrier_destroy()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the barrier specified for `pthread_barrier_destroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_POSIX\_BARRIER\_DESTROY\_IN\_USE

`pthread_barrier_destroy()`: Destruction of a barrier being used by some thread

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_BARRIER_DESTROY_IN_USE       0xa0ff8331
```

## Description

This exception reason code is signaled when `pthread_barrier_destroy()` returns the `EBUSY` error in a state where the SLV for the process is enabled and set to "Abort".

The barrier specified for `pthread_barrier_destroy()` is currently being used by some thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_BARRIER\_WAIT\_DESTROYED

`pthread_barrier_wait()`: Wait for a destroyed barrier

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_BARRIER_WAIT_DESTROYED       0xa0ff8333
```

## Description

This exception reason code is signaled when `pthread_barrier_wait()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the barrier specified for `pthread_barrier_wait()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_CLOSE\_NOT\_PERMITTED\_FD

`close()`: Closing of an unpermitted file descriptor

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_CLOSE_NOT_PERMITTED_FD       0xa0ff8308
```

## Description

This exception reason code is signaled when `close()` returns the `EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

## Notes

Closing `stdin(0)`, `stdout(1)`, or `stderr(2)` is prohibited for applications.

# SLV\_POSIX\_COND\_BROADCAST\_DESTROYED

`pthread_cond_broadcast()`: Broadcast to a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_BROADCAST_DESTROYED       0xa0ff8311
```

## Description

This exception reason code is signaled when `pthread_cond_broadcast()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `pthread_cond_broadcast()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_COND\_DESTROY\_DESTROYED

`pthread_cond_destroy()`: Destruction of a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_DESTROY_DESTROYED       0xa0ff8313
```

## Description

This exception reason code is signaled when `pthread_cond_destroy()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `pthread_cond_destroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_POSIX\_COND\_SIGNAL\_DESTROYED

`pthread_cond_signal()`: Signal to a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_SIGNAL_DESTROYED       0xa0ff8315
```

## Description

This exception reason code is signaled when `pthread_cond_signal()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `pthread_cond_signal()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_COND\_TIMEDWAIT\_DESTROYED

`pthread_cond_timedwait()`: Wait for a destroyed condition variable (with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_TIMEDWAIT_DESTROYED       0xa0ff8335
```

## Description

This exception reason code is signaled when `pthread_cond_timedwait()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `pthread_cond_timedwait()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

This exception is also signaled when an invalid timeout time is specified.

# SLV\_POSIX\_COND\_TIMEDWAIT\_MUTEX\_NOT\_OWNED

`pthread_cond_timedwait()`: Wait for a condition variable with a mutex that is not locked by the calling thread specified (with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_TIMEDWAIT_MUTEX_NOT_OWNED       0xa0ff8319
```

## Description

This exception reason code is signaled when `pthread_cond_timedwait()` returns the `EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `pthread_cond_timedwait()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_COND\_WAIT\_DESTROYED

`pthread_cond_wait()`: Wait for a destroyed condition variable

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_WAIT_DESTROYED       0xa0ff831b
```

## Description

This exception reason code is signaled when `pthread_cond_wait()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the condition variable specified for `pthread_cond_wait()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_COND\_WAIT\_MUTEX\_NOT\_OWNED

`pthread_cond_wait()`:Wait for a condition variable with a mutex that is not locked by the calling thread specified

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_COND_WAIT_MUTEX_NOT_OWNED       0xa0ff831d
```

## Description

This exception reason code is signaled when `pthread_cond_wait()` returns the `EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `pthread_cond_wait()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_CREATE\_THREAD\_NO\_RESOURCE

`pthread_create()`: Failed to create thread because of insufficient resources

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_CREATE_THREAD_NO_RESOURCE       0xa0ff8339
```

## Description

This exception reason code is signaled when `pthread_create()` returns the error `EAGAIN` in a state where the SLV for the process is enabled and set to "Abort".

This exception is signaled when the ceiling for memory resources allocated in the thread runtime library has been reached and an attempt is made to create another thread. A typical case in which this exception occurs is when `pthread_join()` is not called and numerous threads with uncollected resources exist within a process.

The maximum amount of thread resources that can be in any one process is enough for 512 threads.

# SLV\_POSIX\_MUTEX\_DESTROY\_DESTROYED

`pthread_mutex_destroy()`: Destruction of a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_DESTROY_DESTROYED       0xa0ff830a
```

## Description

This exception reason code is signaled when `pthread_mutex_destroy()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `pthread_mutex_destroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_POSIX\_MUTEX\_DESTROY\_LOCKED

`pthread_mutex_destroy()`: Destruction of a locked mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_DESTROY_LOCKED       0xa0ff8304
```

## Description

This exception reason code is signaled when `pthread_mutex_destroy()` returns the `EBUSY` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `pthread_mutex_destroy()` is locked by some thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_MUTEX\_LOCK\_DESTROYED

`pthread_mutex_lock()`: Locking of a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_LOCK_DESTROYED       0xa0ff8306
```

## Description

This exception reason code is signaled when `pthread_mutex_lock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `pthread_mutex_lock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

When the specified mutex has a priority protection attribute, this exception will also be signaled when the priority value of the calling thread is higher than the ceiling value.

# SLV\_POSIX\_MUTEX\_TIMEDLOCK\_DESTROYED

`pthread_mutex_timedlock()`: Locking of a destroyed mutex (with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_TIMEDLOCK_DESTROYED       0xa0ff8334
```

## Description

This exception reason code is signaled when `pthread_mutex_timedlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `pthread_mutex_timedlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

This exception is also signaled when an invalid timeout time is specified.

# SLV\_POSIX\_MUTEX\_TRYLOCK\_DESTROYED

`pthread_mutex_trylock()`: Attempting to lock a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_TRYLOCK_DESTROYED       0xa0ff830d
```

## Description

This exception reason code is signaled when `pthread_mutex_trylock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `pthread_mutex_trylock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

When the specified mutex has a priority protection attribute, this exception will also be signaled when the priority value of the calling thread is higher than the ceiling value.

# SLV\_POSIX\_MUTEX\_UNLOCK\_DESTROYED

`pthread_mutex_unlock()`: Unlocking of a destroyed mutex

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_UNLOCK_DESTROYED       0xa0ff830f
```

## Description

This exception reason code is signaled when `pthread_mutex_unlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the mutex specified for `pthread_mutex_unlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_MUTEX\_UNLOCK\_NOT\_OWNED

`pthread_mutex_unlock()`: Unlocking of a mutex that is not locked by the calling thread

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_MUTEX_UNLOCK_NOT_OWNED       0xa0ff8302
```

## Description

This exception reason code is signaled when `pthread_mutex_unlock()` returns the `EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The mutex specified for `pthread_mutex_unlock()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_RWLOCK\_DESTROY\_DESTROYED

`pthread_rwlock_destroy()`: Destruction of a destroyed reader/writer lock

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_DESTROY_DESTROYED       0xa0ff831f
```

## Description

This exception reason code is signaled when `pthread_rwlock_destroy()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_destroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_POSIX\_RWLOCK\_RDLOCK\_DESTROYED

`pthread_rwlock_rdlock()`: Locking of a destroyed reader/writer lock (for reading)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_RDLOCK_DESTROYED       0xa0ff8321
```

## Description

This exception reason code is signaled when `pthread_rwlock_rdlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_rdlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_RWLOCK\_TIMEDRDLOCK\_DESTROYED

`pthread_rwlock_timedrdlock()`: Locking of a destroyed reader/writer lock (for reading, with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_TIMEDRDLOCK_DESTROYED       0xa0ff8336
```

## Description

This exception reason code is signaled when `pthread_rwlock_timedrdlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_timedrdlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

This exception is also signaled when an invalid timeout time is specified.

# SLV\_POSIX\_RWLOCK\_TIMEDWRLOCK\_DESTROYED

`pthread_rwlock_timedwrlock()`: Locking of a destroyed reader/writer lock (for writing, with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_TIMEDWRLOCK_DESTROYED       0xa0ff8337
```

## Description

This exception reason code is signaled when `pthread_rwlock_timedwrlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_timedwrlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Notes

This exception is also signaled when an invalid timeout time is specified.

# SLV\_POSIX\_RWLOCK\_TRYRDLOCK\_DESTROYED

`pthread_rwlock_tryrdlock()`: Attempting to lock a destroyed reader/writer lock (for reading)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_TRYRDLOCK_DESTROYED       0xa0ff8325
```

## Description

This exception reason code is signaled when `pthread_rwlock_tryrdlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_tryrdlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_RWLOCK\_TRYWRLOCK\_DESTROYED

`pthread_rwlock_trywrlock()`: Attempting to lock a destroyed reader/writer lock (for writing)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_TRYWRLOCK_DESTROYED       0xa0ff8327
```

## Description

This exception reason code is signaled when `pthread_rwlock_trywrlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_trywrlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_RWLOCK\_UNLOCK\_DESTROYED

`pthread_rwlock_unlock()`: Unlocking of a destroyed reader/writer lock

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_UNLOCK_DESTROYED       0xa0ff8329
```

## Description

This exception reason code is signaled when `pthread_rwlock_unlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_unlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_RWLOCK\_UNLOCK\_NOT\_OWNED

`pthread_rwlock_unlock()`: Unlocking of a reader/writer lock that is not locked by the calling thread

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_UNLOCK_NOT_OWNED       0xa0ff832b
```

## Description

This exception reason code is signaled when `pthread_rwlock_unlock()` returns the `EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The reader/writer lock specified for `pthread_rwlock_unlock()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_POSIX\_RWLOCK\_WRLOCK\_DESTROYED

`pthread_rwlock_wrlock()`: Locking of a destroyed reader/writer lock (for writing)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_POSIX_RWLOCK_WRLOCK_DESTROYED       0xa0ff832d
```

## Description

This exception reason code is signaled when `pthread_rwlock_wrlock()` returns the `EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `pthread_rwlock_wrlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_DESTROY\_DESTROYED

`scePthreadRwlockDestroy()`: Destruction of a destroyed reader/writer lock

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_DESTROY_DESTROYED       0xa0ff831e
```

## Description

This exception reason code is signaled when `scePthreadRwlockDestroy()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockDestroy()` has already been discarded or destroyed. At such times, there is a possibility that the application redundantly destroys resources.

# SLV\_RWLOCK\_RDLOCK\_DESTROYED

`scePthreadRwlockRdlock()`: Locking of a destroyed reader/writer lock (for reading)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_RDLOCK_DESTROYED       0xa0ff8320
```

## Description

This exception reason code is signaled when `scePthreadRwlockRdlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockRdlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_TIMEDRDLOCK\_DESTROYED

`scePthreadRwlockTimedrdlock()`: Locking of a destroyed reader/writer lock (for reading, with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_TIMEDRDLOCK_DESTROYED       0xa0ff8322
```

## Description

This exception reason code is signaled when `scePthreadRwlockTimedrdlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockTimedrdlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_TIMEDWRLOCK\_DESTROYED

`scePthreadRwlockTimedwrlock()`: Locking of a destroyed reader/writer lock (for writing, with timeout)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_TIMEDWRLOCK_DESTROYED       0xa0ff8323
```

## Description

This exception reason code is signaled when `scePthreadRwlockTimedwrlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockTimedwrlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_TRYRDLOCK\_DESTROYED

`scePthreadRwlockTryrdlock()`: Attempting to lock a destroyed reader/writer lock (for reading)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_TRYRDLOCK_DESTROYED       0xa0ff8324
```

## Description

This exception reason code is signaled when `scePthreadRwlockTryrdlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockTryrdlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_TRYWRLOCK\_DESTROYED

`scePthreadRwlockTrywrlock()`: Attempting to lock a destroyed reader/writer lock (for writing)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_TRYWRLOCK_DESTROYED       0xa0ff8326
```

## Description

This exception reason code is signaled when `scePthreadRwlockTrywrlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockTrywrlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_UNLOCK\_DESTROYED

`scePthreadRwlockUnlock()`: Unlocking of a destroyed reader/writer lock

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_UNLOCK_DESTROYED       0xa0ff8328
```

## Description

This exception reason code is signaled when `scePthreadRwlockUnlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockUnlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_UNLOCK\_NOT\_OWNED

`scePthreadRwlockUnlock()`: Unlocking of a reader/writer lock that is not locked by the calling thread

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_UNLOCK_NOT_OWNED       0xa0ff832a
```

## Description

This exception reason code is signaled when `scePthreadRwlockUnlock()` returns the `SCE_KERNEL_ERROR_EPERM` error in a state where the SLV for the process is enabled and set to "Abort".

The reader/writer lock specified for `scePthreadRwlockUnlock()` is not locked by the calling thread. There is a possibility that mutual exclusion in the application is broken.

# SLV\_RWLOCK\_WRLOCK\_DESTROYED

`scePthreadRwlockWrlock()`: Locking of a destroyed reader/writer lock (for writing)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SLV_RWLOCK_WRLOCK_DESTROYED       0xa0ff832c
```

## Description

This exception reason code is signaled when `scePthreadRwlockWrlock()` returns the `SCE_KERNEL_ERROR_EINVAL` error in a state where the SLV for the process is enabled and set to "Abort".

A typical reason for this exception to be signaled is because the reader/writer lock specified for `scePthreadRwlockWrlock()` has already been discarded or destroyed. At such times, there is a possibility that mutual exclusion in the application is broken.

## Other Exceptions

# SIGPIPE

Socket write error

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SIGPIPE       13
```

## Description

This exception reason code is signaled when the other party disconnects connection upon writing to a stream-oriented socket using a socket function, such as `sendto()`.

This exception only occurs when using a socket function that is exported from libScePosix\_stub\_weak.a. It does not occur with a function of the Net library.

## Notes

The SDK does not provide a method for processing `SIGPIPE`. Suppress the sending of this exception with a method such as `MSG_NOSIGNAL`, or use a function of the Net library.

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.