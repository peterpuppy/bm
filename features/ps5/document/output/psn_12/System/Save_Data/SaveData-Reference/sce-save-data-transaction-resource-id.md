# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-transaction-resource-id.html

# Transaction Resources

# SceSaveDataTransactionResourceId

Transaction resource ID

## Definition

```
#include <save_data.h>
typedef int32_t SceSaveDataTransactionResourceId;
#define SCE_SAVE_DATA_TRANSACTION_RESOURCE_ID_INVALID (~0U);
```

## Description

This datatype represents the handle of a transaction resource.

## See Also

`sceSaveDataCreateTransactionResource()`, `sceSaveDataDeleteTransactionResource()`

# sceSaveDataCreateTransactionResource

Create a transaction resource

## Definition

```
#include <save_data.h>
int32_t sceSaveDataCreateTransactionResource(
	uint32_t size
)
```

## Arguments

|  |  |
| --- | --- |
| `size` | Size of the transaction resource to create (specify 0) |

## Return Values

Returns the handle of the transaction resource (>0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

It does not return 0.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_RESOURCE_FULL` | 0x809f001a | Reached the maximum number of transaction resources that can be created |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function creates a transaction resource, which is required for mounting a save data directory in the read-write mode.

If a value other than 0 is specified for `size`, it will be ignored and a transaction resource with a size of 0 will always be created.

The `SCE_SAVE_DATA_ERROR_RESOURCE_FULL` error will occur when attempting to create a transaction resource that exceeds the maximum number for transaction resources as defined by `SCE_SAVE_DATA_TRANSACTION_RESOURCE_MAX_COUNT`.

## Examples

```
SceSaveDataTransactionResourceId resource = SCE_SAVE_DATA_TRANSACTION_RESOURCE_ID_INVALID;
if ( resource = sceSaveDataCreateTransactionResource(0) < 0 ) {
	// Error handling
}
```

## Notes

The maximum number of transaction resources that can be created is the same as the maximum number of save data that can be mounted at the same time: `SCE_SAVE_DATA_MOUNT_MAX_COUNT` (=16).

The transaction resource created with this function will be deleted automatically when `sceSaveDataTerminate()` is called. Call `sceSaveDataDeleteTransactionResource()` to delete it explicitly.

## See Also

`SceSaveDataMount3`, `sceSaveDataMount3()`, `sceSaveDataCommit()`

# sceSaveDataDeleteTransactionResource

Delete a transaction resource

## Definition

```
#include <save_data.h>
int32_t sceSaveDataDeleteTransactionResource(
	SceSaveDataTransactionResourceId resource
)
```

## Arguments

|  |  |
| --- | --- |
| `resource` | Transaction resource to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_RESOURCE_BUSY` | 0x809f001b | Transaction resource is in use |
| `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` | 0x809f001c | Transaction resource is invalid |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function deletes the transaction resource created with `sceSaveDataCreateTransactionResource()`. A busy error will be returned when an attempt is made to delete the transaction resource if it is still being used.

For `resource`, specify the handle of the transaction resource to delete. An invalid resource error will be returned if a resource that doesn't exist such as an already-deleted handle is specified.

## Examples

```
// Unmount the corresponding save data
if ( sceSaveDataUmount2( 0, &mountResult.mountPoint ) < 0 ) {
	// Error handling
	return;
}

if ( sceSaveDataDeleteTransactionResource( resource ) < 0 ) {
	// Error handling
}
```

## Notes

Even if a transaction resource isn't deleted explicitly using this function, it will be deleted automatically when `sceSaveDataTerminate()` is called.

## See Also

`SceSaveDataMount3`, `sceSaveDataMount3()`