# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-aio-poll-requests.html

# File System (Asynchronous I/O)

# SCE\_KERNEL\_AIO\_\*\_NUM\_MAX

Maximum values for various data used with asynchronous I/O

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_ID_NUM_MAX` | 128 | Maximum number of asynchronous I/O submit IDs |
| `SCE_KERNEL_AIO_REQUEST_NUM_MAX` | 128 | Maximum number of asynchronous I/O requests |

## Description

These constants represent the maximum values for various data handled with asynchronous I/O.

# SCE\_KERNEL\_AIO\_STATE\_\*

Asynchronous I/O request states

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_STATE_SUBMITTED` | 0x01 | Received |
| `SCE_KERNEL_AIO_STATE_PROCESSING` | 0x02 | Now processing |
| `SCE_KERNEL_AIO_STATE_COMPLETED` | 0x03 | Completed |
| `SCE_KERNEL_AIO_STATE_ABORTED` | 0x04 | Canceled |

## Description

These constants represent the states for a single asynchronous I/O request or all of the asynchronous I/O requests to which a single asynchronous I/O submit ID is assigned.

## See Also

`SceKernelAioResult`, `sceKernelAioCancelRequest()`, `sceKernelAioCancelRequests()`, `sceKernelAioPollRequest()`, `sceKernelAioPollRequests()`, `sceKernelAioWaitRequest()`, `sceKernelAioWaitRequests()`

# SceKernelAioParam

Asynchronous I/O parameters

## Definition

```
typedef struct SceKernelAioParam {
	SceKernelAioSchedulingParam low;
	SceKernelAioSchedulingParam mid;
	SceKernelAioSchedulingParam high;
} SceKernelAioParam;
```

## Members

|  |  |
| --- | --- |
| `low` | Low priority asynchronous I/O scheduling parameters |
| `mid` | Medium priority asynchronous I/O scheduling parameters |
| `high` | High priority asynchronous I/O scheduling parameters |

## Description

This is a parameter structure for configuring scheduling parameters for each priority level for asynchronous I/O requests. For details about each parameter and their default values, refer to the explanation for `SceKernelAioSchedulingParam`.

## See Also

`SceKernelAioSchedulingParam`, `sceKernelAioInitialize()`, `sceKernelAioInitializeParam()`

# SceKernelAioRWRequest

Asynchronous I/O read/write request

## Definition

```
#include <kernel.h>
typedef struct SceKernelAioRWRequest{
    off_t offset;
    size_t nbyte;
    void *buf;
    SceKernelAioResult *result;
    int fd;
} SceKernelAioRWRequest;
```

## Members

|  |  |
| --- | --- |
| `offset` | Data position (number of bytes from the file start) |
| `nbyte` | Data size (bytes) |
| `buf` | Data storage buffer |
| `result` | Destination to store the asynchronous I/O processing results |
| `fd` | Descriptor of the target file |

## Description

This is an asynchronous I/O read/write request structure specified for `sceKernelAioSubmitReadCommands()`, `sceKernelAioSubmitReadCommandsMultiple()`, `sceKernelAioSubmitWriteCommands()`, or `sceKernelAioSubmitWriteCommandsMultiple()`.

For `offset`, specify the number of bytes from the start of the file in order to specify the position where data will be read/written.

For `nbyte`, specify the number of bytes for the size of the data to be read/written. It is not possible to specify a value greater than `INT_MAX`.

For `buf`, specify the buffer to store the read data, or specify the buffer where the data to be written is stored.

For `result`, specify an `SceKernelAioResult` structure to store the results of the asynchronous I/O processing.

For `fd`, specify the descriptor of the target file.

The memory specified for `buf` and `result` cannot be freed until the corresponding request's state obtained using `sceKernelAioPollRequest()`/`sceKernelAioPollRequests()`/`sceKernelAioWaitRequest()`/`sceKernelAioWaitRequests()` becomes `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED`.

## See Also

`SceKernelAioResult`, `sceKernelAioSubmitReadCommands()`, `sceKernelAioSubmitReadCommandsMultiple()`, `sceKernelAioSubmitWriteCommands()`, `sceKernelAioSubmitWriteCommandsMultiple()`

# SceKernelAioResult

Asynchronous I/O processing results

## Definition

```
typedef struct SceKernelAioResult {
    int64_t returnValue; 
    uint32_t state; 
} SceKernelAioResult;
```

## Members

|  |  |
| --- | --- |
| `returnValue` | Return value that represents the asynchronous I/O processing results |
| `state` | State of the asynchronous I/O request |

## Description

This structure stores the execution results of an asynchronous I/O read/write request.

In `returnValue`, the return value that represents the asynchronous I/O processing results will be stored. When successful, the number of bytes read will be stored for an asynchronous I/O read, and the number of bytes written will be stored for an asynchronous I/O write. When execution of the corresponding request fails, an error code (negative value) will be stored.

In `state`, either `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED` (the values that represent the final asynchronous I/O request states to transition to) will be stored.

## See Also

