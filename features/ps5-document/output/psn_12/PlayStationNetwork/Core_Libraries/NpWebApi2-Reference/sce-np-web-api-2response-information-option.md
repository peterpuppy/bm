# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2response-information-option.html

# Requests

# SCE\_NP\_WEBAPI2\_CONTENT\_TYPE\_APPLICATION\_JSON\_UTF8

Type of data to send as a request body

## Definition

| **Value** | **(String)** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_CONTENT_TYPE_APPLICATION_JSON_UTF8` | `"application/json; charset=utf-8"` | Content-Type representing JSON format data |

## Description

This constant represents the type of data to send as a request body when executing a Web API. It is used as the Content-Type value for the HTTP request header.

# SceNpWebApi2HttpMethod, SCE\_NP\_WEBAPI2\_HTTP\_METHOD\_\*

HTTP method upon Web API execution

## Definition

```
#include <np/np_webapi2.h>
#define SCE_NP_WEBAPI2_HTTP_METHOD_GET    "GET"
#define SCE_NP_WEBAPI2_HTTP_METHOD_POST   "POST"
#define SCE_NP_WEBAPI2_HTTP_METHOD_PUT    "PUT"
#define SCE_NP_WEBAPI2_HTTP_METHOD_DELETE "DELETE"
#define SCE_NP_WEBAPI2_HTTP_METHOD_PATCH  "PATCH"
typedef const char* SceNpWebApi2HttpMethod;
```

## Description

These constants represent the HTTP method to specify when executing a Web API.

| **Value** | **String** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_HTTP_METHOD_GET` | "GET" | `GET` method |
| `SCE_NP_WEBAPI2_HTTP_METHOD_POST` | "POST" | `POST` method |
| `SCE_NP_WEBAPI2_HTTP_METHOD_PUT` | "PUT" | `PUT` method |
| `SCE_NP_WEBAPI2_HTTP_METHOD_DELETE` | "DELETE" | `DELETE` method |
| `SCE_NP_WEBAPI2_HTTP_METHOD_PATCH` | "PATCH" | `PATCH` method |

# SceNpWebApi2ContentParameter

Parameters for data to send as request body

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2ContentParameter {
	size_t contentLength;
	const char *pContentType;
	uint8_t reserved[16];
} SceNpWebApi2ContentParameter;
```

## Members

|  |  |
| --- | --- |
| `contentLength` | Total size of the data to send as a request body upon Web API execution (bytes) |
| `pContentType` | Character string to be set for Content-Type of the HTTP header (ASCIIZ string) |
| `reserved` | Reserved area |

## Description

This structure holds the parameters for the data to send as a request body when executing a Web API.

When sending in JSON format (the send data format of many Web APIs), `SCE_NP_WEBAPI2_CONTENT_TYPE_APPLICATION_JSON_UTF8` can be specified for `pContentType`.

For details on the character strings that should be set for `pContentType`, refer to the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document and the references for each Web API.

# SceNpWebApi2ResponseInformationOption

Option information regarding Web API server response

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2ResponseInformationOption {
	int32_t httpStatus;
	char *pErrorObject;
	size_t errorObjectSize;
	size_t responseDataSize;
} SceNpWebApi2ResponseInformationOption;
```

## Members

|  |  |
| --- | --- |
| `httpStatus` | HTTP status code |
| `pErrorObject` | Pointer to buffer to store response body upon server error, or NULL |
| `errorObjectSize` | Size of buffer to store response body upon server error, or 0 |
| `responseDataSize` | Actual size of response body upon server error |

## Description

This structure is for storing the server response content if an error has occurred when the Web APIs are executed with `sceNpWebApi2SendRequest()`.

When a server error has occurred, `sceNpWebApi2SendRequest()` will return an appropriate error code based on the server response. Therefore, applications do not normally need to obtain information of this structure. Use this structure in cases such as when it is desired to perform a detailed investigation of the cause of errors during development.

`pErrorObject` stores information about the error object when there is a response from the error object described in [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html). When an error occurs in communication processing of a lower layer, no information is stored in `pErrorObject` because a Web API error has not been encountered.

