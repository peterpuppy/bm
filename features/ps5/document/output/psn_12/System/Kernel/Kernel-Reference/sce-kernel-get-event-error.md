# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-get-event-error.html

# Event Queues

# sceKernelAddAmprEvent

Add AMPR event

## Definition

```
#include <kernel.h>
int sceKernelAddAmprEvent(
    SceKernelEqueue eq,
    int id,
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID for identifying the event |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid, or value specified with `id` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds an AMPR event to the event queue specified with `eq`.

For `id`, specify an arbitrary value as the ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `id` is specified for the same `eq` when calling this function, the previously added event will be updated.

The following information can be obtained from AMPR events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_AMPR`
* `sceKernelGetEventId()`: Value specified with `id`
* `sceKernelGetEventUserData()`: Value specified with `udata`

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteAmprEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddAmprSystemEvent

Add AMPR system event

## Definition

```
#include <kernel.h>
int sceKernelAddAmprSystemEvent(
    SceKernelEqueue eq,
    int id,
    int watch,
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID for identifying the event |
| `watch` | Flag for the circumstances of the monitoring target |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid, or value specified with `id` is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `watch` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds an AMPR system event to the event queue specified with `eq`.

For `id`, specify an arbitrary value as the ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `id` is specified for the same `eq` when calling this function, the previously added event will be updated.

For `watch`, specify flags that indicate circumstances to trigger this event when those circumstances occur to the file. The following circumstances can be monitored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_EVNOTE_AMPR_AMM_PAGE_TABLE_THRESHOLD_REACHED` | 0x0001 | The number of entries allocated in the AMM page table has reached the threshold set with `sce::Ampr::Amm:setPageTablePoolOccupancyNotificationThreshold()`. |

