# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/obtaining-monitoring-sign-in-states.html

# Obtaining/Monitoring the Signed-in State

# SceNpState

Sign-in state

## Definition

```
#include <np/np_common.h>
typedef enum SceNpState {
	SCE_NP_STATE_UNKNOWN = 0,
	SCE_NP_STATE_SIGNED_OUT,
	SCE_NP_STATE_SIGNED_IN
} SceNpState;
```

## Description

This is an enumerated type that represents the sign-in state of the Np library. The meanings of each value are as follows.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_STATE_UNKNOWN` | 0 | Unknown state |
| `SCE_NP_STATE_SIGNED_OUT` | 1 | Signed out |
| `SCE_NP_STATE_SIGNED_IN` | 2 | Signed in |

The available PlayStation™Network features vary depending on the sign-in state.

With `SCE_NP_STATE_SIGNED_OUT`, almost all of the PlayStation™Network features are unavailable.

With `SCE_NP_STATE_SIGNED_IN`, the PlayStation™Network services can be used.

## See Also

`sceNpGetState()`, `SceNpStateCallbackA`

# sceNpGetState

Gets the sign-in state

## Definition

```
#include <np/np_common.h>
int sceNpGetState(
	SceUserServiceUserId userId,
	SceNpState *state
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID (IN) |
| `state` | Destination to store the obtained sign-in state (OUT) |

## Return Values

Stores the sign-in state in `*state` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |

## Description

This function obtains the sign-in state.

## Notes

Because this function obtains information from system processing using inter-process communication, this function can block other processes for a long period of time depending on the system process load. Do not call this function from a thread onto which you do not want the effects of the system process load (the rendering thread, for example).

# SceNpStateCallbackA

Callback that receives notifications of changes to the sign-in state

## Definition

```
#include <np/np_common.h>
typedef void (*SceNpStateCallbackA)(
	SceUserServiceUserId userId,
	SceNpState state,
	void *userdata
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `state` | New sign-in state |
| `userdata` | User data set upon callback function registration |

## Return Values

None

## Description

This is a prototype of a callback function that receives notification of changes in the sign-in state. Implement a function that follows this specification and register it using `sceNpRegisterStateCallbackA()` in situations where you want to monitor the sign-in state. When monitoring is no longer required, unregister it with `sceNpUnregisterStateCallbackA()`.

When a callback function is registered with `sceNpRegisterStateCallbackA()`, an event will occur that notifies the sign-in state at that time. Afterward, the registered callback function will be called when the application calls `sceNpCheckCallback()`. `state` will show the sign-in state after the change, so perform appropriate processing based on this.

When the sign-in state further changes, an event that notifies the new sign-in state will occur. After this, the callback function will be called when the application calls `sceNpCheckCallback()` and the sign-in state after the change will be passed to `state`.

## Notes

* Sign-in state changes will only be notified for logged in users.
* Avoid processing that would require large amounts of time within the callback function and return promptly.

# sceNpRegisterStateCallbackA

Registers the callback function for notifying the sign-in state

## Definition

```
#include <np/np_common.h>
int sceNpRegisterStateCallbackA(
	SceNpStateCallbackA callback,
	void *userdata
);
```

## Arguments

|  |  |
| --- | --- |
| `callback` | Callback function to register (IN) |
| `userdata` | Arbitrary user data to pass to the callback function (IN) |

## Return Values

Returns a callback ID (a positive value) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_CALLBACK_ALREADY_REGISTERED` | 0x80550008 | Callback function is already registered |

## Description

This function registers the callback function for receiving notifications on user sign-in state changes when they occur.

## Notes

* This function is not multithread safe.
* Because this function entails inter-process communication in order to request processing to the system process, this function can block other processes for a long period of time depending on the system process load. Do not call this function from a thread onto which you do not want the effects of the system process load (the rendering thread, for example).

# sceNpUnregisterStateCallbackA

Deregisters the callback function for notifying the sign-in state

## Definition

```
#include <np/np_common.h>
int sceNpUnregisterStateCallbackA(
	int callbackId
);
```

## Arguments

|  |  |
| --- | --- |
| `callbackId` | Callback ID of callback function to unregister (IN) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_CALLBACK_NOT_REGISTERED` | 0x80550009 | Callback function is not registered |

## Description

This function deregisters the callback function for receiving notifications regarding changes in the sign-in state.

## Notes

* This function is not multithread safe.
* Because this function entails inter-process communication in order to request processing to the system process, this function can block other processes for a long period of time depending on the system process load. Do not call this function from a thread onto which you do not want the effects of the system process load (the rendering thread, for example).

## See Also

`sceNpRegisterStateCallbackA()`