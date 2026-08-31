# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/sce-np-trophy-2unregister-unlock-callback.html

# Detecting Unlocking

# SceNpTrophy2UnlockCallback

Callback for when unlocking occurs

## Definition

```
typedef void (*SceNpTrophy2UnlockCallback)(
    SceNpTrophy2Context context,
    SceNpTrophy2Id trophyId,
    void *userdata
);
```

## Members

|  |  |
| --- | --- |
| `context` | [In] Context of the trophy set and user related to the unlocked trophy |
| `trophyId` | [In] Trophy ID of the trophy that was unlocked |
| `userdata` | [In] User data set at the time of callback registration |

## Description

This is a prototype for a callback function that receives notifications when unlocking occurs. When you want to monitor unlocking, use `sceNpTrophy2RegisterUnlockCallback()` to register a function that matches the prototype's specifications. When monitoring is no longer required, use `sceNpTrophy2UnregisterUnlockCallback()` to unregister the function.

After `sceNpTrophy2RegisterUnlockCallback()` has been used to register your function, the callback function will be called, and an unlocking notification will be issued when the application calls `sceNpCheckCallback()`.

## Notes

Avoid processing that would require large amounts of time within the callback and return promptly.

# sceNpTrophy2RegisterUnlockCallback

Register a callback to receive notifications of trophy unlocking

## Definition

```
#include <np.h>
int sceNpTrophy2RegisterUnlockCallback(
    SceNpTrophy2UnlockCallback callback,
    void *userdata
)
```

## Arguments

|  |  |
| --- | --- |
| `callback` | [In] Callback function to register |
| `userdata` | [In] User data passed to the callback function |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |

## Description

This function is for registering a callback function that receives notifications when trophies are unlocked. If there is no need to receive such notifications, you do not need to register a callback function.

After a callback has been registered, periodic calling of `sceNpCheckCallback()` will cause the callback function to be called as required. For details about `sceNpCheckCallback()`, refer to the [Np Library Reference](../Np-Reference/__document_toc.html) document.

## See Also

`sceNpTrophy2UnregisterUnlockCallback()`

# sceNpTrophy2UnregisterUnlockCallback

Unregister a callback that received notifications of trophy unlocking

## Definition

```
#include <np.h>
int sceNpTrophy2UnregisterUnlockCallback(
    void
)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors.

## Description

This function unregisters any currently registered callback function that receives notifications of trophy unlocking. The function will terminate normally without doing anything if no callback function has been registered.

## See Also

`sceNpTrophy2RegisterUnlockCallback()`