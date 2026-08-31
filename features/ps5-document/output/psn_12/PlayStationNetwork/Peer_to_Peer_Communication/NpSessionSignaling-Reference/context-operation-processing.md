# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/context-operation-processing.html

# Context Operation Processing

# SceNpSessionSignalingCreateContext2Param

Context creation parameters

## Definition

```
#include <np.h>
typedef struct SceNpSessionSignalingCreateContext2Param {
    SceUserServiceUserId userId;
    SceNpServiceLabel serviceLabel;
    SceNpSessionSignalingRequestCallback reqCbFunc;
    void *reqCbArg;
    SceNpSessionSignalingGroupCallback grpCbFunc;
    void *grpCbArg;
    SceNpSessionSignalingConnectionCallback2 connCbFunc;
    void *connCbArg;
} SceNpSessionSignalingCreateContext2Param;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID of the user who creates the context |
| `serviceLabel` | NP service label issued when applying to use the service (not currently available. Specify 0) |
| `reqCbFunc` | Request callback function to register, or NULL. |
| `reqCbArg` | Arbitrary data to be passed to the argument`arg` of a request callback function |
| `grpCbFunc` | Group callback function to register, or NULL |
| `grpCbArg` | Arbitrary data to be passed to the argument `arg` of a group callback function |
| `connCbFunc` | Connection callback function to register, or NULL |
| `connCbArg` | Arbitrary data to be passed to the argument `arg` of a connection callback function |

## Description

This structure represents the context creation parameters for the NpSessionSignaling library.

Specify it as an argument when executing `sceNpSessionSignalingCreateContext2()`.

# sceNpSessionSignalingCreateContext2

Creates a context

## Definition

```
#include <np.h>
int sceNpSessionSignalingCreateContext2(
    const SceNpSessionSignalingCreateContext2Param *param,
    SceNpSessionSignalingContextId *ctxId
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Context creation parameters |
| `ctxId` | Destination to store the context ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `param` is NULL * `ctxId` is NULL * One of the `param` members is invalid |
| `SCE_NP_SESSION_SIGNALING_ERROR_OUT_OF_MEMORY` | 0x80553305 | Could not allocate memory |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTXID_NOT_AVAILABLE` | 0x80553307 | No more contexts can be created.  Re-execute this function after destroying an existing context |

## Description

This function creates an NpSessionSignaling library context. In order to use the NpSessionSignaling library, it is necessary to create a context after initializing the library.

When a context is successfully created, the context ID will be stored to the buffer indicated by `ctxId`. From this point onwards, specify this context ID when calling an NpSessionSignaling library function.

Only one context can be created for each user. If a context has already been generated for a user, an error will be produced, and no new context can be created without deleting it.

## Examples

```
// Assuming that appropriate values are stored
SceUserServiceUserId userId;
SceNpServiceLabel serviceLabel;

// Request callback function
static void requestCallback(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingRequestId reqId,
    SceNpSessionSignalingRequestEvent event,
    const void *eventData,
    int errorCode,
    void *arg)
{
    // Handling of the request callback function
}

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
}

// Connection callback function
static void connectionCallback(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingGroupId grpId,
    SceNpSessionSignalingConnectionId connId,
    SceNpSessionSignalingConnectionEvent event,
    int errorCode,
    void *arg)
{
    // Handling of the connection callback function
}

// Assuming that appropriate values are stored
void *requestCallbackArg;
void *groupCallbackArg;
void *connectionCallbackArg;

SceNpSessionSignalingCreateContext2Param myParam;
SceNpSessionSignalingContextId ctxId;

myParam.userId = userId;
myParam.serviceLabel = serviceLabel;
myParam.reqCbFunc = requestCallback;
myParam.reqCbArg = requestCallbackArg;
myParam.grpCbFunc = groupCallback;
myParam.grpCbArg = groupCallbackArg;
myParam.connCbFunc = connectionCallback;
myParam.connCbArg = connectionCallbackArg;

int ret;

ret = sceNpSessionSignalingCreateContext2(&myParam, &ctxId);
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingDestroyContext()`

# sceNpSessionSignalingDestroyContext

Deletes a context

## Definition

```
#include <np.h>
int sceNpSessionSignalingDestroyContext(
    SceNpSessionSignalingContextId ctxId
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |

## Description

This function destroys an NpSessionSignaling library context.

When this function is executed, the joined-in connection and any request being executed will be deleted. Note that there will be no events occurring to notify these deletions.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;

int ret;

ret = sceNpSessionSignalingDestroyContext(ctxId);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpSessionSignalingCreateContext2()`