# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-init-params3.html

# Initialization/Termination

# SceSaveDataInitParams3

Initialization parameters

## Definition

```
#include <save_data.h>
typedef struct _SceSaveDataInitParams3 SceSaveDataInitParams3;
```

## Description

This datatype is reserved for setting the parameters when initializing the SaveData library with `sceSaveDataInitialize3()`.

# sceSaveDataInitialize3

Initialize the SaveData library

## Definition

```
#include <save_data.h>
int32_t sceSaveDataInitialize3(
	const SceSaveDataInitParams3 *initParam
)
```

## Arguments

|  |  |
| --- | --- |
| `initParam` | Initialization parameters (specify NULL) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |

## Description

This function initializes the SaveData library.

For `initParam`, specify NULL.

SaveData library functions can be used after this function terminates normally.

## Examples

```
if ( sceSaveDataInitialize3() < SCE_OK ) {
	// Error handling
}
```

## See Also

`sceSaveDataTerminate()`

# sceSaveDataTerminate

Terminate the SaveData library

## Definition

```
#include <save_data.h>
int32_t sceSaveDataTerminate()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data is in use (details below) |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |

## Description

This function terminates the SaveData library.

If the save data is in use, or more specifically in the following cases, the `SCE_SAVE_DATA_ERROR_BUSY` error is returned:

* The save data directory is mounted
* The save data memory is being saved
* Save data is being converted

## Examples

```
if (sceSaveDataTerminate() < 0 ) {
	// Error handling
}
```

## See Also

`sceSaveDataInitialize3()`