# NpSessionSignaling Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Overview/overview-of-p2p-connections-provided-by-the-np-session-signa.html

# Using the NpSessionSignaling Library

This topic explains how to use the NpSessionSignaling library. It concerns the mechanism for P2P connections that is provided by this library, the basic processing procedure from initializing the library to establishing a connection to perform P2P communication, and the connection and network information that you can obtain as necessary.

# Overview of P2P Connections Provided by the NpSessionSignaling Library

## P2P Connections with Specific Users

The NpSessionSignaling library uses peer addresses constituted based on account IDs and platform types to indicate specific users. A two-peer connection consisting only of the current user and his or her communication peer can be established by specifying the peer address of the other peer.

## P2P Connections Among Session Members

A connection can be established with or among all members participating in the same Player Session or Game Session who have valid connections by initiating a connection on the session in which the current user is participating.

There are two connection topologies among session members that can be specified: full mesh and star.

P2P Connection Topologies Among Session Members

* **Full mesh:**

  Each member with a valid connection establishes connections with all other members with valid connections.
* **Star:**

  Each member with a valid connection establishes a connection with a member who serves as the host.

  In cases in which anyone may be the member who becomes the host, specify host type AUTO when initiating the connection. If you would like to designate the member who will become the host, specify host type ME when that member initiates his or her connection and specify host type AUTO when the other members initiate their connections. A new host will be automatically selected if the member who is the host leaves the session, with all the other members re-establishing P2P connections with the new host.

## Signaling Groups

The NpSessionSignaling library defines "a group of peer addresses that have initiated P2P connections" as a "signaling group". The initiating of connections among session members can be described as the members joining a signaling group consisting of members with valid connections who share the same session ID. Similarly, initiating a connection with a specific user can be described as joining a signaling group consisting of a combination of the current user's peer address and the peer's peer address.

Signaling Groups and Connections

## Group IDs

With the NpSessionSignaling library, a "group ID" is assigned to each signaling group. The lifespan of a group ID is the same as that for the corresponding signaling group (from when P2P connections are initiated to when they are deactivated). A group ID is a locally unique value and may differ by unit even with membership within the same signaling group. Additionally, group IDs are assigned temporarily, and thus the same value will not necessarily be assigned to the same session ID or group of peer addresses every time.

## Connections

In the NpSessionSignaling library, P2P communication between a given pair of peer addresses are defined as a "connection".

When an application activates a signaling group, the NpSessionSignaling library automatically establishes connections among the peer addresses that belong to the signaling group. Connections cannot be deleted individually. The relevant connections are deleted when a signaling group is deactivated.

## Connection IDs

With the NpSessionSignaling library, a "connection ID" is assigned to each connection. The lifespan of a connection ID is the same as that for the corresponding connection (from when processing to establish the connection begins to when the connection is terminated). A connection ID is a locally unique value, and different values may be assigned to peer address groups in the same connection. Additionally, connection IDs are assigned temporarily, and thus the same value will not necessarily be assigned to the same pair of peer addresses every time.

Relationship Between Group ID and Connection ID

A connection ID is issued for each signaling group joined. Therefore, if the same peer address belongs to multiple different signaling groups, a different connection ID will be issued for each signaling group.

Examples include cases in which a signaling group is activated for a given Player Session while another signaling group is activated for another Game Session that includes the same peer address, or cases in which a connection has been initiated with a specific user and a signal group is activated with a Player Session that contains the same peer address.

If connections have been established with the same peer address across multiple signaling groups and some of those signal groups are then deactivated, the deactivated groups' connections will be deleted, but connections will be maintained with the groups that were not deactivated.

# Basic Procedure of the NpSessionSignaling Library

The procedure for establishing a P2P connection using the NpSessionSignaling library and performing P2P communication with the UDPP2P protocol is shown in the following. Also refer to the ["Connection Status Transitions"](connection-status-transitions.html)

