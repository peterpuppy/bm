# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/sce-np-register-np-reachability-state-callback.html

# Obtaining/Monitoring PlayStation™Network Reachability States

# SceNpReachabilityState

PlayStation™Network reachability state

## Definition

```
#include <np/np_common.h>
typedef enum SceNpReachabilityState {
	SCE_NP_REACHABILITY_STATE_UNAVAILABLE = 0,
	SCE_NP_REACHABILITY_STATE_AVAILABLE,
	SCE_NP_REACHABILITY_STATE_REACHABLE
} SceNpReachabilityState;
```

## Description

These are enumerated types that represent the PlayStation™Network reachability states. The meanings of each value are as follows.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_REACHABILITY_STATE_UNAVAILABLE` | 0 | PlayStation™Network features cannot be used or reachability state cannot be confirmed |
| `SCE_NP_REACHABILITY_STATE_AVAILABLE` | 1 | PlayStation™Network features can be used, but servers of PlayStation™Network cannot be reached |
| `SCE_NP_REACHABILITY_STATE_REACHABLE` | 2 | Servers of PlayStation™Network can be reached (It takes some time for the system software to confirm that the system is not in this state even after the reachable state has, in fact, been lost) |

For details, refer to the [Np Library Overview](../Np-Overview/__document_toc.html) document.

## See Also

`sceNpGetNpReachabilityState()`, `SceNpReachabilityStateCallback`

# sceNpGetNpReachabilityState

Gets the PlayStation™Network reachability state

## Definition

```
#include <np/np_common.h>
int sceNpGetNpReachabilityState(
	SceUserServiceUserId userId,
	SceNpReachabilityState *state
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID (IN) |
| `state` | Destination to store the obtained reachability state (OUT) |

## Return Values

Stores the PlayStation™Network reachability state in `*state` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |

## Description

This function obtains the PlayStation™Network reachability state.

## Notes

Because this function obtains information from system processing using inter-process communication, this function can block other processes for a long period of time depending on the system process load. Do not call this function from a thread onto which you do not want the effects of the system process load (the rendering thread, for example).

# SceNpReachabilityStateCallback

Callback that receives notifications for PlayStation™Network reachability state changes

## Definition

```
#include <np/np_common.h>
typedef void (*SceNpReachabilityStateCallback)(
	SceUserServiceUserId userId,
	SceNpReachabilityState state,
	void *userdata
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `state` | PlayStation™Network reachability state |
| `userdata` | User data set upon callback function registration |

## Return Values

None

## Description

This is a prototype of a callback function that receives notification of PlayStation™Network reachability state changes. Implement a function that follows this specification and register it using `sceNpRegisterNpReachabilityStateCallback()` in situations where you want to monitor the reachability states. When monitoring is no longer required, unregister it with `sceNpUnregisterNpReachabilityStateCallback()`.

When a callback function is registered with `sceNpRegisterNpReachabilityStateCallback()`, an event will occur that notifies the reachability state at that time. Afterward, the registered callback function will be called when the application calls `sceNpCheckCallback()`. `state` will show the reachability state after the change, so perform appropriate processing based on this.

Hereafter, when `sceNpCheckCallback()` is called at regular intervals, the callback function will be called if the reachability state has changed when the application calls `sceNpCheckCallback()`, and the reachability state after the change will be passed to `state`.

## Notes

* PlayStation™Network reachability state changes will only be notified for logged in users.
* Avoid processing that would require large amounts of time within the callback function and return promptly.

# sceNpRegisterNpReachabilityStateCallback

Registers the callback function for notifying PlayStation™Network reachability states

## Definition

```
#include <np/np_common.h>
int sceNpRegisterNpReachabilityStateCallback(
	SceNpReachabilityStateCallback callback,
	void *userdata
);
```

## Arguments

|  |  |
| --- | --- |
| `callback` | Callback function to register (IN) |
| `userdata` | Arbitrary user data to pass to the callback function (IN) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_CALLBACK_ALREADY_REGISTERED` | 0x80550008 | Callback function is already registered |

## Description

This function registers a callback function that receives notifications when the PlayStation™Network reachability state changes.

## Notes

* This function is not multithread safe.
* Because this function entails inter-process communication in order to request processing to the system process, this function can block other processes for a long period of time depending on the system process load. Do not call this function from a thread onto which you do not want the effects of the system process load (the rendering thread, for example).

# sceNpUnregisterNpReachabilityStateCallback

Deregisters the callback function for notifying PlayStation™Network reachability states

## Definition

```
#include <np/np_common.h>
int sceNpUnregisterNpReachabilityStateCallback(
	void
);
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_CALLBACK_NOT_REGISTERED` | 0x80550009 | Callback function is not registered |

## Description

This function unregisters a callback function that receives notifications when the PlayStation™Network reachability state changes.

## Notes

* This function is not multithread safe.
* Because this function entails inter-process communication in order to request processing to the system process, this function can block other processes for a long period of time depending on the system process load. Do not call this function from a thread onto which you do not want the effects of the system process load (the rendering thread, for example).

## See Also

`sceNpRegisterNpReachabilityStateCallback()`