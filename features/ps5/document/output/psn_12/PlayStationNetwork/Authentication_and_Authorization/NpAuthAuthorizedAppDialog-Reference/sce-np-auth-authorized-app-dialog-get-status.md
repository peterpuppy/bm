# NpAuthAuthorizedAppDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuthAuthorizedAppDialog-Reference/sce-np-auth-authorized-app-dialog-get-status.html

# NpAuth Authorized App Dialog Operations

# sceNpAuthAuthorizedAppDialogOpen

Display the NpAuth Authorized App dialog

## Definition

```
#include <np_auth_authorized_app_dialog.h>
int32_t sceNpAuthAuthorizedAppDialogOpen(
    const SceNpAuthAuthorizedAppDialogParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | NpAuth Authorized App dialog parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | The NpAuth Authorized App dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_INVALID_STATE` | 0x80B80006 | Not an operational status in which the function can be called |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | 0x80B80009 | Memory is insufficient |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | 0x80B8000A | `param` content is invalid |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | 0x80B8000D | `param` is NULL |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error has occurred |
| `SCE_COMMON_DIALOG_ERROR_INHIBIT_SHAREPLAY_CLIENT` | 0x80B80010 | While using the "Playing together with host" feature, attempted to display an NpAuth Authorized App dialog for which display to a visitor is not authorized. |

## Description

This function displays the NpAuth Authorized App dialog.

For `*param`, specify an NpAuth Authorized App dialog parameter structure. After initializing in advance with `sceNpAuthAuthorizedAppDialogParamInit()`, set necessary parameters such as the user ID. If the content of `param` is invalid, this function returns `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID`, and the operational status does not change.

This function can be called only when the NpAuth Authorized App dialog operational status is either `SCE_COMMON_DIALOG_STATUS_INITIALIZED` or `SCE_COMMON_DIALOG_STATUS_FINISHED`. Calls made during any other period return `SCE_COMMON_DIALOG_ERROR_INVALID_STATE`.

If successfully called, the operational status immediately transitions to `SCE_COMMON_DIALOG_STATUS_RUNNING`.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.

## Example

```
SceNpAuthAuthorizedAppDialogParam param;
sceNpAuthAuthorizedAppDialogParamInit( &param );

param.userId = user_id;
param.authorizedAppClientId = &authorized_app_client_id;
param.scope = scope;
param.accessType = SCE_NP_AUTH_ACCESS_TYPE_OFFLINE;

if ( sceNpAuthAuthorizedAppDialogOpen( &param ) < 0) {
    // Error handling
}
```

# sceNpAuthAuthorizedAppDialogUpdateStatus

Update and obtain the NpAuth Authorized App dialog operational status

## Definition

```
#include <np_auth_authorized_app_dialog.h>
SceCommonDialogStatus sceNpAuthAuthorizedAppDialogUpdateStatus(void);
```

## Arguments

None

## Return Values

Returns one of the following operational statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | 0 | The NpAuth Authorized App dialog is not running |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | 1 | The NpAuth Authorized App dialog is initialized |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | 2 | The NpAuth Authorized App dialog is being displayed |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | 3 | The NpAuth Authorized App dialog is closed |

## Description

This function updates the NpAuth Authorized App dialog operational status and obtains the latest state. After opening the dialog, ensure that you call this function at a regular interval (for example, per rendered frame) until the operational status is `SCE_COMMON_DIALOG_STATUS_FINISHED`.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.

## See Also

`sceNpAuthAuthorizedAppDialogGetStatus()`

# sceNpAuthAuthorizedAppDialogGetStatus

Obtain the NpAuth Authorized App dialog operational status

## Definition

```
#include <np_auth_authorized_app_dialog.h>
SceCommonDialogStatus sceNpAuthAuthorizedAppDialogGetStatus(void);
```

## Arguments

None

## Return Values

