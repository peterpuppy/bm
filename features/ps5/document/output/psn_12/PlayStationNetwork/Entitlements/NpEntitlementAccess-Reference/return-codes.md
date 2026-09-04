# NpEntitlementAccess Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Reference/return-codes.html

# Constants

# Return Codes

List of return codes returned by the NpEntitlementAccess library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Busy |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_FOUND` | 0x817D0005 | Specified additional content does not exist |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NO_ENTITLEMENT` | 0x817D0007 | Entitlement of the additional content is invalid |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_SUPPORTED` | 0x817D0009 | Unsupported |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NETWORK` | 0x817D0013 | Network error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_SIGNED_OUT` | 0x817D0014 | Called in the signed-out state |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_ABORTED` | 0x817D0016 | Processing aborted |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_USER_NOT_FOUND` | 0x817D0017 | User was not found |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_TIMEOUT` | 0x817D0018 | Processing timed out |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_TITLE_TOKEN` | 0x817D0019 | Failed to obtain title token |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_REQUEST` | 0x817D1001 | Request was invalid or malformed |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_PARAMETER` | 0x817D1002 | Parameter was invalid |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_NOT_IMPLEMENTED` | 0x817D1003 | Client is using an invalid method (`GET`, `POST`, `PUT`, or `DELETE`) |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_JSON` | 0x817D1004 | Request body was invalid |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_REQUEST_TOO_LONG` | 0x817D1005 | `POST` request was too long. Limit to 102400 bytes |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_REQUEST_URI_TOO_LONG` | 0x817D1006 | Request URI was too long. Limit to 2048 bytes |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_HTTP_NOT_IMPLEMENTED` | 0x817D1007 | HTTP is not supported. Use HTTPS |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_ACCESS_TOKEN` | 0x817D1008 | Access token is an invalid value or is corrupted |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_RATE_LIMIT_EXCEEDED` | 0x817D1009 | API rate limit was exceeded |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_NOT_AUTHORIZED` | 0x817D100A | User/client is not authorized to call this function |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INTERNAL` | 0x817D100B | Internal error of the server |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_SERVICE_UNAVAILABLE` | 0x817D100C | Server is not currently available |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_ENTITLEMENT_NOT_FOUND` | 0x817D100D | Invalid entitlement label or transaction ID was specified |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_TITLE_ID` | 0x817D100E | NP Title ID is an invalid value or is corrupted |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_TITLE_SECRET` | 0x817D100F | NP Title Secret is an invalid value or is corrupted |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_TITLE_TOKEN` | 0x817D1010 | NP Title Token is an invalid value or is corrupted |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_SERVICE_LABEL` | 0x817D1011 | NP service label is an invalid value or is corrupted |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_INVALID_RESPONSE` | 0x817D1012 | Inappropriate server response |
| `SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_MISSING_SCOPE_FOR_VC_CONSUMPTION` | 0x817D1013 | In-game currency can only be consumed from a game server; it cannot be consumed through the system software |