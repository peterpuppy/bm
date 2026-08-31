# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/obtaining-trophy-configuration-data-and-trophy-records.html

# Obtaining Trophy Configuration Data and Trophy Records

# SceNpTrophy2Data

Trophy record of a trophy

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2Data {
    SceNpTrophy2Id trophyId;
    bool unlocked;
    uint8_t reserved[3];
    SceNpTrophy2Progress progress;
    SceRtcTick timestamp;
} SceNpTrophy2Data;
```

## Members

|  |  |
| --- | --- |
| `trophyId` | [Out] Trophy ID |
| `unlocked` | [Out] Whether or not the trophy is unlocked |
| `reserved` | [Out] Reserved area (always fill with 0) |
| `progress` | [Out] The current progress value for progressive trophies |
| `timestamp` | [Out] The time stamp of when the trophy was first unlocked, or 0 if the trophy has not been unlocked |

## Description

This structure is used when obtaining the trophy record of each unlocked trophy using `sceNpTrophy2GetTrophyInfo()` or `sceNpTrophy2GetTrophyInfoArray()`.

`timestamp` indicates the time stamp of when the user unlocked the trophy (date and time of unlocking).

If a time stamp has not been recorded, the `timestamp` value will be 0.

This structure represents information that changes depending on user gameplay. Fixed information defined by the trophy set is represented by the `SceNpTrophy2Details` structure.

# SceNpTrophy2Details

Trophy configuration data of a trophy

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2Details {
    SceNpTrophy2Id trophyId;
    SceNpTrophy2Grade trophyGrade;
    SceNpTrophy2GroupId groupId;
    bool hidden;
    bool hasReward;
    uint8_t reserved[2];
    SceNpTrophy2Progress target;
    char name[SCE_NP_TROPHY2_NAME_MAX_SIZE];
    char description[SCE_NP_TROPHY2_DESCR_MAX_SIZE];
    char reward[SCE_NP_TROPHY2_REWARD_MAX_SIZE];
} SceNpTrophy2Details;
```

## Members

