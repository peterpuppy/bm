# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/save-data-conversion.html

# Rollback Feature

This topic explains the rollback feature for save data. The rollback feature is an important mechanism for safely protecting save data in the case of an application or system crash, sudden loss of power, or other unexpected circumstances.

# Overview of the Rollback Feature

The rollback feature rolls back save data to the state it was in immediately before a save was started in cases in which an application crash, system crash, or loss of power occurs after a save has been started and while the save data is being written.

By specifying `SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS` for `SceSaveDataMount3.systemBlocks` when creating new save data, you can allocate an area of system blocks and create save data that has the rollback feature. It is only possible to allocate system blocks when creating new save data. Note that specifying anything other than `SCE_SAVE_DATA_SYSTEM_BLOCKS_EQUAL_TO_BLOCKS` for `SceSaveDataMount3.systemBlocks` will result in an error.

# Rollback Scheme

Save data is first written to system blocks. The data written to system blocks is treated as temporary data, and once the save data update is complete, the data is transferred in one batch to the new area. This transfer is fast and atomic, conducted by overwriting metadata and changing block allocations. If the save data update is not completed, the temporary data is discarded as-is and the save data content is rolled back to the state it was in immediately before the update was started.

Writing to Save Data: Normal Update
Writing to Save Data: Rollback

# Save Data Update Cancellation

A feature for the application to explicitly cancel the update of save data that has been started is also supported using the rollback mechanism. To give a specific example, the save data content is returned to the state immediately before the start of the update by discarding the temporary data written in the system block and the metadata managed in the memory during the save data update.

You can enable save data update cancellation by specifying `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` when calling `sceSaveDataPrepare()` and initiating a save data update. The application can cancel the save data update by calling `sceSaveDataCancel()` or `sceSaveDataUmount2()` with `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` specified, instead of calling `sceSaveDataCommit()`.

# Save Data Size and Space

The size of system blocks added to save data will be the same as the value specified for `SceSaveDataMount3.blocks`. For this reason, the size of the save data in console storage will be double the size that was specified for `SceSaveDataMount3.blocks`. System blocks comprise a dedicated area used by the system for the rollback feature. The space available to games for save data is the size specified in `SceSaveDataMount3.blocks` when new save data is created. Note that the save data size displayed to users on the system software screen does not include the size of system blocks.

Note:

The save data size and total size stipulated in TRC [R5100](../../../TRC/latest/TRC/R5100.html) are applied to space for save data that doesn't include the system blocks.

# Corruption of Save Data

Although very rarely, mounting may fail because information in the console storage has become physically corrupted. If you want to test this behavior in a development environment, use the debug features explained in "[Fake Corrupted Status](fake-corrupted-status.html)".

# Special Cases in Which Updates of Save Data May Fail

If a file inside save data is opened and that file is deleted before being closed after starting to update save data using `sceSaveDataPrepare()`, `sceSaveDataCommit()` will return `SCE_SAVE_DATA_ERROR_BUSY`, and the update will fail, until the file is closed.

You can use the feature indicated in the "[Displaying Notifications for Developers](displaying-notifications-for-developers.html)" section to determine if this special case has occurred.

# Behavior When Save Data Is Created on a Host PC

When save data is created on a host PC using a file path configuration file on a Development Kit, the rollback feature does not function. If the update is interrupted, the save data will be corrupted.

To avoid losing save data on a host PC due to corruption, make a copy of the save data on the host PC outside of the game, or use the "★Ignore Broken Status" setting.

In addition, because the rollback feature does not function when save data is created on the host PC, the feature to cancel the update of save data will also not function. When save data is created on the host PC and `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` is specified for `sceSaveDataPrepare()`, the `SCE_SAVE_DATA_ERROR_PARAMETER` error will occur and the following will be shown in the TTY log.

```
[libSceSaveData] Cancel operation is not supported on HostPC. dirName=<dirName>
```

Therefore, when save data is created on the host PC, the behavior of the application to cancel the update of save data cannot be debugged. However, debug features for normal operation checks are provided. An update of save data can be started without `sceSaveDataPrepare()` returning an error by specifying `SCE_SAVE_DATA_PREPARE_MODE_ENABLE_CANCEL` and `SCE_SAVE_DATA_PREPARE_MODE_DEBUG_IGNORE_CANCEL_ON_HOST` in combination when calling `sceSaveDataPrepare()`. The following will be shown in the TTY log.

