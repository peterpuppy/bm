# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/sce-np-session-signaling-get-connection-status.html

# Obtaining the P2P Connection Status

# SceNpSessionSignalingConnectionInfoCode

Information codes for connection targeted for obtainment

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingConnectionInfoCode {
    (Omitted: see details below)
} SceNpSessionSignalingConnectionInfoCode;
```

## Description

The enum constants below represent information about the connection targeted for obtainment. Specify one of the following constants as an argument when calling `sceNpSessionSignalingGetConnectionInfo()`.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_RTT` | 1 | Round-trip time (microseconds) |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_NET_ADDRESS` | 4 | IP address and port number of the communication peer |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_MAPPED_ADDRESS` | 5 | Application's own IP address and port number as seen from the communication peer |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_PACKET_LOSS` | 6 | Packet loss percentage |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_PEER_ADDRESS` | 7 | Peer address of the communication peer |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_PEER_NAT_STATUS` | 8 | NAT status type of the communication peer |

# SceNpSessionSignalingConnectionInfo

Connection information

## Definition

```
#include <np.h>
typedef union SceNpSessionSignalingConnectionInfo {
    uint32_t rtt; /* SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_RTT */
    SceNpPeerAddressA peerAddrA; /* SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_PEER_ADDRESS */
    struct {
        SceNetInAddr addr;
        SceNetInPort_t port;
        uint8_t padding[2];
    } address; /* SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_NET_ADDRESS, SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_MAPPED_ADDRESS */
    uint32_t packetLoss; /* SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_PACKET_LOSS */
    int peerNatStatus;    /* SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_PEER_NAT_STATUS */
} SceNpSessionSignalingConnectionInfo;
```

## Members

|  |  |
| --- | --- |
| `rtt` | Round-trip time (microseconds) |
| `peerAddrA` | Peer address of the communication peer |
| `address` | The user's own or communication peer's IP address and port number (network byte order) |
| `packetLoss` | Packet loss percentage |
| `peerNatStatus` | NAT status type of the communication peer |

## Description

This datatype represents connection information. A variable of this type is used when obtaining connection information with `sceNpSessionSignalingGetConnectionInfo()`.

# sceNpSessionSignalingGetConnectionInfo

Gets connection information

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetConnectionInfo(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingConnectionId connId,
    SceNpSessionSignalingConnectionInfoCode code,
    SceNpSessionSignalingConnectionInfo *info
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `connId` | Connection ID |
| `code` | Target information code |
| `info` | Destination to store the obtained connection information |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `info` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONN_NOT_FOUND` | 0x8055330C | Connection could not be found  The connection specified in `connId` could not be found. Check the value specified for `connId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONN_IN_PROGRESS` | 0x8055330E | Connection is in the process of being established  The connection specified in `connId` is in the progress of being established, and the information specified with `code` cannot be obtained yet.  Make sure that the values specified to the arguments are correct |

## Description

This function obtains information of the connection specified with `connId`. Of the members of `info`, valid information will only be stored in the member relevant to the information specified with `code`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpSessionSignalingConnectionId connId;

int ret;
SceNpSessionSignalingConnectionInfo info;

ret = sceNpSessionSignalingGetConnectionInfo(ctxId, connId, SCE_NP_SESSION_SIGNALING_CONNECTION_INFO_RTT, &info);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

* The peer address of the communication peer can be obtained even if the connection is still being established. All other information cannot be obtained until after the connection has been established, with any attempt to obtain information before then resulting in the error `SCE_NP_SESSION_SIGNALING_ERROR_CONN_IN_PROGRESS` being returned.
* The IP address and port number of the communication peer can also be obtained using `sceNpSessionSignalingGetConnectionStatus()`.

# SceNpSessionSignalingConnectionStatus

Connection statuses

## Definition

```
#include <np.h>
typedef enum SceNpSessionSignalingConnectionStatus {
    (Omitted: see details below)
} SceNpSessionSignalingConnectionStatus;
```

## Description

The enum constants below represent connection statuses that `sceNpSessionSignalingGetConnectionStatus()` returns.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_STATUS_INACTIVE` | 0 | INACTIVE state (a connection with the specified ID does not exist) |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_STATUS_PENDING` | 1 | PENDING state |
| `SCE_NP_SESSION_SIGNALING_CONNECTION_STATUS_ACTIVE` | 2 | ACTIVE state |

# sceNpSessionSignalingGetConnectionStatus

Gets the connection status

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetConnectionStatus(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingConnectionId connId,
    SceNpSessionSignalingConnectionStatus *connStatus,
    SceNetInAddr *peerAddr,
    SceNetInPort_t *peerPort
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `connId` | Connection ID |
| `connStatus` | Destination to store the obtained connection status |
| `peerAddr` | Destination to store the obtained IP address of the communication peer, or NULL |
| `peerPort` | Destination to store the obtained port number (network byte order) of the communication peer, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `connStatus` is NULL |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found  The context specified in `ctxId` could not be found. Check the value specified for `ctxId` |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONN_NOT_FOUND` | 0x8055330C | Connection could not be found  The connection specified in `connId` could not be found. Check the value specified for `connId` |

## Description

This function obtains the status of the connection specified with `connId`.

In `*peerAddr` and `*peerPort`, the IP address and port number of the connection peer will be stored if the connection is in the ACTIVE state. If the connection is not in the ACTIVE state, these values will be undefined. Additionally, if there is no need to obtain this information, NULL can be specified for `peerAddr` and `peerPort`.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;
SceNpSessionSignalingConnectionId connId;

int ret;
SceNpSessionSignalingConnectionStatus connStatus;
SceNetInAddr peerAddr;
SceNetInPort_t peerPort;

ret = sceNpSessionSignalingGetConnectionStatus(ctxId, connId, &connStatus, &peerAddr, &peerPort);
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpSessionSignalingGetConnectionInfo()`