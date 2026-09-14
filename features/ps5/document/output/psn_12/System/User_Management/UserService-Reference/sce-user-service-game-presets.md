# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-game-presets.html

# Obtaining Game Presets

# SceUserServiceGamePresets

Game presets

## Definition

```
#include <user_service.h>

typedef struct SceUserServiceGamePresets {
	size_t thisSize;
	uint32_t difficulty;
	uint32_t priority;
	uint32_t invertVerticalViewFor1stPersonView;
	uint32_t invertHorizontalViewFor1stPersonView;
	uint32_t invertVerticalViewFor3rdPersonView;
	uint32_t invertHorizontalViewFor3rdPersonView;
	uint32_t displaySubtitles;
	uint32_t audioLanguage;
	uint32_t joinableUserType;
	uint32_t invitableUserType;
} SceUserServiceGamePresets;
```

## Members

|  |  |
| --- | --- |
| `thisSize` | Size of this structure |
| `difficulty` | Difficulty |
| `priority` | Whether to prioritize performance or resolution |
| `invertVerticalViewFor1stPersonView` | Whether to invert vertical camera operations in first-person view |
| `invertHorizontalViewFor1stPersonView` | Whether to invert horizontal camera operations in first-person view |
| `invertVerticalViewFor3rdPersonView` | Whether to invert vertical camera operations in third-person view |
| `invertHorizontalViewFor3rdPersonView` | Whether to invert horizontal camera operations in third-person view |
| `displaySubtitles` | Whether or not to display subtitles |
| `audioLanguage` | Audio language |
| `joinableUserType` | Users who can join Player Sessions without invitations |
| `invitableUserType` | Members who can send invitations to Player Sessions |

One of the following values will be stored for `difficulty`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_NOT_SET` | 0 | Game Default |
| `SCE_USER_SERVICE_GAME_PRESETS_DIFFICULTY_EASIEST` | 1 | Easiest |
| `SCE_USER_SERVICE_GAME_PRESETS_DIFFICULTY_EASY` | 2 | Easy |
| `SCE_USER_SERVICE_GAME_PRESETS_DIFFICULTY_DEFAULT` | 3 | Normal |
| `SCE_USER_SERVICE_GAME_PRESETS_DIFFICULTY_HARD` | 4 | Hard |
| `SCE_USER_SERVICE_GAME_PRESETS_DIFFICULTY_HARDEST` | 5 | Hardest |

One of the following values will be stored for `priority`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_NOT_SET` | 0 | Game Default |
| `SCE_USER_SERVICE_GAME_PRESETS_PRIORITY_PERFORMANCE` | 1 | Prioritize performance |
| `SCE_USER_SERVICE_GAME_PRESETS_PRIORITY_RESOLUTION` | 2 | Prioritize resolution |

One of the following values will be stored for `invertVerticalViewFor1stPersonView`, `invertHorizontalViewFor1stPersonView`, `invertVerticalViewFor3rdPersonView`, and `invertHorizontalViewFor3rdPersonView`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_NOT_SET` | 0 | Game Default |
| `SCE_USER_SERVICE_GAME_PRESETS_INVERT_OFF` | 1 | Do not invert camera operations |
| `SCE_USER_SERVICE_GAME_PRESETS_INVERT_ON` | 2 | Invert camera operations |

One of the following values will be stored for `displaySubtitles`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_NOT_SET` | 0 | Game Default |
| `SCE_USER_SERVICE_GAME_PRESETS_DISPLAY_SUBTITLES_OFF` | 1 | Do not display subtitles |
| `SCE_USER_SERVICE_GAME_PRESETS_DISPLAY_SUBTITLES_ON` | 2 | Display subtitles |

One of the following values will be stored for `audioLanguage`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_AUDIO_LANGUAGE_SAME_AS_SYSTEM` | 0 | Same as console |
| `SCE_USER_SERVICE_GAME_PRESETS_AUDIO_LANGUAGE_ORIGINAL_AUDIO` | 1 | Game's original audio |

One of the following values will be stored for `joinableUserType`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_NOT_SET` | 0 | Game Default |
| `SCE_USER_SERVICE_GAME_PRESETS_PLAYER_SESSION_JOINABLE_USER_TYPE_NO_ONE` | 1 | No one can join without an invitation |
| `SCE_USER_SERVICE_GAME_PRESETS_PLAYER_SESSION_JOINABLE_USER_TYPE_FRIENDS` | 2 | Friends of the leader can join |
| `SCE_USER_SERVICE_GAME_PRESETS_PLAYER_SESSION_JOINABLE_USER_TYPE_FRIENDS_OF_FRIENDS` | 3 | Friends of friends of the leader can join |
| `SCE_USER_SERVICE_GAME_PRESETS_PLAYER_SESSION_JOINABLE_USER_TYPE_ANYONE` | 4 | Anyone can join |

One of the following values will be stored for `invitableUserType`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_GAME_PRESETS_NOT_SET` | 0 | Game Default |
| `SCE_USER_SERVICE_GAME_PRESETS_PLAYER_SESSION_INVITABLE_USER_TYPE_LEADER` | 1 | Only the leader can invite others |
| `SCE_USER_SERVICE_GAME_PRESETS_PLAYER_SESSION_INVITABLE_USER_TYPE_MEMBER` | 2 | All participating members can invite others |

## Description

This datatype is for obtaining a user's game presets with `sceUserServiceGetGamePresets()`.

Refer to the [UserService Library Overview](../UserService-Overview/__document_toc.html) document regarding the meaning of each member variable and the usage of received values.

# sceUserServiceGamePresetsInitialize

Initializes game presets

## Definition

```
#include <user_service.h>
static inline
void sceUserServiceGamePresetsInitialize(SceUserServiceGamePresets *presets)
{
	memset( presets, 0x0, sizeof(SceUserServiceGamePresets) );

	presets->thisSize = sizeof(SceUserServiceGamePresets);
}
```

## Arguments

|  |  |
| --- | --- |
| `presets` | Game presets |

## Return Values

None

## Description

This function initializes game presets.

Make sure to call this function to initialize the structure before calling `sceUserServiceGetGamePresets()` and obtaining game presets. Appropriate default values will be set to each of the `*presets` members by calling this function.

Refer to `SceUserServiceGamePresets` for details on each parameter.

## Examples

```
SceUserServiceGamePresets presets;
sceUserServiceGamePresetsInitialize( &presets );
```

# sceUserServiceGetGamePresets

Gets game presets

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetGamePresets(
	SceUserServiceUserId userId,
	SceUserServiceGamePresets *presets
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `presets` | Destination to store obtained game presets |

## Return Values

Stores game presets in `*presets` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains game presets of the logged in user.

For `userId`, specify the user ID of the target user.

`SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` will be returned if the specified destination to store game `presets` has not been initialized with `sceUserServiceGamePresetsInitialize()`.

## Examples

```
int ret = 0;
SceUserServiceGamePresets presets;

sceUserServiceGamePresetsInitialize( &presets );

ret = sceUserServiceGetGamePresets( userId, &presets );
if (ret != SCE_OK) {
	// Error handling
}
```