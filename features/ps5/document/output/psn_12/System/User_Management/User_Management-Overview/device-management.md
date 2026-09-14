# User Management Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/device-management.html

# Device Management

# Device Library Common Design Model

With PlayStation®5, controllers have built-in microphones and speakers, and it is also possible to connect headsets. Since a single device will have multiple input/output features such as these, applications must have methods for identifying devices through each device library. This can be implemented in applications by specifying devices with users as keys, since a device is linked to a user for management as mentioned earlier in this document.

Since accessing a device is possible with a user as a key, each device library uses a common design model.

Figure 2. Device Library Common Design Model

## Virtual Devices

Physical devices cannot be directly seen from applications, instead they see virtual devices provided by device libraries. Virtual devices are defined for each device library. For example, the following virtual device types are defined for the AudioOut library.

* MAIN
* BGM
* VOICE
* PERSONAL
* PADSPK
* VIBRATION
* AUX

Virtual devices are defined based on their purposes, and do not necessarily have a 1:1 relationship with physical devices. When a virtual device is accessed, what kind of processing is performed and which physical device will ultimately have input/output performed is defined for each virtual device type. The routing/filtering layer performs mapping between virtual devices and physical devices, and the system software determines their configuration.

Applications can access devices by opening ports. Virtual devices are then accessed through these ports.

Note that virtual devices will exist even when corresponding physical devices are not connected, therefore it is not necessary to check the connection status of physical devices when opening ports.

## Virtual Device Type Attributes

Applications must comprehend the following attributes that define virtual device types.

* Whether linked to a specific user or the system
* Number of virtual devices
* Number of ports that can be opened for each virtual device
* Routing/filtering specifications

For more specific information, refer to the respective device library documents.

# Device Usage Procedure

To use a device, a procedure common to each device library will be required as follows.

1. Open a port and obtain the port handle
2. Access a device using the handle
3. Close the port after usage

## (1) Open a port and obtain the port handle

To access a device, a port must be opened and the handle obtained. Functions for this purpose will be in a format similar to the following example which uses the AudioOut library.

```
int32_t sceAudioOutOpen(
    SceUserServiceUserId userId,
    int32_t type,
    int32_t index,
    uint32_t len,
    uint32_t freq,
    uint32_t param
)
```

For the 1st argument, pass the user ID of the logged in user in order to specify the user that will use the device. For the method of obtaining user IDs, refer to the "[User Identifiers Used in a Program](user-identifiers-used-in-a-program.html)" section.

For the 2nd argument, specify the virtual device type. The virtual device type is also called the port type.

For the 3rd argument, specify an index value starting with 0 as the identifier for making distinctions when the same user is using multiple devices of the same virtual device type.

The 4th and later arguments are specific to each device library. They may not exist depending on the library.

When the open function call terminates normally, the port handle will be returned as the return value. If an error occurs, an error code specific to each device library or a common error code will be returned.

In addition to the AudioOut library, similar open functions are provided for each device library in similar formats with an interface that specifies user IDs, virtual device types, and indices. (However, there are also variations where this information is collected and passed together as a structure.)

## (2) Access a device using the handle

Functions for accessing devices are provided for each device library. The procedure varies according to each library, but usage of the handle obtained upon port opening as a device identifier is common between the libraries.

## (3) Close the port

When the processing for using the device has ended, close the port. Functions for this purpose will be in a format similar to the following example which uses the AudioOut library.

```
int32_t sceAudioOutClose(
    int32_t handle
)
```

Pass the handle obtained upon port opening to the argument.

Note:

All opened ports will be automatically closed upon application termination.