# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-mount-result.html

# Mounting/Unmounting

# SceSaveDataMount3

Parameters for mounting save data

## Definition

```
#include <save_data.h>
typedef uint64_t SceSaveDataBlocks;
typedef uint32_t SceSaveDataMountMode;

typedef struct SceSaveDataMount3 {
	SceUserServiceUserId userId;
	int :32;
	const SceSaveDataDirName *dirName;
	SceSaveDataBlocks blocks;
	SceSaveDataBlocks systemBlocks;
	SceSaveDataMountMode mountMode;
	int :32;
	SceSaveDataTransactionResourceId resource;
	uint8_t reserved[32];

} SceSaveDataMount3;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `dirName` | Save data directory name |
| `blocks` | Save data size (number of blocks, from `SCE_SAVE_DATA_BLOCKS_MIN3` (=48) to `SCE_SAVE_DATA_BLOCKS_MAX2` (=16384)) |
| `systemBlocks` | Size of the save data system area (specify `SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS`) |
| `mountMode` | Mount mode |
| `resource` | Unused |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for mounting a save data directory (including save data directories saved with the save data memory feature) with `sceSaveDataMount3()`.

For `userId`, specify the user ID obtained with the UserService library.

For `dirName`, specify the name of the save data directory to mount.

For `blocks`, specify the save data size in blocks. This value will only be referenced when newly creating save data. The minimum value that can be specified to `blocks` is `SCE_SAVE_DATA_BLOCKS_MIN3` (=48), and the maximum value that can be specified is `SCE_SAVE_DATA_BLOCKS_MAX2` (=16384).

Specify `SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS` for `systemBlocks` to create save data that holds a system area and that supports the rollback feature. The value set for `systemBlocks` will only be referenced when creating new save data and will be ignored when existing save data is mounted.

The size of save data to be created in the file system will be `(blocks + systemBlocks) * SCE_SAVE_DATA_BLOCK_SIZE2`.

For `mountMode`, a bitwise OR of the following values can be specified.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_MOUNT_MODE_RDONLY` | 1 | Read-only |
| `SCE_SAVE_DATA_MOUNT_MODE_RDWR` | 2 | Read/write (not used) |
| `SCE_SAVE_DATA_MOUNT_MODE_CREATE` | 4 | Create new (error if save data directory already exists) |
| `SCE_SAVE_DATA_MOUNT_MODE_COPY_ICON` | 16 | Copy save\_data.png in package as icon when newly creating save data |
| `SCE_SAVE_DATA_MOUNT_MODE_CREATE2` | 32 | Create new (mount save data directory if it already exists) |
| `SCE_SAVE_DATA_MOUNT_MODE_DEBUG_IGNORE_CREATE_MAX_COUNT_LIMIT` | 64 | Do not check the maximum number of save data when creating a new one |

Specify `SCE_SAVE_DATA_MOUNT_MODE_RDONLY` to `mountMode`, and add each mode with a logical disjunction as needed.

Specify one of the following combinations to `mountMode` when creating a new save data directory.

* `SCE_SAVE_DATA_MOUNT_MODE_CREATE` and `SCE_SAVE_DATA_MOUNT_MODE_RDONLY` specified in combination (the `SCE_SAVE_DATA_ERROR_EXISTS` error will be returned when a save data directory already exists)
* `SCE_SAVE_DATA_MOUNT_MODE_CREATE2` and `SCE_SAVE_DATA_MOUNT_MODE_RDONLY` specified in combination (save data will be mounted and an error will not be returned even when a save data directory already exists)
* If `SCE_SAVE_DATA_MOUNT_MODE_DEBUG_IGNORE_CREATE_MAX_COUNT_LIMIT` is additionally specified to one of the above combinations, save data can be created beyond the limit of `SCE_SAVE_DATA_CREATE_MAX_COUNT`. This can only be specified in Development Mode/Assist Mode. In Release Mode, this specification will be ignored.

Furthermore, upon newly creating a save data directory, /app0/sce\_sys/save\_data.png will be automatically copied as sce\_sys/icon0.png of the created save data by also specifying `SCE_SAVE_DATA_MOUNT_MODE_COPY_ICON` for `mountMode`.

Note:

`SCE_SAVE_DATA_MOUNT_MODE_RDWR` is reserved for future feature expansions. To access the save data directory in the read/write-enabled mode, call `sceSaveDataPrepare()` after mounting with `SCE_SAVE_DATA_MOUNT_MODE_RDONLY`.

**When mounting save data for the save data memory**

