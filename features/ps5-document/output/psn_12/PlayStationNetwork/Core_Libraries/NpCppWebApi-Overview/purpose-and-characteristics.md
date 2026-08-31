# NpCppWebApi Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Overview/purpose-and-characteristics.html

# Library Overview

# Purpose and Characteristics

The NpCppWebApi library provides a C++ language binding for each feature of the PlayStation™Network Web API (Web API). Although developers can also use the NpWebApi2 library to use Web APIs directly, the NpCppWebApi library enables developers to use Web APIs through function calls and by handling C++ objects. In other words, the library provides alternative functions for specifying the path of each Web API endpoint and HTTP method, as well as classes corresponding to Web API Json objects. Thus, developers no longer need to consider assembling URI strings or parsing Json. In addition, since the compiler issues a warning when an invalid datatype or structure is detected (as with other C/C++ language libraries), simple mistakes can be eliminated at the implementation stage. In summary, the NpCppWebApi library enables developers to use Web APIs while enjoying the benefits of a statically typed language.

# Main Features

The main features provided by the NpCppWebApi library are as follows.

* A group of functions (called Web API call functions) that correspond 1:1 with each combination of Web API endpoint and HTTP method
* A group of classes (encapsulations of Json object parsing/serialization processing) that correspond 1:1 with each Web API Json object
* Networking processing that calls Web APIs (Either synchronous or asynchronous processing is selected when the library is initialized)

# Embedding into a Program

Include np\_cppwebapi.h in the source program. In addition, before calling any NpCppWebApi library function in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_CPP_WEB_API) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceNpCppWebApi\_stub\_weak.a.

## Notes for Creating an Application Package

The NpCppWebApi library is a library that is installed in an application package. Therefore, libSceNpCppWebApi.prx included in the SDK must be copied to the sce\_module directory of the application package. For details, refer to the [Sysmodule Library Overview](../Sysmodule-Overview/__document_toc.html) document.

# Sample Programs

Sample programs that use the NpCppWebApi library are provided as follows.

## sample\_code/playstation\_network/api\_np\_cppwebapi

This sample program uses the basic features of the NpCppWebApi library. The sample is coded so that it uses asynchronous processing.

## sample\_code/playstation\_network/api\_np\_commerce

This sample program uses the In-Game Catalog Web API.

## sample\_code/playstation\_network/api\_np\_profanity

This sample program uses the Profanity Filter Web API.

## sample\_code/playstation\_network/api\_webapi\_advanced\_player\_profile

This sample program uses the Advanced Player Profile Web API.

## sample\_code/playstation\_network/api\_webapi\_communication\_restriction\_status

This sample program uses the Communication Restriction Status Web API.

## sample\_code/playstation\_network/api\_webapi\_leaderboards

This sample program uses the Leaderboards Web API.

## sample\_code/playstation\_network/api\_webapi\_matchmaking

This sample program uses the Matchmaking Web API.

## sample\_code/playstation\_network/api\_webapi\_session\_manager

This sample program uses the Session Manager Web API.

## sample\_code/playstation\_network/api\_webapi\_title\_cloud\_storage\_basic

This sample program uses the Title Cloud Storage Web API.

## sample\_code/playstation\_network/api\_webapi\_title\_cloud\_storage\_data\_distribution

This sample uses the Title Cloud Storage Web API to obtain variables and data that have been distributed to all users of a title.

## sample\_code/playstation\_network/api\_webapi\_user\_profile

This sample program uses the User Profile Web API.

# Reference Materials

Refer to the following document for an overview of the Web API.

* [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html)

Refer to the following documents for information about the Json2 library and NpWebApi2 library. These documents should be consulted before using the NpCppWebApi library.

* [Json2 Library Overview](../Json2-Overview/__document_toc.html), [Json2 Library Reference](../Json2-Reference/__document_toc.html)
* [NpWebApi2 Library Overview](../NpWebApi2-Overview/__document_toc.html), [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html)

In addition, refer to each Web API document for explanations of the various features of corresponding Web API.

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpCppWebApi Library](../ReleaseNotes/PlayStation_Network-NpCppWebApi-ReleaseNotes.html)