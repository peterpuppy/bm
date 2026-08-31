# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/group-searching.html

# Group Searching

# sceNpSessionSignalingGetGroupFromPeerAddress

Searches for a group with the peer address

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetGroupFromPeerAddress (
    SceNpSessionSignalingContextId ctxId,
    const SceNpPeerAddressA *peerAddrA,
    SceNpSessionSignalingGroupId *grpId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `peerAddrA` | Peer address to be searched |
| `grpId` | Destination to store the obtained group ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `peerAddrA` is NULL * `grpId` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |

## Description

The function is used to search for the group ID of the group corresponding to the peer address specified in `peerAddrA`, among the signal groups created using `sceNpSessionSignalingActivateUser()`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpPeerAddressA peerAddrA;

int ret;
SceNpSessionSignalingGroupId grpId;

ret = sceNpSessionSignalingGetGroupFromPeerAddress(ctxId, peerAddrA, &grpId);
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingActivateUser()`

# sceNpSessionSignalingGetGroupFromSessionId

Searches for a group with the session ID

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetGroupFromSessionId (
    SceNpSessionSignalingContextId ctxId,
    const char *sessionId,
    SceNpSessionSignalingGroupId *grpId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `sessionId` | The searched-for session ID |
| `grpId` | Destination to store the obtained group ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `sessionId` is NULL * `grpId` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |

## Description

The function is used to search for the group ID of the group corresponding to the session ID specified in `sessionId`, among the signal groups created using `sceNpSessionSignalingActivateSession()`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
const char* sessionId = "xxxxx-xxxxx-xxx";

int ret;
SceNpSessionSignalingGroupId grpId;

ret = sceNpSessionSignalingGetGroupFromSessionId(ctxId, sessionId, &grpId);
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingActivateSession()`