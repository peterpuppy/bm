# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-pthread-mutexattr-init.html

# Mutexes

# scePthreadMutexDestroy

Destroy a mutex

## Definition

```
#include <kernel.h>
int scePthreadMutexDestroy(
    ScePthreadMutex *mutex
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Mutex to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `mutex` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | `mutex` is locked by another thread  \* SLV detection target error |

## Description

This function destroys a mutex. Resources allocated for the mutex will be released.

## Notes

While other mutex functions are multithread safe, note that this function is an exception; this function is not multithread safe with mutex functions for the same `mutex` including this function. If this function is called targeting a `mutex` when that `mutex` is locked by another thread, this function may generate an exception without returning `SCE_KERNEL_ERROR_EBUSY`. Therefore, this function should not be called for a mutex that may be locked by another thread.

## See Also

`scePthreadMutexInit()`

# scePthreadMutexGetprioceiling

Get the priority ceiling value for a mutex

## Definition

```
#include <kernel.h>
int scePthreadMutexGetprioceiling(
    ScePthreadMutex *mutex,
    int *prioceiling
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Target mutex |
| `prioceiling` | Destination to store the obtained priority ceiling value |

## Return Values

Stores the obtained priority ceiling value in `*prioceiling` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified mutex does not exist |
| Specified mutex does not have a priority protection attribute |

## Description

This function obtains the priority ceiling value currently set for the mutex specified with `mutex`.

## See Also

`scePthreadMutexSetprioceiling()`

# scePthreadMutexInit

Create a mutex

## Definition

```
#include <kernel.h>
int scePthreadMutexInit(
    ScePthreadMutex *mutex, 
    const ScePthreadMutexattr *attr,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Destination to store the created mutex |
| `attr` | Mutex attributes, or NULL |
| `name` | Mutex name (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Stores the created mutex in `*mutex` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Insufficient resources |

## Description

This function creates and initializes a new mutex. The required resources are allocated by the function.

For `attr`, specify the mutex attribute object that has the attributes set for assigning to the mutex to be created. When NULL is specified for `attr`, the default attributes will be assigned. Default attributes are default for type (same as when specifying `SCE_PTHREAD_MUTEX_ERRORCHECK)` and `SCE_PTHREAD_PRIO_NONE` for protocol.

For `name`, specify the name to assign to the mutex to be created. A name up to 32 bytes including the NULL-terminator character can be specified. When NULL is specified for `name`, a mutex without a name will be created.

A mutex is an exclusive control object that can be locked by just one thread, and other threads cannot lock it until it is unlocked by the thread that performed the lock. Shared resources can be exclusively used by each thread following a rule where a specific mutex is locked before using a shared resource and then unlocked when the usage is complete.

## See Also

`scePthreadMutexattrInit()`, `scePthreadMutexDestroy()`

# scePthreadMutexLock

Lock a mutex

## Definition

```
#include <kernel.h>
int scePthreadMutexLock(
    ScePthreadMutex *mutex
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Mutex to lock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `mutex` is invalid  \* SLV detection target error |
| Cannot lock because the calling thread priority is higher than the ceiling value (only when the specified mutex has a priority protection attribute)  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EDEADLK` | 0x8002000b | Calling thread already locks the specified mutex (only when the specified mutex does not have a recursive lock attribute) |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | The maximum number for recursive locks has already been reached (only when the specified mutex has a recursive lock attribute) |

## Description

This function locks the mutex specified with `mutex`. If the specified mutex is already locked by another thread, this function will sleep and wait until the lock is possible, and then return after performing the lock.

## Notes

If the specified mutex is already locked by another thread, `scePthreadMutexTrylock()` is provided as a function that returns an error immediately without waiting for the lock to become possible. In addition, `scePthreadMutexTimedlock()` is provided as a function that waits with a timeout.

## See Also

`scePthreadMutexTimedlock()`, `scePthreadMutexTrylock()`, `scePthreadMutexUnlock()`

# scePthreadMutexSetprioceiling

Change the priority ceiling value for a mutex

## Definition

```
#include <kernel.h>
int scePthreadMutexSetprioceiling(
    ScePthreadMutex *mutex,
    int prioceiling,
    int *old
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Target mutex |
| `prioceiling` | Priority ceiling after the change |
| `old` | Destination to store the priority ceiling before the change, or NULL |

## Return Values

Stores the priority ceiling before the change in `*old` (if `old` is not NULL) and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified mutex does not exist |
| Specified mutex does not have a priority protection attribute |
| Specified priority ceiling value is out of range |

## Description

This function changes the priority ceiling value currently set for the mutex specified with `mutex`. It locks the specified mutex to perform the change. If another thread locks the mutex, this function waits until the lock is possible, and performs the change after locking. After the change, this function will unlock the mutex and return.

## See Also

`scePthreadMutexGetprioceiling()`

# scePthreadMutexTimedlock

Lock a mutex (with timeout)

## Definition

```
#include <kernel.h>
int scePthreadMutexTimedlock(
    ScePthreadMutex *mutex, 
    SceKernelUseconds usec
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Mutex to lock |
| `usec` | Time to wait if a lock is not immediately possible (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error or for a timeout.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `mutex` is invalid  \* SLV detection target error |
| Cannot lock because the calling thread priority is higher than the ceiling value (only when the specified mutex has a priority protection attribute)  \* SLV detection target error |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | The maximum number for recursive locks has already been reached (only when the specified mutex has a recursive lock attribute) |
| `SCE_KERNEL_ERROR_EDEADLK` | 0x8002000b | Calling thread already locks the specified mutex (only when the specified mutex does not have a recursive lock attribute) |

## Description

This function locks the mutex specified with `mutex`. If the specified mutex is already locked by another thread, this function will sleep and wait until the lock is possible, and then return after performing the lock. However, if a lock cannot be performed until the time specified with `usec` elapses, a timeout will occur.

Specification to `usec` can be made in microsecond units. However, the precision of actual processing is in millisecond units.

## Notes

If the specified mutex is already locked by another thread, `scePthreadMutexTrylock()` is provided as a function that returns an error immediately without waiting for the lock to become possible. In addition, `scePthreadMutexLock()` is provided as a function that waits infinitely without a timeout.

## See Also

`scePthreadMutexLock()`, `scePthreadMutexTrylock()`

# scePthreadMutexTrylock

Lock a mutex without blocking

## Definition

```
#include <kernel.h>
int scePthreadMutexTrylock(
    ScePthreadMutex *mutex
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Mutex to lock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `mutex` is invalid  \* SLV detection target error |
| Cannot lock because the calling thread priority is higher than the ceiling value (only when the specified mutex has a priority protection attribute)  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Already locked |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | The maximum number for recursive locks has already been reached (only when the specified mutex has a recursive lock attribute) |

## Description

This function locks the mutex specified with `mutex`. If the specified mutex is already locked, an error will be returned without blocking.

## Notes

If the specified mutex is already locked by another thread, `scePthreadMutexLock()` is provided as a function that waits for the lock to become possible. In addition, `scePthreadMutexTimedlock()` is provided as a function that waits with a timeout.

## See Also

`scePthreadMutexLock()`, `scePthreadMutexTimedlock()`

# scePthreadMutexUnlock

Unlock a mutex

## Definition

```
#include <kernel.h>
int scePthreadMutexUnlock(
    ScePthreadMutex *mutex
)
```

## Arguments

|  |  |
| --- | --- |
| `mutex` | Mutex to unlock |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `mutex` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Specified mutex is not locked by the calling thread  \* SLV detection target error |

## Description

This function unlocks the mutex specified with `mutex`.

If there is a thread waiting for a mutex, this function directly passes ownership of the mutex to the first waiting thread and then wakes that thread. Therefore, the wait for a mutex is always executed as FIFO.

## See Also

`scePthreadMutexLock()`, `scePthreadMutexTrylock()`, `scePthreadMutexTimedlock()`

# scePthreadMutexattrDestroy

Destroy a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrDestroy(
    ScePthreadMutexattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Mutex attribute object to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function destroys a mutex attribute object. Resources allocated for the mutex attribute object will be released.

## See Also

`scePthreadMutexattrInit()`

# scePthreadMutexattrGetprioceiling

Get the priority ceiling value for a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrGetprioceiling(
    ScePthreadMutexattr *attr, 
    int *prioceiling
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target mutex attribute object |
| `prioceiling` | Destination to store the obtained priority ceiling value |

## Return Values

Stores the obtained priority ceiling value in `*prioceiling` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function obtains the priority ceiling value set for the mutex attribute object specified with `attr`.

For `attr`, specify a mutex attribute object with a priority protection attribute. If this is not done, `SCE_KERNEL_ERROR_EINVAL` will be returned.

## See Also

`scePthreadMutexGetprioceiling()`

# scePthreadMutexattrGetprotocol

Get the protocol for a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrGetprotocol(
    ScePthreadMutexattr *attr, 
    int *protocol
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target mutex attribute object |
| `protocol` | Destination to store the obtained protocol |

## Return Values

Stores the obtained protocol in `*protocol` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function obtains the protocol set for the mutex attribute object specified with `attr`.

In `*protocol`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_PRIO_NONE` | 0 | Do not use priority inheritance or priority protection |
| `SCE_PTHREAD_PRIO_INHERIT` | 1 | Priority inheritance |
| `SCE_PTHREAD_PRIO_PROTECT` | 2 | Priority protection |

## See Also

`scePthreadMutexattrInit()`

# scePthreadMutexattrGettype

Get the type parameter of a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrGettype(
    ScePthreadMutexattr *attr, 
    int *type
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target mutex attribute object |
| `type` | Destination to store the obtained type parameter |

## Return Values

Stores the obtained type parameter in `*type` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function obtains the type parameter set for the mutex attribute object specified with `attr`.

In `*type`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_MUTEX_ERRORCHECK` | 1 | Perform error check (default) |
| `SCE_PTHREAD_MUTEX_RECURSIVE` | 2 | Lock recursively |
| `SCE_PTHREAD_MUTEX_NORMAL` | 3 | Do not perform error check |

## See Also

`scePthreadMutexattrInit()`, `scePthreadMutexattrSettype()`

# scePthreadMutexattrInit

Create a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrInit(
    ScePthreadMutexattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Destination to store the created mutex attribute object |

## Return Values

Stores the created mutex attribute object in `*attr` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |

## Description

This function creates a mutex attribute object and stores it in `*attr`. The required resources are allocated by the function.

A mutex attribute object is used for specifying mutex parameters for `scePthreadMutexInit()`. `scePthreadMutexattrInit()` creates a mutex attribute object with all the parameters set to the default values (`SCE_PTHREAD_MUTEX_ERRORCHECK` and `SCE_PTHREAD_PRIO_NONE`). If required, change the parameters using a function such as `scePthreadMutexattrSettype()` and pass them to `scePthreadMutexInit()`. If `scePthreadMutexInit()` returns, the mutex attribute object will no longer be needed, but it is possible to reuse it as is or change the required parameters in order to create another mutex.

Once a mutex attribute object is no longer needed, destroy it using `scePthreadMutexattrDestroy()`.

## See Also

`scePthreadMutexInit()`, `scePthreadMutexattrDestroy()`, `scePthreadMutexattrSetprioceiling()`, `scePthreadMutexattrSetprotocol()`, `scePthreadMutexattrSettype()`

# scePthreadMutexattrSetprioceiling

Set the priority ceiling value for a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrSetprioceiling(
    ScePthreadMutexattr *attr, 
    int prioceiling
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target mutex attribute object |
| `prioceiling` | Priority ceiling value to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` or `prioceiling` is invalid |

## Description

This function sets the priority ceiling value specified with `prioceiling` to the mutex attribute object specified with `attr`.

For `attr`, specify a mutex attribute object with a priority protection attribute. If this is not done, `SCE_KERNEL_ERROR_EINVAL` will be returned.

## See Also

`scePthreadMutexSetprioceiling()`

# scePthreadMutexattrSetprotocol

Set the protocol for a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrSetprotocol(
    ScePthreadMutexattr *attr, 
    int protocol
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target mutex attribute object |
| `protocol` | Protocol to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` or `protocol` is invalid |

## Description

This function sets the protocol specified with `protocol` to the mutex attribute object specified with `attr`.

Consider the following situation: Two threads with different priorities are using the same mutex to perform mutual exclusion. While the thread with lower priority has locked the mutex, the execution of the thread is blocked by yet another thread. If this occurs and the thread from the original pair that has higher priority attempts to lock the mutex, it will be unable to obtain the mutex and will be forced to wait because the thread with lower priority has ownership over the mutex. This situation is called "priority inversion". Priority inversion can be suppressed by selecting the appropriate protocol for the mutex.

For `protocol`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_PRIO_NONE` | 0 | Do not use priority inheritance or priority protection  Mutex locking and waiting have no effect on thread priority. |
| `SCE_PTHREAD_PRIO_INHERIT` | 1 | Priority inheritance  A thread that is locking the mutex will be executed with whichever of the following priorities is higher: the thread's own priority or the highest priority of all threads that are waiting for the mutex in question.  If a thread that has had its priority raised due to priority inheritance waits for another mutex, the effect of the inheritance will be applied recursively. |
| `SCE_PTHREAD_PRIO_PROTECT` | 2 | Priority protection  A thread that is locking the mutex will be executed with whichever of the following priorities is higher: the thread's own priority or the highest priority ceiling value that has been set for any of the mutexes that the thread is locking. |

## Notes

In general, the processing speed of mutex locking and unlocking operations will tend to be slower if `SCE_PTHREAD_PRIO_INHERIT` or `SCE_PTHREAD_PRIO_PROTECT` is set, compared to if `SCE_PTHREAD_PRIO_NONE` is set. The reason for this is that more processing, such as checking and modifying thread priority, must be performed within functions.

## See Also

`scePthreadMutexattrInit()`, `scePthreadMutexSetprioceiling()`

# scePthreadMutexattrSettype

Set the type parameter of a mutex attribute object

## Definition

```
#include <kernel.h>
int scePthreadMutexattrSettype(
    ScePthreadMutexattr *attr, 
    int type
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Target mutex attribute object |
| `type` | Type parameter to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` or `type` is invalid |

## Description

This function sets the value specified with `type` to the type parameter of the mutex attribute object specified with `attr`.

For `type`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_MUTEX_ERRORCHECK` | 1 | Perform error check (default) |
| `SCE_PTHREAD_MUTEX_RECURSIVE` | 2 | Lock recursively |
| `SCE_PTHREAD_MUTEX_NORMAL` | 3 | Do not perform error check |

## See Also

`scePthreadMutexattrInit()`, `scePthreadMutexattrGettype()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.