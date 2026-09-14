# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/process-termination.html

# Process Management

# Overview

The PlayStation®5 kernel provides a process model. It performs resource protection among processes by managing process address space, physical memory, threads, etc., for each individual process.

# Process ID and Execution Priority

Each process has a unique process identifier (PID). The process identifier is a 32-bit positive integer that is assigned by the kernel when the process is created.

A process does not have an execution priority. Instead, an execution priority can be specified to each thread belonging to a process.

# Process Resources

One process has the following process resources.

* One virtual address space
* One main thread (a thread created when the process is created)
* An arbitrary number of threads
* Synchronous primitives such as mutexes

Each process resource has an identifier. These identifiers are unique locally within the process.

# Process Creation

When an application is started, one process (game process) will be created.

A game process cannot create a child process.

# Process Termination

Voluntary process termination by an application is prohibited by TRC [R5093](../../../TRC/latest/TRC/R5093.html). In other words, applications must not return from `main()` or call `exit()`/`_Exit()`. For information about application termination, refer to [Programming Startup Guide - Application State Transitions](../Programming-Startup_Guide/application-state-transitions.html).

## Execution Stop Due to Accessing a TEXT Segment

To improve the security of the system, all TEXT segments are mapped as execution-only (XO) TEXT segments; that is, they are set with only the execution attribute for their memory protection attributes. Both read- and write-accessing of XO TEXT segments are prohibited. If such accessing of an XO TEXT segment is detected, execution of the process will be forcibly stopped by an exception with the exception reason code of `SYSTEM_XO_VIOLATION`.

## Execution Stop/Forced Termination Due to Exceptions

When a status where it is impossible for the application to continue running (an exception) is detected, the kernel will forcefully stop the application and output a message to the TTY.

On a Development Kit with the Release Check Mode set to Development Mode, it is possible to attach a debugger to a stopped process and perform debugging. In addition, by setting "★Debug Settings" > "Core Dump" > "Core Dump Mode" to "coredump", it will be possible to automatically execute a core dump and cause forced termination after a process stops.

On Testing Kits and retail units, a core dump will always be executed, and the application will be forced to terminate after its execution is stopped. In such cases, it will be possible to use the Coredump library to add data to the output core dump file. For details, refer to the [Coredump Library Overview](../Coredump-Overview/__document_toc.html) document.

The causes of exceptions (exception reason codes) are classified with symbols. For details about exception reason codes, refer to the [Kernel Reference](../Kernel-Reference/__document_toc.html) document.

## Forced Termination Due to Asynchronous Exceptions

When the system software or GPU requests forced termination of an application (an asynchronous exception), the kernel will forcefully stop the application and output a message to the TTY. Debugging and core dumps can be performed the same as when an exception occurs.

Since asynchronous exceptions occur outside of processes, note that the threads will not indicate the cause when they occur. Backtraces will also be omitted from the TTY messages output by the kernel.

For details about the exception reason codes reported by the GPU, refer to the [prospero-gpu-coreviewer Overview](../prospero-gpu-coreviewer-Overview/__document_toc.html) document.

Asynchronous exceptions can be identified by "`_ASYNC`" at the end of the symbol.

# Collection of Process Resources

When a process terminates, the kernel will collect process resources that have not been collected. Specifically, the behavior is as described below.

## Threads

Threads are collected regardless of their state. If a thread is being executed, it will be forcefully terminated in the middle of its execution.

## Synchronous Primitives

Synchronous primitives are collected when the process terminates.

## Memory Mapped to Virtual Address Space

All memory areas mapped to the virtual address space are released.

# Initial Settings for the Main Thread

The initial settings for the main thread's name, priority, and stack size are as follows.

* Name: Name of the source executable file for the process (first 31 characters)
* Priority: 700
* Stack size: 2 MiB

To change the initial setting values, define the following global variables in the executable file.

```
#include <kernel.h>
extern const char sceUserMainThreadName[] __attribute__((weak));
extern int sceUserMainThreadPriority __attribute__((weak));
```

* `sceUserMainThreadName`: Specify a string up to 32 bytes including the NULL terminator for the name.
* `sceUserMainThreadPriority`: Specify the priority.