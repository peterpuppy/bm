# SigninDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SigninDialog-Reference/signin-dialog-processing.html

# Signin Dialog Processing

# SceSigninDialogResult

Signin dialog call result

## Definition

```
#include <signin_dialog.h>
typedef enum SceSigninDialogResultType {
	SCE_SIGNIN_DIALOG_RESULT_OK = 0,
	SCE_SIGNIN_DIALOG_RESULT_USER_CANCELED    = 1,
} SceSigninDialogResultType;

typedef struct SceSigninDialogResult {
	SceSigninDialogResultType result;
	int32_t reserved[3];
} SceSigninDialogResult;
```

## Members

|  |  |
| --- | --- |
| `result` | Signin dialog call result |
| `reserved` | Reserved area |

## Description

This structure obtains the signin dialog call result with `sceSigninDialogGetResult()`.

In `result`, the signin dialog call result will be stored. When the call result obtaining terminates normally, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_RESULT_OK` | 0 | Signin dialog terminated normally |
| `SCE_SIGNIN_DIALOG_RESULT_USER_CANCELED` | 1 | Signin dialog was cancelled by user operation |

`reserved` is a reserved area.

## See Also

`sceSigninDialogGetResult()`

# SceSigninDialogStatus

enum constant representing the signin dialog status

## Definition

```
#include <signin_dialog.h>
typedef enum SceSigninDialogStatus;
```

## Description

This enum constant represents the status of the signin dialog. It can be obtained with `sceSigninDialogUpdateStatus()` or `sceSigninDialogGetStatus()`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_STATUS_NONE` | 0 | Signin dialog is not running |
| `SCE_SIGNIN_DIALOG_STATUS_INITIALIZED` | 1 | Signin dialog is initialized |
| `SCE_SIGNIN_DIALOG_STATUS_RUNNING` | 2 | Signin dialog is being displayed |
| `SCE_SIGNIN_DIALOG_STATUS_FINISHED` | 3 | Signin dialog is closed |

## See Also

`sceSigninDialogGetStatus()`, `sceSigninDialogUpdateStatus()`

# sceSigninDialogClose

Close the signin dialog

## Definition

```
#include <signin_dialog.h>
int32_t sceSigninDialogClose()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81350001 | Signin dialog is not initialized |
| `SCE_SIGNIN_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x81350004 | Unexpected fatal error |

## Description

This function closes the signin dialog.

This function can only be called while the operation status is `SCE_SIGNIN_DIALOG_STATUS_INITIALIZED`, `SCE_SIGNIN_DIALOG_STATUS_FINISHED` or `SCE_SIGNIN_DIALOG_STATUS_RUNNING`.

`SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` error code will return when called at any other time - in other words, during `SCE_SIGNIN_DIALOG_STATUS_NONE`.

When this function call is successful, the dialog will start processing to end display if the dialog was being displayed upon call of this function. The operation status will immediately transition to `SCE_SIGNIN_DIALOG_STATUS_FINISHED` once processing completes. If the dialog was not being displayed upon call of this function, the function returns without doing anything and the operation status will immediately transition to `SCE_SIGNIN_DIALOG_STATUS_FINISHED`.

## See Also

`sceSigninDialogOpen()`

# sceSigninDialogGetResult

Get call result of the signin dialog

## Definition

```
#include <signin_dialog.h>
int32_t sceSigninDialogGetResult(
	SceSigninDialogResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `result` | Destination to store the call result of the signin dialog |

## Return Values

Stores the signin dialog call result in `*result` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81350001 | Signin dialog is not initialized |
| `SCE_SIGNIN_DIALOG_ERROR_PARAM_INVALID` | 0x81350003 | Parameter is invalid |
| `SCE_SIGNIN_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x81350004 | Unexpected fatal error |
| `SCE_SIGNIN_DIALOG_ERROR_INVALID_STATE` | 0x81350005 | Signin dialog is not closed |

## Description

This function obtains the call result of the signin dialog.

The call result of signin dialog is stored in `*result`. For details on the call results, refer to `SceSigninDialogResult`.

