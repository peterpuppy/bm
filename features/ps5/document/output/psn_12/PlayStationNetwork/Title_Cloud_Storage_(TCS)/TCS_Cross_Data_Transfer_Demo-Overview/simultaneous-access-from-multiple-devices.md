# TCS Cross-Platform Data Sharing Demo Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/TCS_Cross_Data_Transfer_Demo-Overview/simultaneous-access-from-multiple-devices.html

# Notes

This chapter provides notes about the sample program.

# Simultaneous Access from Multiple Devices

## Uploads

To avoid conflicts between uploads from multiple devices, the overwrite-target TCS data is identified by the update date/time or the slot state when an upload starts. When the upload from a device completes, an error is returned if the update date/time or the slot data of the TCS data has changed since the start of the upload, thereby ensuring atomicity.

## Downloads

Once a download is started, the source data is retained until the download is complete and is not affected by any updates to the data on TCS during this time.

## Deletions

When a deletion is executed for a slot, the processing to check for the existence or lack of uploaded data will be carried out. An error will be returned if data has never been uploaded or if data has already been deleted.

## Details About the Behavior of Simultaneous Uploads

The following is a description of the behavior when simultaneously uploading data from both PlayStation®4 and PlayStation®5 devices.

Prerequisites:

* The same account for PlayStation™Network is used to log in on Console A and Console B (the same account for PlayStation™Network can be used to log in on PlayStation®4 and PlayStation®5)
* Using the PlayStation®4 Cross-Generation SDK, PlayStation®4 titles can access the same TCS as PlayStation®5 titles
* Operation of Console A is performed first, and operation of Console B is performed while processing on the TCS-side is still incomplete

Behavior of Simultaneous Uploads

When Console B uploads data while Console A is in the middle of uploading data

|  |  |  |
| --- | --- | --- |
| **Upload from Console A** | Succeeds | |
| **Upload from Console B** | Fails | |
| **TCS data after both the processing of A and B have completed** | Data from Console A | |