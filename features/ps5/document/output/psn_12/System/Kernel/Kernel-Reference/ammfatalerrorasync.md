# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/ammfatalerrorasync.html

# Exception Reason Codes

## System Software and Compiler Runtime (SYSTEM)

# SYSTEM\_ABNORMAL\_TERMINATION\_REQUEST

Forced termination due to `sceSystemServiceReportAbnormalTermination()`

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_ABNORMAL_TERMINATION_REQUEST       0xa0020318
```

## Description

This exception reason code is signaled when a process is forcefully terminated by calling `sceSystemServiceReportAbnormalTermination()`.

This exception reason code is only used with the corresponding function, and it indicates that an application voluntarily terminated.

## See Also

TRC [R5093](../../../TRC/latest/TRC/R5093.html)

# SYSTEM\_ASAN\_ASSERT

Assert of the AddressSanitizer

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_ASAN_ASSERT       0xa0028324
```

## Description

This exception reason code is signaled when the AddressSanitizer (ASan) detects an error for which execution can still be continued. Although execution can be continued under the user's responsibility when an error is signaled with this exception reason code, actual operation is undefined and program operation is not guaranteed.

Additional information may be output to the debugger or TTY.

When the detected error is fatal and program execution cannot be continued, `SYSTEM_ASAN_FATAL_ASSERT` may be signaled instead.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_ASAN\_FATAL\_ASSERT

Fatal error of the AddressSanitizer

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_ASAN_FATAL_ASSERT       0xa0020325
```

## Description

This exception reason code is signaled when the AddressSanitizer (ASan) detects an error for which execution cannot be continued.

Additional information may be output to the debugger or TTY.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_DEBUG\_RUNTIME\_ERROR

Process monitoring failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_DEBUG_RUNTIME_ERROR       0xa002031d
```

## Description

This exception reason code is signaled when process monitoring using certain debug features on a Development Kit cannot be continued because of insufficient resources, etc.

Process monitoring is carried out while the AddressSanitizer (ASan) of the CPU compiler is executed. Therefore, this exception reason code will not be signaled other than when the application is running on a Development Kit with the Release Check Mode set to Development Mode.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_DUMP\_AND\_CONTINUE\_REQUEST\_ASYNC

Core dump execution and continue request

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_DUMP_AND_CONTINUE_REQUEST_ASYNC       0xa002c315
```

## Description

This exception reason code is signaled when "★Generate Core file" > "Generate Core file and Continue" is selected in the menu displayed by pressing the PS button > options button. SDK libraries cannot cause this exception to occur.

## Notes

This exception is an asynchronous exception. Therefore, note that the thread displayed on the debugger or in the crash report will not necessarily be the thread for which the failure occurred.

# SYSTEM\_EXECUTABLE\_ACCESS\_ERROR

Verification failure of an executable file

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_EXECUTABLE_ACCESS_ERROR       0xa0020311
```

## Description

This exception reason code is signaled when a corruption is detected in the game package or system software in storage. The executable file may be corrupted.

## Notes

* If this exception occurs repeatedly, the problem may be solved by reinstalling the game package or reinstalling the system software in the safe mode.
* Depending on the circumstance in which the corruption is detected, `SYSTEM_INTERNAL_DATA_ACCESS_ERROR` may be signaled instead.

# SYSTEM\_ILLEGAL\_EXCEPTION\_CODE

Use of an invalid exception reason code

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_ILLEGAL_EXCEPTION_CODE       0xa002031a
```

## Description

This exception reason code is signaled when a number that is not recognized as an exception reason code is used as an exception reason code. SDK libraries cannot cause this exception to occur.

# SYSTEM\_ILLEGAL\_FUNCTION\_CALL

Invalid function call

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_ILLEGAL_FUNCTION_CALL       0xa002030a
```

## Description

This exception reason code is signaled when an SDK library function is called by an invalid method.

This exception will be signaled even when a usage prohibited function is called in a core dump handler registered with `sceCoredumpRegisterCoredumpHandler()`.

## See Also

TRC [R5087](../../../TRC/latest/TRC/R5087.html)

# SYSTEM\_IMAGE\_ALLOC\_ERROR

