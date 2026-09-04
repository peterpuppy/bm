# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/sce-np-session-signaling-initialize.html

# Initialization/Termination

# SceNpSessionSignalingInitParam

Initialization parameters

## Definition

```
#include <np.h>
typedef struct SceNpSessionSignalingInitParam {
    int libhttp2CtxId;
    size_t poolSize;
    SceKernelCpumask cpuAffinityMask;
    int32_t threadPriority;
    size_t threadStackSize;
} SceNpSessionSignalingInitParam;
```

## Members

|  |  |
| --- | --- |
| `libhttp2CtxId` | Context ID of the Http2 library |
| `poolSize` | Memory pool size for the NpSessionSignaling library in bytes |
| `cpuAffinityMask` | CPU affinity mask of internal threads |
| `threadPriority` | Priority of internal threads |
| `threadStackSize` | Stack size of internal threads in bytes |

## Description

This structure is used for specifying the parameters when initializing the library with `sceNpSessionSignalingInitialize()`.

For`libhttp2CtxId`, specify the Http2 library context ID obtained by calling `sceHttp2Init()`.

For `poolSize`, specify the memory pool size for the NpSessionSignaling Library.

For `cpuAffinityMask`, `threadPriority`, and `threadStackSize`, specify the CPU affinity mask, thread priority, and stack size of the internal threads.

If 0 is specified for `cpuAffinityMask`, the same CPU affinity mask as the caller thread will be applied.

`threadStackSize` only affects those internal threads that are called by callback functions. If the size specified for `threadStackSize` is too small, it will be increased and set to the required size internally by the NpSessionSignaling library.

## Notes

When attempting to establish multiple P2P connections at the same time, it may take time for the connections to be established. In such cases, the time entailed in establishing P2P connections can be reduced by increasing the maximum number of simultaneous connections specified to `sceHttp2Init()`. As a general guideline for the maximum number of simultaneous connections, setting the maximum to at least twice the number of P2P connections that you are attempting to establish simultaneously will optimize the amount of time required for connection.

Because the Http2 library requires a memory pool of the size corresponding to the maximum number of simultaneous connections, when increasing the maximum number of simultaneous connections, refer to [Http2 Library Overview - Library Overview - Resources Used](../Http2-Overview/resources-used.html) and specify a sufficient memory pool size.

Additionally, if the same Http2 context will also be used by other communications, it will need to be increased by that amount, as well.

# sceNpSessionSignalingInitialize

Initializes the library

## Definition

```
#include <np.h>
int sceNpSessionSignalingInitialize(
    const SceNpSessionSignalingInitParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Library initialization parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_ALREADY_INITIALIZED` | 0x80553302 | Already initialized |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `param` is NULL * One of the `param` members is invalid |
| `SCE_NP_SESSION_SIGNALING_ERROR_OUT_OF_MEMORY` | 0x80553305 | Could not allocate memory |

## Description

This function initializes the NpSessionSignaling library.

For `param`, specify the initialization parameter structure set with the context ID of the Http2 library, memory pool size, and so forth.

Internal threads for the NpSessionSignaling library will be created upon initialization. The CPU affinity mask, priority, and stack size of these internal threads can be specified with `param`.

## Examples

```
// Assuming that the appropriate Http2 library context ID is stored
int libhttp2CtxId;

SceNpSessionSignalingInitParam myParam;
myParam.libhttp2CtxId = libhttp2CtxId;
myParam.poolSize = (256 * 1024);
myParam.cpuAffinityMask = 0;
myParam.threadPriority = SCE_KERNEL_PRIO_FIFO_DEFAULT;
myParam.threadStackSize = (32 * 1024);

int ret;

ret = sceNpSessionSignalingInitialize(&myParam);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

* This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.
* This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpSessionSignalingTerminate()`

# sceNpSessionSignalingTerminate

Terminates the library

## Definition

```
#include <np.h>
int sceNpSessionSignalingTerminate(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |

## Description

This function terminates the NpSessionSignaling library.

Before calling this function, stop/destroy existing contexts.

## Examples

```
int ret;

ret = sceNpSessionSignalingTerminate();
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

* This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.
* This function is a blocking function. Because it may perform blocking for long periods, call it from subthreads. The function must not be called in time-critical threads.

## See Also

`sceNpSessionSignalingInitialize()`, `sceNpSessionSignalingDestroyContext()`