# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-init-param.html

# Initialization/Termination

# SceNpUniversalDataSystemInitParam

Initialization parameters

## Definition

```
#include <np.h>
typedef struct SceNpUniversalDataSystemInitParam {
    size_t size;
    size_t poolSize;
} SceNpUniversalDataSystemInitParam;
```

## Members

|  |  |
| --- | --- |
| `size` | [In] Size of this structure |
| `poolSize` | [In] Size of the memory pool to be used by the NpUniversalDataSystem library (bytes) |

## Description

This structure stores the initialization parameters of the NpUniversalDataSystem library. This structure is used when the NpUniversalDataSystem library is initialized with `sceNpUniversalDataSystemInitialize()`.

For `size`, always specify `sizeof(SceNpUniversalDataSystemInitParam)`.

For `poolSize`, specify the size of the memory pool to be used by the NpUniversalDataSystem library in bytes. The required memory pool size depends on the sizes of events created by the application. The memory size used by the NpUniversalDataSystem library can be checked by calling `sceNpUniversalDataSystemGetMemoryStat()`. Test run your application a few times and check the memory size to finalize the value to specify for `poolSize`.

Note that if the specified memory pool size is not a multiple of 16 KiB, a memory pool of the specified size rounded up to the nearest multiple of 16 KiB will be allocated.

# sceNpUniversalDataSystemInitialize

Initialize the library

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemInitialize(
    const SceNpUniversalDataSystemInitParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | [In] Initialization parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_SIZE` | 0x80553112 | The size specified for the `size` member of the initialization parameter structure is invalid |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_ALREADY_INITIALIZED` | 0x80553118 | Already initialized |

## Description

This function initializes the NpUniversalDataSystem library. This function must be called first before any other NpUniversalDataSystem library functions are used.

For `param`, specify the initialization parameter structure to which the size of the memory pool to be used by the NpUniversalDataSystem library has been set.

## See Also

`sceNpUniversalDataSystemTerminate()`

# sceNpUniversalDataSystemTerminate

Terminate library

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemTerminate()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function terminates the NpUniversalDataSystem library.

`SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` will be returned when an NpUniversalDataSystem library function other than `sceNpUniversalDataSystemInitialize()` is called after the call of this function.

Operation cannot be guaranteed when this function is called during the execution of another NpUniversalDataSystem library function. Check that all NpUniversalDataSystem library function calls have completed before calling this function. Note that resources allocated by a function that manipulates event data will be released automatically when this function is called.