# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/request-operations.html

# Request Operations

# SCE\_NP\_MAX\_REQUEST\_NUM

Maximum number of requests

## Definition

```
#include <np.h>

#define SCE_NP_MAX_REQUEST_NUM	(32)
```

## Description

This constant indicates the maximum number of requests that can exist at one time in the Np library.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`

# SceNpCreateAsyncRequestParameter

Asynchronous processing request creation parameters

## Definition

```
#include <np/np_common.h>
typedef struct SceNpCreateAsyncRequestParameter {
	size_t size;
	SceKernelCpumask cpuAffinityMask;
	int threadPriority;
	uint8_t padding[4];
} SceNpCreateAsyncRequestParameter;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `cpuAffinityMask` | Affinity mask of internal thread, or 0 |
| `threadPriority` | Priority of internal thread, or 0 |
| `padding` | Not used (clear with 0's) |

## Description

This structure indicates the parameters for the internal thread specified during a `sceNpCreateAsyncRequest()` call.

For `size`, specify the size of this structure.

For `cpuAffinityMask`, set an affinity mask for internal threads that will perform communication processing. Using an `SCE_KERNEL_CPUMASK_*` macro is recommended. The system will set an affinity mask when 0 is specified.

For `threadPriority`, specify the priority for internal threads that will perform communication processing. Using an `SCE_KERNEL_PRIO_*` macro is recommended. The system will set the priority when 0 is specified.

Clear `padding` with 0's.

# sceNpCreateAsyncRequest

Creates an asynchronous processing request for the Np library

## Definition

```
#include <np.h>
int sceNpCreateAsyncRequest(
	const SceNpCreateAsyncRequestParameter *pParam
);
```

## Arguments

|  |  |
| --- | --- |
| `pParam` | Initialization parameters for the internal thread (IN) |

## Return Values

Returns the request ID (>0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_INVALID_SIZE` | 0x80550011 | `pParam`->`size` is invalid |
| `SCE_NP_ERROR_REQUEST_MAX` | 0x80550013 | Created more than 32 requests at one time. (Check to see that `sceNpDeleteRequest()` was called as necessary.) |

## Description

This function creates a request used with the Np Library.

This function creates a request for asynchronous processing. When using this request to execute a communication processing function, the function will be executed as an asynchronous function.

A request is an object that is used up for each communication processing function. A request must always be created before using these functions. A used-up request must be deleted with `sceNpDeleteRequest()`.

The maximum number of requests that can exist at the same time is `SCE_NP_MAX_REQUEST_NUM` (= 32).

# sceNpCreateRequest

Creates a synchronous processing request for the Np library

## Definition

```
#include <np.h>
int sceNpCreateRequest(
	void
);
```

## Arguments

None

## Return Values

Returns the request ID (>0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_REQUEST_MAX` | 0x80550013 | Created more than 32 requests at one time. (Check to see that `sceNpDeleteRequest()` was called as necessary.) |

## Description

This function creates a request used with the Np Library.

This function creates a request for synchronous processing. When this request is used to execute a communication processing function, the function will be executed as a synchronous function.

A request is an object that is used up for each communication processing function. A request must always be created before using these functions. A used-up request must be deleted with `sceNpDeleteRequest()`.

The maximum number of requests that can exist at the same time is `SCE_NP_MAX_REQUEST_NUM` (= 32).

# sceNpAbortRequest

Aborts communication processing

## Definition

```
#include <np.h>
int sceNpAbortRequest(
	int reqId
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID of the communication processing to abort (IN) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0) |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550013 | Request specified for `reqId` does not exist |

## Description

This function aborts communication processing.

For `reqId`, specify the ID of the request for the communication processing you wish to abort.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`

# sceNpDeleteRequest

Deletes the Np request

## Definition

```
#include <np.h>
int sceNpDeleteRequest(
	int reqId
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID (IN) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0) |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function deletes a request used by the library.

## Notes

When executing asynchronous processing and attempting to delete a request by calling this function before processing has completed, a long blocking time may be entailed for aborting the processing. When executing asynchronous processing, this function must not be called from a time-critical thread.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`

# sceNpSetTimeout

Sets a timeout period for communication processing functions

## Definition

```
#include <np.h>
#define SCE_NP_TIMEOUT_NO_EFFECT	(0)

int sceNpSetTimeout(
	int reqId,
	int32_t resolveRetry,
	uint32_t resolveTimeout,
	uint32_t connTimeout,
	uint32_t sendTimeout,
	uint32_t recvTimeout
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID (IN) |
| `resolveRetry` | Name resolution retry times (IN) |
| `resolveTimeout` | Name resolution timeout time (microseconds) (IN) |
| `connTimeout` | Timeout time when connecting (microseconds) (IN) |
| `sendTimeout` | Sending timeout time (microseconds) (IN) |
| `recvTimeout` | Receiving timeout time (microseconds) (IN) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0) or an invalid value was specified for `timeout` |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function sets the timeout period for communication processing.

For `reqId`, specify a request ID.

Specify the timeout period in microseconds. The values that can be set are as follows:

| **Argument** | **Values That Can Be Set** |
| --- | --- |
| `resolveRetry` | 1 or more, or `SCE_NP_TIMEOUT_NO_EFFECT` |
| `resolveTimeout` | 1 second or more, or `SCE_NP_TIMEOUT_NO_EFFECT` |
| `connTimeout` | 10 seconds or more, or `SCE_NP_TIMEOUT_NO_EFFECT` |
| `sendTimeout` | 10 seconds or more, or `SCE_NP_TIMEOUT_NO_EFFECT` |
| `recvTimeout` | 10 seconds or more, or `SCE_NP_TIMEOUT_NO_EFFECT` |

When `SCE_NP_TIMEOUT_NO_EFFECT` is set for one of these arguments, the internal default value will be used for the argument's setting. However, it is not possible to set `SCE_NP_TIMEOUT_NO_EFFECT` for all the arguments.

## Notes

* Instead of using this function to set your own timeout period, try to use the default timeout period wherever possible.
* With the values set with this function, it is possible to set the timeout time for each processing, but not the total timeout time; processing is not guaranteed to end within that time. For the purpose of preventing user operations from being blocked over long periods of time, it is recommended to use `sceNpAbortRequest()` to implement timeouts and allow users to cancel in the application.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`

# sceNpWaitAsync

Obtains asynchronous request execution results

## Definition

```
#include <np.h>
int sceNpWaitAsync(
	int reqId,
	int *pResult
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID of the asynchronous request to obtain result for (IN) |
| `pResult` | Destination to store the results of the asynchronous request (OUT) |

## Return Values

Stores the asynchronous request results in `*pResult` and returns 0 for normal termination. Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0) or NULL was specified to `pResult` |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function obtains the execution result of a request executed asynchronously.

For `reqId`, specify the request ID of the communication function started by the asynchronous request.

This function waits for this request to complete if it hasn't already done so, stores the result of the request in `*pResult` and returns 0 for the return value. Make sure the \*`pResult` value is appropriately evaluated as a request execution result.

## Notes

* This function may entail a long blocking time. This function must not be called from a time-critical thread.
* `sceNpPollAsync()` is provided as a non-blocking function that looks up whether or not an asynchronously executed request is complete.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`

# sceNpPollAsync

Obtains asynchronous request execution results

## Definition

```
#include <np.h>
int sceNpPollAsync(
	int reqId,
	int *pResult
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID of the asynchronous request to obtain result for (IN) |
| `pResult` | Destination to store the results of the request (OUT) |

## Return Values

Returns one of the following values for normal termination. (The values stored in `*pResult` will be explained later.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_POLL_ASYNC_RET_FINISHED` | 0 | Asynchronous processing finished |
| `SCE_NP_POLL_ASYNC_RET_RUNNING` | 1 | Asynchronous processing is still running |

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0) or NULL was specified to `pResult` |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function obtains the execution result of a request executed asynchronously.

For `reqId`, specify the request ID of the communication function started by the asynchronous request.

`SCE_NP_POLL_ASYNC_RET_RUNNING` will be returned for the return value if the request has not completed yet. In this case, the value of `*pResult` does not change.

If the request is already completed, the result of the request will be stored in `*pResult`, and `SCE_NP_POLL_ASYNC_RET_FINISHED` will be returned for the return value. Make sure the \*`pResult` value is appropriately evaluated as a request execution result.

## Notes

`sceNpWaitAsync()` is provided as a function that waits until an asynchronously executed request completes to obtain the execution result.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`