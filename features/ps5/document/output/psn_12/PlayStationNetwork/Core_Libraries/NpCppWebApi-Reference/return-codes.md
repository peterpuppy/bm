# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/return-codes.html

# Common Constants

# SCE\_NP\_CPPWEBAPI\_\*

Minimum and maximum values for the sizes of various data

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_CPPWEBAPI_THREAD_STACK_SIZE_DEFAULT` | 32 \* 1024 | Default thread stack size |
| `SCE_NP_CPPWEBAPI_MEMORY_POOL_SIZE_DEFAULT` | 512 \* 1024 | Default memory pool size |

## Description

These constants are used for specifying the default or minimum/maximum values for the sizes of various data used by the NpCppWebApi library.

# Return Codes

Return codes returned by the NpCppWebApi library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_CPPWEBAPI_ERROR_UNKNOWN` | 0x80553501 | Unknown error |
| `SCE_NP_CPPWEBAPI_ERROR_NOT_INITIALIZED` | 0x80553502 | Not initialized |
| `SCE_NP_CPPWEBAPI_ERROR_INVALID_ARGUMENT` | 0x80553503 | Invalid argument |
| `SCE_NP_CPPWEBAPI_ERROR_OUT_OF_MEMORY` | 0x80553504 | Not enough memory.  The value of `sce::Np::CppWebApi::Common::InitParams::poolSize` set upon initializing the library is insufficient, or a memory allocator has not been set to the Json2 library. |
| `SCE_NP_CPPWEBAPI_ERROR_PARSE_FAILURE` | 0x80553505 | Parse failure |
| `SCE_NP_CPPWEBAPI_ERROR_CHILD_CLASS_MISMATCH` | 0x80553506 | Child class mismatch (unused) |
| `SCE_NP_CPPWEBAPI_ERROR_CALLBACK_ALREADY_SET` | 0x80553507 | Callback is already set |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_NOT_AVAILABLE` | 0x80553508 | Transaction cannot be used |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_ALREADY_STARTED` | 0x80553509 | Transaction already started |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_ALREADY_ABORTED` | 0x8055350a | Transaction already aborted |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_ALREADY_IN_USE` | 0x8055350b | Transaction already in use |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_FINISHED` | 0x8055350c | Transaction finished |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_ABORTED` | 0x8055350d | Transaction aborted |
| `SCE_NP_CPPWEBAPI_ERROR_TERMINATING` | 0x8055350e | Library is being terminated |
| `SCE_NP_CPPWEBAPI_ERROR_PARAMETER_ALREADY_INITIALIZED` | 0x8055350f | Parameter already initialized |
| `SCE_NP_CPPWEBAPI_ERROR_PARAMETER_NOT_INITIALIZED` | 0x80553510 | Parameter not initialized |
| `SCE_NP_CPPWEBAPI_ERROR_LIBCONTEXT_ALREADY_INITIALIZED` | 0x80553511 | Library context already initialized |
| `SCE_NP_CPPWEBAPI_ERROR_INSTANTIATED_OBJECT_REQUIRED` | 0x80553512 | Instantiated object required |
| `SCE_NP_CPPWEBAPI_ERROR_STREAM_TRANSACTION_BUSY` | 0x80553513 | Stream transaction is being processed |
| `SCE_NP_CPPWEBAPI_ERROR_REQUIRED_PROPERTY_NOT_PROVIDED` | 0x80553514 | Required property not provided |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_ALREADY_PROCESSED` | 0x80553515 | Transaction has already been processed |
| `SCE_NP_CPPWEBAPI_ERROR_INVAILD_LIBCONTEXT` | 0x80553516 | Invalid library context |
| `SCE_NP_CPPWEBAPI_ERROR_HEADER_FIELD_NOT_FOUND` | 0x80553517 | Specified header field cannot be found |
| `SCE_NP_CPPWEBAPI_ERROR_STREAM_TRANSACTION_NOT_YET_SENT_DATA` | 0x80553518 | Data hasn't been sent yet using a stream transaction |
| `SCE_NP_CPPWEBAPI_ERROR_UNSUPPORTED` | 0x80553519 | Unsupported usage (Example: A value of 2 or greater is specified for `sce::Np::CppWebApi::Common::InitParams::numWorkers`) |
| `SCE_NP_CPPWEBAPI_ERROR_STRING_REPLACE_OUT_OF_RANGE` | 0x8055351a | An area outside the valid range was specified upon replacing the string |
| `SCE_NP_CPPWEBAPI_ERROR_TRANSACTION_BEFORE_CALL_WEBAPI` | 0x8055351b | State before the transaction calls a web API call function |