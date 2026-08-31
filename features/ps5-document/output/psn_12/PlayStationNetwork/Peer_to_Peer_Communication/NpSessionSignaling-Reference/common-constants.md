# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/common-constants.html

# Common Constants

# Error Codes

List of error codes returned by the NpSessionSignaling library

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Library is not initialized |
| `SCE_NP_SESSION_SIGNALING_ERROR_ALREADY_INITIALIZED` | 0x80553302 | Library is already initialized |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument |
| `SCE_NP_SESSION_SIGNALING_ERROR_OWN_PEER_ADDRESS` | 0x80553304 | The user's own peer address is specified |
| `SCE_NP_SESSION_SIGNALING_ERROR_OUT_OF_MEMORY` | 0x80553305 | Insufficient memory |
| `SCE_NP_SESSION_SIGNALING_ERROR_TIMEOUT` | 0x80553306 | Timed out |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTXID_NOT_AVAILABLE` | 0x80553307 | Context ID could not be obtained |
| `SCE_NP_SESSION_SIGNALING_ERROR_CTX_NOT_FOUND` | 0x80553308 | Context could not be found |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRPID_NOT_AVAILABLE` | 0x80553309 | Group ID could not be obtained |
| `SCE_NP_SESSION_SIGNALING_ERROR_GRP_NOT_FOUND` | 0x8055330A | Group could not be found |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONNID_NOT_AVAILABLE` | 0x8055330B | Connection ID could not be obtained |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONN_NOT_FOUND` | 0x8055330C | Connection could not be found |
| `SCE_NP_SESSION_SIGNALING_ERROR_PEER_UNREACHABLE` | 0x8055330D | Could not reach the communication peer |
| `SCE_NP_SESSION_SIGNALING_ERROR_CONN_IN_PROGRESS` | 0x8055330E | Connection is in the process of being established |
| `SCE_NP_SESSION_SIGNALING_ERROR_TERMINATED_BY_PEER` | 0x8055330F | Communication peer executed processing to terminate the connection |
| `SCE_NP_SESSION_SIGNALING_ERROR_TERMINATED_BY_MYSELF` | 0x80553310 | Current user terminated the connection |
| `SCE_NP_SESSION_SIGNALING_ERROR_TOO_MANY_CONN` | 0x80553311 | Exceeded the maximum number of connections |

Note that the application must not malfunction even if other error codes are returned.