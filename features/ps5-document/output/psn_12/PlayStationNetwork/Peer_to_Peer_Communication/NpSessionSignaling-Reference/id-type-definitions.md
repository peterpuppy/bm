# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/id-type-definitions.html

# ID Type Definitions

# SceNpSessionSignalingContextId

Context ID

## Definition

```
#include <np.h>
typedef uint32_t SceNpSessionSignalingContextId
```

## Description

This type represents a context ID.

When a context is created with `sceNpSessionSignalingCreateContext2()`, a new context ID will be assigned.

Afterward, specify this context ID when calling the functions of the NpSessionSignaling library.

# SceNpSessionSignalingRequestId

Request ID

## Definition

```
#include <np.h>
typedef uint32_t SceNpSessionSignalingRequestId
```

## Description

This type represents a request ID.

When `sceNpSessionSignalingRequestPrepare()` is called, a new request ID will be assigned.

This is used to identify which request the calling is in response to when the request callback function `SceNpSessionSignalingRequestCallback` is called.

# SceNpSessionSignalingGroupId

Group ID

## Definition

```
#include <np.h>
typedef uint32_t SceNpSessionSignalingGroupId;
```

## Description

This type represents a group ID.

A new group ID will be assigned when a request to establish a connection is made with `sceNpSessionSignalingActivateUser()` or `sceNpSessionSignalingActivateSession()`. When the group callback function `SceNpSessionSignalingGroupCallback` is called, this group ID will be passed as an argument.

Additionally, the group ID is used when a connection is disconnected using `sceNpSessionSignalingDeactivate()`.

# SceNpSessionSignalingConnectionId

Connection ID

## Definition

```
#include <np.h>
typedef uint32_t SceNpSessionSignalingConnectionId;
```

## Description

This type represents a connection ID.

When there is a notification by the callback function `SceNpSessionSignalingConnectionCallback2` of the establishment or deletion of a connection, this connection ID will be notified as an identifier for the target connection.

Additionally, specify this connection ID when calling one of the connection status-obtaining functions.

## See Also

`sceNpSessionSignalingGetConnectionInfo()`, `sceNpSessionSignalingGetConnectionStatus()`