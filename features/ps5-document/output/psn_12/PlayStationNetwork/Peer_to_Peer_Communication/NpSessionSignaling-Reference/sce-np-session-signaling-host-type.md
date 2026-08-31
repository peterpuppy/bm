# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/sce-np-session-signaling-host-type.html

# Requesting to Establish P2P Connections

# sceNpSessionSignalingActivateUser

Requests a connection with the specified user

## Definition

```
#include <np.h>
int sceNpSessionSignalingActivateUser (
    SceNpSessionSignalingContextId ctxId,
    const SceNpPeerAddressA *peerAddrA,
    SceNpSessionSignalingGroupId *grpId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `peerAddrA` | Peer address that indicates the communication peer |
| `grpId` | Destination to store the group ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `peerAddrA` is NULL * `peerAddrA` is invalid * `grpId` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_OWN_PEER_ADDRESS` | 0x80553304 | The user's own peer address is specified |
| `SCE_NP_SESSION_SIGNALING_ERROR_OUT_OF_MEMORY` | 0x80553305 | Could not allocate memory |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRPID_NOT_AVAILABLE` | 0x80553309 | No more group ID can be created |
| `SCE_NP_SESSION_SIGNALING_ERROR_TOO_MANY_CONN` | 0x80553311 | Exceeded the maximum number of connections |

## Description

This function requests a connection between the user indicated by the user ID specified upon context creation and the user specified with `peerAddrA`.

Upon normal termination of this function, the group ID will be stored in the variable specified with `grpId`.

If the request succeeds, an `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATED` event notification will be sent to the group callback function specified upon context creation. If an error occurs during processing, there will be notification of an `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATE_ERROR` event. If this function is called multiple times with the same `peerAddrA` specified, an event notification will be sent to the group callback function only once.

Afterward, connection establishment processing will be performed in the library. When a connection is established, an `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_ESTABLISHED` event notification will be sent to the connection callback function specified when the context was created. When a connection fails to be established, there will be notification of an `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_DEAD` event.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpPeerAddressA peerAddrA; 

int ret;
SceNpSessionSignalingGroupId grpId;

ret = sceNpSessionSignalingActivateUser(ctxId, &peerAddrA, &grpId);

if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingDeactivate()`

# SceNpSessionSignalingSessionType

Session types

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingSessionType {
    (Omitted: see details below)
} SceNpSessionSignalingSessionType;
```

## Description

The enum constants below represent session types. Specify one of the following constants as an argument when calling `sceNpSessionSignalingActivateSession()`.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_SESSION_TYPE_PLAYER_SESSION` | 0 | Player Session |
| `SCE_NP_SESSION_SIGNALING_SESSION_TYPE_GAME_SESSION` | 1 | Game Session |

# SceNpSessionSignalingTopologyType

Connection topology types

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingTopologyType {
    (Omitted: see details below)
} SceNpSessionSignalingTopologyType;
```

## Description

The enum constants below represent connection topology types. Specify one of the following constants as an option parameter when calling `sceNpSessionSignalingActivateSession()`.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_TOPOLOGY_TYPE_MESH` | 1 | Full mesh |
| `SCE_NP_SESSION_SIGNALING_TOPOLOGY_TYPE_STAR` | 2 | Star |

## See Also

`SceNpSessionSignalingHostType`, `SceNpSessionSignalingSessionOptParam`

# SceNpSessionSignalingHostType

Host types

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingHostType {
    (Omitted: see details below)
} SceNpSessionSignalingHostType;
```

## Description

The enum constants below represent host types. Specify one of the following constants as an option parameter when calling `sceNpSessionSignalingActivateSession()`.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_HOST_TYPE_NONE` | 0 | No specification |
| `SCE_NP_SESSION_SIGNALING_HOST_TYPE_AUTO` | 1 | Selected automatically |
| `SCE_NP_SESSION_SIGNALING_HOST_TYPE_ME` | 2 | The current user is the host |

## See Also

`SceNpSessionSignalingTopologyType`, `SceNpSessionSignalingSessionOptParam`

# SceNpSessionSignalingSessionOptParam

Optional parameters for signaling within a session

## Definition

```
#include <np.h>
typedef struct SceNpSessionSignalingSessionOptParam {
    SceNpSessionSignalingTopologyType topologyType;
    SceNpSessionSignalingHostType hostType;
} SceNpSessionSignalingSessionOptParam;
```

