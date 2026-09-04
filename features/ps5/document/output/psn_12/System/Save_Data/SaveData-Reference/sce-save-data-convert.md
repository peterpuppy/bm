# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-convert.html

# Save Data Conversion

# SceSaveDataConvert

Save data conversion parameters

## Definition

```
#include <save_data.h>

typedef struct SceSaveDataConvert {
      SceUserServiceUserId userId;
      int :32;
      const SceSaveDataDirName *srcDirName;
      const SceSaveDataDirName *dstDirName;
      SceSaveDataBlocks dstBlocks;
      uint8_t reserved[24];
} SceSaveDataConvert;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `srcDirName` | Conversion-source save data directory name |
| `dstDirName` | Conversion-destination save data directory name (or NULL) |
| `dstBlocks` | Size of the conversion-destination save data (number of blocks, a value larger than the conversion-source save data size and up to `SCE_SAVE_DATA_BLOCKS_MAX2` (=16384)) |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used when performing save data conversion with `sceSaveDataConvert()`.

For `userId`, specify the user ID obtained with the UserService library.

For `srcDirName`, specify the name of the save data directory of the conversion-source save data.

If the conversion-destination save data directory name is specified in `dstDirName`, the converted save data is renamed to that name. If NULL is specified, renaming is not carried out.

For `dstBlocks`, specify the save data size after the conversion in block units. You cannot specify a value identical to or less than the number of blocks of the conversion-source save data or a value that exceeds `SCE_SAVE_DATA_BLOCKS_MAX2`.

# sceSaveDataConvert

Convert an instance of save data

## Definition

```
#include <save_data.h>
int32_t sceSaveDataConvert(
	const SceSaveDataConvert *convert
)
```

## Arguments

|  |  |
| --- | --- |
| `convert` | Save data conversion parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Conversion-source save data directory is mounted |
| `SCE_SAVE_DATA_ERROR_EXISTS` | 0x809f0007 | Conversion-destination save data directory exists |
| `SCE_SAVE_DATA_ERROR_NOT_FOUND` | 0x809f0008 | Conversion-source save data directory does not exist |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_MOUNT_FULL` | 0x809f000c | Maximum mount value has been reached |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_SAVE_DATA_ERROR_NO_NEED_CONVERT` | 0x809f001e | Attempted to convert save data to the same size (`convert->dstBlocks` is the same numerical value as the current number of blocks) |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |
| `SCE_SAVE_DATA_ERROR_BLOCKS_FEWER_THAN_SRC` | 0x809f0020 | Attempted to reduce the size of save data (`convert->dstBlocks` is less than the number of blocks of the conversion-source save data) |

## Description

This function converts the size of save data. It can be used to increase the size of save data.

This function returns immediately after requesting the system to perform conversion. Use `sceSaveDataGetConvertProgress()` to obtain the conversion progress. Use `sceSaveDataGetEventResult()` to obtain the conversion process results.

If a value exceeding the maximum number of blocks or a value less than the minimum number of blocks is specified in `convert->dstBlocks`, the `SCE_SAVE_DATA_ERROR_PARAMETER` error will be returned.

If an incorrect directory name or save data memory directory name (`sce_sdmemory*`) is specified, the `SCE_SAVE_DATA_ERROR_PARAMETER` error will be returned.

If the directory name of mounted save data is specified, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned.

If a save data directory name that already exists is specified in `convert->dstDirName`, the `SCE_SAVE_DATA_ERROR_EXISTS` error will be returned.

If you call this function in a state where you have carried out more mounts than defined by `SCE_SAVE_DATA_MOUNT_MAX_COUNT_WITH_CONVERSION`, the `SCE_SAVE_DATA_ERROR_MOUNT_FULL` error will be returned.

If a save data directory name is specified in `convert->srcDirName`, specifying the same number of blocks as the conversion-source save data in `convert->dstBlocks` will return the `SCE_SAVE_DATA_ERROR_NO_NEED_CONVERT` error.

If the initialization function of the UserService library (`sceUserServiceInitialize()`) has not been called, the `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` error will be returned.

If a value less than the number of blocks of the conversion-source save data is specified in `convert->dstBlocks`, the `SCE_SAVE_DATA_ERROR_BLOCKS_FEWER_THAN_SRC` error will be returned.

## Examples

```
SceSaveDataConvert conv;
SceSaveDataDirName srcDirName{"ABCD00001"};
const uint32_t srcBlocks = SCE_SAVE_DATA_BLOCKS_MIN3;

memset(&conv, 0x0, sizeof(conv));
conv.userId = userId;
conv.srcDirName = &srcDirName;
conv.dstBlocks = srcBlocks *2;

ret = sceSaveDataConvert(&conv);
if(ret < SCE_OK)
{
	// Error handling
}
```

## Notes

* The conversion process performed by this function uses the system's I/O resources and does not consume the resources allocated for SSD write throttling.
* The time required for the conversion may take longer depending on the state and size of the save data.
* If the file system runs out of space or if the save data is corrupted and the conversion operation fails, the result is returned to `sceSaveDataGetEventResult()`.
* If one of the following functions is called for save data that is being converted, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned:
  + `sceSaveDataMount3()`
  + `sceSaveDataDelete()`
  + `sceSaveDataConvert()`
* If one of the following functions is called while save data conversion is being carried out, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned:
  + `sceSaveDataTerminate()`
  + `sceSaveDataDirNameSearch2()`

## See Also

`SceSaveDataEvent`, `sceSaveDataGetConvertProgress()`