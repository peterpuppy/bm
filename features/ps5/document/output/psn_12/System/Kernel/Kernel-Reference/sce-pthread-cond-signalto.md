# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-pthread-cond-signalto.html

# Condition Variables

# scePthreadCondBroadcast

Wake up all threads that are waiting for a condition variable

## Definition

```
#include <kernel.h>
int scePthreadCondBroadcast(
    ScePthreadCond *cond
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Target condition variable |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `cond` is invalid  \* SLV detection target error |

## Description

This function wakes up all threads that are waiting for the condition variable specified with `cond`.

## Notes

`scePthreadCondSignal()` is provided as a function that wakes up one of the threads from among the threads waiting for the specified condition variable. In addition, `scePthreadCondSignalto()` is provided as a function that wakes up the specified thread.

## See Also

`scePthreadCondSignal()`, `scePthreadCondSignalto()`

# scePthreadCondDestroy

Destroy a condition variable

## Definition

```
#include <kernel.h>
int scePthreadCondDestroy(
    ScePthreadCond *cond
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Condition variable to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `cond` is invalid  \* SLV detection target error |

## Description

This function destroys the condition variable specified with `cond`. Resources allocated for the condition variable will be released.

## See Also

`scePthreadCondInit()`

# scePthreadCondInit

Create a condition variable

## Definition

```
#include <kernel.h>
int scePthreadCondInit(
    ScePthreadCond *cond, 
    const ScePthreadCondattr *attr,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Destination to store the created condition variable |
| `attr` | Condition variable attributes, or NULL |
| `name` | Condition variable name (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Stores the created condition variable in `*cond` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Temporarily insufficient resources |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |

## Description

This function creates and initializes a new condition variable. The required resources are allocated by the function.

For `attr`, specify the condition variable attribute object that has the attributes set for assigning to the condition variable to be created. When NULL is specified for `attr`, the default attributes will be assigned.

For `name`, specify the name to assign to the condition variable to be created. A name up to 32 bytes including the NULL-terminator character can be specified. When NULL is specified for `name`, a condition variable without a name will be created.

A condition variable is used for synchronization between threads. It is possible to perform synchronization processing where a thread is waiting for a condition variable and another thread sends a signal to the condition variable. The waiting thread will then restart execution.

## Notes

A condition variable is a resource shared between threads, and functions that wait for a condition variable (`scePthreadCondTimedwait()`, `scePthreadCondWait()`) contain exclusive control that uses a mutex. Because of this, the application is required to manage condition variables and mutexes in pairs.

## See Also

`scePthreadCondBroadcast()`, `scePthreadCondDestroy()`, `scePthreadCondSignal()`, `scePthreadCondSignalto()`, `scePthreadCondTimedwait()`, `scePthreadCondWait()`

# scePthreadCondSignal

Wake up a thread that is waiting for a condition variable

## Definition

```
#include <kernel.h>
int scePthreadCondSignal(
    ScePthreadCond *cond
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Target condition variable |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `cond` is invalid  \* SLV detection target error |

## Description

This function sends a signal to the condition variable specified with `cond` and wakes up the thread waiting for this condition variable.

## Notes

`scePthreadCondSignalto()` is provided as a function that wakes up the specified thread. In addition, `scePthreadCondBroadcast()` is provided as a function that wakes up all the threads waiting for the specified condition variable.

## See Also

`scePthreadCondBroadcast()`, `scePthreadCondSignalto()`

# scePthreadCondSignalto

Wake up a specific thread that is waiting for a condition variable

## Definition

```
#include <kernel.h>
int scePthreadCondSignalto(
    ScePthreadCond *cond,
    ScePthread thread
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Target condition variable |
| `thread` | Thread to wake up |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread does not exist |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `cond` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Specified thread is not waiting for the specified condition variable |

## Description

This function wakes up the thread specified with `thread` from among the threads waiting for the condition variable specified with `cond`. An error will be returned if the specified thread is not currently waiting for the specified condition variable.

## Notes

`scePthreadCondBroadcast()` is provided as a function that wakes up all the threads waiting for the specified condition variable. In addition, `scePthreadCondSignal()` is provided as a function that signals one of the threads by just specifying a condition variable.

## See Also

`scePthreadCondBroadcast()`, `scePthreadCondSignal()`

# scePthreadCondTimedwait

Wait for a condition variable (with timeout)

## Definition

```
#include <kernel.h>
int scePthreadCondTimedwait(
    ScePthreadCond *cond, 
    ScePthreadMutex *mutex, 
    SceKernelUseconds usec
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Target condition variable |
| `mutex` | Mutex to be paired with the condition variable (this mutex must be locked) |
| `usec` | Time to wait (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error or for a timeout.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `cond` or `mutex` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Mutex is not locked  \* SLV detection target error |

## Description

This function waits with a timeout until a signal is sent from another thread to the specified condition variable.

For `cond`, specify the target condition variable. For `mutex`, lock then specify the mutex to be paired with this condition variable. The processing for unlocking the mutex is performed atomically by the function along with the blocking of the calling thread. The calling thread sleeps and waits until a signal is sent by another thread to the condition variable. When a signal is sent by `scePthreadCondBroadcast()`, `scePthreadCondSignal()`, or `scePthreadCondSignalto()`, or when the time specified with `usec` elapses, the calling thread will wake up, lock the mutex again, and return.

Specification to `usec` can be made in microsecond units. However, the precision of actual processing is in millisecond units.

## Notes

`scePthreadCondWait()` is provided as a function that waits infinitely until a signal is sent to the condition variable.

## See Also

`scePthreadCondBroadcast()`, `scePthreadCondSignal()`, `scePthreadCondSignalto()`, `scePthreadCondWait()`

# scePthreadCondWait

Wait for a condition variable

## Definition

```
#include <kernel.h>
int scePthreadCondWait(
    ScePthreadCond *cond, 
    ScePthreadMutex *mutex
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Target condition variable |
| `mutex` | Mutex to be paired with the condition variable (this mutex must be locked) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `cond` or `mutex` is invalid  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Mutex is not locked  \* SLV detection target error |

## Description

This function waits until a signal is sent from another thread to a condition variable.

For `cond`, specify the target condition variable. For `mutex`, lock then specify the mutex to be paired with this condition variable. The processing for unlocking the mutex is performed atomically by the function along with the blocking of the calling thread. The calling thread sleeps and waits until a signal is sent by another thread to the condition variable. When a signal is sent by `scePthreadCondBroadcast()`, `scePthreadCondSignal()`, or `scePthreadCondSignalto()`, the calling thread will wake up, lock the mutex again, and return.

## Notes

`scePthreadCondTimedwait()` is provided as a function that waits with a timeout until a signal is sent to the condition variable.

## See Also

`scePthreadCondBroadcast()`, `scePthreadCondSignal()`, `scePthreadCondSignalto()`, `scePthreadCondTimedwait()`

# scePthreadCondattrDestroy

Destroy a condition attribute object

## Definition

```
#include <kernel.h>
int scePthreadCondattrDestroy(
    ScePthreadCondattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Condition attribute object to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function destroys a condition attribute object. Resources allocated for the condition attribute object will be released.

## See Also

`scePthreadCondattrInit()`

# scePthreadCondattrInit

Create a condition attribute object

## Definition

```
#include <kernel.h>
int scePthreadCondattrInit(
    ScePthreadCondattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Destination to store the created condition attribute object |

## Return Values

Stores the created condition attribute object in `*attr` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |

## Description

This function creates a condition attribute object and stores it in `*attr`. The required resources are allocated by the function.

A condition attribute object is used for specifying condition variable supplementary parameters for `scePthreadCondInit()`. `scePthreadCondattrInit()` creates a condition attribute object with all parameters set to the default values. If `scePthreadCondInit()` returns, the condition attribute object will no longer be needed, but it is possible to reuse it as is or change the required parameters in order to create another condition variable.

Once a condition attribute object is no longer needed, destroy it using `scePthreadCondattrDestroy()`.

## See Also

`scePthreadCondInit()`, `scePthreadCondattrDestroy()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.