`SCE_KERNEL_AIO_STATE_*`, `SceKernelAioRWRequest`, `sceKernelAioSubmitReadCommands()`, `sceKernelAioSubmitReadCommandsMultiple()`, `sceKernelAioSubmitWriteCommands()`, `sceKernelAioSubmitWriteCommandsMultiple()`

# SceKernelAioSchedulingParam

Asynchronous I/O scheduling parameters

## Definition

```
typedef struct SceKernelAioSchedulingParam {
	int schedulingWindowSize;
	int delayedCountLimit;
	uint32_t enableSplit;
	uint32_t splitSize;
	uint32_t splitChunkSize;
} SceKernelAioSchedulingParam;
```

## Members

|  |  |
| --- | --- |
| `schedulingWindowSize` | Number of target asynchronous I/O requests for optimization by the system (0 or greater) |
| `delayedCountLimit` | Maximum number of times a target asynchronous I/O request for optimization by the system will be skipped (0 or greater) |
| `enableSplit` | Split feature setting for asynchronous I/O requests |
| `splitSize` | Size to determine the target asynchronous I/O requests for splitting (bytes, multiple of 256 KiB greater than 0) |
| `splitChunkSize` | Chunk size after splitting asynchronous I/O requests (bytes, multiple of 256 KiB greater than 0) |

## Description

This is an asynchronous I/O scheduling parameter structure.

For `schedulingWindowSize`, specify the number of target asynchronous I/O requests for optimization by the system. For `delayedCountLimit`, specify the maximum number of times a target asynchronous I/O request for optimization by the system will be skipped by the requests that will later become the targets for optimization. Specify an integer value of 0 or greater for both. Normally, asynchronous I/O requests are processed in FIFO order for each priority level, but if the system performs I/O optimization, the processing order may vary. I/O optimization by the system will be performed for the requests from the start to the number specified with `schedulingWindowSize`. In addition, a target request for optimization will not be delayed more than the number of times specified with `delayedCountLimit`.

For `enableSplit`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_DISABLE_SPLIT` | 0 | Disable asynchronous I/O request splitting |
| `SCE_KERNEL_AIO_ENABLE_SPLIT` | 1 | Enable asynchronous I/O request splitting |

* When `SCE_KERNEL_AIO_ENABLE_SPLIT` is specified, asynchronous I/O requests greater than the size specified with `splitSize` will be split into chunks in the size specified with `splitChunkSize` and then will be processed. `splitSize` and `splitChunkSize` must both be a multiple of 256 KiB and greater than 0. In addition, note that request cancellation will not be performed at the chunk level after requests are split into chunks.
* When `SCE_KERNEL_AIO_DISABLE_SPLIT` is specified, the `splitSize` and `splitChunkSize` values will be ignored.

Note that the default value for low/medium priority asynchronous I/O scheduling parameters is `SCE_KERNEL_AIO_ENABLE_SPLIT`, and the default value for high priority asynchronous I/O scheduling parameters is `SCE_KERNEL_AIO_DISABLE_SPLIT`.

The maximum values that can be specified for asynchronous I/O scheduling parameters are defined as follows.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_SCHED_WINDOW_MAX` | 128 | Maximum value for `schedulingWindowSize` |
| `SCE_KERNEL_AIO_DELAYED_COUNT_MAX` | 128 | Maximum value for `delayedCountLimit` |
| `SCE_KERNEL_AIO_SPLIT_SIZE_MAX` | 0x1000000 (16 MiB) | Maximum value for `splitSize` |
| `SCE_KERNEL_AIO_SPLIT_CHUNK_SIZE_MAX` | 0x1000000 (16 MiB) | Maximum value for `splitChunkSize` |

