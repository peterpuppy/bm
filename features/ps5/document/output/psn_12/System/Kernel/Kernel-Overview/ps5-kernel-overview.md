# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/ps5-kernel-overview.html

# PlayStation®5 Kernel Overview

# PlayStation®5 Kernel

The PlayStation®5 kernel is the kernel that operates on PlayStation®5 and provides the execution environment for user applications. The PlayStation®5 kernel manages the following hardware resources and features.

* Process management
* Memory management
* CPU management
* Thread management
* Inter-thread synchronization
* Time management
* Timer feature
* Dynamic libraries
* File system
* Development support features

# PlayStation®5 Kernel API

The PlayStation®5 kernel API provides the aforementioned PlayStation®5 kernel features to application developers as an abstracted API. Specifically, the API includes the functions, macros, structures, and other interfaces that are defined or declared in the target/include/kernel.h header file.

These API features are all thread-safe and consist of system calls provided by the PlayStation®5 kernel and several libraries that are executed in userland.

## POSIX-compatible API

In addition to the PlayStation®5 kernel API, a POSIX-compatible API is provided for program portability. PlayStation®5 kernel API features with names that start with "sceKernel" correspond to POSIX-compatible API features, as shown in the table below. The supported POSIX-compatible API features are limited to those that have corresponding relationships with PlayStation®5 kernel API features. POSIX-compatible API features without such corresponding relationships cannot be used, even if they are written into header files.

PlayStation®5 Kernel API Features and POSIX-compatible API Features

|  | PlayStation®5 Kernel API | POSIX-compatible API |
| --- | --- | --- |
| Function | `sceKernelXxxYyy()` | `xxx_yyy()` |
| Type | `SceKernelXxx` | `struct xxx` |
| Value | `SCE_KERNEL_XXX_YYY` | `XXX_YYY` |
| Error code | `SCE_KERNEL_ERROR_XXX`  (negative value returned by a function) | `XXX`  (positive value stored in the variable `errno`) |
| Header | kernel.h | sched.h, unistd.h, time.h, sys/mman.h, sys/time.h, dirent.h, fcntl.h, stdio.h, sys/stat.h, sys/uio.h |
| Library | Not required to link explicitly | Required to explicitly link libScePosix\_stub\_weak.a |

Note the difference in behavior when an error occurs in a function. Functions with names that start with "sceKernel" will return a negative value (`SCE_KERNEL_ERROR_XXX`) indicating the error, while POSIX-compatible functions will return -1 and store a positive value (`XXX`) indicating the error in the global variable `errno`.

Note:

* For `open()`, when the file specified in the first argument does not exist, `O_CREAT` is specified in the second argument, and the specification of the third argument is omitted, the access rights of the generated file will be undefined. In addition, note that there is no compatibility between `SCE_KERNEL_S_*` and `S_*`, which are values that represent access rights. If necessary, specify the appropriate access rights (`SCE_KERNEL_S_*`) described in the explanation of `sceKernelChmod()` in the [Kernel Reference](../Kernel-Reference/__document_toc.html) document for the third argument of `open()`.
* The value of the global variable `errno` only has meaning immediately after a POSIX-compatible function call has failed. The `errno` value will be undefined after a POSIX-compatible function call terminates normally or after an SDK library function other than a POSIX-compatible function is called. (Therefore, the error causes for SDK library functions other than POSIX-compatible functions cannot be determined based on the `errno` value.)

When using POSIX-compatible API features, link libScePosix\_stub\_weak.a.

PlayStation®5 kernel API features with names that start with "scePthread" similarly correspond to pthread API features. For details, refer to the "[Thread Management](thread-management.html)" chapter.

PlayStation®5 kernel API features with names that start with "sceNet" similarly correspond to BSD socket API features. For details, refer to the [Net Library Overview](../Net-Overview/__document_toc.html) document.