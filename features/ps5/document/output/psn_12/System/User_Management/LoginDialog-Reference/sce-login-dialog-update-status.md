# LoginDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginDialog-Reference/sce-login-dialog-update-status.html

# Login Dialog Processing

# SceLoginDialogResult

Login dialog call result

## Definition

```
#include <login_dialog.h>
typedef struct SceLoginDialogResult {
	int32_t result;
	SceUserServiceUserId selectedUser;
	int32_t reserved[2];
} SceLoginDialogResult;
```

## Members

|  |  |
| --- | --- |
| `result` | Login dialog call result |
| `selectedUser` | User selected with login dialog |
| `reserved` | Reserved area |

## Description

This structure obtains the login dialog call result with `sceLoginDialogGetResult()`.

In `result`, the login dialog call result will be stored. When the call result obtaining terminates normally, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_RESULT_OK` | 0 | Login dialog terminated normally |
| `SCE_LOGIN_DIALOG_RESULT_USER_CANCELED` | 1 | Login dialog was cancelled by user operation |

In `selectedUser`, the ID of the user selected by the login dialog will be stored. This member value will only be valid when `result` is `SCE_LOGIN_DIALOG_RESULT_OK`.

`reserved` is a reserved area.

## See Also

`sceLoginDialogGetResult()`

# SceLoginDialogStatus

enum constant representing the login dialog status

## Definition

```
#include <login_dialog.h>
typedef enum SceLoginDialogStatus;
```

## Description

This enum constant represents the status of the login dialog. It can be obtained with `sceLoginDialogUpdateStatus()` or `sceLoginDialogGetStatus()`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_STATUS_NONE` | 0 | Login dialog is not running |
| `SCE_LOGIN_DIALOG_STATUS_INITIALIZED` | 1 | Login dialog is initialized |
| `SCE_LOGIN_DIALOG_STATUS_RUNNING` | 2 | Login dialog is being displayed |
| `SCE_LOGIN_DIALOG_STATUS_FINISHED` | 3 | Login dialog is closed |

## See Also

`sceLoginDialogGetStatus()`, `sceLoginDialogUpdateStatus()`

# sceLoginDialogClose

Close the login dialog

## Definition

```
#include <login_dialog.h>
int32_t sceLoginDialogClose()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81340001 | Login dialog is not initialized |
| `SCE_LOGIN_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x81340004 | Unexpected fatal error |

## Description

This function closes the login dialog.

This function can only be called while the operation status is `SCE_LOGIN_DIALOG_STATUS_INITIALIZED`, `SCE_LOGIN_DIALOG_STATUS_FINISHED` or `SCE_LOGIN_DIALOG_STATUS_RUNNING`.

The `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` error code will return when called at any other time - in other words, during `SCE_LOGIN_DIALOG_STATUS_NONE`.

When this function call is successful, the dialog will start processing to end display if the dialog was being displayed upon call of this function. The operation status will immediately transition to `SCE_LOGIN_DIALOG_STATUS_FINISHED` once processing completes. If the dialog was not being displayed upon call of this function, the function returns without doing anything and the operation status will immediately transition to `SCE_LOGIN_DIALOG_STATUS_FINISHED`.

## See Also

`sceLoginDialogOpen()`

# sceLoginDialogGetResult

Get call result of the login dialog

## Definition

```
#include <login_dialog.h>
int32_t sceLoginDialogGetResult(
	SceLoginDialogResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `result` | Destination to store the call result of the login dialog |

## Return Values

Stores the login dialog call result in `*result` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81340001 | Login dialog is not initialized |
| `SCE_LOGIN_DIALOG_ERROR_PARAM_INVALID` | 0x81340003 | Parameter is invalid |
| `SCE_LOGIN_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x81340004 | Unexpected fatal error |
| `SCE_LOGIN_DIALOG_ERROR_INVALID_STATE` | 0x81340005 | Login dialog is not closed |

## Description

This function obtains the call result of the login dialog.

The call result of the login dialog is stored in `*result`. For details on the call results, refer to `SceLoginDialogResult`.

