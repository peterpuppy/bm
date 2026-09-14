# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-show-controller-settings.html

# Starting Controller Settings

# sceSystemServiceShowControllerSettings

Show the screen for performing controller settings

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceShowControllerSettings();
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function calls the "Controllers" settings screen in the system software and allows users to perform controller settings.

When this function is called, control immediately returns to the application, and the application transitions to background status.