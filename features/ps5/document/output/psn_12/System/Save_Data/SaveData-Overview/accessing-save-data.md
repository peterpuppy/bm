# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/accessing-save-data.html

# Save Data

This topic explains basic mechanisms and methods of operation relating to the management of save data. It covers save data formats and how to access them, transaction processing during updates, size restrictions, support for multiple users, use of the cloud storage feature, database management, and a broad range of other material.

# Save Data Format

The format of save data created using the SaveData library is explained below.

## File Structure

Save Data File Structure

## Save Data Root Directory

This is the root directory for all save data.

## User ID Directory

Save data is managed separately for each user. For details, refer to the "[Multiple User Support](multiple-user-support.html)" section.

## Save Data Title ID Directory

This is the directory where save data for a particular application is stored.

The save data title ID directory will be created with the value of `titleIdForSharing` as the directory name if it has been set; if not, the application's title ID will be used. Refer to the "[Save Data Sharing](save-data-sharing.html)" section for details about `titleIdForSharing`.

## Save Data Directory

This is the directory where files that comprise the save data are stored. This directory is handled as a single save data. It is created using the name specified when creating save data using `sceSaveDataMount3()`. Also refer to `SceSaveDataDirName` in the [SaveData Library Reference](../SaveData-Reference/__document_toc.html) document.

## sce\_sys Directory

This is the directory where the param.sfo file and icon0.png data used by the system are saved.

## param.sfo

This is the file where save data parameters, such as the title name and details, are written.

Although this file is automatically created by the SaveData library, the parameters can be updated later by the application.

## icon0.png

This is the image file used when save data is displayed by the system software. It can be arbitrarily created and updated by the application. For how to create and modify the image file, refer to the "[Setting an Icon](setting-an-icon.html)" section.

# Accessing Save Data

## Access Method

First, use a SaveData library function to mount save data. When the mount succeeds, it will be possible to obtain the pathname to use for accessing the save data. The application can then use this pathname with a standard file input/output function to access data files in the save data directory.

Specifically, mount point names such as "/savedata0", "/savedata1", […] and "/savedata15" can be obtained when mounting. Access the data files in the save data using the pathnames where the subdirectory name and file name are linked to these mount point names.

## Passcode and Fingerprint

A "passcode" must be set at application package creation to prevent another application from accessing save data.

Normally, there is no other need for the application to acknowledge a passcode, but a hash value of the passcode will be required as a "fingerprint" when transferring save data from another application (for example, when save data of a previous title needs to be inherited by the sequel title). For details, refer to the "[Handling Another Title's Save Data](handling-another-titles-save-data.html "This topic describes the methods for the application to load the save data of another title. There are two ways to load the save data of another title: \"save data sharing\" and \"save data transferring\".")" chapter. Also note that a fingerprint may be required in certain situations during development. Refer to the "[Handling of Save Data during Development](handling-of-save-data-during-development.html "This topic describes how to handle save data in the development environment. It provides information on procedures and settings for dealing with various scenarios that a developer might face. With this information, developers can manipulate save data efficiently and safely to test and debug applications.")" chapter.

## Number of Simultaneous Mounts

Up to 16 save data can be mounted at the same time.

## Writing to Save Data

`sceSaveDataPrepare()` must be called to write to save data. `sceSaveDataCommit()` must be called to complete the update of save data. For details, refer to the "[Save Data Update Transaction](save-data-update-transaction.html)" section.

# Save Data Update Transaction

A transaction for updating save data refers to a SaveData library function call and a series of file/directory operations required for updating save data one time. A transaction is started when `sceSaveDataPrepare()` is called and the update of save data is started. A transaction is terminated when `sceSaveDataCommit()` is called and the update of the save data is committed after various processing (such as file creation/overwrite/deletion and directory creation/deletion) is carried out.

Save data cannot be unmounted during a transaction, in other words, without committing the save data update. Content updated during a transaction can be read even before the update is committed.

## Necessity of a Transaction

As a general rule, update of save data must be carried out atomically as a transaction. Otherwise, there is a risk of data contradictions occurring (for example, only being able to update a section of a file or only being able to update one of the paired files) when a save data update is aborted due to the application crashing or because the system power is turned off.

