# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/sce-np-session-signaling-request-event.html

# Callback Function Definitions

# SceNpSessionSignalingRequestEvent

Request event

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingRequestEvent {
    (Omitted: see details below)
} SceNpSessionSignalingRequestEvent;
```

## Description

The enum constant below represents a request event. A request event notification will be sent to the `SceNpSessionSignalingRequestCallback` request callback function.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_REQUEST_EVENT_PREPARE` | 0 | Result of `sceNpSessionSignalingRequestPrepare()` |

# SceNpSessionSignalingRequestCallback

Request callback function

## Definition

```
#include <np.h>
typedef void ( *SceNpSessionSignalingRequestCallback )(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingRequestId reqId,
    SceNpSessionSignalingRequestEvent event,
    const void *eventData,
    int errorCode,
    void *arg
);
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `reqId` | Request ID assigned when `sceNpSessionSignalingRequestPrepare()` was executed |
| `event` | Request event |
| `eventData` | Event data  NULL indicates that there is no event data. |
| `errorCode` | Error code  A negative value indicates that an error occurred while processing `sceNpSessionSignalingRequestPrepare()`. 0 indicates a success. |
| `arg` | Application-specified data |

## Return Values

None

## Description

This is a prototype of a callback function that is notified of request events corresponding to the processing performed by `sceNpSessionSignalingRequestPrepare()`. When an appropriate function is implemented in accordance with this prototype and specified as an argument when `sceNpSessionSignalingCreateContext2()` is called to register it, the implemented function will be notified of the processing results of `sceNpSessionSignalingRequestPrepare()`.

# SceNpSessionSignalingGroupEvent

Group events

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingGroupEvent {
    (Omitted: see details below)
} SceNpSessionSignalingGroupEvent;
```

## Description

The enum constants below represent group events. A group event notification will be sent to the `SceNpSessionSignalingGroupCallback` group callback function.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATED` | 0 | Request to establish a connection succeeded |
| `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATE_ERROR` | 1 | Request to establish a connection resulted in an error |
| `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_PEER_ACTIVATED` | 2 | There was a request to establish a connection from another peer |

# SceNpSessionSignalingGroupCallback

Group callback function

## Definition

```
#include <np.h>
typedef void ( *SceNpSessionSignalingGroupCallback )(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    SceNpSessionSignalingGroupEvent event,
    const void *eventData,
    int errorCode,
    void *arg
);
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `grpId` | Group ID assigned upon a request to establish a connection |
| `event` | Group event |
| `eventData` | Event data  NULL indicates that there is no event data. |
| `errorCode` | Error code |
| `arg` | Application-specified data |

## Return Values

None

## Description

This is a prototype of a callback function that is notified of group events corresponding to processing for requests to establish connections. When an appropriate function is implemented in accordance with this prototype and specified as an argument when `sceNpSessionSignalingCreateContext2()` is called to register it, the implemented function will be notified of the processing results of `sceNpSessionSignalingActivateUser()` or `sceNpSessionSignalingActivateSession()`.

When `event` is notified of the `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_PEER_ACTIVATED` event, the peer address of the peer who called `sceNpSessionSignalingActivateUser()` can be obtained from `eventData`. In addition, the notification of the `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATE_ERROR` event indicates that the function for requesting to establish a connection resulted in an error.

## Examples

```
// Group callback function
static void groupCallback(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    SceNpSessionSignalingGroupEvent event,
    const void *eventData,
    int errorCode,
    void *arg)
{
    // Handling of the group callback function
    if (event == SCE_NP_SESSION_SIGNALING_GROUP_EVENT_PEER_ACTIVATED && eventData) {
        // The peer address of the peer who called sceNpSessionSignalingActivateUser() can be obtained from eventData
        const SceNpPeerAddressA *peerAddrA = (const SceNpPeerAddressA *)eventData;
    }
}
```

# SceNpSessionSignalingConnectionEvent

Connection events

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingConnectionEvent {
    (Omitted: see details below)
} SceNpSessionSignalingConnectionEvent;
```

## Description

The enum constants below represent connection events. A connection event notification will be sent to the `SceNpSessionSignalingConnectionCallback2` connection callback function.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_DEAD` | 0 | Connection was disconnected or failed to be established |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_ESTABLISHED` | 1 | Connection was established |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_ACTIVATED` | 2 | The connection establishment process has started |

# SceNpSessionSignalingConnectionCallback2

Connection callback function

## Definition

```
#include <np.h>
typedef void ( *SceNpSessionSignalingConnectionCallback2 )(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    SceNpSessionSignalingConnectionId connId,
    SceNpSessionSignalingConnectionEvent event,
    int errorCode,
    void *arg
);
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `grpId` | Group ID |
| `connId` | Connection ID |
| `event` | Connection event |
| `errorCode` | Error code  A negative value indicates that processing to establish a connection resulted in an error or that an error disconnected the connection. A value of 0 indicates there was no error. |
| `arg` | Application-specified data |

## Return Values

None

## Description

This is a prototype of a callback function that is notified of events indicating the establishment or disconnection of connections. When an appropriate function is implemented in accordance with this prototype and specified as an argument when `sceNpSessionSignalingCreateContext2()` is called to register it, the implemented function will be notified when the process to establish a connection is begun, a connection is established, or a connection is disconnected.