# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-get-hdr-tone-map-luminance.html

# Obtaining HDR Display Parameters

# sceSystemServiceGetHdrToneMapLuminance

Obtain HDR display parameters

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceGetHdrToneMapLuminance(
	SceSystemServiceHdrToneMapLuminance* hdrToneMapLuminance
);
```

## Arguments

|  |  |
| --- | --- |
| `hdrToneMapLuminance` | Destination to store obtained HDR display parameters |

## Return Values

Stores the obtained HDR display parameters in `*hdrToneMapLuminance` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function obtains the luminance range that the connected TV/display can display (tone map information).

The obtained tone map information is what the user set using "Adjust HDR" in the system software. If this setting has not been configured, values approximating the Category 2 preset values defined in the HDR Gaming Interest Group's Display Category Definitions will be returned, as prescribed by the group's guidelines.

For information about the guidelines, refer to the following link:

* <https://www.hgig.org/>

## Notes

Use the information obtained using this function only as parameters for graphics rendering. Displaying the information obtained using this function on-screen as numerical values is prohibited, because doing so could confuse consumers about TV/display performance.

# SceSystemServiceHdrToneMapLuminance

HDR display parameters

## Definition

```
#include <system_service.h>
typedef struct SceSystemServiceHdrToneMapLuminance {
	float maxFullFrameToneMapLuminance;
	float maxToneMapLuminance;
	float minToneMapLuminance;
} SceSystemServiceHdrToneMapLuminance;
```

## Members

|  |  |
| --- | --- |
| `maxFullFrameToneMapLuminance` | Maximum input luminance at which gradation is preserved even when the entire screen is bright (MaxFFTML) |
| `maxToneMapLuminance` | Maximum input luminance at which gradation is preserved when 10% of the screen is bright (MaxTML) |
| `minToneMapLuminance` | Minimum input luminance at which gradation is identifiable (MinTML) |

## Description

This structure is used when obtaining HDR display parameters with `sceSystemServiceGetHdrToneMapLuminance()`.

Each parameter is expressed as a value, in units of nits, from 0.0 to 10000.0.