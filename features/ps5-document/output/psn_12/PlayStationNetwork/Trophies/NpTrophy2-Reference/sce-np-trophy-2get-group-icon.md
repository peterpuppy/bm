# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/sce-np-trophy-2get-group-icon.html

# Obtaining Icons

# sceNpTrophy2GetGameIcon

Get trophy set still-image icon

## Definition

```
#include <np.h>
int sceNpTrophy2GetGameIcon(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    void *buffer,
    size_t *size
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `buffer` | [Out] Destination to store the obtained icon data, or NULL |
| `size` | [In/Out] Required size for `buffer[]`, or the size of the obtained icon data |

## Return Values

Stores the obtained icon data in `buffer[]` (if `buffer` is not NULL), stores the icon data size in `*size`, and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |
| `SCE_NP_TROPHY2_ERROR_ICON_FILE_NOT_FOUND` | 0x80553911 | Icon file cannot be found |

## Description

This function obtains the trophy set still-image icon included in the trophy set for the specified `context`.

The icon data will be stored in the area specified with `buffer` as a PNG image. Prepare an appropriate buffer, and then specify its address for `buffer` and specify its size for `*size`.

In order to determine the exact buffer size necessary for storing the icon, call this function with `buffer` set to NULL and a pointer to an appropriate variable specified for `size`. The necessary size will be calculated and stored in `*size`.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
int ret;
void *buf = NULL;
size_t s = 0;

ret = sceNpTrophy2GetGameIcon(context, handle, NULL, &s);
if ( ret < 0 ) {
    // Error handling
}
buf = malloc(s);
if (buf == NULL) {
    // Error handling
}
ret = sceNpTrophy2GetGameIcon(context, handle, buf, &s);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`

# sceNpTrophy2GetGroupIcon

Get trophy group still-image icon

## Definition

```
#include <np.h>
int sceNpTrophy2GetGroupIcon(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    SceNpTrophy2GroupId groupId,
    void *buffer,
    size_t *size
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `groupId` | [In] Group ID |
| `buffer` | [Out] Destination to store the obtained icon data, or NULL |
| `size` | [In/Out] Required size for `buffer[]`, or the size of the obtained icon data |

## Return Values

Stores the obtained icon data in `buffer[]` (if `buffer` is not NULL), stores the icon data size in `*size`, and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_INVALID_GROUP_ID` | 0x8055390b | Invalid group ID |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |
| `SCE_NP_TROPHY2_ERROR_ICON_FILE_NOT_FOUND` | 0x80553911 | Icon file cannot be found |

## Description

This function obtains the still-image icon of the trophy group specified with `context` and `groupId`.

Specify the ID of the trophy group you want to obtain information of to `groupId`. If you want to obtain information of the base game group, specify `SCE_NP_TROPHY2_BASE_GAME_GROUP_ID`.

The icon data will be stored in the area specified with `buffer` as a PNG image. Prepare an appropriate buffer, and then specify its address for `buffer` and specify its size for `*size`.

In order to determine the exact buffer size necessary for storing the icon, call this function with `buffer` set to NULL and a pointer to an appropriate variable specified for `size`. The necessary size will be calculated and stored in `*size`.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2GroupId groupId;
int ret;
void *buf = NULL;
size_t s = 0;

ret = sceNpTrophy2GetGroupIcon(context, handle, groupId, NULL, &s);
if ( ret < 0 ) {
    // Error handling
}
buf = malloc(s);
if (buf == NULL) {
    // Error handling
}
ret = sceNpTrophy2GetGroupIcon(context, handle, groupId, buf, &s);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`

# sceNpTrophy2GetTrophyIcon

Get trophy still-image icon

## Definition

```
#include <np.h>
int sceNpTrophy2GetTrophyIcon(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    SceNpTrophy2Id trophyId,
    void *buffer,
    size_t *size
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `trophyId` | [In] Trophy ID |
| `buffer` | [Out] Destination to store the obtained icon data, or NULL |
| `size` | [In/Out] Required size for `buffer[]`, or the size of the obtained icon data |

## Return Values

Stores the obtained icon data in `buffer[]` (if `buffer` is not NULL), stores the icon data size in `*size`, and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_INVALID_TROPHY_ID` | 0x8055390a | Invalid trophy ID |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |
| `SCE_NP_TROPHY2_ERROR_ICON_FILE_NOT_FOUND` | 0x80553911 | Icon file cannot be found |

## Description

This function obtains the still-image icon of the trophy specified with `context` and `trophyId`.

The icon data is stored in the area specified with `buffer` as a PNG image. Prepare an appropriate buffer, and then specify its address for `buffer` and specify its size for `*size`.

In order to determine the exact buffer size necessary for storing the icon, call this function with `buffer` set to NULL and a pointer to an appropriate variable specified for `size`. The necessary size will be calculated and stored in `*size`.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2Id trophyId;
int ret;
void *buf = NULL;
size_t s = 0;

ret = sceNpTrophy2GetTrophyIcon(context, handle, trophyId, NULL, &s);
if ( ret < 0 ) {
    // Error handling
}
buf = malloc(s);
if (buf == NULL) {
    // Error handling
}
ret = sceNpTrophy2GetTrophyIcon(context, handle, trophyId, buf, &s);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`

# sceNpTrophy2GetRewardIcon

Obtain a reward icon

## Definition

```
#include <np.h>
int sceNpTrophy2GetRewardIcon(
    SceNpTrophy2Context context,
    SceNpTrophy2Handle handle,
    SceNpTrophy2Id trophyId,
    void *buffer,
    size_t *size
)
```

## Arguments

|  |  |
| --- | --- |
| `context` | [In] Context |
| `handle` | [In] Handle |
| `trophyId` | [In] Trophy ID |
| `buffer` | [Out] Destination to store the obtained icon data, or NULL |
| `size` | [In/Out] Required size for `buffer[]`, or the size of the obtained icon data |

## Return Values

Stores the obtained icon data in `buffer[]` (if `buffer` is not NULL), stores the icon data size in `*size`, and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_INVALID_TROPHY_ID` | 0x8055390a | Invalid trophy ID |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |
| `SCE_NP_TROPHY2_ERROR_ICON_FILE_NOT_FOUND` | 0x80553911 | Icon file cannot be found |

## Description

This function obtains the reward icon for the trophy specified with `context` and `trophyId`.

The icon data is stored in the area specified with `buffer` as a PNG image. Prepare an appropriate buffer, and then specify its address for `buffer` and specify its size for `*size`.

In order to determine the exact buffer size necessary for storing the icon, call this function with `buffer` set to NULL and a pointer to an appropriate variable specified for `size`. The necessary size will be calculated and stored in `*size`.

## Examples

```
extern SceNpTrophy2Context context;
extern SceNpTrophy2Handle handle;
extern SceNpTrophy2Id trophyId;
int ret;
void *buf = NULL;
size_t s = 0;

ret = sceNpTrophy2GetRewardIcon(context, handle, trophyId, NULL, &s);
if ( ret < 0 ) {
    // Error handling
}
buf = malloc(s);
if (buf == NULL) {
    // Error handling
}
ret = sceNpTrophy2GetRewardIcon(context, handle, trophyId, buf, &s);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpTrophy2CreateContext()`, `sceNpTrophy2CreateHandle()`