```
[libSceSaveData] Ignored enabling cancel operation on HostPC. dirName=<dirName>
```

If either `sceSaveDataCancel()` or `sceSaveDataUmount2()` with `SCE_SAVE_DATA_UMOUNT_MODE_CANCEL` specified is called in this state, the save data update will be committed - as is the case when calling `sceSaveDataCommit()` or when calling `sceSaveDataUmount2()` with `SCE_SAVE_DATA_UMOUNT_MODE_COMMIT` specified - instead of being canceled, and the following message will be displayed in the TTY log.

```
[libSceSaveData] Cancel operation is not supported on HostPC. dirName=<dirName>
```

If save data is created in a system-managed area, the specification of `SCE_SAVE_DATA_PREPARE_MODE_DEBUG_IGNORE_CANCEL_ON_HOST` will be ignored.

# Save Data Conversion

You can use `sceSaveDataConvert()` to increase the size of save data. Some things to keep in mind when converting save data are described below.

Note:

Also refer to the sample program below for the conversion processing of save data. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

* sample\_code/system/api\_save\_data/api\_save\_data\_convert

## Fluctuations in Conversion Performance

The amount of time it takes to convert save data varies depending on the state and size of the save data being converted. If the conversion process takes a long time, we recommend taking the following measures:

* You can set "★Set SaveData Convert Performance" to confirm that the application does not malfunction when the conversion process takes a long time.
* Use `sceSaveDataGetConvertProgress()` during the conversion process to obtain the progress rate and display it on the screen.

## Effect of Conversion Processing on SSD Write Throttling

Writes by `sceSaveDataConvert()` are performed using the system's I/O resources and do not consume the resources allocated for SSD write throttling. Converting multiple large save data in succession does not affect SSD write throttling bandwidth limits.

## Error for Insufficient Free Space in Console Storage during Conversion

If there is not enough free space in the console storage, the save data conversion will fail with the `SCE_SAVE_DATA_ERROR_NO_SPACE_FS` error. TRC [R5096](../../../TRC/latest/TRC/R5096.html) does not apply to this error. If you want to display a system defined message for the insufficient console storage free space error, refer to "[System Defined Message Displayed for the Insufficient Free Space Error](save-data-size.html#save-data-library-overview_1_5__section_eqr_qkk_ndc)".

You can use the "Fake Free Space" feature to check operation when the insufficient free space error occurs. For details, refer to the "[Testing Insufficient Free Space](testing-insufficient-free-space.html)" section.

## Error for Save Data Corruption during Conversion

If the save data targeted for conversion is corrupted, the conversion operation will fail with the `SCE_SAVE_DATA_ERROR_BROKEN` error.

Operation in the case of the save data corruption error can be checked using the "★Fake Save Data Broken Status" feature. For details, refer to the "[Fake Corrupted Status](fake-corrupted-status.html)" section. Also refer to the section "[Corruption of Save Data](corruption-of-save-data.html)".

## Maximum Number of Instances of Save Data That Can Be Mounted Simultaneously during Conversion

Typically, the maximum number of save data instances that an application can mount simultaneously is `SCE_SAVE_DATA_MOUNT_MAX_COUNT` (=16); however, during the conversion process it is limited to `SCE_SAVE_DATA_MOUNT_MAX_COUNT_WITH_CONVERSION` (=14). That is, if 15 or more instances of save data are mounted at the time of the `sceSaveDataConvert()` call, the save data conversion will fail with the `SCE_SAVE_DATA_ERROR_MOUNT_FULL` error.

## Renaming Converted Save Data

You can rename save data during save data conversion. This can be done to differentiate save data using the directory name or when you want to prevent the save data from being visible to older versions of the application. Specify the name of the directory for the converted save data in `SceSaveDataConvert->dstDirName` and call `sceSaveDataConvert()`.

## Conversion of Save Data of the Save Data Memory

Save data conversion cannot be conducted on save data that is in save data memory. If you try to convert save data (sce\_sdmemory\*) in the save data memory, the conversion fails with the `SCE_SAVE_DATA_ERROR_PARAMETER` error.