The default values for asynchronous I/O scheduling parameters are defined as follows.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_SCHED_WINDOW_DEFAULT` | 32 | Default value for `schedulingWindowSize` |
| `SCE_KERNEL_AIO_DELAYED_COUNT_DEFAULT` | 32 | Default value for `delayedCountLimit` |
| `SCE_KERNEL_AIO_SPLIT_SIZE_DEFAULT` | 0x100000 (1 MiB) | Default value for `splitSize` |
| `SCE_KERNEL_AIO_SPLIT_CHUNK_SIZE_DEFAULT` | 0x100000 (1 MiB) | Default value for `splitChunkSize` |

`sceKernelAioInitializeParam()` initializes asynchronous I/O scheduling parameters to the aforementioned default values. If parameters are not explicitly set with `sceKernelAioInitialize()`, the default values will be applied to asynchronous I/O.

## See Also

`SceKernelAioParam`, `sceKernelAioInitialize()`, `sceKernelAioInitializeParam()`

# SceKernelAioSubmitId

Asynchronous I/O submit ID

## Definition

```
#include <kernel.h>
typedef int SceKernelAioSubmitId;
```

## Description

This identifier is obtained when submitting asynchronous I/O read/write request(s) using `sceKernelAioSubmitReadCommands()`, `sceKernelAioSubmitReadCommandsMultiple()`, `sceKernelAioSubmitWriteCommands()`, or `sceKernelAioSubmitWriteCommandsMultiple()`. Use this asynchronous I/O submit ID when performing operations such as obtaining the request state or waiting for request completion.

# sceKernelAioCancelRequest

Cancel asynchronous I/O request(s) for a single specified asynchronous I/O submit ID

## Definition

```
#include <kernel.h>
int sceKernelAioCancelRequest(
    SceKernelAioSubmitId id, 
    int *state
)
```

## Arguments

|  |  |
| --- | --- |
| `id` | Target asynchronous I/O submit ID for cancellation |
| `state` | Destination to store the state (or error code) |

## Return Values

Stores the obtained state in `*state` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `state` address is invalid |

## Description

This function cancels the asynchronous I/O request(s) to which the asynchronous I/O submit ID specified for `id` is assigned.

Only asynchronous I/O requests before they are executed can be canceled. If the request state is `SCE_KERNEL_AIO_STATE_SUBMITTED`, cancel processing will be performed, and `SCE_KERNEL_AIO_STATE_ABORTED` will be stored in `*state` after the cancellation succeeds.

When the request state is `SCE_KERNEL_AIO_STATE_PROCESSING` or `SCE_KERNEL_AIO_STATE_COMPLETED`, the cancel processing will not be performed, and the state will be stored in `*state` as-is.

If an error occurs during cancel processing, the following error code (negative value) will be stored in `*state`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified submit ID is invalid |

However, note that the call of this function will succeed and `SCE_OK` will be returned at such times.

When this function returns `SCE_KERNEL_ERROR_EFAULT`, whether the cancellation succeeded or failed will be undefined. Use `sceKernelAioWaitRequest()`, etc., to check the request state.

**When an asynchronous I/O submit ID is assigned to multiple requests**

When the asynchronous I/O submit ID specified for `id` is assigned to multiple asynchronous I/O requests, only requests where the state is `SCE_KERNEL_AIO_STATE_SUBMITTED` will be cancelled. When even just one request cancellation succeeds, `SCE_KERNEL_AIO_STATE_ABORTED` will be stored in `*state`.

Cancel processing will not be performed when there are no requests where the state is `SCE_KERNEL_AIO_STATE_SUBMITTED` and both a request where the state is `SCE_KERNEL_AIO_STATE_PROCESSING` and a request where the state is `SCE_KERNEL_AIO_STATE_COMPLETED` exist. In such cases, `SCE_KERNEL_AIO_STATE_PROCESSING` will be stored in `*state`.

Cancel processing will also not be performed when the state of all requests is `SCE_KERNEL_AIO_STATE_PROCESSING` or `SCE_KERNEL_AIO_STATE_COMPLETED`, and the state will be stored in `*state` as-is.

## Notes

* Even when this function is used to cancel an asynchronous I/O request, the assigned asynchronous I/O submit ID must not be immediately deleted. Use `sceKernelAioPollRequest()`/`sceKernelAioPollRequests()`/`sceKernelAioWaitRequest()`/`sceKernelAioWaitRequests()` to obtain the request state, confirm that the state is `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED`, and then delete the submit ID.
* `sceKernelAioCancelRequests()` is provided as a function that cancels the asynchronous I/O requests for multiple specified asynchronous I/O submit IDs.

## See Also

`SCE_KERNEL_AIO_STATE_*`, `sceKernelAioCancelRequests()`

# sceKernelAioCancelRequests

Cancel the asynchronous I/O requests for the multiple specified asynchronous I/O submit IDs

## Definition

```
#include <kernel.h>
int sceKernelAioCancelRequests(
    SceKernelAioSubmitId ids[], 
    int num,
    int states[]
)
```

## Arguments

|  |  |
| --- | --- |
| `ids` | Array of target asynchronous I/O submit IDs for cancellation |
| `num` | Number of `ids` array elements |
| `states` | Array to store states (or error codes) |

## Return Values

Stores the obtained states in `states[]` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `ids` or `states` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` value is invalid |

## Description

This function cancels the asynchronous I/O requests to which the multiple asynchronous I/O submit IDs specified for `ids` are assigned.

For `num`, use a positive integer value to specify the number of submit IDs specified for `ids`. `SCE_KERNEL_AIO_ID_NUM_MAX` is defined as the maximum value that can be specified.

Other than specifying multiple submit IDs and storing each state in `states[]`, this function has the same feature as `sceKernelAioCancelRequest()`. Refer to the explanation of `sceKernelAioCancelRequest()`.

When `sceKernelAioCancelRequests()` (this function) returns SCE\_KERNEL\_ERROR\_EFAULT due to `states` being invalid, whether the cancellation succeeded or failed is undefined. Use `sceKernelAioWaitRequests()`, etc., to check the request state.

## Notes

`sceKernelAioCancelRequest()` is provided as a function that cancels the asynchronous I/O request(s) for a single specified asynchronous I/O submit ID.

## See Also

`SCE_KERNEL_AIO_*_NUM_MAX`, `sceKernelAioCancelRequest()`

