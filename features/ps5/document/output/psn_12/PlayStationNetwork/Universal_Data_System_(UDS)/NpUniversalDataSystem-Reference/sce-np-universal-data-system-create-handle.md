# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-create-handle.html

# Handles

# SceNpUniversalDataSystemHandle

Handle

## Definition

```
#include <np.h>
#define SCE_NP_UNIVERSAL_DATA_SYSTEM_INVALID_HANDLE (-1)
typedef int32_t SceNpUniversalDataSystemHandle;
```

## Description

This is the handle datatype.

A handle is required for function calls and for interrupting their processing. The handle created in advance with `sceNpUniversalDataSystemCreateHandle()` must be passed as an argument for some NpUniversalDataSystem library functions.

## See Also

`sceNpUniversalDataSystemDestroyHandle()`, `sceNpUniversalDataSystemAbortHandle()`

# sceNpUniversalDataSystemCreateHandle

Create a handle

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemCreateHandle(
    SceNpUniversalDataSystemHandle *handle
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | [Out] Destination to store the created handle |

## Return Values

Stores the created handle in `*handle` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_HANDLE_EXCEEDS_MAX` | 0x80553107 | Exceeded the maximum number of handles (8) |

## Description

This function creates a handle to be used when calling an NpUniversalDataSystem library function.

A handle can be reused. However, a handle must be destroyed if its processing has been aborted.

## Examples

```
SceNpUniversalDataSystemHandle handle = SCE_NP_UNIVERSAL_DATA_SYSTEM_INVALID_HANDLE;
int ret;

ret = sceNpUniversalDataSystemCreateHandle(&handle);
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpUniversalDataSystemDestroyHandle()`

# sceNpUniversalDataSystemDestroyHandle

Destroy a handle

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemDestroyHandle(
    SceNpUniversalDataSystemHandle handle
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | [In] Handle to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_HANDLE` | 0x80553106 | Invalid handle |

## Description

This function destroys the handle specified with `handle` and frees the internal resources. A handle must be destroyed if its processing has been aborted.

## See Also

`sceNpUniversalDataSystemCreateHandle()`

# sceNpUniversalDataSystemAbortHandle

Abort a handle

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemAbortHandle(
    SceNpUniversalDataSystemHandle handle
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | [In] Handle to be aborted |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_HANDLE` | 0x80553106 | Invalid handle |

## Description

This function aborts the processing of an NpUniversalDataSystem library function. For `handle`, specify the handle specified upon calling the function whose processing is to be aborted. The aborted function will return an error.

Destroy aborted handles without re-using them.

## See Also

`sceNpUniversalDataSystemCreateHandle()`