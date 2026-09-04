# Np Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Overview/library-overview.html

# Library Overview

# Purpose and Characteristics

The Np library serves as the base library for applications that use services provided by PlayStation™Network. In addition to functionalities related to user accounts, the Np library provides functionalities required for using other libraries related to PlayStation™Network.

# Main Features

The main features provided by the Np library are as follows.

* Feature to obtain the account IDs, and Online IDs of each user logged in to the console
* Feature to obtain/monitor the service sign-in state
* Feature to check if PlayStation™Network is reachable
* Feature to check callback functions of libraries related to PlayStation™Network

# Resources Used

The Np library consumes one mutex during the time between loading and unloading the PRX. In addition, one thread will be generated upon asynchronous processing request execution. The generated thread name is `SceNpSdkAsyncXXXXXXXX` (`XXXXXXXX` is a hexadecimal request ID), stack of the generated thread will be 32 KiB, and the application can specify the priority and CPU affinity mask.

In addition, some of the functions will request processing from a system process through inter-process communication, therefore there is a possibility that blocking will be performed for long periods depending on the system process load status.

# Embedding into a Program

Include np.h in the source program.

The application does not have to load (unload) the PRX module as this process will be carried out automatically.

Upon building the program, link libSceNpManager\_stub\_weak.a.

# Sample Program

The sample program using the Np library is as follows:

## sample\_code/playstation\_network/api\_np

This sample exemplifies basic usage of the Np library. Included are programs for obtaining sign-in states, account information, and so forth.

# Reference Materials

Refer to the following document for an overview of user management.

* [User Management Overview](../User_Management-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Np Library](../ReleaseNotes/PlayStation_Network-Np-ReleaseNotes.html)