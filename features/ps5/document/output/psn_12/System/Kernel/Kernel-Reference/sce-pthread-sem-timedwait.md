# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-pthread-sem-timedwait.html

# POSIX Semaphores

# scePthreadSemDestroy

Destroy a POSIX semaphore

## Definition

```
#include <kernel.h>
int scePthreadSemDestroy(
    ScePthreadSem *sem
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | POSIX semaphore to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid |

## Description

This function destroys the POSIX semaphore specified with `sem`. Resources allocated for the POSIX semaphore will be released.

# scePthreadSemGetvalue

Get the POSIX semaphore value

## Definition

```
#include <kernel.h>
int scePthreadSemGetvalue(
    ScePthreadSem * restrict sem,
    int * restrict sval
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target POSIX semaphore |
| `sval` | Destination to store the POSIX semaphore value |

## Return Values

Stores the POSIX semaphore value in `*sval` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid |

## Description

This function obtains the POSIX semaphore value specified with `sem`. The current POSIX semaphore value will be stored in `*sval`.

# scePthreadSemInit

Initialize a POSIX semaphore

## Definition

```
#include <kernel.h>
int scePthreadSemInit(
    ScePthreadSem *sem,
    int flag,
    unsigned int value,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | POSIX semaphore to initialize |
| `flag` | Argument for expansion (specify 0) |
| `value` | Initial value for the POSIX semaphore |
| `name` | POSIX semaphore name (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid, or `value` is larger than `INT_MAX`, or `flag` is not 0 |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Insufficient resources |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |

## Description

This function initializes the POSIX semaphore specified with `sem`.

For `name`, specify the POSIX semaphore name. This name is used for identification when seen by operators during debugging, etc. Therefore, it does not have to be unique. A name up to 32 bytes including the NULL-terminator character can be specified. When NULL is specified for `name`, the POSIX semaphore will be initialized without a name.

# scePthreadSemPost

Return semaphore resources

## Definition

```
#include <kernel.h>
int scePthreadSemPost(
    ScePthreadSem *sem
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target POSIX semaphore |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid |
| `SCE_KERNEL_ERROR_EOVERFLOW` | 0x80020054 | Could not return a semaphore resource because the maximum value for the number of semaphore resources was exceeded |

## Description

This function returns semaphore resources to the POSIX semaphore specified with `sem`. If there is a thread waiting to acquire semaphore resources from this POSIX semaphore, this function will wake up the thread.

## Notes

It is possible for semaphore resources to be returned by a thread that did not acquire the semaphore resources.

# scePthreadSemTimedwait

Wait for semaphore resource acquirement with a timeout

## Definition

```
#include <kernel.h>
int scePthreadSemTimedwait(
    ScePthreadSem *sem,
    SceKernelUseconds usec
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target POSIX semaphore |
| `usec` | Wait time limit (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |

## Description

This function acquires a semaphore resource from the POSIX semaphore specified with `sem`. It returns immediately if there is a semaphore resource remaining at the time when the function is called. If there is no semaphore resource remaining, this function waits until another thread returns a semaphore resource.

An error will be returned if a semaphore resource cannot be acquired within the wait time specified in `usec`.

## Notes

`scePthreadSemTrywait()` is provided as a function that immediately returns an error instead of waiting until a semaphore resource is acquired when one is not immediately available. In addition, `scePthreadSemWait()` is provided as a function that waits without a timeout.

## See Also

`scePthreadSemTrywait()`, `scePthreadSemWait()`

# scePthreadSemTrywait

Wait for semaphore resource acquirement without blocking

## Definition

```
#include <kernel.h>
int scePthreadSemTrywait(
    ScePthreadSem *sem
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target POSIX semaphore |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Semaphore could not be acquired |

## Description

This function acquires a semaphore resource from the POSIX semaphore specified with `sem`. It immediately acquires a semaphore resource if there is one remaining at the time when the function is called. If there is no semaphore resource remaining, this function immediately returns an error.

## Notes

`scePthreadSemWait()` is provided as a function that waits until a semaphore resource is acquired when one is not immediately available. In addition, `scePthreadSemTimedwait()` is provided as a function that waits with a timeout.

## See Also

`scePthreadSemWait()`, `scePthreadSemTimedwait()`

# scePthreadSemWait

Wait for a semaphore resource to be acquired

## Definition

```
#include <kernel.h>
int scePthreadSemWait(
    ScePthreadSem *sem
)
```

## Arguments

|  |  |
| --- | --- |
| `sem` | Target POSIX semaphore |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `sem` is invalid |

## Description

This function acquires a semaphore resource from the POSIX semaphore specified with `sem`. It returns immediately if there is a semaphore resource remaining at the time when the function is called. If there is no semaphore resource remaining, this function waits until another thread returns a semaphore resource.

## Notes

`scePthreadSemTrywait()` is provided as a function that immediately returns an error instead of waiting until a semaphore resource is acquired when one is not immediately available. In addition, `scePthreadSemTimedwait()` is provided as a function that waits with a timeout.

## See Also

`scePthreadSemTrywait()`, `scePthreadSemTimedwait()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.