# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-reenable-music-player.html

# Controlling Media Playback

# sceSystemServiceDisableMediaPlay

Prohibit media playback by the system software

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceDisableMediaPlay();
```

## Arguments

None

## Return Values

Always returns `SCE_OK` (=0).

## Description

After this function is called, the system software will no longer play back audio or video media at the same time as the application.

To re-enable background playback, call `sceSystemServiceReenableMediaPlay()`.

Because this function may take some time to return when it is called successively, don't call it for every frame. Call it once when you want to switch the settings.

# sceSystemServiceReenableMediaPlay

Re-enable media playback by the system software

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceReenableMediaPlay();
```

## Arguments

None

## Return Values

Always returns `SCE_OK` (=0).

## Description

When this function is called, media playback disabled by `sceSystemServiceDisableMediaPlay()` will be re-enabled.

Because this function may take some time to return when it is called successively, don't call it for every frame. Call it once when you want to switch the settings.

# sceSystemServiceDisableMusicPlayer

Prohibit media playback by the system software [non-recommended API call]

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceDisableMusicPlayer();
```

## Arguments

None

## Return Values

Always returns `SCE_OK` (=0).

## Description

This function has been left in for source code compatibility with old versions of the SDK. Calling this function has the same effect as `sceSystemServiceDisableMediaPlay()`.

# sceSystemServiceReenableMusicPlayer

Re-enable media playback by the system software [non-recommended API call]

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceReenableMusicPlayer();
```

## Arguments

None

## Return Values

Always returns `SCE_OK` (=0).

## Description

This function has been left in for source code compatibility with old versions of the SDK. Calling this function has the same effect as `sceSystemServiceReenableMediaPlay()`.