# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-create-sema.html

# Semaphores

# SceKernelSemaOptParam

Semaphore option parameters

## Definition

```
#include <kernel.h>
typedef struct _SceKernelSemaOptParam SceKernelSemaOptParam;
```

## Description

This structure is provided to be used for assigning option parameters when creating a semaphore with `sceKernelCreateSema()`.

# sceKernelCancelSema

Cancel a semaphore

## Definition

```
#include <kernel.h>
int sceKernelCancelSema(
    SceKernelSema sem,
    int setCount,
    int *pNumWaitThreads
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target semaphore |
| `setCount` | Number of semaphore resources to set to the semaphore after canceling, or a value less than 0 |
| `pNumWaitThreads` | Destination to store the number of threads released from the wait due to canceling, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified semaphore could not be found |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `pNumWaitThreads` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `setCount` is larger than `maxCount` specified with `sceKernelCreateSema()` |

## Description

This function cancels the semaphore specified with `sem`. If there are threads waiting to acquire semaphore resources from this semaphore, the threads will be forcibly released from the wait regardless of the number of requests. With `SCE_KERNEL_ERROR_ECANCELED` returned by `sceKernelWaitSema()`, it will be possible to determine that these threads were forcibly released from the wait.

For `setCount`, specify the number of semaphore resources to set to the semaphore after canceling. When a value smaller than 0 is specified, the initial value for the number of semaphore resources when the semaphore was created will be set.

For `pNumWaitThreads`, specify the variable for receiving the number of threads released from the wait due to canceling, or specify NULL if it is not required.

# sceKernelCreateSema

Create a semaphore

## Definition

```
#include <kernel.h>
int sceKernelCreateSema(
    SceKernelSema *sem,
    const char *pName,
    uint32_t attr,
    int initCount,
    int maxCount,
    const SceKernelSemaOptParam *pOptParam
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Destination to store the created semaphore |
| `pName` | Semaphore name (up to 32 bytes including the NULL-terminator character) |
| `attr` | Semaphore attribute (queue order) |
| `initCount` | Initial value for the number of semaphore resources |
| `maxCount` | Maximum value for the number of semaphore resources |
| `pOptParam` | Argument for expansion (specify NULL) |

## Return Values

Stores the created semaphore in `*sem` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `pName` is NULL, `attr` is invalid, `pOptParam` is not NULL, `initCount` is negative, `maxCount` is 0 or less, or `initCount` is larger than `maxCount` |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `pName` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Insufficient resources |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `sem` points to invalid memory |

## Description

This function creates a semaphore and sets the initial value. The required resources are allocated by the function.

For `pName`, specify the semaphore name. This name is used for identification when seen by operators during debugging, etc. Therefore, it does not have to be unique. A name up to 32 bytes including the NULL-terminator character can be specified. NULL cannot be specified.

For `attr`, specify one of the following macros that indicate the queue order as the semaphore attribute.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_SEMA_ATTR_TH_FIFO` | 0x01 | Queue order is FIFO |
| `SCE_KERNEL_SEMA_ATTR_TH_PRIO` | 0x02 | Queue order is thread priority |

If neither of the above is specified, `SCE_KERNEL_SEMA_ATTR_TH_FIFO` will be specified.

A semaphore is an exclusive control object that can be used when restricting the total number of shared resources. The total number of shared resources can be restricted by each thread following a rule where only the number of semaphore resources to be used are acquired from a specific semaphore before using shared resources, and then they are returned when access has ended.

In addition, it has a characteristic where the acquiring thread and returning thread can be different; therefore, they can be used for controlling a producer-consumer type data flow, for example.

# sceKernelDeleteSema

Delete a semaphore

## Definition

```
#include <kernel.h>
int sceKernelDeleteSema(
    SceKernelSema sem
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Semaphore to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified semaphore could not be found |

## Description

This function deletes the semaphore specified with `sem`. Resources allocated for the semaphore will be released.

When this function terminates normally `sem` will become invalid and can no longer be used, but if another CPU is performing processing related to the semaphore (for example), the release of the resources will be delayed until all references have ended.

When a semaphore is deleted, an error (`SCE_KERNEL_ERROR_EACCES`) will be returned to the threads waiting for the semaphore.

# sceKernelPollSema

Acquire semaphore resources without blocking

## Definition

```
#include <kernel.h>
int sceKernelPollSema(
    SceKernelSema sem,
    int needCount
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target semaphore |
| `needCount` | Number of semaphore resources to acquire |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified semaphore could not be found |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Insufficient semaphore resources |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `needCount` is smaller than 1 or larger than the maximum value specified with `sceKernelCreateSema()` |

## Description

This function acquires the `needCount` number of semaphore resources without blocking from the semaphore specified with `sem`.

If the target semaphore resources are less than `needCount`, it will immediately return an error (`SCE_KERNEL_ERROR_EBUSY)`.

## Notes

`sceKernelWaitSema()` is provided as a function that waits instead of returning an error if semaphore resources cannot be acquired.

## See Also

`sceKernelWaitSema()`

# sceKernelSignalSema

Return semaphore resources

## Definition

```
#include <kernel.h>
int sceKernelSignalSema(
    SceKernelSema sem,
    int signalCount
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target semaphore |
| `signalCount` | Number of semaphore resources to return |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified semaphore could not be found |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Could not return a semaphore resource because the maximum value for the number of semaphore resources was exceeded |

## Description

This function returns the `signalCount` number of semaphore resources to the semaphore specified with `sem`. If there are threads waiting to acquire semaphore resources from this semaphore, the threads in the queue beginning with the first in order will attempt to acquire semaphore resources and the threads that are able to acquire the requested number of resources will wake up.

If threads toward the beginning of the queue are requesting large number of semaphore resources and cannot wake up, it is possible for threads more behind in the queue to acquire their requested number of resources and wake up.

## Notes

It is possible for semaphore resources to be returned by a thread that did not acquire the semaphore resources.

# sceKernelWaitSema

Wait for semaphore resources to be acquired

## Definition

```
#include <kernel.h>
int sceKernelWaitSema(
    SceKernelSema sem,
    int needCount,
    SceKernelUseconds *pTimeout
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target semaphore |
| `needCount` | Number of semaphore resources to acquire |
| `pTimeout` | Destination to store the wait time limit (microseconds) and remaining time, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified semaphore could not be found |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_ECANCELED` | 0x80020055 | Specified semaphore was canceled |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `pTimeout` points to invalid memory |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Specified semaphore was deleted |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `needCount` is smaller than 1 or larger than the maximum value specified with `sceKernelCreateSema()` |

## Description

This function acquires the `needCount` number of semaphore resources from the semaphore specified with `sem`. It returns immediately if there are enough semaphore resources remaining at the time when the function is called. If there are not enough remaining, this function waits until another thread returns semaphore resources.

For `pTimeout`, specify a pointer to the variable where the wait time limit is set. Setting can be made in microsecond units; however, the precision of actual processing is in millisecond units. If the semaphore resources cannot be acquired even after waiting for the specified time, the `SCE_KERNEL_ERROR_ETIMEDOUT` error will occur, and 0 will be stored in `*pTimeout`. If they were acquired during the specified time, the remaining time will be stored in `*pTimeout`. To wait infinitely until the semaphore resources are acquired without timing out, specify NULL for `pTimeout`.

If multiple threads attempt to acquire semaphore resources from a single semaphore at the same time, the threads will wait in a queue. The queue order will be the order that threads started waiting (FIFO) or the priority order beginning with the higher priority threads, depending on the attribute specified when the semaphore was created. When other threads return semaphore resources, the threads in the queue beginning with the first in order will acquire semaphore resources and wake up if the requested number of resources are met.

## Notes

`sceKernelPollSema()` is provided as a function that immediately returns an error instead of waiting until semaphore resources are acquired when they are not immediately available.

## See Also

`sceKernelPollSema()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.