Insufficient memory for loading an executable file

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_IMAGE_ALLOC_ERROR       0xa0020326
```

## Description

This exception reason code is signaled when an executable file cannot be loaded due to insufficient flexible memory.

## Notes

Compiler features such as profile-guided optimization (PGO) can bloat an executable file and increase the size of flexible memory required to load it.

# SYSTEM\_INTERNAL\_DATA\_ACCESS\_ERROR

System software corruption

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_INTERNAL_DATA_ACCESS_ERROR       0xa0020319
```

## Description

This exception reason code is signaled when a corruption is detected in the system software in storage. The executable file of the application may also be corrupted.

## Notes

* If this exception occurs repeatedly, the problem may be solved by reinstalling the system software in the safe mode.
* Depending on the circumstance in which the corruption is detected, `SYSTEM_EXECUTABLE_ACCESS_ERROR` may be signaled instead.

# SYSTEM\_INTERNAL\_SERVICE\_CALL\_ERROR

Failure to communicate with the system software

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_INTERNAL_SERVICE_CALL_ERROR       0xa002031f
```

## Description

This exception reason code is signaled when a fatal error occurs during communication between the application and the system software.

This exception reason code is used instead of `SYSTEM_INTERNAL_SERVICE_RUNTIME_ERROR` by some components of the system software.

# SYSTEM\_INTERNAL\_SERVICE\_CALL\_FATAL

Failure to communicate with the system software

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_INTERNAL_SERVICE_CALL_FATAL       0xa0020320
```

## Description

This exception reason code is signaled when a fatal error occurs during communication between the application and the system software.

This exception reason code is used instead of `SYSTEM_INTERNAL_SERVICE_RUNTIME_ERROR` by some components of the system software.

# SYSTEM\_INTERNAL\_SERVICE\_RUNTIME\_ERROR

Failure to communicate with the system software

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_INTERNAL_SERVICE_RUNTIME_ERROR       0xa002031c
```

## Description

This exception reason code is signaled when a fatal error occurs during communication between the application and the system software.

This exception may be signaled, for example, when invalid data is specified as an argument to an SDK library function or when the work area for an SDK library has been corrupted.

# SYSTEM\_INTERNAL\_SERVICE\_RUNTIME\_FATAL

Failure to communicate with the system software

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_INTERNAL_SERVICE_RUNTIME_FATAL       0xa002031e
```

## Description

This exception reason code is signaled when a fatal error occurs during communication between the application and the system software.

This exception reason code is used instead of `SYSTEM_INTERNAL_SERVICE_RUNTIME_ERROR` by some components of the system software.

# SYSTEM\_IO\_PAGE\_FAULT\_ASYNC

Invalid memory access by the Ajm library

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_IO_PAGE_FAULT_ASYNC       0xa0024329
```

## Description

This exception reason code is signaled when invalid memory access by the Ajm library is detected.

For example, this exception may be signaled if the Ajm library accesses memory that does not have an `SCE_KERNEL_PROT_ACP_*` attribute.

## Notes

This exception is an asynchronous exception. Therefore, note that the thread displayed on the debugger or in the crash report will not necessarily be the thread for which the crash occurred.

# SYSTEM\_PTHREAD\_MUTEX\_ERROR

Fatal error of a mutex API

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_PTHREAD_MUTEX_ERROR       0xa0020321
```

## Description

This exception reason code is signaled when the system software's thread runtime library fails to verify a mutex.

This exception may be signaled, for example, when an attempt is made to operate a mutex that has already been deleted.

# SYSTEM\_PTHREAD\_RUNTIME\_ERROR

Fatal error of a thread management API

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_PTHREAD_RUNTIME_ERROR       0xa0020305
```

## Description

This exception reason code is signaled when a fatal error is detected by the system software's thread runtime library.

This exception may be signaled, for example, when a management area for objects such as mutexes is corrupted by the user program.

# SYSTEM\_STACK\_CHECK\_FAILURE

Stack check failure

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_STACK_CHECK_FAILURE       0xa0020307
```

## Description

This exception reason code is signaled when the stack check code generated by the compiler or the SDK library detects a corruption in the stack area.

A stack check code is generated with the `-fstack-protector-strong` option in a compiler.

## Notes

* The stack check code is embedded as a call to the \_\_stack\_chk\_fail symbol. Because of this, if this exception is signaled near a call to the \_\_stack\_chk\_fail symbol, it can be deduced that the stack check code detected an invalid overwrite access to a local variable.
* This exception is also signaled when the stack is corrupted by a parameter specified for certain memory transfer functions, such as `memcpy()` and `memset()`. When the export address generates an overflow, these functions will signal `SYSTEM_WRITE_ADDRESS_WRAPAROUND` instead.

