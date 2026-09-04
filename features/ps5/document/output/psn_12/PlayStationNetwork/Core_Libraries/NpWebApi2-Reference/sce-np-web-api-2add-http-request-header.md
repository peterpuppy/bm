# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2add-http-request-header.html

# HTTP Headers

# sceNpWebApi2AddHttpRequestHeader

Add an HTTP request header

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2AddHttpRequestHeader(
	int64_t requestId,
	const char *pFieldName,
	const char *pValue
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |
| `pFieldName` | Field name of the HTTP header to add (ASCIIZ string) |
| `pValue` | Value of the HTTP header to add (ASCIIZ string) |

## Return Values

Returns `SCE_OK`(=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function adds an HTTP header to the HTTP request upon Web API execution. After creating the request with `sceNpWebApi2CreateRequest()` and before sending the request with `sceNpWebApi2SendRequest()`, add an HTTP header with this function.

## Examples

```
int32_t ret = 0; 
int64_t requestId;

ret = sceNpWebApi2AddHttpRequestHeader(
	requestId, "My-Header-Name", "My-Header-Value");
if(ret < 0){
	/* Error handling */
}
```

# sceNpWebApi2GetHttpResponseHeaderValue

Get the value of the HTTP response data

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2GetHttpResponseHeaderValue(
	int64_t requestId,
	const char *pFieldName,
	char *pValue,
	size_t valueSize
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |
| `pFieldName` | Field name of the HTTP header to obtain (ASCIIZ string) |
| `pValue` | Buffer for storing the value of the obtained HTTP header |
| `valueSize` | Size of the buffer specified to `pValue` |

## Return Values

Stores the value of the obtained HTTP header in `pValue[]` and returns `SCE_OK`(=0) upon normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function obtains the value of the HTTP header of the HTTP response upon Web API execution. The value of the HTTP response header can be obtained with this function after the normal termination of `sceNpWebApi2SendRequest()`. Before obtaining the value of the HTTP response header with this function, execute `sceNpWebApi2GetHttpResponseHeaderValueLength()` to obtain the size of the HTTP response header, prepare a sufficient buffer, and specify the buffer to `pValue`.

## Examples

```
int32_t ret = 0; 
int64_t requestId;
char value[BUF_SIZE];

ret = sceNpWebApi2GetHttpResponseHeaderValue(
	requestId, "My-Header-Name", value, sizeof(value));
if(ret < 0){
	/* Error handling */
}
```

# sceNpWebApi2GetHttpResponseHeaderValueLength

Get the length of the value of the HTTP response header

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2GetHttpResponseHeaderValueLength(
	int64_t requestId,
	const char *pFieldName,
	size_t *pValueLength
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |
| `pFieldName` | Field name of the HTTP header to obtain (ASCIIZ string) |
| `pValueLength` | Destination to store the length of the value of the HTTP header to obtain |

## Return Values

Stores the obtained length of the value of the HTTP header in `*pValueLength` and returns `SCE_OK`(=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function obtains the length of the value of a specific HTTP header of an HTTP response upon executing a Web API. The length of the value of a specific HTTP header can be obtained with this function after the normal termination of `sceNpWebApi2SendRequest()`. Before obtaining the value of the HTTP response header with `sceNpWebApi2GetHttpResponseHeaderValue()`, use this function to obtain the length of the value and to prepare a sufficient buffer.

## Examples

```
int32_t ret = 0; 
int64_t requestId;
size_t valueLength = 0;

ret = sceNpWebApi2GetHttpResponseHeaderValueLength(
	requestId, "My-Header-Name", &valueLength);
if(ret < 0){
	/* Error handling */
}
```