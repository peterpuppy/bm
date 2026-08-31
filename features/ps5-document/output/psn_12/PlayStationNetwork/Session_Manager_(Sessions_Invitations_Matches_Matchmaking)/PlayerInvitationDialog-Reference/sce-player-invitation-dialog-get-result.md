# PlayerInvitationDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerInvitationDialog-Reference/sce-player-invitation-dialog-get-result.html

# Player Invitation Dialog Operation

# ScePlayerInvitationDialogResult

Player invitation dialog call result

## Definition

```
#include <player_invitation_dialog.h>
typedef struct ScePlayerInvitationDialogResult {
	int32_t errorCode;
	SceCommonDialogResult result;
	uint8_t reserved[32];
} ScePlayerInvitationDialogResult;
```

## Members

|  |  |
| --- | --- |
| `errorCode` | Dialog termination status |
| `result` | Dialog call result |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used to obtain the result of calling the player invitation dialog with `scePlayerInvitationDialogGetResult()`. Before this structure is used, it is necessary to fill all its values with 0's and to initialize the structure, and then to set values to the required members.

`errorCode` indicates the termination status of the player invitation dialog. `SCE_OK` (=0) will be stored for normal termination, and a non-0 value will be stored for a fatal error.

`result` indicates the dialog call result. One of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_RESULT_OK` | 0 | Closed by user operation or `scePlayerInvitationDialogClose()` |
| `SCE_COMMON_DIALOG_RESULT_USER_CANCELED` | 1 | Canceled by the user |

`reserved` is a reserved area. This area must be filled with 0's.

## See Also

`scePlayerInvitationDialogGetResult()`

# scePlayerInvitationDialogClose

Close the player invitation dialog

## Definition

```
#include <player_invitation_dialog.h>
int32_t scePlayerInvitationDialogClose(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player invitation dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING` | 0x80B8000B | Player invitation dialog is not being displayed |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_CLOSE` | 0x80B8000C | Player invitation dialog is already closed |

## Description

This function closes the player invitation dialog.

This function can be called only while the operation status of the player invitation dialog is `SCE_COMMON_DIALOG_STATUS_RUNNING`. `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING` will return if this function is called at times other than the above.

When the call of this function succeeds and `scePlayerInvitationDialogUpdateStatus()` is periodically called thereafter, the dialog will carry out processing to close the dialog display; the operation status will transition to `SCE_COMMON_DIALOG_STATUS_FINISHED` upon processing completion.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

When this function is used to close the player invitation dialog, the call result obtained with `scePlayerInvitationDialogGetResult()` will be `SCE_COMMON_DIALOG_RESULT_OK`.

## See Also

`scePlayerInvitationDialogOpen()`, `scePlayerInvitationDialogGetResult()`

# scePlayerInvitationDialogGetResult

Get the player invitation dialog call result

## Definition

```
#include <player_invitation_dialog.h>
int32_t scePlayerInvitationDialogGetResult(
	ScePlayerInvitationDialogResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `result` | Obtained call result |

## Return Values

Stores the player invitation dialog call result in `*result` and returns the `(*result).result` value for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player invitation dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED` | 0x80B80005 | Player invitation dialog is not closed |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | 0x80B8000A | `result` is invalid |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | 0x80B8000D | `result` is NULL |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error occurred |

## Description

This function obtains the player invitation dialog call result.

The player invitation dialog call result will be stored in `*result`. For details on the call result, refer to `ScePlayerInvitationDialogResult`.

Fill all values in `*result` with 0's before using this function. `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` will return if `*result` is not filled with 0's when this function is called.

This function can only be called while the operation status of the player invitation dialog is `SCE_COMMON_DIALOG_STATUS_FINISHED`. Otherwise, `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED` will return.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`ScePlayerInvitationDialogResult`

# scePlayerInvitationDialogGetStatus

Get the player invitation dialog operation status

## Definition

```
#include <player_invitation_dialog.h>
SceCommonDialogStatus scePlayerInvitationDialogGetStatus(void)
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | 0 | Player invitation dialog is not running |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | 1 | Player invitation dialog is initialized |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | 2 | Player invitation dialog is being displayed |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | 3 | Player invitation dialog is closed |

## Description

This function obtains the operation status of the player invitation dialog. It is lighter than `scePlayerInvitationDialogUpdateStatus()`. It is useful for obtaining the status in a thread separate from the thread that updates the operation status.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`SceCommonDialogStatus`, `scePlayerInvitationDialogUpdateStatus()`

# scePlayerInvitationDialogOpen

Display the player invitation dialog

## Definition

```
#include <player_invitation_dialog.h>
int32_t scePlayerInvitationDialogOpen(
	const ScePlayerInvitationDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Player invitation dialog parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player invitation dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_INVALID_STATE` | 0x80B80006 | API is not in a callable state |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | 0x80B80009 | Insufficient memory |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | 0x80B8000A | `param` is invalid |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | 0x80B8000D | `param` is NULL |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error occurred |
| `SCE_COMMON_DIALOG_ERROR_INHIBIT_SHAREPLAY_CLIENT` | 0x80B80010 | While using the "Playing Game with Host" feature, attempted to display the player invitation dialog, which isn't permitted to be displayed to visitors |

## Description

This function displays the player invitation dialog.

For `*param`, specify the structure storing player invitation dialog parameters. Use this function for setting parameters (operation mode, for example) after initializing the structure first with `scePlayerInvitationDialogParamInitialize()`.

`SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` will return when the content of `param` is invalid. The operation status of the dialog will not change at this time.

This function can only be called while the operation status of the player invitation dialog is `SCE_COMMON_DIALOG_STATUS_INITIALIZED` or `SCE_COMMON_DIALOG_STATUS_FINISHED`. Otherwise, `SCE_COMMON_DIALOG_ERROR_INVALID_STATE` will return.

When the call of this function succeeds, the operation status of the dialog will immediately transition to `SCE_COMMON_DIALOG_STATUS_RUNNING`.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## Examples

```
ScePlayerInvitationDialogParam param;

scePlayerInvitationDialogParamInitialize( &param );
param.mode = SCE_PLAYER_INVITATION_DIALOG_MODE_SEND;
param.userId = userId;

ScePlayerInvitationDialogSendParam sendParam;
memset(&sendParam, 0, sizeof(sendParm));
sendParam.sessionId = sessionId;
param.sendParam = &sendParam;

if ( scePlayerInvitationDialogOpen( &param ) < 0 ) {
	// Error handling
}
```

## See Also

`ScePlayerInvitationDialogParam`, `scePlayerInvitationDialogParamInitialize()`

# scePlayerInvitationDialogUpdateStatus

Update and get the player invitation dialog operation status

## Definition

```
#include <player_invitation_dialog.h>
SceCommonDialogStatus scePlayerInvitationDialogUpdateStatus(void)
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | 0 | Player invitation dialog is not running |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | 1 | Player invitation dialog is initialized |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | 2 | Player invitation dialog is being displayed |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | 3 | Player invitation dialog is closed |

## Description

This function updates and obtains the operation status of the player invitation dialog.

After opening the dialog, be sure to call this function at regular intervals (for example, at every rendering frame) until the operation status of the dialog becomes `SCE_COMMON_DIALOG_STATUS_FINISHED`.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`scePlayerInvitationDialogGetStatus()`