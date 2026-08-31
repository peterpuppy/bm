# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-commit-param.html

# Updating Save Data

# SceSaveDataPrepareParam

Parameters for starting a save data update

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataPrepareMode
typedef struct SceSaveDataPrepareParam {
	SceSaveDataTransactionResourceId resource;
	SceSaveDataPrepareMode prepareMode;
	uint8_t reserved[32];
} SceSaveDataPrepareParam;
```

## Members

|  |  |
| --- | --- |
| `resource` | Transaction resource |
| `prepareMode` | Mode |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is for starting a save data update. For `resource`, specify the transaction resource created in advance with `sceSaveDataCreateTransactionResource()`.

For `prepareMode`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_PREPARE_MODE_DEFAULT` | 0 | Start a save data update |
| `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` | 2 | Enable the feature to cancel the update of save data |
| `SCE_SAVE_DATA_PREPARE_MODE_DEBUG_IGNORE_CANCEL_ON_HOST` | 4 | When save data is created on the host PC, ignore the specification of `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` |

`SCE_SAVE_DATA_PREPARE_MODE_DEBUG_IGNORE_CANCEL_ON_HOST` can only be specified when `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` is specified.

## Notes

For information about the usage of `SCE_SAVE_DATA_PREPARE_MODE_DEBUG_IGNORE_CANCEL_ON_HOST`, refer to [SaveData Library Overview - Rollback Feature - Behavior When Save Data Is Created on a Host PC](../SaveData-Overview/behavior-when-save-data-is-created-on-a-host-pc.html).

## See Also

`sceSaveDataMount3()`, `sceSaveDataPrepare()`, `sceSaveDataCommit()`, `SceSaveDataMount3`

# SceSaveDataCommitParam

Parameters for committing a save data update

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataCommitMode;
typedef struct SceSaveDataCommitParam {
	SceSaveDataTransactionResourceId resource;
	SceSaveDataCommitMode commitMode;
	uint8_t reserved[32];
} SceSaveDataCommitParam;
```

## Members

|  |  |
| --- | --- |
| `resource` | Transaction resource |
| `commitMode` | Mode |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is for committing a save data update.

For `resource`, specify the transaction resource that was specified when starting the save data update.

For `commitMode`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_COMMIT_MODE_DEFAULT` | 0 | Only commit the save data update |

## See Also

`sceSaveDataMount3()`, `sceSaveDataCommit()`, `SceSaveDataMount3`

# sceSaveDataPrepare

Start a save data update

## Definition

```
#include <save_data.h>
int32_t sceSaveDataPrepare(
	const SceSaveDataMountPoint *mountPoint,
	const SceSaveDataPrepareParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name |
| `param` | Parameters for starting a save data update |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data update already started |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` | 0x809f000d | Save data directory is not mounted for writing |
| `SCE_SAVE_DATA_ERROR_RESOURCE_BUSY` | 0x809f001b | Transaction resource is in use |
| `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` | 0x809f001c | Transaction resource is invalid |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function starts a save data update

Calling this function enables reading and writing of the mount point.

If `sceSaveDataPrepare()` is executed for the following mount points, the `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` error will be returned.

* A mount point mounted with `sceSaveDataTransferringMount()`
* A mount point mounted with `sceSaveDataTransferringMountPs4()`
* A mount point that mounts save data for the save data memory

The `SCE_SAVE_DATA_ERROR_PARAMETER` error is returned in the following cases.

* `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` is specified for `param->prepareMode` for save data created on a host PC
* Even though `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` is not specified for `param->prepareMode`, `SCE_SAVE_DATA_PREPARE_MODE_DEBUG_IGNORE_CANCEL_ON_HOST` is specified

## Examples

```
// Omitted: Mount save data in the read-only mode with sceSaveDataMount3()

// Start update
SceSaveDataPrepareParam param;
memset(&param, 0x0, sizeof(param));
param.resource = resource; 
param.prepareMode = SCE_SAVE_DATA_PREPARE_MODE_DEFAULT;

if ( sceSaveDataPrepare(&mountPoint, &param) < 0 ) {
	// Error handling
}
```

## Notes

* When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).

## See Also

`sceSaveDataCommit()`

# sceSaveDataCommit

Commit a save data update

## Definition

```
#include <save_data.h>
int32_t sceSaveDataCommit(
	const SceSaveDataCommitParam *param
)
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters for committing a save data update |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | A file/directory that was deleted while being opened has not been closed |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` | 0x809f001c | Not the transaction resource specified upon starting save data update |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function commits a save data update. The update time/date of the save data will be updated when this function reaches normal termination.

For the details of the conditions under which `SCE_SAVE_DATA_ERROR_BUSY` is returned, refer to [SaveData Library Overview - Rollback Feature - Special Cases in Which Updates of Save Data May Fail](../SaveData-Overview/special-cases-in-which-updates-of-save-data-may-fail.html).

## Examples

```
// Omitted: Mount save data using sceSaveDataMount3()

// Omitted: Start save data update using sceSaveDataPrepare()

// Omitted: Update the file

// Commit the update
SceSaveDataCommitParam param;
memset(&param, 0x0, sizeof(param));
param.resource = resource; // Transaction resource specified when starting update

if ( sceSaveDataCommit(&param) < 0 ) {
	// Error handling
}
```

## Notes

* The blocking time of this function is long because it performs a write to internal storage.
* When this function is called during a write to save data, the start of this function's processing will be blocked and forced to wait until the write completes.
* When attempting to write to save data during the processing of this function, the write will be blocked and forced to wait until processing returns from this function.

# sceSaveDataCancel

Cancel a save data update

## Definition

```
#include <save_data.h>
int32_t sceSaveDataCancel(
	SceSaveDataTransactionResourceId resource
)
```

## Arguments

|  |  |
| --- | --- |
| `resource` | Transaction resource |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | A file/directory that was opened has not been closed |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` | 0x809f001c | Not the transaction resource specified upon starting save data update  or  the feature to cancel the update of save data is disabled |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function cancels the update of save data. When this function terminates normally, the save data content will be returned to the state immediately before the update of save data was started and the update will terminate.

`SCE_SAVE_DATA_ERROR_BUSY` will be returned if there are files and directories that are opened under the save data's mount point.

If `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` is not specified for `sceSaveDataPrepare()`, `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` will be returned.

If this function is called when save data is created on the host PC, the save data update will be committed as an exception. Refer to [SaveData Library Overview - Rollback Feature - Behavior When Save Data Is Created on a Host PC](../SaveData-Overview/behavior-when-save-data-is-created-on-a-host-pc.html) for details.

## Examples

```
// Omitted: Mount save data using sceSaveDataMount3()

// Omitted: Start save data update using sceSaveDataPrepare()

// Cancel the update
if ( sceSaveDataCancel(resource) < 0 ) { // Transaction resource specified when starting update

	// Error handling
}
```