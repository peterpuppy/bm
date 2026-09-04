# NpUniversalDataSystem Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Overview/sample-programs.html

# Library Overview

This topic explains basic information that you should understand before using the NpUniversalDataSystem library.

# Purpose and Characteristics

The Universal Data System ("UDS") is a part of the data platform that accumulates in-game events and user actions and standardizes them as UDS model data. This data is used for various cross-title platform features. Refer to the [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) document for an overview of UDS and for information about the platform features that use UDS.

The NpUniversalDataSystem library provides functions for sending various information (events) in an application to the UDS server. Additionally, "np-universal-data-system-codegen", which is a NpUniversalDataSystem code generation tool, is provided to assist the usage of the NpUniversalDataSystem library. Although restricted to events defined in advance, the implementation costs of event processing can be reduced by using this tool. Refer to the "[NpUniversalDataSystem Code Generation Tool](np-universal-data-system-code-generation-tool.html "This topic explains the Host Tool that generates code for executing the creation and posting of events. The functions and structures created using this tool can be embedded in an application to reduce the workload required for implementing event-posting processing..")" chapter for details.

# Main Features

The main features provided by the NpUniversalDataSystem library are as follows:

* Creating events
* Assembling event properties from various data
* Sending events
* Debugging support
  + Obtaining information about the memory and storage in use by the NpUniversalDataSystem library
  + Converting events into strings in a readable format

The main feature provided by np-universal-data-system-codegen is as follows:

* Generation of a source code that creates events and assembles event properties, posts events, and deletes events

# Embedding into a Program

Include np.h in the source program. In addition, before calling any NpUniversalDataSystem library function in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_UNIVERSAL_DATA_SYSTEM) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceNpUniversalDataSystem\_stub\_weak.a.

# Sample Programs

Sample programs that use the NpUniversalDataSystem library are provided as follows. For basic information (directory structure, and so forth) that is common among all the sample programs provided in the SDK, refer to [Sample Program Overview](../Sample-Overview/__document_toc.html).

## sample\_code/playstation\_network/api\_np\_universal\_data\_system

This sample exemplifies basic usage of the NpUniversalDataSystem library. It includes source code generation using np-universal-data-system-codegen and the processing to post events using the created source code.

## sample\_code/playstation\_network/api\_np\_universal\_data\_system\_activity

This sample uses the NpUniversalDataSystem library to perform various processing related to activities (changing the activity availability, starting an activity, ending an activity, and resuming an activity). It includes source code generation using np-universal-data-system-codegen and the processing to post events using the created source code.

## sample\_code/playstation\_network/api\_np\_trophy2

This sample exemplifies basic usage of the NpTrophy2 library. It includes the processing to unlock trophies using the NpUniversalDataSystem library and np-universal-data-system-codegen.

## sample\_code/playstation\_network/api\_np\_universal\_data\_system\_activity\_local\_mode

This sample is based on the api\_np\_universal\_data\_system\_activity sample and is for the Local Mode. It includes UDS configuration using np-universal-data-system-local-tool.

## sample\_code/playstation\_network/api\_np\_trophy2\_local\_mode

This sample is based on the api\_np\_trophy2 sample and is for the Local Mode. It includes trophy configuration using np-universal-data-system-local-tool.

# Reference Materials

Refer to the following document for an overview of the PlayStation™Network functionalities.

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)

Refer to the following documents regarding the Np library, which is commonly required when using the PlayStation™Network functionalities.

* [Np Library Overview](../Np-Overview/__document_toc.html)
* [Np Library Reference](../Np-Reference/__document_toc.html)

Refer to the following document for an overview of UDS and the procedure for UDS-enabled application development.

* [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpUniversalDataSystem Library](../ReleaseNotes/PlayStation_Network-NpUniversalDataSystem-ReleaseNotes.html)