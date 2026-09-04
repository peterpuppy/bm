# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-get-mount-info.html

# Save Data Information

# SceSaveDataIcon

Parameters for accessing an icon

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataIcon {
	void *buf;
	size_t bufSize;
	size_t dataSize;
	uint8_t reserved[32];
} SceSaveDataIcon;
```

## Members

|  |  |
| --- | --- |
| `buf` | Icon data buffer |
| `bufSize` | Icon data buffer size |
| `dataSize` | Icon data size |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for saving/loading a save data icon image.

When saving an icon image, specify the buffer storing the save-target icon data to `buf`, and specify the size of this icon data to `dataSize`. A parameter error will occur for any of the following cases.

* `buf` is NULL
* The content of `buf` is not a valid-format icon image file
* `bufSize` is 0
* `dataSize` is 0
* `dataSize` > `SCE_SAVE_DATA_ICON_FILE_MAXSIZE2`
* `bufSize` < `dataSize`
* `reserved` is not filled with 0's

When loading an icon image, specify a buffer for receiving the icon data for `buf`, and specify the size of this buffer for `bufSize`. When loading succeeds, the size of the icon data will be stored in `dataSize`. A parameter error will occur for any of the following cases.

* `buf` is NULL
* `bufSize` is 0
* `reserved` is not filled with 0's

## See Also

`sceSaveDataSaveIcon()`, `sceSaveDataLoadIcon()`

# SceSaveDataMountInfo

Mount information

## Definition

```
#include <save_data.h>
typedef uint64_t SceSaveDataBlocks;

typedef struct SceSaveDataMountInfo {
	SceSaveDataBlocks blocks;
	SceSaveDataBlocks freeBlocks;
	uint8_t reserved[32];
} SceSaveDataMountInfo;
```

## Members

|  |  |
| --- | --- |
| `blocks` | Total size of save data (number of blocks) |
| `freeBlocks` | Free space of save data (number of blocks) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used when obtaining the mount information of a save data directory with `sceSaveDataGetMountInfo()`.

In `blocks`, the maximum size specified when newly creating save data will be stored. In `freeBlocks`, the value of `blocks` after subtracting the currently used volume will be stored.

## Notes

The same value as `blocks` will be stored in `freeBlocks` for save data saved to the save data root directory specified with the file path configuration file during development. Note that the save data free space will therefore not be indicated by `freeBlocks`.

# SceSaveDataParam

Save data parameters

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataParam {
	char title[SCE_SAVE_DATA_TITLE_MAXSIZE];
	char subTitle[SCE_SAVE_DATA_SUBTITLE_MAXSIZE];
	char detail[SCE_SAVE_DATA_DETAIL_MAXSIZE];
	uint32_t userParam;
	int :32;
	time_t mtime;
	uint8_t reserved[32];
} SceSaveDataParam;
```

## Members

|  |  |
| --- | --- |
| `title` | Save data title name (NULL-terminated, UTF-8, cannot include newline characters) |
| `subTitle` | Save data subtitle name (NULL-terminated, UTF-8, cannot include newline characters) |
| `detail` | Save data detailed information (NULL-terminated, UTF-8, newline characters can be used, usable newline characters are 0x0a or 0x0d, no restriction regarding number of lines) |
| `userParam` | User parameter |
| `mtime` | Date/time of last update |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for setting/obtaining save data parameters, such as the title name and detailed information.

For details about how the values set to `title`, `subTitle`, and `detail` will be displayed in the save data dialog, refer to the [SaveDataDialog Library Overview](../SaveDataDialog-Overview/__document_toc.html) document.

An arbitrary value can be set for `userParam`. For example, it can be used to specify the sort key when searching for save data.

`mtime` is a parameter limited to read-only use, and it will be automatically updated by the system when save data mounted in the read-write mode is updated.

## See Also

`sceSaveDataSetParam()`, `sceSaveDataGetParam()`, `SceSaveDataMemorySet2`, `SceSaveDataMemoryGet2`, `SceSaveDataMemorySetup2`, `SceSaveDataDirNameSearchResult`

# SceSaveDataParamType

Parameter type

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataParamType;
```

## Description

This datatype is used for indicating which parameter(s) to set/obtain when setting/obtaining save data parameter(s) with `sceSaveDataSetParam()` and `sceSaveDataGetParam()`. One of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_PARAM_TYPE_ALL` | 0 | Update/obtain all parameters (`SCE_SAVE_DATA_PARAM_TYPE_MTIME` will not be updated when these parameters are updated) |
| `SCE_SAVE_DATA_PARAM_TYPE_TITLE` | 1 | Update/obtain save data title only |
| `SCE_SAVE_DATA_PARAM_TYPE_SUB_TITLE` | 2 | Update/obtain save data subtitle only |
| `SCE_SAVE_DATA_PARAM_TYPE_DETAIL` | 3 | Update/obtain save data detailed information only |
| `SCE_SAVE_DATA_PARAM_TYPE_USER_PARAM` | 4 | Update/obtain user parameter only |
| `SCE_SAVE_DATA_PARAM_TYPE_MTIME` | 5 | Only obtain the update date and time (no update) |

