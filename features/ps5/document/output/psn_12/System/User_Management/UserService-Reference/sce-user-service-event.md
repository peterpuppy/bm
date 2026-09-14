# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-event.html

# Login/Logout Detection

# SceUserServiceEvent

Structure that holds a UserService event

## Definition

```
#include <user_service.h>
typedef struct SceUserServiceEvent {
	SceUserServiceEventType event;
	SceUserServiceUserId userId;
} SceUserServiceEvent;
```

## Members

|  |  |
| --- | --- |
| `event` | Event type |
| `userId` | User ID |

## Description

This structure is used for receiving the results when obtaining a UserService event with `sceUserServiceGetEvent()`.

# SceUserServiceEventType

enum constants that indicate UserService event types

## Definition

```
#include <user_service.h>
typedef enum SceUserServiceEventType {
	(Omitted: see details below)
} SceUserServiceEventType;
```

## Description

These are enum constants that indicate the UserService event types.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_EVENT_TYPE_LOGIN` | 0 | Login event |
| `SCE_USER_SERVICE_EVENT_TYPE_LOGOUT` | 1 | Logout event |

## See Also

`sceUserServiceGetEvent()`, `SceUserServiceEvent`

# sceUserServiceGetEvent

Gets a UserService event

## Definition

```
#include <user_service.h>
int32_t sceUserServiceGetEvent(
	SceUserServiceEvent *event
)
```

## Arguments

|  |  |
| --- | --- |
| `event` | Destination to store the obtained UserService event |

## Return Values

Stores the obtained event in `*event` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (negative value) for errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |
| `SCE_USER_SERVICE_ERROR_NO_EVENT` | 0x80960007 | No unobtained UserService event exists |

## Description

This function obtains a UserService event.

For `event`, specify a pointer to the `SceUserServiceEvent` structure to store a UserService event.

It is recommended that this function is called once for every Vsync on screens where increases/decreases in users should be monitored. Note that even when multiple UserService events occur at the same time, this function will only obtain them one at a time; therefore, call this function repeatedly until `SCE_USER_SERVICE_ERROR_NO_EVENT` is returned.

## Examples

```
// Call this function in the main loop
int32_t CheckEvents()
{
    int32_t ret;
    SceUserServiceEvent event;
    for (;;) {
        ret = sceUserServiceGetEvent(&event);
        if (ret == SCE_OK) {
            if (event.eventType == SCE_USER_SERVICE_EVENT_TYPE_LOGIN) {
                // Login processing
            } else if (event.eventType == SCE_USER_SERVICE_EVENT_TYPE_LOGOUT) {
                // Logout processing
            }
        } else if (ret == SCE_USER_SERVICE_ERROR_NO_EVENT) {
            break;
        } else {
            // Error handling
            break;
        }
    }
    return ret;
}
```

## Notes

Perform logout event handling if it is required for the application. Even if it is not performed, controller and headset input from a user will no longer be obtainable when that user logs out, and handling of information linked to that user (such as the saving of save data and PlayStation™Network related processing) will fail.