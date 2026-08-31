# Title Cloud Storage Service Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS-Overview/feature-overview.html

# Feature Overview

This topic explains basic information that you should understand before using the Title Cloud Storage service.

## Purpose and Characteristics

The Title Cloud Storage (TCS) service of PlayStation™Network provides online storage per title and per user.

Using the Title Cloud Storage service, 64 64-bit signed integers (TCS variables) and binary data (TCS data) of up to 8 MiB per user, plus 2048 64-bit signed integers and binary data of up to 64 MiB per title, can be stored on the server of PlayStation™Network. Settings can also be made for each piece of data to decide whether to grant read/write access privileges to other users.

Except when performing atomic operations, title cloud storage behaves such that it will have eventual consistency. In other words, another user might not be able to refer immediately to information written by a given user, but the former will be able to refer to it eventually.

In addition to simple read and write operations, atomic additions and conditional writes can be performed on a TCS variable. It is also possible to operate on multiple TCS variables belonging to a single user at the same time, as well as to operate on specific TCS variables of multiple users at the same time. You can also handle certain use cases, such as distributing fixed binary data to all users of a given title by using the Title Cloud Storage Management Web API. Note that advanced features, such as ranking, are not provided by this service; therefore, you must use it in conjunction with, for example, the Leaderboards service, as necessary. Various use cases are demonstrated in "[Applied Examples of Title Cloud Storage](applied-examples-of-title-cloud-storage.html)"; refer there for more information.

There is a storage service from the PlayStation®4 generation, Title User Storage service (TUS), but the use of TCS is recommended because of the following benefits:

* Relative to TUS, TCS has a less restrictive limit on large-volume attachment data.
* With TCS, TCS variables and TCS data can be shared between PlayStation®5 versions of games and PlayStation®4 versions of games.

## Main Features

The main features provided by the Title Cloud Storage service are as follows:

* The Title Cloud Storage Web API, primarily used by consoles, etc.
  + Obtaining, updating, deleting, and atomically updating TCS variables
  + Obtaining, updating, deleting, and obtaining the status of TCS data
* The Title Cloud Storage Tool, which is primarily used during development
  + Setting up services
  + Setting up slots
  + Applying settings
  + Setting up snapshot output schedules
* The Title Cloud Storage Management Web API, which is primarily used after production
  + Obtaining, updating, and deleting TCS variables
  + Obtaining, updating, deleting, and obtaining the status of TCS data

## Sample Programs

Sample programs that use the Title Cloud Storage service are provided as follows. Refer to [Sample Program Overview](../../../SDK/latest/Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

**sample\_code/playstation\_network/api\_webapi\_title\_cloud\_storage\_basic**

This sample exemplifies the basic usage of the Title Cloud Storage service.

**sample\_code/playstation\_network/api\_webapi\_title\_cloud\_storage\_data\_distribution**

This sample exemplifies basic usage of the service when distributing common data/variables to all players via title cloud storage.

## Reference Materials

Refer to the following documents for information about the libraries used to develop applications employing the Title Cloud Storage service:

* [NpWebApi2 Library Overview](../../../SDK/latest/NpWebApi2-Overview/__document_toc.html), [NpWebApi2 Library Reference](../../../SDK/latest/NpWebApi2-Reference/__document_toc.html)
* [NpCppWebApi Library Overview](../../../SDK/latest/NpCppWebApi-Overview/__document_toc.html), [NpCppWebApi Library Reference](../../../SDK/latest/NpCppWebApi-Reference/__document_toc.html)

Refer to the following documents for details about the Sandbox network architecture:

* [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html)
* [NP Service Config User's Guide](../../../SDK/latest/NP_Service_Config-Users_Guide/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Title Cloud Storage Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-TCS_WebAPI-ReleaseNotes.html)
* [Release Notes - Title Cloud Storage Tool](../../../SDK/latest/ReleaseNotes/PlayStation_Network-TCS_Tool-ReleaseNotes.html)