# SigninDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SigninDialog-Reference/sce-signin-dialog-param.html

# Parameter Settings

# SceSigninDialogParam

Parameters for the signin dialog

## Definition

```
#include <signin_dialog.h>
typedef struct SceSigninDialogParam {
	int32_t size;
	SceUserServiceUserId userId;
	int32_t reserved[2];
} SceSigninDialogParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID of user to sign in |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used for specifying dialog parameters when displaying the signin dialog with `sceSigninDialogOpen()`.

Use this structure after initializing it in advance with `sceSigninDialogParamInitialize()`.

For `size`, the size of this structure should be specified. However, because an appropriate value will automatically be stored to this member by initializing this structure with `sceSigninDialogParamInitialize()`, the program is not required to explicitly specify this value.

For `userId`, specify the ID of the user to be signed in. User IDs can be obtained from the UserService library.

`reserved` is a reserved area. This area must be filled with 0's; however, it will be automatically filled with 0's by `sceSigninDialogParamInitialize()`.

## See Also

`sceSigninDialogOpen()`, `sceSigninDialogParamInitialize()`

# sceSigninDialogParamInitialize

Initialize parameters for the signin dialog

## Definition

```
#include <signin_dialog.h>
void sceSigninDialogParamInitialize(
	SceSigninDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the signin dialog |

## Description

This function initializes the parameters for the signin dialog.

Before setting the various parameters, make sure to initialize the parameters with this function. Appropriate default values will be set to each member of `*param` by calling this function; the application is not required to explicitly set values for members that are not used (reserved area, for example).

For details of each parameter, see `SceSigninDialogParam`.

## See Also

`SceSigninDialogParam`