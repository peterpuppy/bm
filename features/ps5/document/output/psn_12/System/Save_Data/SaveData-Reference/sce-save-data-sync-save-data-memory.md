# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-sync-save-data-memory.html

# Save Data Memory

# SceSaveDataMemoryData

Parameters for accessing data of save data memory

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataMemoryData {
	void *buf;
	size_t bufSize;
	off_t offset;
	uint8_t reserved[40];
} SceSaveDataMemoryData;
```

## Members

When used as the `data` member of `SceSaveDataMemoryGet2`

|  |  |
| --- | --- |
| `buf` | Destination to store obtained data |
| `bufSize` | Size of the data to obtain |
| `offset` | Offset value of the data to obtain in the save data memory |
| `reserved` | Reserved area (fill with 0's) |

When used as the `data` member of `SceSaveDataMemorySet2`

|  |  |
| --- | --- |
| `buf` | Data to write to the save data memory |
| `bufSize` | Size of the data to write |
| `offset` | Offset value in the save data memory where data will be written |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used when setting/obtaining data to/from the save data memory with `sceSaveDataGetSaveDataMemory2()` or `sceSaveDataSetSaveDataMemory2()`.

# SceSaveDataMemoryGet2

Parameters for obtaining save data memory data

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataMemoryGet2 {
	SceUserServiceUserId userId;
	uint8_t padding[4];
	SceSaveDataMemoryData *data;
	SceSaveDataParam *param;
	SceSaveDataIcon *icon;
	uint32_t slotId;
	uint8_t reserved[28];
} SceSaveDataMemoryGet2;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `padding` | Padding area (fill with 0's) |
| `data` | Destination to store the obtained save data memory data, or NULL |
| `param` | Destination to store the obtained save data memory parameters, or NULL |
| `icon` | Destination to store the obtained save data memory icon (specify NULL) |
| `slotId` | Slot ID |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used when obtaining data from the save data memory with `sceSaveDataGetSaveDataMemory2()`.

Specify the destinations to store the respective data obtained from the save data memory in `data` and `param`. Specify NULL if such information is not required.

For `slotId`, specify the slot from which data will be obtained with a value in the range from 0 to 3. Specifying a numerical value outside that range will result in a parameter error. If a slot that has not been set up for the user is specified, an error indicating that setup has not been performed will be returned.

# SceSaveDataMemorySet2

Parameters for setting save data memory data

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataMemorySet2 {
	SceUserServiceUserId userId;
	uint8_t padding[4];
	const SceSaveDataMemoryData *data;
	const SceSaveDataParam *param;
	const SceSaveDataIcon *icon;
	uint32_t dataNum;
	uint32_t slotId;
	uint8_t reserved[24];
} SceSaveDataMemorySet2;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `padding` | Padding area (fill with 0's) |
| `data` | Data to set to the save data memory, or NULL |
| `param` | Parameters to set to the save data memory, or NULL |
| `icon` | Icon to set to the save data memory (specify NULL) |
| `dataNum` | Number of data to set to the save data memory |
| `slotId` | Slot ID |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used when setting data to the save data memory with `sceSaveDataSetSaveDataMemory2()`.

Specify the information to set to the save data memory in `data`, `param`, and `icon`. Specify NULL if there is no need to set such information.

If there is one data you want to set to the save data memory, set the address, size, and write destination of the data to write in the `SceSaveDataMemoryData` structure, and specify a pointer to this structure in `data`. Specify 1 in `dataNum`.

If there are multiple data you want to set to the save data memory, specify an array of the `SceSaveDataMemoryData` structure in `data` and the number of array elements in `dataNum`. This enables multiple areas on the save data memory to be atomically updated. The maximum number of elements that can be specified at one time is `SCE_SAVE_DATA_MEMORY_DATANUM_MAX_COUNT`. An error will not occur even if the areas of the data specified in the elements overlap, and content will be applied in order beginning with the top element.

If there is no need to set data to the save data memory, specify NULL in `data` and 0 in `dataNum`. A parameter error will occur at this time if a value other than 0 is specified in `dataNum`.

For `slotId`, specify the slot whose data will be set with a value in the range from 0 to 3. Specifying a numerical value outside that range will result in a parameter error. If a slot that has not been set up for the user is specified, an error indicating that setup has not been performed will be returned.

# SceSaveDataMemorySetup2

Parameters for save data memory setup

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataSaveDataMemoryOption;

typedef struct SceSaveDataMemorySetup2 {
	SceSaveDataSaveDataMemoryOption option;
	SceUserServiceUserId userId;
	size_t memorySize;
	size_t iconMemorySize;
	const SceSaveDataParam *initParam;
	const SceSaveDataIcon *initIcon;
	uint32_t slotId;
	uint8_t reserved[20];
} SceSaveDataMemorySetup2;
```

