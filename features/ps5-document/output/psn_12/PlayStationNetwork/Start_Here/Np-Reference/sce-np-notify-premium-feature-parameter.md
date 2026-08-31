# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/sce-np-notify-premium-feature-parameter.html

# Premium Features

# SCE\_NP\_PREMIUM\_FEATURE

Premium feature types

## Definition

```
#include <np/np_common.h>
#define SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY	0x1
```

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY` | 1 | Real-time multiplayer |

## Description

The above constant represents a Premium feature.

Refer to the [Premium Features Guidelines](../Premium_Features_Guidelines/__document_toc.html) document for details about Premium features.

## See Also

`SceNpNotifyPremiumFeatureParameter`, `SceNpCheckPremiumParameter`

# SCE\_NP\_REALTIME\_MULTIPLAY\_PROPERTY

Real-time multiplayer properties

## Definition

```
#include <np/np_common.h>
#define SCE_NP_REALTIME_MULTIPLAY_PROPERTY_NONE			 (0x0)
#define SCE_NP_REALTIME_MULTIPLAY_PROPERTY_CROSS_PLATFORM_PLAY	 (0x1)
#define SCE_NP_REALTIME_MULTIPLAY_PROPERTY_IN_ENGINE_SPECTATING (0x2)
```

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_REALTIME_MULTIPLAY_PROPERTY_NONE` | 0 | Property not specified (ordinary use of the real-time multiplayer feature that does not apply to the use below) |
| `SCE_NP_REALTIME_MULTIPLAY_PROPERTY_CROSS_PLATFORM_PLAY` | 1 | Cross-Platform Play |
| `SCE_NP_REALTIME_MULTIPLAY_PROPERTY_IN_ENGINE_SPECTATING` | 2 | In-Engine Spectating |

## Description

The above flags represent real-time multiplayer properties. Specify when calling `sceNpNotifyPremiumFeature()`.

Refer to the [Premium Features Guidelines](../Premium_Features_Guidelines/__document_toc.html) document for details of each property.

## See Also

`SceNpNotifyPremiumFeatureParameter`

# SceNpNotifyPremiumFeatureParameter

Notification parameters for using a Premium feature

## Definition

```
#include <np/np_common.h>
typedef struct SceNpNotifyPremiumFeatureParameter {
	size_t size;
	SceUserServiceUserId userId;
	char padding[4];
	uint64_t features;
	uint64_t properties;
	uint8_t reserved[24];
} SceNpNotifyPremiumFeatureParameter;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID |
| `padding` | Not used (clear with 0's) |
| `features` | Premium feature type |
| `properties` | Real-time multiplayer properties |
| `reserved` | Not used (clear with 0's) |

## Description

This structure represents the parameters to specify upon calling `sceNpNotifyPremiumFeature()`.

For `size`, specify the size of this structure.

For `features`, specify the value of the Premium feature type as a bit flag. Refer to the "[SCE\_NP\_PREMIUM\_FEATURE](scenppremiumfeature.html)" section for details.

For `properties`, specify real-time multiplayer properties. Refer to the "[SCE\_NP\_REALTIME\_MULTIPLAY\_PROPERTY](scenprealtimemultiplayproperty.html)" section for details.

Clear `padding` and `reserved` with 0's.

# sceNpNotifyPremiumFeature

Notifies the use of a Premium feature

## Definition

```
#include <np/np_common.h>
int sceNpNotifyPremiumFeature(
	const SceNpNotifyPremiumFeatureParameter *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Premium feature notification parameters (IN) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |

## Description

This function notifies the system that a Premium feature is being executed.

An application using a Premium feature must notify the system when it is executing a Premium feature. Refer to the [Premium Features Guidelines](../Premium_Features_Guidelines/__document_toc.html) document for details.

The usage of this function when using a Premium feature (real-time multiplayer) is as follows:

* Call this function periodically (for example, every second) during use of the real-time multiplayer feature.
* Immediately stop calling this function when real-time multiplayer gameplay is exited due to a user operation or network disconnection.

## See Also

`sceNpCheckPremium()`

# SceNpPremiumEventType

Premium feature event type

## Definition

```
#include <np/np_common.h>
typedef int32_t SceNpPremiumEventType;
#define SCE_NP_PREMIUM_EVENT_RECHECK_NEEDED 1
```

## Description

This integer represents a Premium feature event type.

`SCE_NP_PREMIUM_EVENT_RECHECK_NEEDED` occurs when a Premium check is required again to ensure that the user has the eligibility to use the applicable Premium feature. Refer to the [Premium Features Guidelines](../Premium_Features_Guidelines/__document_toc.html) document for details.

## See Also

`SceNpPremiumEventCallback`

# SceNpPremiumEventCallback

Callback to receive event notification about a Premium feature

## Definition

```
#include <np/np_common.h>
typedef void (*SceNpPremiumEventCallback)(
	SceUserServiceUserId userId,
	SceNpPremiumEventType event,
	void *userdata
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `event` | Premium feature event type |
| `userdata` | User data set upon callback function registration |

## Return Values

None

## Description

This is a prototype for a callback function that receives event notifications about a Premium feature. Implement the function following the specifications described here, and register it using `sceNpRegisterPremiumEventCallback()` wherever you want to monitor Premium feature events. Deregister the function using `sceNpUnregisterPremiumEventCallback()` when you no longer need to monitor Premium feature events.

After you register this callback function, it will be called when you periodically call `sceNpCheckCallback()`.

## Notes

Avoid processing that would require large amounts of time within the callback function and return promptly.

# sceNpRegisterPremiumEventCallback

Registers the callback function for notifying a Premium feature event

## Definition

```
#include <np/np_common.h>
int sceNpRegisterPremiumEventCallback(
	SceNpPremiumEventCallback callback,
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

This function registers the callback function that receives events about Premium features. After the callback function is registered, it will be called due to an event when `sceNpCheckCallback()` is called periodically.

Currently, the registration of the callback function is optional - note that the only event that will be notified is when a Premium check is required again to ensure that the user has the eligibility to use the applicable Premium feature. Refer to the [Premium Features Guidelines](../Premium_Features_Guidelines/__document_toc.html) document for details.

"PlayStation™Network - Premium Recheck Event Interval" of "★Debug Settings" is provided as a debug feature. When "Premium Recheck Event Interval" is "1 Minute Intervals", a notification to prompt a Premium check again will occur in 1-minute intervals.

## Notes

Premium feature events will continue to be notified even when exiting from the used Premium feature as long as the callback function remains registered. To avoid a malfunction, deregister the callback function upon exiting from the Premium feature.

## See Also

`sceNpUnregisterPremiumEventCallback()`, `sceNpCheckPremium()`

# sceNpUnregisterPremiumEventCallback

Deregisters the callback function for notifying Premium feature events

## Definition

```
#include <np/np_common.h>
int sceNpUnregisterPremiumEventCallback(
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

This function deregisters the callback function that receives Premium feature events.

## See Also

`sceNpRegisterPremiumEventCallback()`