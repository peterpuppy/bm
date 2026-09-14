# System Software Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Overview/definition.html

# System Software Overview

# Definition

The system software is a collective name for multiple pieces of software that run on PlayStation®5 hardware (Development Kits, Testing Kits, and retail units) with the following roles and characteristics:

* Software that makes PlayStation®5 hardware and peripherals run
* Software that serves as a platform for applications
* Software that provides user interfaces for users of PlayStation®5 hardware
* Software for users to maintain and manage PlayStation®5 hardware
* Software for configuring and changing PlayStation®5 hardware settings
* Built-in system applications that run in coordination with applications developed by licensees

# Architectural Overview

An overview of the relationship between the system software and an application is shown in the figure below.

Relationship Between the System Software and an Application

The system software comprises the kernel, multiple processes, dynamic libraries (PRX), etc. APIs are disclosed for some of these components, and each of their features can be used by applications. These APIs are provided to applications in a format such that they can be called using a C/C++ programming language.

The system software executes a licensee-developed application (a typical game application) as a single independent process.

# Updating the System Software of a Development Kit or Testing Kit

The system software of a Development Kit or Testing Kit can be updated using a system updater (file with extension ".PUP") for the respective hardware.

The system software of a Development Kit or Testing Kit can be updated so that the version number is incremented; it can also be updated so that the version number is decremented. Note, however, that an update to decrement the version to an arbitrary earlier version will not always be possible.

For details about updating the system software of Development Kits, refer to [Development Kit Setup Guide - Update the System Software](../DevKit-Setup_Guide/update-the-system-software.html).

For details about updating the system software of Testing Kits, refer to [Testing Kit Setup Guide - Update the System Software](../TestKit-Setup_Guide/update-the-system-software.html).