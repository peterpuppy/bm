# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/return-codes.html

# Common Constants

# SCE\_NP\_ONLINEID\_\*\_LENGTH

Data sizes used by PlayStation™Network related libraries

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ONLINEID_MIN_LENGTH` | 3 | Minimum Online ID length |
| `SCE_NP_ONLINEID_MAX_LENGTH` | 16 | Maximum Online ID length |

## Description

This constant is used to represent a data size used by PlayStation™Network related libraries.

# SceNpPlatformType

Platform type used in cross platforms

## Definition

```
#include <np/np_common.h>
typedef int32_t SceNpPlatformType;
```

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_PLATFORM_TYPE_NONE` | 0 | No platform is specified |
| `SCE_NP_PLATFORM_TYPE_PS3` | 1 | PlayStation®3 |
| `SCE_NP_PLATFORM_TYPE_VITA` | 2 | PlayStation®Vita |
| `SCE_NP_PLATFORM_TYPE_PS4` | 3 | PlayStation®4 |
| `SCE_NP_PLATFORM_TYPE_PS5` | 5 | PlayStation®5 |

## Description

This constant is used to represent the platform type used for titles dealing with cross platforms.

## See Also

`SceNpPeerAddressA`

# Return Codes

List of return codes returned by the Np library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_UNKNOWN_PLATFORM_TYPE` | 0x80550004 | Undefined platform |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_CALLBACK_ALREADY_REGISTERED` | 0x80550008 | Callback function is already registered |
| `SCE_NP_ERROR_CALLBACK_NOT_REGISTERED` | 0x80550009 | Callback function is not registered |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |
| `SCE_NP_ERROR_INVALID_SIZE` | 0x80550011 | Structure size specified for the `size` member of the structure is invalid |
| `SCE_NP_ERROR_ABORTED` | 0x80550012 | Processing was aborted |
| `SCE_NP_ERROR_REQUEST_MAX` | 0x80550013 | Requests exceeding the maximum number were generated at the same time |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Specified request does not exist |
| `SCE_NP_ERROR_INVALID_ID` | 0x80550015 | Specified ID is invalid |
| `SCE_NP_ERROR_TIMEOUT` | 0x8055001a | Timed out |
| `SCE_NP_PUSH_ERROR_NETWORK_NOT_AVAILABLE` | 0x8055a02a | Network is not available |