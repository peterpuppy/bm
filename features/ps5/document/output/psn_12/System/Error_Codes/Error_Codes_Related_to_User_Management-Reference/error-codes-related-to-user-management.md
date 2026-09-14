# Error Codes Related to User Management – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Error_Codes_Related_to_User_Management-Reference/error-codes-related-to-user-management.html

# Error Codes Related to User Management

# Error Codes Related to User Management

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_DEVICE_SERVICE_ERROR_INVALID_USER` | 0x809B0001 | Specified user ID is invalid |
| `SCE_DEVICE_SERVICE_ERROR_INVALID_DEVICE_TYPE` | 0x809B0002 | Specified device type does not exist |
| `SCE_DEVICE_SERVICE_ERROR_INVALID_INDEX` | 0x809B0003 | Index value is not supported by the device |
| `SCE_DEVICE_SERVICE_ERROR_MEMORY` | 0x809B0004 | Memory allocation failed |
| `SCE_DEVICE_SERVICE_ERROR_INVALID_DEVICE_ID` | 0x809B0005 | Specified device ID is invalid |
| `SCE_DEVICE_SERVICE_ERROR_INVALID_STATE` | 0x809B000B | A problem exists in the system's internal state |
| `SCE_DEVICE_SERVICE_ERROR_INVALID_PARAM` | 0x809B0080 | Specified argument is invalid |
| `SCE_DEVICE_SERVICE_ERROR_USER_NOT_LOGIN` | 0x809B0081 | User is not logged in |
| `SCE_DEVICE_SERVICE_ERROR_USER_OVER_MAX` | 0x809B0082 | Number of users has reached the maximum value |
| `SCE_DEVICE_SERVICE_ERROR_DRIVER_OVER_MAX` | 0x809B0083 | Number of drivers has reached the maximum value |
| `SCE_DEVICE_SERVICE_ERROR_DEVICE_OVER_MAX` | 0x809B0084 | Number of devices has reached the maximum value |
| `SCE_DEVICE_SERVICE_ERROR_BUS_OVER_MAX` | 0x809B0085 | Number of buses has reached the maximum value |
| `SCE_DEVICE_SERVICE_ERROR_PORT_OVER_MAX` | 0x809B0086 | Number of ports has reached the maximum value |
| `SCE_DEVICE_SERVICE_ERROR_INTERNAL` | 0x809B00FF | Fatal internal error occurred |

## Description

The above error codes are returned by the device management service. They are defined in device\_service/device\_service\_error.h. Because devices are managed in relation to logged in users, the above error codes will be returned as user management-related errors mainly by libraries handling input/output devices.