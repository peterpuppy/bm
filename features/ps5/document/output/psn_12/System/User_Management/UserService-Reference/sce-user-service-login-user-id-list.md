# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-login-user-id-list.html

# Obtaining Logged in User List

# SceUserServiceLoginUserIdList

Structure that holds the user ID list of the logged in users

## Definition

```
#include <user_service.h>
typedef struct SceUserServiceLoginUserIdList {
	SceUserServiceUserId userId[SCE_USER_SERVICE_MAX_LOGIN_USERS];
} SceUserServiceLoginUserIdList;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID array |

## Description

This structure is used for receiving the results when obtaining the user ID list of the logged in users with `sceUserServiceGetLoginUserIdList()`.

# sceUserServiceGetLoginUserIdList

Obtains the user ID list of the logged in users

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetLoginUserIdList(
	SceUserServiceLoginUserIdList *userIdList
)
```

## Arguments

|  |  |
| --- | --- |
| `userIdList` | Destination to store the user ID list |

## Return Values

Stores the user ID list in `*userIdList` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |

## Description

This function obtains the user ID list of the logged in users. In general, user ID lists are managed using `sceUserServiceGetEvent()` to support dynamic user logins/logouts, but if you want to obtain another user ID list for some reason, use `sceUserServiceGetLoginUserIdList()` (this function).

For `userIdList`, specify a pointer to the `SceUserServiceLoginUserIdList` structure to store the user ID list. If the number of logged in users is less than `SCE_USER_SERVICE_MAX_LOGIN_USERS`, `SCE_USER_SERVICE_USER_ID_INVALID` will be obtained for the each of the insufficient number of users.

## Examples

```
SceUserServiceLoginUserIdList userIdList;
if (sceUserServiceGetLoginUserIdList(&userIdList) < 0) {
	// Error handling
}
for (int i = 0; i < SCE_USER_SERVICE_MAX_LOGIN_USERS; i ++) {
	if (userIdList.userId[i] != SCE_USER_SERVICE_USER_ID_INVALID) {
		// Do something
	}
}
```