## See Also

TRC [R5163](../../../TRC/latest/TRC/R5163.html)

# SYSTEM\_SUSPEND\_BLOCK\_TIMEOUT\_ASYNC

Suspend processing timeout

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_SUSPEND_BLOCK_TIMEOUT_ASYNC       0xa0024301
```

## Description

This exception reason code is signaled when the application suspend processing times out.

For information about application suspend processing, refer to [Programming Startup Guide - Application State Transitions - Cautions for Termination/Suspension Support](../Programming-Startup_Guide/ps5-cautions-for-termination-suspension-support.html).

## Notes

This exception is an asynchronous exception. Therefore, note that the thread displayed on the debugger or in the crash report will not necessarily be the thread that blocked suspension processing.

## See Also

TRC [R5089](../../../TRC/latest/TRC/R5089.html)

# SYSTEM\_TRIGGER\_COREDUMP\_REQUEST

Core dump execution request

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_TRIGGER_COREDUMP_REQUEST       0xa0028322
```

## Description

This exception reason code is signaled when a core dump execution request is made with `sceCoredumpDebugTriggerCoredump()`.

When application execution cannot be continued after core dump, for example, when the Release Check Mode is set to Release Mode, `SYSTEM_ILLEGAL_FUNCTION_CALL` will be signaled instead.

# SYSTEM\_TSAN\_ASSERT

Assert of the ThreadSanitizer

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_TSAN_ASSERT       0xa002832d
```

## Description

This exception reason code is signaled when the ThreadSanitizer (TSan) detects an error after which execution can still be continued. Although execution can be continued under the user's responsibility when an error is signaled with this exception reason code, actual operation is undefined and program operation is not guaranteed.

Additional information may be output to the debugger or TTY.

When the detected error is fatal and program execution cannot be continued, `SYSTEM_TSAN_FATAL_ASSERT` may be signaled instead.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_TSAN\_FATAL\_ASSERT

Fatal error of the ThreadSanitizer

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_TSAN_FATAL_ASSERT       0xa002032e
```

## Description

This exception reason code is signaled when the ThreadSanitizer (TSan) detects an error after which execution cannot be continued.

Additional information may be output to the debugger or TTY.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_UBSAN\_ASSERT

Assert of UndefinedBehaviorSanitizer

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_UBSAN_ASSERT       0xa002832a
```

## Description

This exception reason code is signaled when UndefinedBehaviorSanitizer (UBSan) detects an error for which execution can still be continued. Although execution can be continued under the user's responsibility when an error is signaled with this exception reason code, actual operation is undefined and program operation is not guaranteed.

Additional information may be output to the debugger or TTY.

When the detected error is fatal and program execution cannot be continued, `SYSTEM_UBSAN_FATAL_ASSERT` may be signaled instead.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_UBSAN\_FATAL\_ASSERT

Fatal error of UndefinedBehaviorSanitizer

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_UBSAN_FATAL_ASSERT       0xa002032b
```

## Description

This exception reason code is signaled when UndefinedBehaviorSanitizer (UBSan) detects an error for which execution cannot be continued.

Additional information may be output to the debugger or TTY.

## See Also

[Sanitizers Overview](../Sanitizers-Overview/__document_toc.html) document

# SYSTEM\_USER\_DEBUG\_REQUEST\_ASYNC

Simulated crash

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_USER_DEBUG_REQUEST_ASYNC       0xa0024304
```

## Description

This exception reason code is signaled when core dump execution is requested by user operation.

Core dump requested by user operation can be generated by selecting "★Generate Core file" > "Generate Core file and Quit" in the menu displayed by pressing the PS button > options button, or by setting to execute a core dump upon application termination using `sceCoredumpDebugForceCoredumpOnAppClose()` and subsequently terminating the application from the home screen. SDK libraries cannot cause this exception to occur.

## Notes

This exception is an asynchronous exception. Therefore, note that the thread displayed on the debugger or in the crash report will not necessarily be the thread for which the crash occurred.

# SYSTEM\_WRITE\_ADDRESS\_WRAPAROUND

Write address overflow

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_WRITE_ADDRESS_WRAPAROUND       0xa0020323
```

## Description

This exception reason code is signaled when access to an abnormal address occurs because of the parameter specified to some memory transfer functions such as `memcpy()` or `memset()`.

