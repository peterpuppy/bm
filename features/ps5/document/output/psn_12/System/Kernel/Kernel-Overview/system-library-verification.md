# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/system-library-verification.html

# Development Support

# Overview

The PlayStation®5 kernel provides features that can only be used during application development. This chapter explains development support features and the information displayed for the debugger/console.

# Kernel Objects

This chapter uses "kernel objects" to refer to the objects created through kernel functions. Kernel objects can be checked in the System Objects window in the debugger. The following explains kernel objects handled by the kernel functions and how they are expressed in the debugger.

## Threads

Threads can be checked in the System Objects window and Threads window in the debugger. The "ID" displayed in both windows corresponds to the value (thread ID) returned by `scePthreadGetthreadid()`. This value is the same as the "ID" displayed by Razor CPU. Note that this thread ID is different from the `ScePthread` type value returned by `scePthreadCreate()` upon thread creation.

When a debug stop occurs in a process due to a problem that occurs in a thread, the exception reason code that corresponds to the cause will be displayed. For details about debug stop for processes, refer to the "[Process Stop Upon Occurrence of Anomalies](process-stop-upon-occurrence-of-anomalies.html)" section.

## Modules

Modules are dynamic libraries that are already loaded in a process. They can be checked in the System Objects window and Modules window in the debugger. The "ID" displayed in the System Objects window corresponds to the `SceKernelModule` type value that indicates the PRX module handle.

The following objects can only be checked in the System Objects window.

## Virtual Memory Ranges

All memory mapped to a process can be checked. "#" is an index for display and does not have any relation to values in programs. The association with a program can be made with the name displayed in "Detail" if an address or name has been set.

## Files

The files open in a process can be checked. "Descriptor" corresponds to the file descriptor returned by `sceKernelOpen()`.

## Sockets

Sockets correspond to the members of an `SceNetSockInfo` structure of the Net Library. "ID" is `s`, "Name" is the debugger name specified upon socket generation (etc.), "Process" is the process name, "Type" is `socket_type` (however, 0xB will be displayed for epoll), "Policy" is `policy`, "Priority" is unused, "Local Address" is `local_adr`, "Remote Address" is `remote_adr`, "Local Port" is `local_port`, "Remote Port" is `remote_port`, "Local Virtual Port" is `local_vport`, "Remote Virtual Port" is `remote_vport`, "State" is `state`, "Flags" is `flags`, "Receive Queue Length" is `recv_queue_length`, and "Send Queue Length" is `send_queue_length`. For details about these terms, refer to the [Net Library Overview](../Net-Overview/__document_toc.html) document.

## Mutexes

The mutexes with names given upon creation with `scePthreadMutexInit()` can be checked. "ID" is an identifier internally used by the system. "User ID" is an `ScePthreadMutex` type value. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the mutexes cannot be identified with names (because the same name has been given to multiple mutexes, for example), association is possible using the "User ID".

## Reader/Writer Locks

The reader/writer locks with names given upon creation with `scePthreadRwlockInit()` can be checked. "ID" is an identifier internally used by the system. "User ID" is an `ScePthreadRwlock` type value. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the reader/writer locks cannot be identified with names (because the same name has been given to multiple reader/writer locks, for example), association is possible using the "User ID".

## Condition Variables

The condition variables with names given upon creation with `scePthreadCondInit()` can be checked. "ID" is an identifier internally used by the system. "User ID" is an `ScePthreadCond` type value. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the condition variables cannot be identified with names (because the same name has been given to multiple condition variables, for example), association is possible using the "User ID".

## Barriers

The barriers with names given upon creation with `scePthreadBarrierInit()` can be checked. "ID" is an identifier internally used by the system. "User ID" is an `ScePthreadBarrier` type value. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the barriers cannot be identified with names (because the same name has been given to multiple barriers, for example), association is possible using the "User ID".

## Event Queues

The event queues with names given upon creation with `sceKernelCreateEqueue()` can be checked. "ID" is an identifier internally used by the system. "User ID" is an `SceKernelEqueue` type value. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the event queues cannot be identified with names (because the same name has been given to multiple event queues, for example), association is possible using the "User ID".

## Event Flags