|  |  |
| --- | --- |
| `trophyId` | [Out] Trophy ID |
| `trophyGrade` | [Out] Grade of the trophy |
| `groupId` | [Out] ID of the trophy group to which this trophy belongs |
| `hidden` | [Out] Hidden flag |
| `hasReward` | [Out] Whether reward data is included |
| `reserved` | [Out] Reserved area (always fill with 0) |
| `target` | [Out] Target value (progress value at which the trophy will be unlocked) for progressive trophies |
| `name` | [Out] Name of the trophy |
| `description` | [Out] Description of the trophy |
| `reward` | [Out] Reward data (all 0's if `hasReward` is false) |

## Description

This structure is used to obtain trophy unlocking information (trophy record) for each individual trophy using `sceNpTrophy2GetTrophyInfo()` or `sceNpTrophy2GetTrophyInfoArray()`.

This structure represents information that is fixed by the definition of the trophy set. Information that changes depending on user gameplay is represented by the `SceNpTrophy2Data` structure.

# SceNpTrophy2GameData

Trophy record of a trophy set

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2GameData {
    uint32_t unlockedTrophies;
    uint32_t unlockedPlatinum;
    uint32_t unlockedGold;
    uint32_t unlockedSilver;
    uint32_t unlockedBronze;
    uint32_t progressPercentage;
} SceNpTrophy2GameData;
```

## Members

|  |  |
| --- | --- |
| `unlockedTrophies` | [Out] Number of unlocked trophies |
| `unlockedPlatinum` | [Out] Number of unlocked platinum trophies |
| `unlockedGold` | [Out] Number of unlocked gold trophies |
| `unlockedSilver` | [Out] Number of unlocked silver trophies |
| `unlockedBronze` | [Out] Number of unlocked bronze trophies |
| `progressPercentage` | [Out] Percentage of the trophy group, in points, that has been unlocked |

## Description

This structure is used to obtain trophy unlocking information (trophy records) for a trophy set using `sceNpTrophy2GetGameInfo()`.

`progressPercentage` is the percentage of unlocked trophies based on trophy points and does not take into account the progress made toward unlocking progressive trophies that are still locked.

This structure represents information that changes depending on user gameplay. Fixed information defined by the trophy set is represented by the `SceNpTrophy2GameDetails` structure.

# SceNpTrophy2GameDetails

Trophy configuration data of a trophy set

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2GameDetails {
    uint32_t numGroups;
    uint32_t numTrophies;
    uint32_t numPlatinum;
    uint32_t numGold;
    uint32_t numSilver;
    uint32_t numBronze;
    char title[SCE_NP_TROPHY2_GAME_TITLE_MAX_SIZE];
} SceNpTrophy2GameDetails;
```

## Members

|  |  |
| --- | --- |
| `numGroups` | [Out] Total number of trophy groups |
| `numTrophies` | [Out] Total number of trophies |
| `numPlatinum` | [Out] Total number of platinum trophies |
| `numGold` | [Out] Total number of gold trophies |
| `numSilver` | [Out] Total number of silver trophies |
| `numBronze` | [Out] Total number of bronze trophies |
| `title` | [Out] Name of the trophy set |

## Description

This structure is used to obtain trophy configuration data of a trophy set using `sceNpTrophy2GetGameInfo()`.

This structure represents information that is fixed by the definition of the trophy set. Information that changes depending on user gameplay is represented by the `SceNpTrophy2GameData` structure.

# SceNpTrophy2GroupData

Trophy record of a trophy group

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2GroupData {
    SceNpTrophy2GroupId groupId;
    uint32_t unlockedTrophies;
    uint32_t unlockedPlatinum;
    uint32_t unlockedGold;
    uint32_t unlockedSilver;
    uint32_t unlockedBronze;
    uint32_t progressPercentage;
    uint8_t reserved[4];
} SceNpTrophy2GroupData;
```

## Members

|  |  |
| --- | --- |
| `groupId` | [Out] Trophy group ID |
| `unlockedTrophies` | [Out] Number of unlocked trophies |
| `unlockedPlatinum` | [Out] Number of unlocked platinum trophies |
| `unlockedGold` | [Out] Number of unlocked gold trophies |
| `unlockedSilver` | [Out] Number of unlocked silver trophies |
| `unlockedBronze` | [Out] Number of unlocked bronze trophies |
| `progressPercentage` | [Out] Percentage of the trophy group, in points, that has been unlocked |
| `reserved` | [Out] Reserved area (always fill with 0) |

## Description

This structure is used to obtain information about unlocked trophies (trophy records) in a trophy group using `sceNpTrophy2GetGroupInfo()` or `sceNpTrophy2GetGroupInfoArray()`.

`progressPercentage` is the percentage of unlocked trophies based on trophy points and does not take into account the progress made toward unlocking progressive trophies that are still locked.

This structure represents information that changes depending on user gameplay. Fixed information defined by the trophy set is represented by the `SceNpTrophy2GroupDetails` structure.

# SceNpTrophy2GroupDetails

Trophy configuration data of a trophy group

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2GroupDetails {
    SceNpTrophy2GroupId groupId;
    uint32_t numTrophies;
    uint32_t numPlatinum;
    uint32_t numGold;
    uint32_t numSilver;
    uint32_t numBronze;
    char title[SCE_NP_TROPHY2_GROUP_TITLE_MAX_SIZE];
} SceNpTrophy2GroupDetails;
```

## Members

|  |  |
| --- | --- |
| `groupId` | [Out] Trophy group ID |
| `numTrophies` | [Out] Total number of trophies |
| `numPlatinum` | [Out] Total number of platinum trophies |
| `numGold` | [Out] Total number of gold trophies |
| `numSilver` | [Out] Total number of silver trophies |
| `numBronze` | [Out] Total number of bronze trophies |
| `title` | [Out] Name of the trophy group |

## Description

This structure is used to obtain trophy configuration data of a trophy group with `sceNpTrophy2GetGroupInfo()` or `sceNpTrophy2GetGroupInfoArray()`.

This structure represents information that is fixed by the definition of the trophy set. Information that changes depending on user gameplay is represented by the `SceNpTrophy2GroupData` structure.

# SceNpTrophy2ProgressType

Category of progress value for a progressive trophy

## Definition

```
#include <np.h>
typedef int32_t SceNpTrophy2ProgressType;
#define SCE_NP_TROPHY2_PROGRESS_TYPE_NONE    (0)
#define SCE_NP_TROPHY2_PROGRESS_TYPE_UINT64  (1)
```

## Description

This data type indicates whether a trophy is a progressive trophy, and if so, its progress value. It is used to determine the form of the progress value within structures of the type `SceNpTrophy2Progress`.

The defined values are as follows.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_PROGRESS_TYPE_NONE` | 0 | Non-progressive trophy |
| `SCE_NP_TROPHY2_PROGRESS_TYPE_UINT64` | 1 | Progressive trophy; the progress value is a 64-bit non-negative integer |

# SceNpTrophy2Progress

Progress of a progressive trophy

## Definition

```
#include <np.h>
typedef struct SceNpTrophy2Progress {
    SceNpTrophy2ProgressType type;
    uint8t reserved[4]
    union {
        uint64_t valueUInt64;
    } value;
} SceNpTrophy2Progress;
```

## Members

|  |  |
| --- | --- |
| `type` | [Out] Category for progress |
| `reserved` | Reserved area |
| `valueUInt64` | [Out] Progress if the category is `SCE_NP_TROPHY2_PROGRESS_TYPE_UINT64` |

## Description

This structure represents the progress for a progressive trophy.

If the trophy is not a progressive trophy, `SCE_NP_TROPHY2_PROGRESS_TYPE_NONE` will be stored in `type`.

If the trophy is a progressive trophy, a value indicating the type of the progress value will be stored in `type`, and the progress value will be stored in a member within the relevant `value`.

## See Also

`SceNpTrophy2Details`, `SceNpTrophy2Data`

# sceNpTrophy2GetGameInfo

Get trophy set information

## Definition

```
#include <np.h>
int sceNpTrophy2GetGameInfo(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    SceNpTrophy2GameDetails *details,
    SceNpTrophy2GameData *data
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `details` | [Out] Destination to store the obtained trophy configuration data, or NULL |
| `data` | [Out] Destination to store the obtained trophy records, or NULL |

## Return Values

Stores the obtained trophy configuration data in `*details` (if `details` is not NULL), stores the obtained trophy records in `*data` (if `data` is not NULL), and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |

## Description

This function obtains the trophy set information specified with `context`.

For `*details`, static trophy configuration data determined by the definition of the trophy set will be returned. For `*data`, user-specific trophy records based on gameplay status will be returned. If trophy configuration data or trophy records are not required, specify NULL for the corresponding argument. An error will be returned if NULL is specified for both.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
SceNpTrophy2GameDetails details;
SceNpTrophy2GameData data;
int ret;

memset(&details, 0x00, sizeof(details));
memset(&data, 0x00, sizeof(data));

ret = sceNpTrophy2GetGameInfo(context, handle, &details, &data);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`

# sceNpTrophy2GetGroupInfo

Get trophy group information

## Definition

```
#include <np.h>
int sceNpTrophy2GetGroupInfo(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    SceNpTrophy2GroupId groupId,
    SceNpTrophy2GroupDetails *details,
    SceNpTrophy2GroupData *data
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `groupId` | [In] Group ID |
| `details` | [Out] Destination to store the obtained trophy configuration data, or NULL |
| `data` | [Out] Destination to store the obtained trophy records, or NULL |

## Return Values

Stores the obtained trophy configuration data in `*details` (if `details` is not NULL), stores the obtained trophy records in `*data` (if `data` is not NULL), and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_INVALID_GROUP_ID` | 0x8055390b | Invalid group ID |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |

## Description

This function obtains the trophy group information specified with `context` and `groupId`.

In `groupId`, specify the ID of the trophy group whose information you want to obtain. If you want to obtain information of the base game group, specify `SCE_NP_TROPHY2_BASE_GAME_GROUP_ID`.

For `*details`, static trophy configuration data determined by the definition of the trophy set will be returned. For `*data`, user-specific trophy records updated based on gameplay will be returned. If trophy configuration data or trophy records are not required, specify NULL for the corresponding argument. An error will be returned if NULL is specified for both.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2GroupId groupId;
SceNpTrophy2GroupDetails details;
SceNpTrophy2GroupData data;
int ret;

memset(&details, 0x00, sizeof(details));
memset(&data, 0x00, sizeof(data));

ret = sceNpTrophy2GetGroupInfo(context, handle, groupId, &details, &data);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`, `sceNpTrophy2GetGroupInfoArray()`

# sceNpTrophy2GetGroupInfoArray

Obtain information about multiple trophy groups

## Definition

```
#include <np.h>
int sceNpTrophy2GetGroupInfoArray(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    uint32_t offset,
    uint32_t limit,
    SceNpTrophy2GroupDetails *detailsArray,
    SceNpTrophy2GroupData *dataArray,
    uint32_t *count
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `offset` | [In] Position in the list of group IDs of the first group whose information should be obtained. Group IDs are arranged in ascending order. (0: from the start) |
| `limit` | [In] Maximum number of trophy groups whose information will be obtained |
| `detailsArray` | [Out] Destination to store the obtained trophy configuration data, or NULL |
| `dataArray` | [Out] Destination to store the obtained trophy records, or NULL |
| `count` | [Out] Number of trophy groups whose information was obtained |

## Return Values

Stores the obtained trophy configuration data in `*detailsArray` (if `detailsArray` is not NULL), stores the obtained trophy records in `*dataArray` (if `dataArray` is not NULL), and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |

## Description

This function obtains information about multiple trophy groups in the trophy set specified with `context` in a single call.

Information about a set of trophy groups will be obtained from a selected list arranged in ascending order of group ID. Specify the list position of the first group to obtain in `offset` and the maximum number of groups whose information should be obtained in `limit`. Allocate a sufficiently large area to store as many `SceNpTrophy2GroupDetails` structures as indicated by `limit` and specify that area for `detailsArray`; similarly, allocate a sufficiently large area to store as many `SceNpTrophy2GroupData` structures as indicated by `limit` and specify that area for `dataArray`.

Fixed trophy configuration data determined by the trophy set definitions will be returned to \*`detailsArray`, and user-specific trophy records updated based on gameplay will be returned to `*dataArray`. If trophy configuration data or trophy records are not required, specify NULL for the corresponding argument. An error will be returned if NULL is specified for both.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2GroupId groupId;
SceNpTrophy2GroupDetails detailsArray[10];
SceNpTrophy2GroupData dataArray[10];
uint32_t count = 0;
int ret;

memset(&details, 0x00, sizeof(detailsArray));
memset(&data, 0x00, sizeof(dataArray));

ret = sceNpTrophy2GetGroupInfoArray(context, handle, 0, 10, &detailsArray, &dataArray, &count);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`, `sceNpTrophy2GetGroupInfo()`

# sceNpTrophy2GetTrophyInfo

Get trophy information

## Definition

```
#include <np.h>
int sceNpTrophy2GetTrophyInfo(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    SceNpTrophy2Id trophyId,
    SceNpTrophy2Details *details,
    SceNpTrophy2Data *data
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `trophyId` | [In] Trophy ID |
| `details` | [Out] Destination to store the obtained trophy configuration data, or NULL |
| `data` | [Out] Destination to store the obtained trophy records, or NULL |

## Return Values

Stores the obtained trophy configuration data in `*details` (if `details` is not NULL), stores the obtained trophy records in `*data` (if `data` is not NULL), and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_INVALID_TROPHY_ID` | 0x8055390a | Invalid trophy ID |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |

## Description

This function obtains information about the trophy specified with `context` and `trophyId`.

For `*details`, static trophy configuration data determined by the definition of the trophy set will be returned. For `*data`, user-specific trophy records updated based on gameplay will be returned. If trophy configuration data or trophy records are not required, specify NULL for the corresponding argument.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2Id trophyId;
SceNpTrophy2Details details;
SceNpTrophy2Data data;
int ret;

memset(&details, 0x00, sizeof(details));
memset(&data, 0x00, sizeof(data));

ret = sceNpTrophy2GetTrophyInfo(context, handle, trophyId, &details, &data);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

* Trophy configuration data like that of ordinary trophies will be returned even for a hidden trophy. If displaying information about the trophy in-game, check whether the trophy is a hidden trophy and whether it has been unlocked, and display as appropriate.
* This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`, `sceNpTrophy2GetTrophyInfoArray()`

# sceNpTrophy2GetTrophyInfoArray

Obtain multiple instances of trophy information

## Definition

```
#include <np.h>
int sceNpTrophy2GetTrophyInfoArray(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    uint32_t offset,
    uint32_t limit,
    SceNpTrophy2Details *detailsArray,
    SceNpTrophy2Data *dataArray,
    uint32_t *count
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `offset` | [In] Starting position to obtain trophy information, with trophy IDs in ascending order (0: from the start) |
| `limit` | [In] The maximum number of instances of trophy information to obtain |
| `detailsArray` | [Out] Destination to store the obtained trophy configuration data, or NULL |
| `dataArray` | [Out] Destination to store the obtained trophy records, or NULL |
| `count` | [Out] Number of trophies whose information was obtained |

## Return Values

Stores the obtained trophy configuration data in `*detailsArray` (if `detailsArray` is not NULL), stores the obtained trophy records in `*dataArray` (if `dataArray` is not NULL), and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |

## Description

This function obtains information about multiple trophies included in the trophy set specified with `context` at once.

Information about a set of trophies will be obtained from a selected list arranged in ascending order of trophy ID. Specify the list position of the first trophy to obtain for `offset` and the maximum number of trophies whose information should be obtained for `limit`. Allocate a sufficiently large area to store as many `SceNpTrophy2Details` structures as indicated by `limit` and specify that area for `detailsArray`; similarly, allocate a sufficiently large area to store as many `SceNpTrophy2Data` structures as indicated by `limit` and specify that area for `dataArray`.

Fixed trophy configuration data determined by the trophy set definitions will be returned to \*`detailsArray`, and user-specific trophy records updated based on gameplay will be returned to `*dataArray`. If trophy configuration data or trophy records are not required, specify NULL for the corresponding argument. An error will be returned if NULL is specified for both.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2GroupId groupId;
SceNpTrophy2Details detailsArray[10];
SceNpTrophy2Data dataArray[10];
uint32_t count = 0;
int ret;

memset(&details, 0x00, sizeof(detailsArray));
memset(&data, 0x00, sizeof(dataArray));

ret = sceNpTrophy2GetTrophyInfoArray(context, handle, 0, 10, &detailsArray, &dataArray, &count);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

* Trophy configuration data like that of ordinary trophies will be returned even for a hidden trophy. If displaying information about the trophy in-game, check whether the trophy is a hidden trophy and whether it has been unlocked, and display as appropriate.
* This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`, `sceNpTrophy2GetTrophyInfo()`