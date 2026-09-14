# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-load-exec.html

# Switching Executable Files

# sceSystemServiceLoadExec

Switch the application's executable files

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceLoadExec(
	const char* path,
	char* const argv[]
);
```

## Arguments

|  |  |
| --- | --- |
| `path` | Path of executable file to switch to |
| `argv` | Argument to pass to the `main()` function of the program to switch to, or NULL |

## Return Values

This function does not return for normal execution.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | Invalid value specified to `argv` |
| `SCE_SYSTEM_SERVICE_ERROR_REJECTED` | 0x80A10005 | Save data is being updated and a switch cannot be made |
| Other errors | Negative value | Fatal error |

## Description

This function switches the program to execute to the file specified in `path`. When the switch is successful, the process that called this function immediately terminates. Execution - of the global destructor, for example - is not carried out.

The switch fails when save data is being updated.

For `path`, only a file under `/app0/` can be specified.

The last element of the array specified to `argv` must be NULL. The total length of all elements including NULL termination must be within `SCE_SYSTEM_SERVICE_MAX_ARGV_SIZE` bytes.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_MAX_ARGV_SIZE` | 4096 | Maximum size of argument to pass to execution program |

If an argument is not to be passed, specify NULL to `argv`.