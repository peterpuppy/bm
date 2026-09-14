# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-power-tick.html

# Controlling the Power

# sceSystemServicePowerTick

Prevent transition to the power save state

## Definition

```
#include <system_service.h>
int32_t sceSystemServicePowerTick();
```

## Arguments

None

## Return Values

Always returns `SCE_OK` (=0).

## Description

When there is no input from the user for a long period of time while the application is running, the system software may transition the system hardware to the power save state. When transitioning to the power save state, application execution will not be continued.

When this function is called, the system software will not carry out transition to the power save state for a certain period of time even if the state in which there is no input from the user continues. (The time extension varies by user settings and the system software version.)

To continuously prevent transition to the power save state, continue periodically calling this function with an interval between calls of no longer than one minute.

However, do not use this function unnecessarily as it will hinder saving electricity.