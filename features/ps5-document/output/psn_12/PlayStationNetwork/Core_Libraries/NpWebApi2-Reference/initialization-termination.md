# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/initialization-termination.html

# Initialization/Termination

# sceNpWebApi2Initialize

Initialize NpWebApi2 library

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2Initialize(
	int libHttpCtxId,
	size_t poolSize
);
```

## Arguments

|  |  |
| --- | --- |
| `libHttpCtxId` | Http2 library context ID |
| `poolSize` | Memory pool size for the NpWebApi2 library |

## Return Values

Returns the library context ID of the NpWebApi2 library (positive value) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function initializes the NpWebApi2 library. In order to use this function, the Http2 library must be initialized and the Http2 library context ID must be obtained in advance.

For `poolSize`, specify the size of the memory pool that the NpWebApi2 library will generate. This size must be a multiple of 16 KiB. If a value that is not a multiple of 16 KiB is specified, the library will automatically round the value up to a multiple of 16 KiB.

## Examples

```
#define NP_WEBAPI2_POOL_SIZE ( 64 * 1024 )
int libHttpCtxId; // Http2 library context ID

int32_t ret = 0;
int32_t libCtxId = 0;

ret = sceNpWebApi2Initialize(libHttpCtxId, NP_WEBAPI2_POOL_SIZE);
if(ret < 0){
	/* Error handling */
}
libCtxId = ret;
```

## See Also

`sceNpWebApi2Terminate()`

# sceNpWebApi2Terminate

Terminate NpWebApi2 library

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2Terminate(
	int32_t libCtxId
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function terminates the NpWebApi2 library.

If the library context is being used for sending/receiving data, `SCE_NP_WEBAPI2_ERROR_LIB_CONTEXT_BUSY` will be returned. Execute this function after all processing completes.

## Examples

```
int32_t ret = 0;
int32_t libCtxId; // Library context ID

ret = sceNpWebApi2Terminate(libCtxId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2Initialize()`