## Members

|  |  |
| --- | --- |
| `option` | Options |
| `userId` | User ID |
| `memorySize` | Memory size (number of bytes) |
| `iconMemorySize` | Icon memory size (specify 0) |
| `initParam` | Save data parameters used upon newly creating the save data memory, or NULL |
| `initIcon` | Icon used upon newly creating the save data memory (specify NULL) |
| `slotId` | Slot ID |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used when setting up the save data memory with `sceSaveDataSetupSaveDataMemory2()`. For details about the behavior of the save data memory, such as the size of shared memory that will be requested when setting up the save data memory, refer to [SaveData Library Overview - Save Data Memory](../SaveData-Overview/save-data-memory.html).

For `option`, a bitwise OR of the following values can be specified.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_MEMORY_OPTION_NONE` | 0x00000000 | No options |
| `SCE_SAVE_DATA_MEMORY_OPTION_SET_PARAM` | 0x00000001 | Make it possible to change the save data parameters |
| `SCE_SAVE_DATA_MEMORY_OPTION_DOUBLE_BUFFER` | 0x00000002 | Perform double buffering |

When `SCE_SAVE_DATA_MEMORY_OPTION_SET_PARAM` is set for `option`, an `SceSaveDataParam` area that includes the title name, subtitle name, detailed information, etc., will be allocated in shared memory as a parameter section, and it will subsequently be possible to set these parameters with `initParam` and update them with `sceSaveDataSetSaveDataMemory2()`.

When `SCE_SAVE_DATA_MEMORY_OPTION_DOUBLE_BUFFER` is set for `option`, twice the size of the value specified for `memorySize` will be allocated as a data section in shared memory. This data section will be used as a double buffer comprising two buffers each of `memorySize`, and the application will alternately write to one of the buffers every time `sceSaveDataSetSaveDataMemory2()` is called. The most recently written buffer data will be saved when the save data memory is saved. If the application crashes during buffer writing, the data written to the other buffer will be saved by the system. If the application crashes during buffer writing when this option is not set, buffer data will not be saved by the system.

For `memorySize`, specify the size of the data section of the save data memory. Set a value greater than 0 byte and equal to or less than `SCE_SAVE_DATA_MEMORY_MAXSIZE3` (32 MiB). Although `sceSaveDataSetupSaveDataMemory2()` can be called for each user, the total size of `memorySize` specified in each call cannot exceed `SCE_SAVE_DATA_MEMORY_MAXSIZE3` as well. Determine the save data memory size by considering tradeoffs with the number of users who'll be using the save data memory. In addition, note that if `SCE_SAVE_DATA_MEMORY_OPTION_DOUBLE_BUFFER` is specified for `option`, the maximum value that can be specified here and the maximum combined size of the values for memorySize that can be specified for each user will be `SCE_SAVE_DATA_MEMORY_MAXSIZE3/2` (16 MiB). The application will be able to freely use the memory of the size specified here as the save data memory.

Note the memory area to share will be allocated from the system if a space of `memorySize` (`memorySize`\*2 if `SCE_SAVE_DATA_MEMORY_OPTION_DOUBLE_BUFFER` is specified to `option`) is available in system memory (4 MiB). If not, the memory area will be allocated from game memory.

For `iconMemorySize`, a parameter error will occur if a value other than 0 is specified.

For `initParam`, specify the save data parameters to apply upon newly creating the save data memory. This specification will be ignored when save data for the save data memory already exists on console storage.

For `initIcon` , a parameter error will occur if a value other than NULL is specified.

For `slotId`, specify the slot that will be set up for the user with a value in the range from 0 to 3. Specifying a numerical value outside that range will result in an `SCE_SAVE_DATA_ERROR_PARAMETER` error. If a slot that has already been set up for the user is specified, `SCE_SAVE_DATA_ERROR_BUSY` will be returned. Additionally, if the total number of slots that have been set up for all currently logged-in users has reached `SCE_SAVE_DATA_MEMORY_SETUP_MAX_COUNT`, then `SCE_SAVE_DATA_ERROR_SETUP_MAX_LIMIT` will be returned.

## Notes

If save data parameters are not specified with `initParam` (if NULL is specified) when creating new save data memory, default save data parameters will be used. The system default icon image will be used for the icon when creating new save data memory.

# SceSaveDataMemorySync

Parameters for saving the save data memory

## Definition

```
#include <save_data.h>
typedef uint32_t SceSaveDataMemorySyncOption;
typedef struct SceSaveDataMemorySync {
	SceUserServiceUserId userId;
	uint32_t slotId;
	SceSaveDataMemorySyncOption option;
	uint8_t reserved[28];
} SceSaveDataMemorySync;
```

## Members

|  |  |
| --- | --- |
| `userId` | User ID |
| `slotId` | Slot ID |
| `option` | Options |
| `reserved` | Reserved area (fill with 0's) |

## Description

This datatype is used for setting the required information when saving the save data memory using `sceSaveDataSyncSaveDataMemory()`.

For `slotId`, specify the slot to which save data memory will be saved with a value in the range from 0 to 3. Specifying a numerical value outside that range will result in a parameter error. If a slot that has not been set up for the user is specified, an error indicating that setup has not been performed will be returned.

For `option`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_MEMORY_SYNC_OPTION_NONE` | 0x00000000 | No options  (carry out processing asynchronously) |
| `SCE_SAVE_DATA_MEMORY_SYNC_OPTION_BLOCKING` | 0x00000001 | Carry out processing synchronously |