Returns one of the following operational statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | 0 | The NpAuth Authorized App dialog is not running |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | 1 | The NpAuth Authorized App dialog is initialized |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | 2 | The NpAuth Authorized App dialog is being displayed |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | 3 | The NpAuth Authorized App dialog is closed |

## Description

This function obtains the NpAuth Authorized App dialog operational status.

This function is more lightweight than `sceNpAuthAuthorizedAppDialogUpdateStatus()`. This is useful when obtaining the status with a thread other than the thread updating the operational status.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.

# SceNpAuthAuthorizedAppDialogResult

NpAuth Authorized App dialog call results

## Definition

```
#include <np_auth_authorized_app_dialog.h>
typedef struct SceNpAuthAuthorizedAppDialogResult {
    int32_t result;
    int : 32;
    uint8_t reserved[32];
} SceNpAuthAuthorizedAppDialogResult;
```

## Members

|  |  |
| --- | --- |
| `result` | NpAuth Authorized App dialog call results |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is for obtaining NpAuth Authorized App dialog call results with `sceNpAuthAuthorizedAppDialogGetResult()`.

NpAuth Authorized App dialog call results are stored in `result`. Stores one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_RESULT_OK` | 0 | Closed with `sceNpAuthAuthorizedAppDialogClose()` |
| `SCE_COMMON_DIALOG_RESULT_USER_CANCELED` | 1 | Canceled by user |
| `SCE_NP_AUTH_AUTHORIZED_APP_DIALOG_RESULT_CONSENTED` | 2 | User agrees |

Stores an error code (a negative value) for an error.

When call results are `SCE_NP_AUTH_AUTHORIZED_APP_DIALOG_RESULT_CONSENTED`, the authorization code for the target user can be obtained with `sceNpAuthGetAuthorizedAppCode()`.

# sceNpAuthAuthorizedAppDialogGetResult

Obtain NpAuth Authorized App dialog call results

## Definition

```
#include <np_auth_authorized_app_dialog.h>
int32_t sceNpAuthAuthorizedAppDialogGetResult(
    SceNpAuthAuthorizedAppDialogResult *result
);
```

## Arguments

|  |  |
| --- | --- |
| `result` | NpAuth Authorized App dialog call results |

## Return Values

Stores the NpAuth Authorized App dialog call result in `*result` and returns the value of `(*result).result` for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | The NpAuth Authorized App dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED` | 0x80B80005 | The NpAuth Authorized App dialog is not closed |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | 0x80B8000D | `result` is NULL |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error has occurred |

## Description

This function obtains NpAuth Authorized App dialog call results.

NpAuth Authorized App dialog call results are stored in `*result`. For details about call results, refer to `SceNpAuthAuthorizedAppDialogResult`.

This function can be called only when the NpAuth Authorized App dialog operational status is `SCE_COMMON_DIALOG_STATUS_FINISHED`. Calls made during any other period return `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` or `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED`.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.

# sceNpAuthAuthorizedAppDialogClose

Close the NpAuth Authorized App dialog

## Definition

```
#include <np_auth_authorized_app_dialog.h>
int32_t sceNpAuthAuthorizedAppDialogClose(void);
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | The NpAuth Authorized App dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING` | 0x80B8000B | NpAuth Authorized App dialog is not being displayed |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_CLOSE` | 0x80B8000C | The NpAuth Authorized App dialog is already closed |

## Description

This function closes the NpAuth Authorized App dialog.

This can be called only when the NpAuth Authorized App dialog operational status is `SCE_COMMON_DIALOG_STATUS_RUNNING`. Calls made during any other period return `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING`.

By periodically calling `sceNpAuthAuthorizedAppDialogUpdateStatus()` after a successful call to this function, the dialog performs processing to terminate the displaying of itself, and the operational status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED` when the processing is complete.

For the details of operational statuses, refer to the description in `SceCommonDialogStatus`.

If you use this function to close the NpAuthAuthorizedApp dialog, the result of the dialog call obtained with `sceNpAuthAuthorizedAppDialogGetResult()` is `SCE_COMMON_DIALOG_RESULT_OK`.