This function can only be called while the operation status of the login dialog is `SCE_LOGIN_DIALOG_STATUS_FINISHED`. `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` or `SCE_LOGIN_DIALOG_ERROR_INVALID_STATE` will be returned when this function is called at any other time.

## See Also

`SceLoginDialogResult`, `sceLoginDialogGetStatus()`

# sceLoginDialogGetStatus

Get operation status of the login dialog

## Definition

```
#include <login_dialog.h>
SceLoginDialogStatus sceLoginDialogGetStatus()
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_STATUS_NONE` | 0 | Login dialog is not running |
| `SCE_LOGIN_DIALOG_STATUS_INITIALIZED` | 1 | Login dialog is initialized |
| `SCE_LOGIN_DIALOG_STATUS_RUNNING` | 2 | Login dialog is being displayed |
| `SCE_LOGIN_DIALOG_STATUS_FINISHED` | 3 | Login dialog is closed |

## Description

This function obtains the operation status of the login dialog.

Unlike `sceLoginDialogUpdateStatus()`, this function does not update the operation status; thus, there is no guarantee that the latest status can be obtained. Because of this, this function is lighter than `sceLoginDialogUpdateStatus()` and is useful in obtaining the operation status using a thread that is different from the one updating the status.

## See Also

`sceLoginDialogUpdateStatus()`

# sceLoginDialogOpen

Display the login dialog

## Definition

```
#include <login_dialog.h>
int32_t sceLoginDialogOpen(
	SceLoginDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the login dialog |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81340001 | Login dialog is not initialized |
| `SCE_LOGIN_DIALOG_ERROR_PARAM_INVALID` | 0x81340003 | `param` is invalid |
| `SCE_LOGIN_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x81340004 | Unexpected fatal error |
| `SCE_LOGIN_DIALOG_ERROR_INVALID_STATE` | 0x81340005 | The function is not in a callable state |
| `SCE_LOGIN_DIALOG_ERROR_SERVICE_BUSY` | 0x81340006 | Process is busy (process is being restarted, for example) |
| `SCE_LOGIN_DIALOG_ERROR_INVALID_USER_ID` | 0x81340007 | Invalid user ID was specified |

## Description

This function displays the login dialog.

The login dialog is displayed by a process on the system software. `SCE_LOGIN_DIALOG_ERROR_SERVICE_BUSY` returns when attempting to display the login dialog while that process is being restarted (for some reason). In this case, execute this function again.

This function can only be called when the operation status of the login dialog is `SCE_LOGIN_DIALOG_STATUS_INITIALIZED` or `SCE_LOGIN_DIALOG_STATUS_FINISHED`. `SCE_LOGIN_DIALOG_ERROR_NOT_INITIALIZED` or `SCE_LOGIN_DIALOG_ERROR_INVALID_STATE` will return when called at any other time.

When this function call is successful, the operation status will immediately transition to `SCE_LOGIN_DIALOG_STATUS_RUNNING`.

When this function is called, control will immediately return to the application and the application will immediately make a transition to a background state (note that this is not guaranteed to happen in a specific order). When the login dialog is closed, the application will return to the foreground state.

## See Also

`SceLoginDialogParam`

# sceLoginDialogUpdateStatus

Update operation status of the login dialog and obtain latest status

## Definition

```
#include <login_dialog.h>
SceLoginDialogStatus sceLoginDialogUpdateStatus()
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_STATUS_NONE` | 0 | Login dialog is not running |
| `SCE_LOGIN_DIALOG_STATUS_INITIALIZED` | 1 | Login dialog is initialized |
| `SCE_LOGIN_DIALOG_STATUS_RUNNING` | 2 | Login dialog is being displayed |
| `SCE_LOGIN_DIALOG_STATUS_FINISHED` | 3 | Login dialog is closed |

## Description

This function updates the operation status of the login dialog and obtains the latest status.

After dialog is opened, this function must be called at regular intervals (such as at every rendering frame) until the operation status becomes `SCE_LOGIN_DIALOG_STATUS_FINISHED`.

## See Also

`sceLoginDialogGetStatus()`