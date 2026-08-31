# Cross-generation Application Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Cross_Generation_Application-Tutorial/about-this-tutorial.html

# Tutorial Overview

This topic provides an overview of the tutorial supporting cross-generation gameplay between PlayStation®5 and PlayStation®4. A sample program and related reference materials are also introduced.

# About This Tutorial

This tutorial describes how to create applications that support cross-generation gameplay between PlayStation®5 and PlayStation®4. The configuration of the sample is explained first, along with key points regarding sample implementation for various PlayStation™Network-related features such as activities and matchmaking. Next, the points to note for developing cross-generation applications are explained.

The sample for this tutorial contains the files and assets required for Visual Studio projects and packaging for both PlayStation®5 and PlayStation®4, allowing you to build applications and create packages for each platform. (For details, refer to chapters "[Directories and File Structure in This Sample](folder-and-file-configuration.html)" and "[Packaging](packaging.html)".)

The applications created using this tutorial comply with the requirements of the Technical Requirements Checklist and can be used for master submission to Platform Certification and Operations. Specifically, the following applications can be created:

* Applications for PlayStation®5 built using the PlayStation®5 SDK that comply with the [Technical Requirements Checklist for PlayStation®5](../../../TRC/latest/TRC/__document_toc.html)
* Applications for PlayStation®4 built using the PlayStation®4 SDK and PlayStation®4 Cross-Generation SDK (hereafter, "Cross-Gen SDK") that comply with the "Technical Requirements Checklist for PlayStation®4" and the [Technical Requirements Checklist for PlayStation®5 Cross-Generation Supplement](../Technical_Requirements_Checklist-PS4CrossGen_Supplement/__document_toc.html).

  (The PlayStation®4 SDK must be installed to create applications for PlayStation®4.)

The NP Communication ID is shared between the NP Title ID of a PlayStation®5 application and the NP Title ID of a PlayStation®4 application, allowing cross-generation gameplay between the two platforms.

Note:

This tutorial assumes that the reader has basic knowledge of the various PlayStation™Network-related features and application packaging methods for both PlayStation®5 and PlayStation®4.

# Sample Program

The sample program for this tutorial is provided in the following PlayStation®5 SDK directory: For basic information (directory structure, and so forth) that is common among all the sample programs provided in the SDK, refer to [Sample Program Overview](../Sample-Overview/__document_toc.html).

* sample\_code/playstation\_network/tutorial\_cross\_gen

This sample is a first-person shooter game. Refer to the sample readme for details of the game content and operating instructions.

The program supports multiplayer mode, allowing real-time multiplayer gameplay of up to four players. Although features specific to the Cross-Gen SDK are not used, Single Player mode is also supported for single-player gameplay.

This sample also contains Visual Studio projects for both PlayStation®5 and PlayStation®4.

# Reference Materials

For more information about the Cross-Gen SDK as a whole, refer to the document below:

* [Cross-Generation Overview](../Cross_Generation-Overview/__document_toc.html)

For information about bugs, points to note, restrictions and announcements, refer to the release notes below:

* [Release Notes - Cross-generation Application Tutorial](../ReleaseNotes/PlayStation_Network-Cross_Generation_Application-Tutorial-ReleaseNotes.html)