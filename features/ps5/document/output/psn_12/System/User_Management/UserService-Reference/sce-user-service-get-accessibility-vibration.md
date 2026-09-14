# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-get-accessibility-vibration.html

# Obtaining Accessibility Settings

# sceUserServiceGetAccessibilityChatTranscription

Gets an accessibility setting (Enable Chat Transcription)

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAccessibilityChatTranscription(
	SceUserServiceUserId userId,
	int32_t *chatTranscription
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `chatTranscription` | Destination to store the obtained accessibility setting (Enable Chat Transcription) |

## Return Values

Stores the obtained configuration value in `*chatTranscription` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the system software "Enable Chat Transcription" configuration value for a logged-in user.

For `userId`, specify the user ID of the target user.

For `*chatTranscription`, 1 will be stored if the user has enabled the chat transcription feature, and 0 will be stored if they have not.

Refer to the [VoiceChat Library Overview](../VoiceChat-Overview/__document_toc.html) document for an overview of the chat transcription feature.

Obtaining this configuration value is not required to use the chat transcription feature provided by the system software, but the value obtained can be used as the default value when an application implements such a feature on its own.

## Examples

```
int32_t ret;
int32_t chatTranscription;
ret = sceUserServiceGetAccessibilityChatTranscription(userId, &chatTranscription);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetAccessibilityPressAndHoldDelay

Gets an accessibility setting (Press and Hold Delay)

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAccessibilityPressAndHoldDelay(
	SceUserServiceUserId userId,
	int32_t *pressAndHoldDelay
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `pressAndHoldDelay` | Destination to store the obtained accessibility setting (Press and Hold Delay) |

## Return Values

Stores the obtained configuration value in `*pressAndHoldDelay` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the configuration value for the system software "Press and Hold Delay" setting (the amount of time that has been set for a button press to be considered held down) for a logged-in user.

For `userId`, specify the user ID of the target user.

For `*pressAndHoldDelay`, 1 will be stored if the user has set a longer time until a button press is considered held down, and 0 will be stored if not.

## Examples

```
int32_t ret;
int32_t pressAndHoldDelay;
ret = sceUserServiceGetAccessibilityPressAndHoldDelay(userId, &pressAndHoldDelay);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetAccessibilityTriggerEffect

Gets an accessibility setting (Trigger Effect Intensity)

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAccessibilityTriggerEffect(
	SceUserServiceUserId userId,
	int32_t *triggerEffect
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `triggerEffect` | Destination to store the obtained accessibility setting (Trigger Effect Intensity) |

## Return Values

Stores the obtained configuration value in `*triggerEffect` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the system software "Trigger Effect Intensity" configuration value for a logged-in user.

For `userId`, specify the user ID of the target user.

One of the following values will be stored in `*triggerEffect`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_TRIGGER_EFFECT_INTENSITY_OFF` | 0 | Off |
| `SCE_USER_SERVICE_TRIGGER_EFFECT_INTENSITY_STRONG` | 1 | Strong (Standard) |
| `SCE_USER_SERVICE_TRIGGER_EFFECT_INTENSITY_MEDIUM` | 2 | Medium |
| `SCE_USER_SERVICE_TRIGGER_EFFECT_INTENSITY_WEAK` | 3 | Weak |

## Examples

```
int32_t ret;
int32_t triggerEffect;
ret = sceUserServiceGetAccessibilityTriggerEffect(userId, &triggerEffect);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetAccessibilityVibration

Gets an accessibility setting (Vibration Intensity)

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAccessibilityVibration(
	SceUserServiceUserId userId,
	int32_t *vibration
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `vibration` | Destination to store the obtained accessibility setting (Vibration Intensity) |

## Return Values

Stores the obtained configuration value in `*vibration` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the system software "Vibration Intensity" configuration value for a logged-in user.

For `userId`, specify the user ID of the target user.

One of the following values will be stored in `*vibration`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_VIBRATION_INTENSITY_OFF` | 0 | Off |
| `SCE_USER_SERVICE_VIBRATION_INTENSITY_STRONG` | 1 | Strong (Standard) |
| `SCE_USER_SERVICE_VIBRATION_INTENSITY_MEDIUM` | 2 | Medium |
| `SCE_USER_SERVICE_VIBRATION_INTENSITY_WEAK` | 3 | Weak |

## Examples

```
int32_t ret;
int32_t vibration;
ret = sceUserServiceGetAccessibilityVibration(userId, &vibration);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetAccessibilityZoomEnabled

Gets an accessibility setting (Zoom)

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAccessibilityZoomEnabled(
	SceUserServiceUserId userId,
	int32_t *zoomEnabled
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `zoomEnabled` | Destination to store the obtained accessibility setting (Zoom) |

## Return Values

Stores the obtained configuration value in `*zoomEnabled` returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the system software "Zoom" configuration value for a logged-in user.

For `userId`, specify the user ID of the target user.

For `*zoomEnabled`, 1 will be stored if the user has enabled zoom, and 0 will be stored if not.

## Examples

```
int32_t ret;
int32_t zoomEnabled;
ret = sceUserServiceGetAccessibilityZoomEnabled(userId, &zoomEnabled);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetAccessibilityZoomFollowFocus

Gets an accessibility setting ("Adjust Display Area to Movement" for zoom)

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAccessibilityZoomFollowFocus(
	SceUserServiceUserId userId,
	int32_t *zoomFollowFocus
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `zoomFollowFocus` | Destination to store the obtained accessibility setting ("Adjust Display Area to Movement" for zoom) |

## Return Values

Stores the obtained configuration value in `*zoomFolllowFocus` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the system software's configuration value of "Adjust Display Area to Movement" for zoom for a logged-in user.

For `userId`, specify the user ID of the target user.

For `*zoomFollowFocus`, 1 will be stored if the user has enabled the feature for adjusting the display area to zoom movement, and 0 will be stored if not.

## Examples

```
int32_t ret;
int32_t zoomEnabled;
ret = sceUserServiceGetAccessibilityZoomFollowFocus (userId, &zoomFollowFocus);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`