The save data memory is ultimately saved as a file with the filename defined by `SCE_SAVE_DATA_FILENAME_SAVE_DATA_MEMORY` in the save data directory with the directory name defined by `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_*`.

If the save data memory has not yet been set up, this function can be used to mount the save data directory and read its content. In such cases, `SCE_SAVE_DATA_MOUNT_MODE_RDONLY` must be set for `mountMode`. To access the save data memory in the read-write mode, use `sceSaveDataSetupSaveDataMemory2()`.

## Notes

When creating save data on a host PC using a file path configuration file, save data created will not support the rollback feature and a system area will not be allocated.

# SceSaveDataMountResult

Result of a save data mount

## Definition

```
#include <save_data.h>
typedef uint64_t SceSaveDataBlocks;
typedef uint32_t SceSaveDataMountStatus;
#define SCE_SAVE_DATA_MOUNT_STATUS_CREATED (0x00000001)

typedef struct SceSaveDataMountResult {
	SceSaveDataMountPoint mountPoint;
	SceSaveDataBlocks requiredBlocks;
	uint32_t unused;
	SceSaveDataMountStatus mountStatus;
	uint8_t reserved[28];
	int :32;
} SceSaveDataMountResult;
```

## Members

|  |  |
| --- | --- |
| `mountPoint` | Mount point name (NULL-terminated, UTF-8) |
| `requiredBlocks` | Unused |
| `unused` | Unused (specify 0) |
| `mountStatus` | Mount status |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for receiving the result of a save data mount. When the save data directory is successfully mounted, the mount point name will be stored in `mountPoint` of this structure (specified as an argument for the mount function).

`requredBlocks` is not used. If there is not enough free space in the file system, the system will display the insufficient size in an error dialog using the SaveDataDialog library.

If save data was newly created upon mounting the save data directory, `SCE_SAVE_DATA_MOUNT_STATUS_CREATED` will be stored in `mountStatus`. The application can evaluate whether an already existing save data or a newly created save data was mounted from this value.

## Notes

The character string, "/savedata0", "/savedata1", ..."/savedata15", will be stored in `mountPoint`.

## See Also

`sceSaveDataMount3()`

# SceSaveDataTransferringMount

Parameters for mounting save data for transferring

## Definition

