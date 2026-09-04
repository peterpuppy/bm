# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/sce-np-trophy-2show-trophy-list.html

# Calling System Software Features

# sceNpTrophy2ShowTrophyList

Display the trophy list screen

## Definition

```
#include <np.h>
int sceNpTrophy2ShowTrophyList(
    SceNpTrophy2Context context
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_CONTEXT` | 0x80553909 | Invalid context |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |

## Description

This function calls the system software's trophy application and transitions the screen to the screen displaying the trophy set specified with `context`.

`context` must be registered in advance with `sceNpTrophy2RegisterContext()`.

## Examples

```
extern SceNpTrophy2Context context;
int ret;

ret = sceNpTrophy2ShowTrophyList (context)
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpTrophy2CreateContext()`