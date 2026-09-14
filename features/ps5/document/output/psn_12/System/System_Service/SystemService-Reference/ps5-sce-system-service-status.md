# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-status.html

# Obtaining Information for Each Rendering Frame

# sceSystemServiceGetStatus

Get information required for each rendering frame

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceGetStatus(
	SceSystemServiceStatus* status
);
```

## Arguments

|  |  |
| --- | --- |
| `status` | Structure to store information |

## Return Values

Stores the obtained information in `*status` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function collects and obtains information that the application should obtain from the system software for each rendering frame.

# SceSystemServiceStatus

Structure collecting information that should be obtained for each rendering frame

## Definition

```
#include <system_service.h>
typedef struct _SceSystemServiceStatus {
	int32_t eventNum;
	bool isSystemUiOverlaid;
	bool isInBackgroundExecution;
	bool isVrPlayAreaBoundaryOverlaid;
	uint8_t reserved[];
} SceSystemServiceStatus;
```

## Members

|  |  |
| --- | --- |
| `eventNum` | Number of events that can be received with `sceSystemServiceReceiveEvent()` |
| `isSystemUiOverlaid` | Flag indicating whether the system software UI is being overlaid |
| `isInBackgroundExecution` | Flag indicating whether the application is running in the background |
| `isVrPlayAreaBoundaryOverlaid` | Flag indicating whether the VR play area boundary is displayed |
| `reserved` | Reserved area |

## Description

This structure is used when obtaining information with `sceSystemServiceGetStatus()`.

# sceSystemServiceReceiveEvent

Receive information about event that occurred outside the application

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceReceiveEvent(
	SceSystemServiceEvent* event
);
```

## Arguments

|  |  |
| --- | --- |
| `event` | Structure to store event information |

## Return Values

Stores the obtained information in `*event` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_NO_EVENT` | 0x80A10004 | No events that should be received |
| Other errors | Negative value | Fatal error |

## Description

This function can receive information about an event when an event related to an application occurs outside the application.

## Examples

```
SceSystemServiceStatus status;
SceSystemServiceEvent event;

ret = sceSystemServiceGetStatus(&status);
if ((ret == SCE_OK) && (status.eventNum > 0))
{
    for (int i = 0; i < status.eventNum; i++)
    {
        ret = sceSystemServiceReceiveEvent(&event);
        if (ret == SCE_OK) {
            switch(event.eventType) {
            case SCE_SYSTEM_SERVICE_EVENT_ON_RESUME: 
                {
                    // Processing after resuming
                }
                break;
            }
        }
    }
}
```

# SceSystemServiceEvent

Structure to store event information

## Definition

```
#include <system_service.h>
typedef struct _SceSystemServiceEvent {
	SceSystemServiceEventType eventType;
	union {
		char param[8192];
		uint8_t reserved[8192];
		struct {
			SceUserServiceUserId userId;
			uint32_t npServiceLabel;
			uint8_t reserved[8184];
		} serviceEntitlementUpdate;
		struct {
			SceUserServiceUserId userId;
			uint32_t npServiceLabel;
			uint8_t reserved[8184];
		} unifiedEntitlementUpdate;
		struct {
			uint8_t data[8];
			uint8_t reserved[8184];
		} avContentCreated;
	} data;
} SceSystemServiceEvent;
```

## Members

|  |  |
| --- | --- |
| `eventType` | Value indicating event type |
| `data.param` | Parameters associated with event |
| `data.reserved` | Reserved area |
| `data.serviceEntitlementUpdate.userId` | User ID for user with updated service entitlement |
| `data.serviceEntitlementUpdate.npServiceLabel` | NP service label for updated service entitlement |
| `data.serviceEntitlementUpdate.reserved` | Reserved area |
| `data.unifiedEntitlementUpdate.userId` | User ID of the user whose unified entitlement was updated |
| `data.unifiedEntitlementUpdate.npServiceLabel` | NP service label for updated unified entitlement |
| `data.unifiedEntitlementUpdate.reserved` | Reserved area |
| `data.avContentCreated.data` | Data related to the registered AV content |
| `data.avContentCreated.reserved` | Reserved area |

## Description

This structure is used when receiving an event with `sceSystemServiceReceiveEvent()`.

## See Also

`sceSystemServiceGetStatus()`

# SceSystemServiceEventType

Types indicating event type

## Definition

```
#include <system_service.h>
typedef enum SceSystemServiceEventType;
```

## Description

These types indicate the type of event received with `sceSystemServiceReceiveEvent()`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_EVENT_ON_RESUME` | 0x10000000 | Application resumed |
| `SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE` | 0x10000003 | Additional content entitlement was updated |
| `SCE_SYSTEM_SERVICE_EVENT_ADDCONTENT_INSTALL` | 0x10000009 | Additional content was installed |
| `SCE_SYSTEM_SERVICE_EVENT_RESET_VR_POSITION` | 0x1000000a | A reset of tracking information was requested |
| `SCE_SYSTEM_SERVICE_EVENT_PLAYGO_LOCUS_UPDATE` | 0x1000000c | PlayGo chunk state changed |
| `SCE_SYSTEM_SERVICE_EVENT_SERVICE_ENTITLEMENT_UPDATE` | 0x1000000e | Service entitlement was updated |
| `SCE_SYSTEM_SERVICE_EVENT_GAME_INTENT` | 0x10000017 | Game intent event occurred |
| `SCE_SYSTEM_SERVICE_EVENT_UNIFIED_ENTITLEMENT_UPDATE` | 0x10000018 | Unified entitlement was updated |
| `SCE_SYSTEM_SERVICE_EVENT_PLAYGO_CHUNK_ADDED` | 0x10000019 | Installable chunk added |
| `SCE_SYSTEM_SERVICE_EVENT_AVCONTENT_CREATED` | 0x1000001d | AV content was registered |

* For details about `SCE_SYSTEM_SERVICE_EVENT_ADDCONTENT_INSTALL`, refer to the [AppContent Library Overview](../AppContent-Overview/__document_toc.html) document.
* For details about `SCE_SYSTEM_SERVICE_EVENT_RESET_VR_POSITION`, refer to the [VrTracker2 Library Overview](../VrTracker2-Overview/__document_toc.html) document.
* For details about `SCE_SYSTEM_SERVICE_EVENT_PLAYGO_LOCUS_UPDATE` and `SCE_SYSTEM_SERVICE_EVENT_PLAYGO_CHUNK_ADDED`, refer to the [PlayGo Library Overview](../PlayGo-Overview/__document_toc.html) document.
* For details about `SCE_SYSTEM_SERVICE_EVENT_GAME_INTENT`, refer to the [NpGameIntent Library Overview](../NpGameIntent-Overview/__document_toc.html) document. In addition, refer to the [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html) document for details about the game intent feature.
* For details about `SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE`, `SCE_SYSTEM_SERVICE_EVENT_SERVICE_ENTITLEMENT_UPDATE`, and `SCE_SYSTEM_SERVICE_EVENT_UNIFIED_ENTITLEMENT_UPDATE`, refer to the [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html) document.
* For details about `SCE_SYSTEM_SERVICE_EVENT_AVCONTENT_CREATED`, refer to the [ContentSearch Library Overview](../ContentSearch-Overview/__document_toc.html) document.

## See Also

`SceSystemServiceEvent`