```
#include <save_data.h>

typedef struct SceSaveDataTransferringMount {
	SceUserServiceUserId userId;
	const SceSaveDataTitleId *titleId;
	const SceSaveDataDirName *dirName;
	const SceSaveDataFingerprint *fingerprint;
	uint8_t reserved[32];
} SceSaveDataTransferringMount;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `titleId` | Title ID of the transfer source save data |
| `dirName` | Save data directory name |
| `fingerprint` | Fingerprint of the transfer source save data |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used with `sceSaveDataTransferringMount()` and `sceSaveDataTransferringMountPs4()` for mounting save data created by another application for transferring.

For `userId`, specify the user ID obtained with the UserService library.

# sceSaveDataMount3

Mount a save data directory

## Definition

```
#include <save_data.h>
int32_t sceSaveDataMount3(
	const SceSaveDataMount3 *mount,
	SceSaveDataMountResult *mountResult
)
```

## Arguments

|  |  |
| --- | --- |
| `mount` | Parameters for mounting save data |
| `mountResult` | Destination to store the result of mounting save data |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data directory is already mounted, save data in the save data memory is already set up, or save data is being converted |
| `SCE_SAVE_DATA_ERROR_EXISTS` | 0x809f0007 | Save data directory with the same name exists |
| `SCE_SAVE_DATA_ERROR_NOT_FOUND` | 0x809f0008 | Specified save data does not exist |
| `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` | 0x809f000a | Not enough free space in the file system to mount the save data |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_MOUNT_FULL` | 0x809f000c | Maximum mount value has been reached |
| `SCE_SAVE_DATA_ERROR_BROKEN` | 0x809f000f | Save data is corrupted or other reason (details below) |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_SAVE_DATA_ERROR_CREATE_MAX_LIMIT` | 0x809f001f | The maximum number of save data per user has been reached |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function mounts the specified save data directory and allocates a mount point.

When this function terminates normally, a mount point name from "/savedata0" to "/savedata15" will be stored for `mountResult->mountPoint`, and file access within the save data will be subsequently possible with this mount point name + "/" + the filename (or directory name) as the file path.

For `mount`, specify the save data directory name, mount mode, etc. For details, refer to the "Description" of `SceSaveDataMount3`.

When using this function to newly create a save data directory, default values (explained later in the document) will be set for the save data parameters according to the language settings of the system software, and the save data directory will be registered in the save data database.

If a save data directory cannot be created because of insufficient free space on the file system, `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` will be returned for the return value but 0 will be returned in `mountResult->requiredBlocks`.

When neither `SCE_SAVE_DATA_MOUNT_MODE_CREATE` nor `SCE_SAVE_DATA_MOUNT_MODE_CREATE2` is specified for the mount mode, the `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` error will not occur.

The `SCE_SAVE_DATA_ERROR_BROKEN` error occurs only during development; it does not occur in the product versions of applications. For details, refer to the "Development-Specific Mounting Errors" subsection of the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document.

If this function is called for the directory of save data that is being converted by `sceSaveDataConvert()`, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned.

When attempting to create a new save data directory, the `SCE_SAVE_DATA_ERROR_CREATE_MAX_LIMIT` error will be returned if `SCE_SAVE_DATA_CREATE_MAX_COUNT`-number of save data for the user specified by `userId` already exists.

Parameter default values

The default values set for each parameter of the param.sfo file are as follows. (The following values may change in the future; do not use processing that depends on these values.)

* Save data title: as follows according to the system software language setting

| **Language setting** | **Default save data title** |
| --- | --- |
| Japanese | "セーブデータ" |
| English (United States) | "Saved Data" |
| French (France) | "Données sauvegardées" |
| Spanish (Spain) | "Datos guardados" |
| German | "Gespeicherte Daten" |
| Italian | "Dati salvati" |
| Dutch | "Opgeslagen data" |
| Portuguese (Portugal) | "Dados guardados" |
| Russian | "Сохраненные данные" |
| Korean | "저장 데이터" |
| Chinese (traditional) | "保存資料" |
| Chinese (simplified) | "保存数据" |
| Finnish | "Tallennetut tiedot" |
| Swedish | "Sparade data" |
| Danish | "Gemte data" |
| Norwegian | "Lagrede data" |
| Polish | "Zapisane dane" |
| Portuguese (Brazil) | "Dados salvos" |
| English (United Kingdom) | "Saved Data" |
| Turkish | "Kayıtlı Veriler" |
| Spanish (Latin America) | "Datos guardados" |
| Arabic | "" |
| French (Canada) | "Données sauvegardées" |
| Czech | "Uložená data" |
| Hungarian | "Mentett adat" |
| Greek | "Αποθηκευμένα δεδομένα" |
| Romanian | "Date salvate" |
| Thai | "ข้อมูลที่บันทึกไว้" |
| Vietnamese | "Dữ liệu đã lưu" |
| Indonesian | "Data Tersimpan" |
| Ukrainian | "Збережені дані" |

* Save data subtitle: empty string ("")
* Save data detailed information: empty string ("")
* User parameter: 0

These parameters can be changed using `sceSaveDataSetParam()`.

## Examples

```
SceSaveDataDirName dirName;

strlcpy(dirName.data, "SYSTEM", sizeof(dirName.data));

SceSaveDataMount3 mount;
memset(&mount, 0x00, sizeof(mount));
mount.userId = userId;
mount.dirName = &dirName;
mount.blocks = SCE_SAVE_DATA_BLOCKS_MIN3;
mount.systemBlocks = SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS;
mount.mountMode = (SCE_SAVE_DATA_MOUNT_MODE_CREATE2 | SCE_SAVE_DATA_MOUNT_MODE_RDONLY);

SceSaveDataMountResult mountResult;
memset(&mountResult, 0x00, sizeof(mountResult));

if ( sceSaveDataMount3(&mount, &mountResult) < 0 ) {
	// Error handling
}
```

## See Also

`SceSaveDataMountPoint`

# sceSaveDataTransferringMount

Mount a save data directory for transferring

## Definition

```
#include <save_data.h>
int32_t sceSaveDataTransferringMount(
	const SceSaveDataTransferringMount *mount,
	SceSaveDataMountResult *mountResult
)
```

## Arguments

|  |  |
| --- | --- |
| `mount` | Parameters for mounting save data for transferring |
| `mountResult` | Destination to store the mount result |

## Return Values

Stores the mount point name in `mountResult->mountPoint` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data directory is already mounted, or save data in the save data memory is already set up |
| `SCE_SAVE_DATA_ERROR_FINGERPRINT_MISMATCH` | 0x809f0006 | Fingerprint does not match |
| `SCE_SAVE_DATA_ERROR_NOT_FOUND` | 0x809f0008 | Specified save data does not exist |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_MOUNT_FULL` | 0x809f000c | Maximum mount value has been reached |
| `SCE_SAVE_DATA_ERROR_BROKEN` | 0x809f000f | Save data is corrupted or other reason (details below) |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | User for specified user ID is not logged in |
| `SCE_SAVE_DATA_ERROR_PARAMSFO_TRANSFER_TITLE_ID_NOT_FOUND` | 0x809f0019 | Specified title ID of the transfer source is not in param.json |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function mounts the specified save data directory in read mode for transferring and allocates a mount point.

