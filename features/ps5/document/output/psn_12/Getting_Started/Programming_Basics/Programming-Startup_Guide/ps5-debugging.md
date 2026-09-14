# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-debugging.html

# Content Provided by SIE for Developers

This topic discusses various content that SIE provides to enable the development of applications for PlayStation®5 to proceed smoothly. It describes important resources and tools in each stage of development, from specification design to building, debugging, performance tuning, and final testing operations, as well as for managing and operating Development Kits and Testing Kits.

# Specification Design

Upon starting development, make sure to have gone through the following document:

* "TRC (Technical Requirements Checklist) for PlayStation®5":

  Applications to be submitted to SIE must be implemented in compliance with each requirement of the TRC (Technical Requirements Checklist) for PlayStation®5 (TRC). Because there are many requirements relating to implementation, it is strongly recommended that you read this document at the initial stage of application development.

# Building

The compiler used when building applications is a customized version of Clang/LLVM that is provided by SIE. The compiler supports multiple language modes for C and C++. Refer to [C/C++ Compiler Reference - Language Selection and Mode Options - -std=language](../C_Cpp_Compiler-Reference/stdlanguage.html). (Note that the standard library that is used is based on the language mode specified to the compiler. Refer to "[Standard Libraries](standard-libraries.html)" for details.) Start this compiler using Visual Studio with Visual Studio Integration installed to build an application.

## Clang

