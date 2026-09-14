# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-launch-system-deeplink.html

# Launching Specific System Features

# sceSystemServiceLaunchSystemDeeplink

Launches a specific system feature

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceLaunchSystemDeeplink(
    SceUserServiceUserId userId,
    const char* param
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | The user ID of the user who is controlling the application |
| `param` | String (JSON format) passed to the specific system feature |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_INTERNAL` | 0x80A10001 | Unexpected internal error occurred |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | Parameter is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_INCORRECT_USER_ID` | 0x80A1000B | `userId` is invalid |
| `SCE_SYSTEM_SERVICE_ERROR_INVALID_PARAM_LEN` | 0x80A1000C | `param` string is too long |

## Description

This function launches specific features that come standard as part of the system.

For `param`, specify a JSON-format string that is prescribed for each feature that can be launched. For the features that can be started using this function and the strings to specify, see the following document that explains the relevant features. (The features that can be started using this function may be added in addition to those described in the document below.)

* [PlayStation™Network Game Help Guide - PlayStation™Network Game Help Overview - Opening a Consolidated Activity Card Using the SDK](../PSN_Game_Help-Guide/opening-a-consolidated-activity-card-using-the-sdk.html)

## Examples

```
/* If launching a Game Help activity card
 * Specify a JSON-format string for param */
const char *param = R"({"functionName":"gamehelp","screen":"consolidatedActivity"})";

ret = sceSystemServiceLaunchSystemDeeplink( userId , param );
```