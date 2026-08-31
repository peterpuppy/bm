# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/updating-the-title-name-subtitle-name-and-detailed-informati.html

# Save Data Memory

This topic describes the "save data memory" feature, which allows for the efficient management of save data by an application. By reading this topic, you can understand the basic procedures for save data memory, restrictions, and how to use the API.

# About Save Data Memory

The save data memory feature is provided for applications to handle save data more easily.

In order for the application to use save data memory, a memory area that is shared between the application and the system must first be set up. The application reads/writes data from/to this memory area using dedicated functions. The system will save the contents of the memory area to console storage in the form of save data when appropriate.

If save data for the save data memory already exists upon setting up the memory area, the system will automatically read the data from that save data and write it to the memory area. Through this scheme, even after ending the game once, the application will be able to resume game progress based on this data.

When setting up the memory area, a total of four instances of save data memory can be used by using identifiers known as slot IDs, with slot IDs in the range from 0 to 3 assigned on a per-user basis. This is the basic usage procedure of the save data memory. Because the system manipulates save data in place of the application, the application only needs to be aware of simple operations such as reading and writing save data memory and saving save data to storage.

# Memory Area Details

Details of the memory area that is shared between the application and the system for a single slot are as follows.

Memory Area Details for the Save Data Memory

## Memory Area Allocation

Depending on the size of the save data memory, a shared memory area is either allocated from memory managed by the system or from memory managed by the application.

If the total size of the save data memory data sections for all users and all slots is 4 MiB or less, the required memory area will be allocated entirely from system memory. In such cases, the application's memory will not be used.

If the sum of the data sections exceeds 4 MiB, the SaveData library will attempt to allocate a memory area from the memory of the application. (At this time, the entire memory area, including the parameter section, will be allocated from application memory. Note that it will not be only the data sections.)

The following exemplifies the change in memory area allocation.

1. Allocating save data memory (data section of 1.5 MiB) for Slot 0 of User 1:

   Memory of the system is used
2. Allocating save data memory (data section of 1.5 MiB) for Slot 0 of User 2:

   Memory of the system is used
3. Allocating save data memory (data section of 1.5 MiB) for Slot 0 of User 3:

   Because the total amount of system memory exceeds 4 MiB, memory of the application will be used (note: it is not possible for a single save data memory to use memory allocated both from system memory and from memory of the application)
4. Allocating save data memory (data section of 1.0 MiB) for Slot 0 of User 4:

   Because the size fits in the 4 MiB of system memory, system memory will be used.

# Save Data Memory Restrictions

## Quantity Restriction

The application accesses save data memory through the memory area shared with the system; this memory area is limited to four instances (four slots) per user of the application. Therefore, save data for the save data memory is also limited to four instances per user.

Additionally, the number of memory areas that can be simultaneously set up is limited to four. In other words, if User 1 and User 2 each set up two slots of save data memory, then neither additional users User 3 and User 4, nor User 1 and User 2, themselves, can set up any more save data memory. If you want to allow users to start over and set up save data memory slots allocated among themselves differently, you must first call `sceSaveDataTerminate()`to terminate the library.

## Data Size Restriction

The data section size is limited to a maximum of 32 MiB per application. This does not vary by the number of users. The maximum size for standard save data is 1 GiB per user; save data memory is comparatively much smaller and cannot handle large data.

# Format of Save Data for the Save Data Memory

The format of save data for the save data memory is a simplified version of standard save data as shown below.

Note:

Normally, the application will not directly access save data when the save data memory feature is used, and there is no need to be aware of the save data format. The following explanation is provided for reference purposes only.

## File Structure

File Structure of Save Data Created by the Save Data Memory Feature

## Save Data Directory

Save data directories will be created with the following names, based on the slot IDs in the range from 0 to 3 for the save data memory that is set up:

| **Slot ID** | **Directory name** | **SaveData library macro name** |
| --- | --- | --- |
| 0 | sce\_sdmemory | `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY`, or  `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_0` |
| 1 | sce\_sdmemory1 | `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_1` |
| 2 | sce\_sdmemory2 | `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_2` |
| 3 | sce\_sdmemory3 | `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_3` |

