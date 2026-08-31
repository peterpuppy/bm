# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/sce-np-trophy-2handle.html

# Handles

# SceNpTrophy2Handle

Trophy handle

## Definition

```
#include <np.h>
#define SCE_NP_TROPHY2_INVALID_HANDLE (-1)
typedef int32_t SceNpTrophy2Handle;
```

## Description

This is the trophy handle datatype.

A trophy handle is required for making and interrupting function calls. Most of the NpTrophy2 library functions require calling `sceNpTrophy2CreateHandle()` in advance to create a handle then passing it as an argument of the functions.

The `SCE_NP_TROPHY2_ERROR_BUSY` error may occur when multiple threads use the same handle at the same time. When calling NpTrophy2 library functions from multiple threads at the same time, use a different handle per thread.

## See Also

`sceNpTrophy2DestroyHandle()`, `sceNpTrophy2AbortHandle()`

# sceNpTrophy2CreateHandle

Create a handle

## Definition

```
#include <np.h>
int sceNpTrophy2CreateHandle(
    SceNpTrophy2Handle *handle
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | [Out] Destination to store the created handle |

## Return Values

Stores the created handle in `*handle` and returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_HANDLE_EXCEEDS_MAX` | 0x8055391C | Exceeded the maximum number of handles (4) |

## Description

This function creates a handle to be used when calling an NpTrophy2 library function.

A handle can be reused. However, a handle must be destroyed if its processing has been aborted.

## Examples

```
SceNpTrophy2Handle handle = SCE_NP_TROPHY2_INVALID_HANDLE;
int ret;

ret = sceNpTrophy2CreateHandle(&handle);
if ( ret < 0 ) {
    // Error handling
}
```

## See Also

`sceNpTrophy2DestroyHandle()`

# sceNpTrophy2DestroyHandle

Destroy a handle

## Definition

```
#include <np.h>
int sceNpTrophy2DestroyHandle(
    SceNpTrophy2Handle handle
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | [In] Handle to destroy |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_HANDLE` | 0x80553908 | Invalid handle |

## Description

This function destroys the handle specified with `handle` and frees the internal resources. A handle must be destroyed if its processing has been aborted.

## See Also

`sceNpTrophy2CreateHandle()`

# sceNpTrophy2AbortHandle

Abort a handle

## Definition

```
#include <np.h>
int sceNpTrophy2AbortHandle(
    SceNpTrophy2Handle handle
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | [In] Handle to be aborted |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for errors. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_INVALID_HANDLE` | 0x80553908 | Invalid handle |

## Description

This function aborts the processing of an NpTrophy2 library function. For `handle`, specify the handle whose processing is to be aborted upon calling the function. The aborted function will return an error.

Destroy aborted handles without re-using them.

## See Also

`sceNpTrophy2CreateHandle()`, `sceNpTrophy2DestroyHandle()`