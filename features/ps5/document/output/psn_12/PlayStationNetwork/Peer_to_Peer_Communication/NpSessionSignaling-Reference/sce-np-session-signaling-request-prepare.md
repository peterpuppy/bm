# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/sce-np-session-signaling-request-prepare.html

# Waiting for P2P Connections

# sceNpSessionSignalingRequestPrepare

Prepares for a connection

## Definition

```
#include <np.h>
int sceNpSessionSignalingRequestPrepare(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingRequestId *reqId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `reqId` | Destination to store the request ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `reqId` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |

## Description

This function initiates a context created with the NpSessionSignaling library and prepares to receive a request to establish a connection from another user. Once preparations are complete, connection requests from other users can be received by a group callback function.

Upon normal termination, this function stores the request ID in the area specified with `reqId`.

The request callback function specified upon context creation is notified of the results of executing a request via this function, along with the `SCE_NP_SESSION_SIGNALING_REQUEST_EVENT_PREPARE` event. If `errorCode` passed to the request callback function is 0, that indicates that the request succeeded; a negative value indicates that an error occurred during processing of the request.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;

int ret;
SceNpSessionSignalingRequestId reqId;

ret = sceNpSessionSignalingRequestPrepare(ctxId, &reqId);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

If it is not necessary to receive connection requests from other users, there is no need to call this function. If not calling this function, equivalent processing will occur automatically the first time `sceNpSessionSignalingActivateUser()` or `sceNpSessionSignalingActivateSession()` is called after the context is created.

## See Also

`SceNpSessionSignalingRequestCallback`