## memory.dat

This is the file onto which content of the save data memory is reflected. Content written by the application to the memory area will be saved as-is. (If double buffering is performed as shown later in the document, only valid buffers will be saved.)

The filename is defined as `SCE_SAVE_DATA_FILENAME_SAVE_DATA_MEMORY`.

## param.sfo

This file contains the parameters such as the title name and data content details for the system to display save data. This file is automatically created by the SaveData library when the save data memory is set up.

Each parameter is the same as in standard save data. (Refer to the [Content Information Specifications](../Content_Information-Specifications/__document_toc.html) document for details.)

## Viewing Save Data for the Save Data Memory

Normal save data is displayed in an application by the SaveDataDialog library; however, the SaveDataDialog library doesn't support the display of save data in the save data memory. The feature to display a list of save data isn't supported by the save data management screen on retail units. This means that users can't view save data that is in save data memory. Limited to on Development Kits and Testing Kits, save data in save data memory is displayed on the save data management screen.

## Saving Icons to Save Data Memory

Unlike the save data memory feature of the PlayStation®4 SDK, the ability to save icons to save data memory is not supported on PlayStation®5. To save an icon to save data memory, it must be saved in a data section as binary data.

## Size of Save Data for the Save Data Memory

The size of save data for the save data memory is determined according to the data size of the save data memory as follows.

| **Data size of the save data memory** | **Size of save data for the save data memory** |
| --- | --- |
| 1 MiB or less | 3 MiB |
| Greater than 1 MiB but not exceeding 8 MiB | 10 MiB |
| Greater than 8 MiB | Value obtained by calculating "[data size x 1.1] + 2 MiB" then rounding up to the nearest block size (64 KiB) |

The difference in data size and save data size is due to the same reasons as for standard save data. For details, refer to "[Metadata Area](save-data-size.html#save-data-library-overview_1_5__save-data-library-overview_1_5_3)" in the "[Save Data Size](save-data-size.html)" section of the "[Save Data](save-data.html "This topic explains basic mechanisms and methods of operation relating to the management of save data. It covers save data formats and how to access them, transaction processing during updates, size restrictions, support for multiple users, use of the cloud storage feature, database management, and a broad range of other material.")" chapter.

# Procedure for Using the Save Data Memory

This section explains the procedure for using the save data memory. An outline of the process flow is as follows.

