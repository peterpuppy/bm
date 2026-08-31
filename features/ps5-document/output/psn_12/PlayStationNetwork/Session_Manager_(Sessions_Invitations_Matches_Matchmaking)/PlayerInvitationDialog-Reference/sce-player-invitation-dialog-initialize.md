# PlayerInvitationDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerInvitationDialog-Reference/sce-player-invitation-dialog-initialize.html

# Initialization/Termination

# scePlayerInvitationDialogInitialize

Initialize the player invitation dialog

## Definition

```
#include <player_invitation_dialog.h>
#include <user_service.h>
int32_t scePlayerInvitationDialogInitialize(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_SYSTEM_INITIALIZED` | 0x80B80001 | Common dialog process is not started |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_INITIALIZED` | 0x80B80004 | Player invitation dialog is already initialized |
| `SCE_COMMON_DIALOG_ERROR_BUSY` | 0x80B80008 | Another common dialog is running |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | 0x80B80009 | Insufficient memory |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error occurred |

## Description

This function initializes the player invitation dialog.

This function can only be called during periods when other common dialog features (including the player invitation dialog itself) are not called. `SCE_COMMON_DIALOG_ERROR_BUSY` will return when this function is called during the use of another common dialog feature.

When the call of this function succeeds, the operation status of the dialog will immediately transition to `SCE_COMMON_DIALOG_STATUS_INITIALIZED`.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## Examples

```
if ( scePlayerInvitationDialogInitialize() < 0 ) {
    // Error handling
}
```

## See Also

`scePlayerInvitationDialogTerminate()`

# scePlayerInvitationDialogTerminate

Terminate the player invitation dialog

## Definition

```
#include <player_invitation_dialog.h>
int32_t scePlayerInvitationDialogTerminate(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player invitation dialog is not initialized |

## Description

This function terminates the player invitation dialog.

After the player invitation dialog is initialized with `scePlayerInvitationDialogInitialize()`, the dialog must always be terminated with scePlayerInvitationDialogTerminate().

To perform an emergency abort of the dialog display from the application, call this function to terminate dialog display faster than `scePlayerInvitationDialogClose()`.

This function can be called regardless of the operation status of the player invitation dialog as long as the dialog has been initialized with `scePlayerInvitationDialogInitialize()`. `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` will return if the dialog has not been initialized.

When the call of this function succeeds, the operation status of the dialog will immediately transition to `SCE_COMMON_DIALOG_STATUS_NONE`.

For details on operation statuses, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`scePlayerInvitationDialogInitialize()`