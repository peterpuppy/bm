# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-destroy-event.html

# Creating and Manipulating Events

# SceNpUniversalDataSystemEvent

Event

## Definition

```
#include <np.h>
typedef struct SceNpUniversalDataSystemEvent SceNpUniversalDataSystemEvent;
```

## Description

This structure represents a single event.

Refer to [NpUniversalDataSystem Library Overview - Using the Library - Sending Events](../NpUniversalDataSystem-Overview/sending-events.html) for the typical procedure to create and send an event.

## See Also

`sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemDestroyEvent()`, `sceNpUniversalDataSystemPostEvent()`

# sceNpUniversalDataSystemCreateEvent

Create an event

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemCreateEvent(
    const char *eventName,
    const SceNpUniversalDataSystemEventPropertyObject *prop,
    SceNpUniversalDataSystemEvent **newEvent,
    SceNpUniversalDataSystemEventPropertyObject **propPtr
)
```

## Arguments

|  |  |
| --- | --- |
| `eventName` | [In] Event name (UTF-8) |
| `prop` | [In] Object of all properties to set, or NULL |
| `newEvent` | [Out] Destination to store the pointer to the created event |
| `propPtr` | [Out] Destination to store the set property object, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT_NAME` | 0x8055310d | Invalid event name |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_EXCEEDS_EVENT_DATA_SIZE_LIMIT` | 0x80553113 | Exceeds the maximum event size (20 KiB) |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function creates an event with the event name specified to `eventName`.

For `prop`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified. The same operation as when an empty object is specified will be applied when NULL is specified.

Because the object of the property specified as `prop` will be copied entirely (including its child elements) to the event, it is not a problem to delete the object after this function is called.

For `propPtr`, a pointer to all the properties copied to the event will be stored. Specify it when you want to make changes to properties after event creation. Specify NULL for `propPtr` if this is not required.

## Notes

It is not a problem to add an element to the object type value pointed to by `propPtr` using `sceNpUniversalDataSystemEventPropertyObjectSetString()` or another function; however, the object type value cannot be deleted using `sceNpUniversalDataSystemDestroyEventPropertyObject()`.

## Examples

```
SceNpUniversalDataSystemEvent *event = NULL;
SceNpUniversalDataSystemEventPropertyObject *tmpProp;
SceNpUniversalDataSystemEventPropertyObject *prop;
int ret;

ret = sceNpUniversalDataSystemCreateEventPropertyObject(&tmpProp);
if (ret < 0) {
    // Error handling
}

ret = sceNpUniversalDataSystemCreateEvent("event_name", tmpProp, &event, &prop);
if (ret < 0) {
    // Error handling
}
```

## See Also

`sceNpUniversalDataSystemDestroyEvent()`

# sceNpUniversalDataSystemDestroyEvent

Destroy an event

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemDestroyEvent(
    SceNpUniversalDataSystemEvent *event
)
```

## Arguments

|  |  |
| --- | --- |
| `event` | [In] Event to destroy, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function destroys the event specified in `event`.

For `event`, specify a pointer to `SceNpUniversalDataSystemEvent` obtained with `sceNpUniversalDataSystemCreateEvent()` or specify NULL. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEvent` is specified. This function will not do anything and terminate normally when NULL is specified for `event`.

# sceNpUniversalDataSystemEventEstimateSize

Obtain the event size

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventEstimateSize(
    const SceNpUniversalDataSystemEvent *event,
    size_t *size
)
```

## Arguments

|  |  |
| --- | --- |
| `event` | [In] Event |
| `size` | [Out] Destination to store the obtained event size |

## Return Values

Stores the obtained event size in `*size` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_EVENT` | 0x80553116 | Invalid event |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function calculates the data size of the event specified in `event` after serialization. The library adds information to an event when the event is serialized in preparation of a send. Because of this, the event size will become larger than the total size of the event name and properties specified by the application. Call this function to confirm the data size of an event after serialization.

For `event`, specify a pointer to `SceNpUniversalDataSystemEvent` obtained with `sceNpUniversalDataSystemCreateEvent()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEvent` is specified.

For `size`, the calculated data size (bytes) will be stored.

## Notes

* The size of an event after serialization that can be manipulated by the NpUniversalDataSystem library is 20 KiB at maximum.
* This function does not check the validity of an event.

## See Also

`sceNpUniversalDataSystemCreateEvent()`