This function can only be called while the operation status of the signin dialog is `SCE_SIGNIN_DIALOG_STATUS_FINISHED`. `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` or `SCE_SIGNIN_DIALOG_ERROR_INVALID_STATE` will return when called at any other time.

## See Also

`SceSigninDialogResult`, `sceSigninDialogGetStatus()`

# sceSigninDialogGetStatus

Get operation status of the signin dialog

## Definition

```
#include <signin_dialog.h>
SceSigninDialogStatus sceSigninDialogGetStatus()
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_STATUS_NONE` | 0 | Signin dialog is not running |
| `SCE_SIGNIN_DIALOG_STATUS_INITIALIZED` | 1 | Signin dialog is initialized |
| `SCE_SIGNIN_DIALOG_STATUS_RUNNING` | 2 | Signin dialog is being displayed |
| `SCE_SIGNIN_DIALOG_STATUS_FINISHED` | 3 | Signin dialog is closed |

## Description

This function obtains the operation status of the signin dialog.

Unlike `sceSigninDialogUpdateStatus()`, this function does not update the operation status; thus, there is no guarantee that the latest status can be obtained. Because of this, this function is lighter than `sceSigninDialogUpdateStatus()` and is useful in obtaining the operation status using a thread that is different from the one updating the status.

## See Also

`sceSigninDialogUpdateStatus()`

# sceSigninDialogOpen

Display the signin dialog

## Definition

```
#include <signin_dialog.h>
int32_t sceSigninDialogOpen(
	SceSigninDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the signin dialog |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` | 0x81350001 | Signin dialog is not initialized |
| `SCE_SIGNIN_DIALOG_ERROR_PARAM_INVALID` | 0x81350003 | `param` is invalid |
| `SCE_SIGNIN_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x81350004 | Unexpected fatal error |
| `SCE_SIGNIN_DIALOG_ERROR_INVALID_STATE` | 0x81350005 | The API is not in a callable state |
| `SCE_SIGNIN_DIALOG_ERROR_SERVICE_BUSY` | 0x81350006 | Process is busy (process is being restarted, for example) |
| `SCE_SIGNIN_DIALOG_ERROR_INVALID_USER_ID` | 0x81350007 | Invalid user ID was specified |

## Description

This function displays the signin dialog.

The signin dialog is displayed by a process on the system software. `SCE_SIGNIN_DIALOG_ERROR_SERVICE_BUSY` returns when attempting to display the signin dialog while that process is being restarted (for some reason). In this case, execute this function again.

This function can only be called when the operation status is `SCE_SIGNIN_DIALOG_STATUS_INITIALIZED` or `SCE_SIGNIN_DIALOG_STATUS_FINISHED`. `SCE_SIGNIN_DIALOG_ERROR_NOT_INITIALIZED` or `SCE_SIGNIN_DIALOG_ERROR_INVALID_STATE` will return when called at any other time.

When this function call is successful, the operation status will immediately transition to `SCE_SIGNIN_DIALOG_STATUS_RUNNING`.

When this function is called, control will immediately return to the application and the application will immediately make a transition to a background state (note that this is not guaranteed to happen in a specific order). When the signin dialog is closed, the application will return to the foreground state.

## See Also

`SceSigninDialogParam`

# sceSigninDialogUpdateStatus

Update operation status of the signin dialog and obtain latest status

## Definition

```
#include <signin_dialog.h>
SceSigninDialogStatus sceSigninDialogUpdateStatus()
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SIGNIN_DIALOG_STATUS_NONE` | 0 | Signin dialog is not running |
| `SCE_SIGNIN_DIALOG_STATUS_INITIALIZED` | 1 | Signin dialog is initialized |
| `SCE_SIGNIN_DIALOG_STATUS_RUNNING` | 2 | Signin dialog is being displayed |
| `SCE_SIGNIN_DIALOG_STATUS_FINISHED` | 3 | Signin dialog is closed |

## Description

This function updates the operation status of the signin dialog and obtains the latest status.

After opening dialog, be sure to call this function at regular intervals (such as at every rendering frame) until the operation status becomes `SCE_SIGNIN_DIALOG_STATUS_FINISHED`.

## See Also

`sceSigninDialogGetStatus()`