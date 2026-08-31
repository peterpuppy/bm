# NpGameIntent Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpGameIntent-Reference/sce-np-game-intent-init-param.html

# Initialization/Termination

# SceNpGameIntentInitParam

Initialization parameters

## Definition

```
#include <np/np_game_intent.h>
typedef struct SceNpGameIntentInitParam {
    size_t size;
    uint8_t reserved[32];
} SceNpGameIntentInitParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `reserved` | Reserved areas |

## Description

This structure is used to specify the parameters upon initializing the library with `sceNpGameIntentInitialize()`.

Use this structure after initializing it with `sceNpGameIntentInitParamInit()`.

# sceNpGameIntentInitParamInit

Initializes initialization parameters

## Definition

```
#include <np/np_game_intent.h>
void sceNpGameIntentInitParamInit(
    SceNpGameIntentInitParam *p
)
```

## Arguments

|  |  |
| --- | --- |
| `p` | Target initialization parameters |

## Description

This function initializes the `SceNpGameIntentInitParam` structure. Always initialize the `SceNpGameIntentInitParam` structure with this function before passing it to `sceNpGameIntentInitialize()`.

Appropriate initialization values will be set to the members of `*p` by calling this function. The application is not required to explicitly set values to members that are not used, such as the size and reserved areas.

# sceNpGameIntentInitialize

Initializes the library

## Definition

```
#include <np/np_game_intent.h>
int32_t sceNpGameIntentInitialize(
    const SceNpGameIntentInitParam *initParam
)
```

## Arguments

|  |  |
| --- | --- |
| `initParam` | Initialization parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_GAME_INTENT_ERROR_ALREADY_INITIALIZED` | 0x80553801 | Library is already initialized |
| `SCE_NP_GAME_INTENT_ERROR_OUT_OF_MEMORY` | 0x80553803 | Insufficient memory |
| `SCE_NP_GAME_INTENT_ERROR_INVALID_ARGUMENT` | 0x80553804 | * `initParam` is NULL * One of the `initParam` members is invalid |
| `SCE_NP_GAME_INTENT_ERROR_UNKNOWN` | 0x80553800 | Undefined error that is not listed above |

## Description

This function initializes the NpGameIntent library.

For `initParam`, specify the `SceNpGameIntentInitParam` structure initialized using `sceNpGameIntentInitParamInit()`.

Call this function just once at the start of the application.

The `SCE_NP_GAME_INTENT_ERROR_NOT_INITIALIZED` error will be returned when an attempt is made to use other functions provided by the NpGameIntent library in a state where library initialization has not yet been performed.

## Examples

```
SceNpGameIntentInitParam initParam;

/* Initialize initialization parameters */
sceNpGameIntentInitParamInit( &initParam );

/* Initialize the NpGameIntent library */
ret = sceNpGameIntentInitialize( &initParam );
```

## Notes

This function is not multithread safe. Do not call this function at the same time from multiple threads.

## See Also

`sceNpGameIntentTerminate()`

# sceNpGameIntentTerminate

Terminates the library

## Definition

```
#include <np/np_game_intent.h>
int32_t sceNpGameIntentTerminate(
    void
)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_GAME_INTENT_ERROR_NOT_INITIALIZED` | 0x80553801 | Library is not initialized |
| `SCE_NP_GAME_INTENT_ERROR_UNKNOWN` | 0x80553800 | Undefined error that is not listed above |

## Description

This function terminates the NpGameIntent library.

## Examples

```
/* Terminate the NpGameIntent library */
ret = sceNpGameIntentTerminate();
```

## Notes

This function is not multithread safe. Do not call this function at the same time from multiple threads.

## See Also

`sceNpGameIntentInitialize()`