# sceSaveDataGetSaveDataMemory2

Get data/parameters from save data memory

## Definition

```
#include <save_data.h>
int32_t sceSaveDataGetSaveDataMemory2(
	SceSaveDataMemoryGet2 *getParam
)
```

## Arguments

|  |  |
| --- | --- |
| `getParam` | Parameters for obtaining data |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_SAVE_DATA_ERROR_MEMORY_NOT_READY` | 0x809f0012 | Save data memory is not set up |
| `SCE_SAVE_DATA_ERROR_BUSY_FOR_SAVING` | 0x809f0016 | Save data memory is being saved |

## Description

This function (equivalent to a read of standard save data and `sceSaveDataGetParam(SCE_SAVE_DATA_PARAM_TYPE_ALL)`) obtains data and parameters such as the title name from the save data memory that was set up with `sceSaveDataSetupSaveDataMemory2()`.

When obtaining save data parameters with `getParam->param` specified, a parameter error will occur if `SCE_SAVE_DATA_MEMORY_OPTION_SET_PARAM` was not specified for `setupParam->option` upon setup of the save data memory.

## Examples

```
// Save data memory preparations with sceSaveDataSetupSaveDataMemory2() are complete

SceSaveDataMemoryGet2 getParam;
memset(&getParam, 0x00, sizeof(getParam));
getParam.userId = userId;
getParam.data = &data;
getParam.param = &param;
getParam.slotId = 0;

