# NpWebApi2 Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Overview/library-overview.html

# Library Overview

# Purpose and Characteristics

The NpWebApi2 library is a library required for calling PlayStation™Network Web APIs (which may be referred to simply as "Web APIs" below) from PlayStation®5. Normally, procedures such as obtaining the token and determining the base URL are required for executing PlayStation™Network Web APIs, but since many of these processes are internally performed with this library, applications can easily execute Web APIs by using this library. In addition, the NpWebApi2 library provides an interface for receiving Push events.

# Main Features

The main features provided by the NpWebApi2 library are as follows.

* Feature for calling arbitrary PlayStation™Network Web APIs
* Feature for receiving Push events

# Embedding into a Program

Include np.h in the source program.

Upon building the program, link libSceNpWebApi2\_stub\_weak.a. (The application does not have to load the PRX module for the NpWebApi2 library, as this process will be carried out automatically.)

# Reference Materials

For an overall explanation of the PlayStation™Network Web APIs, refer to the following document.

* [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html)

For information about the NpCppWebApi library, which uses Web API features via a C++ interface instead of using the PlayStation™Network Web APIs directly, refer to the following documents.

* [NpCppWebApi Library Overview](../NpCppWebApi-Overview/__document_toc.html)
* [NpCppWebApi Library Reference](../NpCppWebApi-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpWebApi2 Library](../ReleaseNotes/PlayStation_Network-NpWebApi2-ReleaseNotes.html)