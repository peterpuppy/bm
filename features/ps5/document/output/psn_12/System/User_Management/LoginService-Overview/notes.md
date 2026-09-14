# LoginService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginService-Overview/notes.html

# Notes

# Execution Order for Device Assignment Requests and Connection Confirmation

For device reassignment to be completely successful, all devices to assign must be connected to the corresponding PlayStation®5 console. However, device assignment requests are not guaranteed to be completely fulfilled even in cases such as when device connection confirmation has been performed before calling `sceLoginServiceRequestDevices()` (situations such as devices being disconnected after connection confirmation are possible).

Therefore, it is recommended that applications are programmed so that they call `sceLoginServiceRequestDevices()` without confirming device connection; the Pad library (for example) should be used to subsequently check the device assignment status, and users should be appropriately informed if there are insufficient devices.

# Notes on Reassigning Multiple Devices

All desired user and device pairing assignments must be specified as a device assignment request list, even if you want to only change some of the device assignments out of the multiple devices that are already assigned to users.

For example, consider a case where an assignment change is desired as in [Figure 1](notes-on-reassigning-multiple-devices.html#login-service-library-overview_2_2__544e9b8c-e267-11ee-bd3d-0242ac120002).

Figure 1. Example of Multiple Device Reassignment

The following code shows an example where a controller is assigned to User C using the device assignment request list.

```
SceLoginServiceDeviceRequestList list;
sceLoginServiceDeviceRequestListParamInitialize(&list);
list.request[0].userId = userC;
list.request[0].devices = SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD;
```

Since User A and User B are not specified in this device assignment request list, which controller will be assigned to User C is not defined. If User A's controller is assigned to User C, the expected results will not be obtained.

Note:

The results will be the same when `SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_NONE` (no assigned device) is specified for User A and User B.

To ensure controller assignment to User A and User C, controller assignment must be specified for User A. The following shows a code example that guarantees the expected assignment results.

```
SceLoginServiceDeviceRequestList list;
sceLoginServiceDeviceRequestListParamInitialize(&list);
list.request[0].userId = userA;
list.request[0].devices = SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD;
list.request[1].userId = userC;
list.request[1].devices = SCE_LOGIN_SERVICE_USER_ASSIGNED_DEVICE_TYPE_PAD_STANDARD;
```