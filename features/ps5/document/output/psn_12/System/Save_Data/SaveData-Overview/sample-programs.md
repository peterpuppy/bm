# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/sample-programs.html

# Library Overview

This topic provides an overview of the SaveData library and its main features, how to embed it into a program, sample programs for understanding how to use the library, and reference materials for developers.

# Purpose and Characteristics

The SaveData library is a library for handling save data.

Save data refers to data that indicates gameplay progress, data edited by users, user-specific configuration data (for example, the volume for sound effects, button assignments, and the message display speed), etc.

The content of save data can be arbitrarily defined by the application. However, because the console storage where save data is stored is a resource shared by multiple applications, there are some rules regarding the directory name and file structure, as well as a requirement to save the system file and icon file together with the data file. The SaveData library supports file creation according to these rules. Additionally, the save data memory feature can be used to delegate file access processing to the SaveData library. (Restrictions exist regarding the size and number of data that can be handled.)

The SaveData library does not provide features related to user interfaces, such as a dialog display. Such features are provided by the SaveDataDialog library. For details, refer to [SaveDataDialog Library Overview](../SaveDataDialog-Overview/__document_toc.html) and [SaveDataDialog Library Reference](../SaveDataDialog-Reference/__document_toc.html).

# Main Features

The main features provided by the SaveData library are as follows.

* Creating save data
* Mounting existing save data (obtaining the mount point)
* Unmounting save data
* Deleting save data
* Searching for save data (obtaining lists)
* Obtaining used space/free space
* Setting/obtaining save data titles, detailed information, etc.
* Setting/obtaining save data icons
* Setting up the save data memory and performing reads/writes

# Embedding into a Program

Include save\_data.h in the source program.

Upon building the program, link libSceSaveData\_stub\_weak.a. (The application does not have to load the PRX module for the SaveData library, as this process will be carried out automatically.)

# Sample Programs

Sample programs using the SaveData library are as follows. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

## sample\_code/system/api\_save\_data/api\_save\_data\_basic

This sample saves, loads, searches for, and deletes save data using the SaveData library. Refer to the "[Using the Library](using-the-library.html "This topic explains in detail a series of procedures relating to the management of save data, as well as points that should be noted. That is, it discusses in detail important matters in the processing of save data, beginning with the basic procedures for doing so.")" chapter for details about these features.

## sample\_code/system/api\_save\_data/api\_save\_data\_memory2

This sample performs save data memory reads/writes. It uses `sceSaveDataSetupSaveDataMemory2()`, `sceSaveDataSetSaveDataMemory2()`, and `sceSaveDataGetSaveDataMemory2()`. Refer to the "[Save Data Memory](save-data-memory.html "This topic describes the \"save data memory\" feature, which allows for the efficient management of save data by an application. By reading this topic, you can understand the basic procedures for save data memory, restrictions, and how to use the API.")" chapter for details about the save data memory feature.

## sample\_code/system/api\_save\_data/api\_save\_data\_transferring

This sample loads the content of save data belonging to other applications (for PlayStation®5 and PlayStation®4) using `sceSaveDataTransferringMount()` and `sceSaveDataTransferringMountPs4()`. Refer to the "[Save Data Transferring](save-data-transferring.html)" section for details about the feature for loading save data of other applications.

## sample\_code/system/api\_save\_data/api\_save\_data\_convert

This sample uses the SaveData and SaveDataDialog libraries to convert the format and size of save data. Refer to the "[Save Data Conversion](save-data-conversion.html)" section for details about this conversion feature.

# Reference Material

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - SaveData Library](../ReleaseNotes/System-SaveData-ReleaseNotes.html)