# LoginService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginService-Overview/conditions-for-devices-that-can-be-assigned.html

# Using the Library

# Conditions for Devices That Can Be Assigned

The following devices connected to a PlayStation®5 console are excluded from the devices that can be reassigned with the LoginService library.

* Controllers connected through a network using remote play
* Controllers connected through a network using share play
* Controllers without a user assigned (controllers currently being assigned by users in the login screen, etc.)

# Basic Procedure

This section explains the procedure for using the LoginService library to reassign devices to each user. An overview of the processing flow and the functions/datatypes used are as follows:

1. [Initialize the LoginService library](basic-procedure.html#login-service-library-overview_1_2__login-service-library-overview_1_2_1)
2. [Prepare a device assignment request list](basic-procedure.html#login-service-library-overview_1_2__login-service-library-overview_1_2_2)
3. [Request device assignment](basic-procedure.html#login-service-library-overview_1_2__login-service-library-overview_1_2_3)
4. [Terminate the LoginService library](basic-procedure.html#login-service-library-overview_1_2__login-service-library-overview_1_2_4)

## (1) Initialize the LoginService library

Call `sceLoginServiceInitialize()` and initialize the LoginService library.

## (2) Prepare a device assignment request list

Prepare an `SceLoginServiceDeviceRequestList` structure as a device assignment request list and initialize it using `sceLoginServiceDeviceRequestListParamInitialize()`. Afterward, specify pairings of users and the devices to assign to each user. User IDs can be obtained with the UserService library, LoginDialog library, etc. For details on obtaining user IDs, refer to the "[Obtaining Users Assigned to Devices](obtaining-users-assigned-to-devices.html)" section.

```
SceLoginServiceDeviceRequestList list;
sceLoginServiceDeviceRequestListParamInitialize(&list);
list.request[0].userId = m_playerC;
list.request[0].devices = 	SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD;
list.request[1].userId = m_playerD;
list.request[1].devices = 	SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD;
```

## (3) Request device assignment

Call `sceLoginServiceRequestDevices()` when control should be switched over to the other user.

```
if ( sceLoginServiceRequestDevices(&list) != SCE_OK ) {
    // Error handling
}
```

By doing this, the library will request the system software to reassign the devices to each user in accordance with the specified device assignment request list.

However, it is not guaranteed that all of the specified requests will be fulfilled, even when `sceLoginServiceRequestDevices()` terminates normally. For details on the procedure for checking the assignment request results, refer to "[Obtaining Device Assignment Results](obtaining-device-assignment-results.html)".

## (4) Terminate the LoginService library

When the LoginService library is no longer needed, use `sceLoginServiceTerminate()` to terminate the library. This will release the resources that were allocated upon library initialization.

## API Summary

The following shows a summary of the API features used in the basic processing for when reassigning devices to each user.

Table 1.  API Features Used in Basic Processing

| **API Feature** | **Description** |
| --- | --- |
| `sceLoginServiceInitialize()` | Function that initializes the LoginService library |
| `SceLoginServiceDeviceRequestList` | Structure that represents a device assignment request list |
| `sceLoginServiceDeviceRequestListParamInitialize()` | Function that initializes a device assignment request list |
| `sceLoginServiceRequestDevices()` | Function that requests device assignment |
| `sceLoginServiceTerminate()` | Function that terminates the LoginService library |

# Obtaining Users Assigned to Devices

In order to reassign devices with `sceLoginServiceRequestDevices()`, the target users to whom each device will be assigned must be obtained by the application in advance.

* When the target user is logged in

  The user ID can be obtained using the UserService library.
* When the target user is not logged in

  By using the LoginDialog library, it will be possible to display login dialog that provides a GUI for promoting user login. When the user successfully logs in with the login dialog, the user ID of this user will be obtained as the dialog call result.

For details on the login dialog, refer to the [LoginDialog Library Overview](../LoginDialog-Overview/__document_toc.html) document and [LoginDialog Library Reference](../LoginDialog-Reference/__document_toc.html) document.

For details on user login, refer to the [User Management Overview](../User_Management-Overview/__document_toc.html) document.

# Obtaining Device Assignment Results

When `sceLoginServiceRequestDevices()` is called, the system software will attempt to assign a device to each user in order to fulfill the specified device assignment request list as much as possible, but the requests are not guaranteed to be completely fulfilled. For example, when `SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD` is requested for two users with only one controller connected to a PlayStation®5 console, a controller will be assigned to one of the users but not to the other user.

Since the LoginService library does not provide a feature that notifies applications of assignment request results, after calling `sceLoginServiceRequestDevices()` applications must use the Pad library, etc. to check if a device has been assigned to each user as requested or not. For example, by referencing the `connected` member in the `ScePadData` structure obtained by calling the `scePadRead()` or `scePadReadState()` function of the Pad library, it will be possible to determine whether a controller connected to PlayStation®5 console has been assigned to a user.