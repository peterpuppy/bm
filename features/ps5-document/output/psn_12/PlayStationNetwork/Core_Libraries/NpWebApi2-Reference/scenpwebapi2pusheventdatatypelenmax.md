# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/scenpwebapi2pusheventdatatypelenmax.html

# Common Constants

# SCE\_NP\_WEBAPI2\_PUSH\_EVENT\_EXTD\_DATA\_KEY\_LEN\_MAX

Maximum length for Push event extended data keys

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX` | 32 | Maximum length for Push event extended data keys |

# SCE\_NP\_WEBAPI2\_NP\_SERVICE\_NAME\_NONE

Constant indicating that there is no NP service name

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_NP_SERVICE_NAME_NONE` | NULL | There is no NP service name |

## Description

This constant is used to create an event filter for Push events that do not have an NP service name.

# SCE\_NP\_WEBAPI2\_PUSH\_EVENT\_DATA\_TYPE\_LEN\_MAX

Maximum length of Push event data types

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_PUSH_EVENT_DATA_TYPE_LEN_MAX` | 64 | Maximum length of Push event data types |

# SCE\_NP\_WEBAPI2\_PUSH\_EVENT\_UUID\_LENGTH

Maximum length for UUIDs indicating Push context IDs

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_PUSH_EVENT_UUID_LENGTH` | 36 | Maximum length for UUIDs indicating Push context IDs |

# Return Codes

List of return codes returned by the NpWebApi2 library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_WEBAPI2_ERROR_OUT_OF_MEMORY` | 0x80553401 | Insufficient memory |
| `SCE_NP_WEBAPI2_ERROR_INVALID_ARGUMENT` | 0x80553402 | Argument is invalid |
| `SCE_NP_WEBAPI2_ERROR_INVALID_LIB_CONTEXT_ID` | 0x80553403 | Library context ID is invalid |
| `SCE_NP_WEBAPI2_ERROR_LIB_CONTEXT_NOT_FOUND` | 0x80553404 | Library context could not be found |
| `SCE_NP_WEBAPI2_ERROR_USER_CONTEXT_NOT_FOUND` | 0x80553405 | User context could not be found |
| `SCE_NP_WEBAPI2_ERROR_REQUEST_NOT_FOUND` | 0x80553406 | Request could not be found |
| `SCE_NP_WEBAPI2_ERROR_NOT_SIGNED_IN` | 0x80553407 | Function to be executed during a signed-in state was executed during a non-signed in state |
| `SCE_NP_WEBAPI2_ERROR_INVALID_CONTENT_PARAMETER` | 0x80553408 | Content parameter is invalid |
| `SCE_NP_WEBAPI2_ERROR_ABORTED` | 0x80553409 | Processing was aborted |
| `SCE_NP_WEBAPI2_ERROR_USER_CONTEXT_ALREADY_EXIST` | 0x8055340a | User context generated with the specified online ID already exists |
| `SCE_NP_WEBAPI2_ERROR_HANDLE_NOT_FOUND` | 0x8055340d | Handle was not found |
| `SCE_NP_WEBAPI2_ERROR_SIGNED_IN_USER_NOT_FOUND` | 0x8055340e | Signed in user was not found |
| `SCE_NP_WEBAPI2_ERROR_LIB_CONTEXT_BUSY` | 0x8055340f | Library context is being used and termination processing cannot be carried out |
| `SCE_NP_WEBAPI2_ERROR_USER_CONTEXT_BUSY` | 0x80553410 | User context is being used and cannot be deleted |
| `SCE_NP_WEBAPI2_ERROR_REQUEST_BUSY` | 0x80553411 | Request is being used and cannot be deleted |
| `SCE_NP_WEBAPI2_ERROR_INVALID_HTTP_STATUS_CODE` | 0x80553412 | HTTP status code is invalid |
| `SCE_NP_WEBAPI2_ERROR_PROHIBITED_HTTP_HEADER` | 0x80553413 | Specified an HTTP header for which specification is prohibited (not used) |
| `SCE_NP_WEBAPI2_ERROR_PROHIBITED_FUNCTION_CALL` | 0x80553414 | Executed a function for which usage is prohibited (not used) |
| `SCE_NP_WEBAPI2_ERROR_MULTIPART_PART_NOT_FOUND` | 0x80553415 | The part of the multipart specified by the part index number does not exist (not used) |
| `SCE_NP_WEBAPI2_ERROR_PARAMETER_TOO_LONG` | 0x80553416 | Specified parameter is too long |
| `SCE_NP_WEBAPI2_ERROR_HANDLE_BUSY` | 0x80553417 | Handle is being used and cannot be deleted |
| `SCE_NP_WEBAPI2_ERROR_LIB_CONTEXT_MAX` | 0x80553418 | Cannot create any more library contexts |
| `SCE_NP_WEBAPI2_ERROR_USER_CONTEXT_MAX` | 0x80553419 | Cannot create any more user contexts |
| `SCE_NP_WEBAPI2_ERROR_AFTER_SEND` | 0x8055341a | Send processing has already been started |
| `SCE_NP_WEBAPI2_ERROR_TIMEOUT` | 0x8055341b | Processing timed out |
| `SCE_NP_WEBAPI2_ERROR_PUSH_CONTEXT_NOT_FOUND` | 0x8055341c | Push context was not found |

In addition to the above error codes, `sceNpWebApi2SendRequest()` return an error code starting with 0x82. An error code starting with 0x82 indicates a server error; the lower 24 bits excluding 0x82 of this error code expressed as a decimal number serves as the value for determining the specific server error. Refer to the Web API documents for server error definitions.