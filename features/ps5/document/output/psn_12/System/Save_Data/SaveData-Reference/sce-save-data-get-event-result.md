# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-get-event-result.html

# Asynchronous Event Obtainment

# SceSaveDataEvent

Event results

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataEventType;

typedef struct SceSaveDataEvent {
	SceSaveDataEventType type;
	int32_t errorCode;
	SceUserServiceUserId userId;
	uint8_t padding[4];
	SceSaveDataTitleId titleId;
	SceSaveDataDirName dirName;
	uint8_t reserved[40];
} SceSaveDataEvent;
```

## Members

|  |  |
| --- | --- |
| `type` | Event type |
| `errorCode` | Error code |
| `userId` | User ID |
| `padding` | Padding (fill with 0's) |
| `titleId` | Save data title ID, or NULL |
| `dirName` | Save data directory name |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for obtaining event results with `sceSaveDataGetEventResult()`.

In `type`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_EVENT_TYPE_SAVE_DATA_MEMORY_SYNC_END` | 3 | Synchronization processing of `sceSaveDataSyncSaveDataMemory()` ended |
| `SCE_SAVE_DATA_EVENT_TYPE_CONVERT_END` | 5 | Conversion processing of `sceSaveDataConvert()` ended |

`SCE_OK` (=0) will be stored in `errorCode` when processing terminates normally.

One of the following error codes (a negative value) will be stored when an error occurs.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_NO_SPACE` | 0x809f0009 | Not enough free space in the conversion-source save data |
| `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` | 0x809f000a | Not enough free space in the file system to mount the save data |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_BROKEN` | 0x809f000f | Save data is corrupted |

`userId`, `titleId`, `dirName` will store information that identifies the save data that has been processed.

## Notes

Synchronization processing of save data memory may fail, but the application is not required to perform special handling of such cases. Make sure that application progress is not hindered even if a value other than `SCE_OK` is returned to `errorCode`.

The following errors may be returned in `errorCode` only if `type` is `SCE_SAVE_DATA_EVENT_TYPE_CONVERT_END` (event notification for save data conversion).

* `SCE_SAVE_DATA_ERROR_NO_SPACE`
* `SCE_SAVE_DATA_ERROR_NO_SPACE_FS`
* `SCE_SAVE_DATA_ERROR_BROKEN`

# sceSaveDataGetEventResult

Get event results

## Definition

```
#include <save_data.h>
typedef struct _SceSaveDataEventParam SceSaveDataEventParam;

int32_t sceSaveDataGetEventResult (
	const SceSaveDataEventParam *eventParam, 
	SceSaveDataEvent *event
)
```

## Arguments

|  |  |
| --- | --- |
| `eventParam` | Parameters for obtaining the result of the event (specify NULL) |
| `event` | Destination to store the obtained event results |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_NOT_FOUND` | 0x809f0008 | No events and no events being processed |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_EVENT_BUSY` | 0x809f0018 | Event is being processed and results are not available yet |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function is for obtaining as an event the synchronization processing results of `sceSaveDataSyncSaveDataMemory()` or the results of conversion processing performed by `sceSaveDataConvert()`. Make sure to call this function after confirming its return.

A maximum of 20 events are stored by the system. When the stored events exceed 20, they will be deleted starting with the oldest event.

Note that when `sceSaveDataTerminate()` is called, all of the saved events will be deleted.

## Examples

```
// Save data exists

ret = sceSaveDataSyncSaveDataMemory(&syncParam);
if(ret < SCE_OK)
{
    // Error handling
}
SceSaveDataEvent event;
while(1)
{
    memset(&event, 0x00, sizeof(event));

    ret = sceSaveDataGetEventResult(NULL, &event);
    if(ret == SCE_SAVE_DATA_ERROR_EVENT_BUSY)
    {
        sceKernelSleep(1);
        continue;
    }
    else if(ret < SCE_OK)
    {
        // Error
        break;
    }
    break;
}
```

# sceSaveDataGetConvertProgress

Get save data conversion progress

## Definition

```
#include <save_data.h>

int32_t sceSaveDataGetConvertProgress(
	float *progress
);
```

## Arguments

|  |  |
| --- | --- |
| `progress` | Progress (0.0f to 1.0f) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Pointer is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |

## Description

This function obtains the progress of the most recently called `sceSaveDataConvert()`.

Depending on the timing of the call, the following values may be obtained.

* Before calling `sceSaveDataConvert()`: `0.0`
* After calling `sceSaveDataConvert()` and before obtaining the result returned by `sceSaveDataGetEventResult()`: A value greater than or equal to `0.0` and less than or equal to `1.0` (but if the conversion fails, a value greater than or equal to `0.0` and less than `1.0`)
* During the interval after receiving the result returned by `sceSaveDataGetEventResult()` and before calling `sceSaveDataConvert()` again: The same value obtained when obtaining the result of `sceSaveDataGetEventResult()`

## Examples

```
// Assume sceSaveDataConvert() is being executed

float progress = 0.0f;
int32_t ret = sceSaveDataGetConvertProgress(&progress);
if(ret < SCE_OK){
    // Error handling
}
```

## See Also

`sceSaveDataInitialize3()`, `sceSaveDataConvert()`