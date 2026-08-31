# SaveData Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SaveData-Overview/preparing-another-titles-save-data.html

# Handling Another Title's Save Data

This topic describes the methods for the application to load the save data of another title. There are two ways to load the save data of another title: "save data sharing" and "save data transferring".

# Save Data Sharing

Save data sharing is a method where multiple applications share and read/write the same save data. All applications that share save data can read/write the save data, and this can be used in situations - for example - where it is desired to read/write common save data between a limited edition and a regular edition or between versions with different language support.

## Implementation Details

Set the same save data title ID to param.json of applications sharing the save data as follows. Only one save data title ID can be set; it can't be added or changed at a later time using an update package. This setting can be skipped for an application whose save data title ID is the same as its title ID.

```
"savedata" : {
   "titleIdForSharing" : "ABCD00000" 
 }
```

Additionally, the same passcode must be set when generating packages for those applications.

## Notes

Particular care must be taken regarding save data compatibility. In order for save data to be freely read/written between applications, make sure that data saved by one application can be properly read and interpreted by another application. In addition, only one save data title ID can be specified for sharing save data. There is no method for sharing save data using multiple title IDs.

# Save Data Transferring

Save data transferring is a method to access save data of another application (or other applications) with read-only access. This can be used for implementing one-way compatibility - for example, when a sequel in a video game series is able to load the save data of a previous title in the series.

## Implementation Details

When mounting the save data of another application, specify the title ID and the fingerprint of the source application for the `titleId` member and `fingerprint` member, respectively, in the `SceSaveDataTransferringMount` structure and call `sceSaveDataTransferringMount()`.

Set the save data title ID of the transfer source application to param.json of all applications sharing the save data as follows.

```
"savedata" : {
   "titleIdForTransferring" : [ "ABCD12345", "ABCD12346", "ABCD12347", "ABCD12348" ] 
 }
```

Unlike save data sharing, up to 32 save data title IDs can be set. An error will be displayed when the package file is installed and "★Check" is performed if 33 or more save data title IDs are set.

Note:

The fingerprint can be obtained using the pc\_fingerprint command of the Publishing Tools Command Line Version. Refer to the [Publishing Tools Command Line Version User's Guide](../Publishing_Tools_CL-Users_Guide/__document_toc.html) document for details.

# PlayStation®4 Save Data Transferring

Applications for PlayStation®5 can access save data created by applications for PlayStation®4 on a read-only basis. For example, this can be used for transferring PlayStation®4 save data to a sequel or a PlayStation®5 version of a game. The access-target PlayStation®4 save data must be stored on the PlayStation®5.

## Implementation Details

When mounting the PlayStation®4 save data, set the `SceSaveDataTransferringMount` structure's `titleId` and `fingerprint` members to the title ID and fingerprint of the source PlayStation®4 application, respectively, and call `sceSaveDataTransferringMountPs4()`.

Set the save data title IDs of the transfer-source PlayStation®4 applications in the PlayStation®5 application's param.json file as follows.

```
"savedata" : {
   "titleIdForTransferringPs4" : [ "ABCD12345", "ABCD12346", "ABCD12347", "ABCD12348" ] 
 }
```

Up to 32 PlayStation®4 application save data title IDs can be set.

PlayStation®4 save data stored on PlayStation®5 can be searched for by calling `sceSaveDataDirNameSearchPs4()`.

PlayStation®4 save data mounted using `sceSaveDataTransferringMountPs4()`, can, as with PlayStation®5 save data, be accessed using the following functions:

* `sceSaveDataUmount2()`
* `sceSaveDataGetMountInfo()`
* `sceSaveDataGetParam()`
* `sceSaveDataLoadIcon()`

# Notes on Handling Save Data from Other Titles

When reading save data from applications that are not your own title, it is strongly recommended to check for data tampering. For details, refer to the "[Checking Data Read from Save Data](checking-data-read-from-save-data.html)" section.

# Preparing Another Title's Save Data

Methods for storing save data of another title (including a PlayStation®4 application) on the PlayStation®5 are as follows.

* Play the target title on PlayStation®5 and create save data
* Download save data from cloud storage

  Refer to the "[Cloud Storage Feature](cloud-storage-feature.html)" chapter.
* Copy save data using a USB drive

  If the target title is a PlayStation®5 application, both the copy source and destination must be a Development Kit or Testing Kit.