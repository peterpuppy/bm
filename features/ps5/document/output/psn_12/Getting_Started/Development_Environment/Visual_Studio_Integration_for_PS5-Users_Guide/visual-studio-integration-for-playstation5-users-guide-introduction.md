# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/visual-studio-integration-for-playstation5-users-guide-introduction.html

# Visual Studio Integration for PlayStation®5 User's Guide Introduction

Development on this platform is integrated with Visual Studio so that you can easily create projects, build, and then run or debug your applications. This document describes the Visual Studio Integration (VSI) features provided.

## Features and Benefits

The following list describes the main features and benefits of the Visual Studio Integration:

* C and C++ support:
  + Build support with full dependency checking.
  + IntelliSense tailored for PlayStation®5.
  + Integration with the Clang Static Analyzer.
  + Support for displaying preprocessor output, assembly, and disassembly for individual files.
* PlayStation Shader Language (PSSL) support:
  + Build support with full dependency checking.
  + Fully featured editor support for user source and Standard Library information.
  + Support for displaying disassembly for individual files.
* Intel® Implicit SPMD Program Compiler (ISPC) support for SDK 11.00 onwards:
  + Build support with full dependency checking.
* Support for SN-DBS for faster builds.
* Templates included for common project and file types.
* Support for configuration of build and debugging settings via project properties.

## Hardware Support

The following table shows which features are supported by Development Kits (DevKits) and Testing Kits (TestKits), collectively known as Targets, when in various modes.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Development Kit**  (DevKit) | | | **Testing Kit (TestKit)** | |
| **Development** | **Assist** | **Release** | **Assist** | **Release** |
| Launch application stored on Host PC from Host PC | **Yes** | **Yes** | **No** | **Yes** | **No** |
| View console output | **Yes** | **Yes** | **Yes** | **Yes** | **No** |
| Trigger core dump from Host PC | **Yes** | **No** | **No** | **No** | **No** |

For more information on configuring DevKits and TestKits, refer to:

* [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html)
* [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html)

## Installation

Visual Studio Integration (VSI) is usually installed as part of the SDK Manager installation. Before the installation you must first:

* Install Microsoft Visual Studio 2019, 2022, and/or
  2026(Professional
  or above).
* Alternatively, install Build Tools for Visual Studio 2019, 2022, and/or
  2026.
* Install the Visual Studio workloads of "Desktop development with C++" and/or
  "Game development with C++".

Before use of VSI, you must first:

* Install the PlayStation®5 SDK.
* Define an environment variable "`SCE_PROSPERO_SDK_DIR`" to point to the root of the PlayStation®5 SCE run-time library directory, which is the directory containing the "host\_tools" and "target" directories.

## The VSI Toolbar

When you install VSI, a new toolbar appears in Visual Studio, which enables you to perform distributed builds, and view version information and help documentation. The information button on the VSI toolbar displays version information and help documentation.

Note:

Distributed build commands only appear if a supported distributed build system is installed.

## Related Information

In addition to this document, SIE also provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements. You can refer to the release notes below:

* [Release Notes - Visual Studio Integration for PlayStation®5](../ReleaseNotes/Getting_Started-VSI_Release_Notes.html)