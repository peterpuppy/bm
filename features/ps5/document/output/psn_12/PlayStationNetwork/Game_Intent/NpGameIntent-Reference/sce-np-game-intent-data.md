# NpGameIntent Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpGameIntent-Reference/sce-np-game-intent-data.html

# Receiving Game Intent Information

# SceNpGameIntentData

Game intent data

## Definition

```
#include <np/np_game_intent.h>
typedef struct SceNpGameIntentData {
    uint8_t data[SCE_NP_GAME_INTENT_DATA_MAX_SIZE];
    uint8_t padding[7];
} SceNpGameIntentData;
```

## Members

|  |  |
| --- | --- |
| `data` | Data area |
| `padding` | Padding areas |

## Description

This structure is used for storing game intent data. It is included in the game intent information (`SceNpGameIntentInfo` structure) received with `sceNpGameIntentReceiveIntent()`.

Do not directly reference the data area of this structure. Always use `sceNpGameIntentGetPropertyValueString()` to obtain property values.

# SceNpGameIntentInfo

Game intent information

## Definition

```
#include <np/np_game_intent.h>
typedef struct SceNpGameIntentInfo {
    size_t size;
    SceUserServiceUserId userId;
    char intentType[SCE_NP_GAME_INTENT_TYPE_MAX_SIZE];
    uint8_t padding[7];
    uint8_t reserved[256];
    SceNpGameIntentData intentData;
} SceNpGameIntentInfo;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID of the user who made the game intent event occur |
| `intentType` | Game intent event type (NULL terminated) |
| `padding` | Padding areas |
| `reserved` | Reserved areas |
| `intentData` | Game intent data |

## Description

This structure is used for storing game intent information received with `sceNpGameIntentReceiveIntent()`.

Use this structure after initializing it with `sceNpGameIntentInfoInit()`.

For `userId`, the user ID of the user who made the game intent event occur will be stored. An application supporting multiple users can use this user ID to identify the user who made the game intent event occur.

For `intentType`, a string indicating the game intent event type will be stored. Refer to the [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html) document for specifications of the type string. For an example of a typical implementation of receiving game intent information and obtaining the values of properties, refer to [NpGameIntent Library Overview - Using the Library - Implementation Example](../NpGameIntent-Overview/implementation-example.html).

# sceNpGameIntentInfoInit

Initializes game intent information

## Definition

```
#include <np/np_game_intent.h>
void sceNpGameIntentInfoInit(
    SceNpGameIntentInfo *p
)
```

## Arguments

|  |  |
| --- | --- |
| `p` | Target game intent information |

## Return Values

None

## Description

This function initializes the `SceNpGameIntentInfo` structure. Always initialize the `SceNpGameIntentInfo` structure with this function before passing it to `sceNpGameIntentReceiveIntent()`.

Appropriate initialization values will be set to the members of `*p` by calling this function. The application is not required to explicitly set values to members that are not used, such as the size and reserved areas.

## Examples

Refer to "Examples" of `sceNpGameIntentGetPropertyValueString()`.

# sceNpGameIntentReceiveIntent

Receives game intent information

## Definition

```
#include <np/np_game_intent.h>
int32_t sceNpGameIntentReceiveIntent(
    SceNpGameIntentInfo *intentInfo
)
```

## Arguments

|  |  |
| --- | --- |
| `intentInfo` | Destination to store the received game intent information |

## Return Values

Stores the received game intent information in `*intentInfo` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_GAME_INTENT_ERROR_NOT_INITIALIZED` | 0x80553802 | Library is not initialized |
| `SCE_NP_GAME_INTENT_ERROR_OUT_OF_MEMORY` | 0x80553803 | Insufficient memory |
| `SCE_NP_GAME_INTENT_ERROR_INVALID_ARGUMENT` | 0x80553804 | * `intentInfo` is NULL * One of the `intentInfo` members is invalid |
| `SCE_NP_GAME_INTENT_ERROR_INTENT_NOT_FOUND` | 0x80553806 | Game intent information does not exist |
| `SCE_NP_GAME_INTENT_ERROR_UNKNOWN` | 0x80553800 | Undefined error that is not listed above |

## Description

This function receives game intent information. This function can be used to receive game intent information when the occurrence of a game intent event is notified by the feature of the SystemService library that obtains event occurrence notifications.

The receiving of game intent information can fail when, for example, a second game intent event occurs before information of the first event is received. The `SCE_NP_GAME_INTENT_ERROR_INTENT_NOT_FOUND` error will be returned in such cases. Program your application so that it does not malfunction when failing to receive game intent information.

## Examples

Refer to "Examples" of `sceNpGameIntentGetPropertyValueString()`.

# sceNpGameIntentGetPropertyValueString

Gets a property value

## Definition

```
#include <np/np_game_intent.h>
int32_t sceNpGameIntentGetPropertyValueString(
    const SceNpGameIntentData *intentData,
    const char *key,
    char *valueBuf,
    size_t bufSize
)
```

## Arguments

|  |  |
| --- | --- |
| `intentData` | Game intent data |
| `key` | Name string of the property to obtain (NULL terminated) |
| `valueBuf` | Buffer to store the value string of the property to obtain (NULL terminated) |
| `bufSize` | Size of `valueBuf` |

## Return Values

Stores the obtained property value in `*valueBuf` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_GAME_INTENT_ERROR_NOT_INITIALIZED` | 0x80553802 | Library is not initialized |
| `SCE_NP_GAME_INTENT_ERROR_OUT_OF_MEMORY` | 0x80553803 | Insufficient memory |
| `SCE_NP_GAME_INTENT_ERROR_INVALID_ARGUMENT` | 0x80553804 | `intentData`, `key`, or `valueBuf` is NULL |
| `SCE_NP_GAME_INTENT_ERROR_INSUFFICIENT_BUFFER` | 0x80553805 | Insufficient buffer |
| `SCE_NP_GAME_INTENT_ERROR_VALUE_NOT_FOUND` | 0x80553807 | Property value doesn't exist |
| `SCE_NP_GAME_INTENT_ERROR_UNKNOWN` | 0x80553800 | Undefined error that is not listed above |

## Description

This function obtains the value of each property from game intent data.

Specify the `SceNpGameIntentData` structure included in the `SceNpGameIntentInfo` structure received with `sceNpGameIntentReceiveIntent()`, the name string of the property to obtain, and the buffer for storing the property value string as arguments. The successfully obtained property value will be stored in `*valueBuf` as a NULL terminated string. The `SCE_NP_GAME_INTENT_ERROR_VALUE_NOT_FOUND` error will be returned if the property value doesn't exist.

The property value that can be obtained differ by the game intent event type. Maximum size is determined per property; make sure to specify a sufficient buffer size for `bufSize`. The `SCE_NP_GAME_INTENT_ERROR_INSUFFICIENT_BUFFER` error will be returned if the specified size is insufficient.

Refer to the [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html) document for property name strings and maximum sizes of property values that can be obtained for each game intent event type.

## Examples

```
#define PLAYER_SESSION_ID_MAX_SIZE  (37)

SceNpGameIntentInfo intentInfo;

/* Initialize game intent information */
sceNpGameIntentInfoInit( &intentInfo );

/* Receive game intent information */
ret = sceNpGameIntentReceiveIntent( &intentInfo );

/* Obtain a property value */
char playerSessionId[PLAYER_SESSION_ID_MAX_SIZE];
ret = sceNpGameIntentGetPropertyValueString(
&intentInfo.intentData, "playerSessionId",
playerSessionId, sizeof(playerSessionId) );
```

## See Also

`SceNpGameIntentData`