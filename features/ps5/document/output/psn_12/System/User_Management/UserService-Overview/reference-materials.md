# UserService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Overview/reference-materials.html

# Library Overview

This topic describes the purpose and characteristics of the UserService library, its main features, the resources it consumes, embedding it into a program, sample programs that use the UserService library, and reference materials.

# Purpose and Characteristics

The UserService library is a library for obtaining user information and a list of users logged in to the PlayStation®5 system. By using the UserService library, an application can obtain user IDs used for controller operations, audio inputs/outputs, etc.; detect when users log out; obtain user names; and obtain system software settings configured by the user, such as common configuration items (game presets) related to gameplay.

# Main Features

The main features provided by the UserService library are as follows.

* Feature for obtaining a list of logged in users
* Feature for obtaining login/logout events
* Feature for obtaining user information
* Feature for obtaining a user's game presets
* Feature for obtaining settings related to user accessibility

# Resources Used

When the UserService library is initialized, one thread will be generated internally. The thread name is `SceUserServiceEvent`.

The priority of this thread can be specified by the application. By default, the priority is `SCE_KERNEL_PRIO_FIFO_DEFAULT`.

# Embedding into a Program

Include user\_service.h in the source program.

Upon building the program, link libSceUserService\_stub\_weak.a. (The application does not have to load the PRX module for the UserService library, as this process will be carried out automatically.)

# Sample Programs

The sample program using the UserService library is as follows. For basic information (directory structure, and so forth) that is common among all the sample programs provided in the SDK, refer to [Sample Program Overview](../Sample-Overview/__document_toc.html).

## sample\_code/system/api\_user\_service

This program is an example showing the basic usage of the UserService library.

# Reference Materials

For how users are conceptualized in the PlayStation®5 system, refer to the following document.

* [User Management Overview](../User_Management-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - UserService Library](../ReleaseNotes/System-UserService-ReleaseNotes.html)