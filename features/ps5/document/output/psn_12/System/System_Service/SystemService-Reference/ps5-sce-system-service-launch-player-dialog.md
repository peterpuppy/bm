# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-launch-player-dialog.html

# Launching Player Dialogs

# sceSystemServiceInitializePlayerDialogParam

Initializes the player dialog structure

## Definition

```
#include <system_service.h>
void sceSystemServiceInitializePlayerDialogParam(
	SceSystemServicePlayerDialogParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Pointer to an `SceSystemServicePlayerDialogParam` structure |

## Return Values

None

## Description

This function initializes an `SceSystemServicePlayerDialogParam` structure to its default values and sets the size of the structure (its `size` member). Do not change the value of the `size` member after calling this function.

## See Also

`sceSystemServiceLaunchPlayerDialog()`

# sceSystemServiceLaunchPlayerDialog

Launch a player dialog

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceLaunchPlayerDialog(
	const SceSystemServicePlayerDialogParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Pointer to an `SceSystemServicePlayerDialogParam` structure |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_INTERNAL` | 0x80A10001 | Unexpected internal error occurred |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | Parameter is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_INVALID_URI_LEN` | 0x80A10007 | Error occurred when launching player dialog |

## Description

This function launches one of the player dialogs that comes standard with the system software and initiates actions relating to players on the PlayStation™Network.

For `param`, specify a pointer to an `SceSystemServicePlayerDialogParam` structure.

You must first use `sceSystemServiceInitializePlayerDialogParam()` to initialize the structure with its default values. Then, specify values for the members of the structure as the application's purposes require before calling the function described under this header. When this function is called, control immediately returns to the application, and the application transitions to background status.

## Examples

```
SceSystemServicePlayerDialogParam yourDialogParam; 

/* Structure initialized with the default values */
sceSystemServiceInitializePlayerDialogParam(&yourDialogParam);

/* This must be a valid userId, which can be obtained
 * using sceUserServiceGetInitialUser()
 */
yourDialogParam.userId = 123456;

/* This must be the valid accountId of the player whom the dialog's action
 * is targeting
 */
yourDialogParam.targetAccountId = 12345678;

/* Set the display mode */
yourDialogParam.mode = SCE_SYSTEM_SERVICE_LAUNCH_PROFILE;

int ret;

ret = sceSystemServiceLaunchPlayerDialog(&yourDialogParam);
if ((ret == SCE_OK)) {
    printf("Player Profile Has Been Launched!\n");
}
```

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, the library may not operate as expected afterward. Make sure to program the application so that this function is not called at the same time by multiple threads.

# SceSystemServicePlayerDialogParam

Player dialog structure

## Definition

```
#include <system_service.h>
typedef struct SceSystemServicePlayerDialogParam {
	size_t size;
	SceSystemServicePlayerDialogMode mode;
	SceUserServiceUserId userId;
	uint64_t targetAccountId;
	uint8_t reserved[40];
} SceSystemServicePlayerDialogParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of the `SceSystemServicePlayerDialogParam` structure |
| `mode` | Display mode of the player dialog |
| `userId` | User ID of the user operating the application |
| `targetAccountId` | Account ID of the target player |
| `reserved` | Reserved area |

## Description

This structure is used when launching a player dialog with `sceSystemServiceLaunchPlayerDialog()`.

## See Also

`sceSystemServiceInitializePlayerDialogParam()`

# SceSystemServicePlayerDialogMode

Display mode of the player dialog

## Definition

```
#include <system_service.h>
typedef enum {
	SCE_SYSTEM_SERVICE_SEND_FRIEND_REQUEST = 0,
	SCE_SYSTEM_SERVICE_BLOCK_USER,
	SCE_SYSTEM_SERVICE_LAUNCH_PROFILE
} SceSystemServicePlayerDialogMode;
```

## Description

This type is for indicating the display mode of a player dialog. One of the following values can be used.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_SEND_FRIEND_REQUEST` | 0 | Friend request mode |
| `SCE_SYSTEM_SERVICE_BLOCK_USER` | 1 | Block list registration mode |
| `SCE_SYSTEM_SERVICE_LAUNCH_PROFILE` | 2 | Profile display mode |

In friend request mode, the application can send a friend request from the user currently operating the system to the specified player. If a friend request has already been sent to the specified player, or if the user and the player are already friends, an appropriate message will be displayed to the user.

In block list registration mode, the user can block the specified player.

In profile display mode, the profile screen of the specified player launches, and the user in control of the system can view detailed information about the specified user or engage in profile editing.

## See Also

`SceSystemServicePlayerDialogParam`