# sceSaveDataGetMountInfo

Get mount information

## Definition

```
#include <save_data.h>
int32_t sceSaveDataGetMountInfo(
	const SceSaveDataMountPoint *mountPoint,
	SceSaveDataMountInfo *info
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name |
| `info` | Destination to store the obtained mount information |

## Return Values

Stores the mount information in `info` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function obtains the maximum size and free space of save data. Call it after mounting the save data.

## Examples

```
// Mounting with sceSaveDataMount3() is complete

SceSaveDataMountInfo mountInfo;
memset(&mountInfo, 0x00, sizeof(mountInfo));
if ( sceSaveDataGetMountInfo(&mountPoint, &mountInfo) < 0 ) {
	// Error handling
}
```

# sceSaveDataGetParam

Get save data parameter(s)

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataParamType;
int32_t sceSaveDataGetParam(
	const SceSaveDataMountPoint *mountPoint,
	SceSaveDataParamType paramType,
	void *paramBuf,
	size_t paramBufSize,
	size_t *gotSize
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name |
| `paramType` | Parameter(s) to obtain |
| `paramBuf` | Destination to store the obtained parameter(s) |
| `paramBufSize` | Size of the buffer to specify with `paramBuf` |
| `gotSize` | Destination to store the obtained data size |

For `paramType`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_PARAM_TYPE_ALL` | 0 | Obtain all parameters |
| `SCE_SAVE_DATA_PARAM_TYPE_TITLE` | 1 | Obtain the save data title only |
| `SCE_SAVE_DATA_PARAM_TYPE_SUB_TITLE` | 2 | Obtain the save data subtitle only |
| `SCE_SAVE_DATA_PARAM_TYPE_DETAIL` | 3 | Obtain the save data detailed information only |
| `SCE_SAVE_DATA_PARAM_TYPE_USER_PARAM` | 4 | Obtain the user parameter only |
| `SCE_SAVE_DATA_PARAM_TYPE_MTIME` | 5 | Obtain the update date/time only |

## Return Values

Stores the obtained parameter(s) in `paramBuf`, stores the size in `gotSize`, and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This datatype is used for obtaining save data parameters. Note parameter information is obtained from the save data database and not the param.sfo file.

The values that should be specified for `paramBuf` and `paramBufSize` vary according to the `paramType` specification as follows.

* When `SCE_SAVE_DATA_PARAM_TYPE_ALL` is specified for `paramType`:
  + `paramBuf`: pointer to the `SceSaveDataParam` structure
  + `paramBufSize`: `sizeof(SceSaveDataParam)`
* When `SCE_SAVE_DATA_PARAM_TYPE_TITLE` is specified for `paramType`:
  + `paramBuf`: pointer to the buffer that holds the `SCE_SAVE_DATA_TITLE_MAXSIZE` size
  + `paramBufSize`: `SCE_SAVE_DATA_TITLE_MAXSIZE`
* When `SCE_SAVE_DATA_PARAM_TYPE_SUB_TITLE` is specified for `paramType`:
  + `paramBuf`: pointer to the buffer that holds the `SCE_SAVE_DATA_SUBTITLE_MAXSIZE` size
  + `paramBufSize`: `SCE_SAVE_DATA_SUBTITLE_MAXSIZE`
* When `SCE_SAVE_DATA_PARAM_TYPE_DETAIL` is specified for `paramType`:
  + `paramBuf`: pointer to the buffer that holds the `SCE_SAVE_DATA_DETAIL_MAXSIZE` size
  + `paramBufSize`: must not exceed `SCE_SAVE_DATA_DETAIL_MAXSIZE`
* When `SCE_SAVE_DATA_PARAM_TYPE_USER_PARAM` is specified for `paramType`:
  + `paramBuf`: pointer to a `uint32_t` type variable
  + `paramBufSize`: `sizeof(uint32_t)`
* When `SCE_SAVE_DATA_PARAM_TYPE_MTIME` is specified for `paramType`:
  + `paramBuf`: pointer to a `time_t` type variable (A GMT time will be returned)
  + `paramBufSize`: `sizeof(time_t)`

## Examples

