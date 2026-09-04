# NpSessionSignaling Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Overview/connection-status-transitions.html

# Reference Information of the NpSessionSignaling Library

This topic provides, as reference information to help you understand the features of the NpSessionSignaling library at a deeper level, explanations of status transitions within connections, the NAT traversal feature, and the port numbers that are used.

# Connection Status Transitions

## Connection States

The three connection states are as follows.

* **INACTIVE:**

  State when no connection exists. No connection ID is assigned either.
* **PENDING:**

  State when processing is in progress to establish a connection.
* **ACTIVE:**

  State when a connection is established.

Connection Status Transition Diagram

## Status Transition Flow

This section explains the connection status transitions that accompany typical processing.

1. **Activation**

   Activation refers to when an application sends requests that connections be initiated to the NpSessionSignaling library. The application can call `sceNpSessionSignalingActivateUser()` to request the initiation of a connection with a specific user or call `sceNpSessionSignalingActivateSession()` to request the initiation of connections among session members.

   The following processing occurs within the library if activation succeeds:

   1. Assignment of a group ID and joining of a signaling group
   2. (For a connection with a specific user, in parallel with [1](connection-status-transitions.html#np-session-signaling-library-overview_2_1__internal_process_1); for connections among session members, after members with valid connections among the same session are found) initiation of establishment of connections with other endpoints in the same signaling group: assignment of connection IDs and transition from INACTIVE state to PENDING state
   3. (For connections with the PENDING state) obtainment of IP address and port number information using STUN and exchange of address information and UDP packet-based communication tests with other peers
   4. (Once communication tests have concluded) establishment of connection: transition from PENDING state to ACTIVE state and notification of ESTABLISHED event to application

   A sequence where both endpoints for a connection between Endpoint A and Endpoint B are activated at roughly the same time is shown in the following.

   When Activated Roughly at the Same Time

   In addition, a sequence in which Endpoint A activates first and Endpoint B, which was waiting in anticipation, activates in response is shown below.

   Sequence When Endpoint B Waits in Anticipation

   First, Endpoint B calls `sceNpSessionSignalingRequestPrepare()` to prepare to receive a connection request. When Endpoint A calls `sceNpSessionSignalingActivateUser()` targeting the other endpoint, the application will be notified of the PEER\_ACTIVATED event at Endpoint B.

   Next, when Endpoint B activates, Endpoints A and B will both enter the PENDING state and then enter the ACTIVE state after STUN and communication tests complete; the application will then be notified of the ESTABLISHED event. (Refer to [Sequence When Endpoint B Waits in Anticipation](connection-status-transitions.html#np-session-signaling-library-overview_2_1__ed740384-576f-11ee-8c99-0242ac120002).)

   If Endpoint B is not activated within thirty seconds after activation is performed for Endpoint A, a timeout will occur. When a timeout occurs, the connection will enter the INACTIVE state, and Endpoint A will be notified of the DEAD event.

   Note:

   In addition to timeouts, the DEAD event will also be notified when connection establishment processing fails and when a connection is disconnected.

   When there is a connection already in the ACTIVE state and there is an attempt to initiate the establishment of a connection between the same endpoints, there will immediately be a notification of an ESTABLISHED event. For example, if there is an already established connection in a given context and an attempt is made to establish in a separate context a connection with the same combination of peer addresses, the existing connection will be used, and there will immediately be a notification of an ESTABLISHED event.
2. **Connection: keep-alive**

   When the connection is in the ACTIVE state, the NpSessionSignaling library will exchange keep-alive packets in order to maintain communication, regardless of whether or not P2P communication exists in the application. Keep-alive packet exchanging is performed every 10 seconds. If a keep-alive packet does not arrive for over a minute, the connection will be determined to be disconnected, and the DEAD event will be notified.
3. **Disconnection**

   When an application calls `sceNpSessionSignalingDeactivate()`, all connections belonging to the target signaling group will be disconnected and a transition to the INACTIVE state will occur. If the connection at the other endpoint is in the PENDING state or ACTIVE state, the application will be notified of the DEAD event along with the error code `SCE_NP_SESSION_SIGNALING_ERROR_TERMINATED_BY_PEER`. (See [Sequence When Endpoint A Is Disconnected](connection-status-transitions.html#np-session-signaling-library-overview_2_1__ed740528-576f-11ee-8c99-0242ac120002).)

   If `sceNpSessionSignalingActivateSession()` has been called in a Player Session or Game Session to establish connections, connections with any members who leave the session will be disconnected when they leave.

   Sequence When Endpoint A Is Disconnected

# NAT Traversal Feature

The NAT Traversal feature provided in the NpSessionSignaling library is subject to restrictions that depend on the combination of the NAT status type of the network environment (router) with the NAT status type of the communication peer. The NAT status type combinations that allow communication between the host and target host are as follows. (For NAT status types, refer to the "[Obtaining Network Information](obtaining-network-information.html)" section.)

Combinations of NAT Status Types for which Communications Are Possible

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | **Other Host** | | |
| **Type 1** | **Type 2** | **Type 3** |
| **Host** | **Type 1** | enabled | enabled | enabled |
| **Type 2** | enabled | enabled | enabled |
| **Type 3** | enabled | enabled | disabled |

Note that it is possible for combinations marked "enabled" to be disabled to communicate depending on the behavior of the individual routers. Communication is not necessarily guaranteed for all possible combinations of routers.

## NAT Traversal Information

Information regarding the NAT Traversal feature can be confirmed from ★Debug Settings > Network > NAT Traversal Information of Development Kits.

**STUN Status (Failed/Succeeded)**

Indicates the usage of STUN.

**NAT Type (Type1/Type2/Type3)**

Indicates the NAT status type.

**Mapped Address**

When STUN Status is Succeeded, indicates the external IP address obtained by STUN.

**Mapping Policy (Endpoint Independent/Address Dependent/Address and Port Dependent)**

When STUN Status is Succeeded, indicates the assignment policy for the external port of NAT obtained by STUN.

**Port Preservation (True/False)**

When STUN Status is Succeeded, indicates whether or not the external port obtained by STUN is the same as the local port.

**Delta**

When STUN Status is Succeeded, indicates the destination IP address of STUN, as well as the difference of the external port assignment if it has been changed.

# Port Numbers

The port numbers to specify when calling each function are shown in the following:

## Port numbers used with UDPP2P

* When using `sceNetBind()` with the host
  + `addr->sin_port`: `SCE_NP_PORT` (=3658; however, it may be replaced by the kernel)
  + `addr->sin_vport`: game port
* When using `sceNetBind()` with the client
  + `addr->sin_port`: `SCE_NP_PORT` (=3658; however, it may be replaced by the kernel)
  + `addr->sin_vport`: game port
* When using `sceNetSendto()`
  + `addr->sin_port`: port number obtained with `sceNpSessionSignalingGetConnectionStatus()`
  + `addr->sin_vport`: game port

## Port numbers used with TCP over UDPP2P

* When using `sceNetBind()` with the host
  + `addr->sin_port`: game port
  + `addr->sin_vport`: `SCE_NP_PORT` (=3658)
* When using `sceNetBind()` with the client
  + `addr->sin_port`: game port
  + `addr->sin_vport`: `SCE_NP_PORT` (=3658)
* When using `sceNetConnect()`
  + `addr->sin_port`: game port
  + `addr->sin_vport`: peer port number obtained with `sceNpSessionSignalingGetConnectionStatus()`