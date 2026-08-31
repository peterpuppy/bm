# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/automatic-deletion-of-the-corrupted-save-data.html

# Using the Library

This topic explains in detail a series of procedures relating to the management of save data, as well as points that should be noted. That is, it discusses in detail important matters in the processing of save data, beginning with the basic procedures for doing so.

# Basic Procedure

This chapter explains the basic procedure for accessing save data. An overview of the process flow is as follows.

1. **[Initialize the UserService library](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_1)**
2. **[Initialize the SaveData library](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_2)**
3. **[Create a transaction resource](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_3)**
4. **[Mount save data](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_4)**
5. **[Start the save data update](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_5)**
6. **[Write/read data files](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_6)**
7. **[Commit the save data update](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_7)**
8. **[Unmount the save data](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_8)**
9. **[Terminate the SaveData library](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_9)**
10. **[Terminate the UserService Library](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_10)**

The details of each step are as follows.

1. **Initialize the UserService library**

   Call `sceUserServiceInitialize()` or `sceUserServiceInitialize2()` to initialize the library.
2. **Initialize the SaveData library**

   Call `sceSaveDataInitialize3()` to initialize the library.
3. **Create a transaction resource**

   To write to save data, call `sceSaveDataCreateTransactionResource()` to create a transaction resource and obtain the handle for it. Specify the size of the transaction resource to create as an argument. (Refer to "[Save Data Update Transaction](save-data-update-transaction.html)" for details about transaction resources.)
4. **Mount save data**

   Call `sceSaveDataMount3()` to mount save data. Specify the user ID and save data directory name as arguments. Specifications for newly creating save data and for the read-only mode can also be made as the mount mode. In the case of newly creating save data, specify the size of the save data itself and the size of the save data system area (`SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS`)

   The mount point name will be obtained when mounting is successful. Use a path that includes this mount point for subsequent file access.
5. **Start the save data update**

   `sceSaveDataPrepare()` must be called in advance to write to save data. As arguments, specify the mount point name of the write target and the handle of the transaction resource. This will make the mount point write-enabled.
6. **Write/read data files**

   The writing and reading of data files are performed using the file system API features that are described in the [Kernel Reference](../Kernel-Reference/__document_toc.html) document and the file access API features in stdio.h of the C/C++ standard libraries.

   The path will be the mount point name obtained during mounting + "/" + the filename (or directory name).

   Writing to/reading from the param.sfo and icon0.png files used by the system can be performed using exclusive functions for each.

   The save data parameters included in param.sfo can be written/read using `sceSaveDataSetParam()`/`sceSaveDataGetParam()`.

   icon0.png (save data icon) can be saved using `sceSaveDataSaveIcon()` or `sceSaveDataSaveIconByPath()` and loaded using `sceSaveDataLoadIcon()`.