If obtaining a response body is not required (when it is desired to only obtain the HTTP status code), set NULL for `pErrorObject` or set 0 for `errorObjectSize`.

# sceNpWebApi2AbortRequest

Abort request processing

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2AbortRequest(
	int64_t requestId
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function aborts the request processing.

The processing of `sceNpWebApi2SendRequest()` and `sceNpWebApi2ReadData()` will be aborted. Communication with the server will be immediately aborted, and currently processing functions will immediately return.

## Examples

```
int32_t ret = 0;
int64_t requestId;

ret = sceNpWebApi2AbortRequest(requestId);
if(ret < 0){
	/* Error handling */
}
```

# sceNpWebApi2CreateRequest

Create request

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2CreateRequest(
	int32_t userCtxId,
	const char *pApiGroup,
	const char *pPath,
	SceNpWebApi2HttpMethod method,
	const SceNpWebApi2ContentParameter *pContentParameter,
	int64_t *pRequestId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `pApiGroup` | API group of the Web API to execute (ASCIIZ string) |
| `pPath` | Path of the Web API to execute (ASCIIZ string) |
| `method` | HTTP method upon Web API execution |
| `pContentParameter` | Parameters relating to the data to send as request body, or NULL |
| `pRequestId` | Storage destination for the obtained request ID |

## Return Values

Stores the obtained request ID in `*pRequestId` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function creates a request for executing a Web API. When the request is properly created, the request ID will be stored in `*pRequestId`.

The path specified for `pPath` is a character string that links the resource path of the Web API to execute and the query string. This character string must always be percent-encoded (URL-encoded) based on RFC 3986.

For `method`, specify a constant indicating the HTTP method (`SCE_NP_WEBAPI2_HTTP_METHOD_GET`, etc.).

For `*pContentParameter`, if sending data upon Web API execution, specify a `SceNpWebApi2ContentParameter` structure that stores the parameters relating to the data. If there is no data to send, specify NULL. Because this structure will be deep-copied within `sceNpWebApi2CreateRequest()`, it doesn't need to be kept on the application side.

## Examples

```
#define API_GROUP "userProfile"
#define PATH "/v1/users/user000/profile"

int32_t ret = 0;
int32_t userCtxId;
int64_t requestId = 0;

ret = sceNpWebApi2CreateRequest(
	userCtxId, API_GROUP, PATH,
	SCE_NP_WEBAPI2_HTTP_METHOD_GET, 
	NULL, &requestId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2DeleteRequest()`

# sceNpWebApi2DeleteRequest

Delete request

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2DeleteRequest(
	int64_t requestId
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function deletes a request.

If the request is being used for sending/receiving data, `SCE_NP_WEBAPI2_ERROR_REQUEST_BUSY` will be returned. Execute this function after all processing completes.

## Examples

```
int32_t ret = 0;
int64_t requestId;

ret = sceNpWebApi2DeleteRequest(requestId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2CreateRequest()`

# sceNpWebApi2ReadData

Receive response body

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2ReadData(
	int64_t requestId,
	void *pData,
	size_t size
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |
| `pData` | Storage destination for the obtained response body |
| `size` | Size of the buffer specified with `pData` (bytes) |

## Return Values

Stores the obtained response body in the `*pData` buffer and returns the size of the stored data for normal termination. Returns 0 if all response bodies have already been received and there is no data to be stored in the buffer.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function receives the response body of the request specified with `requestId`. The received response body will be written to the address specified with `pData`.

This function is a blocking function. The conditions for this function to return will be one of the following:

* (a) Data in bytes specified with `size` was received and stored in the buffer
* (b) If Content-Length is in the HTTP response header, a response body of the size specified with Content-Length was received completely and stored in the buffer
* (c) `sceNetRecv()` returned 0 or a negative value after being called in the library
* (d) If chunk encoded data is being received, the last chunk was received completely and stored in the buffer
* (e) `sceNpWebApi2AbortRequest()` was executed in another thread
* (f) The timeout period set with `sceNpWebApi2SetRequestTimeout()` has elapsed

In the case of [(a)](sce-np-web-api-2read-data.html#np-web-api2-library-reference_2_8__np-web-api2-library-reference_2_8_4_1), there is a possibility that the entire response body has not been received/stored completely. The entire response body can be obtained by repeatedly calling this function until 0 returns.

## Examples

```
int64_t requestId; // Request ID of the request to send

int32_t ret = 0;
char buf[2*1024];

do {
	ret = sceNpWebApi2ReadData(requestId, buf, sizeof(buf));
	if(ret < 0){
		/* Error handling */
	}
	else if (ret > 0) {
		printf("sceNpWebApi2ReadData() read %d bytes\n", ret);
	}
} while (ret > 0);
```

## Notes

This function is a blocking function. Processing may take time; therefore, it should be called from a subthread.

## See Also

`sceNpWebApi2SendRequest()`

# sceNpWebApi2SendRequest

Send request and execute Web API

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2SendRequest(
	int64_t requestId,
	const void *pData,
	size_t dataSize,
	SceNpWebApi2ResponseInformationOption *pRespInfoOption
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |
| `pData` | Data to send as request body (all or part), or NULL |
| `dataSize` | Size of data pointed to by `pData` (bytes), or 0 |
| `pRespInfoOption` | Structure to store server response content upon server error, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function sends the request specified with `requestId` to the server and executes a Web API.

If there is data to send as a request body upon Web API execution, place the data in memory then specify `pData` and `dataSize`.

There is no need to send the entire data at once; it is also possible to partition the data and send it by calling this function multiple times. In order to properly partition and send data, specify the total size of the data for `contentLength` of \**`pContentParameter`* when creating the request with `sceNpWebApi2CreateRequest()`.

When a server error has occurred, the error response data will be obtained internally by this function, then an error code (0x82XXXXXX) that indicates the server error will be generated and will be returned as the return value of this function.

The return of the 0x82200284 or 0x82200182 error code indicates that an invalid NP Title ID or NP Title Secret is set. Check if the NP Title ID and NP Title Secret set by `sceNpSetNpTitleId()` are correct.

To obtain the error response data for development purposes, specify a pointer to the structure to store the response content for `*pRespInfoOption`.

This function is a blocking function. The conditions for this function to return are as follows:

* If there is no data to send as a request body:

  This function returns when the request has been sent to the server and the HTTP response header has been received.
* If there is data to send as a request body:

  If the entire send data size set with `contentLength` of `*pContentParameter` is still being sent, this function returns when data in the size specified with this function call has been sent. If the entire send data size has been sent, this function returns when the HTTP response header has been received from the server.
* When a function that aborts request processing has been executed in another thread:

  When `sceNpWebApi2AbortRequest()` is executed for a request that is being processed by this function, this function will abort processing of the request and immediately return. At this time, `SCE_NP_WEBAPI2_ERROR_ABORTED` will be returned as a return value.
* When the timeout period set with `sceNpWebApi2SetRequestTimeout()` has elapsed:

  When a timeout occurs, this function aborts request processing and then returns. At this time, `SCE_NP_WEBAPI2_ERROR_TIMEOUT` will be returned as a return value.

## Examples

```
int32_t ret = 0;
int64_t requestId;

char errorObjectBuf[ERROR_OBJECT_BUF_SIZE];
memset(errorObjectBuf, 0, sizeof(errorObjectBuf));

SceNpWebApi2ResponseInformationOption respInfoOption;
memset(&respInfoOption, 0, sizeof(respInfoOption));
respInfoOption.pErrorObject = errorObjectBuf;
respInfoOption.errorObjectSize = sizeof(errorObjectBuf);

ret = sceNpWebApi2SendRequest(requestId, NULL, 0, &respInfoOption);
if(ret < 0){
	/* Error handling */
}
```

## Notes

This function is a blocking function. Processing may take time; therefore, it should be called from a subthread.

## See Also

`sceNpWebApi2ReadData()`