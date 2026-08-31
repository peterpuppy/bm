# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/sce-save-data-fingerprint.html

# Common Datatypes

# SceSaveDataDirName

Save data directory name

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataDirName {
	char data[SCE_SAVE_DATA_DIRNAME_DATA_MAXSIZE];
} SceSaveDataDirName;
```

## Members

|  |  |
| --- | --- |
| `data` | Save data directory name (NULL-terminated, UTF-8) |

## Description

This datatype is used for specifying the save data directory name when mounting, searching for, and deleting save data. It is also used for receiving directory names in search results.

## Notes

The save data directory name is a string that can include only alphanumeric characters ("a" to "z", "A" to "Z", and "0" to "9"), "-", ".", and "@".

Although directory names created by the system may contain the underscore character "\_" in addition to these characters, the application cannot use the underscore "\_".

In addition, save data directory names beginning with "sce\_" are reserved.

Directory names differing only in terms of uppercase/lowercase letters cannot be created. For example, if a directory named "AAAA" already exists when attempting to create a directory named "aaaa" or "aAaa", it will be determined that a directory with the same name already exists, creation of the new directory will fail, and the following error message will be output to the TTY.

```
[libSceSaveData] ERROR : Save data with the same name as <specified dir name> but different case already exists : <existing dir name>
```

If you are specifying existing save data, it must match exactly, including the uppercase and lowercase letters.

## See Also

`SceSaveDataMount3`, `SceSaveDataDelete`, `SceSaveDataDirNameSearchCond`, `SceSaveDataDirNameSearchResult`, `SceSaveDataEvent`

# SceSaveDataMountPoint

Save data mount point name

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataMountPoint {
	char data[SCE_SAVE_DATA_MOUNT_POINT_DATA_MAXSIZE];
} SceSaveDataMountPoint;
```

## Members

|  |  |
| --- | --- |
| `data` | Mount point name (NULL-terminated, UTF-8) |

## Description

This datatype is used for receiving the save data mount point name. When a save data directory is successfully mounted, the mount point name will be returned to this structure specified for the argument of the mounting function. A file path starting with this mount point name can subsequently be used to access and write/read data in save data until the save data directory is unmounted.

## Notes

The save data mount point name is a character string called "/savedata0", "/savedata1", […] or "/savedata15".

## See Also

`SceSaveDataMountResult`, `sceSaveDataUmount2()`, `sceSaveDataGetMountInfo()`, `sceSaveDataSetParam()`, `sceSaveDataGetParam()`, `sceSaveDataSaveIcon()`, `sceSaveDataLoadIcon()`, `sceSaveDataTransferringMount()`

# SceSaveDataFingerprint

Fingerprint

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataFingerprint {
	char data[SCE_SAVE_DATA_FINGERPRINT_DATA_SIZE];
	char padding[15];
} SceSaveDataFingerprint;
```

## Members

|  |  |
| --- | --- |
| `data` | Fingerprint (NULL-terminated, ASCII "0" to "9", "a" to "f") |
| `padding` | Padding (fill with 0's) |

## Description

This datatype is used for setting the passcode fingerprint when mounting a save data directory for mounting.

A fingerprint is a key for protecting save data from access by other applications. When a passcode (character string comprising "a" to "z", "A" to "Z" and/or "0" to "9" characters) is specified during application package creation, the fingerprint can be obtained as a hash value of the passcode. (For details, refer to the [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html) document.) Other applications will be required to specify this fingerprint when mounting this application's save data for transferring.

However, there is no need for a fingerprint to be specified when the application mounts its own save data.

## See Also

`SceSaveDataDialogWizardParam`, `SceSaveDataTransferringMount`

# SceSaveDataTitleId

Save data title ID

## Definition

```
#include <save_data.h>
typedef struct SceSaveDataTitleId {
	char data[SCE_SAVE_DATA_TITLE_ID_DATA_SIZE];
	char padding[6];
} SceSaveDataTitleId;
```

## Members

|  |  |
| --- | --- |
| `data` | Save data title ID (NULL-terminated, UTF-8) |
| `padding` | Padding (fill with 0's) |

## Description

This datatype is used for specifying the save data title ID when mounting, searching for, and deleting save data of another application.

## Notes

The save data title ID is a character string comprising four uppercase characters and five numeric characters.

## See Also

`SceSaveDataDelete`, `SceSaveDataDirNameSearchCond`, `SceSaveDataEvent`