# sceKernelAioDeleteRequest

Delete a single asynchronous I/O submit ID

## Definition

```
#include <kernel.h>
int sceKernelAioDeleteRequest(
    SceKernelAioSubmitId id, 
    int *ret
)
```

## Arguments

|  |  |
| --- | --- |
| `id` | Target asynchronous I/O submit ID for deletion |
| `ret` | Destination to store deletion results |

## Return Values

Stores the deletion processing results in `*ret` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `ret` address is invalid |

## Description

This function deletes the asynchronous I/O submit ID specified for `id`.

A submit ID assigned to a submitted asynchronous I/O request must always be deleted when the ID is no longer required. Before deleting the ID, obtain and then check the state of the request with `sceKernelAioWaitRequest()`/`sceKernelAioWaitRequests()`/`sceKernelAioPollRequest()`/`sceKernelAioPollRequests()`. A submit ID assigned to a request may only be deleted if the obtained state for the request is either `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED`.

`SCE_OK` (=0) will be stored in `*ret` when deletion of the specified submit ID succeeds, and one of the following error codes (a negative value) will be stored when deletion fails.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified submit ID is invalid |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Request state is improper |

However, note that the call of this function will succeed and `SCE_OK` will be returned at such times.

When this function returns `SCE_KERNEL_ERROR_EFAULT`, whether the deletion succeeded or failed will be undefined. Specify an appropriate `ret`, call this function again, and check the results.

## Notes

`sceKernelAioDeleteRequests()` is provided as a function that deletes multiple asynchronous I/O submit IDs.

## See Also

`sceKernelAioDeleteRequests()`

# sceKernelAioDeleteRequests

Delete multiple asynchronous I/O submit IDs

## Definition

```
#include <kernel.h>
int sceKernelAioDeleteRequests(
    SceKernelAioSubmitId ids[], 
    int num,
    int rets[]
)
```

## Arguments

|  |  |
| --- | --- |
| `ids` | Array of target asynchronous I/O submit IDs for deletion |
| `num` | Number of `ids` array elements |
| `rets` | Array to store deletion results |

## Return Values

