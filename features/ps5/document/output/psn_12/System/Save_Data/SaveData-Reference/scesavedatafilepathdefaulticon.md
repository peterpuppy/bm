# SaveData Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Reference/scesavedatafilepathdefaulticon.html

# Common Constants

# Character String Sizes

Sizes of various character strings used in the SaveData library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_TITLE_ID_DATA_SIZE` | 10 | Save data title ID size |
| `SCE_SAVE_DATA_DIRNAME_DATA_MAXSIZE` | 32 | Maximum size for a save data directory name |
| `SCE_SAVE_DATA_MOUNT_POINT_DATA_MAXSIZE` | 16 | Maximum size for a mount point name |
| `SCE_SAVE_DATA_FINGERPRINT_DATA_SIZE` | 65 | Fingerprint size |
| `SCE_SAVE_DATA_TITLE_MAXSIZE` | 128 | Maximum size for a save data title name (NULL-terminated, UTF-8) |
| `SCE_SAVE_DATA_SUBTITLE_MAXSIZE` | 128 | Maximum size for a save data subtitle name (NULL-terminated, UTF-8) |
| `SCE_SAVE_DATA_DETAIL_MAXSIZE` | 1024 | Maximum size for save data detailed information (NULL-terminated, UTF-8) |

## Description

These are definitions related to various character string data used in the SaveData library.

# SCE\_SAVE\_DATA\_FILEPATH\_DEFAULT\_ICON

Default icon file path

## Definition

| **Value** | **(String)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_FILEPATH_DEFAULT_ICON` | "/app0/sce\_sys/save\_data.png" | Default icon file path |

## Description

This constant represents the file path where the save data default icon to be used by the SaveData library is stored.

It is used when specifying the default icon for save data with `sceSaveDataSaveIconByPath()`.

# SCE\_SAVE\_DATA\_DIRNAME\_SAVE\_DATA\_MEMORY\*

Save data directory names for save data memory

## Definition

| **Value** | **(String)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY` | "sce\_sdmemory" | Save data directory name corresponding to when no slot is specified for save data memory (value for preserving compatibility) |
| `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_0` | "sce\_sdmemory" | Save data directory name corresponding to slot 0 for save data memory |
| `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_1` | "sce\_sdmemory1" | Save data directory name corresponding to slot 1 for save data memory |
| `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_2` | "sce\_sdmemory2" | Save data directory name corresponding to slot 2 for save data memory |
| `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_3` | "sce\_sdmemory3" | Save data directory name corresponding to slot 3 for save data memory |

## Description

The above constants represent the save data directory names used in the SaveData library for save data memory.

# SCE\_SAVE\_DATA\_FILENAME\_SAVE\_DATA\_MEMORY

Name of the file to which the contents of save data memory is reflected

## Definition

| **Value** | **(String)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_FILENAME_SAVE_DATA_MEMORY` | "memory.dat" | Name of the file to which the content of the save data memory is reflected |

## Description

This constant represents the name of the file, to which the content of the save data memory is reflected, that is used in the SaveData library.

# Various Constants

Various constants used in the SaveData library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SAVE_DATA_MOUNT_MAX_COUNT` | 16 | Maximum number of save data instances that can be mounted simultaneously |
| `SCE_SAVE_DATA_MOUNT_MAX_COUNT_WITH_CONVERSION` | 14 | Maximum number of save data instances that can be mounted simultaneously when performing save data conversion |
| `SCE_SAVE_DATA_DIRNAME_MAX_COUNT` | 1024 | Maximum number of save data directories |
| `SCE_SAVE_DATA_ICON_WIDTH_SMALL` | 688 | Width of the small-sized icon |
| `SCE_SAVE_DATA_ICON_HEIGHT_SMALL` | 388 | Height of the small-sized icon |
| `SCE_SAVE_DATA_ICON_WIDTH_FULL` | 776 | Width of the full-sized icon |
| `SCE_SAVE_DATA_ICON_HEIGHT_FULL` | 436 | Height of the full-sized icon |
| `SCE_SAVE_DATA_ICON_FILE_MAXSIZE2` | 1353344 | Maximum size for an icon file |
| `SCE_SAVE_DATA_ICON_PATH_MAXSIZE` | 128 | Maximum size of the icon's file path |
| `SCE_SAVE_DATA_BLOCK_SIZE2` | 65536 | Block size (bytes) |
| `SCE_SAVE_DATA_BLOCKS_MIN3` | 48 | Minimum number of blocks |
| `SCE_SAVE_DATA_BLOCKS_MAX2` | 16384 | Maximum number of blocks |
| `SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS` | -1 | Allocates system area of the same size as the number of blocks |
| `SCE_SAVE_DATA_MEMORY_MAXSIZE3` | 33554432 | Maximum size for the data sections of the save data memory (maximum value for the total save data memory size of all users) |
| `SCE_SAVE_DATA_MEMORY_SETUP_MAX_COUNT` | 4 | Maximum number of save data memory instances that can be set up simultaneously |
| `SCE_SAVE_DATA_MEMORY_DATANUM_MAX_COUNT` | 5 | Maximum number of data that can be specified at the same time to the data sections of the save data memory |
| `SCE_SAVE_DATA_TRANSACTION_RESOURCE_MAX_COUNT` | 16 | Maximum number of transaction resources that can be created simultaneously |
| `SCE_SAVE_DATA_CREATE_MAX_COUNT` | 496 | Maximum number of save data per user |

## Description

These are various constants used in the SaveData library.

`SCE_SAVE_DATA_DIRNAME_MAX_COUNT` represents the maximum number of save data directories per user per application for when the system software displays save data.

However, `SCE_SAVE_DATA_CREATE_MAX_COUNT` is the maximum number per user when an application creates a new save data directory. Note that SaveData library functions do not check the maximum number of directories, except when creating new ones.