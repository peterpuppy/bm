# NpAuth Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Reference/sce-np-auth-abort-request.html

# Request Operations

# SCE\_NP\_AUTH\_MAX\_REQUEST\_NUM

Maximum number of requests

## Definition

```
#include <np/np_auth.h>
#define SCE_NP_AUTH_MAX_REQUEST_NUM	(16)
```

## Description

This constant indicates the maximum number of requests that can exist at one time in the NpAuth library.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`

# SceNpAuthCreateAsyncRequestParameter

Asynchronous processing request creation parameters

## Definition

```
#include <np/np_auth.h>
typedef struct SceNpAuthCreateAsyncRequestParameter {
	size_t size;
	SceKernelCpumask cpuAffinityMask;
	int threadPriority;
	uint8_t padding[4];
} SceNpAuthCreateAsyncRequestParameter;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `cpuAffinityMask` | Affinity mask of internal thread, or 0 |
| `threadPriority` | Priority of internal thread, or 0 |
| `padding` | Not used |

## Description

This structure indicates the parameters for the internal thread specified during an `sceNpAuthCreateAsyncRequest()` call.

For `size`, specify the size of this structure.

For `cpuAffinityMask`, set an affinity mask for internal threads that will perform communication processing. Using an `SCE_KERNEL_CPUMASK_*` macro is recommended. The system will set an affinity mask when 0 is specified.

For `threadPriority`, specify the priority for internal threads that will perform communication processing. Using an `SCE_KERNEL_PRIO_*` macro is recommended. If 0 is specified, the system will set the priority.

# sceNpAuthCreateAsyncRequest

Create asynchronous processing request for NpAuth

## Definition

```
#include <np/np_auth.h>
int sceNpAuthCreateAsyncRequest(
	const SceNpAuthCreateAsyncRequestParameter *pParam
);
```

## Arguments

|  |  |
| --- | --- |
| `pParam` | Initialization parameters for the internal thread |

## Return Values

Returns the request ID (>0) for normal termination.

