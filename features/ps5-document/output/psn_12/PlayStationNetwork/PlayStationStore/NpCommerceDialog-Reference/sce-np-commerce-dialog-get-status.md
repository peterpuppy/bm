# NpCommerceDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCommerceDialog-Reference/sce-np-commerce-dialog-get-status.html

# NP Commerce Dialog Operation

# sceNpCommerceDialogClose

Closes the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
int32_t sceNpCommerceDialogClose()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Error Code** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | NP commerce dialog is not initialized. |
| `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING` | NP commerce dialog is not being displayed. |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_CLOSE` | NP commerce dialog is already closed. |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | Unexpected fatal error occurred. |

## Description

This function closes the NP commerce dialog.

Use this function to close the dialog by the application without user operation.

This function can only be called while the operation status of the NP commerce dialog is`SCE_COMMON_DIALOG_STATUS_RUNNING`. When called at any other time, `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED`, `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING`, or `SCE_COMMON_DIALOG_ERROR_ALREADY_CLOSE` returns according to the status of the dialog.

When the call of this function succeeds and [sceNpCommerceDialogUpdateStatus()](sce-np-commerce-dialog-update-status.html "Updates and gets operation status of the NP commerce dialog.") is periodically called thereafter, the dialog carries out processing to close the dialog display; the operation status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED` upon processing completion.

For details on the operation status, see the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

