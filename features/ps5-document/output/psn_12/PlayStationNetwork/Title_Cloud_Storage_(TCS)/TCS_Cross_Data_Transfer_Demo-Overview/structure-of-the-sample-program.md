# TCS Cross-Platform Data Sharing Demo Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/TCS_Cross_Data_Transfer_Demo-Overview/structure-of-the-sample-program.html

# Structure of the Sample Program

This chapter describes the structure of the sample program.

# Menu Screen

This is the first screen displayed after launching the demo. The following operations can be performed on this screen:

* Saving (uploading) local data to TCS
* Loading (downloading) data from TCS locally
* Verifying the identity of local data and data on TCS (hash value comparison)
* Obtaining update timestamps for data stored on TCS
* Deleting data stored on TCS

Menu

# Files

The main files and classes of the sample program are described below:

Sample Main Files

| Files | Description |
| --- | --- |
| tcs\_config.cpp | Contains the processing for obtaining the TCS slot number to which various TCS processes are to be performed. |
| webapi\_job\_items.cpp | Contains the job processing that makes Web API calls to access the various features of TCS. The application creates a job and performs processing including uploading data to TCS within that job. |
| tcs\_cross\_data\_transfer\_manager.cpp | Contains the `TcsCrossDataTransferManager` class to facilitate calling the various features of TCS from the application. |
| tcs\_cross\_data\_transfer\_request.cpp | Contains the `TcsCrossDataTransferRequest` class, which calls Web API features via the NpCppWebApi library in order to upload and download data to and from TCS. |

## Main Classes

**TcsCrossDataTransferManager class**

This is a Manager class to facilitate calling the various features of TCS from the application. It contains processing required prior to sending data, processing for generating hash values, etc. It also serves as a wrapper for the `TcsCrossDataTransferRequest` class that makes requests via the NpCppWebApi library.

**TcsCrossDataTransferRequest class**

Calls Web API features via the NpCppWebApi library in order to upload and download data to and from TCS, as well as to delete data on TCS. Reference this class for TCS operations.