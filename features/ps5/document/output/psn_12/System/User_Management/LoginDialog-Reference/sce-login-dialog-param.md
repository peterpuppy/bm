# LoginDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginDialog-Reference/sce-login-dialog-param.html

# Parameter Settings

# SceLoginDialogParam

Parameters for the login dialog

## Definition

```
#include <login_dialog.h>
typedef struct SceLoginDialogParam {
	int32_t size;
	SceLoginDialogMode mode;
	SceUserServiceUserId
		excludeUsersFromLoginList[SCE_USER_SERVICE_MAX_LOGIN_USERS];
	SceUserServiceUserId
		excludeUsersFromLogoutList[SCE_USER_SERVICE_MAX_LOGIN_USERS];
	SceUserServiceUserId initialFocus;
	int32_t reserved[5];
} SceLoginDialogParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `mode` | Login dialog operation mode |
| `excludeUsersFromLoginList` | Users to exclude from login |
| `excludeUsersFromLogoutList` | Users to exclude from logout |
| `initialFocus` | User with initial focus |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is used for specifying dialog parameters when displaying the login dialog with `sceLoginDialogOpen()`.

Use this structure after initializing it in advance with `sceLoginDialogParamInitialize()`.

For `size`, the size of this structure should be specified. However, because an appropriate value will automatically be stored to this member by initializing this structure with `sceLoginDialogParamInitialize()`, the program is not required to explicitly specify this value.

For `mode`, specify one of the following values as the login dialog operation mode. For details on each operation mode, refer to the "Login Dialog Operation Modes" section in the "Using the Library" chapter in the [LoginDialog Library Overview](../LoginDialog-Overview/__document_toc.html) document.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_DIALOG_MODE_ALL_USERS` | 0 | All users registered on the PlayStation®5 (both users logged in and users not logged in) can be selected |
| `SCE_LOGIN_DIALOG_MODE_NOT_LOGGED_IN_USERS_ONLY` | 1 | Only users not logged in can be selected |

For `excludeUsersFromLoginList`, specify the users to exclude from the selections of users to log in. By setting this member, it is possible to exclude selections in advance, such as a user that has been confirmed as Player 1 when selecting Player 2 in a 2-player game.

The only users that can be specified for elements in this array are logged in users or `SCE_USER_SERVICE_USER_ID_INVALID`. Obtain the user IDs of logged in users with the UserService library.

In addition, this member is valid only when `SCE_LOGIN_DIALOG_MODE_ALL_USERS` is specified for `mode`. It will be ignored when `SCE_LOGIN_DIALOG_MODE_NOT_LOGGED_IN_USERS_ONLY` is specified.

For `excludeUsersFromLogoutList`, specify the users to exclude from user selections for logout when logging out another user is required for user login processing.

The only users that can be specified for elements in this array are logged in users or `SCE_USER_SERVICE_USER_ID_INVALID`. Obtain the user IDs of logged in users with the UserService library.

For details on the logout feature in the login dialog, refer to the "User Logout Feature" section in the "Notes" chapter in the [LoginDialog Library Overview](../LoginDialog-Overview/__document_toc.html) document.

For `initialFocus`, specify the user on which the initial focus will be placed when the login dialog is displayed. The only users that can be specified are logged in users or `SCE_USER_SERVICE_USER_ID_INVALID`. Obtain the user IDs with the UserService library. When `SCE_USER_SERVICE_USER_ID_INVALID` is specified, the initial focus will be determined automatically by the system software.

In addition, this member is valid only when `SCE_LOGIN_DIALOG_MODE_ALL_USERS` is specified for `mode`. It will be ignored when `SCE_LOGIN_DIALOG_MODE_NOT_LOGGED_IN_USERS_ONLY` is specified for `mode`, and the initial focus will be determined automatically by the system software.

`reserved` is a reserved area. This area must be filled with 0's; however, it will be automatically filled with 0's by `sceLoginDialogParamInitialize()`.

## Notes

For the arrays `excludeUsersFromLoginList[]` and `excludeUsersFromLogoutList[]`, specify `SCE_USER_SERVICE_USER_ID_INVALID` for elements that will not be used. However, by initializing this structure with `sceLoginDialogParamInitialize()`, `SCE_USER_SERVICE_USER_ID_INVALID` will be stored in all the elements in each array, therefore programs do not need to explicitly specify it.

## See Also

`sceLoginDialogOpen()`, `sceLoginDialogParamInitialize()`

# sceLoginDialogParamInitialize

Initialize parameters for the login dialog

## Definition

```
#include <login_dialog.h>
void sceLoginDialogParamInitialize(
	SceLoginDialogParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for the login dialog |

## Description

This function initializes the parameters for the login dialog.

Before setting the various parameters, make sure to initialize the parameters with this function. Appropriate default values will be set to each member of `*param` by calling this function; the application is not required to explicitly set values for members that are not used (reserved area, for example).

For details of each parameter, see `SceLoginDialogParam`.

## See Also

`SceLoginDialogParam`