When the NP commerce dialog is closed with this function, the call result that can be obtained with [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog.") is `SCE_COMMON_DIALOG_RESULT_OK`.

## See Also

[sceNpCommerceDialogOpen()](sce-np-commerce-dialog-open.html "Displays the NP commerce dialog."), [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog."), [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog.")

# sceNpCommerceDialogGetResult

Gets result of calling the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
int32_t sceNpCommerceDialogGetResult(
    SceNpCommerceDialogResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `result` | Area to store result of calling the NP commerce dialog. |

## Return Values

Stores the result of calling the NP commerce dialog in `*result` and returns the setting value of `*result.result` for normal termination.

Returns one of the following codes (a positive value) for normal termination.

| **Code** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_RESULT_OK` | Closed by [sceNpCommerceDialogClose()](sce-np-commerce-dialog-close.html "Closes the NP commerce dialog."). |
| `SCE_COMMON_DIALOG_RESULT_USER_CANCELED` | NP commerce dialog was canceled and terminated due to user operation without making product purchase or promotion code redemption. |
| `SCE_NP_COMMERCE_DIALOG_RESULT_PURCHASED` | NP commerce dialog performed product purchase (including free/$0 products) or promotion code redemption and terminated. |

Returns one of the following error codes (a negative value) for errors.

| **Error Code** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | NP commerce dialog is not initialized. |
| `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED` | NP commerce dialog is not closed. |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | `result` is NULL. |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | Unexpected fatal error occurred. |

## Description

This function obtains the result of calling the NP commerce dialog.

The result of calling the dialog is stored in \*`result`.

For details on call results, see [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.").

This function can only be called while the operation status of the NP commerce dialog is`SCE_COMMON_DIALOG_STATUS_FINISHED`. When called at any other time, `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` or `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED` returns according to the status of the dialog.

For details on the operation status, see the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## See Also

[SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.")

# sceNpCommerceDialogGetStatus

Gets operation status of the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
SceCommonDialogStatussceNpCommerceDialogGetStatus()
```

## Arguments

None

## Return Values

Returns one of the following operation statuses as the value of the function.

| **Operation Status** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | NP commerce dialog is not running. |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | NP commerce dialog is initialized. |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | NP commerce dialog is being displayed. |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | NP commerce dialog is closed. |

## Description

This function obtains the operation status of the NP commerce dialog.

This function entails a lighter load than [sceNpCommerceDialogUpdateStatus()](sce-np-commerce-dialog-update-status.html "Updates and gets operation status of the NP commerce dialog."). This function is useful in obtaining the operation status from a thread that is different from the thread to update the status.

For details on the operation status, see the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## Examples

```
SceCommonDialogStatus stat = sceNpCommerceDialogGetStatus();
```

## See Also

[sceNpCommerceDialogUpdateStatus()](sce-np-commerce-dialog-update-status.html "Updates and gets operation status of the NP commerce dialog.")

# sceNpCommerceDialogOpen2

Displays the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
int32_t sceNpCommerceDialogOpen2 (
    const SceNpCommerceDialogParam2 *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the NP commerce dialog. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors:

| **Error Code** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | NP commerce dialog is not initialized. |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | `param` is invalid. |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | `param` is NULL. |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | Unexpected fatal error occurred. |
| `SCE_COMMON_DIALOG_ERROR_INHIBIT_SHAREPLAY_CLIENT` | Display of NP commerce dialog not permitted for display to visitors during usage of the "Playing Game with Host" feature was attempted. |

## Description

This function displays the NP commerce dialog.

Set \*`param` as the parameter structure of the NP commerce dialog. Initialized the structure using [sceNpCommerceDialogParamInitialize2()](sce-np-commerce-dialog-param-initialize2.html "Initializes parameters for the NP commerce dialog.") before setting required parameters, such as the dialog display mode and user ID. This function returns `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` if the content of the parameter structure is invalid and the operation status immediately transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED`.

The `param` entity does not have to remain allocated after returning from this function.

This function can only be called while the operation status of the NP commerce dialog is `SCE_COMMON_DIALOG_STATUS_INITIALIZED` or `SCE_COMMON_DIALOG_STATUS_FINISHED`.

When this function call is successful, the operation status immediately transitions to `SCE_COMMON_DIALOG_STATUS_RUNNING`.

For details on the operation status, see [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## See Also

[SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters."), [sceNpCommerceDialogParamInitialize2()](sce-np-commerce-dialog-param-initialize2.html "Initializes parameters for the NP commerce dialog.")

# sceNpCommerceDialogOpen

Displays the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
int32_t sceNpCommerceDialogOpen (
    const SceNpCommerceDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the NP commerce dialog. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Error Code** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | NP commerce dialog is not initialized. |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | `param` is invalid. |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | `param` is NULL. |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | Unexpected fatal error occurred. |
| `SCE_COMMON_DIALOG_ERROR_INHIBIT_SHAREPLAY_CLIENT` | Display of NP commerce dialog not permitted for display to visitors during usage of the "Playing Game with Host" feature was attempted. |

## Description

This function displays the NP commerce dialog.

For `*param`, specify the parameter structure of the NP commerce dialog. Have the structure initialized in advance with [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog.") and required parameters - such as, the dialog display mode and user ID - set before use. This function returns `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` if the content of the parameter structure is invalid and the operation status immediately transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED`.

The `param` entity does not have to remain allocated after returning from this function.

This function can only be called while the operation status of the NP commerce dialog is `SCE_COMMON_DIALOG_STATUS_INITIALIZED` or `SCE_COMMON_DIALOG_STATUS_FINISHED`.

When this function call is successful, the operation status immediately transitions to `SCE_COMMON_DIALOG_STATUS_RUNNING`.

For details on the operation status, see [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## See Also

[SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters."), [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog.")

# sceNpCommerceDialogUpdateStatus

Updates and gets operation status of the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
SceCommonDialogStatussceNpCommerceDialogUpdateStatus()
```

## Return Values

Returns one of the following operation statuses as the value of the function.

| **Operation Status** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | NP commerce dialog is not running. |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | NP commerce dialog is initialized. |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | NP commerce dialog is being displayed. |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | NP commerce dialog is closed. |

## Description

This function updates the NP commerce dialog operation status and obtaining the latest status. After opening dialog, be sure to call this function at regular intervals (such as at every rendering frame) until the operation status becomes `SCE_COMMON_DIALOG_STATUS_FINISHED`.

For details on the operation status, see the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## Examples

```
SceCommonDialogStatus stat = sceNpCommerceDialogUpdateStatus();
```

## See Also

[sceNpCommerceDialogGetStatus()](sce-np-commerce-dialog-get-status.html "Gets operation status of the NP commerce dialog.")

# SceNpCommerceDialogResult

Result of calling the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
typedef struct SceNpCommerceDialogResult {
    int32_t result;
    bool authorized;
    char : 8;
    short : 16;
    void *userData;
    uint8_t reserved[32]
} SceNpCommerceDialogResult;
```

## Members

|  |  |
| --- | --- |
| `result` | Result of calling the NP commerce dialog. |
| `authorized` | Whether or not the specified premium features can be used. |
| `userData` | Application defined argument specified upon calling the NP commerce dialog. |
| `reserved` | Reserved area. |

## Description

This parameter structure is used for obtaining the result of calling the NP commerce dialog with [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog.").

The result of calling the dialog is stored in `result`. If obtainment of the call result terminates normally, one of the following values is stored.

| **Value** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_RESULT_OK` | Closed by [sceNpCommerceDialogClose()](sce-np-commerce-dialog-close.html "Closes the NP commerce dialog."). |
| `SCE_COMMON_DIALOG_RESULT_USER_CANCELED` | NP commerce dialog was canceled and terminated due to user operation without making product purchase or promotion code redemption. |
| `SCE_NP_COMMERCE_DIALOG_RESULT_PURCHASED` | NP commerce dialog performed product purchase (including free/$0 products) or promotion code redemption and terminated. |

The following error code (negative value) is returned for an error.

| **Error Code** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | Parameter is invalid. |

`authorized` is true when all premium features specified in `features` of [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.") or [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.") are usable, and false in all other cases. This value is only valid when the NP commerce dialog is displayed in the Join Premium mode.

For `userData`, the value of the `userData` member of the `param` argument specified upon calling [sceNpCommerceDialogOpen()](sce-np-commerce-dialog-open.html "Displays the NP commerce dialog.") or [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog.") is directly stored. This member can be used by the application for an arbitrary purpose.

## See Also

[sceNpCommerceDialogInitialize()](sce-np-commerce-dialog-initialize.html "Initializes the NP commerce dialog."), [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog."), [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters."), [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.")