7. **Commit the save data update**

   Call `sceSaveDataCommit()` after writing to save data and commit the save data update. As an argument, specify the handle of the transaction resource that was specified in `sceSaveDataPrepare()` .

   The mount point will return to read-only when the update is committed. Steps [5](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_5) through [7](basic-procedure.html#save-data-library-overview_2_1__save-data-library-overview_2_1_7) can be repeated as necessary. The transaction resource used for updating save data can be deleted after the update is committed by calling `sceSaveDataDeleteTransactionResource()`.
8. **Unmount the save data**

   Save data can be unmounted by calling `sceSaveDataUmount2()`. The following three modes can be selected for unmounting save data:

   * A mode that makes unmount fail if there is an update that hasn't been committed yet with `sceSaveDataCommit()`
   * A mode that commits any update that hasn't been committed yet with `sceSaveDataCommit()` and then unmounts the save data
   * A mode that cancels any update that hasn't been committed yet with `sceSaveDataCommit()` and then unmounts the save data
9. **Terminate the SaveData library**

   Normally, there is no need to terminate this library; however, when you want to free resources (for example), call `sceSaveDataTerminate()` to perform termination processing. When `sceSaveDataTerminate()` is called in a state where save data is mounted, the `SCE_SAVE_DATA_ERROR_BUSY` error will be returned. Created transaction resources will be deleted automatically when the library terminates; however, it can also be deleted at any time other than during a save data update by calling `sceSaveDataDeleteTransactionResource()`.
10. **Terminate the UserService Library**

    When the UserService library is no longer needed, call `sceUserServiceTerminate()` to perform termination processing. This releases resources that were allocated internally in the library.

## API Summary

The functions used in basic processing of the SaveData library are shown below.

Functions Used in Basic Processing

| **Function** | **Description** |
| --- | --- |
| `sceSaveDataInitialize3()` | Function that initializes the library |
| `sceSaveDataCreateTransactionResource()` | Function to create a transaction resource |
| `sceSaveDataMount3()` | Function that mounts a save data directory |
| `sceSaveDataPrepare()` | Function that starts a save data update |
| `sceSaveDataSetParam()` | Function that sets system file information |
| `sceSaveDataGetParam()` | Function that obtains system file information |
| `sceSaveDataSaveIcon()` | Function that saves an icon |
| `sceSaveDataLoadIcon()` | Function that loads an icon |
| `sceSaveDataCommit()` | Function to commit a save data update |
| `sceSaveDataUmount2()` | Function that unmounts a save data directory |
| `sceSaveDataDeleteTransactionResource()` | Function to delete a transaction resource |
| `sceSaveDataTerminate()` | Function that terminates the library |

# Setting an Icon

The application can have one of the images it holds be set as the save data icon. The application can also dynamically create and set the save data icon. The set icon will be stored as icon0.png.

## Automatically Setting an Icon

Prepare the default icon image to be used for save data as /app0/sce\_sys/save\_data.png. This icon file will be set automatically (copied as icon0.png) according to the parameters set when `sceSaveDataMount3()` is called for the creation of new save data.

For details about the sce\_sys directory that contains save\_data.png, refer to the [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html) document.

Furthermore, "sce\_sys\save\_data.png" placed under the working directory will be used as the save data icon when the application is launched from ★Workspace during development.

## Dynamically Setting an Icon

The application can use the following functions to set an arbitrary image as a save data icon:

* `sceSaveDataSaveIcon()`: image data on memory can be set as the save data icon
* `sceSaveDataSaveIconByPath()`: an image file can be directly specified and set as the save data icon

## Icon Image Format

Images of the required format must be specified for save data images regardless of how the save data icon image is set (automatically or dynamically). Refer to the [Content Information Specifications](../Content_Information-Specifications/__document_toc.html) document for the details of the image format.

If the format of the save data icon image is invalid, the creation of new save data and the update of save data will fail, and the following error message will be output to the TTY:

```
[libSceSaveData] ERROR : check icon0.png failed : <error code>
```

For example, if the format of save\_data.png is invalid, then when the application automatically attempts to set that image file as the icon for save data newly created with `sceSaveDataMount3()`, `SCE_SAVE_DATA_ERROR_PARAMETER` will be returned and the save data will not be created. The following error message will be output to the TTY:

```
[libSceSaveData] ERROR : check icon0.png failed : 0x809f8004
```

# Save Data Update Periods

The application must complete updates to save data within 15 seconds or less. As it degrades the user experience to make users wait for long periods of time when application suspension is blocked, the system will induce an application crash and forcibly unmount save data if an attempt is made to continue an update for over 15 seconds.

## Write Processing in Consideration of the Update Period

The speed of a save data write will vary depending on various factors such as SSD write throttling (explained later in the document) and competition with other threads that are accessing system storage.

To avoid obstructing application termination/suspension for a long period of time, determine the application's save specifications and write processing implementation in consideration of unfavorable conditions. Points to note are as follows.

* Avoid save processing (especially auto save) from being performed at the same time as high-priority continuous read processing (e.g., video streaming).

  Set save points at locations where streaming will not be performed, and perform appropriate mutual exclusion.
* Reduce the frequency of read processing and write processing.

  The frequency of reading and writing the same amount of data can be reduced by allocating a large buffer area. Because increasing the buffer size is not effective when many small files are accessed, file composition should also be adjusted to reduce the number of files accessed at once.
* Reduce the size of data to write within a single update period as much as possible.

  First, reduce the size of data to write in a single save by compressing the data and adjusting file composition. It is also effective to partition the size and to perform update start, write, and update committing multiple times. It is strongly recommended that the user is notified of the ongoing save (for example, by displaying a progress bar) when taking such measures. Even if a progress bar is displayed, the user may accidentally perform terminate/suspend operation; we strongly recommend an implementation where save data can still be properly read even after multiple writes could not be completed.

## SSD Write Throttling Countermeasures

Writes to storage via SaveData library function calls are subject to bandwidth limiting by SSD write throttling. (Refer to [Kernel Overview - File System - SSD Write Throttling](../Kernel-Overview/ssd-write-throttling.html) for more details about bandwidth limiting.) It is therefore necessary to avoid performing saves that cause a large volume of writing in a short period of time. However, `sceSaveDataConvert()` is not subject to bandwidth-limiting behavior.

# System Behavior upon User Logout

If the save data of a user is being mounted when the user logs out, logout processing by the system will be delayed until the save data is unmounted.

However, because the user experience will be negatively affected if the user is made to wait a long time, save data that isn't unmounted within 30 seconds from the start of logout processing will be forcibly unmounted by the system.

# Automatic Deletion of Corrupted Save Data

If the system detects save data corruption when the application mounts save data, processing to delete the save data is carried out automatically. Also refer to the section "[Corruption of Save Data](corruption-of-save-data.html)".

If save data has been deleted when mounting is executed, the result will differ according to the mount mode, as follows.

* New creation mode and read-only mode logic disjunction: newly created save data will be mounted
* Read-only mode: the `SCE_SAVE_DATA_ERROR_NOT_FOUND` error will be returned

Note:

When processing to delete save data is carried out, a notification will be displayed to the user. Therefore, there is no need for the application to notify the user.

For Development Kits/Testing Kits only, the save data being deleted will be displayed in a notification in the format `DirName:` *Save data directory name*.

## Special Case When Processing to Delete Save Data Is Not Carried Out

When save data can't be mounted because "Fake Owner" (refer to "[Owner Information on Development Machines](transferring-save-data-between-systems.html#save-data-library-overview_4_1__save-data-library-overview_4_1_1)") or "Keystone File" (refer to "[Keystone File](transferring-save-data-between-systems.html#save-data-library-overview_4_1__save-data-library-overview_4_1_2)") is incorrectly set, processing to delete the save data won't be carried out, and the `SCE_SAVE_DATA_ERROR_BROKEN` error will be returned. This behavior is to prevent save data from being deleted automatically during development when a setting is wrongly made.

# Handling of Save Data After an Update Is Applied to the Application

Take care to maintain save data compatibility before and after an update is applied to the application. Carelessly changing the data format may cause the system to stall. It is effective to take measures, such as embedding the data format version to save data and performing appropriate processing according to the version. At the very least, ensure that a stall does not occur when save data - saved by the application before the update was applied to the application - is loaded after the update has been applied. Also, do not forget to unmount save data if it cannot be correctly loaded.

# Notes on Handling Save Data Containing Information That Is Dependent on Additional Content

Even if the user has the entitlement required to use additional content, they may lose this entitlement in the future. As required by TRC [R5116](../../../TRC/latest/TRC/R5116.html), when the user does not have the entitlement to use the additional content, the resulting effects of that additional content must not be shown in gameplay. Therefore, when saving information that contains the effects of the additional content in save data, design and implementation must be carefully considered so that TRC [R5116](../../../TRC/latest/TRC/R5116.html) is satisfied even when the user loses the entitlement to use the additional content. In other words, the information saved in the save data must be used appropriately after confirming whether or not the user has the entitlement to use the additional content.

Also, when adopting an implementation that prevents save data from being loaded if the user does not have the required entitlement, carefully consider the risk that the user may effectively lose their save data.

Refer to TRC [R5116](../../../TRC/latest/TRC/R5116.html) for details.

# Checking Data Read from Save Data

Cheating by tampering with save data is quite common. It is recommended that you perform the following checks on any data read from save data in order to avoid unexpected behavior or game balance being adversely affected.

* Are the parameters that affect gameplay considerably advantageous to the player, and are the values unnatural?
* Are any other data outside expected ranges?

There are no rules for how strict or frequent these checks must be. Applications can perform checks to the extent that is considered appropriate for each application.

# Notes Regarding the Calling-Source Thread

If the following functions of the SaveData library are called immediately after the start of an application's suspension processing, the functions will block the calling-source thread until the suspension completes.

* `sceSaveDataPrepare()`
* `sceSaveDataDelete()`
* `sceSaveDataDirNameSearch()`
* `sceSaveDataDirNameSearch2()`
* `sceSaveDataDirNameSearchPs4()`
* `sceSaveDataSetupSaveDataMemory2()`
* `sceSaveDataGetSaveDataMemory2()`
* `sceSaveDataSetSaveDataMemory2()`

Meanwhile, application suspension will be delayed until `suspendPoint()` is called. Because of this, a deadlock may occur if the above SaveData library functions are called from the application's main thread (calling-source thread of `suspendPoint()`). Make sure to call these functions from a subthread (as defined in TRC [R5089](../../../TRC/latest/TRC/R5089.html)).

Moreover, SaveData library functions basically entail the access of console storage. It is strongly recommended that functions other than the above also be called from subthreads.

# Notes About Loading Save Data on Other Consoles

Save data for PlayStation®5 applications may be loaded on other consoles through the use of cloud storage. The content through which the user played on the original console must be properly loaded even when loading save data on another console. Refer to TRC [R5021](../../../TRC/latest/TRC/R5021.html) for details.

The features described below can be used to test the loading of save data on other consoles.

## USB Drive

With Development Kits/Testing Kits, a USB drive can be used to copy save data to other consoles.

## Cloud Storage and the ★Fake Plus Subscription Status

With Development Kits/Testing Kits, cloud storage can also be used to copy save data to other consoles. Typically, a user must be logged in with an account that has purchased the right to use PlayStation®Plus to use cloud storage. However, accounts that do not have the right to use PlayStation®Plus can use cloud storage when the following setting is turned "On":

"★Debug Settings" > "Multi User" > "User XX" > "PlayStation Network" > "Fake Plus Subscription Status"

Note that save data cannot be individually processed with the cloud storage feature; it is only possible to display a list of applications and upload/download/delete save data at the application level.