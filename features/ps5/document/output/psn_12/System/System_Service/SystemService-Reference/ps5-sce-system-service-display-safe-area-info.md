# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-display-safe-area-info.html

# Obtaining the Display's Safe Area

# sceSystemServiceGetDisplaySafeAreaInfo

Get information about the display's safe area

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceGetDisplaySafeAreaInfo(
        SceSystemServiceDisplaySafeAreaInfo* info
);
```

## Arguments

|  |  |
| --- | --- |
| `info` | Destination to store obtained information about the safe area |

## Return Values

Stores information about the safe area in `*info` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for other errors. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function obtains information about the display's safe area (area without the possibility of being hidden by being close to the screen edge).

# SceSystemServiceDisplaySafeAreaInfo

Information about the display's safe area

## Definition

```
#include <system_service.h>
typedef struct SceSystemServiceDisplaySafeAreaInfo {
	float ratio;
	uint8_t reserved[128];
} SceSystemServiceDisplaySafeAreaInfo;
```

## Members

|  |  |
| --- | --- |
| `ratio` | Ratio of the safe area (0.9 or more, 1.0 or less) |
| `reserved` | Reserved area |

## Description

This structure is used when obtaining information with `sceSystemServiceGetDisplaySafeAreaInfo()`.

`ratio` represents the ratio of the safe area's width (or height) against the width (or height) of the frame buffer.