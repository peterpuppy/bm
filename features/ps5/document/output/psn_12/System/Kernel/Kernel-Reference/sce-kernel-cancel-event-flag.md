# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-cancel-event-flag.html

# Event Flags

# SceKernelEventFlagOptParam

Event flag option parameters

## Definition

```
#include <kernel.h>
typedef struct _SceKernelEventFlagOptParam SceKernelEventFlagOptParam;
```

## Description

This structure is provided to be used for assigning option parameters when creating an event flag with `sceKernelCreateEventFlag()`.

## See Also

`sceKernelCreateEventFlag()`

# sceKernelCancelEventFlag

Cancel an event flag

## Definition

```
#include <kernel.h>
int sceKernelCancelEventFlag(
    SceKernelEventFlag ef,
    uint64_t setPattern,
    int *pNumWaitThreads
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Event flag to cancel |
| `setPattern` | Value to set for the event flag after canceling |
| `pNumWaitThreads` | Destination to store the number of threads released from the wait due to canceling, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified event flag does not exist |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `pNumWaitThreads` points to invalid memory |

## Description

This function cancels the event flag specified with `ef`. If there is a thread waiting for the event flag, it will be forcibly released from the wait regardless of the wait conditions. With `SCE_KERNEL_ERROR_ECANCELED` returned by `sceKernelWaitEventFlag()`, it will be possible to determine that these threads were forcibly released from the wait.

For `setPattern`, specify the new value to set for the event flag after canceling.

For `pNumWaitThreads`, specify the variable for receiving the number of threads released from the wait due to canceling, or specify NULL if it is not required.

## See Also

`sceKernelWaitEventFlag()`

# sceKernelClearEventFlag

Clear an event flag value

## Definition

```
#include <kernel.h>
int sceKernelClearEventFlag(
    SceKernelEventFlag ef,
    uint64_t bitPattern
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Target event flag |
| `bitPattern` | Bit pattern to clear |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified event flag does not exist |

## Description

This function clears the bits of the event flag specified with `ef`. The bitwise AND of the value specified for `bitPattern` and the current event flag value will become the new value for the event flag.

A thread already waiting for the event flag will not be released from the wait by calling this function.

# sceKernelCreateEventFlag

Create an event flag

## Definition

```
#include <kernel.h>
int sceKernelCreateEventFlag(
    SceKernelEventFlag *ef,
    const char *pName,
    uint32_t attr,
    uint64_t initPattern,
    const SceKernelEventFlagOptParam *pOptParam
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Destination to store the created event flag |
| `pName` | Event flag name (up to 32 bytes including the NULL-terminator character) |
| `attr` | Event flag attributes (queue order and whether or not multiple threads can wait) |
| `initPattern` | Event flag initial value |
| `pOptParam` | Argument for expansion (specify NULL) |

## Return Values

Stores the created event flag in `*ef` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `pName` is NULL, `attr` is invalid, or `pOptParam` is not NULL |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `pName` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Insufficient resources |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `ef` points to invalid memory |

## Description

This function creates an event flag and sets the initial value. The required resources are allocated by the function.

For `pName`, specify the event flag name. This name is used for identification when seen by operators during debugging, etc. Therefore, it does not have to be unique. A name up to 32 bytes including the NULL-terminator character can be specified. NULL cannot be specified.

For `attr`, specify the bitwise OR of the following macros that indicate the queue order and whether or not multiple threads can wait as event flag attributes.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_EVF_ATTR_TH_FIFO` | 0x01 | Queue order is FIFO |
| `SCE_KERNEL_EVF_ATTR_TH_PRIO` | 0x02 | Queue order is thread priority |
| `SCE_KERNEL_EVF_ATTR_SINGLE` | 0x10 | Multiple threads cannot wait at the same time |
| `SCE_KERNEL_EVF_ATTR_MULTI` | 0x20 | Multiple threads can wait at the same time |

When the specification for the queue order is omitted, `SCE_KERNEL_EVF_ATTR_TH_FIFO` will be specified. When the specification for whether or not multiple threads can wait is omitted, `SCE_KERNEL_EVF_ATTR_SINGLE` will be specified.

An event flag is a synchronization control object that indicates wait conditions with a bit pattern. When a thread waits for an event flag, specify the bit pattern along with whether it will wait until all bits match those of the event flag or it will wait until any 1 bit matches that of the event flag. The thread will be released from the wait if another thread sets a value for the event flag and the conditions are met.

## See Also

`SceKernelEventFlagOptParam`

# sceKernelDeleteEventFlag

Delete event flag

## Definition

```
#include <kernel.h>
int sceKernelDeleteEventFlag(
    SceKernelEventFlag ef
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Event flag to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Event flag specified with `ef` does not exist |

## Description

This function deletes the event flag specified with `ef`. Resources allocated for the event flag will be released.

When this function terminates normally `ef` will become invalid and can no longer be used, but if another CPU is performing processing related to the event flag (for example), the release of the resources will be delayed until all references have ended.

When an event flag is deleted, an error (`SCE_KERNEL_ERROR_EACCES)` will be returned to the threads waiting for the event flag.

# sceKernelPollEventFlag

Poll an event flag

## Definition

```
#include <kernel.h>
int sceKernelPollEventFlag(
    SceKernelEventFlag ef,
    uint64_t bitPattern,
    uint32_t waitMode,
    uint64_t *pResultPat
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Target event flag |
| `bitPattern` | Comparison value that will be a wait condition |
| `waitMode` | Wait mode and processing when the wait conditions have been met (see details below) |
| `pResultPat` | Destination to store the event flag value when the wait conditions are met, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error or for when the wait conditions are not met at the time when this function is called.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified event flag does not exist |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `waitMode` is invalid, or `bitPattern` is 0 |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Wait conditions are not met |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Multiple threads cannot wait for the specified event flag, and another thread is already waiting |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `pResultPat` points to invalid memory |

## Description

This function checks whether or not the value of the event flag specified with `ef` has met the conditions specified with `bitPattern` and `waitMode`. If the conditions are not met at the time when this function is called, it will immediately return the error `SCE_KERNEL_ERROR_EBUSY` without waiting, but otherwise has the same feature as `sceKernelWaitEventFlag()`.

For details about `bitPattern`, `waitMode`, and `pResultPat`, refer to the explanation of `sceKernelWaitEventFlag()`.

## See Also

`sceKernelWaitEventFlag()`

# sceKernelSetEventFlag

Set an event flag value

## Definition

```
#include <kernel.h>
int sceKernelSetEventFlag(
    SceKernelEventFlag ef,
    uint64_t bitPattern
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Target event flag |
| `bitPattern` | Bit pattern to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified event flag does not exist |

## Description

This function sets a value to the event flag specified with `ef`. The bitwise OR of the value specified for `bitPattern` and the current event flag value will become the new value for the event flag.

When the new event flag value meets the wait conditions of the thread waiting for the event flag, the thread will wake up. For details about wait conditions, refer to the explanation of `sceKernelWaitEventFlag()`.

## See Also

`sceKernelWaitEventFlag()`

# sceKernelWaitEventFlag

Wait for an event flag

## Definition

```
#include <kernel.h>
int sceKernelWaitEventFlag(
    SceKernelEventFlag ef,
    uint64_t bitPattern,
    uint32_t waitMode,
    uint64_t *pResultPat,
    SceKernelUseconds *pTimeout
)
```

## Arguments

|  |  |
| --- | --- |
| `ef` | Target event flag |
| `bitPattern` | Comparison value that will be a wait condition |
| `waitMode` | Wait mode and processing when the wait conditions have been met (see details below) |
| `pResultPat` | Destination to store the event flag value when the wait conditions are met, or NULL |
| `pTimeout` | Destination to store the wait time limit (microseconds) and remaining time, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error or for a timeout.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified event flag does not exist |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `waitMode` is invalid, or `bitPattern` is 0 |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Multiple threads cannot wait for the specified event flag, and another thread is already waiting |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_ECANCELED` | 0x80020055 | Canceled |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `pResultPat` or `pTimeout` points to invalid memory |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Event flag was deleted |

## Description

This function waits until the value of the event flag specified with `ef` meets the conditions specified with `bitPattern` and `waitMode`. If the conditions are already met at the time when this function is called, it will continue execution without waiting.

For `waitMode`, specify one of the following values that will become the wait condition operator.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_EVF_WAITMODE_AND` | 0x01 | When the bitwise AND of the event flag value and `bitPattern` is `bitPattern` (when the bits specified with `bitPattern` from among the event flag value are all 1's), the wait conditions will be considered met |
| `SCE_KERNEL_EVF_WAITMODE_OR` | 0x02 | When the bitwise AND of the event flag value and `bitPattern` is non-0 (when at least one of the bits specified with `bitPattern` from among the event flag value is 1), the wait conditions will be considered met |

By further adding one of the following values with the bitwise OR, the event flag bits can be cleared when the wait conditions are met.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_EVF_WAITMODE_CLEAR_ALL` | 0x10 | When the wait conditions are met, all event flag bits will be cleared |
| `SCE_KERNEL_EVF_WAITMODE_CLEAR_PAT` | 0x20 | When the wait conditions are met, the bits that correspond to `bitPattern` will be cleared |

For `pResultPat`, specify the variable that receives the event flag value, or specify NULL if the event flag value is not required. The details concerning the values that can be received are as follows.

* Wait conditions are met (`SCE_OK` returned): Event flag value immediately after the conditions are met, in other words before clearing is performed with `SCE_KERNEL_EVF_WAITMODE_CLEAR_ALL` or `SCE_KERNEL_EVF_WAITMODE_CLEAR_PAT`
* Was waiting but was canceled (the error `SCE_KERNEL_ERROR_ECANCELED` returned): Event flag value specified with `sceKernelCancelEventFlag()`
* Was waiting but the event flag was deleted (the error `SCE_KERNEL_ERROR_EACCES` returned): Event flag value immediately before deletion
* Was waiting but timed out (the error `SCE_KERNEL_ERROR_ETIMEDOUT` returned): Event flag value immediately before timeout

For `pTimeout`, specify a pointer to the variable where the wait time limit is set. Setting can be made in microsecond units; however, the precision of actual processing is in millisecond units. If the wait conditions are not met even after waiting for the specified time, the `SCE_KERNEL_ERROR_ETIMEDOUT` error will occur, and 0 will be stored in `*pTimeout`. If the wait conditions are met during the specified time, the remaining time will be stored in `*pTimeout`. To wait infinitely until the wait conditions are met without timing out, specify NULL for `pTimeout`.

The behavior of this function will change depending on the attributes of the event flag specified with `ef` and the states of other threads.

If an event flag has the `SCE_KERNEL_EVF_ATTR_SINGLE` attribute and another thread is waiting for the event flag, this function will immediately return the error `SCE_KERNEL_ERROR_EPERM`.

If an event flag has the `SCE_KERNEL_EVF_ATTR_MULTI` attribute, multiple threads can wait in a queue for the event flag. The queue order will be the order that threads started waiting if the event flag has the `SCE_KERNEL_EVF_ATTR_TH_FIFO` attribute. The queue order will be the thread priority order if the flag has the `SCE_KERNEL_EVF_ATTR_TH_PRIO` attribute.

If multiple threads are waiting, depending on the event flag value it is possible for the wait conditions of multiple threads to be met all at once. In such cases, note that beginning with the first thread in the queue and continuing in order, whether or not the wait conditions are met will be determined and if the conditions are met, processing for clearing the event flag bits will be performed according to the option specifications. In other words, if there is a thread waiting with the option to clear the event flag bits when the conditions are met, when the wait conditions are met for this thread, the threads later in the queue will be determined based on the event flag value after clearing; therefore, their wait conditions may not be met.

## Notes

`sceKernelPollEventFlag()` is provided as a function that immediately returns an error instead of waiting for the conditions to be met when the wait conditions are not met.

## See Also

`sceKernelCreateEventFlag()`, `sceKernelPollEventFlag()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.