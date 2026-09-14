# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-report-abnormal-termination.html

# Handling a Fatal Abnormal State

# sceSystemServiceReportAbnormalTermination

Report a fatal abnormal state and terminate the application

## Definition

```
#include <system_service.h>
typedef struct SceSystemServiceAbnormalTerminationInfo SceSystemServiceAbnormalTerminationInfo;

int32_t sceSystemServiceReportAbnormalTermination(
	const SceSystemServiceAbnormalTerminationInfo* info
);
```

## Arguments

|  |  |
| --- | --- |
| `info` | Reserved (specify NULL) |

## Return Values

When the execution of this function is properly carried out, the function call will not return.

Returns `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` when a value other than NULL is provided to `info`.

## Description

The application can call this function to immediately abort its execution. Use this function when entering a fatal abnormal state in which proper program operation cannot be continued.

Specify NULL to `info`. The `SceSystemServiceAbnormalTerminationInfo` structure is defined for reservation but cannot be used.

Application developers can use this function to examine the state of the application, immediately after detecting an abnormal state, via a debugger or the core dump system.

When this function is called, the system software will report the occurrence of an error to the user, determine the application has crashed due to a problem, and forcefully terminate the application in the same manner as when a process exception (invalid memory access, for example) occurs. However, if this function is called on a Development Kit with the Release Check Mode set to Development Mode, the system software will only abort application execution.