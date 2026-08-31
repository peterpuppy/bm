# NpAuthAuthorizedAppDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuthAuthorizedAppDialog-Reference/sce-np-auth-authorized-app-dialog-initialize.html

# Initialization/Termination

# sceNpAuthAuthorizedAppDialogInitialize

Initialize the NpAuth Authorized App dialog

## Definition

```
#include <np_auth_authorized_app_dialog.h>
int32_t sceNpAuthAuthorizedAppDialogInitialize(void);
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_SYSTEM_INITIALIZED` | 0x80B80001 | Common dialog process is not started |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_INITIALIZED` | 0x80B80004 | The NpAuth Authorized App dialog is already initialized |
| `SCE_COMMON_DIALOG_ERROR_BUSY` | 0x80B80008 | Other common dialogs are operating |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | 0x80B80009 | Memory is insufficient |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error has occurred |

## Description

This function initializes the NpAuth Authorized App dialog.

This function can only be called when other common dialog features (including the NpAuth Authorized App dialog itself) are not being called. Calling this function while other common dialog features are in use returns `SCE_COMMON_DIALOG_ERROR_BUSY`.

If successfully called, the operational status immediately transitions to `SCE_COMMON_DIALOG_STATUS_INITIALIZED`.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.

## Example

```
if (sceNpAuthAuthorizedAppDialogInitialize() < 0) {
    // Error handling
}
```

## See Also

`sceNpAuthAuthorizedAppDialogTerminate()`

# sceNpAuthAuthorizedAppDialogTerminate

Terminate the NpAuth Authorized App dialog

## Definition

```
#include <np_auth_authorized_app_dialog.h>
int32_t sceNpAuthAuthorizedAppDialogTerminate(void);
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | The NpAuth Authorized App dialog is not initialized |

## Description

This function terminates the NpAuth Authorized App dialog.

After initializing NpAuth Authorized App dialog with `sceNpAuthAuthorizedAppDialogInitialize()`, it is necessary to terminate the dialog using this function.

If you would like to urgently interrupt the display of the dialog from your application, you can call this function to terminate the display more quickly than is possible with `sceNpAuthAuthorizedAppDialogClose()`.

This function can be called regardless of the operational status if the NpAuth Authorized App dialog has already been initialized with `sceNpAuthAuthorizedAppDialogInitialize()`. If the NpAuth Authorized App dialog is not initialized, this function returns `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED`.

If this function is successfully called, the operational status immediately transitions to `SCE_COMMON_DIALOG_STATUS_NONE`.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.