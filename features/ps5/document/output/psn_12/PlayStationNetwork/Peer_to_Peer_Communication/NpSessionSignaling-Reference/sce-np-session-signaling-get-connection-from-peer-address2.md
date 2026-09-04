# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/sce-np-session-signaling-get-connection-from-peer-address2.html

# P2P Connection Searching

# SceNpSessionSignalingConnectionList

Connection list

## Definition

```
#include <np.h>

#define SCE_NP_SESSION_SIGNALING_MAX_CONNECTION_NUM (64)

typedef struct SceNpSessionSignalingConnectionList {
    SceNpSessionSignalingConnectionId connId[SCE_NP_SESSION_SIGNALING_MAX_CONNECTION_NUM];
    size_t connIdNum;
} SceNpSessionSignalingConnectionList;
```

## Members

|  |  |
| --- | --- |
| `connId` | Connection ID list |
| `connIdNum` | Number of connection IDs |

## Description

This structure represents a connection list.

A variable of this type is used when obtaining the results of `sceNpSessionSignalingGetGroupInfo()` and `sceNpSessionSignalingGetConnectionFromNetAddress2()`.

# sceNpSessionSignalingGetGroupInfo

Gets a connection belonging to a group

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetGroupInfo(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    SceNpSessionSignalingConnectionList *connList
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `grpId` | Group ID |
| `connList` | Connection list |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `connList` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRP_NOT_FOUND` | 0x8055330A | Group could not be found  The group specified in `grpId` could not be found. Check the value specified for `grpId` |

## Description

This function checks for connections belonging to the signaling group specified with `grpId`.

Note that connections that can be obtained by this function do not depend on the connection status. To determine if the connection is in the PENDING state or ACTIVE state, pass the connection ID included in `*connList` to `sceNpSessionSignalingGetConnectionStatus()`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpSessionSignalingGroupId grpId;

int ret;
SceNpSessionSignalingConnectionList connList;

ret = sceNpSessionSignalingGetGroupInfo(ctxId, grpId, &connList);
if ( ret < 0 ) {
    // Error handling
}
```

# sceNpSessionSignalingGetConnectionFromPeerAddress2

Searches for a connection with the peer address

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetConnectionFromPeerAddress2(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    Const SceNpPeerAddressA *peerAddrA,
    SceNpSessionSignalingConnectionId *connId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `grpId` | Group ID |
| `peerAddrA` | Peer address to be searched |
| `connId` | Destination to store the obtained connection ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `peerAddrA` is NULL * `connId` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRP_NOT_FOUND` | 0x8055330A | Group could not be found  The group specified in `grpId` could not be found. Check the value specified for `grpId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONN_NOT_FOUND` | 0x8055330C | Connection could not be found  This means that the connection for the `pPeerAddrA` peer address does not exist.  Make sure that the value specified to the argument is correct. |

## Description

This function checks if a connection with the peer address specified with `peerAddrA` as the peer exists in the signaling group specified with `grpId`.

Note that "a connection exists" for this function does not depend on the connection status. To determine if the connection is in the PENDING state or ACTIVE state, pass the value returned to `*connId` to `sceNpSessionSignalingGetConnectionStatus()`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpSessionSignalingGroupId grpId;
SceNpPeerAddressA peerAddrA;

int ret;
SceNpSessionSignalingConnectionId connId;

ret = sceNpSessionSignalingGetConnectionFromPeerAddress2(ctxId, grpId, peerAddrA, &connId);
if ( ret < 0 ) {
    // Error handling
}
```

# sceNpSessionSignalingGetConnectionFromNetAddress2

Gets a connection with the address of the communication peer

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetConnectionFromNetAddress2(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    SceNetInAddr peerAddr,
    SceNetInPort_t peerPort,
    SceNpSessionSignalingConnectionList *connList
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `grpId` | Group ID |
| `peerAddr` | IP address of the communication peer |
| `peerPort` | Port number (network byte order) of the communication peer |
| `connList` | Destination to store the obtained connection list |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `connList` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRP_NOT_FOUND` | 0x8055330A | Group could not be found  The group specified in `grpId` could not be found. Check the value specified for `grpId` |

## Description

This function obtains a list of the connections with the communication peer specified by the `peerAddr` IP address and `peerPort` port number, from among the connections belonging to the signaling group specified with `grpId`. A list for connections in the ACTIVE state can be obtained.

In many cases, only one connection will be returned as matching for `peerAddr` and `peerPort`. However, if multiple users are included in the same signaling group on the same device, multiple connections may be returned by `connList`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpSessionSignalingGroupId grpId;
SceNetInAddr peerAddr;
SceNetInPort_t peerPort;

int ret;
SceNpSessionSignalingConnectionList connList;

ret = sceNpSessionSignalingGetConnectionFromNetAddress2(ctxId, grpId, peerAddr, peerPort, &connList);
if ( ret < 0 ) {
    // Error handling
}
```