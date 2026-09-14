# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-pthread-setcancelstate.html

# Thread Management

# sceKernelGetCurrentCpu

Get CPU number

## Definition

```
#include <kernel.h>
int sceKernelGetCurrentCpu(void)
```

## Arguments

None

## Return Values

Returns the number of the CPU.

## Description

This function obtains the CPU number of the CPU executing the caller thread. The CPU number of the CPU being executed when this function is called can be obtained; note that, after the CPU number has been obtained, the caller thread may have moved to another CPU.

# sceKernelNanosleep

Put the calling thread to sleep (in nanoseconds)

## Definition

```
#include <kernel.h>
int sceKernelNanosleep(
    const SceKernelTimespec *rqtp,
    SceKernelTimespec *rmtp
)
```

## Arguments

|  |  |
| --- | --- |
| `rqtp` | Sleep time (nanoseconds, 0 to 1000000000) |
| `rmtp` | Destination to store the time the thread did not sleep, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `rqtp` or `rmtp` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `rqtp` is invalid (negative value or greater than or equal to 1 billion) |

## Description

This function interrupts processing for the specified time. If an error does not occur, the thread that called this function will be put to sleep, and this function will terminate normally when the specified time elapses.

For `rqtp`, specify the time to interrupt processing. Specification can be made in nanosecond units; however, the precision of actual processing is in units of 100 microseconds.

For `rmtp`, specify the variable for receiving the time the thread did not sleep. If receiving it is not required, specify NULL. Note that sleep will not be interrupted before the time specified in `rqtp` passes, and a meaningful value will never be stored in `*rmtp`; thus, it is recommended that NULL be specified.

## Notes

When 0 is specified for `rqtp`, this function will terminate normally without doing anything. The CPU will not be yielded to another thread.

## See Also

`sceKernelSleep()`, `sceKernelUsleep()`

# sceKernelSleep

Put the calling thread to sleep (in seconds)

## Definition

```
#include <kernel.h>
unsigned int sceKernelSleep(
    unsigned int seconds
)
```

## Arguments

|  |  |
| --- | --- |
| `seconds` | Sleep time (seconds) |

## Return Values

Returns 0.

## Description

This function interrupts processing for the specified time. The thread that called this function will be put to sleep, and this function will terminate normally when the time specified with `seconds` elapses.

## Notes

* Depending on the behavior of the system, the processing may be interrupted longer than the specified time. The longer time is undefined.
* When 0 is specified for `seconds`, this function will terminate normally without doing anything. The CPU will not be yielded to another thread.

## See Also

`sceKernelNanosleep()`, `sceKernelUsleep()`

# sceKernelUsleep

Put the calling thread to sleep (in microseconds)

## Definition

```
#include <kernel.h>
int sceKernelUsleep(
    SceKernelUseconds microseconds
)
```

## Arguments

|  |  |
| --- | --- |
| `microseconds` | Sleep time (microseconds) |

## Return Values

Returns 0.

## Description

This function interrupts processing for the specified time. The thread that called this function will be put to sleep, and this function will terminate normally when the time specified with `microseconds` elapses.

Specification to `microseconds` can be made in microsecond units. However, the precision of actual processing is in units of 100 microseconds.

## Notes

* Depending on the behavior of the system, the processing may be interrupted longer than the specified time. The longer time is undefined.
* This function is implemented using `sceKernelNanosleep()`. Therefore, sleep using sceKernelUsleep() (this function) does not affect the process time.
* When 0 is specified for `microseconds`, this function will terminate normally without doing anything. The CPU will not be yielded to another thread.

## See Also

`sceKernelNanosleep()`, `sceKernelSleep()`

# scePthreadAttrDestroy