ret = sceSaveDataGetSaveDataMemory2(&getParam);
if (ret < SCE_OK ) {
          // Error handling
}
```

## Notes

When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).

## See Also

`sceSaveDataSetSaveDataMemory2()`

# sceSaveDataSetSaveDataMemory2

Write data/parameters to save data memory

## Definition

```
#include <save_data.h>
int32_t sceSaveDataSetSaveDataMemory2(
	const SceSaveDataMemorySet2 *setParam
)
```

## Arguments

|  |  |
| --- | --- |
| `setParam` | Parameters for setting data |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_SAVE_DATA_ERROR_MEMORY_NOT_READY` | 0x809f0012 | Save data memory is not set up |
| `SCE_SAVE_DATA_ERROR_BUSY_FOR_SAVING` | 0x809f0016 | Save data memory is being saved |

## Description

This function (equivalent to a write to standard save data or `sceSaveDataSetParam(SCE_SAVE_DATA_PARAM_TYPE_ALL)`) writes data and parameters such as the title name to the save data memory that was set up with `sceSaveDataSetupSaveDataMemory2()`.

A parameter error will occur if `setParam->param` is specified and `SCE_SAVE_DATA_MEMORY_OPTION_SET_PARAM` was not specified for `setupParam->option` upon setup of the save data memory.

## Examples

```
// Save data memory preparations with sceSaveDataSetupSaveDataMemory2() are complete

SceSaveDataMemorySet2 setParam;
memset(&setParam, 0x00, sizeof(setParam));
setParam.userId = userId;
setParam.data = &data;
setParam.param = &param;
setParam.dataNum = dataNum;
setParam.slotId = 0;

ret = sceSaveDataSetSaveDataMemory2(&setParam);
if (ret < SCE_OK ) {
          // Error handling
}
```

## Notes

When called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).

## See Also

`sceSaveDataGetSaveDataMemory2()`

# sceSaveDataSetupSaveDataMemory2

Set up save data memory

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataMemorySetupResult {
    size_t    existedMemorySize;
    uint8_t   reserved[16];
} SceSaveDataMemorySetupResult;

int32_t sceSaveDataSetupSaveDataMemory2 (
	const SceSaveDataMemorySetup2 *setupParam,
	SceSaveDataMemorySetupResult *result
)
```

## Arguments

|  |  |
| --- | --- |
| `setupParam` | Setup parameters |
| `result` | Destination to store the setup result |

## Return Values

Stores the setup result in `*result` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data directory for the save data memory is mounted or the save data memory has already been set up |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_SAVE_DATA_ERROR_SETUP_MAX_LIMIT` | 0x809f0017 | The maximum number of save data memory instances that can be set up per user has exceeded `SCE_SAVE_DATA_MEMORY_SETUP_MAX_COUNT`, or the total maximum of save data for all users in total has exceeded `SCE_SAVE_DATA_MEMORY_MAXSIZE3` |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function initializes the save data memory.

For details about the parameters that can be specified, refer to the "Description" of `SceSaveDataMemorySetup2`.

If save data (sce\_sdmemory\*, that is, the save data directory corresponding to the slot ID specified with `setupParam->slotId` and which is one of sce\_sdmemory, sce\_sdmemory1, sce\_sdmemory2, or sce\_sdmemory3) saved using the save data memory feature already exists, the data file (memory.dat) in the save data will be loaded.

The loaded memory.dat will be placed at the beginning of the save data memory. If the size specified with `setupParam->memorySize` is greater than the size of memory.dat, the save data memory after the memory.dat size will be cleared with 0's. If, conversely, the size specified with `setupParam->memorySize` is less than the size of memory.dat, only the first `setupParam->memorySize` part of memory.dat will be loaded.

If sce\_sdmemory does not exist, nothing will be loaded to the save data memory, and its usage will start in the initial state with the entire area filled with 0's. The sce\_sdmemory directory will not be created at this time; therefore, this function will not return an insufficient free space error for the file system.

## Examples

