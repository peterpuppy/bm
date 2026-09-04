# PlayerSelectionDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerSelectionDialog-Reference/sce-player-selection-dialog-result.html

# Player Selection Dialog Operation

# ScePlayerSelectionDialogResult

Result of calling the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
typedef struct ScePlayerSelectionDialogResult {
    int32_t result;
    SceCommonDialogResult userAction;
    SceNpAccountId *playerList;
    uint32_t playerListLength;
    uint8_t reserved[32];
} ScePlayerSelectionDialogResult;
```

## Members

|  |  |
| --- | --- |
| `result` | Termination state of the player selection dialog |
| `userAction` | Result of calling the player selection dialog |
| `playerList` | Account ID list of the selected player |
| `playerListLength` | Number of players selected (number of valid elements in `playerList`) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used for obtaining the result of calling the player selection dialog with `scePlayerSelectionDialogGetResult()`.

Initialize this structure in advance filling all values with 0's and set values to the required members before use.

`result` indicates the termination state of the player selection dialog. `SCE_OK` (=0) will be stored for normal termination; a non-zero value will be stored for a fatal error.

`userAction` indicates the result of calling the player selection dialog. One of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_RESULT_OK` | 0 | Closed by user operation or `scePlayerSelectionDialogClose()` |
| `SCE_COMMON_DIALOG_RESULT_USER_CANCELED` | 1 | Canceled by the user |

If player selection succeeded, an array of the account IDs of the players the user selected is stored in `playerList`.

This array must be allocated and specified on the calling end beforehand. Be sure that the size of the array matches the maximum number of players specified with `ScePlayerSelectionDialogParam``::maxSelectable` when `scePlayerSelectionDialogOpen()` is called.

`reserved` is a reserved area. It must be filled with all 0's.

## See Also

`scePlayerSelectionDialogGetResult()`

# scePlayerSelectionDialogOpen