Returns a negative value for an error. The main error codes are shown below; however, the application must not malfunction even if other error codes are returned. (Note that 0 is never returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | Specified argument is invalid |
| `SCE_NP_AUTH_ERROR_INVALID_SIZE` | 0x80550302 | `pParam`->`size` is invalid |
| `SCE_NP_AUTH_ERROR_OUT_OF_MEMORY` | 0x80550303 | Not enough free memory |
| `SCE_NP_AUTH_ERROR_REQUEST_MAX` | 0x80550305 | Created more than 16 requests at one time.  (Check to see that `sceNpAuthDeleteRequest()` was called as necessary.) |

## Description

This function creates a request used with the NpAuth Library.

This function creates a request for asynchronous processing. When using this request to execute a communication processing function, the function will be executed as an asynchronous function.

A request is an object that is used up for each communication processing function. A request must always be created before using these functions. A used-up request must then be deleted with `sceNpAuthDeleteRequest()`.

The maximum number of requests that can exist at the same time is `SCE_NP_AUTH_MAX_REQUEST_NUM` (= 16).

# sceNpAuthCreateRequest

Create synchronous processing request for NpAuth

## Definition

```
#include <np/np_auth.h>
int sceNpAuthCreateRequest(
	void
);
```

## Arguments

None

## Return Values

Returns the request ID (>0) for normal termination.

Returns a negative value for an error. The main error codes are shown below; however, the application must not malfunction even if other error codes are returned. (Note that 0 is never returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_OUT_OF_MEMORY` | 0x80550303 | Not enough free memory |
| `SCE_NP_AUTH_ERROR_REQUEST_MAX` | 0x80550305 | Created more than 16 requests at one time.  (Check to see that `sceNpAuthDeleteRequest()` was called as necessary.) |

## Description

This function creates a request used with the NpAuth Library.

This function creates a request for synchronous processing. When this request is used to execute a communication processing function, the function will be executed as a synchronous function.

A request is an object that is used up for each communication processing function. A request must always be created before using these functions. A used-up request must then be deleted with `sceNpAuthDeleteRequest()`.

The maximum number of requests that can exist at the same time is `SCE_NP_AUTH_MAX_REQUEST_NUM` (= 16).

# sceNpAuthAbortRequest

Abort communication processing

## Definition

```
#include <np/np_auth.h>
int sceNpAuthAbortRequest(
	int reqId
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID of the communication processing to abort |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0) |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |

## Description

This function aborts communication processing.

For `reqId`, specify the ID of the request for the communication processing you wish to abort.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`

# sceNpAuthDeleteRequest

Delete the NpAuth request

## Definition

```
#include <np/np_auth.h>
int sceNpAuthDeleteRequest(
	int reqId
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0) |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |

## Description

This function deletes a request used by the library.

## Notes

When asynchronous processing is being executed and this function is called in an attempt to delete a request before processing completes, blocking may be performed for long periods of time in order to abort the processing. If asynchronous processing has been executed, this function must not be called from a time-critical thread.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`

# sceNpAuthSetTimeout

Set a timeout period for communication processing functions

## Definition

```
#include <np/np_auth.h>
#define SCE_NP_AUTH_TIMEOUT_NO_EFFECT	(0)

int sceNpAuthSetTimeout(
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
| `reqId` | NpAuth request ID |
| `resolveRetry` | Name resolution retry times |
| `resolveTimeout` | Name resolution timeout time (microseconds) |
| `connTimeout` | Timeout time when connecting (microseconds) |
| `sendTimeout` | Sending timeout time (microseconds) |
| `recvTimeout` | Receiving timeout time (microseconds) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0) or an invalid value was specified for `timeout` |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |

## Description

This function sets the timeout period for various stages of communication processing.

For `reqId`, specify an NpAuth request ID.

Specify the timeout period in microseconds. The values that can be set are as follows:

| **Argument** | **Settable values** |
| --- | --- |
| `resolveRetry` | 1 or more, or `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` |
| `resolveTimeout` | 1 second or more, or `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` |
| `connTimeout` | 10 seconds or more, or `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` |
| `sendTimeout` | 10 seconds or more, or `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` |
| `recvTimeout` | 10 seconds or more, or `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` |

When `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` is set for one of these arguments, the internal default value will be used for the argument's setting. However, it is not possible to set `SCE_NP_AUTH_TIMEOUT_NO_EFFECT` for all the arguments.

## Notes

* Instead of using this function to set your own timeout period, try to use the default timeout period wherever possible.
* This function cannot set the total timeout time; it cannot be used for the purpose of guaranteeing that communication processing will complete within a certain amount of time. For the purpose of preventing user operation from being blocked for extensive periods of time, it is recommended that `sceNpAuthAbortRequest()` be used to implement timeouts and user cancellation in the application.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`

# sceNpAuthWaitAsync

Obtain asynchronous request execution results

## Definition

```
#include <np/np_auth.h>
int sceNpAuthWaitAsync(
	int reqId,
	int *pResult
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID of the asynchronous request to obtain result for |
| `pResult` | Destination to store the results of the asynchronous request |

## Return Values

Stores the asynchronous request results in `*pResult` and returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0) or NULL specified to `pResult` |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |

## Description

This function obtains the execution result of a request executed asynchronously.

For `reqId`, specify the request ID of the communication function started by the asynchronous request.

This function waits for this request to complete if it hasn't already done so, stores the result of the request in `*pResult` and returns 0 for the return value. Make sure that the `*pResult` value is appropriately evaluated as a request execution result.

If the `*pResult` value is 0x82XXXXXX, it means a server error code. For details, refer to [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html).

## Notes

* This function may perform blocking for long periods of time. This function must not be called from a time-critical thread.
* `sceNpAuthPollAsync()` is provided as a non-blocking function that looks up whether or not an asynchronously executed request is complete.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`

# sceNpAuthPollAsync

Obtain asynchronous request execution results

## Definition

```
#include <np/np_auth.h>
int sceNpAuthPollAsync(
	int reqId,
	int *pResult
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID of the asynchronous request to obtain result for |
| `pResult` | Destination to store the results of the request |

## Return Values

Returns one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_POLL_ASYNC_RET_FINISHED` | 0 | Asynchronous processing finished |
| `SCE_NP_AUTH_POLL_ASYNC_RET_RUNNING` | 1 | Asynchronous processing is still running |

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0) or NULL specified to `pResult` |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |

## Description

This function obtains the execution result of a request executed asynchronously.

For `reqId`, specify the request ID of the communication function started by the asynchronous request.

`SCE_NP_AUTH_POLL_ASYNC_RET_RUNNING` will be returned for the return value if the request has not completed yet. In this case, the value of `*pResult` does not change.

If the request is already completed, the result of the request will be stored in `*pResult` and `SCE_NP_AUTH_POLL_ASYNC_RET_FINISHED` will be returned for the return value. Make sure that the `*pResult` value is appropriately evaluated as a request execution result. If the `*pResult` value is 0x82XXXXXX, it means a server error code. For details, refer to [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html).

## Notes

`sceNpAuthWaitAsync()` is provided as a function that waits until an asynchronously executed request completes to obtain the execution result.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`