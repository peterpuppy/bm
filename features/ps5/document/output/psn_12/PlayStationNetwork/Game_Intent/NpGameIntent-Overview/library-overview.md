# NpGameIntent Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpGameIntent-Overview/library-overview.html

# Library Overview

This topic describes the purpose and characteristics of the NpGameIntent library, its main features, how to embed it into a program and a sample program that uses the library.

# Purpose and Characteristics

The NpGameIntent library is a library for receiving game intent information. An application can use this library to receive game intent information from the system when a game intent event occurs and to obtain the required property values.

# Main Features

The main features provided by the NpGameIntent library are as follows:

* Feature to receive game intent information from the system
* Feature to obtain property values from the received game intent information

# Embedding into a Program

Include np\_game\_intent.h in the source program.

Link libSceNpGameIntent\_stub\_weak.a upon building the program (the application does not have to load the PRX module for the NpGameIntent library as this process will be carried out automatically).

In addition, refer to the "[Preparation](preparation.html)" section of the "[Using the Library](using-the-library.html "This topic describes the preparations and basic procedure for using the NpGameIntent library, and also introduces a typical implementation example.")" chapter to prepare a parameter file (param.json) describing the types of game intents that are supported by the application.

# Sample Program

A sample program using the NpGameIntent library is as follows. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

## sample\_code/playstation\_network/api\_webapi\_session\_manager

This sample exemplifies basic usage of Player Sessions/Game Sessions and the Matches Web API. This sample includes processing to receive game intent information from the system using the NpGameIntent library and to join a Player Session.

# Reference Materials

Refer to the following document for an overall explanation of the game intent system:

* [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpGameIntent Library](../ReleaseNotes/PlayStation_Network-NpGameIntent-ReleaseNotes.html)