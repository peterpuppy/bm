# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-is-trinity-mode.html

# CPU Management

# SceKernelCpumask

CPU mask

## Definition

```
#include <kernel.h>
typedef uint64_t SceKernelCpumask;
```

## Description

This a type for handling masks. Each bit corresponds one-to-one to a CPU. From the lowest bit as 0, the position of each bit represents the number of a CPU. In other words, bit 0 represents CPU#0, bit 1 CPU#1, bit 2 CPU#2, and so forth, in order. For details about the CPUs that an application can use, refer to [Kernel Overview - CPU Management](../Kernel-Overview/cpu-management.html).

This type is used for CPU masks ("CPU affinity masks") that represent CPU affinities for threads in the kernel API features listed under "See Also" and in the APIs of various libraries. For details about CPU affinities, refer to [Kernel Overview - Thread Management - Thread Scheduling](../Kernel-Overview/thread-scheduling.html).

When setting a CPU affinity mask, you can use the macros listed below that represent all CPUs that can be used by the application based on its operating mode.

* `SCE_KERNEL_CPUMASK_13CPU` (if the operation mode is Base Mode or Trinity Mode)
* `SCE_KERNEL_CPUMASK_8CPU` (if the operation mode is low energy mode)

This type is also used when obtaining which CPUs can be used based on the application's operation mode using `sceKernelGetAvailableCpumask()`.

## See Also

`scePthreadAttrGetaffinity()`, `scePthreadAttrSetaffinity()`, `scePthreadGetaffinity()`, `scePthreadSetaffinity()`

# sceKernelGetAvailableCpumask

Gets which CPUs can be used based on the application's operation mode

## Definition

```
#include <kernel.h>
SceKernelCpumask sceKernelGetAvailableCpumask(void)
```

## Arguments

None

## Return Values

Returns a CPU mask (`SceKernelCpumask`) where the bits representing each of the CPUs that the application can use are toggled to 1.

## Description

This function obtains which CPUs an application can use based on its operation mode.

For details about the CPUs that can be used in each operating mode, refer to [Kernel Overview - CPU Management - Overview of CPU Resources and CPU Management During Foreground Execution](../Kernel-Overview/cpu-resources-and-cpu-management-during-foreground-execution.html). For details about each operation mode and how the operation mode is determined, refer to [Programming Startup Guide - Basic Information on Application Execution Environments - Application Operation Modes](../Programming-Startup_Guide/ps5-application-operation-modes.html).

# sceKernelGetOperationMode

Get the operation mode applied to the application

## Definition

```
#include <kernel.h>
void sceKernelGetOperationMode(
    int *mode,
    int *sub
)
```

## Arguments

|  |  |
| --- | --- |
| `mode` | Destination to store the obtained operation mode |
| `sub` | Destination to store the retrieved sub-operation mode (whether the application is running in low energy mode) |

## Return Values

None

## Description

This function checks the operation mode applied to the application.

In `*mode`, one of the following values that represents the application's operation mode is stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_OPERATION_MODE_PS4_BASE` | 0 | PlayStation®4 Base mode  The PlayStation®5 SDK does not allow you to create applications that run in this operation mode. |
| `SCE_KERNEL_OPERATION_MODE_NEO` | 1 | PlayStation®4 NEO mode  The PlayStation®5 SDK does not allow you to create applications that run in this operation mode. |
| `SCE_KERNEL_OPERATION_MODE_PS5_BASE` | 2 | Base mode (for PlayStation®5) |
| `SCE_KERNEL_OPERATION_MODE_TRINITY` | 3 | Trinity mode |

In `*sub`, one of the following values that represents whether the application is running in low energy mode is stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_OPERATION_SUBMODE_NONE` | 0 | Not operating in low energy mode |
| `SCE_KERNEL_OPERATION_SUBMODE_LOW_ENERGY` | 1 | Operating in low energy mode |

In summary, the following values are stored in each argument, depending on the operation mode applied to the application.

| **Operation mode** | `mode` | `sub` |
| --- | --- | --- |
| Base mode (for PlayStation®5) | 2 | 0 |
| Trinity mode | 3 | 0 |
| Low energy mode | 2\* | 1 |

\*When in low energy mode, 2 (`SCE_KERNEL_OPERATION_MODE_PS5_BASE`) is stored in `mode`. This represents the fact that low energy mode is the same as Base mode, except that the resources that can be used in it are limited.

For details about each operation mode and how the operation mode is determined, refer to [Programming Startup Guide - Basic Information on Application Execution Environments - Application Operation Modes](../Programming-Startup_Guide/ps5-application-operation-modes.html).

# sceKernelIsTrinityMode

**[PS5® Pro Dedicated]** Checks whether the application is running in Trinity mode

## Definition

```
#include <kernel.h>
int sceKernelIsTrinityMode(void)
```

## Arguments

None

## Return Values

Returns 1 if the application is running in Trinity mode. Returns 0 if that is not the case.

## Description

This function checks whether the application is running in Trinity mode.

When running a PlayStation®5 Pro-compatible application, this function returns 0 if the application is running in low energy mode or if the Force PS5 Base Mode feature is enabled on a Trinity Development Kit. For details about low energy mode and the Force PS5 Base Mode feature, refer to [Programming Startup Guide - Basic Information on Application Execution Environments - Application Runtime Modes](../Programming-Startup_Guide/ps5-application-runtime-modes.html).

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.