## Transaction Resource

A transaction resource is a buffer cache that is used for transaction processing. Every update for the mounted save data (creation, update, deletion of a file or directory) is first accumulated in the transaction resource and written to console storage when the update is committed. Write speed acceleration can be expected by performing writes to console storage in a batch. Data stored in the transaction resource can also be read at high speed.

Note:

At present, buffer caching for the transaction resource is not supported; however, the transaction resource must be specified to update save data.

## Using the Transaction Resource

Create the transaction resource using `sceSaveDataCreateTransactionResource()`. Specify the created transaction resource when starting a save data update. To update multiple pieces of save data concurrently, the same number of transaction resources or more need to be created. As long as updating is not performed concurrently, that is, if it is after a given instance of completed save data update has been committed with `sceSaveDataCommit()`, the transaction resource that was used can then be used for other save data. The maximum number of transaction resources that can be created is 16 (the same as the maximum number of instances of save data that can be mounted). The transaction resource can be explicitly deleted using `sceSaveDataDeleteTransactionResource()`. A transaction resource will be implicitly deleted when calling `sceSaveDataTerminate()`.

## Transaction Start and Termination

A transaction is started by calling `sceSaveDataPrepare()` targeting mounted save data to start a save data update. The transaction will terminate when the save data update is committed by calling `sceSaveDataCommit()`.

## Transaction Cancellation

If `sceSaveDataCancel()` or `sceSaveDataUmount2()` with `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` specified is called instead of `sceSaveDataCommit()`, all of the save data updates performed during the transaction will be canceled and the transaction will terminate. The save data content will be rolled back to the state before the start of the save data update.

This feature, which cancels save data updates, can only be used for save data that supports the rollback feature explained later in this document. Also refer to "[Save Data Update Cancellation](save-data-update-cancellation.html)".

## Behavior When a Transaction Does Not Terminate Normally

It will be determined that a transaction did not normally terminate when save data is updated after a transaction is started and the application crashes or a system power off occurs before the update can be committed. In such cases, when save data is next mounted, its content will be rolled back to the state it was in immediately before the start of the transaction. For details, refer to the "[Rollback Feature](rollback-feature.html "This topic explains the rollback feature for save data. The rollback feature is an important mechanism for safely protecting save data in the case of an application or system crash, sudden loss of power, or other unexpected circumstances.")" chapter.

## Transaction Effects

The rollback operation eliminates the problem of a series of data writes being interrupted and leading to discrepancies within the contents of the data and to the save data being corrupted.

# Data in Save Data

The application can create almost any subdirectory or data file within the save data directory. Restrictions are as follows. (For other restrictions not mentioned below, such as the maximum length for a pathname, refer to the description of the file system in the [Kernel Overview](../Kernel-Overview/__document_toc.html) document.)

## Characters That Can Be Used

Only ASCII characters can be used for subdirectories and data filenames. Upper-case and lower-case letters are not distinguished.

## System Reserved Filenames

The sce\_sys directory directly below the save data directory is automatically created by the system. There are no other reserved filenames or directory names.

## Program Files

Program files (elf file and prx file) cannot be placed in the save data directory.

# Save Data Size

The save data size is specified by the application upon creating the save data directory. Points to consider when determining the size are explained below.

## Save Data Size Limits

The following upper limits exist for the save data size.

* The maximum size for one piece of save data is 1 GiB
* Multiple instances of save data can be created for a single user, but the maximum total size for save data is 1 GiB per user

Note:

The size of a single piece of save data is restricted by the specifications of the library. Because up to four users can join an application at the same time, the maximum size of save data that can be handled at the same time by one application is a total of 4 GiB. Exceeding 1 GiB per user is prohibited by the requirements in the TRC (Technical Requirements Checklist). Refer to TRC [R5100](../../../TRC/latest/TRC/R5100.html) for details.

## Save Data Size Increase/Decrease

The actual save data entity is an image file (loopback device) of a fixed size. Therefore, once it is created, free space in the save data directory will not decrease even when the console storage is used by other applications or by the system.

