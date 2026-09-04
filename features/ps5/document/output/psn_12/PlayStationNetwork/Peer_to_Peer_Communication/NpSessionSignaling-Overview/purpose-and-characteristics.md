# NpSessionSignaling Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Overview/purpose-and-characteristics.html

# Basic Information about the NpSessionSignaling Library

This topic provides, as basic information needed to use the NpSessionSignaling library, the purpose and characteristics of the library, its main features, the resources used by the library, how to embed the library into a program, and a sample program and reference materials provided by SIE.

# Purpose and Characteristics of the NpSessionSignaling Library

The NpSessionSignaling library is a library for performing the communication processing required for P2P communication, such as for online games and chats on PlayStation™Network. The library provides methods of establishing two types of P2P connections: connections with specific users and connections (full mesh type and star type) among session members. The NpSessionSignaling library and the UDPP2P protocol provided by the Net library enable developers to implement P2P communication environments compatible with various user network environments. By further combining with the Rudp library, it will be possible to divide usage based on the purposes of the various communication types required by P2P communication, such as absence/presence of reliability and packet delivery order guarantees.

# Main Features of the NpSessionSignaling Library

The features provided by the NpSessionSignaling library are as follows:

* Feature for establishing a connection with a specific user or establishing connections with the other members of a session (activating a signaling group)
* Feature for obtaining the IP address and UDP port number from the peer address (account ID and platform type) of the communication peer
* NAT Traversal feature for communicating across a NAT router
* Feature for obtaining the user's own network information

# Resources Used by the NpSessionSignaling Library

The NpSessionSignaling library uses the following system resources:

System Resources Used by the NpSessionSignaling Library

| **Resource** | **Description** |
| --- | --- |
| Work memory | The size of the memory pool used by the NpSessionSignaling library can be specified with the `poolSize` member of the `param` argument of `sceNpSessionSignalingInitialize()`. When `sceNpSessionSignalingInitialize()` is called, an additional 1 MiB of memory separate form that specified with `poolSize` will be allocated.  Size of the required memory pool greatly differs depending on what is being processed You can use `sceNpSessionSignalingGetMemoryInfo()` to check how much memory is being used by the NpSessionSignaling library; test several times and refer to the obtained values to determine the value. If memory runs out in the middle of P2P connection establishment processing, rather than at the time of the API call, a timed-out error code, rather than an insufficient memory error code, may be returned. In particular, note that, if there is insufficient memory on the peer side when establishing a P2P connection, the connection will time out during the connection process. Therefore, you should check the amount of memory using `sceNpSessionSignalingGetMemoryInfo()` on the peer side as well as on the device on which the error occurs. |
| Thread | Multiple threads will be created when `sceNpSessionSignalingInitialize()` is called. The application can specify the priorities and CPU affinities.  The stack sizes of the threads called by the callback function can be specified. |

# Embedding the NpSessionSignaling Library into a Program

Include np.h in the source program. In addition, before calling any NpSessionSignaling library function in the program, load the PRX module with the relevant Sysmodule library function, as follows:

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_SESSION_SIGNALING) != SCE_OK ) {
    // Error handling
}
```

Link libSceNpSessionSignaling\_stub\_weak.a upon building the program.

# NpSessionSignaling Library Sample Program

A sample program using the NpSessionSignaling library is as follows:

## sample\_code/playstation\_network/api\_np\_session\_signaling

This sample exemplifies basic usage of the NpSessionSignaling library.

# Reference Materials for Using the NpSessionSignaling Library

Refer to the following document for an overview of the PlayStation™Network functionalities.

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)

Refer to the following documents regarding the Np library, which is commonly required when using the PlayStation™Network functionalities.

* [Np Library Overview](../Np-Overview/__document_toc.html) and [Np Library Reference](../Np-Reference/__document_toc.html)

Refer to the following documents regarding the P2P exclusive protocols.

* [Network Overview](../Network-Overview/__document_toc.html)
* [Net Library Overview](../Net-Overview/__document_toc.html) and [Net Library Reference](../Net-Reference/__document_toc.html)

Refer to the following documents regarding the Rudp library, which supports reliable data transfer (RUDP).

* [Rudp Library Overview](../Rudp-Overview/__document_toc.html) and [Rudp Library Reference](../Rudp-Reference/__document_toc.html)

For an overall look at sessions and the difference between a Player Session and a Game Session, refer to the following document:

* [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html)

A request to use the Session Manager service is required for using the NpSessionSignaling library. Refer to the following document regarding how to make a service request.

* [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpSessionSignaling Library](../ReleaseNotes/PlayStation_Network-NpSessionSignaling-ReleaseNotes.html)