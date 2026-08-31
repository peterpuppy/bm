# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-storage-stat.html

# Debugging Support

# SceNpUniversalDataSystemMemoryStat

Memory information of the NpUniversalDataSystem library

## Definition

```
#include <np.h>
typedef struct SceNpUniversalDataSystemMemoryStat {
    size_t poolSize;
    size_t maxInuseSize;
    size_t currentInuseSize;
} SceNpUniversalDataSystemMemoryStat;
```

## Members

|  |  |
| --- | --- |
| `poolSize` | [Out] Size of the NpUniversalDataSystem library memory pool |
| `maxInuseSize` | [Out] Maximum size of memory used by the NpUniversalDataSystem library |
| `currentInuseSize` | [Out] Size of memory currently used by the NpUniversalDataSystem library |

## Description

This structure represents memory information of the NpUniversalDataSystem library. This structure is used when memory information is obtained with `sceNpUniversalDataSystemGetMemoryStat()`.

# SceNpUniversalDataSystemStorageStat

Storage information

## Definition

```
#include <np.h>
typedef struct SceNpUniversalDataSystemStorageStat {
    size_t inEvents;
    size_t outEvents;
    size_t lostEvents;
    size_t maxInuseSize;
    size_t currentEvents;
    size_t currentInuseSize;
    size_t currentFreeSize;
} SceNpUniversalDataSystemStorageStat;
```

## Members

|  |  |
| --- | --- |
| `inEvents` | [Out] Number of events stored in storage since context creation |
| `outEvents` | [Out] Number of events taken from storage since context creation |
| `lostEvents` | [Out] Number of events deleted since context creation |
| `maxInuseSize` | [Out] Maximum consumption size since context creation |
| `currentEvents` | [Out] Number of events currently in storage |
| `currentInuseSize` | [Out] Current storage consumption size |
| `currentFreeSize` | [Out] Current storage available size |

## Description

This structure represents storage information. This structure is used when storage information is obtained with `sceNpUniversalDataSystemGetStorageStat()`.

# sceNpUniversalDataSystemGetMemoryStat

Get memory information of the NpUniversalDataSystem library

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemGetMemoryStat(
    SceNpUniversalDataSystemMemoryStat *stat
)
```

## Arguments

|  |  |
| --- | --- |
| `stat` | [Out] Destination to store the obtained memory information |

## Return Values

Stores the obtained memory information in `*stat` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function obtains memory information of the NpUniversalDataSystem library. Information obtained with this function can mainly be used to determine the memory pool size to specify for library initialization.

## Examples

```
SceNpUniversalDataSystemMemoryStat stats;
int ret;

memset(&stats, 0, sizeof(stats));
ret = sceNpUniversalDataSystemGetMemoryStat(&stats);
if (ret < 0) {
    // Error handling
}
```

## See Also

`SceNpUniversalDataSystemInitParam`

# sceNpUniversalDataSystemGetStorageStat

Get storage information

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemGetStorageStat(
    SceNpUniversalDataSystemContext context,
    SceNpUniversalDataSystemStorageStat *stat
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `stat` | [Out] Destination to store the obtained storage information |

## Return Values

Stores the obtained storage information in `*stat` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |

## Description

This function obtains storage information such as the cumulative number of events since the context was created and the storage consumption size. The information obtained with this function is mainly used to determine event sizes and frequency of transmission. Note this information will be affected by events generated internally by the system as well as events explicitly posted by the game. For example, the cumulative number of events may increase even when the game has not posted any events.

## Examples

```
extern SceNpUniversalDataSystemContext context;
SceNpUniversalDataSystemStorageStat stats;
int ret;

memset(&stats, 0, sizeof(stats));
ret = sceNpUniversalDataSystemGetStorageStat(context, &stats);
if (ret < 0) {
    // Error handling
}
```

# sceNpUniversalDataSystemEventToString

Convert an event to a readable string

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventToString(
    const SceNpUniversalDataSystemEvent *event,
    char *buf,
    size_t bufSize,
    size_t *stringSize
)
```

## Arguments

|  |  |
| --- | --- |
| `event` | [In] Event |
| `buf` | [Out] Destination to store the converted string |
| `bufSize` | [In] Size of the destination storage |
| `stringSize` | [Out] Destination to store the size (including the NULL terminator) of the converted string, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function converts an event to a readable string similar to JSON. It can be used in development to check if an event is assembled as intended.

When the converted string does not fit the destination storage, this function will store the section of the string that does fit, set the size of the string in `*stringSize`, and terminate normally. Specify NULL for `stringSize` if the size of the converted string is not required.

## Examples

```
SceNpUniversalDataSystemEvent *event = NULL;
char buf[256];
int ret;

ret = sceNpUniversalDataSystemCreateEvent("event_name", NULL, &event, NULL);
if (ret < 0) {
    // Error handling
}

ret = sceNpUniversalDataSystemEventToString(event, buf, sizeof(buf), NULL);
if (ret < 0) {
    // Error handling
}

ret = sceNpUniversalDataSystemDestroyEvent(event);
if (ret < 0) {
    // Error handling
}
```