# NpBandwidthTest Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpBandwidthTest-Reference/sce-np-bandwidth-test-get-status.html

# Bandwidth Measurement

# SceNpBandwidthTestInitParam

Parameters for initializing bandwidth measurement

## Definition

```
#include <np.h>
typedef struct SceNpBandwidthTestInitParam {
	size_t size;
	int threadPriority;
	char padding[4];
	SceKernelCpumask cpuAffinityMask;
	uint32_t reserved[8];
} SceNpBandwidthTestInitParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Structure size |
| `threadPriority` | Priority of the internal thread, or 0 |
| `padding` | Not used |
| `cpuAffinityMask` | Affinity mask of the internal thread, or 0 |
| `reserved` | Reserved area (clear with 0's) |

## Description

This structure represents the initialization parameters for bandwidth measurement specified upon calling `sceNpBandwidthTestInitStartUpload()` or `sceNpBandwidthTestInitStartDownload()`.

For `size`, specify the size of this structure.

For `threadPriority`, specify the priority of the internal thread for carrying out bandwidth measurement processing. Use of the `SCE_KERNEL_PRIO_*` macro is recommended. When 0 is specified, the system will set the priority.

For `cpuAffinityMask`, set the affinity mask. Use of the `SCE_KERNEL_CPUMASK_*` macro is recommended. When 0 is specified, the system will set the affinity mask.

`reserved` is a reserved area. Clear with 0's.

## See Also

`sceNpBandwidthTestInitStartUpload()`, `sceNpBandwidthTestInitStartDownload()`

# SceNpBandwidthTestResult

Results of bandwidth measurement

## Definition

```
#include <np.h>
typedef struct SceNpBandwidthTestResult {
	double uploadBps;
	double downloadBps;
	int result;
	uint8_t padding[4];
} SceNpBandwidthTestResult;
```

## Members

|  |  |
| --- | --- |
| `uploadBps` | Upload rate (bit per second) |
| `downloadBps` | Download rate (bit per second) |
| `result` | Measurement result code (0: normal termination) |
| `padding` | Not used |

## Description

This structure represents the results of bandwidth measurement retrieved with `sceNpBandwidthTestShutdown()`.

If measurement terminates normally, 0 will be stored in `result`. If any error occurs during measurement, an error code representing the cause of the error will be stored.

If measurement is aborted with `sceNpBandwidthTestAbort()` or when it times out, the applicable result code will be stored in `result`, and the bandwidth will be calculated based on measurement results up to that point.

The measured bandwidth will be stored in `uploadBps` and `downloadBps`. 0 will be set if the bandwidth could not be calculated.

## See Also

`sceNpBandwidthTestShutdown()`

# sceNpBandwidthTestAbort

Force termination of bandwidth measurement

## Definition

```
#include <np.h>
int sceNpBandwidthTestAbort(
	int contextId
);
```

## Arguments

|  |  |
| --- | --- |
| `contextId` | NpBandwidthTest library context ID |

## Return Values

Returns 0 upon normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_ERROR_CONTEXT_NOT_AVAILABLE` | 0x80551f07 | Specified context cannot be used |

## Description

This function aborts bandwidth measurement.

Even when measurement is aborted with this function, always call `sceNpBandwidthTestShutdown()` to carry out termination processing.

Even when measurement is aborted with this function, bandwidth will be calculated based on the results obtained up to the call of the function.

## See Also

`sceNpBandwidthTestInitStartUpload()`, `sceNpBandwidthTestInitStartDownload()`, `sceNpBandwidthTestShutdown()`

# sceNpBandwidthTestGetStatus

Obtain progress of bandwidth measurement

## Definition

```
#include <np.h>
int sceNpBandwidthTestGetStatus(
	int contextId,
	int *status
);
```

## Arguments

|  |  |
| --- | --- |
| `contextId` | NpBandwidthTest library context ID |
| `status` | Destination to store progress of bandwidth measurement |

## Return Values

Stores the constant representing the progress in `*status` and returns 0 upon normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_ARGUMENT` | 0x80551f05 | Address specified in `status` is invalid |
| `SCE_NP_BANDWIDTH_TEST_ERROR_CONTEXT_NOT_AVAILABLE` | 0x80551f07 | Specified context cannot be used |

## Description

This function obtains the progress of bandwidth measurement started with `sceNpBandwidthTestInitStartUpload()` or `sceNpBandwidthTestInitStartDownload()`.

The obtained result will be returned as one of the following values in `*status`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_STATUS_NONE` | 0 | Measurement not started yet |
| `SCE_NP_BANDWIDTH_TEST_STATUS_RUNNING` | 1 | Measuring |
| `SCE_NP_BANDWIDTH_TEST_STATUS_FINISHED` | 2 | Measuring complete (including termination by error) |

## See Also

