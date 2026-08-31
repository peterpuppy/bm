# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/return-codes.html

# Common Constants

# SCE\_NP\_UNIVERSAL\_DATA\_SYSTEM\_EVENT\_DATA\_SIZE\_MAX

Maximum event size for the NpUniversalDataSystem library

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_EVENT_DATA_SIZE_MAX` | 20480 | Maximum size for an event that can be posted with the NpUniversalDataSystem library |

## See Also

`sceNpUniversalDataSystemEventEstimateSize()`

# Return Codes

List of return codes returned by the NpUniversalDataSystem library

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_UNKNOWN` | 0x80553100 | Undefined error, not listed below |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_SHUTDOWN` | 0x80553103 | System is shutting down |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_CONTEXT` | 0x80553104 | Invalid context |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_CONTEXT_EXCEEDS_MAX` | 0x80553105 | Exceeded the maximum number of contexts |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_HANDLE` | 0x80553106 | Invalid handle |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_HANDLE_EXCEEDS_MAX` | 0x80553107 | Exceeded the maximum number of handles |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_BUSY` | 0x80553108 | (Deprecated: This error code is defined but will not be returned) |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_ABORT` | 0x80553109 | Handle has been aborted |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_USER` | 0x8055310a | Invalid user |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_USER_NOT_LOGGED_IN` | 0x8055310b | User is not logged in |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_NAME` | 0x8055310d | Invalid event name |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_PROPERTY_KEY` | 0x8055310e | Invalid event property key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_PROPERTY_VALUE` | 0x8055310f | Invalid event property value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_DATA_CORRUPTED` | 0x80553111 | Temporary file is corrupted |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_SIZE` | 0x80553112 | Structure size specified for the `size` member of the structure is invalid |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_EXCEEDS_EVENT_DATA_SIZE_LIMIT` | 0x80553113 | Event data size exceeds the maximum size |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT` | 0x80553116 | Invalid event |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_ALREADY_INITIALIZED` | 0x80553118 | Already initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_REGISTERED` | 0x80553120 | Context is not registered |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_ALREADY_REGISTERED` | 0x80553121 | Context is already registered |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_NP_SERVICE_LABEL` | 0x80553122 | Invalid NP service label |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NP_BIND_DAT_NOT_FOUND` | 0x80553123 | npbind.dat cannot be found |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_PARAM_FILE_NOT_FOUND` | 0x80553124 | param.json cannot be found |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_SUPPORTED_APP` | 0x80553126 | Called from an unsupported application |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_NP_BIND` | 0x80553127 | npbind.dat is invalid |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_APP_RUNNING` | 0x80553128 | Operation that cannot be performed while an application is running |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_STATS_DATA_TYPE_MISMATCH` | 0x8055b74c | The type for existing data and the version-updated data doesn't match |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_CONF_NOT_FOUND` | 0x8055b75b | uds00.ucp cannot be found |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NP_BIND_LOCAL_NOT_FOUND` | 0x8055b775 | The console is set to UDS Local Mode but npbind\_local.json cannot be found |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_UCP_FILE_MODE_MISMATCH` | 0x8055b778 | The Universal Data System Development Mode setting doesn't match the ucp file |