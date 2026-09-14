# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/return-codes.html

# Common Constants

# SCE\_USER\_SERVICE\_MAX

Constants that indicate the maximum values for the lengths of various types of data

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_MAX_LOGIN_USERS` | 4 | Maximum number of users that can be logged in at once |
| `SCE_USER_SERVICE_MAX_USER_NAME_LENGTH` | 16 | Maximum user name length |

## Description

These constants are used for specifying the maximum values for the lengths of various types of data used in this library.

# SCE\_USER\_SERVICE\_USER\_ID

Constants that indicate special user IDs

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_USER_ID_INVALID` | -1 | An invalid user ID |
| `SCE_USER_SERVICE_USER_ID_SYSTEM` | 255 | User ID specified when using a device that cannot be allocated to a specific user |
| `SCE_USER_SERVICE_USER_ID_EVERYONE` | 254 | User ID specified when not limiting common dialog operation to a specific user |

## Description

These constants are used for special purposes by this library and by libraries that receive user IDs obtained with this library.

# Return Codes

List of return codes returned by the UserService library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_INTERNAL` | 0x80960001 | Internal error |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_ALREADY_INITIALIZED` | 0x80960003 | Already initialized |
| `SCE_USER_SERVICE_ERROR_NO_MEMORY` | 0x80960004 | Could not allocate memory |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_OPERATION_NOT_SUPPORTED` | 0x80960006 | This operation cannot be used |
| `SCE_USER_SERVICE_ERROR_NO_EVENT` | 0x80960007 | No unobtained event exists |
| `SCE_USER_SERVICE_ERROR_NOT_LOGGED_IN` | 0x80960009 | User is not logged in |
| `SCE_USER_SERVICE_ERROR_BUFFER_TOO_SHORT` | 0x8096000A | Buffer size is not enough |