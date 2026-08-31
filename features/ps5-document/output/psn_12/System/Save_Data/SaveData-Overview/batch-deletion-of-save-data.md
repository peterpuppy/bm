# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/batch-deletion-of-save-data.html

# Handling of Save Data during Development

This topic describes how to handle save data in the development environment. It provides information on procedures and settings for dealing with various scenarios that a developer might face. With this information, developers can manipulate save data efficiently and safely to test and debug applications.

# Transferring Save Data between Systems

The copy destination directory when copying save data to a USB drive will be `/PS5/SAVEDATA/(account ID directory)`.

If you do not have an account for PlayStation™Network, the USB drive directory for copying is `/PS5/SAVEDATA/0000000000000000`.

If you have an account of PlayStation™Network and "★Debug Settings" > "Game" > "SaveData" > "Fake Owner" is set to "Off", the directory for copying is `/PS5/SAVEDATA/`(directory of account ID of PlayStation™Network). When set to "On", the directory is `/PS5/SAVEDATA/0000000000000000` - the same as when you do not have an account.

## Owner Information on Development Machines

Note:

"Development machine" is used in this document wherever a distinction isn't necessary between the Development Kit and Testing Kit.

In order for development machines to handle the save data of other users without restriction, a debug setting is provided for pretending to be the save data owner. When "★Debug Settings" > "Game" > "SaveData" > "Fake Owner" is set to "On", save data will always be determined as yours regardless of the owner information written in the save data. Additionally, save data that is created or updated with this setting "On" is treated as though it were in a corrupted state when the setting is "Off". Therefore, perform any operations while the setting is "On".

## Keystone File

Save data created from a package-installed application includes a "keystone file" to prevent mounting by third parties. This keystone file is automatically created based on the passcode upon package creation, added to the package and included in save data when it is saved.

However, because there is no keystone file in an application started in debugger mode, the keystone file will also not be included in save data created from such an application.

On development machines, the system checks whether the application keystone file matches the save data keystone file only if a keystone file is included in the save data. For example, because save data saved with a package-installed application on a development machine includes a keystone file, if an application started on a Development Kit in debugger mode for analysis purposes attempts to mount that save data, an error will occur because the keystone files do not match. In such cases, setting the title ID and fingerprint to the Development Kit system will serve as a replacement for the application keystone file, and it will be possible to mount save data that includes a keystone file. For setting the fingerprint, refer to "[Setting a fingerprint to save data on a Development Kit](transferring-save-data-between-systems.html#save-data-library-overview_4_1__save-data-library-overview_4_1_2_1)".

Note:

