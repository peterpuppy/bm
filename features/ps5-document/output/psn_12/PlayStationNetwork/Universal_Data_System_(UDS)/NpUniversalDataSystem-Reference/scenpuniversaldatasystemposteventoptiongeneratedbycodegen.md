# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/scenpuniversaldatasystemposteventoptiongeneratedbycodegen.html

# Posting Events

# SCE\_NP\_UNIVERSAL\_DATA\_SYSTEM\_POST\_EVENT\_OPTION\_GENERATED\_BY\_CODEGEN

Value that indicates a call from source code that was generated using np-universal-data-system-codegen.exe

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_POST_EVENT_OPTION_GENERATED_BY_CODEGEN` | 1 | This value is specified for the `options` argument of `sceNpUniversalDataSystemPostEvent()` by source code that was generated using np-universal-data-system-codegen.exe. The value has no practical effect on the behavior of `sceNpUniversalDataSystemPostEvent()`. |

## See Also

`sceNpUniversalDataSystemPostEvent()`

# sceNpUniversalDataSystemPostEvent

Post an event

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemPostEvent(
    SceNpUniversalDataSystemContext context,
    SceNpUniversalDataSystemHandle handle,
    const SceNpUniversalDataSystemEvent *event,
    uint64_t options
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `event` | [In] Event to post |
| `options` | [In] Options (reserved for extension: typically specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_CONTEXT` | 0x80553104 | Invalid context |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_HANDLE` | 0x80553106 | Invalid handle |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_USER` | 0x8055310a | Invalid user |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_USER_NOT_LOGGED_IN` | 0x8055310b | User is not logged in |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_NAME` | 0x8055310d | Invalid event name |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_PROPERTY_KEY` | 0x8055310e | Invalid event property key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_PROPERTY_VALUE` | 0x8055310f | Invalid event property value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_DATA_CORRUPTED` | 0x80553111 | Temporary file is corrupted |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_EXCEEDS_EVENT_DATA_SIZE_LIMIT` | 0x80553113 | Exceeds the maximum event size (20 KiB) |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT` | 0x80553116 | Invalid event |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_REGISTERED` | 0x80553120 | Context is not registered |

## Description

This function posts the event specified in `event` to the context specified in `context`.

For `event`, specify a pointer to `SceNpUniversalDataSystemEvent` obtained with `sceNpUniversalDataSystemCreateEvent()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEvent` is specified.

The user posting an event must be logged in to the PlayStation®5 system.

## Examples

```
extern SceNpUniversalDataSystemContext context;
extern SceNpUniversalDataSystemHandle handle;

SceNpUniversalDataSystemEvent *event = NULL;
int ret;

ret = sceNpUniversalDataSystemCreateEvent("event_name", NULL, &event, NULL);
if (ret < 0) {
    // Error handling
}

ret = sceNpUniversalDataSystemPostEvent(context, handle, event, 0);
if (ret < 0) {
    // Error handling
}

ret = sceNpUniversalDataSystemDestroyEvent(event);
if (ret < 0) {
    // Error handling
}
```

## Notes

* The posted event will be stored temporarily on the internal SSD when this function is called. The stored event will be sent to the PlayStation™Network server by the system software asynchronously.
* This function blocks until write to the internal SSD completes but it does not wait for the event to be sent over the network. UDS events written to the internal SSD are sequentially sent to the server in the background while the application is running. If there is no network connection or if the user is not signed in to PlayStation™Network, the UDS events will be sent after the console is able to communicate with the server.
* If the call rate limit (300 times in 5 minutes) is exceeded, a notification is displayed. Events posted in excess of the rate limit may be discarded, so implement your application so that this limit will not be exceeded. Note that it is also possible to configure a setting so that notifications are not displayed even if the rate limit is exceeded. For details, refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html).
* This is a blocking function. Call this function from a subthread as processing may take time. This function must not be called from a time-critical thread.
* Source code that was generated using np-universal-data-system-codegen.exe specifies `SCE_NP_UNIVERSAL_DATA_SYSTEM_POST_EVENT_OPTION_GENERATED_BY_CODEGEN` for the `options` argument of this function. There is no practical difference in the behavior of the function compared to when 0 is specified, so such source code may be used without modification.

## See Also

`sceNpUniversalDataSystemCreateHandle()`, `sceNpUniversalDataSystemCreateContext()`