# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-user-id.html

# Obtaining User Information

# SceUserServiceUserId

User ID

## Definition

```
#include <user_service.h>
typedef int32_t SceUserServiceUserId;
```

## Description

This is a datatype for the user ID.

A user ID is usually a positive number represented as a 32-bit signed integer. Note that in most cases the value is larger than 16, which is the maximum number of local accounts.

In addition, several user IDs to be used for special purposes are defined. Refer to the "[SCE\_USER\_SERVICE\_USER\_ID](sceuserserviceuserid.html "Constants that indicate special user IDs")" section.

# sceUserServiceGetAgeLevel

Gets the value set for "Age Level for PS5 Games"

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetAgeLevel(
	SceUserServiceUserId userId,
	uint32_t *ageLevel
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `ageLevel` | Destination to store the obtained age level |

## Return Values

Stores the age level of the specified user in `*ageLevel` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the value (age level) set for "Age Level for PS5 Games" for the specified user.

"Age Level for PS5 Games" is one item of the parental control settings; it is set for each user.

When an attempt is made to start an application and the value of "Age Level for Boot Restriction" set in the application's parameter file (param.json) is higher than a value set for "Age Level for PS5 Games" for any of the logged in users, the system software will block the start of the application. Therefore, applications are usually not required to be aware of the value set for "Age Level for PS5 Games" for each user.

Use this function when it is necessary to determine whether content can be accessed using the value set for "Age Level for PS5 Games" in cases when, for example, the rating of the main application and the rating of additional content do not necessarily match (e.g., an application that uses various music).

For `*ageLevel`, the age level set for the target user or `SCE_USER_SERVICE_AGE_LEVEL_ANY` (=0xFFFFFFFF), which indicates that there is no restriction, will be stored.

It is not a problem to call this function for an adult account. `SCE_USER_SERVICE_AGE_LEVEL_ANY` will be stored in `*ageLevel` in such cases.

| **Value (Number)** | **Description** |
| --- | --- |
| `SCE_USER_SERVICE_AGE_LEVEL_ANY(`0xFFFFFFFF) | Not restricted |
| 0 to 21 | Set age level |

For information about the values for "Age Level for Boot Restriction" set in an application's parameter file (param.json), refer to "ageLevel" in [Param.json File Specification - Param File (param.json) Specifications - Parameter Definitions for Applications](../Param_Json-Specification/parameter-definitions-for-applications.html). For details about age levels and ratings for age levels, refer to TRC [R5005](../../../TRC/latest/TRC/R5005.html).

## Examples

```
int32_t ret;
uint32_t ageLevel;
ret = sceUserServiceGetAgeLevel(userId, &ageLevel);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetInitialUser

Gets the user ID of user that started the application

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetInitialUser(
	SceUserServiceUserId *userId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | Destination to store the obtained user ID |

## Return Values

Stores the user ID of the user that started the application in `*userId` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_OPERATION_NOT_SUPPORTED` | 0x80960006 | This operation cannot be used |

## Description

This function obtains the user ID of the user that started the application. Applications that are presumed to be played by one player can use it for obtaining the user ID.

For `userId`, specify a pointer to a `SceUserServiceUserId` type variable to store the user ID of the user that started the application.

This function cannot be used with applications that have the InitialUserAlwaysLoggedIn flag set to disabled in param.json; `SCE_USER_SERVICE_ERROR_OPERATION_NOT_SUPPORTED` will be returned.

## Examples

```
int32_t ret;
SceUserServiceUserId userId;
ret = sceUserServiceGetInitialUser(&userId);
if (ret != SCE_OK) {
	// Error handling
}
```

# sceUserServiceGetUserNumber

Gets the user number

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetUserNumber(
	const SceUserServiceUserId userId,
	int32_t *number
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `number` | Destination to store the obtained user number |

## Return Values

Stores the user number in `*number` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |

## Description

This function obtains the user number (number allocated by the system to a user).

For `userId`, specify the user ID of the target user.

For `number`, specify a pointer to the `int32_t` type variable to store the obtained user number.

The user number may change every time a user logs in; reobtain the user number every time a login is detected.

In addition, reobtain the user numbers for all users after resuming from a suspend. If a user logs out and then logs back in during a suspend, the user will appear to be continually logged in from the point of view of the application, but there is a possibility that the user number for that user will have changed.

## Examples

```
int32_t ret;
int32_t number;
ret = sceUserServiceGetUserNumber(userId, &number);
if (ret != SCE_OK) {
	// Error handling
}
```

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`

# sceUserServiceGetUserName

Gets the user name

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetUserName(
	const SceUserServiceUserId userId,
	char *userName,
	const size_t size
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID of the target user |
| `userName` | Destination to store the buffer for the obtained user name |
| `size` | Size of the buffer specified with `userName` |

## Return Values

Stores the user name in `*userName` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |
| `SCE_USER_SERVICE_ERROR_BUFFER_TOO_SHORT` | 0x8096000A | Buffer size is not enough |

## Description

This function obtains the user name of the logged in user.

For `userId`, specify the user ID of the target user.

For `userName` and `size`, specify the address and size of the buffer to store the obtained user name. The buffer must have a size of `SCE_USER_SERVICE_MAX_USER_NAME_LENGTH` + 1 or more.

After a user signs in to the PlayStation™Network, the user name that can be obtained with this function will be the same as the online ID of the account of PlayStation™Network.

## Examples

```
int32_t ret;
char username[SCE_USER_SERVICE_MAX_USER_NAME_LENGTH + 1];
ret = sceUserServiceGetUserName(userId, username, sizeof(username));
if (ret != SCE_OK) {
	// Error handling
}
```

## Notes

The user name is a 3- to 16-character string composed of alphanumeric characters (A-Z, a-z, 0-9), hyphens, and/or underscores; the user name is guaranteed to be unique on the same console.

## See Also

`sceUserServiceGetLoginUserIdList()`, `sceUserServiceGetEvent()`, `sceUserServiceGetInitialUser()`