Clang is a compiler front end for programming languages such as C and C++. For details about Clang, refer to "Clang: a C language family frontend for LLVM" (<https://clang.llvm.org/>).

## LLVM

LLVM is a compiler infrastructure that optimizes programs and creates code that is executed in high speed. For details about LLVM, refer to "The LLVM Compiler Infrastructure" (<https://llvm.org/>).

## Visual Studio Integration for PlayStation®5 (VSI)

VSI is a Visual Studio add-in to integrate and manage the compiler, debugger, and the performance analysis tool "Razor CPU", which are also provided as Visual Studio add-ins.

# Operating a DevKit/TestKit from the Host PC

The types of software provided for operating and managing a DevKit/TestKit from the host PC are as follows.

Note:

It may not be possible to perform the operations shown below depending on the DevKit/TestKit Release Check Mode setting.

## Target Manager for PlayStation®5

DevKit/TestKit operation from the host PC is possible using the Target Manager for PlayStation®5 (Target Manager hereafter). In addition to connecting the host PC to the DevKit/TestKit and controlling power states, the following features are provided.

* Settings feature:

  By using the [Target Settings] feature, the DevKit/TestKit settings can be changed. For details about the items that can be configured, refer to the [Target Settings Application User's Guide for Development Kit/Testing Kit Configuration](../Target_Settings_Application-Users_Guide_for_DevKit_TestKit_Configuration/__document_toc.html) document.
* Console input/output confirmation feature:

  By using the [Console Output] feature, the TTY output that is output from the DevKit/TestKit can be confirmed on the host PC. In addition, standard input can also be performed with [Console Input]. For details, refer to the [Console Output User's Guide](../Console_Output-Users_Guide/__document_toc.html) document.
* File system map feature:

  By using the [Map Filesystem] feature, files in the console storage/M.2 SSD storage of the DevKit/TestKit can be accessed from Windows Explorer. Refer to the [Target Manager GUI User's Guide](../Target_Manager_GUI-Users_Guide/__document_toc.html) document for details.
* Capture and playback:

  By using the [Controller Capture and Playback] feature, input data from DevKit/TestKit input devices, such as controllers, can be captured. By saving the captured input data to a file, it is also possible to playback the user input. For details, refer to the [Controller Capture and Playback User's Guide](../Controller_Capture_and_Playback-Users_Guide/__document_toc.html) document.

## prospero-ctrl (Command Line Tool)

You can operate a DevKit/TestKit from a host PC using the prospero-ctrl command line tool. Since it is a command line tool, series of processes can be easily automated by writing them as batch files.

For details about prospero-ctrl, refer to the [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html) document.

## Target Manager (TM) API

The Target Manager API is for operating DevKits/TestKits from programs on the host PC. The Target Manager API is provided as a C# API - use it when you want to manage and operate a DevKit/TestKit in coordination with your own host tools.

prospero-ctrl and prospero-run are command line tools created using the Target Manager API. Their source code is provided in %SCE\_ROOT\_DIR%\PROSPERO\Tools\Target Manager Server\samples.

For details about the Target Manager API, refer to the [Target Manager API Reference](../Target_Manager_API-Reference/__document_toc.html) document.

# Executing Executable Files in the Host PC on the DevKit/TestKit

The following methods are provided for executing executable files in the host PC on a DevKit/TestKit.

## Visual Studio

An executable file stored on the host PC can be executed on a DevKit/TestKit by selecting [Debug] - [Start Debugging] or [Debug] - [Start Without Debugging] in Visual Studio.

## Target Manager for PlayStation®5

An ELF file stored in the host PC can be executed on the DevKit/TestKit by selecting the DevKit/TestKit with Target Manager and then selecting [Load Executable]. An ELF file can also be started by dragging and dropping the ELF file into the Target Manager target list.

## prospero-run (Command Line Tool)

An ELF file in the host PC can be executed on a DevKit/TestKit using the prospero-run command line tool.

For details about prospero-run, refer to the [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html) document.

# Debugging

Use the Debugger for PlayStation®5 that is integrated into Visual Studio for debugging applications.

## Debugger for PlayStation®5

Applications running on DevKit can be debugged using a Visual Studio debug interface, in a similar manner to how Windows programs are debugged.

For details about Debugger for PlayStation®5, refer to the [Debugger User's Guide](../Debugger-Users_Guide/__document_toc.html) document.

## Core Dump

The core dump feature is provided as a method for investigating problems that occur when the Debugger for PlayStation®5 is not connected. The core dump feature outputs the system state as a core dump file set when an exception occurs and an application crashes. It will be possible to determine the cause of the exception by analyzing the output core dump file set. It is also possible to copy the core dump file set to a USB drive with [★Debug Settings] > [Core Dump] > [Copy & Delete] in the system software.

For details about the core dump feature, refer to the [Core Dump System Overview](../Core_Dump_System-Overview/__document_toc.html) document.

# Performance Tuning

Performance tuning can be carried out by using Razor CPU Live, Razor CPU, and Razor GPU on the host PC.

## Razor CPU Live

Razor CPU Live is a performance analysis tool that streams real-time performance data and graphs the data using a simple UI. Session length is restricted only for a local storage area; it is possible to jump to an arbitrary point and to identify performance deterioration. Razor CPU Live is useful in evaluating performance problems that do not occur frequently - for example, spikes and I/O bottlenecks that extend over multiple frames. If you need a more detailed analysis, it is possible to select the target time range and to create a Razor CPU full capture.

## Razor CPU

Razor CPU captures detailed performance data to identify and resolve bottlenecks in a code. Razor CPU can capture hardware operation at the lowest level, including thread scheduling, system call, command sampling, performance counter, disassembly, etc. The libSceRazorCPU library provides many target-side functions such as push/pop user marker and capture control.

## Razor GPU

Razor GPU is a stand-alone GPU performance analysis and debug tool based on the Capture-Replay feature. By using Razor GPU, it is possible to optimize, and analyze bugs of, the graphics processing section of an application.

# Executing an Application from the System Software

Launch tests (for example) simulating operation on a retail unit can be performed on a developed application by executing the application from the system software.

## ★Workspace

The ★Workspace feature is provided as a method for executing applications that are in the console storage/M.2 SSD storage of a DevKit/TestKit from the system software. For details, refer to the [System Software User's Guide (Application Development Support)](../System_Software-Users_Guide_for_Development_Support/__document_toc.html) document.

## Release Mode

When the DevKit/TestKit Release Check Mode is set to "Release Mode" (from [★Debug Settings] > [Boot Parameters] > [Release Check Mode] in the system software), features that are not implemented on retail units will be restricted. When testing operations in this state, it will be possible to detect processing being carried out by the application that cannot be executed on retail units - for example, file access to /host and DECI communication with the development host PC.

# Testing Operation with the TestKit

Applications are required by TRC [R5017](../../../TRC/latest/TRC/R5017.html) to ensure using the TestKit that the implemented features operate as intended. In order to test operation using the TestKit, the following features are provided. For details about the TestKit, refer to the [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html) document.

## Assist Mode

When setting the TestKit Release Check Mode to "Assist Mode" (from the system software's [★Debug Settings] > [Boot Parameters] > [Release Check Mode]), it will be possible to use some of the host tool development support features on TestKit. For details, refer to [System Software User's Guide (Settings) - Features of the ★Debug Settings Menu - Boot Parameters － Release Check Mode](../System_Software-Users_Guide_for_Settings/boot-parameters-release-check-mode.html).

Note that it is also possible to set "Assist Mode" on DevKit.

# Package File Installing

A package file created using the Publishing Tools can be installed on DevKit or TestKit as follows: Refer to the [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html) and [Content Information Specifications](../Content_Information-Specifications/__document_toc.html) documents for details about package creation.

## Installing a Package File on a USB Drive Using Package Installer

A package file on a USB drive can be installed on a DevKit/TestKit from [★Debug Settings] > [Game] > [Package Installer] in the system software. For details, refer to [System Software User's Guide (Application Development Support) - Development Support Features by Application - Package Installation Feature](../System_Software-Users_Guide_for_Development_Support/package-installation-feature.html).

## Installing a Package File on the Host PC Using Target Manager/prospero-ctrl

A package file on the host PC can be installed on DevKit/TestKit with "Packages and entitlements" > "Install package" of the Target Manager or the package install command of prospero-ctrl. Refer to each document for details.

* Target Manager GUI User's Guide
* Target Manager CLI User's Guide

## Installing a Package File on a Web Server Using Package Downloader

A package file placed on a web server can be installed on DevKit/TestKit from the system software's [★Debug Settings] > [Game] > [Package Downloader]. For details, refer to [PlayGo Library Overview - Appendix C: Package Downloader](../PlayGo-Overview/appendix-c-package-downloader.html).