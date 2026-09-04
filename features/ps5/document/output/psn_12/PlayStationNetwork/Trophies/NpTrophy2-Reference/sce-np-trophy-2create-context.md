# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/sce-np-trophy-2create-context.html

# Contexts

# SceNpTrophy2Context

Trophy context

## Definition

```
#include <np.h>
#define SCE_NP_TROPHY2_INVALID_CONTEXT (-1)
typedef int32_t SceNpTrophy2Context;
```

## Description

This is the datatype that represents the trophy context. The trophy context includes the NP service label that identifies trophy configuration data and information that represents a user for identification of the trophy record.

Most NpTrophy2 library functions require calling `sceNpTrophy2CreateContext()` in advance to create a context, calling `sceNpTrophy2RegisterContext()` to register it, and then passing the context as an argument.

## See Also

`sceNpTrophy2DestroyContext()`

# sceNpTrophy2CreateContext

Create a context

## Definition

```
#include <np.h>
int sceNpTrophy2CreateContext(
    SceNpTrophy2Context *context,
    SceUserServiceUserId userId,
    SceNpServiceLabel serviceLabel,
    uint64_t options
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Destination to store the created context |
| `userId` | [In] User ID |
| `serviceLabel` | [In] Np service label |
| `options` | [In] Options (reserved for future use: always specify 0) |

## Return Values

Stores the created context in `*context` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_CONTEXT_ALREADY_EXISTS` | 0x80553910 | Context already exists  There is a possibility that multiple contexts have been created for a single NP service label/user. |
| `SCE_NP_TROPHY2_ERROR_CONTEXT_EXCEEDS_MAX` | 0x8055391B | Exceeded the maximum number of contexts (8) |

## Description

This function creates a context to be used when calling an NpTrophy2 library function. Use the created context after registering it with `sceNpTrophy2RegisterContext()`.

The created context can be used until it is deleted by `sceNpTrophy2DestroyContext()` or the user logs out. Even when a handle is aborted, there is no need to delete the context.

## Examples

```
extern SceUserServiceUserId userId;
extern SceNpServiceLabel serviceLabel;

SceNpTrophy2Context context = SCE_NP_TROPHY2_INVALID_CONTEXT;
int ret;

ret = sceNpTrophy2CreateContext(&context, userId, serviceLabel, 0);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

It is recommended that a context be used without deleting it for as long as possible while the application is being used.

Normally, a context is created when a user logs in and joins a game, and the context is registered with `sceNpTrophy2RegisterContext()`.

Then when the user quits the game or when the user logs out, the context is destroyed.

# sceNpTrophy2DestroyContext

Destroy a context

## Definition

```
#include <np.h>
int sceNpTrophy2DestroyContext(
    SceNpTrophy2Context context
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_CONTEXT` | 0x80553909 | Invalid context |

## Description

This function destroys the context specified with `context` and frees the internal resources.

## Notes

It is recommended that a context be used without deleting it for as long as possible while the application is being used. Normally, the context is destroyed when the user logs out or when the user quits the game.

# sceNpTrophy2RegisterContext

Register context

## Definition

```
#include <np.h>
int sceNpTrophy2RegisterContext(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    uint64_t options
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context to register |
| `handle` | [In] Handle |
| `options` | [In] Options (reserved for future use: always specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_CONTEXT` | 0x80553909 | Invalid context |
| `SCE_NP_TROPHY2_ERROR_ALREADY_REGISTERED` | 0x80553921 | Context is already registered |
| `SCE_NP_TROPHY2_ERROR_TITLE_CONF_NOT_INSTALLED` | 0x8055391e | Trophy configuration data is not installed.  Confirm that the trophy configuration files are in the correct place. |
| `SCE_NP_TROPHY2_ERROR_UCP_FILE_MODE_MISMATCH` | 0x805539cc | The Universal Data System Development Mode settings and the trophy configuration file format do not match.  Make sure that you have not renamed trophy00\_local.ucp to trophy00.ucp or vice versa. |

## Description

This function registers a context. This function must be called before obtaining trophy data.

Before registering a context, a check is performed for whether or not the trophy configuration data and trophy record files are installed. If a trophy record file is already installed, a data corruption check and version update requirement check will be performed. After installation, re-installation, and update processing is performed on the trophy record file as required, the context will be registered. Additionally, the Universal Data System, which is used by the trophy system, will be set up.

## Notes

* A context will become invalid when the user linked to the context logs out. Even if the user later logs in again, it will not be possible to continue to use the invalid context. The context must first be destroyed with `sceNpTrophy2DestroyContext()`, and then a new context must be created.
* This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`