The event flags created with `sceKernelCreateEventFlag()` can be checked. "ID" and "User ID" are `SceKernelEventFlag` type values. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the event flags cannot be identified with names (because the same name has been given to multiple event flags, for example), association is possible using the "ID" or "User ID".

## Semaphores

The semaphores created with `sceKernelCreateSema()` can be checked. "ID" and "User ID" are `SceKernelSema` type values. Association with a program can be made between the name given upon creation and the name displayed for "Name". If the semaphores cannot be identified with names (because the same name has been given to multiple semaphores, for example), association is possible using the "ID" or "User ID".

## POSIX Semaphores

The POSIX semaphores with names given upon initialization with `scePthreadSemInit()` can be checked. "ID" and "User ID" are `ScePthreadSem` type values. Association with a program can be made between the name given upon initialization and the name displayed for "Name". If the POSIX semaphores cannot be identified with names (because the same name has been given to multiple POSIX semaphores, for example), association is possible using the "ID" or "User ID".

## JobManager Runtimes

For details about using a job manager and debugger to check runtimes, refer to the [Job Library Overview](../Job-Overview/__document_toc.html) document.

## Various ULT Objects

For details about ULTs (user level threads), refer to the [Ult Library Overview](../Ult-Overview/__document_toc.html) document.

# System Library Verification

The system software provides "System Library Verification" (SLV) as a feature for dynamically (while an application is running) detecting potentially serious errors due to programming mistakes during development. The system will detect when specific errors are returned by specific functions in the SDK, and this feature will notify the application developers. This feature can only be used in Development Kits with the Release Check Mode set to Development Mode.

Note:

"Potentially serious errors" refer to mutual exclusion that is clearly broken, use of invalid objects, etc. Examples include the following cases.

* When `scePthreadMutexUnlock()` returns `SCE_KERNEL_ERROR_EPERM` (mutual exclusion broken)
* When `scePthreadMutexLock()` returns `SCE_KERNEL_ERROR_EINVAL` (invalid mutex use)

To enable SLV, specify the SLV setting upon starting a process with one of the various launcher tools (debugger, prospero-run.exe, etc.). One of two methods can be selected for notification upon detection of an error: "Abort" or "Warn".

Note:

The SLV setting (Abort/Warn) can only be specified upon process start. For the details of the specific methods for specifying the setting in the various launcher tools (debugger, prospero-run.exe, etc.), refer to the respective documents.

