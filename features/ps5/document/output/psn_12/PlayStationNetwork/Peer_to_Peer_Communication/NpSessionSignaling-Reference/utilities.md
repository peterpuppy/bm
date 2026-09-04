# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/utilities.html

# Utilities

# SceNpSessionSignalingConnectionStatistics

Connection statistics

## Definition

```
#include <np.h>
typedef struct SceNpSessionSignalingConnectionStatistics {
    uint32_t maxConnection;
    uint32_t totalConnection;
    uint32_t connecting;
    uint32_t connected;
} SceNpSessionSignalingConnectionStatistics;
```

## Members

|  |  |
| --- | --- |
| `maxConnection` | Maximum number of connections that existed at the same time in the past |
| `totalConnection` | Total number of existing connections |
| `connecting` | Number of connections in the PENDING state |
| `connected` | Number of connections in the ACTIVE state |

## Description

This structure represents connection statistics of the NpSessionSignaling library.

Specify it as an argument when executing `sceNpSessionSignalingGetConnectionStatistics()`.

# sceNpSessionSignalingGetConnectionStatistics

Gets connection statistics

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetConnectionStatistics(
    SceNpSessionSignalingConnectionStatistics *stats
)
```

## Arguments

|  |  |
| --- | --- |
| `stats` | Destination to store the obtained connection statistics |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `stats` is NULL |

## Description

This function obtains statistics on the connections managed internally by the NpSessionSignaling library.

## Examples

```
int ret;
SceNpSessionSignalingConnectionStatistics stats;

ret = sceNpSessionSignalingGetConnectionStatistics(&stats);
if ( ret < 0 ) {
    // Error handling
}
```

# SceNpSessionSignalingMemoryInfo

Memory information

## Definition

```
#include <np.h>
typedef struct SceNpSessionSignalingMemoryInfo {
    size_t totalMemSize;
    size_t curMemUsage;
    size_t maxMemUsage;
    uint8_t reserved[12];
} SceNpSessionSignalingMemoryInfo;
```

## Members

|  |  |
| --- | --- |
| `totalMemSize` | Memory pool size in bytes |
| `curMemUsage` | Current memory usage in bytes |
| `maxMemUsage` | Maximum memory usage in the past in bytes |
| `reserved` | Reserved area |

## Description

This structure represents information of the memory used by the NpSessionSignaling library.

Specify it as an argument when executing `sceNpSessionSignalingGetMemoryInfo()`.

# sceNpSessionSignalingGetMemoryInfo

Gets memory information

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetMemoryInfo(
    SceNpSessionSignalingMemoryInfo *memInfo
)
```

## Arguments

|  |  |
| --- | --- |
| `memInfo` | Destination to store the obtained memory information |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `memInfo` is NULL |

## Description

This function obtains the status of how much of the memory pool is used by the NpSessionSignaling library.

The memory pool size specified upon library initialization, the current memory usage volume, and the maximum memory usage in the past, can be obtained. Use this function in application development and check the memory size required by your application.

## Examples

```
int ret;
SceNpSessionSignalingMemoryInfo memInfo;

ret = sceNpSessionSignalingGetMemoryInfo(&memInfo);
if ( ret < 0 ) {
    // Error handling
}
```