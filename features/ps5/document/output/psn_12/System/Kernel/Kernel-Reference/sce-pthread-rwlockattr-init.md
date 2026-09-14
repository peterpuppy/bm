# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-pthread-rwlockattr-init.html

# Reader/Writer Locks

# scePthreadRwlockDestroy

Destroy a reader/writer lock

## Definition

```
#include <kernel.h>
int scePthreadRwlockDestroy(
    ScePthreadRwlock *rwlock
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Reader/writer lock to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Calling thread does not have permission |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid  \* SLV detection target error |

## Description

This function destroys the reader/writer lock specified with `rwlock`. Resources allocated for the reader/writer lock will be released.

## See Also

`scePthreadRwlockInit()`

# scePthreadRwlockInit

Create a reader/writer lock

## Definition

```
#include <kernel.h>
int scePthreadRwlockInit(
    ScePthreadRwlock *rwlock, 
    const ScePthreadRwlockattr *attr,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Destination to store the created reader/writer lock |
| `attr` | Reader/writer lock attributes, or NULL |
| `name` | Reader/writer lock name (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Stores the created reader/writer lock in `*rwlock` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Non-memory resources are insufficient |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Calling thread does not have permission |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |

## Description

This function creates and initializes a new reader/writer lock. The required resources are allocated by the function.

For `attr`, specify the reader/writer lock attribute object that has the attributes set for assigning to the reader/writer lock to be created. When NULL is specified for `attr`, the default attributes will be assigned.

For `name`, specify the name to assign to the reader/writer lock to be created. A name up to 32 bytes including the NULL-terminator character can be specified. When NULL is specified for `name`, a reader/writer lock without a name will be created.

A reader/writer lock is an exclusive control object that can perform a lock for reading or for writing. When performing a lock for reading, up to a specific number of threads can be locked if not locked for writing. By contrast, when performing a lock for writing, only one thread can be locked if not locked for reading. For example, buffers can be safely and efficiently shared by each thread following a rule where a thread must be locked as a reader before reading and then unlocked after the reading is complete, and a thread must be locked as a writer before writing and then unlocked after the writing is complete.

## Notes

The results are undefined if an already created reader/writer lock is specified for `rwlock`.

## See Also

`scePthreadRwlockattrInit()`, `scePthreadRwlockDestroy()`

# scePthreadRwlockRdlock

Lock a reader/writer lock for reading

## Definition

```
#include <kernel.h>
int scePthreadRwlockRdlock(
    ScePthreadRwlock *rwlock
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Target reader/writer lock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Maximum number of locks possible for reading has already been reached |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid  \* SLV detection target error |

## Description

This function locks the reader/writer lock specified with `rwlock` for reading. If the specified reader/writer lock is already locked for writing, or if there is a thread that has been blocked due to an attempt to lock for writing, it will not be possible to lock the specified reader/writer lock for reading. In such cases, this function will sleep and wait until the lock becomes possible and return after performing the lock.

## Notes

* It is possible to again perform a lock for reading if the reader/writer lock is already locked by the calling thread for reading. In such cases, note that `scePthreadRwlockUnlock()` must be called the same number of times as the number of locks.
* If an attempt is made to lock for reading if the reader/writer lock is already locked by the calling thread for writing, the results are undefined.
* `scePthreadRwlockTryrdlock()` is provided as a function that returns an error instead of waiting if a lock cannot be performed. In addition, `scePthreadRwlockTimedrdlock()` is provided as a function that waits with a timeout.

## See Also

`scePthreadRwlockUnlock()`, `scePthreadRwlockTryrdlock()`, `scePthreadRwlockTimedrdlock()`

# scePthreadRwlockTimedrdlock

Lock a reader/writer lock for reading (with timeout)

## Definition

```
#include <kernel.h>
int scePthreadRwlockTimedrdlock(
    ScePthreadRwlock *rwlock, 
    SceKernelUseconds usec
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Target reader/writer lock |
| `usec` | Time to wait if a lock is not immediately possible (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Maximum number of locks possible for reading has already been reached |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid (is not an initialized reader/writer lock object)  \* SLV detection target error |

## Description

This function locks the reader/writer lock specified with `rwlock` for reading. If the specified reader/writer lock is already locked for writing, or if there is a thread that has been blocked due to an attempt to lock for writing, it will not be possible to lock the specified reader/writer lock for reading. In such cases, this function will sleep and wait for the time specified with `usec`, and if a lock is not possible after waiting, a timeout error will be returned.

Specification to `usec` can be made in microsecond units. However, the precision of actual processing is in millisecond units.

## Notes

* It is possible to again perform a lock for reading if the reader/writer lock is already locked by the calling thread for reading. In such cases, note that `scePthreadRwlockUnlock()` must be called the same number of times as the number of locks.
* If an attempt is made to lock for reading if the reader/writer lock is already locked by the calling thread for writing, the results are undefined.
* `scePthreadRwlockRdlock()` is provided as a function that waits infinitely if a lock cannot be performed. In addition, `scePthreadRwlockTryrdlock()` is provided as a function that returns an error without waiting.

## See Also

`scePthreadRwlockUnlock()`, `scePthreadRwlockRdlock()`, `scePthreadRwlockTryrdlock()`

# scePthreadRwlockTimedwrlock

Lock a reader/writer lock for writing (with timeout)

## Definition

```
#include <kernel.h>
int scePthreadRwlockTimedwrlock(
    ScePthreadRwlock *rwlock, 
    SceKernelUseconds usec
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Target reader/writer lock |
| `usec` | Time to wait if a lock is not immediately possible (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid (is not an initialized reader/writer lock object)  \* SLV detection target error |

## Description

This function locks the reader/writer lock specified with `rwlock` for writing. When the specified reader/writer lock is already locked for reading or for writing, it will not be possible to lock it for writing. In such cases, this function will sleep and wait for the time specified with `usec`, and if a lock is not possible after waiting, a timeout error will be returned.

Specification to `usec` can be made in microsecond units. However, the precision of actual processing is in millisecond units.

## Notes

`scePthreadRwlockWrlock()` is provided as a function that waits infinitely if a lock cannot be performed. In addition, `scePthreadRwlockTrywrlock()` is provided as a function that returns an error without waiting.

## See Also

`scePthreadRwlockWrlock()`, `scePthreadRwlockTrywrlock()`

# scePthreadRwlockTryrdlock

Lock a reader/writer lock for reading without blocking

## Definition

```
#include <kernel.h>
int scePthreadRwlockTryrdlock(
    ScePthreadRwlock *rwlock
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Target reader/writer lock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Already locked for writing or an attempt to lock for writing has been already made |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Maximum number of locks possible for reading has already been reached |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid  \* SLV detection target error |

## Description

This function locks the reader/writer lock specified with `rwlock` for reading. If the specified reader/writer lock is already locked for writing, or if there is a thread that has been blocked due to an attempt to lock for writing, it will not be possible to lock the specified reader/writer lock for reading. In such cases, an error will be returned.

## Notes

* It is possible to again perform a lock for reading if the reader/writer lock is already locked by the calling thread for reading. In such cases, note that `scePthreadRwlockUnlock()` must be called the same number of times as the number of locks.
* If an attempt is made to lock for reading if the reader/writer lock is already locked by the calling thread for writing, the results are undefined.
* `scePthreadRwlockRdlock()` is provided as a function that waits if a lock cannot be performed. In addition, `scePthreadRwlockTimedrdlock()` is provided as a function that waits with a timeout.

## See Also

`scePthreadRwlockUnlock()`, `scePthreadRwlockRdlock()`, `scePthreadRwlockTimedrdlock()`

# scePthreadRwlockTrywrlock

Lock a reader/writer lock for writing without blocking

## Definition

```
#include <kernel.h>
int scePthreadRwlockTrywrlock(
    ScePthreadRwlock *rwlock
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Reader/writer lock to lock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Specified reader/writer lock is already locked |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid  \* SLV detection target error |

## Description

This function locks the reader/writer lock specified with `rwlock` for writing. When the specified reader/writer lock is already locked for reading or for writing by another thread, it will not be possible to lock it for writing. In such cases, an error will be returned.

## Notes

* If this function is used to attempt to lock a reader/writer lock that is already locked by the calling thread for reading or for writing, the results are undefined.
* `scePthreadRwlockWrlock()` is provided as a function that waits until a lock is possible if a lock cannot be performed. In addition, `scePthreadRwlockTimedwrlock()` is provided as a function that waits with a timeout.

## See Also

`scePthreadRwlockWrlock()`, `scePthreadRwlockTimedwrlock()`

# scePthreadRwlockUnlock

Unlock a reader/writer lock

## Definition

```
#include <kernel.h>
int scePthreadRwlockUnlock(
    ScePthreadRwlock *rwlock
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Reader/writer lock to unlock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Specified reader/writer lock is not locked by the calling thread  \* SLV detection target error |

## Description

This function unlocks the reader/writer lock specified with `rwlock` (regardless of whether the lock is for reading or for writing).

## See Also

`scePthreadRwlockRdlock()`, `scePthreadRwlockWrlock()`, `scePthreadRwlockTryrdlock()`, `scePthreadRwlockTrywrlock()`, `scePthreadRwlockTimedrdlock()`, `scePthreadRwlockTimedwrlock()`

# scePthreadRwlockWrlock

Lock a reader/writer lock for writing

## Definition

```
#include <kernel.h>
int scePthreadRwlockWrlock(
    ScePthreadRwlock *rwlock
)
```

## Arguments

|  |  |
| --- | --- |
| `rwlock` | Reader/writer lock to lock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `rwlock` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory (for a statically initialized reader/writer lock) |

## Description

This function locks the reader/writer lock specified with `rwlock` for writing. When the specified reader/writer lock is already locked for reading or for writing, it will not be possible to lock it for writing. In such cases, this function will sleep and wait until the lock becomes possible and return after performing the lock.

## Notes

* If this function is used to attempt to lock a reader/writer lock that is already locked by the calling thread for reading or for writing, the results are undefined.
* `scePthreadRwlockTrywrlock()` is provided as a function that returns an error instead of waiting if a lock cannot be performed. In addition, `scePthreadRwlockTimedwrlock()` is provided as a function that waits with a timeout.

## See Also

`scePthreadRwlockTrywrlock()`, `scePthreadRwlockTimedwrlock()`

# scePthreadRwlockattrDestroy

Destroy a reader/writer lock attribute object

## Definition

```
#include <kernel.h>
int scePthreadRwlockattrDestroy(
    ScePthreadRwlockattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Reader/writer lock attribute object to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function destroys a reader/writer lock attribute object. Resources allocated for the reader/writer lock attribute object will be released.

## See Also

`scePthreadRwlockattrInit()`

# scePthreadRwlockattrGettype

Get the type parameter of a reader/writer lock attribute object

## Definition

```
#include <kernel.h>
int scePthreadRwlockattrGettype(
    ScePthreadRwlockattr *attr,
    int *type
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target reader/writer lock attribute object |
| `type` | Destination to store the obtained type parameter |

## Return Values

Stores the obtained type parameter in `*type` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function obtains the type parameter set for the reader/writer lock attribute object specified with `attr`.

In `*type`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_RWLOCK_NORMAL` | 1 | Prioritize writer lock (default) |
| `SCE_PTHREAD_RWLOCK_PREFER_READER` | 2 | Prioritize reader lock |

## See Also

`scePthreadRwlockattrInit()`, `scePthreadRwlockattrSettype()`

# scePthreadRwlockattrInit

Create a reader/writer lock attribute object

## Definition

```
#include <kernel.h>
int scePthreadRwlockattrInit(
    ScePthreadRwlockattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Destination to store the created reader/writer lock attribute object |

## Return Values

Stores the created reader/writer lock attribute object in `*attr` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function creates a reader/writer lock attribute object and stores it in `*attr`. The required resources are allocated by the function.

A reader/writer lock attribute object is used for specifying reader/writer lock supplementary parameters for `scePthreadRwlockInit()`. `scePthreadRwlockattrInit()` creates a reader/writer lock attribute object with all parameters set to the default values. If `scePthreadRwlockInit()` returns, the reader/writer lock attribute object will no longer be needed, but it is possible to reuse it as is or change the required parameters in order to create another reader/writer lock.

Once a reader/writer lock attribute object is no longer needed, destroy it using `scePthreadRwlockattrDestroy()`.

The behavior of this function is undefined when an invalid value is specified for `attr`. However, `SCE_KERNEL_ERROR_EINVAL` may be returned for specific invalid values.

## See Also

`scePthreadRwlockattrDestroy()`, `scePthreadRwlockInit()`

# scePthreadRwlockattrSettype

Set the type parameter of a reader/writer lock attribute object

## Definition

```
#include <kernel.h>
int scePthreadRwlockattrSettype(
    ScePthreadRwlockattr *attr, 
    int type
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target reader/writer lock attribute object |
| `type` | Type parameter to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` or `type` is invalid |

## Description

This function sets the value specified with `type` to the type parameter of the reader/writer lock attribute object specified with `attr`.

For `type`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_RWLOCK_NORMAL` | 1 | Prioritize writer lock (default) |
| `SCE_PTHREAD_RWLOCK_PREFER_READER` | 2 | Prioritize reader lock |

## See Also

`scePthreadRwlockattrInit()`, `scePthreadRwlockattrGettype()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.