1. **[Initialize the library](procedure-for-using-the-save-data-memory.html#save-data-library-overview_5_5__save-data-library-overview_5_5_1)**
2. **[Set up the save data memory](procedure-for-using-the-save-data-memory.html#save-data-library-overview_5_5__save-data-library-overview_5_5_2)**
3. **[Read/write memory area in the save data memory](procedure-for-using-the-save-data-memory.html#save-data-library-overview_5_5__save-data-library-overview_5_5_3)**
4. **[Save data for the save data memory is created/overwritten by the system](procedure-for-using-the-save-data-memory.html#save-data-library-overview_5_5__save-data-library-overview_5_5_4)**
5. **[Terminate the library](procedure-for-using-the-save-data-memory.html#save-data-library-overview_5_5__save-data-library-overview_5_5_5)**

The details of each step are as follows.

1. **Initialize the library**

   Call `sceSaveDataInitialize3()` to initialize the library. `SCE_OK` (=0) will be returned when initialization is successful.
2. **Set up the save data memory**

   Call `sceSaveDataSetupSaveDataMemory2()` to set up the save data memory. For the input argument, specify the user ID, size of the save data memory, options such as double buffering, the title name to set when the new save data memory is created, etc., using an `SceSaveDataMemorySetup2` structure.

   In this function, a memory area of the specified size is allocated from flexible memory. Next, the console storage is checked to see whether save data for the save data memory already exists. If it exists, the save data will be mounted and its data content will be loaded and copied to the memory area. If save data does not exist, the data section of the memory area will be zero-cleared; the rest of the memory area will be filled with the parameters specified for creating new save data memory.

   If save data for the save data memory is corrupted, the content that will be read will be determined after the processing described in "[Automatic Deletion of Corrupted Save Data](automatic-deletion-of-the-corrupted-save-data.html)" is carried out.

   Since `sceSaveDataSetupSaveDataMemory2()` accesses save data files, it may perform blocking for a long period; make sure to call it from a subthread.

   Unlike when newly creating standard save data, free space on the console storage will not become insufficient when setting up save data memory; there is no need to handle the possibility of insufficient free space on the console storage.

   Save data memory that has been set up will be saved to save data when its user logs out, and it will be in the uninitialized state. It will be necessary to set up the save data memory again when the user subsequently logs in.
3. **Read/write memory area in the save data memory**

   Call `sceSaveDataGetSaveDataMemory2()` to read data from a memory area in the save data memory, and call `sceSaveDataSetSaveDataMemory2()` to write data to a memory area in the save data memory.

   Note:

   `sceSaveDataGetSaveDataMemory2()` returns a copy of the memory area. Even if the content of that memory area copy is updated, it will not be reflected to the actual memory area.

   `sceSaveDataSetSaveDataMemory2()` must be called to update the memory area.
4. **Save data for the save data memory is created/overwritten by the system**

   The system will create and overwrite save data for the save data memory at the timings described below. `sceSaveDataSyncSaveDataMemory()`, which explicitly initiates a save, is also provided for use. Note the save processing of the save data memory is handled as game I/O and is targeted for SSD write throttling.

   For details about save timings, refer to the "[Save Timing of Save Data Memory](timing-to-save-save-data-memory.html)" section.
5. **Terminate the library**

   Normally, there is no need to terminate this library; however, when ending the application process once (for example), call `sceSaveDataTerminate()` to perform termination processing.

# API Summary

The functions used in basic processing of the save data memory are shown as follows.

Functions Used in Basic Processing of the Save Data Memory

| **Function** | **Description** |
| --- | --- |
| `sceSaveDataInitialize3()` | Function that initializes the library |
| `sceSaveDataSetupSaveDataMemory2()` | Setup function for the save data memory |
| `sceSaveDataSetSaveDataMemory2()` | Function that sets the data of save data memory |
| `sceSaveDataGetSaveDataMemory2()` | Function that obtains the data, title name, etc., of save data memory |
| `sceSaveDataSyncSaveDataMemory()` | Function that explicitly saves the save data memory |
| `sceSaveDataTerminate()` | Function that terminates the library |

# Updating the Title Name, Subtitle Name, and Detailed Information

The title name, subtitle name, and detailed information can be specified when setting data to save data memory with `sceSaveDataSetSaveDataMemory2()`. Use this function, for example, when you want to overwrite such information according to gameplay progress.

Note:

To update the above information, `SCE_SAVE_DATA_MEMORY_OPTION_SET_PARAM` must be specified as an option to `sceSaveDataSetupSaveDataMemory2()` upon setting up the save data memory.

# Save Timing of Save Data Memory

The timings at which save data memory content is saved to save data are as follows.

* When the user terminates or suspends the application
* When the user logs out
* When the application crashes

  Note: content will not be saved if a crash occurs while accessing save data memory with `sceSaveDataSetSaveDataMemory2()` or `sceSaveDataGetSaveDataMemory2()`. However, the immediately preceding data will be saved if the double buffer option is specified.
* When the application calls `sceSaveDataSyncSaveDataMemory()`
* When the application calls `sceSystemServiceLoadExec()`
* When the application calls `sceSaveDataTerminate()`
* When the application started by a debugger terminates normally or is forced to terminate (during development)

In the event of a system crash or power loss, the contents of the save data memory are not stored in the save data. For this reason, it is recommended that your application call `sceSaveDataSyncSaveDataMemory()` on a regular basis, or at an arbitrary timing. When determining the call timing, take into consideration the bandwidth limitations of SSD write throttling.

# Automatic Deletion of Save Data Memory

If save data for the save data memory is corrupted, it will be deleted as follows.

1. The system mounts the target save data when the application calls `sceSaveDataSetupSaveDataMemory2()`.
2. If the save data is corrupted, it will be automatically deleted. For the conditions by which save data will be deleted, refer to "[Automatic Deletion of Corrupted Save Data](automatic-deletion-of-the-corrupted-save-data.html)".
3. The system loads the content of the newly created save data on memory and subsequently returns processing to the application.

# Double Buffering of Data

Even if it is for an extremely short period, if the application stalls while the save data memory is being updated, the system will consider the update of that data to be incomplete and not save it to save data. If the content of the save data memory is not saved to save data for a long time, the data that the user will load next from the save data memory will be an old version. The damage entailed whenever the system is unable to save the save data memory to save data can be lessened by double buffering data.

When you have double buffering be performed, the system writes data with `sceSaveDataSetSaveDataMemory2()` to both buffers in the double-buffered memory area, alternating between the two. By doing so, you can ensure that data that was successfully written to the immediately preceding buffer will be saved as save data even if the application stalls while updating data.

The [figure below](double-buffering-of-data.html#save-data-library-overview_5_10__0_mon_1529931995) shows a comparison of what happens when double buffering is and is not performed.

Operation Comparison When Save Data Memory Double Buffering Is Enabled and When It Is Disabled

To perform double buffering, specify `SCE_SAVE_DATA_MEMORY_OPTION_DOUBLE_BUFFER` to the argument of the `sceSaveDataSetupSaveDataMemory2()` setup function. At this time, memory that is twice the size of the value specified for the size of the save data memory's data sections will be requested.

It is also possible to rewrite a part of the double buffered save data memory with `sceSaveDataSetSaveDataMemory2()` by specifying an offset or memory size; however, given the characteristics of double buffering, data must first be copied from the previously rewritten buffer to the buffer for the current rewrite, and processing will take slightly longer than when the entire buffer area is rewritten.

# Memory Area Release Timings

A memory area allocated for the save data memory will be released at the following timings.

* When `sceSaveDataSetupSaveDataMemory2()` is called

  Setup processing will be performed after the memory area of already logged-out users is released. (Note that memory areas are not released immediately when users log out.)
* When `sceSaveDataTerminate()` is called

  Normally, there is no need to call this function; however, if you want to free resources (for example), call this function to release the memory of all users.

# Usage with Standard Save Data

Save data memory can be used together with standard save data.

However, the system handles standard save data differently from save data for the save data memory. Standard save data cannot be accessed using functions for the save data memory. It is also not possible to access save data for the save data memory using functions for standard save data.

# Sharing and Transferring Save Data

Save data for the save data memory can also be shared/transferred if the preparatory steps in "Sharing and Transferring Save Data" are taken.

## Sharing Save Data

Load and access save data for the save data memory of another title using `sceSaveDataSetupSaveDataMemory2()`.

## Transferring Save Data

The following procedure can be used to transfer save data for the save data memory of another title.

1. Set up the current title's save data memory with `sceSaveDataSetupSaveDataMemory2()`
2. Specify the save data title ID of the transfer source application and the `SCE_SAVE_DATA_DIRNAME_SAVE_DATA_MEMORY_SLOT_*` directory name, and call `sceSaveDataTransferringMount()` to mount save data for the save data memory in the read-only mode
3. Load data required for the transfer from `SCE_SAVE_DATA_FILENAME_SAVE_DATA_MEMORY` (memory.dat) in the save data
4. Write the read content to the current title's save data memory

## API Summary

The functions used for save data memory sharing and transferring are shown as follows.

Functions Used for Save Data Memory Sharing

| **Function** | **Description** |
| --- | --- |
| `sceSaveDataInitialize3()` | Function that initializes the library |
| `sceSaveDataSetupSaveDataMemory2()` | Setup function for the save data memory |
| `sceSaveDataTransferringMount()` | Function that mounts the transfer-target save data directory |