When a stack is corrupted due to a write, `SYSTEM_STACK_CHECK_FAILURE` will be signaled instead.

# SYSTEM\_XO\_VIOLATION

Error due to reading from/writing to an XO TEXT segment

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SYSTEM_XO_VIOLATION       0xa0020328
```

## Description

This exception reason code is signaled when read or write access has been performed on an execution-only (XO) TEXT segment.

To improve system security, all TEXT segments are mapped with the XO memory protection attribute.

## CPU Exceptions

# SIGBUS

Bus error (#GP)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SIGBUS       10
```

## Description

This exception reason code is generally signaled when the memory attempted to be accessed is not a canonical address. In addition, it may be signaled when CPU instructions are used with an invalid operand.

`SIGBUS` corresponds to a #GP exception in AMD64 architecture.

## Notes

* A canonical address in AMD64 architecture refers to a range expressed by an address with a signed 48-bit integer. Therefore, if an invalid pointer is referenced, `SIGBUS` or `SIGSEGV` will be signaled in accordance with the pointer value.
* Unlike `SIGSEGV`, `SIGBUS` will not record the access target address when executing a core dump even if the instruction that caused the exception is an instruction that accesses memory.
* If a process without a debugger attached executes an `SCE_BREAK()` or `SCE_STOP()` macro, `SIGBUS` may be signaled.

# SIGFPE