When this function terminates normally, a mount point name from "/savedata0" to "/savedata15" will be stored for `mountResult->mountPoint`, and file access within the save data will be subsequently possible with this mount point name + "/" + the filename (or directory name) as the file path.

The title ID specified in `mount->titleid` for the transfer source save data must be specified in advance as `titleIdForTransferring` in the param.json file of the application calling this function.

To read content of the save data memory and to transfer it, use this function to mount the save data directory with the name defined with `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_*`, and read the file with the name defined with `SCE_SAVE_DATA_FILENAME_SAVE_DATA_MEMORY`.

The `SCE_SAVE_DATA_ERROR_BROKEN` error occurs only during development; it does not occur in the product versions of applications. For details, refer to the "Development-Specific Mounting Errors" subsection of the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document.

## Examples

```
SceSaveDataTitleId titleId;
SceSaveDataDirName dirName;
SceSaveDataFingerprint fingerprint;

memset(&titleId, 0x00, sizeof(titleId));
strlcpy(titleId.data, 'NPXS00001', sizeof(titleId.data));
memset(&dirName, 0x00, sizeof(dirName));
strlcpy(dirName.data, "SYSTEM", sizeof(dirName.data));
memset(&fingerprint, 0x00, sizeof(fingerprint));
strlcpy(fingerprint.data, "dc1e3fde1c0913af519d107ea87610ba7b72039ac476b5521fc5cc5be32e7793", sizeof(fingerprint.data));

SceSaveDataTransferringMount mount;
memset(&mount, 0x00, sizeof(mount));
mount.userId = userId;
mount.titleId = &titleId;
mount.dirName = &dirName;
mount.fingerprint = &fingerprint;

SceSaveDataMountResult mountResult;
memset(&mountResult, 0x00, sizeof(mountResult));

if ( sceSaveDataTransferringMount(&mount, &mountResult) < 0 ) {
	// Error handling
}
```

## See Also

`SceSaveDataMountPoint`

# sceSaveDataTransferringMountPs4

Mount a PlayStation®4 save data directory for transferring

## Definition

```
#include <save_data.h>
int32_t sceSaveDataTransferringMountPs4(
	const SceSaveDataTransferringMount *mount,
	SceSaveDataMountResult *mountResult
)
```

## Arguments

|  |  |
| --- | --- |
| `mount` | Parameters for mounting save data for transferring |
| `mountResult` | Destination to store the mount result |

## Return Values

Stores the mount point name in `mountResult->mountPoint` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data directory is already mounted, or save data in the save data memory is already set up |
| `SCE_SAVE_DATA_ERROR_FINGERPRINT_MISMATCH` | 0x809f0006 | Fingerprint does not match |
| `SCE_SAVE_DATA_ERROR_NOT_FOUND` | 0x809f0008 | Specified save data does not exist |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_MOUNT_FULL` | 0x809f000c | Maximum mount value has been reached |
| `SCE_SAVE_DATA_ERROR_BROKEN` | 0x809f000f | Save data is corrupted or other reason (details below) |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | User for specified user ID is not logged in |
| `SCE_SAVE_DATA_ERROR_PARAMSFO_TRANSFER_TITLE_ID_NOT_FOUND` | 0x809f0019 | Specified title ID of the transfer source is not in param.json |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function mounts the specified save data directory saved by a PlayStation®4 application in read mode for transferring and allocates a mount point.

When this function terminates normally, a mount point name from "/savedata0" to "/savedata15" will be stored for `mountResult->mountPoint`, and file access within the save data will be subsequently possible with this mount point name + "/" + the filename (or directory name) as the file path.

The title ID specified for `mount->titleid` for the transfer-source save data must be specified in advance as `titleIdForTransferringPs4` in the param.json file of the application calling this function.

To read content of the save data memory and to transfer it, use this function to mount the save data directory with the name defined with `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_*`, and read the file with the name defined with `SCE_SAVE_DATA_FILENAME_SAVE_DATA_MEMORY`.

If the specified save data is corrupted, the error `SCE_SAVE_DATA_ERROR_BROKEN` will be returned.

## Examples

```
SceSaveDataTitleId titleId;
SceSaveDataDirName dirName;
SceSaveDataFingerprint fingerprint;

