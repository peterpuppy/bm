# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-get-notice-screen-skip-flag.html

# Controlling the Notice Screen Skip Flag

# sceSystemServiceGetNoticeScreenSkipFlag

Obtain the value of the Notice Screen Skip flag

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceGetNoticeScreenSkipFlag(
    bool* value
);
```

## Arguments

|  |  |
| --- | --- |
| `value` | Destination to store the obtained value |

## Return Values

Stores the obtained value of the Notice Screen Skip flag in `*value` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function obtains the value of the Notice Screen Skip flag immediately after the application is launched.

If the obtained value is true, the application should skip over displaying warnings, logos, and other notice screens. For details, refer to the "Controlling the Notice Screen Skip Flag" section of the "Using the Library" chapter of the [SystemService Library Overview](../SystemService-Overview/__document_toc.html) document. The value returned by the function for the flag will not change until the application is terminated. Even if the system software or the application modifies the value of the flag, the function will continue to return a consistent value.

## See Also

`sceSystemServiceDisableNoticeScreenSkipFlagAutoSet()`, `sceSystemServiceSetNoticeScreenSkipFlag()`

# sceSystemServiceDisableNoticeScreenSkipFlagAutoSet

Put the Notice Screen Skip flag in manually set mode

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceDisableNoticeScreenSkipFlagAutoSet();
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function puts the Notice Screen Skip flag in manually set mode.

When this function has been called, the system software will no longer change the Notice Screen Skip flag to true after a certain amount of time elapses after the application is launched. Instead, the application will now be able to call `sceSystemServiceSetNoticeScreenSkipFlag()` to change the Notice Screen Skip flag to true.

## Notes

Use this function promptly after the application is launched if using manually set mode.

Once the Notice Screen Skip flag has been automatically changed to true by the system software, the state of the flag will not be turned back to false even if the function is called. In this case, the function will return an error code (a negative value).

The system software changes the value of this flag back to false when the application is updated. This behavior is unchanged in manually set mode.

# sceSystemServiceSetNoticeScreenSkipFlag

Change the Notice Screen Skip flag to true

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceSetNoticeScreenSkipFlag();
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for an error. (Refer to "[Return Codes](ps5-return-codes.html)" for details.)

## Description

This function changes the Notice Screen Skip flag to true. However, `sceSystemServiceDisableNoticeScreenSkipFlagAutoSet()` must be called beforehand to enter manually set mode. If not in manually set mode, the attempt to change the flag will fail and an error will occur.

## Notes

There is no way to manually change the Notice Screen Skip flag to false.