`sceNpBandwidthTestInitStartUpload()`, `sceNpBandwidthTestInitStartDownload()`, `sceNpBandwidthTestShutdown()`

# sceNpBandwidthTestInitStartUpload

Start bandwidth measurement for an upload

## Definition

```
#include <np.h>
int sceNpBandwidthTestInitStartUpload(
	const SceNpBandwidthTestInitParam *param,
	uint32_t timeOutInUsec
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Initialization parameters for the internal thread |
| `timeOutInUsec` | Timeout time (microseconds) |

## Return Values

Returns the NpBandwidthTest library context ID (a value of 0 or more) upon normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_ERROR_OUT_OF_MEMORY` | 0x80551f04 | Memory required for execution could not be allocated |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_ARGUMENT` | 0x80551f05 | Specified argument is invalid |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_SIZE` | 0x80551f06 | Specified size is invalid |

## Description

This function starts bandwidth measurement for an upload.

When this function call succeeds, an internal thread is generated based on the specified `param` and bandwidth measurement is started; this function itself will return without blocking. Use `sceNpBandwidthTestGetStatus()` to check whether measurement completed or not.

Specify a timeout time other than 0 in microseconds to `timeOutInUsec` in order to set a timeout time for bandwidth measurement.

When bandwidth measurement times out, bandwidth will be calculated based on the results obtained up to the timeout.

## See Also

`sceNpBandwidthTestInitStartDownload()`, `sceNpBandwidthTestGetStatus()`, `sceNpBandwidthTestShutdown()`, `sceNpBandwidthTestAbort()`

# sceNpBandwidthTestInitStartDownload

Start bandwidth measurement for a download

## Definition

```
#include <np.h>
int sceNpBandwidthTestInitStartDownload(
	const SceNpBandwidthTestInitParam *param,
	uint32_t timeOutInUsec
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Initialization parameters for the internal thread |
| `timeOutInUsec` | Timeout time (microseconds) |

## Return Values

Returns the NpBandwidthTest library context ID (a value of 0 or more) upon normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_ERROR_OUT_OF_MEMORY` | 0x80551f04 | Memory required for execution could not be allocated |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_ARGUMENT` | 0x80551f05 | Specified argument is invalid |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_SIZE` | 0x80551f06 | Specified size is invalid |

## Description

This function starts bandwidth measurement for a download.

When this function call succeeds, an internal thread is generated based on the specified `param` and bandwidth measurement is started; this function itself will return without blocking. Use `sceNpBandwidthTestGetStatus()` to check whether measurement completed or not.

Specify a timeout time other than 0 in microseconds to `timeOutInUsec` in order to set a timeout time for bandwidth measurement.

When bandwidth measurement times out, bandwidth will be calculated based on the results obtained up to the timeout.

## See Also

`sceNpBandwidthTestInitStartUpload()`, `sceNpBandwidthTestGetStatus()`, `sceNpBandwidthTestShutdown()`, `sceNpBandwidthTestAbort()`

# sceNpBandwidthTestShutdown

Terminate bandwidth measurement and get result

## Definition

```
#include <np.h>
int sceNpBandwidthTestShutdown(
	int contextId,
	SceNpBandwidthTestResult *result
);
```

## Arguments

|  |  |
| --- | --- |
| `contextId` | NpBandwidthTest library context ID |
| `result` | Storage destination of bandwidth measurement results |

## Return Values

Stores the measurement result in `*result` and returns 0 upon normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_ARGUMENT` | 0x80551f05 | Address specified in `result` is invalid |
| `SCE_NP_BANDWIDTH_TEST_ERROR_CONTEXT_NOT_AVAILABLE` | 0x80551f07 | Specified context cannot be used |

## Description

This function simultaneously performs termination of bandwidth measurement and result obtainment.

Since the internal thread created with `sceNpBandwidthTestInitStartUpload()` or `sceNpBandwidthTestInitStartDownload()` is deleted in this function, always call this function after the call of `sceNpBandwidthTestInitStartUpload()` or `sceNpBandwidthTestInitStartDownload()` succeeds, including when processing is aborted with `sceNpBandwidthTestAbort()`.

## Notes

An error does not occur when this function is called while bandwidth measurement is ongoing; however, the correct result (including the appropriate error code) cannot be obtained. Call this function after obtaining `SCE_NP_BANDWIDTH_TEST_STATUS_FINISHED` from `sceNpBandwidthTestGetStatus()`, or after calling `sceNpBandwidthTestAbort()`.

When sceNpBandwidthTestShutdown() (this function) is called before bandwidth measurement is complete, blocking may be performed for long periods in order to abort communication. This function must not be called from a time-critical thread.

## See Also

`sceNpBandwidthTestInitStartUpload()`, `sceNpBandwidthTestInitStartDownload()`