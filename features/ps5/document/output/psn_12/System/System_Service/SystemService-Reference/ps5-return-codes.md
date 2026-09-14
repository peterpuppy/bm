# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-return-codes.html

# Common Constants

# Return Codes

List of return codes returned by the SystemService library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_INTERNAL` | 0x80A10001 | Unexpected internal error occurred |
| `SCE_SYSTEM_SERVICE_ERROR_UNAVAILABLE` | 0x80A10002 | SystemService is in an unusable state |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | Parameter is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_NO_EVENT` | 0x80A10004 | No receivable events |
| `SCE_SYSTEM_SERVICE_ERROR_REJECTED` | 0x80A10005 | Use of feature rejected |
| `SCE_SYSTEM_SERVICE_ERROR_NEED_DISPLAY_SAFE_AREA_SETTINGS` | 0x80A10006 | Safe area information has not been set |
| `SCE_SYSTEM_SERVICE_ERROR_INVALID_URI_LEN` | 0x80A10007 | URI length is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_INVALID_URI_SCHEME` | 0x80A10008 | URI scheme is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_NO_APP_INFO` | 0x80A10009 | No application information |
| `SCE_SYSTEM_SERVICE_ERROR_NOT_FLAG_IN_PARAM_SFO` | 0x80A1000A | Flag required for param.json is not set |
| `SCE_SYSTEM_SERVICE_ERROR_INCORRECT_USER_ID` | 0x80A1000B | User ID is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_INVALID_PARAM_LEN` | 0x80A1000C | Parameter string is too long |

## Description

Every function provided by the SystemService library returns `SCE_OK` (=0) for normal termination and the return codes (negative values) listed above for abnormal termination.