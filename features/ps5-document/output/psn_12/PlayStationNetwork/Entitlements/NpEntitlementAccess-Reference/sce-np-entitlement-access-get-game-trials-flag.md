# NpEntitlementAccess Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Reference/sce-np-entitlement-access-get-game-trials-flag.html

# Obtaining the GameTrials Flag

# sceNpEntitlementAccessGetGameTrialsFlag

Gets the GameTrials flag (an integer value)

## Definition

```
#include <np_entitlement_access.h>
typedef uint32_t SceNpEntitlementAccessGameTrialsFlag;

int32_t sceNpEntitlementAccessGetGameTrialsFlag(
	SceNpEntitlementAccessGameTrialsFlag *GameTrialsFlag
)
```

## Arguments

|  |  |
| --- | --- |
| `GameTrialsFlag` | Destination to store the obtained GameTrials flag |

## Return Values

Stores the obtained GameTrials flag in `*GameTrialsFlag` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |

## Description

This function obtains the GameTrials flag that is set in the application. The GameTrials flag is an integer value indicating whether the application is a trial version of the game.

In `*GameTrialsFlag`, one of the following values representing the GameTrials flag is stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_GAME_TRIALS_FLAG_OFF` | 0 | Not a trial version of the game |
| `SCE_NP_ENTITLEMENT_ACCESS_GAME_TRIALS_FLAG_ON` | 1 | Trial version of the game |

A parameter error occurs if NULL is specified for `GameTrialsFlag`.

## Examples

```
/* Obtain the GameTrials flag */
SceNpEntitlementAccessGameTrialsFlag GameTrialsflag;
ret = sceNpEntitlementAccessGetGameTrialsFlag( &GameTrialsflag );
```