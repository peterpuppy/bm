# Workspace Explorer User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspace_Explorer-Users_Guide/002_setting-the-file-serving-directory.html

# Workspace Explorer User's Guide Introduction

Workspace Explorer is an application for managing the creation and contents of a workspace. All functionality available in the application is also available via CUI tools, refer to
[Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html).

For more information on workspaces, refer to
[Workspaces Overview](../Workspaces-Overview/__document_toc.html).

Note: The term 'workspaces' is used to mean both Standalone and System Managed Host Mirror workspaces. If there is an explicit difference between the two workspace types, the appropriate workspace type name will be used.

## Features and Benefits

Workspace Explorer has the following features:

* Create, Delete and Manage workspaces on the Target.
* Push files from the Host PC to a workspace.
* Pull files from a workspace back to the Host PC.
* View file differences between workspace and the Host PC.

## Hardware Support

The following table shows which features are supported by Development Kits (DevKits) and Testing Kits (TestKits), collectively known as Targets, when in various modes.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Development Kit** | | | **Testing Kit** | |
| **Development mode** | **Assist mode** | **Release mode** | **Assist mode** | **Release mode** |
| Create Workspaces | **Yes** | **Yes** | **No** | **Yes** | **No** |
| Delete Workspaces | **Yes** | **Yes** | **No** | **Yes** | **No** |
| Manage Workspaces | **Yes** | **Yes** | **No** | **Yes** | **No** |

For more information on setting up DevKits and TestKits, refer to:

* [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html)
* [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html)

## Installation

Workspace Explorer is installed using the SDK Manager.

## Launching Workspace Explorer

Workspace Explorer is one of the Target Manager UI family of GUI products.

To start Workspace Explorer:

* From the **Start** menu, in **SCE** - **PS5** folder, click **Workspace Explorer**.
* From Target Manager, choose **Workspace Explorer** from the **Apps** menu.
* From the notification area, click **Taskbar Application for PlayStation®5**, then **Workspace Explorer**.

You can also pin an open instance of **Workspace Explorer** to the taskbar for future launching.

## Home Tab

For Workspace Explorer, the Home tab enables you to access the following:

| **Option** | **Icon** | **Description** |
| --- | --- | --- |
| Add |  | Adds a new workspace. Refer to [Creating a New Workspace in Workspace Explorer](creating-a-new-workspace-in-workspace-explorer.html) for more information. |
| Manage |  | Opens the **Manage Workspaces** dialog. Refer to [Managing Workspaces in Workspace Explorer](managing-workspaces-in-workspace-explorer.html) for more information. |
| Deploy |  | Populates the currently selected workspace with files and directories defined by a GP5 File. Can also launch the associated `.elf` after the deploy process has been completed. Refer to [Deploy Files Using Workspace Explorer](deploy-files-using-workspace-explorer.html) for more information. |
| Push |  | Pushes files from the Host PC to the selected workspace. Refer to [Push Files to a Target Workspace Using Workspace Explorer](push-files-to-a-target-workspace-using-workspace-explorer.html) for more information. |
| Mirror push |  | Prepopulate the System Managed Host Mirror with the selected files/folders. Refer to [Mirror Push Files Using Workspace Explorer](mirror-push-files-using-workspace-explorer.html) for more information. |
| Pull |  | Pulls files from the selected workspace to the Host PC. Refer to [Pull Files from a Target Workspace Using Workspace Explorer](pull-files-from-target-workspace-using-workspace-explorer.html) for more information. |
| Compression Level |  | Sets the compression level for file transfer. Refer to [Compression Level](comparing-target-workspace-and-local-file-system-contents.html#workspace-explorer-users-guide_1_9__section_vbv_3bq_chc) for more information. |
| Create Diff |  | Creates a list of files that are different between the Host PC and the Target. Refer to [Comparing Target Workspace and Local File System Contents](comparing-target-workspace-and-local-file-system-contents.html) for more information. |
| Comparison mode |  | Sets how the file differences should be calculated.   * **Accurate** - Considers files to be the same if their hash matches. * **Quick** - Considers files to be the same if they have the same size and their modification times are within 10µs of each other.   Refer to [Comparing Target Workspace and Local File System Contents](comparing-target-workspace-and-local-file-system-contents.html) for more information. |
| Refresh |  | Refreshes the file lists. |
| Reset Layout |  | Returns the screen to the default layout. |

## Accessing Help

To launch the PlayStation®5 Help, click the **Help** icon  on the Ribbon UI.

## Related Information

In addition to this document, SIE also provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements. You can refer to the release notes below:

* [Release Notes - Workspace Explorer for PlayStation®5](../ReleaseNotes/Getting_Started-Workspace_Explorer_Release_Notes.html)

# Workspace Explorer Application Interface

Workspace Explorer uses the Ribbon UI common to all Target Manager applications. The [**Home** tab](workspace-explorer-users-guide-introduction.html#workspace-explorer-users-guide_0__section_w4f_nw4_chc) for each application contains functionality unique to that application.

Refer to the [Target Management Applications UI Overview](../TM_Applications_UI-Overview/__document_toc.html) for further information about the other tabs and menus in the Ribbon.

| **Number** | **Name** | **Description** |
| --- | --- | --- |
| 1 | **File** menu | Collection of tools for file management and software information. |
| 2 | **Home** tab | Collection tools unique to Workspace Explorer. |
| 3 | **Target** tab | Collection of tools for Target management and communication. Refer to [Target Management Applications UI Overview](../TM_Applications_UI-Overview/__document_toc.html) for more information. |
| 4 | Ribbon UI | The persistent Ribbon UI containing the main tools available to the user. Refer to [Home Tab](workspace-explorer-users-guide-introduction.html#workspace-explorer-users-guide_0__section_w4f_nw4_chc) for more information. |
| 5 | Target folder structure | List of the folder hierarchy on the Target workspace. |
| 6 | Target file list | List of files in the selected folder on the Target workspace. |
| 7 | Status bar | Status of the connection to the Target. |
| 8 | Host file list | List of files in the selected folder on the Host PC. |
| 9 | Host folder structure | List of the folder hierarchy on the Host PC. |

# The TMUI Status Bar

For all TMUI applications except Target Manager, the status bar contains information about the Target that the application is currently using.

The status bar contains the following information:

| Element | Description |
| --- | --- |
| **File Serving Directory** | The File Serving directory address on the Host PC. Refer to [Setting the File-Serving Directory](002_setting-the-file-serving-directory.html) for more information. |
| **Status** | The status of the connection between the Host PC and the Target. This can be **Connected**, **Available**, or the username of any other user connected. |
| **Power** | The power status of the Target.   * **Powering On** * **On** * **Powering Off** * **Off** * **Going into Rest Mode** * **Rest Mode (standby)** * **Rest Mode (main on standby)** - The Target is performing a   background task and will enter Rest Mode when it has completed. |
| **SDK** | The software version installed on the Target. |

# Setting the File-Serving Directory

The file-serving directory enables an application on the Target to access files on the Host PC by using "`/host`" in the code.

Note:

When using the command line tools such as `prospero-ctrl`, the file serving directory is referred to as `fsroot`.

For more information on the file-serving directory, refer to [Programming Startup Guide - Basic Information on File Access](../Programming-Startup_Guide/basic-information-on-file-access.html).

To set the file-serving directory from TMUI applications:

1. On the **Target** tab, in the **More** group, click **Set file serving directory** ().
2. In the **Set File Serving Directory** dialog box, browse to the folder to use as the file-serving directory, and then click **Select Folder**.

You can also set the file serving directory from Target Manager.

To set the file-serving directory in Target Manager, use any of the following methods:

* Select one or more Targets, and then drag the folder to the selection.
* Select one or more Targets, and then on the **Home** tab, in the **More** group, click **Set file serving directory** (). Then, in the **Set File Serving Directory** dialog box, browse to the folder to use as the file-serving directory, and then click **Select Folder**.

The file-serving directory is displayed in the **File Serving Directory** column.

For the default Target, you can also right-click any folder in Windows Explorer, point to **PS5**, and then click **Set File Serving Directory** to set the file-serving directory.

Note:

The file-serving directory applies to an individual Target. Use Working Directory for per-process file access.