* When using the debugger, refer to the [Visual Studio Integration for PlayStation®5 User's Guide](../Visual_Studio_Integration_for_PS5-Users_Guide/__document_toc.html) document.
* When using prospero-run.exe, refer to the [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html) document.

## Abort

A unique exception (SLV exception) for which execution can still be continued occurs for each target error for detection, and the program will stop. When attached to a debugger, it will be possible to perform debugging similar to when a general exception occurs. At such times, in addition to information that can normally be obtained from a debugger, it will be possible to check the function name, reason for the error occurring, error code, and function arguments (up to the fourth argument). The behavior when not attached to a debugger depends on the debug settings (core dump settings) of the Development Kit.

## Warn

A warning log will be output to the console for notification when a target error for detection occurs. Except for the overhead for console output processing, there is no effect on program execution. The following information will be included in the warning log.

* Label that indicates error detection (`** System Library Verification **`)
* Function name/reason for the error occurring
* Thread ID/name
* Error code
* Function arguments (up to the fourth argument)
* Backtrace to the location where the error occurred

**Warning log example: `scePthreadMutexUnlock()` returning `SCE_KERNEL_ERROR_EPERM`**

```
** System Library Verification **                    // label
[scePthreadMutexUnlock(): Specified 'mutex' has been not locked by the calling thread. Synchronous control may have been failed.]
                                                     // Function name/reason for the error occurring
ThreadID  : 100996[slv_test]                         // Thread ID/name
Error code: 0x80020001                               // Error code
Arguments :                                          // Function arguments
  [0] 0x00000007ef2aabb8 : mutex
Backtrace :                                          // Backtrace
0x0000000078854108 [eboot.bin + 0x00000108]
0x00000000788564c9 [eboot.bin + 0x000024c9]
0x00000000788541af [eboot.bin + 0x000001af]
```

Note:

If a SLV warning log and console output from a source other than SLV occur at about the same time, there is a possibility that they will become mixed together. Therefore, waring logs are not guaranteed to always be output in the above format.

## Combinations of Detectable Functions and Errors

The combinations of detectable functions and error codes in SLV are shown in the following along with the SLV exception reason codes that are signaled for the "Abort" setting. For details about SLV exception reason codes, refer to the [Kernel Reference](../Kernel-Reference/__document_toc.html) document.

Combinations of Detectable Functions/Error Codes and SLV Exception Reason Codes

| **Function** | **Error code** | **SLV exception reason code** |
| --- | --- | --- |
| `sceKernelClose()` | `SCE_KERNEL_ERROR_EPERM` | `SLV_CLOSE_NOT_PERMITTED_FD` |
| `scePthreadMutexDestroy()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_MUTEX_DESTROY_DESTROYED` |
| `SCE_KERNEL_ERROR_EBUSY` | `SLV_MUTEX_DESTROY_LOCKED` |
| `scePthreadMutexLock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_MUTEX_LOCK_DESTROYED` |
| `scePthreadMutexTimedlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_MUTEX_TIMEDLOCK_DESTROYED` |
| `scePthreadMutexTrylock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_MUTEX_TRYLOCK_DESTROYED` |
| `scePthreadMutexUnlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_MUTEX_UNLOCK_DESTROYED` |
| `SCE_KERNEL_ERROR_EPERM` | `SLV_MUTEX_UNLOCK_NOT_OWNED` |
| `scePthreadCondBroadcast()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_COND_BROADCAST_DESTROYED` |
| `scePthreadCondDestroy()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_COND_DESTROY_DESTROYED` |
| `scePthreadCondSignal()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_COND_SIGNAL_DESTROYED` |
| `scePthreadCondSignalto()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_COND_SIGNALTO_DESTROYED` |
| `scePthreadCondTimedwait()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_COND_TIMEDWAIT_DESTROYED` |
| `SCE_KERNEL_ERROR_EPERM` | `SLV_COND_TIMEDWAIT_MUTEX_NOT_OWNED` |
| `scePthreadCondWait()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_COND_WAIT_DESTROYED` |
| `SCE_KERNEL_ERROR_EPERM` | `SLV_COND_WAIT_MUTEX_NOT_OWNED` |
| `scePthreadRwlockDestroy()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_DESTROY_DESTROYED` |
| `scePthreadRwlockRdlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_RDLOCK_DESTROYED` |
| `scePthreadRwlockTimedrdlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_TIMEDRDLOCK_DESTROYED` |
| `scePthreadRwlockTimedwrlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_TIMEDWRLOCK_DESTROYED` |
| `scePthreadRwlockTryrdlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_TRYRDLOCK_DESTROYED` |
| `scePthreadRwlockTrywrlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_TRYWRLOCK_DESTROYED` |
| `scePthreadRwlockUnlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_UNLOCK_DESTROYED` |
| `SCE_KERNEL_ERROR_EPERM` | `SLV_RWLOCK_UNLOCK_NOT_OWNED` |
| `scePthreadRwlockWrlock()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_RWLOCK_WRLOCK_DESTROYED` |
| `scePthreadBarrierDestroy()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_BARRIER_DESTROY_DESTROYED` |
| `SCE_KERNEL_ERROR_EBUSY` | `SLV_BARRIER_DESTROY_IN_USE` |
| `scePthreadBarrierWait()` | `SCE_KERNEL_ERROR_EINVAL` | `SLV_BARRIER_WAIT_DESTROYED` |
| `scePthreadCreate()` | `SCE_KERNEL_ERROR_EAGAIN` | `SLV_CREATE_THREAD_NO_RESOURCE` |
| `close()` | `EPERM` | `SLV_POSIX_CLOSE_NOT_PERMITTED_FD` |
| `pthread_mutex_destroy()` | `EINVAL` | `SLV_POSIX_MUTEX_DESTROY_DESTROYED` |
| `EBUSY` | `SLV_POSIX_MUTEX_DESTROY_LOCKED` |
| `pthread_mutex_lock()` | `EINVAL` | `SLV_POSIX_MUTEX_LOCK_DESTROYED` |
| `pthread_mutex_timedlock()` | `EINVAL` | `SLV_POSIX_MUTEX_TIMEDLOCK_DESTROYED` |
| `pthread_mutex_trylock()` | `EINVAL` | `SLV_POSIX_MUTEX_TRYLOCK_DESTROYED` |
| `pthread_mutex_unlock()` | `EINVAL` | `SLV_POSIX_MUTEX_UNLOCK_DESTROYED` |
| `EPERM` | `SLV_POSIX_MUTEX_UNLOCK_NOT_OWNED` |
| `pthread_cond_broadcast()` | `EINVAL` | `SLV_POSIX_COND_BROADCAST_DESTROYED` |
| `pthread_cond_destroy()` | `EINVAL` | `SLV_POSIX_COND_DESTROY_DESTROYED` |
| `pthread_cond_signal()` | `EINVAL` | `SLV_POSIX_COND_SIGNAL_DESTROYED` |
| `pthread_cond_timedwait()` | `EINVAL` | `SLV_POSIX_COND_TIMEDWAIT_DESTROYED` |
| `EPERM` | `SLV_POSIX_COND_TIMEDWAIT_MUTEX_NOT_OWNED` |
| `pthread_cond_wait()` | `EINVAL` | `SLV_POSIX_COND_WAIT_DESTROYED` |
| `EPERM` | `SLV_POSIX_COND_WAIT_MUTEX_NOT_OWNED` |
| `pthread_rwlock_destroy()` | `EINVAL` | `SLV_POSIX_RWLOCK_DESTROY_DESTROYED` |
| `pthread_rwlock_rdlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_RDLOCK_DESTROYED` |
| `pthread_rwlock_timedrdlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_TIMEDRDLOCK_DESTROYED` |
| `pthread_rwlock_timedwrlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_TIMEDWRLOCK_DESTROYED` |
| `pthread_rwlock_tryrdlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_TRYRDLOCK_DESTROYED` |
| `pthread_rwlock_trywrlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_TRYWRLOCK_DESTROYED` |
| `pthread_rwlock_unlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_UNLOCK_DESTROYED` |
| `EPERM` | `SLV_POSIX_RWLOCK_UNLOCK_NOT_OWNED` |
| `pthread_rwlock_wrlock()` | `EINVAL` | `SLV_POSIX_RWLOCK_WRLOCK_DESTROYED` |
| `pthread_barrier_destroy()` | `EINVAL` | `SLV_POSIX_BARRIER_DESTROY_DESTROYED` |
| `EBUSY` | `SLV_POSIX_BARRIER_DESTROY_IN_USE` |
| `pthread_barrier_wait()` | `EINVAL` | `SLV_POSIX_BARRIER_WAIT_DESTROYED` |
| `pthread_create()` | `EAGAIN` | `SLV_POSIX_CREATE_THREAD_NO_RESOURCE` |

Note:

There may be future additions to the combinations of detectable functions and error codes.

# Process Stop Upon Occurrence of Anomalies

When a process enters a state where execution cannot continue, the system software on a Development Kit/Testing Kit will cause the corresponding process to make a transition to a debug stop state. Upon the process making a transition to the debug stop state, an exception reason code will be set for the process and thread. By using the exception reason code, it will be possible to obtain the type and state of anomaly that occurred in the process.

Note that stops that coincide with exception reason codes are unrelated to the exception mechanism provided in C++. It will not be possible to use the C++ catch syntax to catch or prevent the stops.

## Anomaly Types

There are two main types of causes for the system software stopping execution of a process: thread causes (synchronous exceptions) and termination requests from the system software (asynchronous exceptions).

Synchronous exceptions will be signaled when an anomaly has been detected in a CPU instruction or SDK function executed by a thread.

Asynchronous exceptions will be signaled when an anomaly in a process has been detected by the system software. Since "`_ASYNC`" will be added to the end of the exception reason code symbols, these asynchronous exceptions can be distinguished from synchronous exceptions. Note that asynchronous exceptions are sent from the system software to a process; therefore, the thread displayed in the debugger will not necessarily be the thread that caused the exception.

The exception reason code will be stored in the `reason_code` member of the `SceCoredumpStopInfoCpu` structure that can be obtained using the core dump handler. Values are defined by the macro in kernel/stop\_codes.h.

The following shows some of the anomalous states and corresponding exception reason codes. For a complete list of exception reason codes, refer to the [Kernel Reference](../Kernel-Reference/__document_toc.html) document.

Anomalous States and Corresponding Exception Reason Codes

| **Anomaly** | **Exception type** | **Exception reason code** | **Notes** |
| --- | --- | --- | --- |
| Abnormal address (such as a NULL pointer) was accessed | Synchronous | `SIGSEGV` or `SIGBUS` | The code varies depending on the address value where the actual access was attempted. |
| Function in a dynamic library that has not been loaded was called | Synchronous | `PRX_NOT_RESOLVED_FUNCTION` |  |
| Stack protector detected stack corruption | Synchronous | `SYSTEM_STACK_CHECK_FAILURE` |  |
| Error was detected when SLV was enabled with the Abort setting | Synchronous | `SLV_*` |  |
| Application program called `abort()` | Synchronous | `LIBC_ABORT` |  |
| SDK function called `abort()` | Synchronous | `LIBC_INTERNAL_ABORT` |  |
| Page fault occurred in the GPU | Asynchronous | `GPU_FAULT_PAGE_FAULT_ASYNC` | Processes will also stop due to anomalies in the GPU. |
| Application suspension could not be carried out within a certain amount of time | Asynchronous | `SYSTEM_SUSPEND_BLOCK_TIMEOUT_ASYNC` |  |

## Analysis of Blocked Threads

When a thread is not scheduled, the kernel will analyze the progress status of the SDK function that was called by the thread and provide a block reason code. This code is useful for easily checking the kernel function call that is blocking the thread. In addition, some block reason codes also provide function parameter information and the predicted timeout time information in addition to the reason.

**Block reason codes**

The block reason codes for threads can be referenced through the debugger as part of the thread status. When using the synchronous object functions provided by the kernel, the wait object can be identified by the block reason code. The following shows some of the block reasons and corresponding block reason codes. For a complete list of block reason codes, refer to the [Kernel Reference](../Kernel-Reference/__document_toc.html) document.

Block Reasons and Corresponding Block Reason Codes

| **Block reason** | **Block reason code** | **Notes** |
| --- | --- | --- |
| No block reason | `WAIT_NONE` |  |
| Waiting for a condition variable | `WAIT_PTHREAD_CONDVAR` | This will also be used (and not `WAIT_SLEEP`) for waits with timeouts. |
| Communicating with the system software | `WAIT_SERVICE` |  |
| Sleeping (`sceKernelSleep()`, etc.) | `WAIT_SLEEP` |  |
| Reason could not be identified | `WAIT_THREAD_SUSPEND` or `WAIT_OTHER` | Refer to "[When the thread block reason cannot be identified](process-stop-upon-occurrence-of-anomalies.html#kernel-overview_9_4__p_jjx_dtv_42c)". |

**When the thread block reason cannot be identified**

Kernel block reason analysis is performed heuristically. Therefore, there are cases where the kernel cannot properly identify a block reason. If the thread state is RUN QUEUED, it is possible that it is blocked by another thread assigned to the same CPU. Refer to "[Blocks due to busy states](process-stop-upon-occurrence-of-anomalies.html#kernel-overview_9_4__p_d1l_2tv_42c)". Note that when identifying kernel functions called by a thread on a Development Kit/Testing Kit, the system software symbol information provided by SDK Manager must also be used.

**Blocks due to busy states**

Blocks due to busy states cannot be analyzed by the kernel. The following table shows some of the typical reasons for busy states.

Reasons for Busy States

| **Reason** | **Description** |
| --- | --- |
| An appropriate priority has not been set for the thread | When newly generating an attribute object, the attribute (thread priority) set with `scePthreadAttrSetschedparam()` will not be reflected. Confirm that the `SCE_PTHREAD_EXPLICIT_SCHED` attribute is set. |
| A sleep function such as `sceKernelSleep()` was called with a wait time of zero | Calls with a wait time of zero will terminate without doing anything, and thus a CPU will not be yielded to another thread. Consider using synchronization with a synchronization object instead. |
| `scePthreadYield()` was used in a state where there are no other threads with the same priority | Thread priorities are precisely applied. Therefore, a CPU will not be yielded to a thread with a lower priority than the caller thread by using `scePthreadYield()`. |
| The CPU affinity restrictions cannot be fulfilled by threads with the same priority | Except when using a round-robin scheduling policy, the kernel does not change the CPU assignment for an already scheduled thread to a thread with the same priority. |

# Messages Indicating Insufficient System Reserved Area

The following objects are allocated from the system reserved area:

* Synchronous objects and attributes of synchronous objects
* Thread management objects
* Thread attribute objects

When a large number of these objects have been allocated without being released, the system reserved area may be insufficient, and a message to that effect may be output to the console. If this happens, conduct the proper processing to release resources.

If you experience difficulties investigating which objects are using up resources, use the "★Debug Settings" > "Game" > "Internal Memory Dump" feature and inquire via the "Post new issue" page found under Private Support (<https://game.develop.playstation.net/support>). For details, refer to [Core Dump System Overview - Appendix A: Setting the Core Dump Feature Using Debug Settings](../Core_Dump_System-Overview/ps5-setting-core-dump-feature-using-debug-settings.html).

## Synchronous Objects and Attributes of Synchronous Objects

Objects are allocated from the system reserved area when the initialization functions (`scePthreadXxxInit()`) and object attribute initialization functions (`scePthreadXxxattrInit()`) of the following synchronous objects are called: mutexes, condition variables, reader/writer locks, and barriers. These objects can be released by calling, respectively, `scePthreadXxxDestroy()` and `scePthreadXxxattrDestroy()`.

If an object cannot be allocated, the following message is output to the console, and the initialization function returns `SCE_KERNEL_ERROR_ENOMEM`.

```
[ScePthread/System] Internal Memory is running out
```

## Thread Management Objects

Thread management objects are allocated from the system reserved area when threads are created and are released when the threads terminate. (For details, refer to the "[Threads and Memory Resources](threads-and-memory-resources.html)" section.) Allocation normally succeeds; however, if allocation does not succeed because of unforeseen circumstances, one of the following messages will be output to the console, and `scePthreadCreate()` will return `SCE_KERNEL_ERROR_ENOMEM`.

```
[ScePthread/System] Internal Memory for Pthread is running out

[ScePthread/System] Internal Memory for System TLS is running out
```

When threads that can be joined terminate, they can be released or put in a status awaiting reuse by calling `scePthreadJoin()`.

## Thread Attribute Objects

Thread attribute objects are allocated from the system reserved area when `scePthreadAttrInit()` is called and can be released by calling `scePthreadAttrDestroy()`. If a thread attribute object cannot be allocated, the following message will be output to the console, and `scePthreadAttrInit()` will return `SCE_KERNEL_ERROR_ENOMEM`.

```
[ScePthread/System] Internal Memory is running out
```

# GPI Switch

A single 64-bit length memory area called a GPI (General Purpose Input) switch is provided in the system for the purpose of debugging support. Applications can read the GPI switch value only during development. The read values can be freely interpreted and used by applications.

A value can be set for the GPI switch from "★Debug Settings" > "System" > "GPI Switch". Once set, it will be retained as long as the system is not initialized.

To read a value set for the GPI switch, use `sceKernelGetGPI()`. This function can obtain the GPI switch value only during the following times. At other times, 0x0 will always be obtained.

* When the Release Check Mode is set to Development Mode or Assist Mode

The initial value for the GPI switch is 0x0. To change a set value back to the initial value, set 0x0 from "GPI Switch". It is also possible to change a set value back to the initial value by initializing the system, but note that other important information concerning the GPI switch will also be initialized.

Only one GPI switch exists in the system. When a value is set for the GPU switch, note that there is a possibility that it will affect all applications that are run in the system. Also note that all execution entities and libraries included in the system software and SDKs provided by SIE will not have their behavior changed in relation to the GPI switch.

# GPO and Front Panel LEDs

Eight LEDs are provided on the front panel of a Development Kit for debugging purposes. These LEDs can be freely turned on/off by applications through GPO (General Purpose Output).

To control LED illumination, use `sceKernelSetGPO()`. This function can be used only when the Release Check Mode is set to Development Mode on a Development Kit. In other cases, the function will terminate normally without doing anything.