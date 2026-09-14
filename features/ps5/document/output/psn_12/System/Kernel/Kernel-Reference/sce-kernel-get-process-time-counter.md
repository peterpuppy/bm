# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-get-process-time-counter.html

# Time Management

# SceKernelTimespec

Time structure

## Definition

```
#include <kernel.h>
struct timespec { 
    time_t tv_sec; 
    long tv_nsec; 
};
typedef struct timespec SceKernelTimespec;
```

## Members

|  |  |
| --- | --- |
| `tv_sec` | Number of seconds |
| `tv_nsec` | Fraction less than one second (nanoseconds) |

## Description

This structure represents the time. The time elapsed from January 1, 1970 12:00 a.m. will be stored separately in the number of seconds and the fraction less than one second.

# SceKernelTimeval

Time structure

## Definition

```
#include <kernel.h>
struct timeval { 
    time_t tv_sec;
    suseconds_t tv_usec;
};
typedef struct timeval SceKernelTimeval;
```

## Members

|  |  |
| --- | --- |
| `tv_sec` | Number of seconds |
| `tv_usec` | Fraction less than one second (microseconds) |

## Description

This structure represents the time. It is used when obtaining the time with `sceKernelGettimeofday()`. The time elapsed from January 1, 1970 12:00 a.m. will be stored separately in the number of seconds and the fraction less than one second.

## See Also

`sceKernelGettimeofday()`

# sceKernelClockGetres

Get the precision of a clock

## Definition

```
#include <kernel.h>
int sceKernelClockGetres(
    SceKernelClockid clockId, 
    SceKernelTimespec *tp
)
```

## Arguments

|  |  |
| --- | --- |
| `clockId` | Clock type |
| `tp` | Destination to store the obtained precision |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `clockId` value is invalid |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | Memory that `tp` points to is invalid |

## Description

This function obtains the precision of the specified clock.

For `clockId`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_CLOCK_REALTIME` | 0 | Clock that indicates the real-world date and time |
| `SCE_KERNEL_CLOCK_MONOTONIC` | 4 | Clock that increases monotonically from the time of system startup |

For `tp`, the precision (granularity) of the clock specified in the `SceKernelTimespec` structure that tp points to is returned.

## See Also

`sceKernelClockGettime()`, `SceKernelTimespec`

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

# sceKernelClockGettime

Get the time

## Definition

```
#include <kernel.h>
int sceKernelClockGettime(
    SceKernelClockid clockId, 
    SceKernelTimespec *tp
)
```

## Arguments

|  |  |
| --- | --- |
| `clockId` | Clock type |
| `tp` | Destination to store the obtained time |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `clockId` value is invalid |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | Memory that `tp` points to is invalid |

## Description

This function obtains the time.

For `clockId`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_CLOCK_REALTIME` | 0 | Clock that indicates the real-world date and time |
| `SCE_KERNEL_CLOCK_MONOTONIC` | 4 | Clock that increases monotonically from the time of system startup |

For `tp`, specify a pointer to the `SceKernelTimespec` structure for receiving the time.

* When `SCE_KERNEL_CLOCK_REALTIME` is specified for `clockId`, the elapsed time from January 1, 1970 12:00 a.m. will be returned to `tp`.
* When `SCE_KERNEL_CLOCK_MONOTONIC` is specified for `clockId`, the elapsed time from the time of system startup will be returned to `tp`.

The precision of the clock can be obtained with `sceKernelClockGetres()`.

## See Also

`sceKernelClockGetres()`, `sceKernelGettimeofday()`, `SceKernelTimespec`

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

# sceKernelGetProcessTime

Get process time

## Definition

```
#include <kernel.h>
uint64_t sceKernelGetProcessTime(void)
```

## Arguments

None

## Return Values

Returns the process time (microseconds).

## Description

This function obtains the elapsed time (process time) from the process startup in microseconds. The process time is suspended during process suspension.

## See Also

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

# sceKernelGetProcessTimeCounter

Get process time counter

## Definition

```
#include <kernel.h>
uint64_t sceKernelGetProcessTimeCounter(void)
```

## Arguments

None

## Return Values

Returns the process time counter.

## Description

This function returns the value of the monotonic 64-bit counter that is synchronized with the process time. The frequency can be obtained with `sceKernelGetProcessTimeCounterFrequency()`.

The calling cost of this function is high speed compared to `sceKernelGetProcessTime()`.

The process time counter is provided for the purpose of replacing the time stamp counter that can be obtained with the CPU instructions rdtsc and rdtscp. The use of rdtsc or rdtscp is not recommended as the time stamp counter is prone to cause problems because it continues advancing even while the application is suspended. Use this function instead.

## See Also

`sceKernelGetProcessTimeCounterFrequency()`

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

# sceKernelGetProcessTimeCounterFrequency

Get the process time counter frequency

## Definition

```
#include <kernel.h>
uint64_t sceKernelGetProcessTimeCounterFrequency(void)
```

## Arguments

None

## Return Values

Returns the process time counter frequency (Hz).

## Description

This function returns the frequency (in Hz units) of the process time counter that can be obtained with `sceKernelGetProcessTimeCounter()`. This frequency will not change during the lifetime of a process.

## See Also

`sceKernelGetProcessTimeCounter()`

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

# sceKernelGetTscFrequency

Get the time stamp counter frequency

## Definition

```
#include <kernel.h>
uint64_t sceKernelGetTscFrequency(void)
```

## Arguments

None

## Return Values

Returns the time stamp counter frequency (Hz).

## Description

This function returns the time stamp counter frequency in Hz.

A time stamp counter exists for each CPU, but the frequency is the same value for all CPUs. This frequency will not change during the lifetime of a process.

Use of the time stamp counter is not recommended as it is prone to cause problems because it continues advancing even while the application is suspended. Instead, use the process time counter that can be obtained with `sceKernelGetProcessTimeCounter()`.

## See Also

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

# sceKernelGettimeofday

Get the time

## Definition

```
#include <kernel.h>
int sceKernelGettimeofday(
    SceKernelTimeval *tp
)
```

## Arguments

|  |  |
| --- | --- |
| `tp` | Destination to store the obtained time |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | Memory that `tp` points to is invalid |

## Description

This function obtains the current time.

For `tp`, specify a pointer to the `SceKernelTimeval` structure for receiving the time. The time elapsed from January 1, 1970 12:00 a.m. will be returned to this structure.

The precision of the clock can be obtained with `sceKernelClockGetres()`.

## See Also

`sceKernelClockGetres()`, `sceKernelClockGettime()`, `SceKernelTimeval`

[Kernel Overview - Time Management](../Kernel-Overview/time-management.html)

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.