The following information can be obtained from AMPR system events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_AMPR_SYSTEM`
* `sceKernelGetEventId()`: Value specified with `id`
* `sceKernelGetEventFflags()`: Bitwise OR that indicates the circumstances that occurred
* `sceKernelGetEventUserData()`: Value specified with `udata`

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteAmprSystemEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddFileEvent

Add file event

## Definition

```
#include <kernel.h>
int sceKernelAddFileEvent(
    SceKernelEqueue eq, 
    int fd, 
    int watch, 
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `fd` | File descriptor to be monitored |
| `watch` | Flag for the circumstances of the monitoring target |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid, or file descriptor specified with `fd` is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `watch` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a file event to the event queue specified with `eq`.

For `fd`, specify the file descriptor to be monitored. The `fd` value is also used as an ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `fd` is specified for the same `eq` when calling this function, the previously added event will be updated.

For `watch`, specify flags that indicate circumstances to trigger this event when those circumstances occur to the file. The following circumstances can be monitored. To monitor multiple circumstances, specify the bitwise OR of these.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_EVNOTE_DELETE` | 0x0001 | File has been deleted |
| `SCE_KERNEL_EVNOTE_WRITE` | 0x0002 | Data has been written to the file |
| `SCE_KERNEL_EVNOTE_EXTEND` | 0x0004 | File has been extended |
| `SCE_KERNEL_EVNOTE_ATTRIB` | 0x0008 | An attribute of the file has been changed |
| `SCE_KERNEL_EVNOTE_RENAME` | 0x0020 | The name of the file has been changed |

The following information can be obtained from file events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_FILE`
* `sceKernelGetEventId()`: Value specified with `fd`
* `sceKernelGetEventFflags()`: Bitwise OR that indicates the circumstances that occurred
* `sceKernelGetEventUserData()`: Value specified with `udata`

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteFileEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddHRTimerEvent

Add high precision timer event

## Definition

```
#include <kernel.h>
int sceKernelAddHRTimerEvent(
    SceKernelEqueue eq, 
    int id, 
    SceKernelTimespec *ts,
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID for identifying the event |
| `ts` | Time to trigger a high precision timer event (nanosecond granularity, 100 microseconds to less than 100 seconds) |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | A time of 100+ seconds or less than 100 microseconds was specified for `ts` |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a high precision timer event to the event queue specified with `eq`.

For `id`, specify an arbitrary value as the ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `id` is specified for the same `eq` when calling this function, the previously added event will be updated.

For `ts`, specify the timer time in seconds and nanoseconds in `SceKernelTimespec` format. When this time has elapsed after this function has been called, a high precision timer event will occur in `eq`. The times that can be specified are 100 microseconds or more and less than 100 seconds. If another time is specified, an error will be returned.

An arbitrary value can be specified for `udata`. This value will not be used by the system.

The following information can be obtained from high precision timer events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_HRTIMER`
* `sceKernelGetEventId()`: Value specified with `id`
* `sceKernelGetEventUserData()`: Value specified with `udata`

When the application receives high-precision timer events, events are removed from the event queue automatically.

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteHRTimerEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddReadEvent

Add read event

## Definition

```
#include <kernel.h>
int sceKernelAddReadEvent(
    SceKernelEqueue eq, 
    int fd, 
    size_t size, 
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `fd` | File descriptor to be monitored |
| `size` | The number of readable bytes that triggers an event. Only valid when `fd` is a socket but not a listening socket (a socket made to wait for a connection by `sceNetListen()`). Specify 0 when not used |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid, or file descriptor specified with `fd` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a read event to the event queue specified with `eq`.

For `fd`, specify the file descriptor to be monitored. The `fd` value is also used as an ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `fd` is specified for the same `eq` when calling this function, the previously added event will be updated.

If `fd` is a file, this event occurs unless the read/write position is at the end of the file. At this time, the offset from the current read/write position to the end of the file can be obtained as event data (the value that can be obtained with `sceKernelGetEventData()`).

If `fd` is a listening socket (a socket made to wait for a connection by `sceNetListen()`), this event occurs when a suspended connection request exists. At this time, the size of the listen backlog can be obtained as event data.

If `fd` is another socket, this event will occur when the socket has readable data. In such cases, it is also possible to use `size` to specify the number of bytes to trigger the event when that amount of data becomes readable.

If `fd` is a socket, in addition to the above an event will occur when communication is disconnected and when an error occurs.

The following information can be obtained from read events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_READ`
* `sceKernelGetEventId()`: Value specified with `fd`
* `sceKernelGetEventData()`
  + If `fd` is a file: The offset from the current position to the end of the file
  + If `fd` is a listening socket: The size of the listen backlog
  + If `fd` is any other socket: The number of readable bytes
* `sceKernelGetEventFflags()`
  + If `fd` is a listening socket: Any of the following error codes:
    - `SCE_NET_ECONNABORTED` (53): Connection was aborted
    - `SCE_NET_EINACTIVEDISABLED` (163): Network disconnection occurred because of an IP address release
    - `SCE_NET_ENETINTR` (167): Abort function was called
  + If `fd` is any other socket: Any of the following error codes:
    - `SCE_NET_ECONNRESET` (54): Connection was reset
    - `SCE_NET_EINACTIVEDISABLED` (163): Network disconnection occurred because of an IP address release
    - `SCE_NET_ENETINTR` (167): Abort function was called

If `fd` is a socket and the return value of `sceKernelGetEventFflags()` is other than zero, the above error codes can also be obtained by calling `sceNetGetsockopt()` with the socket option `SCE_NET_SO_ERROR` or `SCE_NET_SO_ERROR_EX` specified.

* `sceKernelGetEventUserData()`: Value specified with `udata`

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteReadEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddTimerEvent

Add timer event

## Definition

```
#include <kernel.h>
int sceKernelAddTimerEvent(
    SceKernelEqueue eq, 
    int id, 
    SceKernelUseconds usec, 
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID for identifying the event |
| `usec` | Time to trigger a timer event (microseconds) |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a timer event to the event queue specified with `eq`.

For `id`, specify an arbitrary value as the ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `id` is specified for the same `eq` when calling this function, the previously added event will be updated.

For `usec`, specify the timer time in microseconds. When this time has elapsed after this function has been called, a timer event will occur in `eq`. This event occurs periodically every time the time specified with `usec` elapses. The event occurrence will not stop even when the event is obtained with `sceKernelWaitEqueue()` and will continue until the event is deleted with `sceKernelDeleteTimerEvent()`.

An arbitrary value can be specified for `udata`. This value will not be used by the system.

The following information can be obtained from timer events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_TIMER`
* `sceKernelGetEventId()`: Value specified with `id`
* `sceKernelGetEventData()`: Number of times the event occurred
* `sceKernelGetEventUserData()`: Value specified with `udata`

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteTimerEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddUserEvent

Add user event

## Definition

```
#include <kernel.h>
int sceKernelAddUserEvent(
    SceKernelEqueue eq, 
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID for identifying the event |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a user event to the event queue specified with `eq`.

Added events will be handled as level triggers. In other words, after the event added with this function is triggered with `sceKernelTriggerUserEvent()`, the event will remain until it is deleted with `sceKernelDeleteUserEvent()`. Use `sceKernelAddUserEventEdge()` to add a user event to handle as an edge trigger.

For `id`, specify an arbitrary value as the ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `id` is specified for the same `eq` when calling this function, the previously added event will be updated.

When `sceKernelTriggerUserEvent()` is called for the same `id` of the same `eq`, this event will occur. The following information can be obtained from user events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_USER`
* `sceKernelGetEventId()`: Value specified with `id`
* `sceKernelGetEventUserData()`: Value specified with `udata` of `sceKernelTriggerUserEvent()`

## See Also

`sceKernelAddUserEventEdge()`, `sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelTriggerUserEvent()`, `sceKernelDeleteUserEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddUserEventEdge

Add edge trigger type user event

## Definition

```
#include <kernel.h>
int sceKernelAddUserEventEdge(
    SceKernelEqueue eq, 
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID for identifying the event |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a user event to the event queue specified with `eq`.

Added events will be handled as edge triggers. In other words, after the event added with this function is triggered with `sceKernelTriggerUserEvent()` and obtained with `sceKernelWaitEqueue()`, the event will be in an untriggered state. When calling `sceKernelTriggerUserEvent()`, it is possible to cause the same event to occur again (if it has not been deleted by `sceKernelDeleteUserEvent()`). Use `sceKernelAddUserEvent()` to add a user event to handle as a level trigger.

For `id`, specify an arbitrary value as the ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `id` is specified for the same `eq` when calling this function, the previously added event will be updated.

When `sceKernelTriggerUserEvent()` is called for the same `id` of the same `eq`, this event will occur. The following information can be obtained from user events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_USER`
* `sceKernelGetEventId()`: Value specified with `id`
* `sceKernelGetEventUserData()`: Value specified with `udata` of `sceKernelTriggerUserEvent()`

## See Also

`sceKernelAddUserEvent()`, `sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelTriggerUserEvent()`, `sceKernelDeleteUserEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelAddWriteEvent

Add write event

## Definition

```
#include <kernel.h>
int sceKernelAddWriteEvent(
    SceKernelEqueue eq, 
    int fd, 
    size_t size, 
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `fd` | File descriptor to be monitored |
| `size` | The number of writable bytes that triggers an event. Only valid when `fd` is a socket but not a listening socket (a socket made to wait for a connection by `sceNetListen()`). Specify 0 when not used |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid, or file descriptor specified with `fd` is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Limit on the number of events that the application can add has been reached (For information about this limit, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |

## Description

This function adds a write event to the event queue specified with `eq`.

For `fd`, specify the file descriptor to be monitored. The `fd` value is also used as an ID for identifying the event. Events are identified in the event queue by ID and filter. If the same `fd` is specified for the same `eq` when calling this function, the previously added event will be updated.

If `fd` is a file, this event occurs unless the read/write position is at the end of the file. At this time, the offset from the current read/write position to the end of the file can be obtained as event data (the value that can be obtained with `sceKernelGetEventData()`).

If `fd` is a listening socket (a socket made to wait for a connection by `sceNetListen()`), this event occurs when a suspended connection request exists. At this time, the size of the listen backlog can be obtained as event data.

If `fd` is another socket, an event will occur when the socket has writable data. In such cases, it is also possible to use `size` to specify the number of bytes to trigger the event when that amount of data becomes writable.

If `fd` is a socket, in addition to the above an event will occur when communication is disconnected and when an error occurs.

The following information can be obtained from write events that have occurred using the following functions.

* `sceKernelGetEventFilter()`: `SCE_KERNEL_EVFILT_WRITE`
* `sceKernelGetEventId()`: Value specified with `fd`
* `sceKernelGetEventData()`
  + If `fd` is a file: The offset from the current position to the end of the file
  + If `fd` is a listening socket: The size of the listen backlog
  + If `fd` is any other socket: The number of writable bytes
* `sceKernelGetEventFflags()`
  + If `fd` is a socket made to wait for a connection to complete (`sceNetConnect()` is being executed): Any of the following error codes:
    - `SCE_NET_ETIMEDOUT` (60): TCP resend timeout occurred
    - `SCE_NET_ECONNREFUSED` (61): Connection request was denied
    - `SCE_NET_EINACTIVEDISABLED` (163): Network disconnection occurred because of an IP address release
    - `SCE_NET_ENETINTR` (167): Abort function was called
  + If `fd` is any other socket: Any of the following error codes:
    - `SCE_NET_ECONNRESET` (54): Connection was reset
    - `SCE_NET_ETIMEDOUT` (60): TCP resend timeout occurred
    - `SCE_NET_EINACTIVEDISABLED` (163): Network disconnection occurred because of an IP address release
    - `SCE_NET_ENETINTR` (167): Abort function was called

If `fd` is a socket and the return value of `sceKernelGetEventFflags()` is other than zero, the above error codes can also be obtained by calling `sceNetGetsockopt()` with the socket option `SCE_NET_SO_ERROR` or `SCE_NET_SO_ERROR_EX` specified.

* `sceKernelGetEventUserData()`: Value specified with `udata`

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`, `sceKernelDeleteWriteEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelCreateEqueue

Create event queue

## Definition

```
#include <kernel.h>
int sceKernelCreateEqueue(
    SceKernelEqueue *eq, 
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Destination to store the created event queue |
| `name` | Event queue name (up to 32 bytes including the NULL-terminator character) |

## Return Values

Stores the created event queue to `*eq` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EMFILE` | 0x80020018 | Limit on the number of event queues that the application can generate has been reached. (For information about this limit, refer to "Number of Event Queues That Can Be Created" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `name` is NULL |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | The `name` address is invalid |

## Description

This function creates an event queue. The required resources are allocated by the function.

For `name`, specify the name of the event queue. NULL cannot be specified. This name is used for identification when seen by operators during debugging, etc. Therefore, it does not have to be unique. A name up to 32 bytes including the NULL-terminator character can be specified.

## See Also

`sceKernelDeleteEqueue()`, `sceKernelWaitEqueue()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteAmprEvent

Delete AMPR event

## Definition

```
#include <kernel.h>
int sceKernelDeleteAmprEvent(
    SceKernelEqueue eq, 
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | AMPR event specified with `id` does not exist |

## Description

This function deletes the AMPR event that is identified with `id` from the event queue specified with `eq`. For `eq` and `id`, specify the values that were specified when the AMPR event was added with `sceKernelAddAmprEvent()`.

## See Also

`sceKernelAddAmprEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteAmprSystemEvent

Delete AMPR system event

## Definition

```
#include <kernel.h>
int sceKernelDeleteAmprSystemEvent(
    SceKernelEqueue eq,
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | AMPR system event specified with `id` does not exist |

## Description

This function deletes the AMPR system event that is identified with `id` from the event queue specified with `eq`. For `eq` and `id`, specify the values that were specified when the AMPR system event was added with `sceKernelAddAmprSystemEvent()`.

## See Also

`sceKernelAddAmprSystemEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteEqueue

Delete event queue

## Definition

```
#include <kernel.h>
int sceKernelDeleteEqueue(
    SceKernelEqueue eq
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Event queue to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |

## Description

This function deletes the event queue specified with `eq`. Resources allocated for the event queue will be released.

## See Also

`sceKernelCreateEqueue()`, `sceKernelWaitEqueue()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteFileEvent

Delete file event

## Definition

```
#include <kernel.h>
int sceKernelDeleteFileEvent(
    SceKernelEqueue eq, 
    int fd
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `fd` | ID (file descriptor) of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | File event specified with `fd` does not exist |

## Description

This function deletes the file event that is identified with `fd` from the event queue specified with `eq`. For `eq` and `fd`, specify the values that were specified when the file event was added with `sceKernelAddFileEvent()`.

## See Also

`sceKernelAddFileEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteHRTimerEvent

Delete high precision timer event

## Definition

```
#include <kernel.h>
int sceKernelDeleteHRTimerEvent(
    SceKernelEqueue eq, 
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | High precision timer event specified with `id` does not exist |

## Description

This function deletes the high precision timer event that is identified with `id` from the event queue specified with `eq`. For `eq` and `id`, specify the values that were specified when the high precision timer event was added with `sceKernelAddHRTimerEvent()`.

## See Also

`sceKernelAddHRTimerEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteReadEvent

Delete read event

## Definition

```
#include <kernel.h>
int sceKernelDeleteReadEvent(
    SceKernelEqueue eq, 
    int fd
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `fd` | ID (file descriptor) of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Read event specified with `fd` does not exist |

## Description

This function deletes the read event that is identified with `fd` from the event queue specified with `eq`. For `eq` and `fd`, specify the values that were specified when the read event was added with `sceKernelAddReadEvent()`.

## See Also

`sceKernelAddReadEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteTimerEvent

Delete timer event

## Definition

```
#include <kernel.h>
int sceKernelDeleteTimerEvent(
    SceKernelEqueue eq, 
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Timer event specified with `id` does not exist |

## Description

This function deletes the timer event that is identified with `id` from the event queue specified with `eq`. For `eq` and `id`, specify the values that were specified when the timer event was added with `sceKernelAddTimerEvent()`.

## See Also

`sceKernelAddTimerEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteUserEvent

Delete user event

## Definition

```
#include <kernel.h>
int sceKernelDeleteUserEvent(
    SceKernelEqueue eq, 
    int id
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | User event specified with `id` does not exist |

## Description

This function deletes the user event that is identified with `id` from the event queue specified with `eq`. For `eq` and `id`, specify the values that were specified when the user event was added with `sceKernelAddUserEvent()` or `sceKernelAddUserEventEdge()`.

## See Also

`sceKernelAddUserEvent()`, `sceKernelAddUserEventEdge()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelDeleteWriteEvent

Delete write event

## Definition

```
#include <kernel.h>
int sceKernelDeleteWriteEvent(
    SceKernelEqueue eq, 
    int fd
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `fd` | ID (file descriptor) of the event to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Write event specified with `fd` does not exist |

## Description

This function deletes the write event that is identified with `fd` from the event queue specified with `eq`. For `eq` and `fd`, specify the values that were specified when the write event was added with `sceKernelAddWriteEvent()`.

## See Also

`sceKernelAddWriteEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelGetEventData

Get data from an event

## Definition

```
#include <kernel.h>
intptr_t sceKernelGetEventData(
    const SceKernelEvent *ev
)
```

## Arguments

|  |  |
| --- | --- |
| `ev` | Target event |

## Return Values

Returns event data.

## Description

This function obtains data from the event specified with `ev`.

For `ev`, specify an event obtained with `sceKernelWaitEqueue()`.

The values returned by this function vary by filter and by event status. For details, refer to the explanations of functions indicated in "See Also" that add each event.

## See Also

`sceKernelWaitEqueue()`, `sceKernelAddTimerEvent()`, `sceKernelAddReadEvent()`, `sceKernelAddWriteEvent()`

# sceKernelGetEventError

Get error from an event

## Definition

```
#include <kernel.h>
int sceKernelGetEventError(
    const SceKernelEvent *ev
)
```

## Arguments

|  |  |
| --- | --- |
| `ev` | Target event |

## Return Values

Returns an event error.

## Description

This function obtains an error from the event specified with `ev`.

For `ev`, specify an event obtained with `sceKernelWaitEqueue()`.

The value returned by this function varies depending on the filter. (However, at this time, there are no filters by which errors can be obtained using this function.)

## See Also

`sceKernelWaitEqueue()`

# sceKernelGetEventFflags

Get filter-specific flags from the event

## Definition

```
#include <kernel.h>
intptr_t sceKernelGetEventFflags(
    const SceKernelEvent *ev
)
```

## Arguments

|  |  |
| --- | --- |
| `ev` | Target event |

## Return Values

Returns the filter-specific flags of an event.

## Description

This function obtains the filter-specific flags from the event specified with `ev`.

For `ev`, specify an event obtained with `sceKernelWaitEqueue()`.

The values returned by this function vary by filter. For details, refer to the explanations of functions indicated in "See Also" that add each event.

## See Also

`sceKernelWaitEqueue()`, `sceKernelAddReadEvent()`, `sceKernelAddWriteEvent()`, `sceKernelAddFileEvent()`, `sceKernelAddAmprSystemEvent()`

# sceKernelGetEventFilter

Get filter from an event

## Definition

```
#include <kernel.h>
int sceKernelGetEventFilter(
    const SceKernelEvent *ev
)
```

## Arguments

|  |  |
| --- | --- |
| `ev` | Target event |

## Return Values

Returns the value that indicates the event filter.

## Description

This function obtains the filter from the event specified with `ev`.

For `ev`, specify an event obtained with `sceKernelWaitEqueue()`.

For values returned by this function, refer to the explanations of functions that add each event.

## See Also

`sceKernelWaitEqueue()`, `sceKernelAddTimerEvent()`, `sceKernelAddHRTimerEvent()`, `sceKernelAddReadEvent()`, `sceKernelAddWriteEvent()`, `sceKernelAddFileEvent()`, `sceKernelAddUserEvent()`, `sceKernelAddUserEventEdge()`, `sceKernelAddAmprEvent()`, `sceKernelAddAmprSystemEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelGetEventId

Get identifier from an event

## Definition

```
#include <kernel.h>
uintptr_t sceKernelGetEventId(
    const SceKernelEvent *ev
)
```

## Arguments

|  |  |
| --- | --- |
| `ev` | Target event |

## Return Values

Returns the event identifier.

## Description

This function obtains the identifier from the event specified with `ev`.

For `ev`, specify an event obtained with `sceKernelWaitEqueue()`.

The values returned by this function vary by filter and are an `id` value or `fd` value specified when adding an event. For details, refer to the explanations of functions that add each event.

## See Also

`sceKernelWaitEqueue()`, `sceKernelAddTimerEvent()`, `sceKernelAddHRTimerEvent()`, `sceKernelAddReadEvent()`, `sceKernelAddWriteEvent()`, `sceKernelAddFileEvent()`, `sceKernelAddUserEvent()`, `sceKernelAddUserEventEdge()`, `sceKernelAddAmprEvent()`, `sceKernelAddAmprSystemEvent()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelGetEventUserData

Get user data from an event

## Definition

```
#include <kernel.h>
void *sceKernelGetEventUserData(
    const SceKernelEvent *ev
)
```

## Arguments

|  |  |
| --- | --- |
| `ev` | Target event |

## Return Values

Returns the user data of an event.

## Description

This function obtains user data from the event specified with `ev`.

For `ev`, specify an event obtained with `sceKernelWaitEqueue()`.

User data is arbitrary values specified with the argument `udata` when adding an event (or when triggering a user event with `sceKernelTriggerUserEvent()`). This value will not be changed by the system.

## See Also

`sceKernelWaitEqueue()`, `sceKernelAddTimerEvent()`, `sceKernelAddHRTimerEvent()`, `sceKernelAddReadEvent()`, `sceKernelAddWriteEvent()`, `sceKernelAddFileEvent()`, `sceKernelAddAmprEvent()`, `sceKernelAddAmprSystemEvent()`, `sceKernelTriggerUserEvent()`

# sceKernelTriggerUserEvent

Trigger user event

## Definition

```
#include <kernel.h>
int sceKernelTriggerUserEvent(
    SceKernelEqueue eq, 
    int id, 
    void *udata
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `id` | ID of the event to trigger |
| `udata` | User data (arbitrary value) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | User event specified with `id` does not exist |

## Description

This function triggers the user event specified with `eq` and `id`. For `eq` and `id`, specify the values that were specified when the user event was added with `sceKernelAddUserEvent()` or `sceKernelAddUserEventEdge()`.

## See Also

`sceKernelAddUserEvent()`, `sceKernelAddUserEventEdge()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

# sceKernelWaitEqueue

Wait for event to arrive

## Definition

```
#include <kernel.h>
int sceKernelWaitEqueue(
    SceKernelEqueue eq, 
    SceKernelEvent *ev, 
    int num, 
    int *out, 
    SceKernelUseconds *timo
)
```

## Arguments

|  |  |
| --- | --- |
| `eq` | Target event queue |
| `ev` | Array to store the arrived event |
| `num` | Number of events that can be stored in `ev` |
| `out` | Destination to store the number of events actually stored in `ev` |
| `timo` | Time to time out (microseconds), or NULL |

## Return Values

Stores the result events in `*ev`, stores the number of events in `*out`, and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | Event queue specified with `eq` is invalid |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | The `ev` address is invalid |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` is smaller than 1 |

## Description

This function waits for an event to arrive in the event queue specified with `eq`.

For `ev`, specify the buffer for receiving the arrived events. For `num`, specify the maximum number of events to receive. `ev` requires a space for receiving events that is greater than or equal to `num`.

When even just one event arrives in `eq`, the wait state will be canceled. Note that this function will not wait for the number of events specified with `num` to arrive.

In `*out`, the number of events actually stored in `ev` will be stored.

For `timo`, specify the pointer to the variable to which the timeout time has been set. Setting can be made in microsecond units; however, the precision of actual processing is in millisecond units. If NULL is specified for `timo`, this function will wait until an event arrives without timing out. If 0 is specified for `*timo`, only events that have already arrived at the time of this function call can be received. If an event has not arrived, a timeout will occur and `SCE_KERNEL_ERROR_ETIMEDOUT` will be returned.

It is possible to identify the filters for the events stored in `*ev` using `sceKernelGetEventFilter()`. The information that can be obtained from events differs depending on the filter, so refer to the explanations for the functions that add each of the events.

## See Also

`sceKernelCreateEqueue()`, `sceKernelDeleteEqueue()`, `sceKernelGetEventFilter()`

[Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html)

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.