# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-dir-name-search-cond.html

# Save Data Search

# SceSaveDataDirNameSearchCond

Parameters for setting save data directory search conditions

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataSortKey;
typedef uint32_t SceSaveDataSortOrder;

typedef struct SceSaveDataDirNameSearchCond {
	SceUserServiceUserId userId;
	int :32;
	const SceSaveDataTitleId *titleId;
	const SceSaveDataDirName *dirName;
	SceSaveDataSortKey key;
	SceSaveDataSortOrder order;
	uint8_t reserved[32];
} SceSaveDataDirNameSearchCond;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `titleId` | Save data title ID, or NULL |
| `dirName` | Save data directory name, or NULL |
| `key` | Sort key |
| `order` | Sort order |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for specifying search conditions when searching for save data directories with `sceSaveDataDirNameSearch()`, `sceSaveDataDirNameSearch2()`, or `sceSaveDataDirNameSearchPs4()`.

To search for save data created by the caller application, specify NULL for `titleId`.

Also specify NULL for `titleId` to search for save data shared by another application (save data of an application with the same title ID specified for the `titleIdForSharing` parameter in param.json).

When NULL or an empty string is specified for `dirName`, all save data directory names below the save data title ID directory will be applicable for the searching. It is also possible with `dirName` to specify "%" as a wildcard for matching an arbitrary character string of 0 characters or more and "\_" as a wildcard for matching a single arbitrary character.

For `key`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_SORT_KEY_DIRNAME` | 0 | Directory name |
| `SCE_SAVE_DATA_SORT_KEY_USER_PARAM` | 1 | User parameter |
| `SCE_SAVE_DATA_SORT_KEY_BLOCKS` | 2 | Number of blocks |
| `SCE_SAVE_DATA_SORT_KEY_MTIME` | 3 | Date/time of last update |
| `SCE_SAVE_DATA_SORT_KEY_FREE_BLOCKS` | 5 | Number of free blocks |

For `order`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_SORT_ORDER_ASCENT` | 0 | Ascending order |
| `SCE_SAVE_DATA_SORT_ORDER_DESCENT` | 1 | Descending order |

# SceSaveDataDirNameSearchResult

Save data directory search results

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataDirNameSearchResult {
	uint32_t hitNum;
	int :32;
	SceSaveDataDirName *dirNames;
	uint32_t dirNamesNum;
	uint32_t setNum;
	SceSaveDataParam *params;
	SceSaveDataSearchInfo *infos;
	uint8_t reserved[12];
	int :32;
} SceSaveDataDirNameSearchResult;
```

## Members

|  |  |
| --- | --- |
| `hitNum` | Total number of directories included in the search results |
| `dirNames` | Array to store each directory name of save data directories included in the search results |
| `dirNamesNum` | Number of `dirNames` elements |
| `setNum` | Number of data stored in `dirNames` |
| `params` | Array to store the save data parameter information of each save data in the search results (or NULL) |
| `infos` | Array to store information of each save data in the search results (or NULL) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for obtaining the results when searching for save data directories with `sceSaveDataDirNameSearch()`, `sceSaveDataDirNameSearch2()`, or `sceSaveDataDirNameSearchPs4()`.

Prepare an array of the `SceSaveDataDirName` datatype, specify the start address for `dirNames`, and specify the number of elements for `dirNamesNum`.

The number of save data directories included in the search results will be stored in `hitNum`, and of these, directory name data up to `dirNamesNum` will be stored in `dirNames` and the number of actually stored data will be stored in `setNum`. In addition, if `params` and `infos` are not NULL, `setNum` number of data will be stored. For `dirNames`, `params`, and `infos`, specify an array that is sufficiently large considering application specifications.

# SceSaveDataSearchInfo

Location to store additional information of search results

## Definition

```
#include <save_data.h>
typedef uint64_t SceSaveDataBlocks;
typedef struct SceSaveDataSearchInfo {
	SceSaveDataBlocks blocks;
	SceSaveDataBlocks freeBlocks;
	uint8_t reserved[32];
} SceSaveDataSearchInfo;
```

## Members

|  |  |
| --- | --- |
| `blocks` | Total size of save data (number of blocks) |
| `freeBlocks` | Free space of save data (number of blocks) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for obtaining additional information of save data when searching for save data with `sceSaveDataDirNameSearch()`, `sceSaveDataDirNameSearch2()`, or `sceSaveDataDirNameSearchPs4()`. By setting a pointer to this structure for the `infos` member of an `SceSaveDataDirNameSearchResult` structure, it will be possible to obtain the total size of save data in the search results, etc.

## Notes

* The same value as `blocks` will be stored in `freeBlocks` for save data saved to the save data root directory specified with the file path configuration file during development. Note that the save data free space will therefore not be indicated by `freeBlocks`.
* The save data free space when mounted in the read/write-enabled mode is the free space at the time of the previous unmount (or the total size allocated upon creation). Note that if the application or system later consumes free space due to writes, it will not be reflected.

# sceSaveDataDirNameSearch

Search for save data directories

## Definition

```
#include <save_data.h>
int32_t sceSaveDataDirNameSearch(
	const SceSaveDataDirNameSearchCond *cond,
	SceSaveDataDirNameSearchResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Search conditions |
| `result` | Destination to store search results |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function searches for save data directories and returns a list of save data directories that satisfy the specified conditions.

Searching is possible whether or not mounting has completed.

If an update to the save data directory was previously interrupted, the save data may be deleted by the system's automatic deletion process when it tries to mount the data, even if the save data is included in the list returned by this function. Note that the above problem can be avoided by using `sceSaveDataDirNameSearch2()`.

## Examples

```
// Obtain all save data directory names under the save data title ID

SceSaveDataDirNameSearchCond cond;
memset(&cond, 0x00, sizeof(SceSaveDataDirNameSearchCond));
cond.userId = userId;
cond.dirName = NULL;
cond.key = SCE_SAVE_DATA_SORT_KEY_DIRNAME;
cond.order = SCE_SAVE_DATA_SORT_ORDER_ASCENT;

SceSaveDataDirNameSearchResult result;
memset(&result, 0x00, sizeof(result));

result.dirNames = new SceSaveDataDirName[SCE_SAVE_DATA_DIRNAME_MAX_COUNT];
// SCE_SAVE_DATA_DIRNAME_MAX_COUNT can be the maximum number of save data directories the application will create
if ( result.dirNames == NULL ) {
	// Error handling
}
result.dirNamesNum = SCE_SAVE_DATA_DIRNAME_MAX_COUNT;

if ( sceSaveDataDirNameSearch(&cond, &result) < 0 ) {
	// Error handling
	delete [] result.dirNames;
	result.dirNames = NULL;
}
```

## Notes

* This function performs blocking until a search completes. The blocking time will become longer in proportion to the number of save data.
* When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).
* This function cannot search for save data created with the save data memory feature. (For example, even if "sce\_sdmemory" exists and search conditions are specified so that there should be hits for that directory, they will not be included in the search results.)