memset(&titleId, 0x00, sizeof(titleId));
strlcpy(titleId.data, 'NPXS00001', sizeof(titleId.data));
memset(&dirName, 0x00, sizeof(dirName));
strlcpy(dirName.data, "SYSTEM", sizeof(dirName.data));
memset(&fingerprint, 0x00, sizeof(fingerprint));
strlcpy(fingerprint.data, "dc1e3fde1c0913af519d107ea87610ba7b72039ac476b5521fc5cc5be32e7793", sizeof(fingerprint.data));

SceSaveDataTransferringMount mount;
memset(&mount, 0x00, sizeof(mount));
mount.userId = userId;
mount.titleId = &titleId;
mount.dirName = &dirName;
mount.fingerprint = &fingerprint;

SceSaveDataMountResult mountResult;
memset(&mountResult, 0x00, sizeof(mountResult));

if ( sceSaveDataTransferringMountPs4(&mount, &mountResult) < 0 ) {
	// Error handling
}
```

## See Also

`SceSaveDataMountPoint`

# sceSaveDataUmount2

Unmount a save data directory

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataUmountMode;
int32_t sceSaveDataUmount2(
	SceSaveDataUmountMode mode,
	const SceSaveDataMountPoint *mountPoint
)
```

## Arguments

|  |  |
| --- | --- |
| `mode` | Unmount mode |
| `mountPoint` | Mount point name |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | File is open |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` | 0x809f000d | Save data directory is not mounted for writing |
| `SCE_SAVE_DATA_ERROR_RESOURCE_BUSY` | 0x809f001b | An update that hasn't been committed still remains |
| `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` | 0x809f001c | The feature to cancel the update of save data is disabled |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function unmounts the save data directory. After the call of this function succeeds, the specified mount point will no longer be accessible.

For `mode`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_UMOUNT_MODE_DEFAULT` | 0 | Let the unmounting fail if the save data update has not been committed |
| `SCE_SAVE_DATA_UMOUNT_MODE_COMMIT` | 1 | Commit the save data update and unmount the save data directory |
| `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` | 1<<1 | Cancel the save data update and unmount the save data directory |

If `SCE_SAVE_DATA_UMOUNT_MODE_DEFAULT` is specified, an error indicating that the transaction resource is busy will be returned when an update that hasn't been committed still remains, and the unmount will fail.

`SCE_SAVE_DATA_UMOUNT_MODE_COMMIT` can be specified even when not updating save data. The update date for save data will be updated simultaneously with the unmounting when this function is called during a save data update.

If `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` is specified, uncommitted updates will be canceled and the save data directory will be unmounted. If this value is specified at a time other than while save data is being updated by `sceSaveDataPrepare()`, only the unmounting will be performed.

If `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` is not specified for `sceSaveDataPrepare()`, the `SCE_SAVE_DATA_ERROR_RESOURCE_INVALID` error will be returned.

If `SCE_SAVE_DATA_UMOUNT_MODE_COMMIT` and `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` are specified simultaneously, the `SCE_SAVE_DATA_ERROR_PARAMETER` error will be returned.

If this function is called with `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` specified when save data is created on the host PC, as an exception, its behavior will be the same as `SCE_SAVE_DATA_UMOUNT_MODE_COMMIT`. Refer to [SaveData Library Overview - Rollback Feature - Behavior When Save Data Is Created on a Host PC](../SaveData-Overview/behavior-when-save-data-is-created-on-a-host-pc.html) for details.

The `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` error will be returned when specifying `SCE_SAVE_DATA_UMOUNT_MODE_COMMIT` for the following mount points.

* A mount point mounted by `sceSaveDataTransferringMount()`
* A mount point mounted by `sceSaveDataTransferringMountPs4()`
* A mount point that mounts save data for the save data memory

## Examples

```
// Mounting with sceSaveDataMount3() is complete

// File access processing

if ( sceSaveDataUmount2( SCE_SAVE_DATA_UMOUNT_MODE_DEFAULT, &mountPoint) < 0 ) {
	// Error handling
}
```

## Notes

* The blocking time of this function is long, because it performs a write to console storage.
* Call this function after completing file input/output of save data. In particular, when using asynchronous IO, carry out scheduling with care so that IO operations complete while save data is mounted and before this function is called.