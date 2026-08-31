# SigninDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SigninDialog-Reference/sce-signin-dialog-terminate.html

# Initialization/Termination

# sceSigninDialogInitialize

Initialize the signin dialog

## Definition

```
#include <signin_dialog.h>
int32_t sceSigninDialogInitialize()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error code defined by this library is shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_ERROR_ALREADY_INITIALIZED` | 0x81350002 | Signin dialog is already initialized |

## Description

This function initializes the signin dialog.

When the call of this function succeeds, the operation status will immediately transition from `SCE_SIGNIN_DIALOG_STATUS_NONE` to `SCE_SIGNIN_DIALOG_STATUS_INITIALIZED`.

If the signin dialog is already initialized, `SCE_SIGNIN_DIALOG_ERROR_ALREADY_INITIALIZED` returns.

## See Also

`sceSigninDialogTerminate()`

# sceSigninDialogTerminate

Terminate the signin dialog

## Definition

```
#include <signin_dialog.h>
int32_t sceSigninDialogTerminate()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error code defined by this library is shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81350001 | Signin dialog is not initialized |

## Description

This function terminates the signin dialog.

After initializing the signin dialog with `sceSigninDialogInitialize()`, this function must ultimately be called to terminate the dialog.

To quickly abort dialog processing by the application, display can be terminated faster by calling this function rather than `sceSigninDialogClose()`.

This function can be called regardless of the dialog's operation status as long as it is after the signin dialog has been initialized with `sceSigninDialogInitialize()`. `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` returns if the signin dialog is not initialized.

When the call of this function succeeds, the operation status will immediately transition to `SCE_SIGNIN_DIALOG_STATUS_NONE`.

## See Also

`sceSigninDialogInitialize()`, `sceSigninDialogClose()`