```
// Mounting with sceSaveDataMount3() is complete

size_t gotSize = 0;
time_t mtime;
ret = sceSaveDataGetParam(&mountPoint,
                          SCE_SAVE_DATA_PARAM_TYPE_MTIME,
                          &mtime,
                          sizeof(mtime),
                          &gotSize);
if ( ret < 0 ) {
          // Error handling
}
```

## See Also

`sceSaveDataSetParam()`

# sceSaveDataLoadIcon

Load an icon

## Definition

```
#include <save_data.h>
int32_t sceSaveDataLoadIcon(
	const SceSaveDataMountPoint *mountPoint,
	SceSaveDataIcon *icon
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name of the load source |
| `icon` | Destination to store the loaded icon |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_FILE_NOT_FOUND` | 0x809f000e | No file |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function loads the sce\_sys/icon0.png file of the save data directory specified with `mountPoint` into the buffer specified with `icon`.

Prepare a buffer of an appropriate size in advance and specify it with `icon->buf` and `icon->bufSize`. The size of the loaded icon data will be stored in `icon->dataSize` for normal termination.

## Examples

```
// Mounting with sceSaveDataMount3() is complete
// Allocate iconBuf[] as icon data storage area in advance

SceSaveDataIcon icon;
memset(&icon, 0x00, sizeof(icon));
icon.buf = &iconBuf;
icon.bufSize = iconBufSize;
sceSaveDataLoadIcon(&mountPoint, &icon);
```

## See Also

`sceSaveDataSaveIcon()`

# sceSaveDataSaveIcon

Save an image data on memory as an icon

## Definition

```
#include <save_data.h>
int32_t sceSaveDataSaveIcon(
	const SceSaveDataMountPoint *mountPoint,
	const SceSaveDataIcon *icon
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name of the save destination |
| `icon` | Icon to save |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_NO_SPACE` | 0x809f0009 | There isn't enough free space to write the icon image at the mount point |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` | 0x809f000d | Save data directory is not mounted for writing, or data update has not started |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function saves the icon image specified with `icon` as sce\_sys/icon0.png in the save data directory specified with `mountPoint`.

The `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` error will be returned if `sceSaveDataSaveIcon()` is called under any of the following conditions.

* The mount point was mounted by `sceSaveDataTransferringMount()`
* The mount point mounts save data for the save data memory
* `sceSaveDataPrepare()` has not been called

A parameter error will occur if the specified icon image is invalid. Refer to the [Content Information Specifications](../Content_Information-Specifications/__document_toc.html) document regarding image format of save data icons.

## Examples

```
// Mounting with sceSaveDataMount3() is complete

SceSaveDataIcon icon;
memset(&icon, 0x00, sizeof(icon));
// Prepare icon data for iconBuf[] in advance
icon.buf = &iconBuf;
icon.bufSize = iconBufSize;
icon.dataSize = 32768;  // Icon data size
if ( sceSaveDataSaveIcon(&mountPoint, &icon) < 0 ) {
	// Error handling
}
```

## See Also

`sceSaveDataLoadIcon()`

# sceSaveDataSaveIconByPath

Save an image from the specified path as an icon

## Definition

```
#include <save_data.h>
int32_t sceSaveDataSaveIconByPath(
	const SceSaveDataMountPoint *mountPoint,
	const char *iconPath
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name of the save destination |
| `iconPath` | Path of the icon to save |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_NO_SPACE` | 0x809f0009 | There isn't enough free space to write the icon image at the mount point |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` | 0x809f000d | Save data directory is not mounted for writing, or data update has not started |
| `SCE_SAVE_DATA_ERROR_FILE_NOT_FOUND` | 0x809f000e | No file |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function saves the save data icon file specified with `iconPath` to the save data directory specified with `mountPoint` as sce\_sys/icon0.png.

The `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` error will be returned if `sceSaveDataSaveIconByPath()` is called under any of the following conditions.

* The mount point was mounted by `sceSaveDataTransferringMount()`
* The mount point mounts save data for the save data memory
* `sceSaveDataPrepare()` has not been called

For `iconPath`, specify a file path that starts with "/app0/" of the `SCE_SAVE_DATA_ICON_PATH_MAXSIZE` size or less (including the NULL terminator). The characters \, :, \*, ?, ", <, >, and | or the string "../" must not be included.

A parameter error will occur if the string specified in `iconPath` is invalid or if the image format of the specified icon file is invalid. Refer to the [Content Information Specifications](../Content_Information-Specifications/__document_toc.html) document regarding image format of save data icons.

To specify the application's save data default image, specify `SCE_SAVE_DATA_FILEPATH_DEFAULT_ICON`.

## Examples

