# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-hide-splash-screen.html

# Clearing the Splash Screen

# sceSystemServiceHideSplashScreen

Stop display of the startup image

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceHideSplashScreen();
```

## Arguments

None

## Return Values

Always returns `SCE_OK` (=0).

## Description

This function stops the system software from displaying the startup image included in the package that is used as a splash screen when the application is launched so that an image rendered by the application can be displayed. For information about startup images, refer to [Content Information Specifications - Startup Image [Application Information]](../Content_Information-Specifications/startup-image-application-information.html).