Destroy a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrDestroy(
    ScePthreadAttr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is invalid |

## Description

This function destroys the thread attribute object specified with `attr`.

## See Also

`scePthreadAttrInit()`, `scePthreadCreate()`

# scePthreadAttrGet

Get thread attributes

## Definition

```
#include <kernel.h>
int scePthreadAttrGet(
    ScePthread thread,
    ScePthreadAttr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Thread |
| `attr` | Destination to store the obtained thread attributes |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `thread` or `attr` is invalid |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Thread corresponding to `thread` does not exist |

## Description

This function obtains the attributes of an existing thread specified with `thread`.

For `attr`, specify the thread attribute object for storing the obtained thread attributes. Allocating thread attribute objects using `scePthreadAttrInit()` is strongly recommended.

Individual attributes such as the thread priority can be obtained from the thread attribute object obtained with this function by using functions such as `scePthreadAttrGetschedparam()`.

The thread attributes do not change after creating a thread, except for the stack address.

## Examples

```
size_t 
my_thread_stack_size(ScePthread thread) 
{ 
    ScePthreadAttr attr;
    size_t size; 
 
    scePthreadAttrInit(&attr); 
    scePthreadAttrGet(thread, &attr);
    scePthreadAttrGetstacksize(&attr, &size); 
    scePthreadAttrDestroy(&attr); 
    return(size); 
}
```

## See Also

`scePthreadAttrDestroy()`, `scePthreadAttrGetdetachstate()`, `scePthreadAttrGetinheritsched()`, `scePthreadAttrGetschedparam()`, `scePthreadAttrGetschedpolicy()`, `scePthreadAttrGetstack()`, `scePthreadAttrGetstackaddr()`, `scePthreadAttrGetstacksize()`, `scePthreadAttrInit()`

# scePthreadAttrGetaffinity

Get the CPU affinity mask from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetaffinity(
    const ScePthreadAttr *pattr,
    SceKernelCpumask *mask
)
```

## Arguments

|  |  |
| --- | --- |
| `pattr` | Thread attribute object |
| `mask` | Destination to store the obtained CPU affinity mask |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `pattr` or a thread attribute object pointed to by `pattr` is NULL |

## Description

This function obtains the CPU affinity mask from a thread attribute object.

The CPU affinity mask set to the thread attribute object specified with `pattr` will be stored in `*mask`.

## See Also

`scePthreadAttrSetaffinity()`, `scePthreadGetaffinity()`

# scePthreadAttrGetdetachstate

Get the detach state from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetdetachstate(
    const ScePthreadAttr *attr,
    int *detachstate
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `detachstate` | Destination to store the obtained detach state |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `detachstate` is NULL |

## Description

This function obtains the detach state from a thread attribute object.

The detach state (the value that indicates whether thread resources are released upon thread termination or held until the thread is joined with another thread) set to the thread attribute object specified with `attr` will be stored in `*detachstate`.

## See Also

`scePthreadAttrSetdetachstate()`, `scePthreadAttrGet()`, `scePthreadJoin()`

# scePthreadAttrGetguardsize

Get the guard size from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetguardsize(
    const ScePthreadAttr *attr,
    size_t *guardSize
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `guardSize` | Destination to store the obtained guard size |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `guardSize` is NULL |

## Description

This function obtains the guard size from a thread attribute object.

The guard size (the threshold value for alerting that the remaining stack is low) set to the thread attribute object specified with `attr` will be stored in `*guardSize`.

## See Also

`scePthreadAttrSetguardsize()`, `scePthreadAttrGet()`

# scePthreadAttrGetinheritsched

Get the scheduling inheritance flag from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetinheritsched(
    const ScePthreadAttr *attr,
    int *inheritSched
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `inheritSched` | Destination to store the obtained scheduling inheritance flag |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `inheritSched` is NULL |

## Description

This function obtains the scheduling inheritance flag from a thread attribute object.

The scheduling inheritance flag (the value that indicates whether the scheduling policy and scheduling parameter are inherited from the parent thread or are explicitly set) set to the thread attribute object specified with `attr` will be stored in `*inheritSched`.

## See Also

`scePthreadAttrSetinheritsched()`, `scePthreadAttrGet()`

# scePthreadAttrGetschedparam

Get the scheduling parameter from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetschedparam(
    const ScePthreadAttr *attr,
    SceKernelSchedParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `param` | Destination to store the obtained scheduling parameter |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `param` is NULL |
| `attr` is invalid |

## Description

This function obtains the scheduling parameter from a thread attribute object.

The scheduling parameter (the thread priority) set to the thread attribute object specified with `attr` will be stored in `param->sched_priority`.

## See Also

`scePthreadAttrSetschedparam()`

# scePthreadAttrGetschedpolicy

Get the scheduling policy from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetschedpolicy(
    const ScePthreadAttr *attr,
    int *policy
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `policy` | Destination to store the obtained scheduling policy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `policy` is NULL |

## Description

This function obtains the scheduling policy from the thread attribute object specified with `attr`.

In `*policy`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_SCHED_FIFO` | 1 | Fixed-priority and FIFO (for same-priority threads) scheduling |
| `SCE_KERNEL_SCHED_RR` | 3 | Fixed-priority and round-robin (for same-priority threads) scheduling |

## See Also

`scePthreadAttrSetschedpolicy()`

# scePthreadAttrGetsolosched

Get the Solo thread attribute from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetsolosched(
    const ScePthreadAttr *attr,
    int *solosched
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `solosched` | Destination to store the obtained Solo thread attribute |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `solosched` is NULL |

## Description

This function obtains the Solo thread attribute from the thread attribute object specified with `attr`.

In `*solosched`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_SOLO_SCHED` | 0x10 | Solo thread attribute is set |
| `SCE_PTHREAD_UNSOLO_SCHED` | 0 | Solo thread attribute is not set |

## See Also

`scePthreadAttrSetsolosched()`

# scePthreadAttrGetstack

Get stack information from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetstack(
    const ScePthreadAttr * restrict attr,
    void ** restrict stackAddr,
    size_t * restrict stackSize
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `stackAddr` | Destination to store the obtained stack address |
| `stackSize` | Destination to store the obtained stack size |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr`, `stackAddr`, or `stackSize` is NULL |

## Description

This function obtains the stack information from a thread attribute object.

The stack information set to the thread attribute object specified with `attr` will be stored in `*stackAddr` and `*stackSize`.

## See Also

`scePthreadAttrSetstack()`, `scePthreadAttrSetstackaddr()`, `scePthreadAttrSetstacksize()`, `scePthreadAttrGetstackaddr()`, `scePthreadAttrGetstacksize()`, `scePthreadAttrGet()`

# scePthreadAttrGetstackaddr

Get the stack address from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetstackaddr(
    const ScePthreadAttr *attr,
    void **stackAddr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `stackAddr` | Destination to store the obtained stack address |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `stackAddr` is NULL |

## Description

This function obtains the stack information from a thread attribute object.

The stack address set to the thread attribute object specified with `attr` will be stored in `*stackAddr`.

## See Also

`scePthreadAttrSetstackaddr()`, `scePthreadAttrSetstack()`, `scePthreadAttrGetstack()`, `scePthreadAttrGetstacksize()`, `scePthreadAttrGet()`

# scePthreadAttrGetstacksize

Get the stack size from a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrGetstacksize(
    const ScePthreadAttr *attr,
    size_t *stackSize
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `stackSize` | Destination to store the obtained stack size |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `stackSize` is NULL |

## Description

This function obtains the stack information from a thread attribute object.

The stack size set to the thread attribute object specified with `attr` will be stored in `*stackSize`.

## See Also

`scePthreadAttrSetstacksize()`, `scePthreadAttrSetstack()`, `scePthreadAttrGetstack()`, `scePthreadAttrGetstackaddr()`, `scePthreadAttrGet()`

# scePthreadAttrInit

Create a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrInit(
    ScePthreadAttr *attr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Destination to store the pointer to the created thread attribute object |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |

## Description

This function creates a thread attribute object and stores its pointer in `*attr`. The kernel allocates the required memory.

A thread attribute object is used for passing thread parameters to `scePthreadCreate()`. A thread attribute object with the default values set for all parameters is created using `scePthreadAttrInit()`. If required, change the parameters using a function such as `scePthreadAttrSetstack()` and pass them to `scePthreadCreate()`. It is possible to repeatedly use a single thread attribute object to create multiple threads. Once a thread attribute object is no longer needed, destroy it using `scePthreadAttrDestroy()`.

## See Also

`scePthreadAttrGet()`, `scePthreadCreate()`

# scePthreadAttrSetaffinity

Set the CPU affinity mask to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetaffinity(
    ScePthreadAttr *pattr,
    const SceKernelCpumask mask
)
```

## Arguments

|  |  |
| --- | --- |
| `pattr` | Thread attribute object |
| `mask` | CPU affinity mask |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `pattr` or a thread attribute object pointed to by `pattr` is NULL |
| `mask` is invalid (the kernel does not support the specified CPU) |

## Description

This function sets the CPU affinity mask to a thread attribute object.

The CPU affinity mask is the information that indicates a combination of the CPUs. By specifying the CPU affinity mask (via a thread attribute object) when creating a thread, the thread will have affinity with the CPUs indicated by the CPU affinity mask, in other words it will be executed on one of those CPUs only. By setting an appropriate CPU affinity for each thread, the load balance between CPUs can be adjusted.

Specify a thread attribute object for `pattr`.

Specify the CPU affinity mask to set to the thread attribute object for `mask`. For the details of how to make these specifications, refer to the Description of `SceKernelCpumask`.

This function will return an error if a CPU not supported by the kernel is specified, but an error will not be returned if the caller process specifies a CPU that is supported by the kernel but is not permitted for usage by that process. If a thread attribute object with such a specification is passed to `scePthreadCreate()` when creating a thread, `scePthreadCreate()` will return an error.

## See Also

`scePthreadAttrGetaffinity()`, `scePthreadSetaffinity()`

# scePthreadAttrSetdetachstate

Set the detach state to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetdetachstate(
    ScePthreadAttr *attr,
    int detachstate
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `detachstate` | Detach state to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is NULL or `detachstate` is invalid |

## Description

This function sets the detach state (the timing of when to release the thread resources) to the thread attribute object specified with `attr`.

For `detachstate`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_CREATE_DETACHED` | 0x1 | Detached mode: Release resources when the thread terminates |
| `SCE_PTHREAD_CREATE_JOINABLE` | 0 | Joinable mode: Hold resources even after the thread terminates, and release when the thread is joined with another thread |

Set an appropriate detach state depending on whether or not the thread will be joined with another thread.

## See Also

`scePthreadAttrGetdetachstate()`, `scePthreadJoin()`

# scePthreadAttrSetguardsize

Set the guard size to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetguardsize(
    ScePthreadAttr *attr,
    size_t guardSize
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `guardSize` | Guard size to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is NULL |

## Description

This function sets the guard size specified with `guardSize` to the thread attribute object specified with `attr`.

The guard is a non-readable/non-writable memory area adjacent to the stack. An exception will occur if the guard is accessed due to a stack overflow.

## See Also

`scePthreadAttrGetguardsize()`

# scePthreadAttrSetinheritsched

Set the scheduling inheritance flag to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetinheritsched(
    ScePthreadAttr *attr,
    int inheritSched
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `inheritSched` | Scheduling inheritance flag to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is invalid |
| `SCE_KERNEL_ERROR_ENOTSUP` | 0x8002002d | `inheritSched` is invalid |

## Description

This function sets the scheduling inheritance flag specified with `inheritSched` to the thread attribute object specified with `attr`.

For `inheritSched`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_EXPLICIT_SCHED` | 0 | Explicit setting mode: Set the scheduling policy and scheduling parameter explicitly |
| `SCE_PTHREAD_INHERIT_SCHED` | 0x4 | Inheritance mode: Inherit the scheduling policy and scheduling parameter of the parent thread |

## See Also

`scePthreadAttrGetinheritsched()`, `scePthreadCreate()`

# scePthreadAttrSetschedparam

Set the scheduling parameter to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetschedparam(
    ScePthreadAttr *attr,
    const SceKernelSchedParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `param` | Scheduling parameter to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is invalid |
| `SCE_KERNEL_ERROR_ENOTSUP` | 0x8002002d | `param` is invalid |

## Description

This function sets the scheduling parameter (thread priority) specified with `param` to the thread attribute object specified with `attr`.

Set the thread priority to `param->sched_priority`. Smaller values represent higher priorities. The default priority is defined as `SCE_KERNEL_PRIO_FIFO_DEFAULT`. The highest priority is defined as `SCE_KERNEL_PRIO_FIFO_HIGHEST` and the lowest priority is defined as `SCE_KERNEL_PRIO_FIFO_LOWEST`.

By default, the scheduling inheritance flag of the thread attribute object is the inheritance mode. Because of this, to reflect the priority set with this function onto the thread, the scheduling inheritance flag must be changed to the explicit setting mode. More specifically, specify `SCE_PTHREAD_EXPLICIT_SCHED` with `scePthreadAttrSetinheritsched()`.

## See Also

`scePthreadAttrGetschedparam()`, `scePthreadAttrSetinheritsched()`, `scePthreadAttrSetschedpolicy()`

# scePthreadAttrSetschedpolicy

Set the scheduling policy to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetschedpolicy(
    ScePthreadAttr *attr,
    int policy
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `policy` | Scheduling policy to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is invalid |
| `SCE_KERNEL_ERROR_ENOTSUP` | 0x8002002d | `policy` is invalid |

## Description

This function sets the scheduling policy specified with `policy` to the thread attribute object specified with `attr`.

For `policy`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_SCHED_FIFO` | 1 | Fixed-priority and FIFO (for same-priority threads) scheduling |
| `SCE_KERNEL_SCHED_RR` | 3 | Fixed-priority and round-robin (for same-priority threads) scheduling |

By default, the scheduling inheritance flag of the thread attribute object is the inheritance mode. Because of this, to reflect the scheduling policy set with this function onto the thread, the scheduling inheritance flag must be changed to the explicit setting mode. More specifically, specify `SCE_PTHREAD_EXPLICIT_SCHED` with `scePthreadAttrSetinheritsched()`.

When the scheduling policy is changed with this function, the thread priority set to the thread attribute object will also be changed to the default value.

## See Also

`scePthreadAttrGetschedpolicy()`, `scePthreadAttrSetinheritsched()`, `scePthreadAttrSetschedparam()`

# scePthreadAttrSetsolosched

Set the Solo thread attribute to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetsolosched(
    ScePthreadAttr *attr,
    int solosched
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `solosched` | Solo thread attribute to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is invalid |
| `SCE_KERNEL_ERROR_ENOTSUP` | 0x8002002d | `solosched` is invalid |

## Description

This function sets the Solo thread attribute specified with `solosched` to the thread attribute object specified with `attr`.

For `solosched`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_SOLO_SCHED` | 0x10 | Set the Solo thread attribute |
| `SCE_PTHREAD_UNSOLO_SCHED` | 0 | Remove the Solo thread attribute |

By default, no Solo thread attribute is set.

## See Also

`scePthreadAttrGetsolosched()`

# scePthreadAttrSetstack

Set stack information to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetstack(
    ScePthreadAttr *attr,
    void *stackAddr,
    size_t stackSize
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `stackAddr` | Stack address to set |
| `stackSize` | Stack size to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `stackSize` is smaller than the minimum value (`SCE_PTHREAD_STACK_MIN`) |
| `attr` or `stackAddr` is NULL |

## Description

This function sets the stack information specified with `stackAddr` and `stackSize` to the thread attribute object specified with `attr`. `scePthreadCreate()` rounds up the stack size set to the thread attribute object in page units to allocate memory for stack.

## See Also

`scePthreadAttrGetstack()`, `scePthreadAttrSetstackaddr()`, `scePthreadAttrSetstacksize()`

# scePthreadAttrSetstackaddr

Set the stack address to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetstackaddr(
    ScePthreadAttr *attr,
    void *stackAddr
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `stackAddr` | Stack address to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` or `stackAddr` is NULL |

## Description

This function sets the stack address specified with `stackAddr` to the thread attribute object specified with `attr`.

## See Also

`scePthreadAttrGetstackaddr()`, `scePthreadAttrSetstack()`, `scePthreadAttrSetstacksize()`

# scePthreadAttrSetstacksize

Set the stack size to a thread attribute object

## Definition

```
#include <kernel.h>
int scePthreadAttrSetstacksize(
    ScePthreadAttr *attr,
    size_t stackSize
)
```

## Arguments

|  |  |
| --- | --- |
| `attr` | Thread attribute object |
| `stackSize` | Stack size to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `stackSize` is smaller than the minimum value (`SCE_PTHREAD_STACK_MIN`) |

## Description

This function sets the stack size specified with `stackSize` to the thread attribute object specified with `attr`. `scePthreadCreate()` rounds up the stack size set to the thread attribute object in page units to allocate memory for stack.

## See Also

`scePthreadAttrGetstacksize()`, `scePthreadAttrSetstack()`, `scePthreadAttrSetstackaddr()`

# scePthreadCancel

Make a request to terminate another thread

## Definition

```
#include <kernel.h>
int scePthreadCancel(
    ScePthread thread
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Thread to terminate |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `thread` is NULL |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread does not exist |

## Description

This function makes a request to terminate the thread specified with `thread`.

When the specified thread is actually terminated depends on the cancel state and cancel type of the thread. It will not be synchronized with a return from this function.

## Notes

* When a terminated thread is joined, `SCE_PTHREAD_CANCELED` will be returned. The type of this value is (void \*), not NULL and it does not point to any object.
* When a thread terminates, the cleanup handlers of the thread will be called one after another. When the final cleanup handler returns, the destructors for the thread-specific data will be called one after another, and when the final destructor returns, the thread will be destroyed.

## See Also

`scePthreadCleanupPop()`, `scePthreadCleanupPush()`, `scePthreadExit()`, `scePthreadJoin()`, `scePthreadSetcancelstate()`, `scePthreadSetcanceltype()`, `scePthreadTestcancel()`

# scePthreadCleanupPop

Delete a cleanup handler

## Definition

```
#include <kernel.h>
void scePthreadCleanupPop(
    int execute
)
```

## Arguments

|  |  |
| --- | --- |
| `execute` | Whether or not to execute the cleanup handler |

## Return Values

None

## Description

This function deletes a cleanup handler from a stack.

If true (non-zero) is specified for `execute`, the cleanup handler at the top of the cleanup handler stack will be executed and deleted from the stack. If false (zero) is specified for `execute`, the cleanup handler at the top of the stack will be deleted from the stack without being executed.

If the cleanup handler stack is empty, this function will return without doing anything.

## See Also

`scePthreadCleanupPush()`, `scePthreadExit()`

# scePthreadCleanupPush

Register a cleanup handler

## Definition

```
#include <kernel.h>
void scePthreadCleanupPush(
    void (*cleanup_routine)(void *), 
    void *arg
)
```

## Arguments

|  |  |
| --- | --- |
| `cleanup_routine` | Pointer to the cleanup handler |
| `arg` | User-defined argument to pass to the cleanup handler |

## Return Values

None

## Description

This function registers a cleanup handler, in other words a function that is automatically executed when a thread terminates.

For `cleanup_routine`, specify a pointer to a function that will receive (void \*) as an argument and will not return a value.

For `arg`, specify an argument to pass to this function.

Cleanup handlers are stacked in cleanup handler stacks that are exclusive to each thread. When a thread terminates, they will be executed in the order opposite of how they were registered.

## Notes

* Do not call `scePthreadExit()` in a cleanup handler.
* `scePthreadCleanupPush()` and `scePthreadCleanupPop()` are implemented as macros. Always use them in pairs within the same scope.

## See Also

`scePthreadCleanupPop()`, `scePthreadExit()`

# scePthreadCreate

Create a new thread

## Definition

```
#include <kernel.h>
int scePthreadCreate(
    ScePthread *thread, 
    const ScePthreadAttr *attr, 
    void *(*start_routine)(void *), 
    void *arg, 
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Destination to store the created thread |
| `attr` | Attributes of the created thread (or specify NULL) |
| `start_routine` | Function to start execution of the created thread |
| `arg` | Argument to pass to `start_routine` |
| `name` | Name of the created thread (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Insufficient resources or the number of threads that the process can hold has already reached the maximum (`SCE_PTHREAD_THREADS_MAX`) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `attr` is invalid |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` pointer is invalid |
| `SCE_KERNEL_ERROR_EDEADLK` | 0x8002000b | CPU affinity mask set for `attr` is invalid |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | CPU not permitted for usage is specified for CPU affinity mask set for `attr` |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |

## Description

This function creates a new thread.

For `thread`, specify the variable for receiving the created thread.

For `attr`, specify the thread attribute object for specifying the attributes of the new thread. When NULL is specified for `attr`, a thread with the default attributes will be created. If the priority and CPU affinity aren't specified in `attr`, the priority and CPU affinity of the created thread will be inherited from the thread that called this function. The thread attributes are held inside the kernel, so even if the content for the thread attribute object indicated by `attr` is overwritten after returning from this function, the thread will not be affected. In addition, it is possible to use the same thread attribute object to create other threads.

For `start_routine`, specify the first function to be called in the created thread. For `arg`, specify the argument to be passed to this function.

For `name`, specify the name of the created thread. A name up to 32 bytes including the NULL-terminator character can be specified. If NULL is specified to `name`, the default name will be applied. Because the name will be copied to a system area, the memory pointed to by `name` can be freed after thread creation.

## Notes

When the created thread returns from `start_routine` it will terminate, and the value that the `start_routine` return value will be the thread termination status. This is the same operation as when `scePthreadExit()` is called with the `start_routine` return value as an argument.

## See Also

`scePthreadCleanupPop()`, `scePthreadCleanupPush()`, `scePthreadExit()`, `scePthreadJoin()`

# scePthreadDetach

Detach a thread

## Definition

```
#include <kernel.h>
int scePthreadDetach(
    ScePthread thread
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Thread to detach |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `thread` is not a joinable thread |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread does not exist |

## Description

This function changes a joinable mode thread to detached mode. The resources of a joinable mode thread are saved even after termination and until the thread is joined with another thread, but the resources of a detached mode thread are released upon termination.

## Notes

* The specified thread will not be terminated by calling this function.
* The operation is undefined when the same thread is specified and this function is called multiple times.

## See Also

`scePthreadAttrSetdetachstate()`, `scePthreadJoin()`

# scePthreadEqual

Compare threads

## Definition

```
#include <kernel.h>
int scePthreadEqual(
    ScePthread thread1, 
    ScePthread thread2
)
```

## Arguments

|  |  |
| --- | --- |
| `thread1` | Thread to compare |
| `thread2` | Thread to compare |

## Return Values

Returns true (non-zero) if `thread1` and `thread2` are the same thread. Returns false (zero) if they are different.

## Description

This function compares threads.

# scePthreadExit

Terminate the calling thread

## Definition

```
#include <kernel.h>
void scePthreadExit(
    void *value_ptr
)
```

## Arguments

|  |  |
| --- | --- |
| `value_ptr` | Pointer to the value to be passed to the thread that will join |

## Return Values

None (because this function does not return)

## Description

This function terminates the calling thread.

For `value_ptr`, specify a pointer to the value to be passed when `scePthreadJoin()` is called for this thread. However, a pointer to a local variable (auto variable) of this thread should not be specified. This is because local variable values will become undefined after a thread terminates.

For the thread termination processing, the cleanup handlers registered to the stack are executed one after another in the order opposite of how they were registered. Then, if the thread holds thread-specific data, the appropriate destructors are called. The order in which the destructors are called is undefined.

When terminating a thread, process resources such as mutexes and file descriptors are not released. In addition, cleanup processing at the process level such as the calling of a termination function registered with `atexit()` will not be performed. If such processing is required, explicitly perform it before calling `scePthreadExit()`.

When a thread other than the main thread (the thread that first called `main()` after a process was created) returns from its start routine (the function that was first called after a thread was created), `scePthreadExit()` will be implicitly called. The value returned by the start routine will be the thread termination status.

When all threads in a process have terminated, the process will terminate at termination status 0, the same as when `exit(0)` is called.

The operation is undefined when this function is called in a cleanup handler or destructor that was called when this function is explicitly or implicitly called.

## Notes

Voluntary process termination by an application is prohibited by TRC [R5093](../../../TRC/latest/TRC/R5093.html).

## See Also

`scePthreadJoin()`

# scePthreadGetaffinity

Get the CPU affinity of a thread

## Definition

```
#include <kernel.h>
int scePthreadGetaffinity(
    ScePthread thread, 
    SceKernelCpumask *mask
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread |
| `mask` | Destination to store the obtained CPU affinity mask |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread could not be found |

## Description

This function obtains the CPU affinity of a thread, in other words the information that indicates which CPU(s) the thread will be executed on.

The CPU affinity mask of the thread specified for `thread` will be stored in `*mask`.

## See Also

`scePthreadSetaffinity()`, `scePthreadAttrGetaffinity()`

# scePthreadGetthreadid

Get the thread ID

## Definition

```
#include <kernel.h>
int scePthreadGetthreadid(void)
```

## Arguments

None

## Return Values

Returns the thread ID.

## Description

This function obtains the thread ID for the thread that called this function. A thread ID is a thread identifier used in the debugger, Razor CPU, etc., and is different from the `ScePthread` type values for handling threads in programs.

## See Also

`scePthreadCreate()`

# scePthreadGetname

Get thread name

## Definition

```
#include <kernel.h>
int scePthreadGetname(
    ScePthread thread, 
    char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Thread to obtain the name of |
| `name` | Destination to store the obtained name |

## Return Values

Stores the name in `*name` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Thread corresponding to `thread` does not exist |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |

## Description

This function obtains the name of the thread set with `scePthreadCreate()` and `scePthreadRename()`. For `*name`, a character string up to 32 bytes including the NULL-terminator character will be stored.

# scePthreadGetprio

Get thread priority

## Definition

```
#include <kernel.h>
int scePthreadGetprio(
    ScePthread thread,
    int *prio
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread |
| `prio` | Destination to store the obtained priority |

## Return Values

Stores the priority in `*prio` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread could not be found |

## Description

This function obtains the priority of the specified thread.

## See Also

`scePthreadGetschedparam()`, `scePthreadSetprio()`

# scePthreadGetschedparam

Get the scheduling policy and priority of a thread

## Definition

```
#include <kernel.h>
int scePthreadGetschedparam(
    ScePthread thread, 
    int *policy, 
    SceKernelSchedParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread |
| `policy` | Destination to store the obtained scheduling policy |
| `param` | Destination to store the obtained scheduling parameter (priority) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread could not be found |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `policy` or `param` is NULL |

## Description

This function obtains the scheduling policy and priority of an existing thread.

For normal termination, one of the following values that indicate the scheduling policy will be stored in `*policy`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_SCHED_FIFO` | 1 | Fixed-priority and FIFO (for same-priority threads) scheduling |
| `SCE_KERNEL_SCHED_RR` | 3 | Fixed-priority and round-robin (for same-priority threads) scheduling |

In addition, the thread priority will be stored in `param->sched_priority`.

## See Also

`scePthreadAttrGetschedparam()`, `scePthreadAttrGetschedpolicy()`

# scePthreadGetspecific

Get thread-specific data

## Definition

```
#include <kernel.h>
void * scePthreadGetspecific(
    ScePthreadKey key
)
```

## Arguments

|  |  |
| --- | --- |
| `key` | Key for thread-specific data |

## Return Values

Returns the value of the thread-specific data associated with `key`. Returns NULL if the corresponding thread-specific data does not exist (or has not been saved).

## Description

This function obtains a value associated with a key specified with `key` from among the specific data of the calling thread.

The value to be specified to `key` must be a key value that was obtained with `scePthreadKeyCreate()`. The operation is undefined when other values are specified. The operation is also undefined when a specified key value has already been deleted with `scePthreadKeyDelete()`.

Calling this function from a thread-specific data destructor will not cause any problems.

## See Also

`scePthreadKeyCreate()`, `scePthreadKeyDelete()`, `scePthreadSetspecific()`

# scePthreadJoin

Wait for another thread to terminate

## Definition

```
#include <kernel.h>
int scePthreadJoin(
    ScePthread thread, 
    void **value_ptr
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread to wait for |
| `value_ptr` | Destination to store the termination status of the target thread (specify NULL if not required) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `thread` is not a joinable thread |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread could not be found |
| `SCE_KERNEL_ERROR_EDEADLK` | 0x8002000b | A deadlock has occurred, or `thread` is the calling thread |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | Another thread is already waiting for the same target thread |

## Description

This function waits until the specified thread has terminated and receives the termination status of the thread. "Join" in the function name refers to the joining of process flows that were in two separate threads. Calling this function to merge with another thread is simply called "joining".

The thread that called this function will be in a wait state until the thread specified with `thread` terminates. When the thread terminates, this function will return. However, if the target thread has already terminated when this function is called, this function will return immediately without the calling thread going into a wait state. When this function returns without an error, the termination status passed to `scePthreadExit()` by the target thread will be stored in `*value_ptr`. If receiving the termination status is not required, specify NULL to `value_ptr`.

The operation is undefined when multiple threads call this function with the same target thread at the same time.

## Notes

* Joinable threads will remain in the system even after they terminate until they are joined, and they will be detached by being joined. The maximum number of threads defined with `SCE_PTHREAD_THREADS_MAX` is the maximum number including these threads that have terminated but have not been joined.
* If a thread that called this function terminates, the target thread will remain without being detached.

## See Also

`scePthreadCreate()`, `scePthreadAttrSetdetachstate()`

# scePthreadKeyCreate

Create a key for thread-specific data

## Definition

```
#include <kernel.h>
int scePthreadKeyCreate(
    ScePthreadKey *key, 
    void (*destructor)(void *)
)
```

## Arguments

|  |  |
| --- | --- |
| `key` | Destination to store the created key |
| `destructor` | Destructor for the data associated with the key (specify NULL if not required) |

## Return Values

Stores the created key in `*key` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Insufficient resources or the number of keys has already reached the maximum (`SCE_PTHREAD_KEYS_MAX`) |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |

## Description

This function creates a key for thread-specific data.

A key created with this function can be associated with a value by using `scePthreadSetspecific()`. The associated value can be obtained by using `scePthreadGetspecific()`. A key can be shared by each thread in a process, but even if the same key is used a value will be independently managed by each thread, and only the value associated by the calling thread (or the initial value, NULL) can be obtained.

When a key is created, NULL will be associated with the key for the specific data of all threads that are active at that time. When a thread is created, thread-specific data will be created with NULL associated with all keys that have been created at that time.

For `destructor`, specify the destructor for the thread-specific data. (Specify NULL if a destructor is not required.) If the value associated with this key is not NULL at the time of thread termination, the destructor will be called with this value as an argument. With the destructor, release the resources allocated relating to this key. Once the release completes, associate NULL with this key and return from the destructor.

However, when multiple destructors are called, the calling order is not fixed. Therefore, it may not be possible to release resources because of dependencies. In such cases, return from the destructor without releasing resources and associating NULL with the key. After all destructors have been called, if non-NULL thread-specific data remains, the destructor will be called for that data again. This operation will be repeated for at least the number of times defined in `SCE_PTHREAD_DESTRUCTOR_ITERATIONS`, so release the resources in the meantime.

## See Also

`scePthreadGetspecific()`, `scePthreadKeyDelete()`, `scePthreadSetspecific()`

# scePthreadKeyDelete

Delete a key for thread-specific data

## Definition

```
#include <kernel.h>
int scePthreadKeyDelete(
    ScePthreadKey key
)
```

## Arguments

|  |  |
| --- | --- |
| `key` | Key to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `key` is invalid |

## Description

This function deletes a key for thread-specific data. When attempting to access thread-specific data using a key after the key is deleted, the result will be undefined. In addition, the destructor corresponding to this key will no longer be called when the thread terminates.

The deletion of a key and the release of resources allocated relating to the key are separate. When deleting a key, there will be no problems if the key is associated with a value, and the corresponding destructor will not be called even if specified. The release of all resources (for all threads) related to a deleted key is the responsibility of the application, but both releasing resources before deleting a key and releasing resources after deleting a key are possible. It is also possible to delete a key by calling this function from a thread-specific data destructor.

## See Also

`scePthreadGetspecific()`, `scePthreadKeyCreate()`, `scePthreadSetspecific()`

# scePthreadOnce

Call an initialization function once

## Definition

```
#include <kernel.h>
ScePthreadOnce once_control = SCE_PTHREAD_ONCE_INIT;

int scePthreadOnce(
    ScePthreadOnce *once_control, 
    void (*init_routine)(void)
)
```

## Arguments

|  |  |
| --- | --- |
| `once_control` | Flag for controlling whether or not initialization is already performed |
| `init_routine` | Function that performs initialization |

## Return Values

Returns 0.

## Description

This function performs control so that a function is called only once in a process.

For `once_control`, specify a pointer to the static variable initialized with `SCE_PTHREAD_ONCE_INIT`. If a variable not initialized with `SCE_PTHREAD_ONCE_INIT` or an automatic variable is specified, or if the same variable is not specified to each thread, the operation is not guaranteed.

For `init_routine()`, specify the function that you want to call only once. When returning from `scePthreadOnce()`, the execution of the function specified for `init_routine()` will be guaranteed to be complete.

If a thread is terminated using `scePthreadCancel()` during execution of an initialization function specified for `init_routine()`, the `once_control` value will remain `SCE_PTHREAD_ONCE_INIT`.

# scePthreadRename

Rename a thread

## Definition

```
#include <kernel.h>
int scePthreadRename(
    ScePthread thread, 
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Thread to rename |
| `name` | New name (up to 32 bytes including the NULL-terminator character), or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Thread corresponding to `thread` does not exist |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory |

## Description

This function changes the name of a thread.

By specifying NULL for `name`, the thread will be changed to have no name.

# scePthreadSelf

Get the object of the calling thread

## Definition

```
#include <kernel.h>
ScePthread scePthreadSelf(void)
```

## Arguments

None

## Return Values

Returns the thread object.

## Description

This function obtains the object (`ScePthread` type value) of the thread that called this function.

## See Also

`scePthreadEqual()`

# scePthreadSetaffinity

Set the CPU affinity to a thread

## Definition

```
#include <kernel.h>
int scePthreadSetaffinity(
    ScePthread thread, 
    const SceKernelCpumask mask
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread |
| `mask` | CPU affinity mask to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Thread specified for `thread` could not be found |
| `SCE_KERNEL_ERROR_EDEADLK` | 0x8002000b | CPU affinity mask specified for `mask` is invalid |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | CPU not permitted for usage is specified for CPU affinity mask specified for `mask` |

## Description

This function sets/changes the CPU affinity of a thread, in other words the information that indicates which CPU(s) the thread will be executed on.

For `thread`, specify the target thread.

For `mask`, specify the CPU affinity mask that indicates the combination of CPUs on which the target thread is to be executed. For the details of how to make these specifications, refer to the Description of `SceKernelCpumask`.

After this function terminates normally, the thread will have affinity with the CPUs specified in the CPU affinity mask, in other words it will be executed on one of these CPUs only. By specifying an appropriate CPU affinity for each thread, the load balance can be adjusted.

## See Also

`scePthreadAttrSetaffinity()`, `scePthreadGetaffinity()`

# scePthreadSetcancelstate

Set the cancel state

## Definition

```
#include <kernel.h>
int scePthreadSetcancelstate(
    int state, 
    int *oldState
)
```

## Arguments

|  |  |
| --- | --- |
| `state` | Cancel state to newly set |
| `oldState` | Destination to store the previous cancel state (specify NULL if not required) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `state` is invalid |

## Description

This function sets the cancel state, in other words whether to accept or hold a request when a termination request has been made by another thread with `scePthreadCancel()`.

For `state`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_CANCEL_ENABLE` | 0 | Accept the termination request |
| `SCE_PTHREAD_CANCEL_DISABLE` | 1 | Hold the termination request |

For `oldState`, specify a pointer to the variable for receiving the cancel state before calling this function to change the state. If receiving it is not required, specify NULL.

The initial value for the cancel state (the value when a thread is created) is `SCE_PTHREAD_CANCEL_ENABLE`. This is also the same for the main thread (the thread that first called `main()`).

The behavior of a thread when termination is requested depends on the cancel type as well as the cancel state. For details, refer to `scePthreadSetcanceltype()`.

## Notes

Adhere to the following principles in order to properly handle cancellations.

* Set the cancel state to `SCE_PTHREAD_CANCEL_DISABLE` when making entries in objects. Do not set `SCE_PTHREAD_CANCEL_ENABLE` in an object. Reset the cancel state to the previous state when returning.
* The cancel type can be either `SCE_PTHREAD_CANCEL_DEFERRED` or `SCE_PTHREAD_CANCEL_ASYNCHRONOUS`. However, reset it to the previous type when returning.
* Call only cancel-safe functions from `SCE_PTHREAD_CANCEL_ASYNCHRONOUS` threads.

## See Also

`scePthreadSetcanceltype()`, `scePthreadCancel()`

# scePthreadSetcanceltype

Set the cancel type

## Definition

```
#include <kernel.h>
int scePthreadSetcanceltype(
    int type, 
    int *oldType
)
```

## Arguments

|  |  |
| --- | --- |
| `type` | Cancel type to newly set |
| `oldType` | Destination to store the previous cancel type (specify NULL if not required) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `type` is invalid |

## Description

This function sets the cancel type, in other words the termination timing for when a termination request has been made by another thread with `scePthreadCancel()`.

For `type`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PTHREAD_CANCEL_DEFERRED` | 0 | Continue processing and terminate when the cancel point has been reached |
| `SCE_PTHREAD_CANCEL_ASYNCHRONOUS` | 2 | Terminate immediately upon termination request |

A cancel point refers to the point where a specific function such as `scePthreadTestcancel()` is called in a program. For details, refer to `scePthreadTestcancel()`.

No matter the cancel type, a received termination request is held when the cancel state is `SCE_PTHREAD_CANCEL_DISABLE`. When the cancel state is changed to `SCE_PTHREAD_CANCEL_ENABLE`, processing will be performed depending on the cancel type.

For `oldType`, specify a pointer to the variable for receiving the cancel type before calling this function to change the type. If receiving it is not required, specify NULL.

The initial value for the cancel type (the value when a thread is created) is `SCE_PTHREAD_CANCEL_DEFERRED`. This is also the same for the main thread (the thread that first called `main()`).

## Notes

Adhere to the following principles in order to properly handle cancellations.

* Set the cancel state to `SCE_PTHREAD_CANCEL_DISABLE` when making entries in objects. Do not set `SCE_PTHREAD_CANCEL_ENABLE` in an object. Reset the cancel state to the previous state when returning.
* The cancel type can be either `SCE_PTHREAD_CANCEL_DEFERRED` or `SCE_PTHREAD_CANCEL_ASYNCHRONOUS`. However, reset it to the previous type when returning.
* Call only cancel-safe functions from `SCE_PTHREAD_CANCEL_ASYNCHRONOUS` threads.

## See Also

`scePthreadSetcancelstate()`, `scePthreadTestcancel()`, `scePthreadCancel()`

# scePthreadSetprio

Set thread priority

## Definition

```
#include <kernel.h>
int scePthreadSetprio(
    ScePthread thread,
    int prio
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread |
| `prio` | Priority to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread could not be found |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified priority is outside the valid range |

## Description

This function sets/changes the priority of a thread. It differs from `scePthreadSetschedparam()` since it does not change the scheduling policy.

For `prio`, specify the priority to set. Smaller values represent higher priorities. The default priority is defined as `SCE_KERNEL_PRIO_FIFO_DEFAULT`. The highest priority is defined as `SCE_KERNEL_PRIO_FIFO_HIGHEST` and the lowest priority is defined as `SCE_KERNEL_PRIO_FIFO_LOWEST`.

## Notes

`scePthreadSetschedparam()` is provided as a function for setting the scheduling policy and priority.

## See Also

`scePthreadSetschedparam()`, `scePthreadGetprio()`

# scePthreadSetschedparam

Set the scheduling policy and priority for a thread

## Definition

```
#include <kernel.h>
int scePthreadSetschedparam(
    ScePthread thread, 
    int policy, 
    const SceKernelSchedParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `thread` | Target thread |
| `policy` | Scheduling policy to set |
| `param` | Scheduling parameter (priority) to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `policy` is invalid |
| One of the `param` members is invalid |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified thread could not be found |

## Description

This function changes the scheduling policy and priority of an existing thread.

For `policy`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_SCHED_FIFO` | 1 | Fixed-priority and FIFO (for same-priority threads) scheduling |
| `SCE_KERNEL_SCHED_RR` | 3 | Fixed-priority and round-robin (for same-priority threads) scheduling |

Set the thread priority to `param->sched_priority`. Smaller values represent higher priorities. The default priority is defined as `SCE_KERNEL_PRIO_FIFO_DEFAULT`. The highest priority is defined as `SCE_KERNEL_PRIO_FIFO_HIGHEST` and the lowest priority is defined as `SCE_KERNEL_PRIO_FIFO_LOWEST`.

## See Also

`scePthreadAttrSetschedparam()`, `scePthreadAttrSetschedpolicy()`

# scePthreadSetspecific

Set a value for thread-specific data

## Definition

```
#include <kernel.h>
int scePthreadSetspecific(
    ScePthreadKey key, 
    const void *value
)
```

## Arguments

|  |  |
| --- | --- |
| `key` | Key for thread-specific data |
| `value` | Value to associate with `key` |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `key` is invalid |

## Description

This function associates a value with a key for thread-specific data.

For `key`, specify a key created using `scePthreadKeyCreate()`.

For `value`, specify the value to be associated. Typically, place the data in dynamically allocated memory, and specify the address of this memory to `value`.

A key can be shared with other threads. Even if the key is the same, if the threads are different the data will be managed as separate data. If a key value that is not created with `scePthreadKeyCreate()` is specified to `key` or if a key that was already deleted with `scePthreadKeyDelete()` is specified, the operation will be undefined.

It is also possible to call this function from a thread-specific data destructor. However, there is a risk of data being lost or falling into an infinite loop.

## See Also

`scePthreadGetspecific()`, `scePthreadKeyCreate()`, `scePthreadKeyDelete()`

# scePthreadTestcancel

Check if a termination request is being received

## Definition

```
#include <kernel.h>
void scePthreadTestcancel(void)
```

## Arguments

None

## Return Values

None

## Description

This function checks whether or not a termination request from another thread using `scePthreadCancel()` is being received, and if there is a termination request and the cancel state is `SCE_PTHREAD_CANCEL_ENABLE`, this function terminates the thread. If the cancel state is `SCE_PTHREAD_CANCEL_DISABLE`, termination requests are held so nothing will happen even if this function is called.

This function call will be an explicit cancel point. The following function calls will be an implicit cancel point.

`sceKernelNanosleep()`, `scePthreadCondTimedwait()`, `scePthreadCondWait()`, `scePthreadJoin()`, `sceKernelSleep()`

## See Also

`scePthreadCancel()`, `scePthreadSetcancelstate()`

# scePthreadYield

Yield execution rights

## Definition

```
#include <kernel.h>
void scePthreadYield(void)
```

## Arguments

None

## Return Values

None

## Description

This function yields a CPU to an existing executable (but not yet executed) thread with the same priority as the caller thread. If there are no such threads, this function will have no effect on the thread scheduling.

## Notes

If this function is executed consecutively at short intervals, the execution time of the function will be adjusted to maintain application operation stability.

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.