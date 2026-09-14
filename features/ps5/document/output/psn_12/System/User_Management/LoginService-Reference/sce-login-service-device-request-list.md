# LoginService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginService-Reference/sce-login-service-device-request-list.html

# Device Assignment

# SceLoginServiceDeviceRequestItem

User and device pairing

## Definition

```
#include <login_service.h>
typedef struct _SceLoginServiceDeviceRequestItem {
    SceUserServiceUserId userId;
    SceLoginServiceUserAssignedDeviceType devices;
    int32_t reserved[2];
} SceLoginServiceDeviceRequestItem;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `devices` | Device types |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure represents a user and a device to pair with the user. An array with this structure as elements is specified to `request` member in an `SceLoginServiceDeviceRequestList` structure when requesting device assignment with `sceLoginServiceRequestDevices()`.

For `userId`, specify the ID of the user to pair with the device. User IDs can be obtained from the UserService library.

For `devices`, specify the bitwise OR of the following values that represent the types of devices to assign to the user specified with `userId`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_NONE` | 0x0 | No assigned device |
| `SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD` | 0x1 | Standard game controller (wireless controller for PlayStation®5 or a controller compatible with it) or an arcade stick type controller |
| `SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_SPECIAL` | 0x2 | Special game controller (third-party special controller with PlayStation®5 compatibility) |

`reserved` is a reserved area. This area must be filled with 0's; however, it will automatically be filled with 0's by initializing the `SceLoginServiceDeviceRequestList` structure with `sceLoginServiceDeviceRequestListParamInitialize()`.

## Notes

The LoginService assignment processing does not apply to remote play controllers. For details on the conditions for devices that can be assigned, refer to the "Conditions for Devices That Can Be Assigned" section in the [LoginService Library Overview](../LoginService-Overview/__document_toc.html) document.

# SceLoginServiceDeviceRequestList

Device assignment request list

## Definition

```
#include <login_service.h>
typedef struct _SceLoginServiceDeviceRequestList {
	SceLoginServiceDeviceRequestItem request[SCE_USER_SERVICE_MAX_LOGIN_USERS];
} SceLoginServiceDeviceRequestList;
```

## Members

|  |  |
| --- | --- |
| `request` | Array of device assignment requests for each user |

## Description

This structure is for specifying user-device pairings when requesting device assignments with `sceLoginServiceRequestDevices()`.

Before using this structure, first initialize it using `sceLoginServiceDeviceRequestListParamInitialize()`.

For element in `request[]`, specify `SceLoginServiceDeviceRequestItem` structures that represent the pairings between each user and the devices to assign. If there are elements that will not be used at this time, specify `SCE_USER_SERVICE_USER_ID_INVALID` for the `userId` member and specify `SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_NONE` for the `devices` member.

However, these values will be appropriately stored in all elements in `request[]` upon initialization with `sceLoginServiceDeviceRequestListParamInitialize()`, therefore there is no need for applications to explicitly specify these values.

# sceLoginServiceDeviceRequestListParamInitialize

Initialize device assignment request list

## Definition

```
#include <login_service.h>
void sceLoginServiceDeviceRequestListParamInitialize(
    SceLoginServiceDeviceRequestList * param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Device assignment request list |

## Description

This function initializes an `SceLoginServiceDeviceRequestList` structure that represents a device assignment request list.

Before setting values in each member in this structure, this function must be called to initialize the structure. By calling this function, appropriate initial values will be set in each member in `*param`, therefore it is not necessary for applications to explicitly set values for members that will not be used such as reserved areas.

For details on each parameter in a device assignment request list, refer to `SceLoginServiceDeviceRequestList` and `SceLoginServiceDeviceRequestItem`.

## See Also

`sceLoginServiceRequestDevices()`

# sceLoginServiceRequestDevices

Request device assignment

## Definition

```
#include <login_service.h>
int32_t sceLoginServiceRequestDevices(
    const SceLoginServiceDeviceRequestList *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Device assignment request list |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The error codes defined by this library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_SERVICE_ERROR_NOT_INITIALIZED` | 0x813A0001 | LoginService library is not initialized |
| `SCE_LOGIN_SERVICE_ERROR_PARAM_INVALID` | 0x813A0003 | Parameter is invalid |
| `SCE_LOGIN_SERVICE_ERROR_UNEXPECTED_FATAL` | 0x813A0004 | Unexpected fatal error |
| `SCE_LOGIN_SERVICE_ERROR_SERVICE_BUSY` | 0x813A0005 | Process is busy (being restarted, for example) |
| `SCE_LOGIN_SERVICE_ERROR_INVALID_USER_ID` | 0x813A0006 | User ID is invalid |

## Description

This function requests the system software to reassign devices to each user.

When this function is normally executed, the system software will attempt to assign a device to each user according to the specified device assignment request list. However, all specified requests will not necessarily be fulfilled. For details, refer to the "Obtaining Device Assignment Results" section of the [LoginService Library Overview](../LoginService-Overview/__document_toc.html).

When this function is normally executed, the user and device holder relations set by users in the system software login screen will be forcibly discarded. In order to avoid user confusion, call this function only once every time it is desired to change the holders of devices, such as when switching from Player 1 to Player 2. Calling it at regular intervals such as every second is not recommended.

This function is a blocking function that returns after the device assignment processing completes. Since this processing takes a few hundred milliseconds, calling this function in a thread other than the main thread is highly recommended.

## See Also

`sceLoginServiceDeviceRequestListParamInitialize()`