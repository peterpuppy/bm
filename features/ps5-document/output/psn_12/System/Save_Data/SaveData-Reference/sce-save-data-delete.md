# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-delete.html

# Deleting Save Data

# SceSaveDataDelete

Parameters for deleting a save data directory

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataDelete {
	SceUserServiceUserId userId;
	int :32;
	const SceSaveDataTitleId *titleId;
	const SceSaveDataDirName *dirName;
	uint32_t unused;
	uint8_t reserved[32];
	int :32;
} SceSaveDataDelete;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `titleId` | Save data title ID (specify NULL) |
| `dirName` | Save data directory name (NULL-terminated, UTF-8) |
| `unused` | Unused (specify 0) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for deleting a save data directory with `sceSaveDataDelete()`.

Specify NULL for `titleId`.

For `dirName`, specify the name of the save data directory to delete.

# sceSaveDataDelete

Delete a save data directory

## Definition

```
#include <save_data.h>
int32_t sceSaveDataDelete(
	const SceSaveDataDelete *del
)
```

## Arguments

|  |  |
| --- | --- |
| `del` | Parameters for deleting a save data directory |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data directory is mounted, or save data is being converted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function deletes the specified save data directory.

It is used for deleting save data created by the caller application or save data shared by another application (save data with the title ID specified with the `titleIdForSharing` parameter in the application's param.json file).

This function performs blocking until deletion completes.

If this function is called for the directory of save data that is being converted by `sceSaveDataConvert()`, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned.

## Notes

When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).

## Examples

```
// Unmounted state

SceSaveDataDirName dirName;

strlcpy(dirName.data, "SYSTEM", sizeof(dirName.data));

SceSaveDataDelete del;
memset(&del, 0x00, sizeof(del));
del.userId = userId;
del.dirName = &dirName;

if ( sceSaveDataDelete(&del) ) {
	// Error handling
}
```