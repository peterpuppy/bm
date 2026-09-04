# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2check-timeout.html

# Timeout

# sceNpWebApi2CheckTimeout

Check timeout

## Definition

```
#include <np/np_webapi2.h>
void sceNpWebApi2CheckTimeout(
	void
);
```

## Arguments

None

## Return Values

Always ends in normal termination.

## Description

This function checks whether the processing of the request/handle to which a timeout was set with `sceNpWebApi2SetRequestTimeout()`/`sceNpWebApi2PushEventSetHandleTimeout()` timed out.

The application must periodically call this function when using `sceNpWebApi2SetRequestTimeout()`/`sceNpWebApi2PushEventSetHandleTimeout()`.

# sceNpWebApi2SetRequestTimeout

Set timeout to a request

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2SetRequestTimeout(
	int64_t requestId,
	uint32_t timeout
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of a request to set timeout to |
| `timeout` | Timeout time (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function sets a timeout to a request.

After creating a request with `sceNpWebApi2CreateRequest()`, call this function to set a timeout before executing `sceNpWebApi2SendRequest()` or `sceNpWebApi2ReadData()`, and periodically call `sceNpWebApi2CheckTimeout()`.

When a timeout occurs, `sceNpWebApi2SendRequest()` and `sceNpWebApi2ReadData()` will return the `SCE_NP_WEBAPI2_ERROR_TIMEOUT` error.

## Examples

```
int32_t ret = 0;
int64_t requestId;

ret = sceNpWebApi2SetRequestTimeout(requestId, 10*1000*1000);
if(ret < 0){
	/* Error handling */
}
```