```
// Initialization with sceSaveDataInitialize3() is complete

// Save data memory use start

SceSaveDataMemorySetup2 param;
memset(&param, 0x00, sizeof(param));
param.option = SCE_SAVE_DATA_MEMORY_OPTION_SET_PARAM;
param.userId = userId;
param.memorySize = 4 * 1024 * 1024;
param.iconMemorySize = 0;
param.slotId = 0;

ret = sceSaveDataSetupSaveDataMemory2(&param, NULL);
if ( ret < 0 ) {
          // Error handling
}
```

## Notes

This function is a synchronous function and may perform blocking for a long period of time in order to carry out save data load processing or deletion processing of corrupted save data. Furthermore, when called immediately after the start of application suspension, the blocking time of this function may be longer than usual. For details, refer to [SaveData Library Overview - Using the Library - Notes Regarding the Calling-Source Thread](../SaveData-Overview/notes-regarding-the-calling-source-thread.html).

## See Also

`sceSaveDataGetSaveDataMemory2()`, `sceSaveDataSetSaveDataMemory2()`

# sceSaveDataSyncSaveDataMemory

Save an instance of save data memory

## Definition

```
#include <save_data.h>
int32_t sceSaveDataSyncSaveDataMemory(
	const SceSaveDataMemorySync *syncParam
)
```

## Arguments

|  |  |
| --- | --- |
| `syncParam` | Synchronization parameters |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_ERROR_PARAMETER` | 0x809f0000 | Parameter is invalid |
| `SCE_SAVE_DATA_ERROR_NOT_INITIALIZED` | 0x809f0001 | The SaveData library isn't initialized |
| `SCE_SAVE_DATA_ERROR_OUT_OF_MEMORY` | 0x809f0002 | Memory allocation failed |
| `SCE_SAVE_DATA_ERROR_BUSY` | 0x809f0003 | Save data directory is mounted |
| `SCE_SAVE_DATA_ERROR_INTERNAL` | 0x809f000b | Fatal internal error |
| `SCE_SAVE_DATA_ERROR_INVALID_LOGIN_USER` | 0x809f0011 | Specified user is not logged in |
| `SCE_SAVE_DATA_ERROR_MEMORY_NOT_READY` | 0x809f0012 | Save data memory is not ready |
| `SCE_SAVE_DATA_ERROR_BUSY_FOR_SAVING` | 0x809f0016 | Save data memory is being saved |
| `SCE_USER_SERVICE_ERROR_NOT_INITIALIZED` | 0x80960002 | UserService library is not initialized |

## Description

This function saves the save data memory.

When called as an asynchronous processing, this function returns immediately after requesting the system to perform save processing. Use `sceSaveDataGetEventResult()` to obtain the save results.

When called as a synchronous processing, this function blocks until save processing completes and returns the save result.

`SCE_SAVE_DATA_ERROR_BUSY` will be returned when this function is called for a save data memory directory that was mounted by `sceSaveDataMount3()` or `sceSaveDataTransferringMount()`.

`SCE_SAVE_DATA_ERROR_MEMORY_NOT_READY` will be returned when this function is called for save data memory that has not been set up.

`SCE_SAVE_DATA_ERROR_BUSY_FOR_SAVING` will be returned when an attempt is made to save the save data memory for a slot for which save processing is underway. When saving multiple slots at the same time, each will be processed in the call order of the save functions.

## Examples

```
// Save data memory preparations with sceSaveDataSetupSaveDataMemory2() are complete

ret = sceSaveDataSyncSaveDataMemory(syncParam);
if (ret < SCE_OK ) {
          // Error handling
}
```

## Notes

Since the save data memory is saved by the system at appropriate timings, there is basically no need for the application to explicitly call this function. Do not implement the application so that this function is called frequently. For details about the timings at which save data memory is saved, refer to the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document.

## See Also

`sceSaveDataGetSaveDataMemory2()`, `sceSaveDataSetSaveDataMemory2()`