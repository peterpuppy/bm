# PlayerSelectionDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerSelectionDialog-Reference/sce-player-selection-dialog-player-label.html

# Setting Initial Status Parameters for Players

# ScePlayerSelectionDialogPlayerSelectStatus

Initial status of a player

## Definition

```
#include <player_selection_dialog.h>
typedef enum {
    (Omitted: see details below)
} ScePlayerSelectionDialogPlayerSelectStatus;
```

## Description

This constant indicates the initial status of a player.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_SELECT_STATUS_NOT_SELECTED` | 0 | Displays with non-selected status (default) |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_SELECT_STATUS_SELECTED` | 1 | Displays with selected status |

## See Also

`ScePlayerSelectionDialogInitialPlayerStatus`

# ScePlayerSelectionDialogPlayerEnableStatus

Status of whether a player is selectable

## Definition

```
#include <player_selection_dialog.h>
typedef enum {
    (Omitted: see details below)
} ScePlayerSelectionDialogPlayerEnableStatus;
```

## Description

This constant indicates whether a player has a selectable status.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_ENABLE_STATUS_ENABLE` | 0 | Modifiable (default) |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_ENABLE_STATUS_DISABLE` | 1 | Not modifiable |

## See Also

`ScePlayerSelectionDialogInitialPlayerStatus`

# ScePlayerSelectionDialogPlayerLabel

Type of string displayed in the player tile

## Definition

```
#include <player_selection_dialog.h>
typedef enum {
    (Omitted: see details below)
} ScePlayerSelectionDialogPlayerLabel;
```

## Description

This constant indicates the type of string to be displayed in the player tile.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_NONE` | 0 | No label (default) |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_CANT_SELECT` | 1 | Displays the label "Cannot Select" |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_JOINED` | 2 | Displays the label "Joined" |

## See Also

`ScePlayerSelectionDialogInitialPlayerStatus`

# ScePlayerSelectionDialogInitialPlayerStatus

Parameter indicating the initial status of a player

## Definition

```
#include <player_selection_dialog.h>

typedef struct ScePlayerSelectionDialogInitialPlayerStatus {
    SceNpAccountId accountId;
    ScePlayerSelectionDialogPlayerSelectStatus selectStatus;
    ScePlayerSelectionDialogPlayerEnableStatus enableStatus;
    ScePlayerSelectionDialogPlayerLabel label;
    uint8_t reserved[64];
} ScePlayerSelectionDialogInitialPlayerStatus;
```

## Members

|  |  |
| --- | --- |
| `accountId` | Account ID of the player |
| `selectStatus` | Initial selection status of the player |
| `enableStatus` | Whether the player's selection status can be modified |
| `label` | Type of string to be displayed in the player tile |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is for setting the initial status of each player displayed in the list of players to select in the player selection dialog.

For `accountId`, specify the account ID of the selectable player.

For `selectStatus`, specify the initial status for the player. Specify either of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_SELECT_STATUS_NOT_SELECTED` | 0 | Displays with non-selected status (default) |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_SELECT_STATUS_SELECTED` | 1 | Displays with selected status |

With `enableStatus`, specify whether or not the player's selection status can be modified. Specify either of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_ENABLE_STATUS_ENABLE` | 0 | Modifiable (default) |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_ENABLE_STATUS_DISABLE` | 1 | Not modifiable |

For `type`, specify the type of display label for the player. Specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_NONE` | 0 | No label (default) |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_CANT_SELECT` | 1 | Displays the label "Cannot Select" |
| `SCE_PLAYER_SELECTION_DIALOG_PLAYER_LABEL_JOINED` | 2 | Displays the label "Joined" |

`reserved` is a reserved area. This area must be filled with all 0's.

## See Also

`scePlayerSelectionDialogOpen()`