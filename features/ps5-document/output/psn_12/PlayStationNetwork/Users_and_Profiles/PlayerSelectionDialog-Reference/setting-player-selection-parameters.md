# PlayerSelectionDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerSelectionDialog-Reference/setting-player-selection-parameters.html

# Setting Player Selection Parameters

# ScePlayerSelectionDialogParam

Parameters for the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
#define SCE_PLAYER_SELECTION_DIALOG_MAX_TITLE_SIZE (64)
typedef enum ScePlayerSelectionDialogBehaviorOption {
    (Omitted: see details below)
} ScePlayerSelectionDialogBehaviorOption;

typedef struct ScePlayerSelectionDialogParam {
    SceCommonDialogBaseParam baseParam;
    size_t size;
    SceUserServiceUserId userId;
    char dialogTitle[SCE_PLAYER_SELECTION_DIALOG_MAX_TITLE_SIZE];
    uint32_t maxSelectable;
    ScePlayerSelectionDialogBehaviorOption behaviorOptions;
    const ScePlayerSelectionDialogInitialPlayerStatus *initialPlayerStatusList;
    uint32_t initialPlayerStatusListLength;
    uint8_t reserved[64];
} ScePlayerSelectionDialogParam;
```

## Members

|  |  |
| --- | --- |
| `baseParam` | Common dialog base parameters |
| `size` | Size of the structure |
| `userId` | User ID of the user making selections |
| `dialogTitle` | Title text for the player selection dialog (UTF-8, NULL-terminated) |
| `maxSelectable` | Number of players who can be selected with the selection dialog |
| `behaviorOptions` | Selection options |
| `initialPlayerStatusList` | List of initial statuses for each player, or NULL |
| `initialPlayerStatusListLength` | Number of elements in `initialPlayerStatusList` |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used for specifying dialog parameters when displaying the player selection dialog with `scePlayerSelectionDialogOpen()`. Initialize this structure in advance using `scePlayerSelectionDialogParamInitialize()` and set values to the required members before use.

The common dialog base parameters are specified for `baseParam` and the size of the structure is specified for `size`, but appropriate values will be automatically stored in these members by initializing with `scePlayerSelectionDialogParamInitialize()`; therefore, they do not need to be explicitly specified in the program.

For `dialogTitle`, specify the text to display at the upper section of the dialog. If there is no specification or an empty string is specified, a system-provided text encouraging the user to select a player will be displayed.

For `userId`, specify the user ID of the user who will be selecting players. The user ID can be obtained by using an API of the UserService library, for example.

For `behaviorOptions`, specify behavior options for the player selection dialog. Do so by specifying the bitwise OR of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_BEHAVIOR_OPTION_NONE` | 0x00000000 | None (default) |
| `SCE_PLAYER_SELECTION_DIALOG_BEHAVIOR_OPTION_DISABLE_BLOCKED_PLAYER` | 0x00000001 | Makes players on the user's blocklist incapable of being selected |
| `SCE_PLAYER_SELECTION_DIALOG_BEHAVIOR_OPTION_ENABLE_DONE_BUTTON_WHEN_NO_ONE_SELECTED` | 0x00000002 | Enables the "Done" button when nobody is selected |

For `maxSelectable`, specify the maximum number of users capable of being selected. You can specify a numerical value of up to 256 (`SCE_PLAYER_SELECTION_DIALOG_MAX_SELECTABLE_SIZE`). When the structure is initialized with `scePlayerSelectionDialogParamInitialize()`, 256 is automatically set.

With `initialPlayerStatusList`, you can specify the initial status of the list, such as in cases in which you would like certain players to be pre-selected as their initial statuses. If there is no need to do something of this nature, specify NULL. For details, refer to `ScePlayerSelectionDialogInitialPlayerStatus`. Specify the number of valid elements in the `initialPlayerStatusList` array with `initialPlayerStatusListLength`. A value of up to 256 (`SCE_PLAYER_SELECTION_DIALOG_MAX_PLAYER_LIST_SIZE`) can be specified.

`reserved` is a reserved area. This area must be filled with all 0's, but it will be automatically filled with 0's by initializing with `scePlayerSelectionDialogParamInitialize()`.

## See Also

`scePlayerSelectionDialogOpen()`, `scePlayerSelectionDialogParamInitialize()`

# scePlayerSelectionDialogParamInitialize

Initialize parameters for the player selection dialog

## Definition

```
#include <player_selection_dialog.h>
void scePlayerSelectionDialogParamInitialize(
    ScePlayerSelectionDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters to initialize |

## Return Values

None

## Description

This function initializes the parameters for the player selection dialog.

Before setting the various parameters, make sure to initialize the structure with this function. Appropriate default values will be set to each member of `*param` by calling this function; the application is not required to explicitly set values for members that are not used (reserved area, for example).

For details of each parameter, refer to `ScePlayerSelectionDialogParam`.

## Examples

```
ScePlayerSelectionDialogParam param;

scePlayerSelectionDialogParamInitialize( &param );
param.userId = user_id;
if (scePlayerSelectionDialogOpen ( &param ) < 0 ) {
    // Error handling
}
```

## See Also

`ScePlayerSelectionDialogParam`, `scePlayerSelectionDialogOpen()`