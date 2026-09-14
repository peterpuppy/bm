# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-challenge-activity-cohort.html

# Displaying Challenge Activity Cards

# sceSystemServiceInitializeChallengeActivityParam

Initialize a challenge activity card parameter structure

## Definition

```
#include <system_service.h>
void sceSystemServiceInitializeChallengeActivityParam(
    SceSystemServiceChallengeActivityParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Pointer to an `SceSystemServiceChallengeActivityParam` structure |

## Return Values

None

## Description

This function initializes an `SceSystemServiceChallengeActivityParam` structure to its default values and sets the size of the structure (its `size` member). Do not change the value of the `size` member after calling this function.

## See Also

`sceSystemServiceOpenChallengeActivity()`

# sceSystemServiceOpenChallengeActivity

Open a challenge activity card

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceOpenChallengeActivity(
    const SceSystemServiceChallengeActivityParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Pointer to an `SceSystemServiceChallengeActivityParam` structure |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_INTERNAL` | 0x80A10001 | Unexpected internal error occurred |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | Parameter is invalid |

## Description

This function makes the system software open a challenge activity card. It can be used to display interactions undertaken via challenges between users on PlayStation™Network.

For `param`, specify a pointer to an `SceSystemServiceChallengeActivityParam` structure.

You must first use `sceSystemServiceInitializeChallengeActivityParam()` to initialize the structure with its default values. Then, specify values for the members of the structure as the application's purposes require before calling the function described under this header.

## Examples

```
SceSystemServiceChallengeActivityParam yourActivityParam; 

/* Structure initialized with the default values */
sceSystemServiceInitializeChallengeActivityParam(&yourDialogParam);

/* This must be a valid userId, which can be obtained
 * using sceUserServiceGetInitialUser()
 */
yourActivityParam.userId = 123456;

/* This must be the valid activityId of the player whom the challenge activity card
 * is targeting
 */
yourActivityParam.activityId = 12345678;

/* Configure the challenge activity screen
 * The following two modes are available
 * SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_DEFAULT (default)
 * SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_LEADERBOARD
 * If no screen has been selected, this will be set to the default screen
 */
yourActivityParam.screen = SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_DEFAULT;

/* Configure the challenge activity cohort
 * This option is selected when navigating to the leaderboard
 * The following three cohort options are available
 * SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_DEFAULT (default)
 * SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_FRIENDS
 * SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_GLOBAL
 * If no cohort has been selected, this will be set to the default cohort
 */
yourActivityParam.cohort = SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_DEFAULT;

int ret;

ret = sceSystemServiceOpenChallengeActivity(&yourActivityParam);
if ((ret == SCE_OK)) {
    printf("Challenge Activity Has Been Opened!\n");
}
```

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, the library may not operate as expected afterward. Make sure to program the application so that this function is not called at the same time by multiple threads.

# SceSystemServiceChallengeActivityParam

Challenge activity card parameter structure

## Definition

```
#include <system_service.h>
typedef struct SceSystemServiceChallengeActivityParam {
    size_t size;
    const char* activityId;
    SceUserServiceUserId userId;
    SceSystemServiceChallengeActivityScreen screen;
    SceSystemServiceChallengeActivityCohort cohort;
} SceSystemServiceChallengeActivityParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of the `SceSystemServiceChallengeActivityParam` structure |
| `activityId` | Challenge activity ID |
| `userId` | The user ID of the user who is controlling the application |
| `screen` | Challenge activity card screen display mode |
| `cohort` | Leaderboard cohort |

## Description

This structure is used when a challenge activity card is opened using `sceSystemServiceOpenChallengeActivity()`.

## See Also

`sceSystemServiceInitializeChallengeActivityParam()`

# SceSystemServiceChallengeActivityScreen

Challenge activity card screen display mode

## Definition

```
#include <system_service.h>
typedef enum {
    SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_DEFAULT = 0,
    SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_LEADERBOARD = 1
} SceSystemServiceChallengeActivityScreen;
```

## Description

This type represents a challenge activity card screen display mode. One of the following values can be used.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_DEFAULT` | 0 | Displays in the default mode |
| `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_LEADERBOARD` | 1 | Displays in leaderboard mode |

## See Also

`SceSystemServiceChallengeActivityParam`

# SceSystemServiceChallengeActivityCohort

Challenge activity card leaderboard cohort

## Definition

```
#include <system_service.h>
typedef enum {
    SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_DEFAULT = 0,
    SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_FRIENDS = 1,
    SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_GLOBAL = 2
} SceSystemServiceChallengeActivityCohort;
```

## Description

This type represents a challenge activity card leaderboard cohort. One of the following values can be used.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_DEFAULT` | 0 | Default cohort |
| `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_FRIENDS` | 1 | Friend ranking cohort |
| `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_GLOBAL` | 2 | Global ranking cohort |

## See Also

`SceSystemServiceChallengeActivityParam`