The fingerprint can be obtained using the pc\_fingerprint command of the Publishing Tools Command Line Version. Refer to the [Publishing Tools Command Line Version User's Guide](../Publishing_Tools_CL-Users_Guide/__document_toc.html) document for details.

To allow an application started in debugger mode to include a keystone file in save data when it saves it, use the Publishing Tools command line version to create a keystone file and place it with the filename "keystone" in the sce\_sys subdirectory of the work directory. For details, refer to the "ks\_create Command" section of the [Publishing Tools Command Line Version User's Guide](../Publishing_Tools_CL-Users_Guide/__document_toc.html) document.

**Setting a fingerprint to save data on a Development Kit**

A fingerprint can be set to save data by setting the Passcode Fingerprint that can be obtained using the pc\_fingerprint command of the Publishing Tools Command Line Version to "★Debug Settings" > "Game" > "SaveData" > "Set Fingerprint".

This will enable an application started in debugger mode to mount save data that was saved by an application started from an installed package. For example, save data created on the Testing Kit can be copied to the Development Kit and mounted to an application started in debugger mode to reproduce/study a bug. (In this case, it is also necessary to set "★Debug Settings" > "Game" > "SaveData" > "Fake Owner" to "On".)

## Development-Specific Mounting Errors

The following error cases are specific to the stage during the development process:

* When save data imported with "★Debug Settings" > "Game" > "SaveData" > "Fake Owner" turned "On" is accessed after switching "Fake Owner" to "Off" (occurs with `sceSaveDataMount3()` and `sceSaveDataTransferringMount()`)

  ```
  TTY log upon error occurrence (one of the following)
  [libSceSaveData] GetResult : ExecResult : 0x809f8052
  [libSceSaveData] GetResult : ExecResult : 0x809f8053
  ```

* When an attempt is made to mount save data that was saved by an application with a different passcode (occurs only with `sceSaveDataMount3()`)

  ```
  TTY log upon error occurrence
  [libSceSaveData] GetResult : ExecResult : 0x809f805d
  ```

* When an application started from the debugger attempts to mount save data (that is, save data including a keystone file) that was saved by an application that was installed from a package without a fingerprint being set (occurs only with `sceSaveDataMount3()`)

  ```
  TTY log upon error occurrence
  [libSceSaveData] GetResult : ExecResult : 0x809f805c
  ```

In these cases, the processing to delete save data described in the "[Automatic Deletion of Corrupted Save Data](automatic-deletion-of-the-corrupted-save-data.html)" section will not be performed, and the mounting function will return `SCE_SAVE_DATA_ERROR_BROKEN` and fail. This behavior is intended to prevent processing to delete save data from being performed and save data from being lost unintentionally when the settings for mounting save data during application development have been configured incorrectly.

In the product version of an application, a corruption error will not usually be returned by `sceSaveDataMount3()`.

# Features Not Supported on Retail Units

The following features under "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" are not supported on retail units.

* A feature to write save data to a USB drive and a feature to read save data from a USB drive
* Features to copy and delete individual save data items shown on lists

  (Can only display the application list)

# Save Data Write Destinations

Save data will be saved to one of the following locations on a Development Kit.

* (a) Save data root directory specified in the file path configuration file
* (b) System-managed area

The save data root directory specified in the file path configuration file will be prioritized over a system-managed area. The directory on the host PC specified to savedataRootDir will serve as the save data root directory, and the SaveData library will write save data in this directory. (See "[Save Data File Structure](save-data-format.html#save-data-library-overview_1_1__600d77c8-8e5a-161a-8c41-d0cb1f870000)".)

Note:

Refer to the [Programming Startup Guide](../Programming-Startup_Guide/__document_toc.html) document for details about the file path configuration file.

## Save Data Root Directory Specified in the File Path Configuration File

A developer will be able to directly view/edit the content of save data as plain text when a directory on the host PC is set as the save data root directory.

This is convenient for verifying the written data and for reading test data.

Note:

The same value as the total size (`blocks`) will be stored in free space (`freeBlocks`) for save data saved to the save data root directory specified with the file path configuration file. For details, see the Notes for `SceSaveDataMountInfo` in the [SaveData Library Reference](../SaveData-Reference/__document_toc.html).

## System-Managed Area

The SaveData library will write to an area managed by the system when the save data root directory is not set in the file path configuration file or when the file path configuration file is not used. Save data written to this area will be encrypted, and file volumes and read and write performance will be almost identical to those of retail units.

Save data in this area can be copied or deleted with software features. (The explanation "[Fake Corrupted Status](fake-corrupted-status.html)" assumes save data is saved to this area.) Note that only the application program can access save data content. Use this area when running the Development Kit as a standalone without an intermediary host PC, or when performing a final check of operations on save data. Only save data written to an area managed by the system can be displayed and managed in "Settings" > "Application Saved Data Management" > "Saved Data in System Storage".

# Fake Corrupted Status

You can set "★Fake Save Data Broken Status" to test the behavior of the application when the save data is corrupted. The procedure for making this setting on the system software is as follows:

1. From "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Upload or Delete from Console Storage", select an item for which a list of save data is displayed, such as "Delete".
2. On the displayed list of save data, align the focus on the save data to set to the corrupted state and press the options button
3. Once the options menu is displayed, select "★Fake Save Data Broken Status" and set to on or off

The following operations can be verified using save data for which the corrupted state has been set.

* Application behavior when corrupted save data has been mounted (refer to the "[Automatic Deletion of Corrupted Save Data](automatic-deletion-of-the-corrupted-save-data.html)" section)
* Application behavior when save data conversion fails due to corrupted save data (refer to the "[Error for Save Data Corruption during Conversion](save-data-conversion.html#save-data-library-overview_6_13__save-data-library-overview_6_13_4)" section)

Note:

Even while the application is running, it is possible to set "★Fake Save Data Broken Status" to save data if it is not mounted.

# Save Data Conversion Performance

You can set "★Set SaveData Convert Performance" to test the application behavior when the conversion of save data takes a long time. The procedure for making this setting on the system software is as follows:

1. From "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Upload or Delete from Console Storage", select an item for which a list of save data is displayed, such as "Delete".
2. On the displayed list of save data, align the focus on the save data to set conversion performance and press the options button.
3. When the option menu appears, select "★Set SaveData Convert Performance" and set Default/Slow.

The meaning of the values that can be set is as follows:

* Default: default performance
* Slow: performance whereby processing takes a long time

For both settings, make sure that the behavior is appropriate; for example, by checking the progress indicator. Refer to the "[Fluctuations in Conversion Performance](save-data-conversion.html#save-data-library-overview_6_13__save-data-library-overview_6_13_1)" section for details about the save data conversion performance.

Note:

You can set "★Set SaveData Convert Performance" even while the application is running.

# Save Data Limit Removal

Save data with no limit on the maximum number of save data per user can only be created in the development environment. For details, see `SceSaveDataMount3` in the [SaveData Library Reference](../SaveData-Reference/__document_toc.html) document. When save data with no limit on the maximum number of save data is created, the following system message will be displayed in TTY.

```
[libSceSaveData] Ignoring the upper limit of savedata per user for this title
```

# Rebuilding the Save Data Database

Save data stored on a host PC can be freely deleted during development on the host PC; however, if deleted, inconsistencies may arise between actual data and the save data database that is managed by the system for accelerating searches (for example). When the system detects inconsistencies between the save data directory and save data database, the following system message will be output to TTY.

```
[libSceSaveData] The saved data database and the saved data do not match.
                   To resolve this problem, set [★Debug Settings] > [Game] > 
                  [SaveData] > [Rebuild Database on Launching Application] to [On].
```

In such cases, set "★Debug Settings" > "Game" > "SaveData" > "Rebuild Database on Launching Application" to "On" as instructed in the message. The save data database will be rebuilt upon application startup. (This item is set to "Off" by default; note that application startup will take longer when this item is set to "On".)

Select "★Debug Settings" > "Game" > "SaveData" > "Rebuild Database" to immediately rebuild the database if save data is saved in a system-managed area.

# Testing Insufficient Free Space

When setting "★Debug Settings" > "Game" > "SaveData" > "Fake Free Space" to "On" ("Off" by default) on a development machine, it is possible to generate a state of insufficient free space upon calling any function that saves save data. At this time, each function will return the error indicated below. This will enable you to test application behavior when free space is insufficient.

Error Returned by Each Function

| **Function** | **Error** |
| --- | --- |
| `sceSaveDataMount3()` | `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` is returned when newly creating save data  (only when save data does not yet exist) |
| `sceSaveDataConvert()` | When converting save data, `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` is returned when `sceSaveDataGetEventResult()` is called |

# Displaying Notifications for Developers

On development machines, notifications for developers concerning save data processing can be displayed by setting "★Debug Settings" > "Game" > "SaveData" > "Debug Notification" to "On" (initially "Off" by default).

Notifications Displayed

| **Content displayed** | **Description** |
| --- | --- |
| SaveData:  The elapsed time after prepare is over 15 seconds  [Save data directory name] | Displayed when save data updates continue for 15 seconds or longer. |
| SaveData:  The elapsed time between prepare and commit is XX seconds [Save data directory name] | Displayed when save data updates which continued for 15 seconds or longer are committed.  XX is the number of seconds elapsed since save data updates began |
| SaveData:  Commit was called without closing file which has already been removed. | Displayed when the save data update indicated in the "[Special Cases in Which Updates of Save Data May Fail](special-cases-in-which-updates-of-save-data-may-fail.html)" section is performed. |

# Displaying Information for Developers

On development machines, information for developers concerning save data can be displayed in certain sections within the "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" menu of the system software. The menu items for each of these pieces of information include the "★" mark and are not displayed on retail units.

## Displaying Information on an Application List Display Screen

Information concerning save data can be checked by performing the operations below.

1. From "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Upload or Delete from Console Storage" in the system software, select an item for which a list of applications is displayed, such as "Delete".
2. Focus on the application icon and press the options button.

Items that can be checked are shown below.

| **Item** | **Description** |
| --- | --- |
| ★Size | Total size of all save data for the application XXXX MB |
| ★Title ID | Title ID of the application  (The title ID set for titleId in the application's param.json) |
| ★Save Data Sharing | Save data title ID for which sharing of save data is allowed  (The title ID set for titleIdForSharing in the application's param.json) |
| ★Save Data Transferring | Save data title ID for which transferring of save data is allowed  (The title ID set for titleIdForTransferring in the application's param.json) |
| ★Save Data Transferring (PS4) | Save data title ID targeted for PlayStation®4 save data transferring  (The title ID set for titleIdForTransferringPs4 in the application's param.json) |

"★Size" has the same value as the size displayed on the application list display screen. TRC [R5100](../../../TRC/latest/TRC/R5100.html) requires that this size not exceed 1 GiB.

## Displaying Information on a Save Data List Display Screen

When "Information" is selected from the options menu displayed upon pressing the options button over a save data icon (displayed for example, after selecting an application icon from "Console Storage" > "Delete"), the following information about the save data on which the focus is placed will be displayed:

| **Item** | **Description** |
| --- | --- |
| Size | Save data capacity information XXXX MB/YYYY MB   * XXXX MB: Capacity used * YYYY MB: Save data size |
| ★Title ID | Save data title ID  (The title ID set for `titleIdForSharing` in the param.json for the application that created the save data, if that value has been set. If it has not been set, then the title ID set for `TITLE_ID`) |
| ★DirName | Save data directory name  (The `dirName` specified when creating the save data using `sceSaveDataMount3()`) |
| ★User ID | User ID and user name of the user who created the save data |
| ★Account ID | Account ID of the user who created the save data |
| ★Faked Owner | Whether the save data has ever been updated with the state of "★Debug Settings" > "Game" > "SaveData" > "Fake Owner" set to "On" (True/False) |
| ★Backup Data | Whether or not backup data exists (Exists/Does Not Exist) |
| ★Rollback | Whether or not the rollback feature is supported (Support/Not Support) |

The string consisting of a 16-digit hexadecimal value displayed for "★Account ID" corresponds to the `(account ID directory)` referred to in the "[Transferring Save Data between Systems](transferring-save-data-between-systems.html)" section.

In order to export save data for which "★Faked Owner" has a value of True from the development machine to a USB drive, "★Debug Settings">"Game">"SaveData">"Fake Owner" must be set to "On".

## Conditions on Displaying Application Information

When application information is displayed using the system software menu item "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)", any application that is not installed on the development machine has "Unknown" displayed as its title name and the system default icon displayed as its thumbnail.

If an application that is sharing save data is installed, that application's title name and icon are displayed.

# Batch Deletion of Save Data

To delete the save data of all users at once on a development machine, select "★Delete" > "★Delete User's All Save Data" or "★Delete" > "★Delete All Users' All Save Data" in the options menu displayed by pressing the options button over an application icon (any icon anywhere on the screen is fine) on the home screen.

"★Delete User's All Save Data" deletes all the save data of the user currently operating the system.

"★Delete All Users' All Save Data" deletes all the save data of all users.

# Command Line Operations of Save Data Using prospero-ctrl

The prospero-ctrl utility (prospero-ctrl.exe), which is a command line tool, can be used to view a list of save data on a development machine, export save data to a host PC, import that save data back to a development machine, and delete it. Because exported save data is encrypted, its content cannot be viewed on a host PC. This feature enables the state of save data on a development machine to be saved as a snapshot on a host PC and enables this state to be reproduced on a development machine. (For the details of how to execute prospero-ctrl and about parameters that are not described below, refer to the [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html) document.)

## Displaying a List of Save Data

```
savedata list [/validate][/target:<target>]
```

All the save data of a user currently logged in on a development machine can be viewed as a list.

If `/validate` is specified, the information regarding whether the save data is corrupted will also be displayed.

## Exporting Save Data

```
savedata export <title ID> <path> [/directory:<save data directory 1> [<save data directory 2> ...]] [/target:<target>]
```

Specify the title ID of the save data to export for `title ID`. All the save data of the user currently logged in on the development machine will be exported to the host PC directory specified in `path`. It is also possible to specify the save data directory you want to export. Exported save data will each have the following file structure. Backup data is exported with "sce\_bu\_" added as a prefix to the save data directory name as in "sce\_bu\_`save data directory`".

```
\--(title Id directory)
 +--(save data directory)        Save data files
```

## Importing Save Data

```
savedata import <path> [/directory:<save data directory 1> [<save data directory 2> ...]] [/target:<target>]
```

For `path`, specify the `title Id directory` host PC directory exported with `savedata export`. All the save data instances in the `title Id directory` are imported by the development machine as save data belonging to the user currently logged in to the development machine. It is also possible to specify the save data directory you want to import. Even if save data is renamed on the host PC, it will be imported with the save data directory name that it had when it was newly created.

## Exporting Plain Text Save Data

```
savedata export-raw <title ID> <path> [/keystone:<keystone file path>] [/fingerprint:<fingerprint>] [/directory:<save data directory 1> [<save data directory 2> ...]] [/target:<target>]
```

Specify the title ID of the save data to export for `title ID`. All the save data of the user currently logged in on the development machine will be exported as plain text to the host PC directory specified in `path`. If the application is not installed on the development machine, the save data with the save data title ID that matches `title ID` will be exported.

Either `/keystone` or `/fingerprint` must be specified for authentication. An error will occur if authentication with the keystone file included in the save data fails. If the save data does not include a keystone file, the specification of `/keystone` and `/fingerprint` can be omitted, but specifying them will not result in an error.

Plain text of save data is exported in save data directory units with the following configuration:

```
\--(title Id directory) Save data title ID directory
 +--(save data directory) Save data directory
  +---sce_sys
   +----param.xml     Parameter file
   +----icon0.png     Icon file
  +--- (protected user data files) Data files
```

System files are exported in param.xml format instead of param.sfo. Refer to "[param.xml Parameter File Format](command-line-operations-of-save-data-using-prospero-ctrl.html#save-data-library-overview_4_13__save-data-library-overview_4_13_6)". Data files in the save data are exported with the same directory configuration.

An error will occur if a non-empty `title Id directory` already exists at the export destination.

You can explicitly specify any number of save data directories to export by specifying `/directory`. In such cases, an error will occur if a non-empty `save data directory` already exists at the export destination.

Backup data is exported with "sce\_bu\_" added as a prefix to the save data directory name as in "sce\_bu\_`save data directory`".

Note:

`export_raw` does not support save data of PlayStation®4. It will be ignored even if it exists.

## Importing Plain Text Save Data

```
savedata import-raw <title ID> <path> [/keystone:<keystone file path>] [/fingerprint:<fingerprint>] [/directory:<save data directory 1> [<save data directory 2> ...]] [/target:<target>]
```

For `path`, specify the `title Id directory` on the host PC where the plain text save data to be imported is located. Refer to "[Exporting Plain Text Save Data](command-line-operations-of-save-data-using-prospero-ctrl.html#save-data-library-overview_4_13__save-data-library-overview_4_13_4)" for the directory configuration. All the save data instances in the `title Id directory` are imported by the development machine as save data belonging to the user currently logged in to the development machine. If the application is not installed on the development machine, the product code specified in *title ID* will be used as the save data title ID.

Either `/keystone` or `/fingerprint` must be specified for authentication. `/fingerprint` cannot be specified if the application with the product code specified in `title ID` is not installed. An error will occur if authentication with the main application or with the save data that already exists on the development machine fails. An error will not occur when authentication is performed with save data that does not include a keystone file.

Imported save data will include the application's keystone file or the keystone file specified with `/keystone`. Only in cases when the application is not installed, the specification of `/keystone` and `/fingerprint` can be omitted and save data without a keystone file can be imported.

You can also explicitly specify any number of save data directories to import by specifying `/directory`. The save data directories that can be specified must have one of the following names; specifying a directory with a different name will result in an error.

* (a) Names supported by `SceSaveDataDirName`
* (b) Save data directory names for save data memory (sce\_sdmemory\*)

In param.xml, save data parameters can be set in the format shown in "[param.xml Parameter File Format](command-line-operations-of-save-data-using-prospero-ctrl.html#save-data-library-overview_4_13__save-data-library-overview_4_13_6)". Default values determined by the system will be used when not placing param.xml or if parameters omitted in param.xml exist.

When not placing icon0.png, the application's default save data icon will be used if the application with the product code specified in `title ID` is installed. If the application is not installed or does not have a default save data icon, no icon will be set for imported save data.

Save data in directories with the name `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY*` (sce\_sdmemory\*) will be imported as save data for the save data memory. In such cases, an error will occur under the following conditions:

* The `blocks` parameter is set in sce\_sys/param.xml.
* Files or directories other than sce\_sys and memory.dat exist directly under the sce\_sdmemory\* directory.
* sce\_sys/icon0.png exists.

Note:

`import_raw` does not support the feature to import save data as save data of PlayStation®4. All data imported with `import_raw` will become save data of PlayStation®5.

## param.xml Parameter File Format

param.xml files exported with `export_raw` include the following save data parameters. Attempting to import a param.xml file with other parameters set using `import_raw` will result in an error.

| **Parameter** | **Description** | **Format** | **import-raw default value** |
| --- | --- | --- | --- |
| `title` | Save data title name | String | Default save data title |
| `subTitle` | Save data subtitle name | String | Empty string |
| `detail` | Save data detailed information | String | Empty string |
| `blocks` | Save data size (number of blocks) | Number | 110% of the total size of all files in the specified directory + the margin for system files |
| `supportRollback` | Whether or not the rollback feature is enabled | true or false | true |
| `mtime` | Date/time of last update | RFC 3339 (ISO 8601) format | Time of the import |
| `userParam` | User parameter | Number | 0 |

An example param.xml is shown below.

```
<param>
  <title>Player ABC profile</title>
  <subTitle>Player Level 16 :  Game progress 27% : Elapsed time 01:45:30</subTitle>
  <detail>Player's Skill: [Level 16] High Jump / Rapid Run / Rocket Punch</detail>
  <blocks>160</blocks>
  <supportRollback>true</supportRollback>
  <mtime>2023-11-14T05:44:54.00Z</mtime>
  <userParam>42</userParam>
</param>
```

## Deleting Save Data

```
savedata delete <title ID> [/directory:<save data directory 1> [<save data directory 2> ...]] [/target:<target>]
```

Specify the title ID of the save data to delete for `title ID`. All of the save data of the specified title ID of the user currently logged in on the development machine will be deleted. It is also possible to explicitly specify an arbitrary number of save data directories to delete.

## Mounting Save Data

```
application mount-data <title ID> [/fingerprint:<fingerprint>] [/target:<target>]
```

Specify the title ID of the application installed on the development machine for `title ID`. The save data of the user currently logged in to the development machine for that application will be mounted. Mounted save data can be read and written directly from the host PC.

Note:

This cannot be performed while in the "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" menu of the system software or while in specific screens that access save data in the options menu.

If there's save data that couldn't be mounted, the mounting of that save data will be skipped and the following will be displayed in the TTY log.

```
[libSceSaveData] mount skip > <dir name> : <reason>
```

One of the following will be displayed in `<reason>`.

* `fingerprint mismatch:`

  Even if the title ID is the same, this save data has been created by an application with a different passcode
* `corrupted(0x809f8052)` or `corrupted(0x809f8053):`

  An attempt was made to mount save data, which was imported to a development machine with "★Debug Settings" > "Game" > "SaveData" > "Fake Owner" set to "On", with "Fake Owner" set to "Off".
* `corrupted(<error code>):`

  The save data is corrupted

# Handling of Save Data During Cloud Streaming

The cloud streaming feature allows you to check game streaming on the development machine. Refer to the PlayStation™Network Cloud Streaming Overview document for more information.

Cloud streaming syncs save data in cloud storage. Refer to "[Cloud Storage and the ★Fake Plus Subscription Status](notes-about-loading-save-data-on-other-consoles.html#save-data-library-overview_2_10__save-data-library-overview_2_10_2)" for more information about cloud storage.

## Synchronization of Save Data with Cloud Streaming

During cloud streaming, the save data is synchronized with the cloud storage at the start and end of cloud streaming.

## How to Use Save Data on Console Storage for Cloud Streaming

If you would like to use save data created or updated on a development machine with cloud streaming for the same application title ID, the save data that exists in console storage can be used by first uploading it to cloud storage from "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Upload or Delete from Console Storage" > "Upload to Cloud Storage".

## How to Use Cloud Streaming Save Data on a Development Machine

Save data created or updated via cloud streaming can be downloaded to console storage from "Settings" > "Saved Data and Game/App Settings" > "Saved Data (PS5)" > "Download or Delete from Cloud Storage" > "Download Save Data to Cloud Storage" once cloud streaming has ended.

## How to Resolve Save Data Synchronization Errors in Cloud Streaming

If save data fails to sync with the cloud storage when cloud streaming starts or ends, this can be resolved by synchronizing save data the next time cloud streaming is started or by using the following feature

* "Settings" > "Saved Data and Game/App Settings" > "Sync Saved Data" > "View Sync Status"
* Check the synchronization status by selecting the notification that is sent when cloud streaming ends

## Features Not Supported by Cloud Streaming

The following features are not supported by cloud streaming:

* Save data transfer feature: This is not available even if you have already saved save data in cloud storage.