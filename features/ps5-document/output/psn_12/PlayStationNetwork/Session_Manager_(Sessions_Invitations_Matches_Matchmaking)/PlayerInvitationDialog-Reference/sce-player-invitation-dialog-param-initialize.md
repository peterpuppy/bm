# PlayerInvitationDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerInvitationDialog-Reference/sce-player-invitation-dialog-param-initialize.html

# Parameter Settings

# ScePlayerInvitationDialogSendParam

Player invitation dialog send parameter

## Definition

```
#include <player_invitation_dialog.h>
#define SCE_PLAYER_INVITATION_DIALOG_SESSION_ID_MAX_SIZE (45)

typedef struct {
	const char* sessionId;
	uint8_t reserved[64];
} ScePlayerInvitationDialogSendParam;
```

## Members

|  |  |
| --- | --- |
| `sessionId` | Player session ID obtained from the server (NULL-terminated) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used to specify the parameter required for sending invitations with the player invitation dialog.

For `sessionId`, specify the Player session ID obtained from the server. The string must be NULL-terminated and within the maximum size of `SCE_PLAYER_INVITATION_DIALOG_SESSION_ID_MAX_SIZE` (number of characters).

For the session feature of PlayStation™Network, refer to the [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html) document.

`reserved` is a reserved area. This area must be filled with 0's.

## See Also

`ScePlayerInvitationDialogParam`

# ScePlayerInvitationDialogMode

Player invitation dialog display mode

## Definition

```
#include <player_invitation_dialog.h>
typedef enum {
    (Omitted: see details below)
} ScePlayerInvitationDialogMode;
```

## Description

The following constants indicate the display mode of the player invitation dialog.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_INVITATION_DIALOG_MODE_INVALID` | 0 | Invalid mode/initial value |
| `SCE_PLAYER_INVITATION_DIALOG_MODE_SEND` | 1 | Send mode |

## See Also

`ScePlayerInvitationDialogParam`

# ScePlayerInvitationDialogParam

Player invitation dialog parameters

## Definition

```
#include <player_invitation_dialog.h>
typedef struct ScePlayerInvitationDialogParam {
	SceCommonDialogBaseParam baseParam;
	uint32_t size;
	SceUserServiceUserId userId;
	ScePlayerInvitationDialogMode mode;
	union {
		const ScePlayerInvitationDialogSendParam* sendParam;
	};
	uint8_t reserved[64];
} ScePlayerInvitationDialogParam;
```

## Members

|  |  |
| --- | --- |
| `baseParam` | Common dialog base parameters |
| `size` | Size of the structure |
| `userId` | User ID of the sender |
| `mode` | Player invitation dialog display mode |
| `sendParam` | Data parameter required for sending invitations |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used to specify the parameters of the player invitation dialog when the dialog is displayed with `scePlayerInvitationDialogOpen()`. Initialize this structure in advance using `scePlayerInvitationDialogParamInitialize()` and set values to the required members before use.

For `mode`, specify the display mode of the player invitation dialog. Specify the following value:

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_PLAYER_INVITATION_DIALOG_MODE_SEND` | 1 | Send mode |

For `userId`, specify the user ID of the user sending the invitations. For details on user IDs, refer to the [UserService Library Overview](../UserService-Overview/__document_toc.html) document.

For `sendParam`, specify the data parameter required for sending invitations. For details, refer to `ScePlayerInvitationDialogSendParam`.

`baseParam` is for specifying the common dialog base parameters and `size` is for specifying the structure size, but appropriate values for these members will be automatically stored when the structure is initialized with `scePlayerInvitationDialogParamInitialize()`, and there is no need to explicitly specify them in the program.

`reserved` is a reserved area. This area must be filled with 0's, but it will be automatically filled with 0's by `scePlayerInvitationDialogParamInitialize()`.

## See Also

`ScePlayerInvitationDialogSendParam`, `scePlayerInvitationDialogOpen`(), `scePlayerInvitationDialogParamInitialize()`

# scePlayerInvitationDialogParamInitialize

Initialize player invitation dialog parameters

## Definition

```
#include <player_invitation_dialog.h>
void scePlayerInvitationDialogParamInitialize(
	ScePlayerInvitationDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Initialization target parameters |

## Return Values

None

## Description

This function initializes player invitation dialog parameters.

Before each parameter can be set, this function must be used to initialize the structure. Because this function sets appropriate initial values to each of the structure members, there is no need for the application to explicitly set values for members that aren't used (reserved area, for example).

For details on each parameter of the player invitation dialog, refer to `ScePlayerInvitationDialogParam`.

## Examples

```
ScePlayerInvitationDialogParam param;

scePlayerInvitationDialogParamInitialize( &param );
```

## See Also

`ScePlayerInvitationDialogParam`