Display the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
int32_t scePlayerSelectionDialogOpen(
    const ScePlayerSelectionDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the player selection dialog |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player selection dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_INVALID_STATE` | 0x80B80006 | The function is not in a callable state |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | 0x80B80009 | Insufficient memory |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | 0x80B8000A | `param` is invalid |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | 0x80B8000D | `param` is NULL |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error occurred |
| `SCE_COMMON_DIALOG_ERROR_INHIBIT_SHAREPLAY_CLIENT` | 0x80B80010 | Display of player selection dialog not permitted for display to visitors during usage of the "Playing Game with Host" feature was attempted |

## Description

This function displays the player selection dialog.

For `*param`, specify the parameter structure for the player selection dialog. Initialize this structure in advance using `scePlayerSelectionDialogParamInitialize()` and set user IDs and other required parameters.

If the content of `param` is invalid, `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` will be returned. When this happens, there will be no change in operation status.

It can only be called when the player selection dialog operation status is `SCE_COMMON_DIALOG_STATUS_INITIALIZED` or `SCE_COMMON_DIALOG_STATUS_FINISHED`. If it is called at times other than the above, `SCE_COMMON_DIALOG_ERROR_INVALID_STATE` is returned.

When the call is successful, the operation status will immediately switch to `SCE_COMMON_DIALOG_STATUS_RUNNING`.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## Examples

If Not Setting the Initial Status of Players

```
ScePlayerSelectionDialogParam param;

scePlayerSelectionDialogParamInitialize( &param );
param.userId = user_id;

if (scePlayerSelectionDialogOpen ( &param ) < 0 ) {
    // Error handling
}
```

If Setting the Initial Status of Players (One Player Pre-Selected and One Player Non-Modifiable)

```
ScePlayerSelectionDialogParam param;

scePlayerSelectionDialogParamInitialize( &param );
param.userId = user_id;

ScePlayerSelectionDialogInitialPlayerStatus playerStatusList[2];
memset(&playerStatusList, 0, sizeof(playerStatusList));
param.initialPlayerStatusList = playerStatusList
param.initialPlayerStatusListLength = 2;

playersStatusList[0].accountId = selectedUserAccountId;
playersStatusList[0].selectStatus = SCE_PLAYER_SELECTION_DIALOG_PLAYER_SELECT_STATUS_SELECTED;

playersStatusList[1].accountId = disabledUserAccountId;
playersStatusList[1].selectStatus = SCE_PLAYER_SELECTION_DIALOG_PLAYER_ENABLE_STATUS_DISABLE;
playersStatusList[1].label = SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_CANT_SELECT;

if (scePlayerSelectionDialogOpen ( &param ) < 0 ) {
    // Error handling
}
```

## See Also

`ScePlayerSelectionDialogParam`, `scePlayerSelectionDialogParamInitialize()`

# scePlayerSelectionDialogGetStatus

Get operation status of the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
SceCommonDialogStatus scePlayerSelectionDialogGetStatus(void)
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | 0 | Player selection dialog is not running |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | 1 | Player selection dialog is initialized |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | 2 | Player selection dialog is being displayed |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | 3 | Player selection dialog is closed |

## Description

This function obtains the operation status of the player selection dialog. This function entails a lighter load than `scePlayerSelectionDialogUpdateStatus()`. This function is useful; for example, in obtaining the operation status from a thread that is different from the thread to update the status.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`scePlayerSelectionDialogUpdateStatus()`

# scePlayerSelectionDialogUpdateStatus

Update and get operation status of the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
SceCommonDialogStatus scePlayerSelectionDialogUpdateStatus(void)
```

## Arguments

None

## Return Values

Returns one of the following operation statuses.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_STATUS_NONE` | 0 | Player selection dialog is not running |
| `SCE_COMMON_DIALOG_STATUS_INITIALIZED` | 1 | Player selection dialog is initialized |
| `SCE_COMMON_DIALOG_STATUS_RUNNING` | 2 | Player selection dialog is being displayed |
| `SCE_COMMON_DIALOG_STATUS_FINISHED` | 3 | Player selection dialog is closed |

## Description

This function updates the player selection dialog operation status and obtaining the latest status. After opening dialog, be sure to call this function at regular intervals (such as at every rendering frame) until the operation status becomes `SCE_COMMON_DIALOG_STATUS_FINISHED`.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## See Also

`scePlayerSelectionDialogGetStatus()`

# scePlayerSelectionDialogClose

Close the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
int32_t scePlayerSelectionDialogClose(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player selection dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING` | 0x80B8000B | Player selection dialog is not being displayed |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_CLOSE` | 0x80B8000C | Player selection dialog is already closed |

## Description

This function closes the player selection dialog.

This function can be called only while the operation status of the player selection dialog is `SCE_COMMON_DIALOG_STATUS_RUNNING`. If this function is called at times other than the above, `SCE_COMMON_DIALOG_ERROR_NOT_RUNNING` is returned.

When the call of this function succeeds and `scePlayerSelectionDialogUpdateStatus()` is periodically called thereafter, the dialog will carry out processing to close the dialog display; the operation status will transition to `SCE_COMMON_DIALOG_STATUS_FINISHED` upon processing completion.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

When the player selection dialog is closed with this function, the dialog call result that can be obtained with `scePlayerSelectionDialogGetResult()` is `SCE_COMMON_DIALOG_RESULT_OK`.

## See Also

`scePlayerSelectionDialogUpdateStatus()`, `scePlayerSelectionDialogGetResult()`

# scePlayerSelectionDialogGetResult

Get result of calling the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
int32_t scePlayerSelectionDialogGetResult(
    ScePlayerSelectionDialogResult *resultParam
)
```

## Arguments

|  |  |
| --- | --- |
| `resultParam` | Result of calling the player selection dialog |

## Return Values

Stores the result of calling the player selection dialog in `*resultParam` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | 0x80B80003 | Player selection dialog is not initialized |
| `SCE_COMMON_DIALOG_ERROR_NOT_FINISHED` | 0x80B80005 | Player selection dialog is not closed |
| `SCE_COMMON_DIALOG_ERROR_RESULT_NONE` | 0x80B80007 | The common dialog result does not exist |
| `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` | 0x80B8000A | `resultParam` is invalid |
| `SCE_COMMON_DIALOG_ERROR_ARG_NULL` | 0x80B8000D | `resultParam` is NULL |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | 0x80B8000E | Unexpected fatal error occurred |

## Description

This function obtains the result of calling the player selection dialog.

The call result of the player selection dialog is stored in `*resultParam`. For details on the call results, refer to `ScePlayerSelectionDialogResult`.

Fill all values in `*resultParam` with 0's before using this function. If `*resultParam` is not filled with 0's when this function is called, `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` will be returned.

This function can be called only while the operation status of the player selection dialog is `SCE_COMMON_DIALOG_STATUS_FINISHED`. If it is called at times other than the above, an error is returned.

For details on the operation status, refer the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document.

## Examples

```
int32_t maxNum = 256; // Number specified with ScePlayerSelectionDialogParam::maxSelectable
ScePlayerSelectionDialogResult result;
memset( &result, 0x0, sizeof(ScePlayerSelectionDialogResult) );

// Allocate memory for obtaining player information list
result.playerList= new SceNpAccountId[ maxNum ];

ret = scePlayerSelectionDialogGetResult( &result );
if (ret < 0) {
    // Error handling
    delete[] result.playerList;
    return;
}

// Processing for selected players
printf("%u player(s) selected\n", result.playerListLength);

for (uint32_t i = 0; i < result.playerListLength; ++i) {
  printf("[%u] %lu", i, result.playerList[i]);
}

delete [] result.playerList;
```

## See Also

`ScePlayerSelectionDialogResult`