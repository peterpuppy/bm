# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-open-tournament-occurrence.html

# Displaying Tournament Activity Cards

# sceSystemServiceInitializeTournamentOccurrenceParam

Initialize a tournament occurrence structure

## Definition

```
#include <system_service.h>
void sceSystemServiceInitializeTournamentOccurrenceParam(
    SceSystemServiceTournamentOccurrenceParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Pointer to an `SceSystemServiceTournamentOccurrenceParam` structure. |

## Return Values

None

## Description

This function initializes an `SceSystemServiceTournamentOccurrenceParam` structure to its default values and sets the size of the structure (its `size` member). Do not change the value of the `size` member after calling this function.

## See Also

`sceSystemServiceOpenTournamentOccurrence()`

# sceSystemServiceOpenTournamentOccurrence

Open a tournament activity card

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceOpenTournamentOccurrence(
    const SceSystemServiceTournamentOccurrenceParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Pointer to an `SceSystemServiceTournamentOccurrenceParam` structure. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_INTERNAL` | 0x80A10001 | Unexpected internal error occurred |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | Parameter is invalid |

## Description

This function makes the system software open a tournament activity card and allows users to join tournaments on PlayStation™Network.

For `param`, specify a pointer to an `SceSystemServiceTournamentOccurrenceParam` structure. The contents of the activity card that is opened differ depending on the values of the members of this structure. For details, refer to the description of `SceSystemServiceTournamentOccurrenceParam`.

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, the library may not operate as expected afterward. Make sure to program the application so that this function is not called at the same time by multiple threads.

# SceSystemServiceTournamentOccurrenceParam

Tournament Occurrence structure

## Definition

```
#include <system_service.h>
typedef struct SceSystemServiceTournamentOccurrenceParam {
    size_t size;
    const char* tournamentId;
    SceUserServiceUserId userId;
    const char* occurrenceId;
} SceSystemServiceTournamentOccurrenceParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of the `SceSystemServiceTournamentOccurrenceParam` structure. |
| `tournamentId` | Tournament object ID |
| `userId` | User ID of the user who is manipulating the tournament activity card |
| `occurrenceId` | Specify NULL |

## Description

This structure is used when opening a tournament activity card using `sceSystemServiceOpenTournamentOccurrence()`. First, use `sceSystemServiceInitializeTournamentOccurrenceParam()` to initialize the structure with its default values. Afterward, specify values for the members according to the purpose of the structure.

When a tournament object ID is specified for `tournamentId`, the activity card for the next available tournament occurrence in that tournament object is opened. If the user specified with `userId` is already active for that tournament object, the relevant activity card is opened.

You can also specify one of the following values for `tournamentId`:

* If you specify `"_nextAvailableTournament"`, the tournament activity card for the next available tournament occurrence across all tournament objects is opened.
* If you specify, `"_activeTournament"`, the tournament activity card for the tournament that is currently active for the user who is specified with `userId` is opened.