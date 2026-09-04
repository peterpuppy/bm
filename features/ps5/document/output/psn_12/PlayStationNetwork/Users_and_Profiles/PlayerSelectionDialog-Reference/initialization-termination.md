# PlayerSelectionDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerSelectionDialog-Reference/initialization-termination.html

# Initialization/Termination

# scePlayerSelectionDialogInitialize

Initialize the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
int32_t scePlayerSelectionDialogInitialize(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_SYSTEM_INITIALIZED` | 0x80B80001 | Common dialog process is not started |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_INITIALIZED` | 0x80B80004 | Player selection dialog is already initialized |
| `SCE_COMMON_DIALOG_ERROR_BUSY` | 0x80B80008 | Another common dialog is running |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | 0x80B80009 | Insufficient memory |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error occurred |

## Description

This function initializes the player selection dialog.

This function can only be called when other common dialog features (including the player selection dialog itself) are not called. When this function is called during use of another common dialog feature, `SCE_COMMON_DIALOG_ERROR_BUSY` will be returned.

When the call of this function succeeds, the operation status immediately changes to `SCE_COMMON_DIALOG_STATUS_INITIALIZED`.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## Examples

```
if (scePlayerSelectionDialogInitialize() < 0 ) {
    // Error handling
}
```

## See Also

`scePlayerSelectionDialogTerminate()`

# scePlayerSelectionDialogTerminate

Terminate the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
int32_t scePlayerSelectionDialogTerminate(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (a negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player selection dialog is not initialized |

## Description

This function terminates the player selection dialog.

After initializing the player selection dialog with `scePlayerSelectionDialogInitialize()`, it must always be terminated with scePlayerSelectionDialogTerminate().

To quickly abort dialog display by the application, display can be terminated faster by calling this function rather than `scePlayerSelectionDialogClose()`.

This function can be called regardless of the dialog's operation status as long as it is after the player selection dialog has been initialized with `scePlayerSelectionDialogInitialize()`. `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` will be returned if the player selection dialog is not initialized.

When the call of this function succeeds, the operation status will immediately transition to `SCE_COMMON_DIALOG_STATUS_NONE`.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`scePlayerSelectionDialogInitialize()`