Stores the deletion results in `rets[]` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `ids` or `rets` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` value is invalid |

## Description

This function deletes the multiple asynchronous I/O submit IDs specified for `ids`.

For `num`, use a positive integer value to specify the number of submit IDs specified for `ids`. `SCE_KERNEL_AIO_ID_NUM_MAX` is defined as the maximum value that can be specified.

Other than specifying multiple submit IDs and storing the deletion results for each ID in `rets[]`, this function has the same feature as `sceKernelAioDeleteRequest()`. Refer to the explanation of `sceKernelAioDeleteRequest()`.

When `sceKernelAioDeleteRequests()` (this function) returns `SCE_KERNEL_ERROR_EFAULT` due to `rets` being invalid, whether the deletion succeeded or failed is undefined. Specify an appropriate `rets`, call this function again, and check the results.

## Notes

`sceKernelAioDeleteRequest()` is provided as a function that deletes a single asynchronous I/O submit ID.

## See Also

`SCE_KERNEL_AIO_*_NUM_MAX`, `sceKernelAioDeleteRequest()`

# sceKernelAioInitialize

Initialize asynchronous I/O

## Definition

```
#include <kernel.h>
int sceKernelAioInitialize(
    SceKernelAioParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Asynchronous I/O parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Asynchronous I/O initialization has already been performed |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | An invalid asynchronous I/O parameter was specified |

## Description

This function initializes asynchronous I/O with the specified parameters. It can only be called once before starting use of asynchronous I/O.

If another asynchronous I/O function is called before calling this function, the default asynchronous I/O parameters will be used, and it will not be possible to later change them. For details about each parameter and their default values, refer to the explanations of `SceKernelAioParam` and `SceKernelAioSchedulingParam`.

## See Also

`SceKernelAioParam`, `SceKernelAioSchedulingParam`

# sceKernelAioInitializeParam

Initialize asynchronous I/O parameters

## Definition

```
#include <kernel.h>
void sceKernelAioInitializeParam(
    SceKernelAioParam* param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Target asynchronous I/O parameter structure for initialization |

## Return Values

None

## Description

This function initializes the specified asynchronous I/O parameter structure using the default values. For details about each parameter and their default values, refer to the explanations of `SceKernelAioParam` and `SceKernelAioSchedulingParam`.

## See Also

`SceKernelAioParam`, `SceKernelAioSchedulingParam`, `sceKernelAioInitialize()`

# sceKernelAioPollRequest

Get the state of the asynchronous I/O request(s) for a single specified asynchronous I/O submit ID

## Definition

```
#include <kernel.h>
int sceKernelAioPollRequest(
    int id,
    int *state
)
```

## Arguments

|  |  |
| --- | --- |
| `id` | Target asynchronous I/O submit ID for state obtaining |
| `state` | Destination to store the state (or error code) |

## Return Values

Stores the obtained state in `*state` and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `state` address is invalid |

## Description

This function obtains the state of the asynchronous I/O request(s) to which the asynchronous I/O submit ID specified for `id` is assigned.

Other than obtaining the current state and returning without blocking, this function has the same feature as `sceKernelAioWaitRequest()`. Refer to the explanation of `sceKernelAioWaitRequest()`.

When `sceKernelAioPollRequest()` (this function) returns `SCE_KERNEL_ERROR_EFAULT`, whether the state obtaining succeeded or failed is undefined. Specify an appropriate `state`, call this function again, and check the results.

## Notes

* `sceKernelAioPollRequests()` is provided as a function that obtains the states of the asynchronous I/O requests for multiple specified asynchronous I/O submit IDs.
* To wait for completion of asynchronous I/O request(s), use `sceKernelAioWaitRequest()` or `sceKernelAioWaitRequests()`.

## See Also

`sceKernelAioPollRequests()`, `sceKernelAioWaitRequest()`, `sceKernelAioWaitRequests()`

# sceKernelAioPollRequests

Get the states of the asynchronous I/O requests for multiple specified asynchronous I/O submit IDs

## Definition

```
#include <kernel.h>
int sceKernelAioPollRequests(
    int ids[],
    int num,
    int states[]
)
```

## Arguments

|  |  |
| --- | --- |
| `ids` | Array of target asynchronous I/O submit IDs for obtaining states |
| `num` | Number of `ids` array elements |
| `states` | Array to store states (or error codes) |

## Return Values

Stores the obtained states in `states[]` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `ids` or `states` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` value is invalid |

## Description

This function obtains the states of the asynchronous I/O requests to which the multiple asynchronous I/O submit IDs specified for `ids` are assigned.

Other than obtaining the current states and returning without blocking, this function has the same feature as `sceKernelAioWaitRequests()`. Refer to the explanation of `sceKernelAioWaitRequests()`.

When `sceKernelAioPollRequests()` (this function) returns `SCE_KERNEL_ERROR_EFAULT` due to `states` being invalid, whether the obtainment of `states` succeeds or fails is undefined. Specify an appropriate `states`, call this function again, and check the results.

## Notes

* `sceKernelAioPollRequest()` is provided as a function that obtains the state of the asynchronous I/O request(s) for a single specified asynchronous I/O submit ID.
* To wait for completion of asynchronous I/O request(s), use `sceKernelAioWaitRequest()` or `sceKernelAioWaitRequests()`.

## See Also

`sceKernelAioPollRequest()`, `sceKernelAioWaitRequest()`, `sceKernelAioWaitRequests()`

# sceKernelAioSetParam

Set an asynchronous I/O scheduling parameter structure

## Definition

```
#include <kernel.h>
int sceKernelAioSetParam(
    SceKernelAioSchedulingParam *param,
    int schedulingWindowSize,
    int delayedCountLimit,
    uint32_t enableSplit,
    uint32_t splitSize,
    uint32_t splitChunkSize
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Target asynchronous I/O scheduling parameter structure to set |
| `schedulingWindowSize` | Number of target asynchronous I/O requests for optimization by the system (0 or greater) |
| `delayedCountLimit` | Maximum number of times a target asynchronous I/O request for optimization by the system will be skipped (0 or greater) |
| `enableSplit` | Split feature setting for asynchronous I/O requests |
| `splitSize` | Size to determine the target asynchronous I/O requests for splitting (bytes, multiple of 256 KiB greater than 0) |
| `splitChunkSize` | Chunk size after splitting asynchronous I/O requests (bytes, multiple of 256 KiB greater than 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Invalid asynchronous I/O scheduling parameter was specified |

## Description

This function sets the scheduling parameters (that will be set for each priority level upon asynchronous I/O initialization) to the specified values. For details about each parameter, refer to the explanation of `SceKernelAioSchedulingParam`.

## See Also

`SceKernelAioSchedulingParam`, `sceKernelAioInitialize()`

# sceKernelAioSubmitReadCommands

Submit multiple asynchronous I/O read requests and assign a single submit ID

## Definition

```
#include <kernel.h>
int sceKernelAioSubmitReadCommands(
    SceKernelAioRWRequest reqs[],
    int num,
    int priority,
    SceKernelAioSubmitId *id
)
```

## Arguments

|  |  |
| --- | --- |
| `reqs` | Array of asynchronous I/O read request structures |
| `num` | Number of `reqs` array elements |
| `priority` | Request priority level |
| `id` | Destination to store asynchronous I/O submit ID |

## Return Values

Stores the asynchronous I/O submit ID in `*id` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `reqs` or `id` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` or `priority` value is invalid |

## Description

This function submits asynchronous I/O read request(s) to the system. Multiple requests can be submitted at the same time. Only one asynchronous I/O submit ID will be assigned to the requests submitted with this function.

For `reqs`, specify an array of asynchronous I/O read requests.

For `num`, use a positive integer value to specify the number of asynchronous I/O read requests to submit. `SCE_KERNEL_AIO_REQUEST_NUM_MAX` is defined as the maximum value that can be specified.

For `priority`, specify the priority level of the asynchronous I/O read requests to submit with one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_PRIORITY_LOW` | 1 | Low priority |
| `SCE_KERNEL_AIO_PRIORITY_MID` | 2 | Middle priority |
| `SCE_KERNEL_AIO_PRIORITY_HIGH` | 3 | High priority |

When an asynchronous I/O request with a higher priority level exists, execution of asynchronous I/O requests with lower priority levels will be skipped. In addition, the order of execution of asynchronous I/O requests with the same priority level may change due to the system optimization processing.

When this function succeeds and the system receives all of the specified asynchronous I/O read requests, the asynchronous I/O submit ID will be stored in `*id` as an identifier. This submit ID can be used to wait for request completion or to cancel request(s). This submit ID will be valid until it is deleted with `sceKernelAioDeleteRequest()`/`sceKernelAioDeleteRequests()`.

Assigned submit IDs must be deleted. Refer to the "Description" of `sceKernelAioDeleteRequest()` for details.

Asynchronous I/O read request submission is successful when this function succeeds, but it does not mean that the requested asynchronous I/O read processing is successful. The submitted request content will be saved by the system upon execution of this function, but the validity of the requests will be confirmed upon the actual read processing. Therefore, note that even if this function succeeds, the actual read processing is not guaranteed to succeed.

In addition, valid data will be stored in each element in `reqs` as the read processing results after `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED` is obtained for the corresponding request state using `sceKernelAioWaitRequest()`/`sceKernelAioWaitRequests()`/`sceKernelAioPollRequest()`/`sceKernelAioPollRequests()`.

## Notes

`sceKernelAioSubmitReadCommandsMultiple()` is provided as a function that assigns an asynchronous I/O submit ID to each submitted asynchronous I/O read request.

## See Also

`SCE_KERNEL_AIO_*_NUM_MAX`, `sceKernelAioSubmitReadCommandsMultiple()`

# sceKernelAioSubmitReadCommandsMultiple

Submit asynchronous I/O read requests and assign a submit ID to each request

## Definition

```
#include <kernel.h>
int sceKernelAioSubmitReadCommandsMultiple(
    SceKernelAioRWRequest reqs[],
    int num,
    int priority,
    SceKernelAioSubmitId ids[]
)
```

## Arguments

|  |  |
| --- | --- |
| `reqs` | Array of asynchronous I/O read request structures |
| `num` | Number of `reqs` array elements |
| `priority` | Request priority level |
| `ids` | Array to store asynchronous I/O submit IDs |

## Return Values

Stores the asynchronous I/O submit IDs in `ids[]` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `reqs` or `ids` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` or `priority` value is invalid |

## Description

This function submits asynchronous I/O read request(s) to the system.

Other than assigning an asynchronous I/O submit ID to each specified request and storing the IDs in `ids[]`, this function has the same feature as `sceKernelAioSubmitReadCommands()`. Refer to the explanation of `sceKernelAioSubmitReadCommands()`.

## Notes

`sceKernelAioSubmitReadCommands()` is provided as a function that assigns a single asynchronous I/O submit ID to multiple submitted asynchronous I/O read requests.

## See Also

`sceKernelAioSubmitReadCommands()`

# sceKernelAioSubmitWriteCommands

Submit asynchronous I/O write requests and assign a single submit ID

## Definition

```
#include <kernel.h>
int sceKernelAioSubmitWriteCommands(
    SceKernelAioRWRequest reqs[],
    int num,
    int priority,
    SceKernelAioSubmitId *id
)
```

## Arguments

|  |  |
| --- | --- |
| `reqs` | Array of asynchronous I/O write request structures |
| `num` | Number of `reqs` array elements |
| `priority` | Request priority level |
| `id` | Destination to store asynchronous I/O submit ID |

## Return Values

Stores the asynchronous I/O submit ID in `*id` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `reqs` or `id` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` or `priority` value is invalid |

## Description

This function submits asynchronous I/O write request(s) to the system. Multiple requests can be submitted at the same time. Only one asynchronous I/O submit ID will be assigned to the requests submitted with this function.

For `reqs`, specify an array of asynchronous I/O write requests.

For `num`, use a positive integer value to specify the number of asynchronous I/O write requests to submit. `SCE_KERNEL_AIO_REQUEST_NUM_MAX` is defined as the maximum value that can be specified.

For `priority`, specify the priority level of the asynchronous I/O write requests to submit with one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_PRIORITY_LOW` | 1 | Low priority |
| `SCE_KERNEL_AIO_PRIORITY_MID` | 2 | Middle priority |
| `SCE_KERNEL_AIO_PRIORITY_HIGH` | 3 | High priority |

When an asynchronous I/O request with a higher priority level exists, execution of asynchronous I/O requests with lower priority levels will be skipped. In addition, the order of execution of asynchronous I/O requests with the same priority level may change due to the system optimization processing.

When this function succeeds and the system receives all of the specified asynchronous I/O write requests, the asynchronous I/O submit ID will be stored in `*id` as an identifier. This submit ID can be used to wait for request completion or to cancel request(s). This submit ID will be valid until it is deleted with `sceKernelAioDeleteRequest()`/`sceKernelAioDeleteRequests()`.

Assigned submit IDs must be deleted. Refer to the "Description" of `sceKernelAioDeleteRequest()` for details.

Asynchronous I/O write request submission is successful when this function succeeds, but it does not mean that the requested asynchronous I/O write processing is successful. The submitted request content will be saved by the system upon execution of this function, but the validity of the requests will be confirmed upon the actual write processing. Therefore, note that even if this function succeeds, the actual write processing is not guaranteed to succeed.

In addition, valid data will only be stored in each element in `reqs` as the write processing results after `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED` is obtained for the corresponding request state using `sceKernelAioWaitRequest()`/`sceKernelAioWaitRequests()`/`sceKernelAioPollRequest()`/`sceKernelAioPollRequests()`.

## Notes

`sceKernelAioSubmitWriteCommandsMultiple()` is provided as a function that assigns an asynchronous I/O submit ID to each submitted asynchronous I/O write request.

## See Also

`SCE_KERNEL_AIO_*_NUM_MAX`, `sceKernelAioSubmitWriteCommandsMultiple()`

# sceKernelAioSubmitWriteCommandsMultiple

Submit asynchronous I/O write requests and assign a submit ID to each request

## Definition

```
#include <kernel.h>
int sceKernelAioSubmitWriteCommandsMultiple(
    SceKernelAioRWRequest reqs[],
    int num,
    int priority,
    SceKernelAioSubmitId ids[]
)
```

## Arguments

|  |  |
| --- | --- |
| `reqs` | Array of asynchronous I/O write request structures |
| `num` | Number of `reqs` array elements |
| `priority` | Request priority level |
| `ids` | Array to store asynchronous I/O submit IDs |

## Return Values

Stores the asynchronous I/O submit IDs in `ids[]` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `reqs` or `ids` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` or `priority` value is invalid |

## Description

This function submits asynchronous I/O write request(s) to the system.

Other than assigning an asynchronous I/O submit ID to each specified request and storing the IDs in `ids[]`, this function has the same feature as `sceKernelAioSubmitWriteCommands()`. Refer to the explanation of `sceKernelAioSubmitWriteCommands()`.

## Notes

`sceKernelAioSubmitWriteCommands()` is provided as a function that assigns a single asynchronous I/O submit ID to multiple submitted asynchronous I/O write requests.

## See Also

`sceKernelAioSubmitWriteCommands()`

# sceKernelAioWaitRequest

Wait for the completion of the asynchronous I/O request(s) for a single specified asynchronous I/O submit ID

## Definition

```
#include <kernel.h>
int sceKernelAioWaitRequest(
    int id,
    int *state,
    SceKernelUseconds *usec
)
```

## Arguments

|  |  |
| --- | --- |
| `id` | Target asynchronous I/O submit ID to wait for completion |
| `state` | Destination to store the state (or error code) |
| `usec` | Timeout time (microseconds) or NULL |

## Return Values

Stores the obtained state in `*state` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `state` address is invalid |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |

## Description

This function waits for completion for the asynchronous I/O submit ID specified for `id`.

In other words, it waits for completion of the asynchronous I/O request(s) to which the specified submit ID is assigned. In `*state`, `SCE_KERNEL_AIO_STATE_COMPLETED` will be stored if all requests with the specified submit ID assigned are complete, and `SCE_KERNEL_AIO_STATE_ABORTED` will be stored if one or more request has been canceled. (For details about the state values, refer to "`SCE_KERNEL_AIO_STATE_*`".) Note that `SCE_KERNEL_AIO_STATE_COMPLETED` indicates that the system has completed asynchronous I/O processing, but it does not indicate that the processing has succeeded. Whether the asynchronous I/O processing has succeeded or failed will be stored in each `SceKernelAioRWRequest` structure specified upon request submission, check this structure as required.

Multiple threads can wait for the same submit ID. However, one of these threads will obtain just the state of the requests with the submit ID assigned, but a bitwise OR of the state and the following value will be stored in `*state` for the other threads.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_STATE_NOTIFIED` | 0x10000 | Wait already performed |

Similarly, a bitwise OR of the aforementioned values will also be stored in `*state` and this function will immediately return when a wait is performed for a submit ID for which a wait has already been performed.

The following error code (negative value) will be stored in `*state` when a wait fails.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified submit ID is invalid |

However, note that the call of this function will succeed and `SCE_OK` will be returned at such times.

A timeout time can be specified for `usec`. A timeout will occur if the specified submit ID has not completed when the specified time elapses. When a timeout occurs, this function will return `SCE_KERNEL_ERROR_ETIMEDOUT`, and the state at this time will be stored in `*state`. When a wait succeeds without a timeout occurring, the remaining time until the timeout will be stored in `*usec`. When NULL is specified for `usec`, this function will perform blocking until the specified submit ID completes. Specification to `usec` can be made in microsecond units. However, the precision of actual processing is in millisecond units.

When this function returns `SCE_KERNEL_ERROR_EFAULT`, whether the wait succeeded or failed will be undefined. Specify an appropriate `state`, call this function again, and check the results.

## Notes

* `sceKernelAioWaitRequests()` is provided as a function that waits for completion of the asynchronous I/O request(s) for multiple specified asynchronous I/O submit IDs.
* To obtain the state of asynchronous I/O request(s) without performing blocking, use `sceKernelAioPollRequest()` or `sceKernelAioPollRequests()`.

## See Also

`SCE_KERNEL_AIO_STATE_*`, `sceKernelAioWaitRequests()`, `sceKernelAioPollRequest()`, `sceKernelAioPollRequests()`

# sceKernelAioWaitRequests

Wait for the completion of asynchronous I/O requests for multiple specified asynchronous I/O submit IDs

## Definition

```
#include <kernel.h>
int sceKernelAioWaitRequests(
    int ids[],
    int num,
    int states[],
    uint32_t mode,
    SceKernelUseconds *usec
)
```

## Arguments

|  |  |
| --- | --- |
| `ids` | Array of target asynchronous I/O submit IDs to wait for completion |
| `num` | Number of `ids` array elements |
| `states` | Array to store states (or error codes) |
| `mode` | Completion wait mode |
| `usec` | Timeout time (microseconds) or NULL |

## Return Values

Stores the obtained states in `states[]` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `ids` or `states` address is invalid |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `num` or `mode` value is invalid |
| `SCE_KERNEL_ERROR_ETIMEDOUT` | 0x8002003c | Timed out |

## Description

This function waits for completion for the multiple asynchronous I/O submit IDs specified for `ids`. In other words, it waits for completion of the asynchronous I/O requests to which the specified submit IDs are assigned.

For `num`, use a positive integer value to specify the number of submit IDs specified for `ids`. `SCE_KERNEL_AIO_ID_NUM_MAX` is defined as the maximum value that can be specified.

In `states[]`, `SCE_KERNEL_AIO_STATE_COMPLETED` will be stored if all requests with the specified submit IDs assigned are complete, and `SCE_KERNEL_AIO_STATE_ABORTED` will be stored if one or more request has been canceled. (For details about the state values, refer to "`SCE_KERNEL_AIO_STATE_*`".) Note that `SCE_KERNEL_AIO_STATE_COMPLETED` indicates that the system has completed asynchronous I/O processing, but it does not indicate that the processing has succeeded. Whether the asynchronous I/O processing has succeeded or failed will be stored in each `SceKernelAioRWRequest` structure specified upon request submission, check this structure as required.

Multiple threads can wait for the same submit ID. However, one of these threads will obtain just the state of the requests with the submit ID assigned, but a bitwise OR of the state and the following value will be stored in `states[]` for the other threads.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_STATE_NOTIFIED` | 0x10000 | Wait already performed |

Similarly, a bitwise OR of the aforementioned values will also be stored in `states[]` and this function will immediately return when a wait is performed for a submit ID for which a wait has already been performed.

The following error code (negative value) will be stored in `states[]` when a wait fails.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | Specified submit ID is invalid |

However, note that the call of this function will succeed and `SCE_OK` will be returned at such times.

For `mode`, specify a completion wait mode with one of the following values. Note that the `mode` value will be ignored when `num` is 1, and the operation will be the same as when `SCE_KERNEL_AIO_WAIT_AND` is specified.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_AIO_WAIT_AND` | 0x01 | Wait for completion for all specified asynchronous I/O submit IDs |
| `SCE_KERNEL_AIO_WAIT_OR` | 0x02 | Wait for completion of one of the specified asynchronous I/O submit IDs |

A timeout time can be specified for `usec`. A timeout will occur if the specified submit IDs have not completed in the specified `mode` when the specified time elapses. When a timeout occurs, this function will return `SCE_KERNEL_ERROR_ETIMEDOUT`, and the states at this time will be stored in `states[]`. When a wait succeeds without a timeout occurring, the remaining time until the timeout will be stored in `*usec`. When NULL is specified for `usec`, this function will perform blocking in the specified `mode` until the specified submit IDs complete. Specification to `usec` can be made in microsecond units. However, the precision of actual processing is in millisecond units.

When this function returns `SCE_KERNEL_ERROR_EFAULT` due to `states` being invalid, whether the wait succeeded or failed will be undefined. Specify an appropriate `states`, call this function again, and check the results.

## Notes

* `sceKernelAioWaitRequest()` is provided as a function that waits for completion of the asynchronous I/O request(s) for a single specified asynchronous I/O submit ID.
* To obtain the state of asynchronous I/O request(s) without performing blocking, use `sceKernelAioPollRequest()` or `sceKernelAioPollRequests()`.

## See Also

`SCE_KERNEL_AIO_*_NUM_MAX`, `SCE_KERNEL_AIO_STATE_*`, `sceKernelAioWaitRequest()`, `sceKernelAioPollRequest()`, `sceKernelAioPollRequests()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.