By the same token, the application cannot write a file or directory exceeding the size of save data that was set when the save data directory was created. Although it is possible to expand the size after creation, doing so requires dedicated processing; make sure to carefully determine the save data size. Refer to the "[Save Data Conversion](save-data-conversion.html)" section for instructions on how to increase the save data size.

## Metadata Area

The application can create and use arbitrary directories and files in the save data directory, but an area is also required for metadata that is used by the system. Metadata includes a file system management area, icon0.png and param.sfo for display in the system software, temporary files used by the system, etc. The application must determine the save data size in consideration of this metadata area.

For example, when save data is 3 MiB, which is the minimum size of save data that can be created (=`SCE_SAVE_DATA_BLOCK_SIZE2 * SCE_SAVE_DATA_BLOCKS_MIN3`), approximately 2 MiB will be used as the metadata area immediately after creation, and approximately 1 MiB will be free space.

The metadata area increases proportionally to the save data size. This is mainly due to an increase of the file system management area. When the size of a single file written by the application increases or when the number of files to write increases, the metadata will increase accordingly.

The free space always increases according to the size of files deleted by the application, but metadata will not necessarily be deleted. Therefore, there will be cases where the free space of save data will not return to what it was before file creation even if the created file is deleted.

## Benchmark for the Optimal Save Data Size

Given the above, make sure there is sufficient extra space for the save data size when creating save data. As a general benchmark for the save data size, it is recommended to allocate a space that is approximately 10% larger than the total size of all the files saved by the application upon creating the save data.

This measure is required to ensure that free space does not become insufficient even when metadata unexpectedly increases because of repeated file and directory creations/deletions.

However, it is also a problem when there is too much extra space. As noted earlier, the actual save data entity is an image file of a fixed size. Therefore, when the application creates save data with 100 MiB of free space and only 10 MiB is used, for example, the unused 90 MiB will needlessly take up space.

It is important to appropriately determine the size and number of save data according to application specifications. Take various factors into consideration, such as the possibility of changing usage in the future with an update.

## Procedure for Determining the Save Data Size

In order to determine the save data size, it is important to actually run the application and check the amount of free space for the save data. An example of this procedure is as follows.

1. Create a large-sized save data
2. Use `sceSaveDataGetMountInfo()` to obtain the current free space
3. In the save data directory, create the maximum sizes/numbers of files and directories possible given application specifications
4. Use `sceSaveDataGetMountInfo()` to obtain the current free space again, and then determine the difference in free space from step [2](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_5_2) to calculate the total space used in step [3](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_5_3)
5. Calculate a size for save data so that the free space upon save data creation is approximately 10% larger than the total space calculated in step [4](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_5_4).

Actually create save data of the above size and repeat steps [2](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_5_2) through [5](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_5_5). The procedure is complete when the save data size calculated in step [5](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_5_5) is a close match to the size of the created save data.

## Free Space Checking by the System

When creating new save data, the system will deem there to be insufficient free space if there is not free space available from console storage that is at least somewhat larger than the specified save data size. This is due to a check that the system performs based on the amount of console storage that would actually be consumed if the save data were to be created and is normal behavior.

## Handling and Testing Insufficient Free Space

**Insufficient Free Space upon Newly Creating Save Data**

This error must be appropriately handled. Refer to TRC [R5096](../../../TRC/latest/TRC/R5096.html) for details.

Insufficient free space can be intentionally generated during development. Use this feature and check that appropriate processing is carried out when an error for insufficient free space occurs. For the method to generate insufficient free space, refer to the "[Testing Insufficient Free Space](testing-insufficient-free-space.html)" item of the "[Handling of Save Data during Development](handling-of-save-data-during-development.html "This topic describes how to handle save data in the development environment. It provides information on procedures and settings for dealing with various scenarios that a developer might face. With this information, developers can manipulate save data efficiently and safely to test and debug applications.")" chapter.

## System Defined Message Displayed for the Insufficient Free Space Error

The SaveDataDialog library can be used to display an error message regarding insufficient free space in console storage. Call `sceSaveDataDialogOpen()` with the following settings. The system also automatically displays the amount of insufficient free space.