## Members

|  |  |
| --- | --- |
| `topologyType` | Topology type |
| `hostType` | Host type |

## Description

This structure represents parameters for a session. Specify this structure as an argument when calling `sceNpSessionSignalingActivateSession()`.

Specify the host type based on the topology type, as described below:

* If the topology type is mesh, specify `SCE_NP_SESSION_SIGNALING_HOST_TYPE_NONE`
* If the topology type is star, specify `SCE_NP_SESSION_SIGNALING_HOST_TYPE_AUTO` or `SCE_NP_SESSION_SIGNALING_HOST_TYPE_ME`

If `AUTO`, the host member for the session will be decided automatically. If `ME`, the caller will be the host member.

# sceNpSessionSignalingActivateSession

Activates a connection within a session

## Definition

```
#include <np.h>
int sceNpSessionSignalingActivateSession (
    SceNpSessionSignalingContextId ctxId,
    const char *sessionId,
    SceNpSessionSignalingSessionType sessionType,
    const SceNpSessionSignalingSessionOptParam *optParam,
    SceNpSessionSignalingGroupId *grpId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `sessionId` | Session ID |
| `sessionType` | Session type (Player Session/Game Session) |
| `optParam` | Signaling options |
| `grpId` | Destination to store the group ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `sessionId` is NULL * `optParam` is NULL * One of the `optParam` members is invalid * `grpId` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_OUT_OF_MEMORY` | 0x80553305 | Could not allocate memory |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRPID_NOT_AVAILABLE` | 0x80553309 | No more group ID can be created |
| `SCE_NP_SESSION_SIGNALING_ERROR_GROUP_SIGNALING_ALREADY_ACTIVATED` | 0x80553312 | This function has already been called with the same Session ID specified  Confirm that multiple calls have not been made with the same Session ID specified for `sessionId`. |

## Description

This function activates connection features for the current user in a created and joined Player Session/Game Session specified with `sessionId`.

Upon normal termination of this function, the group ID will be stored in the variable specified with `grpId`.

If activation of connection features succeeds, an `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATED` event notification will be sent to the group callback function specified when the context was created. If an error occurs, there will be a notification of an `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATE_ERROR` event.

Afterward, processing to establish connections with other units that have activated connection features in the same session will occur within the library. When each of the connections is established, the connection callback function specified upon context creation will be notified of an `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_ESTABLISHED` event. When a connection fails to be established, there will be notification of an `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_DEAD` event.

The topology type specified for `optParam` will be overwritten by whatever is last set within the session. For example, if MESH is set but later another member calls this function and selects STAR, the topology type will be changed to STAR.

When the topology type is `STAR` and `ME` is specified for the host type, the member that was last set within the session will be the host member. When the host type is `AUTO`, the host member will not change if it has already been determined.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;

const char* sessionId = "xxxxx-xxxxx-xxx"; // Session ID of a created and joined session
SceNpSessionSignalingSessionOptParam optParam;
optParam.topologyType = SCE_NP_SESSION_SIGNALING_TOPOLOGY_TYPE_STAR;
optParam.hostType = SCE_NP_SESSION_SIGNALING_HOST_TYPE_ME;

int ret;
SceNpSessionSignalingGroupId grpId;

ret = sceNpSessionSignalingActivateSession(ctxId, sessionId, SCE_NP_SESSION_SIGNALING_SESSION_TYPE_PLAYER_SESSION, &optParam, &grpId);

if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingDeactivate()`

# sceNpSessionSignalingDeactivate

Deactivates a signaling group

## Definition

```
#include <np.h>
int sceNpSessionSignalingDeactivate (
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `grpId` | Group ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRP_NOT_FOUND` | 0x8055330A | Group could not be found  The group specified in `grpId` could not be found. Check the value specified for `grpId` |

## Description

This function deactivates the signaling group specified with `grpId` and deletes the group ID. Connection events relating to connections belonging to the group in question will no longer be notified, and the group ID will no longer be able to be used.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpSessionSignalingGroupId grpId;

int ret;

ret = sceNpSessionSignalingDeactivate(ctxId, grpId); 

if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingActivateUser()`, `sceNpSessionSignalingActivateSession()`