```
// Mounting with sceSaveDataMount3() is complete

// Prepare a save data icon file in the application data
const char iconPath[] = "/app0/savedata_icon/icon00.png";
if ( sceSaveDataSaveIconByPath(&mountPoint, &iconPath) < 0 ) {
	// Error handling
}
```

## See Also

`sceSaveDataLoadIcon()`

# sceSaveDataSetParam

Set save data parameter(s)

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataParamType;
int32_t sceSaveDataSetParam(
	const SceSaveDataMountPoint *mountPoint,
	SceSaveDataParamType paramType,
	const void *paramBuf,
	size_t paramBufSize
)
```

## Arguments

|  |  |
| --- | --- |
| `mountPoint` | Mount point name |
| `paramType` | Parameter(s) to set |
| `paramBuf` | Value to set (details below) |
| `paramBufSize` | `paramBuf` size |

For `paramType`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_PARAM_TYPE_ALL` | 0 | Update all parameters |
| `SCE_SAVE_DATA_PARAM_TYPE_TITLE` | 1 | Update save data title only |
| `SCE_SAVE_DATA_PARAM_TYPE_SUB_TITLE` | 2 | Update save data subtitle only |
| `SCE_SAVE_DATA_PARAM_TYPE_DETAIL` | 3 | Update save data detailed information only |
| `SCE_SAVE_DATA_PARAM_TYPE_USER_PARAM` | 4 | Update user parameter only |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_NOT_MOUNTED` | 0x809f0004 | Save data directory is not mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` | 0x809f000d | Save data directory is not mounted for writing, or data update has not started |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function is for re-writing the content of param.sfo when newly creating save data with `sceSaveDataMount3()`. In addition to re-writing the param.sfo file, the information registered in the save data database will be updated.

The `SCE_SAVE_DATA_ERROR_BAD_MOUNTED` error will be returned if `sceSaveDataSetParam()` is called under any of the following conditions.

* The mount point was mounted by `sceSaveDataTransferringMount()`
* The mount point mounts save data for the save data memory
* `sceSaveDataPrepare()` has not been called

The values that should be specified for `paramBuf` and `paramBufSize` vary according to the `paramType` specification as follows.

* When `SCE_SAVE_DATA_PARAM_TYPE_ALL` is specified for `paramType`:
  + `paramBuf`: pointer to a `SceSaveDataParam` structure with each parameter value set
  + `paramBufSize`: `sizeof(SceSaveDataParam)`
* When `SCE_SAVE_DATA_PARAM_TYPE_TITLE` is specified for `paramType`:
  + `paramBuf`: character string for the save data title name (NULL-terminated, UTF-8)

    Cannot include a newline character. In addition, must include more than just the NULL terminator.
  + `paramBufSize`: number of bytes including NULL-terminated strings, does not exceed `SCE_SAVE_DATA_TITLE_MAXSIZE`
* When `SCE_SAVE_DATA_PARAM_TYPE_SUB_TITLE` is specified for `paramType`:
  + `paramBuf`: character string for the save data subtitle name (NULL-terminated, UTF-8)

    Cannot include a newline character. Can include just the NULL terminator; if there is an existing subtitle name, it will be cleared.
  + `paramBufSize`: number of bytes including NULL-terminated strings, does not exceed `SCE_SAVE_DATA_SUBTITLE_MAXSIZE`
* When `SCE_SAVE_DATA_PARAM_TYPE_DETAIL` is specified for `paramType`:
  + `paramBuf`: character string for the save data detailed information (NULL-terminated, UTF-8)

    It is possible to include a newline character (0x0a or 0x0d), there is no restriction on the number of lines.

    In addition, it is possible to set only a NULL terminator; if there is existing detailed information, it will be cleared.
  + `paramBufSize`: number of bytes including NULL-terminated strings, does not exceed `SCE_SAVE_DATA_DETAIL_MAXSIZE`
* When `SCE_SAVE_DATA_PARAM_TYPE_USER_PARAM` is specified for `paramType`:
  + `paramBuf`: pointer to a `uint32_t` type user data value
  + `paramBufSize`: `sizeof(uint32_t)`

## Examples

```
// Mounting with sceSaveDataMount3() is complete

char title[SCE_SAVE_DATA_TITLE_MAXSIZE];
memset(title, 0x00, sizeof(title));
strlcpy (title, "This is ABCD00000 Saved Data.",sizeof(title));

ret = sceSaveDataSetParam(&mountPoint,
                          SCE_SAVE_DATA_PARAM_TYPE_TITLE,
                          title,
                          sizeof(title));
if ( ret < 0 ) {
          // Error handling
}
```

## See Also

`sceSaveDataGetParam()`