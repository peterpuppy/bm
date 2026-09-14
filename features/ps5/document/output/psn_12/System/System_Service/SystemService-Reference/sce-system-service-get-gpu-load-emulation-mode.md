# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-get-gpu-load-emulation-mode.html

# Controlling GPU Load of the System Software

# sceSystemServiceSetGpuLoadEmulationMode

Set the GPU load mode of the system software

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceSetGpuLoadEmulationMode(
        SceSystemServiceGpuLoadEmulationMode mode
);
```

## Arguments

|  |  |
| --- | --- |
| `mode` | GPU load mode of the system software |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function sets the GPU load of the system software from two levels - none, normal.

The system software uses the GPU irrespective of the application's operational state and its load varies. Use this function to test the effects of this load on the application or to analyze the application's performance when there is no load (for example).

This function can only be used when the Release Check Mode of the Development Kit is set to Development Mode. In all other cases, the GPU load of the system software will not change even if this function is used.

## Notes

The GPU load mode of the system software can also be set by using "★Debug Settings" of the system software or "Target Settings" of Target Manager. The system software operates accordingly to the latest setting made, regardless of how that setting was made.

## See Also

`sceSystemServiceGetGpuLoadEmulationMode()`

# sceSystemServiceGetGpuLoadEmulationMode

Get the current GPU load mode of the system software

## Definition

```
#include <system_service.h>
SceSystemServiceGpuLoadEmulationMode sceSystemServiceGetGpuLoadEmulationMode();
```

## Arguments

None

## Return Values

Returns the current GPU load mode of the system software.

## Description

This function obtains the current GPU load mode of the system software. The GPU load mode set by a method other than `sceSystemServiceSetGpuLoadEmulationMode()` can also be obtained.

# SceSystemServiceGpuLoadEmulationMode

GPU load mode of the system software

## Definition

```
#include <system_service.h>
typedef enum SceSystemServiceGpuLoadEmulationMode;
```

## Description

This type indicates the GPU load mode of the system software. One of the following values can be used.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_GPU_LOAD_EMULATION_MODE_OFF` | 0 | Do not use the GPU (excluding when it is required by user operation or by the application) |
| `SCE_SYSTEM_SERVICE_GPU_LOAD_EMULATION_MODE_NORMAL` | 1 | Normal GPU load |

Note that even when `SCE_SYSTEM_SERVICE_GPU_LOAD_EMULATION_MODE_OFF` is set, dialog rendering by the system software (for example) will entail a GPU load if the controller's PS button is pressed or when the application calls a library that displays dialog.

## See Also

`sceSystemServiceSetGpuLoadEmulationMode()`, `sceSystemServiceGetGpuLoadEmulationMode()`