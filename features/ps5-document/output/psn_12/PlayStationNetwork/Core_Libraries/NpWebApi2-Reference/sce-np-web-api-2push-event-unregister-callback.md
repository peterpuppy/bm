# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2push-event-unregister-callback.html

# Push Events

# SceNpWebApi2PushEventDataType

Push event data type

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2PushEventDataType {
	char val[SCE_NP_WEBAPI2_PUSH_EVENT_DATA_TYPE_LEN_MAX + 1];
} SceNpWebApi2PushEventDataType;
```

## Members

|  |  |
| --- | --- |
| `val` | Buffer to store the character string that indicates the Push event data type |

## Description

This structure indicates the data type of a Push event. It is used when specifying a Push event to be received with a Push event filter and when identifying the data type of a received Push event.

For details on Push event data types, refer to the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document and the reference for each Web API.

# SceNpWebApi2PushEventExtdDataKey

Push event extended data key

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2PushEventExtdDataKey {
	char val[SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX + 1];
} SceNpWebApi2PushEventExtdDataKey;
```

## Members

|  |  |
| --- | --- |
| `val` | Buffer to store character string that represents extended data key for Push event |

## Description

This structure represents an extended data key for a Push event. It is used when specifying an extended data key for a Push event to be received with a Push event filter, and when identifying extended data for a received Push event.

For details on extended data keys for Push events, refer to the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document and each Web API reference document.

## See Also

`SceNpWebApi2PushEventFilterParameter`, `SceNpWebApi2PushEventExtdData`

# SceNpWebApi2PushEventFilterParameter

Push event filter parameters

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2PushEventFilterParameter {
	SceNpWebApi2PushEventDataType dataType;
	SceNpWebApi2PushEventExtdDataKey *pExtdDataKey;
	size_t extdDataKeyNum;
} SceNpWebApi2PushEventFilterParameter;
```

## Members

|  |  |
| --- | --- |
| `dataType` | Data type of Push event to receive |
| `pExtdDataKey` | Array of extended data keys for Push event to receive |
| `extdDataKeyNum` | Number of elements in array represented by `pExtdDataKey` |

## Description

This structure represents the parameters to specify when creating a Push event filter.

## See Also

`sceNpWebApi2PushEventCreateFilter()`

# SceNpWebApi2PushEventExtdData

Push event extended data

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2PushEventExtdData {
	SceNpWebApi2PushEventExtdDataKey extdDataKey;
	char *pData;
	size_t dataLen;
} SceNpWebApi2PushEventExtdData;
```

## Members

|  |  |
| --- | --- |
| `extdDataKey` | Extended data key for received Push event |
| `pData` | Extended data for received Push event |
| `dataLen` | Length of extended data for received Push event |

## Description

This structure represents extended data for a received Push event.

## See Also

`SceNpWebApi2PushEventCallback`

# SceNpWebApi2PushEventCallback

Callback function that is notified of Push events

## Definition

```
#include <np/np_webapi2.h>
typedef void (*SceNpWebApi2PushEventCallback)(
	int32_t userCtxId,
	int32_t callbackId,
	const char *pNpServiceName,
	SceNpServiceLabel npServiceLabel,
	const SceNpPeerAddressA *pTo,
	const SceNpOnlineId *pToOnlineId,
	const SceNpPeerAddressA *pFrom,
	const SceNpOnlineId *pFromOnlineId,
	const SceNpWebApi2PushEventDataType *pDataType,
	const char *pData,
	size_t dataLen,
	const SceNpWebApi2PushEventExtdData *pExtdData,
	size_t extdDataNum,
	void *pUserArg
);
```

## Members

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `callbackId` | Callback ID |
| `pNpServiceName` | NP service name or NULL |
| `npServiceLabel` | NP service label or `SCE_NP_INVALID_SERVICE_LABEL` |
| `pTo` | Peer address of the user who is being notified of a Push event |
| `pToOnlineId` | Online ID of the user who is being notified of a Push event |
| `pFrom` | Peer address of the originating user of a Push event |
| `pFromOnlineId` | Online ID of the originating user of a Push event |
| `pDataType` | Data type of the notified Push event |
| `pData` | Data attached to the notified Push event or NULL |
| `dataLen` | Size of the data attached to the notified Push event or 0 |
| `pExtdData` | Array containing the extended data attached to the notified Push event or NULL |
| `extdDataNum` | Number of elements of the array representing `pExtdData` |
| `pUserArg` | User data |

## Description

This is a callback function notified by a received Push event. It is possible for a Push event that matches the data type of the Push event filter created with `sceNpWebApi2PushEventCreateFilter()` to be notified and then obtain the extended data that matches the extended data key.

