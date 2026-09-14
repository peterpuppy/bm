# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-pthread-barrier-init.html

# Barriers

# scePthreadBarrierDestroy

Destroy a barrier

## Definition

```
#include <kernel.h>
int scePthreadBarrierDestroy(
    ScePthreadBarrier *barrier
)
```

## Arguments

|  |  |
| --- | --- |
| `barrier` | Barrier to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Attempted to destroy a barrier in use  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `barrier` is invalid  \* SLV detection target error |

## Description

This function destroys the barrier specified with `barrier`. Resources allocated for the barrier will be released.

The behavior of this function is undefined when an invalid value is specified for `barrier`. However, `SCE_KERNEL_ERROR_EINVAL` may return for specific invalid values.

## See Also

`scePthreadBarrierInit()`

# scePthreadBarrierInit

Create a barrier

## Definition

```
#include <kernel.h>
int scePthreadBarrierInit(
    ScePthreadBarrier *barrier, 
    const ScePthreadBarrierattr *attr, 
    unsigned count,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `barrier` | Destination to store the created barrier |
| `attr` | Barrier attributes, or NULL |
| `count` | Number of threads required to release the barrier (specify 1 or more) |
| `name` | Barrier name (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Stores the created barrier in `*barrier` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Non-memory resources are insufficient |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The `count` value is less than 1 |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |

## Description

This function creates and initializes a barrier. The required resources are allocated by the function.

For `barrier`, specify the variable for receiving the created barrier.

For `attr`, specify the barrier attribute object that has the attributes set for assigning to the barrier. When NULL is specified for `attr`, the default attributes will be assigned.

For `count`, specify the number of threads required to release the barrier. Each thread will wait by calling `scePthreadBarrierWait()`, and when the number of threads that called `scePthreadBarrierWait()` reaches `count`, the barrier will be released, and the threads that were waiting can resume execution.

For *`name`*, specify the name to assign to the barrier. A name up to 32 bytes including the NULL-terminator character can be specified. When NULL is specified for `name`, a barrier without a name will be created.

## See Also

`scePthreadBarrierattrInit()`, `scePthreadBarrierWait()`

# scePthreadBarrierWait

Wait for barrier release

## Definition

```
#include <kernel.h>
int scePthreadBarrierWait(
    ScePthreadBarrier *barrier
)
```

## Arguments

|  |  |
| --- | --- |
| `barrier` | Barrier to wait for |

## Return Values

For normal termination, returns `SCE_OK` (=0) to all but the final thread, and returns `SCE_PTHREAD_BARRIER_SERIAL_THREAD` to the final thread.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `barrier` is invalid  \* SLV detection target error |

## Description

This function waits until the barrier specified with `barrier` is released. A barrier is released by calling this function the same number of times as the number of threads set in advance when creating the barrier (the number specified with the argument `count` when calling `scePthreadBarrierInit()`).

When a barrier is released it will be reset, and until this function is called again by the specified number of threads, the barrier will cause the threads that called this function to wait.

## See Also

`scePthreadBarrierInit()`

# scePthreadBarrierattrDestroy

Destroy a barrier attribute object

## Definition

```
#include <kernel.h>
int scePthreadBarrierattrDestroy(
    ScePthreadBarrierattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Barrier attribute object to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Value specified for `attr` is invalid |

## Description

This function destroys the barrier attribute object specified with `attr`. Resources allocated for the barrier attribute object will be released.

## See Also

`scePthreadBarrierattrInit()`

# scePthreadBarrierattrInit

Create a barrier attribute object

## Definition

```
#include <kernel.h>
int scePthreadBarrierattrInit(
    ScePthreadBarrierattr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Destination to store the created barrier attribute object |

## Return Values

Stores the created barrier attribute object in `*attr` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |

## Description

This function creates a barrier attribute object and stores it in `*attr`. The required resources are allocated by the function.

A barrier attribute object is used for passing barrier supplementary parameters to `scePthreadBarrierInit()`. This function creates a barrier attribute object with the default values set for all parameters. It is possible to repeatedly use a single barrier attribute object to create multiple barriers. Once a barrier attribute object is no longer needed, destroy it using `scePthreadBarrierattrDestroy()`.

## See Also

`scePthreadBarrierInit()`, `scePthreadBarrierattrDestroy()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.