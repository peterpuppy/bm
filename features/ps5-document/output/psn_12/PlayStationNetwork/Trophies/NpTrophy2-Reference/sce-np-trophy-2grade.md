# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/sce-np-trophy-2grade.html

# Common Datatypes

# SceNpTrophy2Id

Trophy ID

## Definition

```
#include <np.h>
#define SCE_NP_TROPHY2_INVALID_TROPHY_ID (-1)
typedef int32_t SceNpTrophy2Id;
```

## Description

This datatype represents a trophy ID.

A trophy ID is a unique value that identifies a single trophy in a trophy set identified by the NP Title ID and NP service label.

## See Also

`sceNpTrophy2GetTrophyInfo()`, `sceNpTrophy2GetTrophyIcon()`

# SceNpTrophy2Grade

Trophy grade

## Definition

```
#include <np.h>
typedef int32_t SceNpTrophy2Grade;
#define SCE_NP_TROPHY2_GRADE_UNKNOWN        (0)
#define SCE_NP_TROPHY2_GRADE_PLATINUM       (1)
#define SCE_NP_TROPHY2_GRADE_GOLD           (2)
#define SCE_NP_TROPHY2_GRADE_SILVER         (3)
#define SCE_NP_TROPHY2_GRADE_BRONZE         (4)
```

## Description

This datatype represents the grade of a trophy. A grade indicates how difficult it is for a user to earn that trophy.

The values that can be set are as follows:

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_GRADE_UNKNOWN` | 0 | Grade is unknown |
| `SCE_NP_TROPHY2_GRADE_PLATINUM` | 1 | Platinum trophy:  Trophy that is automatically unlocked by the system when all the required trophies are earned |
| `SCE_NP_TROPHY2_GRADE_GOLD` | 2 | Gold trophy:  Most difficult trophy to earn |
| `SCE_NP_TROPHY2_GRADE_SILVER` | 3 | Silver trophy:  Relatively difficult trophy to earn |
| `SCE_NP_TROPHY2_GRADE_BRONZE` | 4 | Bronze trophy:  Trophy that is easily earned; the most common type of trophy |

## See Also

`SceNpTrophy2Details`

# SceNpTrophy2GroupId

Trophy group ID

## Definition

```
#include <np.h>
#define SCE_NP_TROPHY2_BASE_GAME_GROUP_ID (-1)
#define SCE_NP_TROPHY2_INVALID_GROUP_ID (-2)
typedef int32_t SceNpTrophy2GroupId;
```

## Description

This datatype represents a trophy group ID.

A trophy group ID is a unique value that identifies a single trophy group in a trophy set identified by the NP Title ID and NP service label.

## See Also

`SceNpTrophy2Details`, `SceNpTrophy2GroupData`, `SceNpTrophy2GroupDetails`, `sceNpTrophy2GetGroupInfo()`, `sceNpTrophy2GetGroupIcon()`