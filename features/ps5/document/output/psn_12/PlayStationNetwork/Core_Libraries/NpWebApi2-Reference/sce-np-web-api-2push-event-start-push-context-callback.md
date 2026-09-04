# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2push-event-start-push-context-callback.html

# Order-Guaranteed Push Events

# SceNpWebApi2PushEventPushContextCallbackType

Push context callback type

## Definition

```
#include <np/np_webapi2.h>
typedef enum SceNpWebApi2PushEventPushContextCallbackType {
	SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_RECEIVED,
	SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED,
} SceNpWebApi2PushEventPushContextCallbackType;
```

## Description

This enum constant indicates the type of notification that is passed to callback function notified of an order-guaranteed Push event.

`SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_RECEIVED` indicates a notification that a Push event was received without issue.

`SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED` indicates a notification that the lack of a Push event was detected. If this notification is received, Push events are not arriving in the correct order; therefore, you must follow the specifications of the Web API server to handle the issue appropriately with the application.

# SceNpWebApi2PushEventPushContextId

Push context ID

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2PushEventPushContextId {
	char uuid[SCE_NP_WEBAPI2_PUSH_EVENT_UUID_LENGTH + 1];
} SceNpWebApi2PushEventPushContextId;
```

## Members

|  |  |
| --- | --- |
| `uuid` | Buffer to store UUIDs that indicate Push context IDs |

## Description

This structure represents Push context IDs. Push contexts are expressed as UUIDs, the values of which are stored in `uuid`.

Register UUIDs with the Web API server to receive order-guaranteed Push events. For how to register, refer to the documentation for each Web API.

Additionally, when callbacks are notified of order-guaranteed Push events, the Push context ID is notified, as well. Based on the Push context ID, you can identify the Web API server from which the Push event was received.

The format of the string stored in `uuid` is a random string with a very low collision probability. This string is data for receiving order-guaranteed Push events, so do not use it for any other purpose. In particular, it cannot be used for the purpose of specifying individual devices.

# SceNpWebApi2PushEventPushContextCallback

Callback function notified of order-guaranteed Push events

## Definition

```
#include <np/np_webapi2.h>
typedef void(*SceNpWebApi2PushEventPushContextCallback)(
	int32_t userCtxId,
	int32_t callbackId,
	const SceNpWebApi2PushEventPushContextId *pPushCtxId,
	SceNpWebApi2PushEventPushContextCallbackType cbType,
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
| `pPushCtxId` | Push context ID |
| `cbType` | Callback type |
| `pNpServiceName` | NP service name or NULL |
| `npServiceLabel` | NP service label or `SCE_NP_INVALID_SERVICE_LABEL` |
| `pTo` | Peer address of the user who is being notified of a Push event |
| `pToOnlineId` | Online ID of the user who is being notified of a Push event, or NULL (when `cbType` is `SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED`) |
| `pFrom` | Peer address of the originating user of a Push event, or NULL ( when `cbType` is `SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED`) |
| `pFromOnlineId` | Online ID of the originating user of a Push event, or NULL (when `cbType` is `SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED`) |
| `pDataType` | Data type of the notified Push event, or NULL (when `cbType` is `SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED`) |
| `pData` | Data attached to the notified Push event or NULL |
| `dataLen` | Size of the data attached to the notified Push event or 0 |
| `pExtdData` | Array containing the extended data attached to the notified Push event or NULL |
| `extdDataNum` | Number of elements of the array representing `pExtdData` |
| `pUserArg` | User data |

## Description

This callback function is notified of order-guaranteed Push events.

The three main differences from callback functions defined with `SceNpWebApi2PushEventCallback` are as follows:

* (a) Push events are notified after being ordered by the Push context
* (b) The Push context ID is notified (order is guaranteed for Push events for which there are pairs of Push context IDs and callback IDs)
* (c) Two types of notification are performed: ordinary receiving and loss detection

The two callback functions are the same in that Push events matching the data type of the Push event filter created beforehand with `sceNpWebApi2PushEventCreateFilter()` are notified and in that extended data matching the extended data key can be obtained.

Have the application call `sceNpCheckCallback()` periodically so that this callback function is called.

# sceNpWebApi2PushEventRegisterPushContextCallback

Register a Push context callback

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventRegisterPushContextCallback(
	int32_t userCtxId,
	int32_t filterId,
	SceNpWebApi2PushEventPushContextCallback cbFunc,
	void *pUserArg
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `filterId` | Push event filter ID indicating the Push events intended to be received |
| `cbFunc` | Push context callback function notified of Push events |
| `pUserArg` | User data |

## Return Values

Returns the callback ID (a positive value) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function registers callback functions that are notified of order-guaranteed Push events. Before registering a callback function with this function, you must call `sceNpWebApi2PushEventCreateFilter()` to create a push event filter indicating the push events you intend to receive.

The callback IDs that this function issues on normal termination are specified when unregistering Push context callback functions.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
int32_t filterId;
void *userdata;
int32_t callbackId = 0;
	
ret = sceNpWebApi2PushEventRegisterPushContextCallback(
	userCtxId, filterId, cbFunc, userdata);
if (ret < 0) {
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventUnregisterPushContextCallback()`

# sceNpWebApi2PushEventUnregisterPushContextCallback

Unregisters a Push context callback

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventUnregisterPushContextCallback(
	int32_t userCtxId,
	int32_t callbackId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `callbackId` | Callback ID of the Push context callback function to be unregistered |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function unregisters Push context callback functions that are no longer needed.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
int32_t callbackId;

ret = sceNpWebApi2PushEventUnregisterPushContextCallback (
	userCtxId, callbackId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventRegisterPushContextCallback()`

# sceNpWebApi2PushEventCreatePushContext

Create a Push context

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventCreatePushContext(
	int32_t userCtxId,
	SceNpWebApi2PushEventPushContextId *pPushCtxId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `pPushCtxId` | Location to store the created Push context ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function creates a Push context for receiving order-guaranteed Push events. A Push context receives Push events whose order is not guaranteed by the server and reorders them into the expected order. A Push context has a queue for performing that reordering.

Push events can be sent once the created Push context is registered on the Web API server. For how to register, refer to the documentation for the respective Web API.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
SceNpWebApi2PushEventPushContextId pushCtxId;
memset(&pushCtxId, 0, sizeof(pushCtxId));

ret = sceNpWebApi2PushEventCreatePushContext(
	userCtxId, &pushCtxId);
if (ret < 0) {
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventDeletePushContext()`

# sceNpWebApi2PushEventDeletePushContext

Delete a Push context

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventDeletePushContext(
	int32_t userCtxId,
	const SceNpWebApi2PushEventPushContextId *pPushCtxId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `pPushCtxId` | Push context ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function deletes Push contexts that are no longer needed. Use this function to delete a Push context once there is no longer a need for the Web API server to receive Push events for the relevant Push context.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
int32_t filterId;
int32_t callbackId = 0;

ret = sceNpWebApi2PushEventDeletePushContext(
	userCtxId, &pushCtxId);
if (ret < 0) {
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventCreatePushContext()`

# sceNpWebApi2PushEventStartPushContextCallback

Starts a Push context callback

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2PushEventStartPushContextCallback(
	int32_t userCtxId,
	const SceNpWebApi2PushEventPushContextId *pPushCtxId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |
| `pPushCtxId` | Push context ID of the callback to start receiving Push events |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function starts a callback function that is notified of order-guaranteed Push events. Once a callback function has been registered using `sceNpWebApi2PushEventRegisterPushContextCallback()`, use this function to start the callback function. Afterward, the callback to which Push events directed to a Push context will be able to receive the Push events through the repeated calling of `sceNpCheckCallback()`. The callback occurs in the thread that called `sceNpCheckCallback()`.

This function may be called either before or after a Push context is registered with a Web API server. However, if this function is called before registration, be aware that the registration complete response from the Web API server may arrive earlier than Push events. On the other hand, be aware that, if this function is called after registration, the gap in time may result in Push events arriving from the Web API server remaining without the callback being notified and the Push context queue overflowing.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;
SceNpWebApi2PushEventPushContextId pushCtxId;

ret = sceNpWebApi2PushEventStartPushContextCallback(
	userCtxId, &pushCtxId);
if (ret < 0) {
	/* Error handling */
}
```

## See Also

`sceNpWebApi2PushEventCreatePushContext()`