Arithmetic instruction exception (#DE, #MF, or #XF)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SIGFPE       8
```

## Description

This exception reason code is signaled when an exception occurs due to a CPU arithmetic instruction.

`SIGFPE` corresponds to a #DE, #MF, or #XF exception in AMD64 architecture.

## Notes

Note that `SIGFPE` will occur even for integer divide by zero exceptions (#DE).

# SIGILL

Invalid instruction exception (#UD)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SIGILL       4
```

## Description

This exception reason code is signaled when an invalid instruction is executed.

Using the `__builtin_trap()` built-in function in the compiler or `SCE_NORETURN_STOP()`, it is possible to embed instructions that cause `SIGILL`.

`SIGILL` corresponds to a #UD exception in AMD64 architecture.

## Notes

The compiler may output instructions that will cause this exception for undefined operations, such as referencing a NULL pointer.

# SIGSEGV

Segmentation violation (#PF)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SIGSEGV       11
```

## Description

This exception reason code is signaled when access to a memory area is rejected by the CPU paging mechanism.

`SIGSEGV` corresponds to a #PF exception in AMD64 architecture.

## Notes

If the memory that was attempted to be accessed is not in a canonical address range, `SIGBUS` will occur instead of `SIGSEGV`. A canonical address in AMD64 architecture refers to a range expressed by an address with a signed 48-bit integer. Therefore, if an invalid pointer is referenced, `SIGBUS` or `SIGSEGV` will be signaled in accordance with the pointer value.

# SIGTRAP

Debug exception (#DB)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_SIGTRAP       5
```

## Description

This exception reason code is signaled when program execution is stopped due to the CPU debugging mechanism. This exception will also be signaled when a break point set by `sceDbgSetHardwareBreakPoint()` is hit in a process without a debugger attached.

`SIGTRAP` corresponds to a #DB exception in AMD64 architecture.

## Notes

When the cause of `SIGTRAP` occurring can be recognized, a debugger or Target Manager API may display a different exception reason code than the one displayed in the TTY.

## GPU exceptions

# CPU\_FAULT\_\*

Suspend prohibited area timeout (GPU idle)

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_CPU_FAULT_SUSPENDPOINT_TIMEOUT_IN_RUN_ASYNC       0xa0d0c00e
#define SCE_KERNEL_STOP_CODE_CPU_FAULT_SUSPENDPOINT_TIMEOUT_IN_SUSPEND_ASYNC       0xa0d0c00f
```

## Description

The `CPU_FAULT_*` exception reason code will be signaled when a GPU driver cannot start suspend processing during a GPU idle state.

For a GPU driver to start suspension processing, `sce::Agc::suspendPoint()` must be called in advance. Refer to the technical note (<https://game.develop.playstation.net/technotes/view/100>) regarding the call to `suspendPoint()`.

## Notes

`CPU_FAULT_*` exceptions are all asynchronous exceptions. Therefore, note that the thread displayed in the debugger or crash report is not necessarily the thread that caused the exception.

## See Also

TRC [R5089](../../../TRC/latest/TRC/R5089.html)

# GPU\_FAULT\_\*

GPU exceptions

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_PAGE_FAULT_ASYNC       0xa0d0c005
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_BAD_COMMAND_ASYNC       0xa0d0c006
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_IDLE_TIMEOUT_AFTER_SUBMITDONE_ASYNC       0xa0d0c00b
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_SUSPENDPOINT_TIMEOUT_IN_RUN_ASYNC       0xa0d0c00c
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_SUSPENDPOINT_TIMEOUT_IN_SUSPEND_ASYNC       0xa0d0c00d
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_IDLE_TIMEOUT_AFTER_SUSPENDPOINT_ASYNC       0xa0d0c010
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_CONTEXT_STATE_OP_ERROR_ASYNC       0xa0d0c011
#define SCE_KERNEL_STOP_CODE_GPU_FAULT_WAVEFRONT_ERROR_ASYNC       0xa0d0c012
```

## Description

The `GPU_FAULT_*` exception reason code is signaled when a program execution stop is requested due to a GPU exception.

The kernel may output additional GPU exception information to the TTY. For details on GPU exception debugging, refer to the [prospero-gpu-coreviewer Overview](../prospero-gpu-coreviewer-Overview/__document_toc.html) document.

## Notes

`GPU_FAULT_*` exceptions are all asynchronous exceptions. Therefore, note that the thread displayed in the debugger or crash report is not necessarily the thread that caused the exception.

## AMM exceptions

# AMM\_FATAL\_ERROR\_ASYNC

Fatal AMM error

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_AMM_FATAL_ERROR_ASYNC       0xa002c501
```

## Description

This exception reason code is signaled when a fatal error is detected in AMM and the program is unable to continue running. Additional information is output to the TTY.

## See Also

[AMM Library Overview](../AMM-Overview/__document_toc.html) document

## APR Exceptions

# APR\_FATAL\_ERROR\_ASYNC

Fatal APR error

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_APR_FATAL_ERROR_ASYNC       0xa002c502
```

## Description

This exception reason code is signaled when the Release Check Mode is set to Release Mode and a fatal error is detected in APR whereby the program is unable to continue running.

## See Also

[APR Library Overview](../APR-Overview/__document_toc.html) document

## Dynamic Libraries (PRX)

# PRX\_INVALID\_IMAGE

Fatal data error for executable file

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_PRX_INVALID_IMAGE       0xa0020105
```

## Description

This exception reason code is signaled when the system software could not recognize a program file (eboot.bin, etc.) or dynamic library. There is a possibility that the file is corrupted.

## Notes

In order to correct this error, the file must be replaced. Instead of this error, `SYSTEM_EXECUTABLE_ACCESS_ERROR` will be signaled for storage read errors.

# PRX\_NOT\_RESOLVED\_FUNCTION

Unloaded PRX function call

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_PRX_NOT_RESOLVED_FUNCTION       0xa0020101
```

## Description

This exception reason code is signaled when attempting to call a function in an unloaded PRX (including an SDK library PRX). The library name and ID for the function that was attempted to be called will be displayed in the TTY when the exception occurs. To look up the function name using the displayed ID, process the linked PRX stub library with the `prospero-llvm-readelf` command in accordance with the TTY message.

If the function attempted to be called is in an SDK library, refer to the "Embedding Into a Program" section of the overview document for that library and confirm that the required PRX is loaded in advance. Note that there are SDK libraries that require explicit loading with `sceSysmoduleLoadModule()` and libraries that do not.

For PRX other than SDK libraries, confirm that the loading processing with `sceKernelLoadStartModule()` succeeded for the PRX for the function that was attempted to be called.

# PRX\_PROCESS\_STARTUP\_FAILURE

Failure to start process

## Definition

```
#include <kernel/stop_codes.h>
#define SCE_KERNEL_STOP_CODE_PRX_PROCESS_STARTUP_FAILURE       0xa0020104
```

## Description

This exception reason code is signaled when the loading/initialization of the SDK runtime library to be loaded automatically by the system fails.

This exception only occurs when the loading of a library that is automatically loaded by the system fails. SDK library calls by the application cannot cause this exception to occur. Therefore, when explicitly loading a PRX with `sceSysmoduleLoadModule()`, this exception will not occur due to load failure.

When the loading of the PRX in the/app0/sce\_module directory fails upon process startup, `PRX_SCE_MODULE_LOAD_ERROR` will be signaled instead.

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

## Other Exceptions