# sceSaveDataDirNameSearch2

Search after restoring save data directories

## Definition

```
#include <save_data.h>
int32_t sceSaveDataDirNameSearch2(
	const SceSaveDataDirNameSearchCond *cond,
	SceSaveDataDirNameSearchResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Search conditions |
| `result` | Destination to store search results |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data is being converted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function searches for save data directories and returns a list of save data directory names that satisfy the specified conditions.

Searching is possible whether or not mounting has completed.

Unlike `sceSaveDataDirNameSearch()`, this function searches for save data directories in a state where any corrupted save data that satisfies the specified conditions has been deleted. For this reason, there will be no disagreement between the output of this function and the actual result when save data is mounted.

If this function is called while save data is being converted by `sceSaveDataConvert()`, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned, regardless of whether the conversion target is included in the search results or not.

## Examples

```
// Obtain all save data directory names under the save data title ID

SceSaveDataDirNameSearchCond cond;
memset(&cond, 0x00, sizeof(SceSaveDataDirNameSearchCond));
cond.userId = userId;
cond.dirName = NULL;
cond.key = SCE_SAVE_DATA_SORT_KEY_DIRNAME;
cond.order = SCE_SAVE_DATA_SORT_ORDER_ASCENT;

SceSaveDataDirNameSearchResult result;
memset(&result, 0x00, sizeof(result));

result.dirNames = new SceSaveDataDirName[SCE_SAVE_DATA_DIRNAME_MAX_COUNT];
// SCE_SAVE_DATA_DIRNAME_MAX_COUNT can be the maximum number of save data directories the application will create
if ( result.dirNames == NULL ) {
	// Error handling
}
result.dirNamesNum = SCE_SAVE_DATA_DIRNAME_MAX_COUNT;

if ( sceSaveDataDirNameSearch2(&cond, &result) < 0 ) {
	// Error handling
	delete [] result.dirNames;
	result.dirNames = NULL;
}
```

## Notes

* This function performs blocking until a search completes. The blocking time will become longer in proportion to the number of save data.
* When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).
* This function cannot search for save data created with the save data memory feature. (For example, even if "sce\_sdmemory" exists and search conditions are specified so that there should be hits for that directory, they will not be included in the search results.)

# sceSaveDataDirNameSearchPs4

Search for PlayStation®4 save data directories

## Definition

```
#include <save_data.h>
int32_t sceSaveDataDirNameSearchPs4(
	const SceSaveDataDirNameSearchCond *cond,
	SceSaveDataDirNameSearchResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `cond` | Search conditions |
| `result` | Destination to store search results |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function searches for save data directories saved by PlayStation®4 applications and returns a list of save data directory names that satisfy the specified conditions.

Searching is possible whether or not mounting has completed.

## Examples

```
// Obtain all save data directory names under the save data title ID directory

SceSaveDataDirNameSearchCond cond;
memset(&cond, 0x00, sizeof(SceSaveDataDirNameSearchCond));
cond.userId = userId;
cond.dirName = NULL;
cond.key = SCE_SAVE_DATA_SORT_KEY_DIRNAME;
cond.order = SCE_SAVE_DATA_SORT_ORDER_ASCENT;

SceSaveDataDirNameSearchResult result;
memset(&result, 0x00, sizeof(result));

result.dirNames = new SceSaveDataDirName[SCE_SAVE_DATA_DIRNAME_MAX_COUNT];
// SCE_SAVE_DATA_DIRNAME_MAX_COUNT can be the maximum number of save data directories the application will create
if ( result.dirNames == NULL ) {
	// Error handling
}
result.dirNamesNum = SCE_SAVE_DATA_DIRNAME_MAX_COUNT;

if ( sceSaveDataDirNameSearchPs4(&cond, &result) < 0 ) {
	// Error handling
	delete [] result.dirNames;
	result.dirNames = NULL;
}
```

## Notes

* This function performs blocking until a search completes. The blocking time will become longer in proportion to the number of save data.
* When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).
* This function can also search for save data created with the save data memory feature.