An application should call `sceNpCheckCallback()` at regular intervals in order for this callback function to be called.

Whether data or extended data is attached to a Push event or not depends on the type of Push event, so refer to each Web API reference document. If data will not be attached, NULL will be passed to `pData`, and 0 will be passed to `dataLen`. If extended data that matches the extended data key does not exist, NULL will be passed to `pExtdData`, and 0 will be passed to `extdDataNum`.

# sceNpWebApi2PushEventAbortHandle

Abort handle processing

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventAbortHandle(
	int32_t libCtxId,
	int32_t handleId
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `handleId` | Handle ID of handle for which processing will be aborted |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function aborts the processing of the `sceNpWebApi2PushEventCreateFilter()` being executed with the handle indicated by `handleId`.

## Examples

```
int32_t ret = 0;
int32_t libCtxId;
int32_t handleId;

ret = sceNpWebApi2PushEventAbortHandle(libCtxId, handletId);
if(ret < 0){
	/* Error handling */
}
```

# sceNpWebApi2PushEventCreateHandle

Create handle

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventCreateHandle(
	int32_t libCtxId
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |

## Return Values

Returns the handle ID (positive value) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function creates the handle required for execution of `sceNpWebApi2PushEventCreateFilter()`.

After the execution of `sceNpWebApi2PushEventCreateFilter()`, call `sceNpWebApi2PushEventDeleteHandle()` and delete the handle.

## Examples

```
int32_t ret = 0;
int32_t libCtxId;
int32_t handleId = 0;

ret = sceNpWebApi2PushEventCreateHandle(libCtxId);
if(ret < 0){
	/* Error handling */
}
handleId = ret;
```

## See Also

`sceNpWebApi2PushEventDeleteHandle()`, `sceNpWebApi2PushEventAbortHandle()`

# sceNpWebApi2PushEventCreateFilter

Create Push event filter

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventCreateFilter(
	int32_t libCtxId,
	int32_t handleId,
	const char *pNpServiceName,
	SceNpServiceLabel npServiceLabel,
	const SceNpWebApi2PushEventFilterParameter *pFilterParam,
	size_t filterParamNum
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `handleId` | Handle ID |
| `pNpServiceName` | NP service name |
| `npServiceLabel` | NP service label  Specify the NP service label that was set up upon submitting the request for PlayStation™Network service usage. |
| `pFilterParam` | Array of Push event filter parameters |
| `filterParamNum` | Number of elements in array represented by `pFilterParam` |

## Return Values

Returns the filter ID (positive value) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function creates a filter for specifying the data types of Push events to receive. When registering a Push event callback function, specify the filter ID issued upon normal termination of this function.

For `npServiceLabel`, specify the NP service label set upon requesting PlayStation™Network service usage.

For `pFilterParam`, specify the `SceNpWebApi2PushEventFilterParameter` structure, which stores datatypes indicating the Push events the application wants to receive and an array of extended data keys of Push events the application wants to receive. Because this structure will be deep-copied within `sceNpWebApi2PushEventCreateFilter()`, it doesn't need to be kept on the application side.

## Examples

```
#define NP_SERVICE_NAME "npServiceName"
#define SERVICE_LABEL (0)  // NP service label set upon requesting PlayStation™Network service usage

int32_t ret = 0;
int32_t libCtxId;
int32_t handleId;
int32_t filterId = 0;

SceNpWebApi2PushEventDataType dataType[2];
SceNpWebApi2PushEventFilterParameter filterParam[2];
SceNpWebApi2PushEventExtdDataKey extdDataKey1[2], extdDataKey2[2];	

memset(dataType, 0, sizeof(dataType));
snprintf(dataType[0].val, SCE_NP_WEBAPI2_PUSH_EVENT_DATA_TYPE_LEN_MAX,
	"dataType1");
snprintf(dataType[1].val, SCE_NP_WEBAPI2_PUSH_EVENT_DATA_TYPE_LEN_MAX,
	"dataType2");

memset(extdDataKey1, 0, sizeof(extdDataKey1));
snprintf(extdDataKey1[0].val,
	SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX, "key1-1");
snprintf(extdDataKey1[1].val,
	SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX, "key1-2");

memset(extdDataKey2, 0, sizeof(extdDataKey2));
snprintf(extdDataKey2[0].val,
	SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX, "key2-1");
snprintf(extdDataKey2[1].val,
	SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX, "key2-2");

memset(filterParam, 0, sizeof(filterParam));	
memcpy(&filterParam[0].dataType, &dataType[0],
	sizeof(SceNpWebApi2PushEventDataType));
filterParam[0].pExtdDataKey = extdDataKey1;
filterParam[0].extdDataKeyNum = 2;
memcpy(&filterParam[1].dataType, &dataType[1],
	sizeof(SceNpWebApi2PushEventDataType));
filterParam[1].pExtdDataKey = extdDataKey2;
filterParam[1].extdDataKeyNum = 2;

// Blocking function
ret = sceNpWebApi2PushEventCreateFilter(
	libCtxId, handleId, NP_SERVICE_NAME, SERVICE_LABEL, filterParam, 2);
if(ret < 0){
	/* Error handling */
}
filterId = ret;
```

## Notes

This function is a blocking function. Processing may take time; therefore, it should be called from a subthread.

## See Also

`sceNpWebApi2PushEventDeleteFilter()`, `sceNpWebApi2PushEventRegisterCallback()`

# sceNpWebApi2PushEventDeleteHandle

Delete handle

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventDeleteHandle(
	int32_t libCtxId,
	int32_t handleId
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `handleId` | Handle ID of handle to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function deletes a handle that is no longer needed. Because a handle becomes unnecessary after returning from `sceNpWebApi2PushEventCreateFilter()` or `sceNpWebApi2PushEventAbortHandle()`, use this function to delete it.

## Examples

```
int32_t ret = 0;
int32_t libCtxId;
int32_t handleId;

ret = sceNpWebApi2PushEventDeleteHandle(libCtxId, handleId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventCreateHandle()`

# sceNpWebApi2PushEventDeleteFilter

Delete Push event filter

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventDeleteFilter(
	int32_t libCtxId,
	int32_t filterId
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `filterId` | Filter ID for the Push event filter to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function deletes a Push event filter that is no longer needed. Once it is no longer necessary to receive Push events and you use `sceNpWebApi2PushEventUnregisterCallback()` to unregister the Push event callback function, use this function to delete the Push event filter.

## Examples

```
int32_t ret = 0;
int32_t libCtxId;
int32_t filterId;

ret = sceNpWebApi2PushEventDeleteFilter(libCtxId, filterId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventCreateFilter()`

# sceNpWebApi2PushEventSetHandleTimeout

Set timeout to a handle

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventSetHandleTimeout(
	int32_t libCtxId,
	int32_t handleId,
	uint32_t timeout
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `handleId` | Handle ID of a handle to set timeout to |
| `timeout` | Timeout time (microseconds) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function sets a timeout to a handle.

After creating a handle with `sceNpWebApi2PushEventCreateHandle()`, call this function to set a timeout before executing `sceNpWebApi2PushEventCreateFilter()`, and periodically call `sceNpWebApi2CheckTimeout()`.

When a timeout occurs, `sceNpWebApi2PushEventCreateFilter()` will return the `SCE_NP_WEBAPI2_ERROR_TIMEOUT` error.

## Examples

```
int32_t ret = 0;
int32_t libCtxId;
int32_t handleId;

ret = sceNpWebApi2PushEventSetHandleTimeout(libCtxId, handleId, 10*1000*1000);
if(ret < 0){
	/* Error handling */
}
```

# sceNpWebApi2PushEventRegisterCallback

Register Push event callback function

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventRegisterCallback(
	int32_t userCtxId,
	int32_t filterId,
	SceNpWebApi2PushEventCallback cbFunc,
	void *pUserArg
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `filterId` | Push event filter ID indicating the Push events intended to be received |
| `cbFunc` | Callback function that is notified of Push events |
| `pUserArg` | User data |

## Return Values

Returns the callback ID (a positive value) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function registers a callback function that is notified of received Push events. Before registering a callback function with this function, calling `sceNpWebApi2PushEventCreateFilter()` to create a Push event filter to indicate the Push events to receive is required.

Specify the callback ID issued for normal termination of this function when unregistering a Push event callback function.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
int32_t filterId;
int32_t callbackId = 0;

ret = sceNpWebApi2PushEventRegisterCallback(
	userCtxId, filterId, cbFunc, NULL);
if(ret < 0){
	/* Error handling */
}
callbackId = ret;
```

## See Also

`sceNpWebApi2PushEventUnregisterCallback()`

# sceNpWebApi2PushEventUnregisterCallback

Unregister Push event callback function

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventUnregisterCallback(
	int32_t userCtxId,
	int32_t callbackId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `callbackId` | Callback ID of the callback function to unregister |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function unregisters a Push event callback function that is no longer required.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
int32_t callbackId;

ret = sceNpWebApi2PushEventUnregisterCallback(
	userCtxId, callbackId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventRegisterCallback()`