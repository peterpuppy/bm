# UserService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Reference/sce-user-service-initialize2.html

# Initialization/Termination

# SceUserServiceInitializeParams

Initialization parameters

## Definition

```
#include <user_service.h>
typedef struct SceUserServiceInitializeParams {
	int32_t priority;
} SceUserServiceInitializeParams;
```

## Members

|  |  |
| --- | --- |
| `priority` | Priority for the thread created in the library |

## Description

This structure is used for specifying the parameters when the library is initialized with `sceUserServiceInitialize()`.

For `priority`, specify a value from `SCE_KERNEL_PRIO_FIFO_HIGHEST` to `SCE_KERNEL_PRIO_FIFO_LOWEST`.

# sceUserServiceInitialize

Initializes the library

## Definition

```
#include <user_service.h>
int32_t sceUserServiceInitialize(
	const SceUserServiceInitializeParams *initParams
)
```

## Arguments

|  |  |
| --- | --- |
| `initParams` | Initialization parameters, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination. One thread will be started within the library.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_ALREADY_INITIALIZED` | 0x80960003 | Already initialized |
| `SCE_USER_SERVICE_ERROR_NO_MEMORY` | 0x80960004 | Could not allocate memory |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |

## Description

This function initializes the UserService library.

One thread will be generated in the library. The priority of this thread can be specified with `initParams`. If NULL is specified for `initParams`, the default priority (`SCE_KERNEL_PRIO_FIFO_DEFAULT`) will be considered to be specified.

## Examples

```
#include <kernel.h>
SceUserServiceInitializeParams params;
memset(&params, 0, sizeof(params));
params.priority = SCE_KERNEL_PRIO_FIFO_DEFAULT;
if (sceUserServiceInitialize(&params) < SCE_OK) {
	// Error handling
}
```

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.

## See Also

`sceUserServiceInitialize2()`, `sceUserServiceTerminate()`

# sceUserServiceInitialize2

Initializes the library

## Definition

```
#include <user_service.h>
int32_t sceUserServiceInitialize2(
	int threadPriority,
	SceKernelCpumask cpuAffinityMask
)
```

## Arguments

|  |  |
| --- | --- |
| `threadPriority` | Thread priority |
| `cpuAffinityMask` | CPU affinity mask for thread |

## Return Values

Returns `SCE_OK` (=0) for normal termination. One thread will be started within the library.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_ALREADY_INITIALIZED` | 0x80960003 | Already initialized |
| `SCE_USER_SERVICE_ERROR_NO_MEMORY` | 0x80960004 | Could not allocate memory |
| `SCE_USER_SERVICE_ERROR_INVALID_ARGUMENT` | 0x80960005 | Specified parameter is not appropriate |

## Description

This function initializes the UserService library.

One thread will be generated in the library. The priority and CPU affinity mask for this thread can be specified with `threadPriority` and `cpuAffinityMask`.

To explicitly specify a CPU affinity mask, use this function instead of `sceUserServiceInitialize()`.

## Examples

```
#include <kernel.h>
int ret = sceUserServiceInitialize2(
	SCE_KERNEL_PRIO_FIFO_DEFAULT, SCE_KERNEL_CPUMASK_13CPU);
if (ret < SCE_OK) {
	// Error handling
}
```

If the operation mode of the application is low energy mode, the maximum number CPUs that can be used is 8 (defined as `SCE_KERNEL_CPUMASK_8CPU`). For details, refer to [Kernel Overview - CPU Management - Overview of CPU Resources and CPU Management During Foreground Execution](../Kernel-Overview/cpu-resources-and-cpu-management-during-foreground-execution.html).

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.

## See Also

`sceUserServiceTerminate()`

# sceUserServiceTerminate

Terminates the library

## Definition

```
#include <user_service.h>
int32_t sceUserServiceTerminate(
	void
)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (negative value) for errors. The error codes defined by the UserService library are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | Not initialized |

## Description

This function terminates the UserService library.

The thread generated in the library will be terminated.

## Examples

```
if (sceUserServiceTerminate() < SCE_OK) {
	// Error handling
}
```

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.

## See Also

`sceUserServiceInitialize()`, `sceUserServiceInitialize2()`