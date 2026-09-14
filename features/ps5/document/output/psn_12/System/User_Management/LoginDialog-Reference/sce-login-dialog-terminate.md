# LoginDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginDialog-Reference/sce-login-dialog-terminate.html

# Initialization/Termination

# sceLoginDialogInitialize

Initialize the login dialog

## Definition

```
#include <login_dialog.h>
int32_t sceLoginDialogInitialize()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error code defined by this library is shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_ERROR_ALREADY_INITIALIZED` | 0x81340002 | Login dialog is already initialized |

## Description

This function initializes the login dialog.

When the call of this function succeeds, the operation status will immediately transition from `SCE_LOGIN_DIALOG_STATUS_NONE` to `SCE_LOGIN_DIALOG_STATUS_INITIALIZED`.

If the login dialog is already initialized, `SCE_LOGIN_DIALOG_ERROR_ALREADY_INITIALIZED` returns.

## See Also

`sceLoginDialogTerminate()`

# sceLoginDialogTerminate

Terminate the login dialog

## Definition

```
#include <login_dialog.h>
int32_t sceLoginDialogTerminate()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error code defined by this library is shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81340001 | Login dialog is not initialized |

## Description

This function terminates the login dialog.

After initializing the login dialog with `sceLoginDialogInitialize()`, this function must ultimately be called to terminate the dialog.

To quickly abort dialog processing by the application, display can be terminated faster by calling this function rather than `sceLoginDialogClose()`.

This function can be called regardless of the dialog's operation status as long as it is after the login dialog has been initialized with `sceLoginDialogInitialize()`. `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` returns if the login dialog is not initialized.

When the call of this function succeeds, the operation status will immediately transition to `SCE_LOGIN_DIALOG_STATUS_NONE`.

## See Also

`sceLoginDialogInitialize()`, `sceLoginDialogClose()`