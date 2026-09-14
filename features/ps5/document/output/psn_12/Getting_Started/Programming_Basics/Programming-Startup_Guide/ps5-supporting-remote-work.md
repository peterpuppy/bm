# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-supporting-remote-work.html

# Appendix: Remote Work Support

This topic introduces some useful features for working remotely from home or other locations using a DevKit/TestKit that is located in an office.

# Remote Viewer

## Using Remote Viewer on a Remote PC

Remote Viewer provides the "Remote Worker Mode". Remote Worker Mode allows users to stream high-quality audio and video from a target to a remote PC and to control the target using input, such as from a controller, from the remote PC. Users can, simultaneously with the above, connect their local PC to the target to debug applications.

## Using Remote Viewer via Remote Desktop

Users can also control a target using a controller or other input device connected to a remote PC when using Remote Desktop.

Refer to [Remote Viewer User's Guide - Remote Working with Remote Viewer](../Remote_Viewer-Users_Guide/remote-working-with-remote-viewer.html) for details.

# Safe Mode

The `prospero-ctrl power safe-mode` command allows you to transition a target to Safe Mode by operating from a remote PC. Refer to "Target Manager CLI User's Guide - Controlling Targets using the command line - Controlling Targets with prospero-ctrl" for details about this command. Refer to [Development Kit Setup Guide - Safe Mode Features](../DevKit-Setup_Guide/safe-mode-features.html) and [Testing Kit Setup Guide - Safe Mode Features](../TestKit-Setup_Guide/safe-mode-features.html) for details about Safe Mode.

# Workspace Management API

**Writing to a Workspace by an Application**

In a working environment in which the target is in an office and the host PC is accessed remotely, the Workspace Management API of the Workspace library can be used to copy assets from the office server to the target when doing so is necessary. In other words, an application can call the Workspace Management API to download assets from a server and write them to a standalone workspace on the target. Refer to [Workspace Library Overview - Using the Library - Basic Procedure for Writing Data to a Standalone Workspace](../Workspace_Library-Overview/basic-procedure-for-writing-data-to-a-standalone-workspace.html) for details.