# Title Cloud Storage Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS_Management_WebAPI-Overview/feature-overview.html

# Feature Overview

This topic provides basic information that you should understand before using the Title Cloud Storage Management feature, including the Web API's purpose and characteristics, its main features, and reference information.

## Purpose and Characteristics

The Title Cloud Storage (TCS) Management feature of PlayStation™Network is one of the Management features provided for back office servers. Its main purposes are uploading data for distribution to production environments and correcting/deleting invalid information uploaded to title cloud storage in production environments. For example, the feature can be used to initialize a slot or to update it with an appropriate value in cases such as when game balance is lost as a result of invalid information being uploaded from an invalid companion application.

Note:

Careless use of the TCS Management feature may compromise the user's game experience. Use this feature while following all items shown in "[Notes](notes.html "This topic explains points to note when using the Title Cloud Storage Management Web API.")".

Another purpose of the TCS Management feature is uploading various information to title cloud storage in the development environment and testing application behavior.

## Main Features

The following operations can be performed by back office servers using the Title Cloud Storage Management Web API.

* Obtaining/updating/deleting TCS variables
* Obtaining/updating/deleting TCS data
* Obtaining multiple TCS data statuses

## Reference Materials

Refer to the following document for information about the Title Cloud Storage Service as a whole:

* [Title Cloud Storage Service Overview](../TCS-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Title Cloud Storage Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-TCS_WebAPI-ReleaseNotes.html)