1. [Initialize NpSessionSignaling library](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_1)
2. [Create a context](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_2)
3. [Prepare to receive connection requests from others (optional)](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_3)
4. [Activate a signaling group](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_4)
5. [Establish a connection](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_5)
6. [Obtain IP address and port number](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_6)
7. [Create a UDPP2P protocol socket and bind the address](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_7)
8. [Send and receive packets](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_8)
9. [Deactivate the signaling group (terminate the connection)](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_9)
10. [Terminate the NpSessionSignaling library](basic-procedure.html#np-session-signaling-library-overview_1_2__basic_procedure_10)

1. **Initialize NpSessionSignaling library**

   Call `sceNpSessionSignalingInitialize()` to initialize the NpSessionSignaling library. The following processing is performed in the initialization of the NpSessionSignaling library.

   * Creation of internal threads
   * Creation of the heap area used by the NpSessionSignaling library
2. **Create a context**

   Call `sceNpSessionSignalingCreateContext2()` and create a context. If multiple users use the NpSessionSignaling library at the same time, a unique context must be created for each of those users. When creating a context, set the user ID for a signed-in user, an NP service label specific to the title, and a callback function for receiving event notifications. Only one context can be created for each user. If a context has already been generated for a user, an error will be produced, and no new context can be created unless the old one is deleted.

   There are three callback functions, differentiated by the type of events they receive, defined: a request callback function, a group callback function, and a connection callback function. The function prototypes for these callback functions are defined as `SceNpSessionSignalingRequestCallback`, `SceNpSessionSignalingGroupCallback`, and `SceNpSessionSignalingConnectionCallback2`, respectively.

   When context creation is successful, the context ID can be obtained.
3. **Prepare to receive connection requests from others (optional)**

   Call `sceNpSessionSignalingRequestPrepare()` to initiate the context that you created and prepare to receive connection requests from others.

   Perform this step when you will be engaging in P2P communication with a specific user and when you will have an action of some kind occur upon receiving connection requests from others. This step is not necessary if engaging in P2P communication among session members or when engaging in P2P communication with a specific user but not using the connection request from the other peer, instead, having both peers always calling one another.

   When a connection request from another user is received, the group callback function will be notified of the `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_PEER_ACTIVATED` event, indicating that `sceNpSessionSignalingActivateUser()` was called on the other peer's end with the current user's peer address specified.
4. **Activate a signaling group**

   If communicating with a specific user, call `sceNpSessionSignalingActivateUser()`, specifying the other peer's peer address; if communicating among session members, call `sceNpSessionSignalingActivateSession()`, specifying the session ID. Regardless of the function, the group ID will be obtained upon calling it if there are no issues.

   When processing to initiate a connection succeeds within the library, the group callback function will be notified of the `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATED` event along with the group ID.

   If processing to initiate a connection fails, the `SCE_NP_SESSION_SIGNALING_GROUP_EVENT_ACTIVATE_ERROR` event will be notified; handle the error.
5. **Establish a connection**

   The NpSessionSignaling library attempts to establish a connection between the two peers that successfully initiated connections and notifies the connection callback function of the result.

   When processing begins to establish a connection, the `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_ACTIVATED` event will be notified along with the group ID and connection ID.

   When a connection is successfully established, the `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_ESTABLISHED` event will be notified along with the group ID and connection ID.

   When a connection establishment fails, the `SCE_NP_SESSION_SIGNALING_CONNECTION_EVENT_DEAD` event will be notified; handle the error.

   Use the connection ID, which is included in the event notifying that processing to establish a connection has been started, to check with which peer address a connection was started. Then, the connection ID, which is included in the event notifying that connection establishment failed, can be used to determine the peer address with which connection failed.
6. **Obtain IP address and port number**

   After the connection is established, call `sceNpSessionSignalingGetConnectionStatus()` to obtain the IP address and port number of the communication peer. Specify the context ID and connection ID as arguments.

   In addition, call `sceNpSessionSignalingGetLocalNetInfo()` to obtain the local IP address of the host.
7. **Create a UDPP2P protocol socket and bind the address**

   Call `sceNetSocket()` to create a UDPP2P protocol socket. Specify `SCE_NET_AF_INET` for the domain and `SCE_NET_SOCK_DGRAM_P2P` for the type as arguments.

   Then, call `sceNetBind()` to bind the address to the socket. Specify the `SceNetSockaddrIn` structure with the local IP address set for the IP address and `SCE_NP_PORT` (=3658) set for the port number as arguments. For the virtual port number, an arbitrary port for use by the application can be specified.
8. **Send and receive packets**

   To send packets, call `sceNetSend()` and `sceNetSendto()`. Specify the destination (communication peer) address with the `SceNetSockaddrIn` structure. For the virtual port number, specify an arbitrary port for use by the application.

   To receive packets, call `sceNetRecv()` or `sceNetRecvfrom()`. Specify the address of the sender (the communication peer) with the `SceNetSockaddrIn` structure.
9. **Deactivate the signaling group (terminate the connection)**

   When P2P communication is no longer required, call `sceNpSessionSignalingDeactivate()`to deactivate the signaling group. Specify the context ID and group ID as arguments.

   Leaving a signal group will terminate connections with the peer addresses in the group. The disconnected peer will also have their connection terminated, but unless deactivated, their peer address will remain in the signaling group, and there will be an attempt to establish a new connection when the peer attempts to re-activate. If no P2P communication is necessary for the peer, deactivate the signaling group.
10. **Terminate the NpSessionSignaling library**

    When terminating the NpSessionSignaling library, call `sceNpSessionSignalingDestroyContext()` to delete the context. Specify the context ID as an argument.

    Then call `sceNpSessionSignalingTerminate()` to terminate the NpSessionSignaling library.

# Obtaining Connection Information

After there has been notification of the ESTABLISHED event, `sceNpSessionSignalingGetConnectionInfo()` can be used to obtain information about the connection such as the following:

* Round-trip time
* Peer address of the peer
* IP address and port number of the peer
* The user's own IP address and port number as seen from the peer
* Packet loss percentage
* NAT status type of the peer

Each type of information is explained below.

## Round-trip time (SCE\_NP\_SESSION\_SIGNALING\_CONNECTION\_INFO\_RTT)

This is the time it takes a UDPP2P packet to make a round-trip to a connected peer and back (in microseconds). Measurement is made upon the exchange of the keep-alive packet, which takes place every 10 seconds. The average of the last 6 measurements is returned.

## Peer address of the peer (SCE\_NP\_SESSION\_SIGNALING\_CONNECTION\_INFO\_PEER\_ADDRESS)

This is the peer address of the connected peer (account ID and platform type).

## IP address and port number of the peer (SCE\_NP\_SESSION\_SIGNALING\_CONNECTION\_INFO\_NET\_ADDRESS)

This is the IP address and port number of the connected peer. The same values can be obtained as those given by `peerAddr` and `peerPort` in `sceNpSessionSignalingGetConnectionStatus()`.

## The user's own IP address and port number as seen from the peer (SCE\_NP\_SESSION\_SIGNALING\_CONNECTION\_INFO\_MAPPED\_ADDRESS)

This is the user's own IP address and port number as seen from the connected peer. For the connection between unit A and unit B, "the user's own IP address and port number as seen from the peer" for unit A will be the same value as "IP address and port number of the peer" for unit B.

## Packet loss percentage (SCE\_NP\_SESSION\_SIGNALING\_CONNECTION\_INFO\_PACKET\_LOSS)

This is the packet loss percentage when making a round-trip of a UDPP2P packet to a connected peer and back. Measurement is made upon the exchange of the keep-alive packet, which takes place every 10 seconds. The value of the last 6 measurements is returned.

## NAT status type of the peer (SCE\_NP\_SESSION\_SIGNALING\_CONNECTION\_INFO\_PEER\_NAT\_STATUS)

This is the NAT status type of the connection peer.

## Example of using connection information: RTT display

The following is an example that uses the connection information's round-trip time: For example, when implementing a menu that displays multiple Game Sessions onscreen and allows the user to choose which one to join, you can use the following procedure to obtain the round-trip time between the user and the representative of each Game Session and display it in that menu.

1. Use `getGameSessions` of the Session Manager Web API to obtain information of the Game Session's representative (`accountId` and `platform` of `representative`).

   Note: If you don't know the `sessionId` of the Game Session, obtain it using the Game Session search feature of the Session Manager Web API. Refer to [Session Manager Web API Overview - Using the Web API - Basic Usage of Game Session Search](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/basic-usage-of-game-session-search.html) for details.
2. Use `sceNpSessionSignalingActivateUser()` to create a signaling group between you and the representative.
3. Use `sceNpSessionSignalingGetConnectionInfo()` to obtain the RTT with the host.

# Obtaining Network Information

The NpSessionSignaling library retains the local IP address of the host, external IP address, NAT status type, and STUN status as network information required for establishing and maintaining a connection. Applications can obtain this network information by calling `sceNpSessionSignalingGetLocalNetInfo()`.

Each type of information is explained below.

## Local IP address

The local IP address is the IP address allocated to the interface.

## External IP address

The external IP address is the IP address used when connecting to the Internet. If the connection is via a NAT router, the address used by the NAT router to connect to the Internet is the external IP address. If connected directly to the Internet, the local IP address and the external IP address are the same.

## NAT status type

The NAT status type indicates the level of support that the NAT Traversal feature of the NpSessionSignaling library provides for the various NAT router statuses.

NAT Status Types

| **Type** | **Description** |
| --- | --- |
| Unknown | The NAT status type is being identified or the identification failed |
| Type 1 | The local IP address and the external IP address are the same (directly connected to the internet). |
| Type 2 | The local IP address and the external IP address are different, and the external port assignment does not depend on the communication peer |
| Type 3 | Type other than Type 1 or Type 2 |

## STUN status

This value indicates the STUN status. When the NAT status type is deemed unknown, this means that either STUN hasn't completed yet or STUN failed. This value can be used to determine which is the case. Note that valid values for the external IP address and NAT status type can only be obtained when STUN succeeds.