| **Variable** | **Value to Set** |
| --- | --- |
| `SceSaveDataDialogParam.mode` | `SCE_SAVE_DATA_DIALOG_MODE_SYSTEM_MSG` |
| `SceSaveDataDialogParam.dispType` | `SCE_SAVE_DATA_DIALOG_TYPE_SAVE` |
| `SceSaveDataDialogParam.sysMsgParam->sysMsgType` | `SCE_SAVE_DATA_DIALOG_SYSMSG_TYPE_NOSPACE` or `SCE_SAVE_DATA_DIALOG_SYSMSG_TYPE_NOSPACE_CONTINUABLE` |

# Multiple User Support

Save data is managed per user. On PlayStation®5, multiple users can be logged in to one console at the same time, and the application can access save data of each of the logged in users.

## User ID

A user ID is an identifier for identifying users on a single console. A user ID will be assigned when a user is created in the system software menu.

When mounting save data, specify this user ID in addition to various other parameters. It is not possible to specify the user ID of a user that is not currently logged in and mount save data.

The user IDs of currently logged in users can be obtained with a function of the UserService library.

User IDs are local identifiers on each console. The same user will be assigned a different user ID on another console; and even on the same console, when deleting a user and creating a new user, a different user ID will be assigned.

Therefore, it is not possible to determine the owner of save data based on the user ID. Do not embed the user ID in save data to have the application independently determine save data owners.

## Mount Restriction According to Owner Information

"Owner information" is automatically written to save data. Because this owner information is used when save data is copied to another console system to determine if the user is using their own save data or another user's save data, the owner information is based on the account for PlayStation™Network and not the user ID.

There is a restriction for retail units where mounting of save data is not possible unless it can be confirmed from the owner information that the save data belongs to the logged in user. (Importing and uploading save data are also not possible.) Looking at this restriction from the opposite direction, successful mounting will serve as a confirmation that the save data belongs to the user.

It is possible to mount save data belonging to another user on a Development Kit or Testing Kit. Refer to the "[Owner Information on Development Machines](transferring-save-data-between-systems.html#save-data-library-overview_4_1__save-data-library-overview_4_1_1)" item.

# Cloud Storage Feature

Cloud storage for saving save data is provided to users who have purchased the right to use PlayStation®Plus. This cloud storage can be used for moving save data among consoles, as well as for backup purposes.

On the system software screen, the user can display a list of applications and then batch-upload/download/delete save data for a selected application. Save data in console storage can be uploaded to cloud storage from "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Upload or Delete from Console Storage" > "Upload to Cloud Storage".

Save data in cloud storage can be downloaded to console storage from "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Download or Delete from Cloud Storage" > "Download to Console Storage".

Save data in cloud storage can be deleted from "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Download or Delete from Cloud Storage" > "Delete".

Note:

PlayStation®4 application save data can also be uploaded, downloaded, and deleted from cloud storage using the features under "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS4)".

# Save Data Limit

The maximum number of save data that a user can create is defined by `SCE_SAVE_DATA_CREATE_MAX_COUNT`(=`496`), and if the application attempts to create new save data beyond this maximum, an error will occur. However, since TRC [R5100](../../../TRC/latest/TRC/R5100.html) defines the upper limit for the total size of save data per user to be 1 GiB, this maximum is not normally reached. For testing purposes during development, it is possible to create save data that exceeds the maximum number of save data, and a feature is supported that does not cause an error even if the maximum is exceeded. (Refer to "[Save Data Limit Removal](save-data-limit-removal.html)".) However, the maximum number of instances of save data that the system software can handle is `SCE_SAVE_DATA_DIRNAME_MAX_COUNT` (=1024).

# Save Data Database

The system records information relating to save data in a database and uses it for searches and sorting. Normally, there is no need for the application to be aware of the existence of the save data database; however, there may be occasions when the database must be rebuilt, such as when there's a misalignment between the state of save data on console storage and the content of the save data database. For details, refer to the "[Rebuilding the Save Data Database](rebuilding-the-save-data-database.html)" section.