# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-destroy-context.html

# Contexts

# SceNpUniversalDataSystemContext

Context

## Definition

```
#include <np.h>
#define SCE_NP_UNIVERSAL_DATA_SYSTEM_INVALID_CONTEXT (-1)
typedef int32_t SceNpUniversalDataSystemContext;
```

## Description

This is the datatype that represents a context. A context includes information that identifies the user who sent an event.

A context created in advance with `sceNpUniversalDataSystemCreateContext()` and registered with `sceNpUniversalDataSystemRegisterContext()` must be passed as an argument for most NpUniversalDataSystem library functions.

## See Also

`sceNpUniversalDataSystemDestroyContext()`

# sceNpUniversalDataSystemCreateContext

Create a context

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemCreateContext(
    SceNpUniversalDataSystemContext *context,
    SceUserServiceUserId userId,
    SceNpServiceLabel serviceLabel,
    uint64_t options
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [Out] Destination to store the created context |
| `userId` | [In] User ID |
| `serviceLabel` | [In] NP service label |
| `options` | [In] Options (reserved for extension: always specify 0) |

## Return Values

Stores the created context in `*context` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_CONTEXT_EXCEEDS_MAX` | 0x80553105 | Exceeded the maximum number of contexts (8) |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_USER` | 0x8055310a | Invalid user |

In addition, there is a possibility that an error code relating to user management will be returned. (Refer to the [Error Codes Related to User Management](../Error_Codes_Related_to_User_Management-Reference/__document_toc.html) document for details.) The application must not malfunction even if error codes that are not listed above are returned.

## Description

This function creates a context to be used when calling an NpUniversalDataSystem library function.

## Examples

```
extern SceUserServiceUserId userId;
extern SceNpServiceLabel serviceLabel;
SceNpUniversalDataSystemContext context = SCE_NP_UNIVERSAL_DATA_SYSTEM_INVALID_CONTEXT;
int ret;

ret = sceNpUniversalDataSystemCreateContext(&context, userId, serviceLabel, 0);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

It is recommended that a context be used as long as possible without deleting it while an application is running. Normally, a context is created and registered when a user logs in and joins a game. The context is then destroyed when the user quits the game or when the user logs out.

## See Also

`sceNpUniversalDataSystemRegisterContext()`, `sceNpUniversalDataSystemDestroyContext()`

# sceNpUniversalDataSystemRegisterContext

Register a context

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemRegisterContext(
    SceNpUniversalDataSystemContext context,
    SceNpUniversalDataSystemHandle handle,
    uint64_t options
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context to register |
| `handle` | [In] Handle |
| `options` | [In] Options (reserved for extension: always specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_ALREADY_REGISTERED` | 0x80553121 | Context is already registered |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NP_BIND_DAT_NOT_FOUND` | 0x80553123 | npbind.dat cannot be found |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_CONF_NOT_FOUND` | 0x8055b75b | uds00.ucp cannot be found |

## Description

This function registers a context. This function must be called before an event is posted.

Before context registration, a check is performed in this function to see if UDS configuration information and UDS Stats data files are installed. If UDS Stats data files are installed, this function checks for data corruption and whether there is a need to update the file version. UDS Stats data files will be installed, re-installed, and updated as necessary before a context is registered. This function also entails setup processing of features that run in coordination with UDS (example: trophy-related features).

It is recommended that a context be used as long as possible without deleting it while an application is running. Normally, a context is created and registered when a user logs in and joins a game. The context is then destroyed when the user quits the game or when the user logs out.

## Notes

* A context will be invalidated when the user linked to the context logs out. The invalidated context cannot be used even if the same user logs in again. It must be deleted with `sceNpUniversalDataSystemDestroyContext()`, and a new context must be created and registered again.
* When the application is launched from the package installed on the console and this function causes an error, the system will display the error code and terminate the application. The application will not be terminated if it was launched from the debugger or workspace, but the error code will be displayed by the notification feature.
* A misalignment may occur with existing data upon updating uds00.ucp in the development environment and may cause this function to generate an error. In such cases, the problem can be resolved by deleting UDS-related data. For details, refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html).
* This is a blocking function. Call this function from a subthread as processing may take time. This function must not be called from a time-critical thread.

## See Also

`sceNpUniversalDataSystemCreateContext()`

# sceNpUniversalDataSystemDestroyContext

Destroy a context

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemDestroyContext(
    SceNpUniversalDataSystemContext context
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_CONTEXT` | 0x80553104 | Invalid context |

## Description

This function destroys the context specified with `context` and frees the internal resources.

## Notes

It is recommended that a context be used as long as possible without deleting it while an application is running. Normally, the context is destroyed when the user logs out or when the user quits the game.

## See Also

`sceNpUniversalDataSystemCreateContext()`