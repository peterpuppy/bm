# Workspace Explorer User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspace_Explorer-Users_Guide/selecting-a-workspace-in-workspace-explorer.html

# Using Workspace Explorer

Workspace Explorer enables you to create, manage, and populate workspaces on the Target. The following topics describe how to use Workspace Explorer:

* [Creating a New Workspace in Workspace Explorer](creating-a-new-workspace-in-workspace-explorer.html)
* [Managing Workspaces in Workspace Explorer](managing-workspaces-in-workspace-explorer.html)
* [Selecting a Workspace in Workspace Explorer](selecting-a-workspace-in-workspace-explorer.html)
* [Viewing the Contents of the Local File System and the Target Workspace Views in Workspace Explorer](local-file-system-and-target-workspace-views.html)
* [Push Files to a Target Workspace Using Workspace Explorer](push-files-to-a-target-workspace-using-workspace-explorer.html)
* [Mirror Push Files Using Workspace Explorer](mirror-push-files-using-workspace-explorer.html)
* [Deploy Files Using Workspace Explorer](deploy-files-using-workspace-explorer.html)
* [Pull Files from a Target Workspace Using Workspace Explorer](pull-files-from-target-workspace-using-workspace-explorer.html)
* [Comparing Target Workspace and Local File System Contents](comparing-target-workspace-and-local-file-system-contents.html)
* [Specifying the Correct Workspace When Launching an ELF](specifying-the-correct-workspace-when-launching-an-elf.html)

# Creating a New Workspace in Workspace Explorer

Creating a new workspace requires filling out the **Create Workspace** dialog.

| Field | **Description** |
| --- | --- |
| **Name** | The name of the workspace.  Note: Maximum size for the workspace name is 62 characters. |
| **Workspace Type** | Sets the type of workspace to be created.  Two options are available:   * **Fixed Size** (static) * **Auto-grow** (expands on demand) |
| **Minimum Size** | Sets the initial size of the workspace on storage.  The units available are:   * **MiB** - Mebibytes * **GiB** - Gibibytes   Note: Required if the **Workspace Type** is "**Fixed Size**". |
| **Maximum Size (Optional)** | Sets the maximum size a workspace can grow to.  Optional  Only available when the **Workspace Type** is set to **Auto-grow**.  Values can be set using one of two units:   * **MiB** - Mebibytes * **GiB** - Gibibytes   Note: A size of zero means "no maximum size". |
| **Select this workspace after it is created** | Sets whether or not Workspace Explorer automatically selects the new workspace after creation. |
| **Use M.2 SSD storage** | Sets whether or not the new workspace is created on the M.2 SSD storage installed on the Target.  Only available if a M.2 SSD has been installed on the Target and formatted ready for use. Refer to [Target Manager GUI User's Guide - Using Target Manager to Manage Files and Targets - Configuring M.2 SSD Storage on a Target](../Target_Manager_GUI-Users_Guide/004_configuring-m2-ssd-storage-on-a-target.html) for more details. |

To create a new Workspace:

1. On the **Home** tab, in the **Workspaces** group, click **Add** ()
   .
2. In the **Create Workspaces** dialog, type the name of the workspace into the **Name** combo box, or select a previously entered name from the drop-down list.
3. Choose a **Workspace Type**.
4. Set a **Minimum size** and **Maximum size** (if required) for the workspace, choosing the relevant units from the drop-down lists.
5. Check the **Select this workspace after it is created** checkbox if required.
6. Check the **Use M.2 SSD storage** checkbox if required.
7. Click **OK**.

# Managing Workspaces in Workspace Explorer

The **Manage Workspaces** dialog enables management of all the workspaces on the Target's filesystem including those configured by other users of the Target. The **Manage Workspaces** dialog shows the current capacity, maximum size and current size of a workspace and offers operations that can be carried out on single or multiple workspaces.

Within the **Manage Workspaces** dialog, the following actions are available:

* **Delete** - Deletes an existing workspace.
* **Purge** - Removes the contents of the workspace, but retains the root directory.
* **Run FSCK** - Checks the integrity of the file system.

## Delete

When an existing workspace is no longer required, it can be deleted.

To delete a workspace:

1. On the Ribbon, in the **Workspaces** section, click **Manage** ().
2. In the **Manage Workspaces** dialog, in the list view, select the workspace(s) to be deleted.
3. Click **Delete**.

## Purge

If the workspace becomes significantly fragmented, as indicated by the **Garbage Size** column, then it may be necessary to purge the workspace. Purging removes the contents of the workspace, but leaves the root directory in place. The removed files can then be restored using a [Deploy](deploy-files-using-workspace-explorer.html) or [Push](push-files-to-a-target-workspace-using-workspace-explorer.html) command.

Note:

**Purge** is not available for use with the System Managed Host Mirror(s).

To purge a workspace:

1. On the Ribbon, in the **Workspaces** section, click **Manage** ().
2. In the **Manage Workspaces** dialog, in the list view, select the workspace(s) to be purged.
3. Click **Purge**.

## File System Check - Run FSCK

If the file system shows signs of corruption, you can check the integrity of the file system of the workspace.

Note:

**FSCK** is not available for use with the System Managed Host Mirror(s).

To run a File System check:

1. On the Ribbon, in the **Workspaces** section, click **Manage** ().
2. In the **Manage Workspaces** dialog, in the list view, select the workspace(s) to be checked.
3. Click **Run FSCK**.

# Selecting a Workspace in Workspace Explorer

Workspace Explorer can only push or pull from one workspace at a time.

The **Target workspace** drop-down list
enables you to you select which workspace is currently active in the application.

The area to the right of the **Target workspace** selection control shows the usage information and the garbage levels of the workspace.

# Viewing the Contents of the Local File System and the Target Workspace Views in Workspace Explorer

**Local file system** view and **Target workspace** view display both a Windows Explorer-style hierarchy tree, and a file window. The file window contains the following columns:

| **Column** | **Description** |
| --- | --- |
| **Name** | The name of the file, folder or drive. |
| **Status** | Displays the compression status of the files.  If a file is compressed, this will display **Compressed**. |
| **Date modified** | Displays the time and date when latest modification was made on the file. |
| **Type** | The type of file, folder or drive. |
| **Size** | Size of the file. |
| **Compression ratio** | Illustrates the ratio between the file's uncompressed and compressed size. |

## Local File System View

**Local file system** view shows the local file system of the Host PC.

The currently selected folder is used as the root folder during push operations and the destination folder during pull operations.

The following table describes the options available in the context menu in the **Local file system** view:

| **Command** | **Description** |
| --- | --- |
| Push | Pushes files from the Host PC to the selected workspace. Refer to [Push Files to a Target Workspace Using Workspace Explorer](push-files-to-a-target-workspace-using-workspace-explorer.html) to target for more information. |
| Mirror push | Prepopulate the system managed host mirror workspace with the selected files/folders. Refer to [Mirror Push Files Using Workspace Explorer](mirror-push-files-using-workspace-explorer.html) for more information. |
| Deploy | Populates the currently selected workspace with files and directories defined by a GP5 File.  Note: Can also launch the associated `.elf` after the deploy process has been completed. Refer to [Deploy Files Using Workspace Explorer](deploy-files-using-workspace-explorer.html) for more information. |

Note:

Commands in the **Local file system** view are in addition to the regular Windows context menu commands.

## Target Workspace View

The **Target workspace** view shows the contents of the currently selected workspace.

The currently selected folder is used as the destination folder during a push operation.

The following table describes the options available in the context menu in the **Target workspace** view:

| **Command** | **Description** |
| --- | --- |
| Pull | Pulls files from the selected workspace to the Host PC. Refer to [Pull Files from a Target Workspace Using Workspace Explorer](pull-files-from-target-workspace-using-workspace-explorer.html) for more information. |
| Delete | Deletes any files or folders that are no longer required. Refer to [Delete](managing-workspaces-in-workspace-explorer.html#workspace-explorer-users-guide_1_2__section_mnk_lcp_chc) for more information. |
| Copy | Copies selected files in order to move them to another location within the workspace structure.  Equivalent to Windows **Copy** command.  Note: It is only possible to copy and paste files within the defined Workspace. |
| Paste | Pastes files that had previously been copied into a new location within the workspace structure.  Equivalent to Windows **Paste** command.  Note: It is only possible to copy and paste files within the defined Workspace. |
| Copy as path | Copies the path to a file relative to the workspace root to clipboard. This can be useful when performing [Diff](comparing-target-workspace-and-local-file-system-contents.html) commands, or [launching a ELF](specifying-the-correct-workspace-when-launching-an-elf.html). |
| Create folder | Creates a new sub-folder within the workspace structure. |

# Push Files to a Target Workspace Using Workspace Explorer

A Push operation enables the contents of a workspace to be populated or updated with files from the local file system. It is also possible to apply compression to files before commencing the Push operation. Pushing folders from Workspace Explorer is recursive.

To push files to the Target workspace:

1. In the **Local file system** view, select a source folder or set of files.
2. In the **Target workspace** view, select a destination folder.
3. On the **Home** tab, in the **File operations** section, select the required
   **Compression level** ().
4. On the **Home** tab, in the **File operations** section, click **Push** (), or in the **Local file system** view, select the file(s) and choose **Push files** from the context menu.
5. Check the size and compression level (if set), then click **OK**.

After completion, the workspace view will reflect the transferred contents.

Note:

Canceling the operation does not remove any files that have already been transferred. You will need to remove these files manually.

Note:

Once a workspace has been created and populated, any further file changes will only deal with the differences between the Host PC and Target versions of the workspace.

Note:

If you try to copy/paste an item from the **Local file system** to a **Target workspace** and the local copy is deleted before being pasted, a missing item error will occur.

# Mirror Push Files Using Workspace Explorer

Prepopulate the
System
Managed
Host
Mirror
with the files/folders selected in the **Local file system** view.

To mirror push files:

1. In the **Local file system** view, select a source folder or set of files.
2. On the **Home** tab, in the **File operations** section, click **Mirror push** (), or in the **Local file system** view, select the file(s) and choose **Mirror push** from the context menu.
3. In the confirmation dialog, check the number of item(s) to be mirrored is correct, then click **OK**.

# Deploy Files Using Workspace Explorer

Populates the selected workspace directory with files and directories defined in the specified GP5 File.

To deploy files:

1. On the **Home** tab, in the **File operations** section, click **Deploy** (), or in the **Local file system** view, select the file(s) and choose **Deploy** from the context menu.
2. In the **Deploy to workspace** dialog, in the **Deploy using the following GP5 file** drop-down list either navigate to the required GP5 File, or select a previously used GP5 file from the drop-down list.
3. Select the required destination from the **Destination workspace** drop-down list.
4. If required, in the **Launch path (Optional)** either navigate to the required `.elf` directory, or select a previously used location from the drop-down list.
5. Check the **Select this workspace after deploy** checkbox to move Workspace Explorer to the selected workspace.
6. Click **OK**.

Note:

If a System Managed Host Mirror has been selected, but no workspace has been configured, the workspace will be created as part of the Deploy process.

# Pull Files from a Target Workspace Using Workspace Explorer

Transferring files from a Target workspace to the local file system is known as a Pull operation. This follows the same process as a Push operation but in reverse.

Note:

Pull is not available for use with the System Managed Host Mirror.

To pull files from a Target:

1. In the **Target workspace** view, select a source folder or set of files.
2. In the **Local file system** view, select a destination folder.
3. On the **Home** tab, in the **File operations** section, click **Pull** (), or in the **Target workspace** view, select the file(s) and choose **Pull** from the context menu.

# Comparing Target Workspace and Local File System Contents

Workspace Explorer enables comparison of arbitrary paths within the Target workspace and local file system. There are two comparison modes available:

* **Accurate** - Considers files to be the same if their hash matches.
* **Quick** - Considers files to be the same if they have the same size and their modification times are within 10µs of each other.

Note:

Modification times may be up to 10µs different due to differences in filesystem timestamp storage precision between the Target and the Host PC.

The default is **Quick**.

It is possible to filter the produced list by newer files on either the Host PC, Target workspace or both, as well as by free text. You can select all, none, or some files to be synced between the Host PC and the workspace.

| **Number** | **Name** | **Description** |
| --- | --- | --- |
| 1 | White background | Identifies that the entry is a file. |
| 2 | Grey background | Identifies that the entry is a folder. |
| 3 | Diff status column | Visual marker of the difference between Host PC and Workspace.  If there is an arrow, this identifies that the file on the Host PC will be pushed to the Workspace.  Note: Roll over icon for a tooltip. |
| 4 | Green arrow | Identifies that file or folder has been selected for synchronization and that the file is currently only available on the Host PC. |
| 5 | Red arrow | Identifies that a file has been selected for synchronization and the file is different on the Host PC from the equivalent file in the workspace. |
| 6 | Red cross | Identifies that the file or folder has been selected for synchronization, but that the file only exists on the Workspace and is at risk of deletion. |
| 7 | [Compression Level](comparing-target-workspace-and-local-file-system-contents.html#workspace-explorer-users-guide_1_9__section_vbv_3bq_chc) | Identifies the compression level to be applied during the synchronization. |
| 8 | Empty square | Identifies a file or folder that has not been selected for synchronization. |
| 9 | Tick | Identifies a file selected for synchronization. |
| 10 | Filled square | Identifies a folder where some, but not all, of the contents of that folder have been selected for synchronization. |

To start comparing local filesystem and workspace contents:

1. In the **Local file system** view, select a folder to be compared.
2. In the **Target workspace** view, select the other folder to be compared.
3. On the **Home** tab, in the **Diff** section, click **Create Diff** ().
4. In the **Diff workspace** dialog, check the Host path and Workspace path entries are correct, then click **Create Diff**.

To change the comparison mode:

1. Select a folder in both the **Local file system** view and the **Target workspace** view.
2. On the ribbon, in the **Diff** section, click **Comparison mode** (), then select the required mode from the drop-down list.

To change the filtering of the Diff list:

|  |  |
| --- | --- |
|  | Select to show files only on Host PC. |
|  | Select to show files only on the Target. |
|  | Select to show files which are different between Host PC and the Target. |
|  | Select to turn the case-sensitivity of the Combo box on. |
| Combo box | Free text entry to filter, or select from the drop-down list. |

To select and sync files:

1. In the **Diff workspace** dialog, select the files to be synchronized from the list, or click **Check all** to select all the files in the list, or click **Uncheck all** to deselect all the files in the list.
2. Click **Sync Target**.

Note:

Pay attention to the arrow which shows the direction the files will be updated.

## Compression Level

**Compression Level** sets the level of compression to be used during the transfer in the range -4 to 9 with 0 being no compression.

* Negative values favor compression speed.
* Positive values favor compression ratio.

Note:

Compression level can only be set on [Push](push-files-to-a-target-workspace-using-workspace-explorer.html) or [Diff](comparing-target-workspace-and-local-file-system-contents.html) operations. When performing a sync after a Diff operation, it should be noted that any files being Pulled from the Target will not be compressed.

To set a compression level:

* On the **Ribbon**, in the **File operations** section, select the desired compression level from the **Compression Level** drop-down list.

Note:

The set compression level is displayed in the confirmation dialog before the process is triggered.

# Specifying the Correct Workspace When Launching an ELF

When launching an ELF there are several methods of ensuring that the correct workspace is specified.

| **Tool** | **Type** | **Link** |
| --- | --- | --- |
| `prospero-ctrl workspace` | CLI | [Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) |
| * Console Output * Controller Capture and Playback * Memory Analyzer * Remote Viewer * Screen Capture | GUI | [Target Management Applications UI Overview - Loading and Launching Applications](../TM_Applications_UI-Overview/loading-and-launching-applications.html) |
| Razor CPU Live | GUI | [Razor CPU Live User's Guide - Launching an ELF File or Installed Application](../Razor_Live-Users_Guide/launching-an-elf-or-package-file.html) |
| Razor CPU | GUI | [Razor CPU User's Guide - Performing Razor CPU Captures](../Razor_CPU-Users_Guide/performing-cpu-traces.html) |
| Debugger | GUI | [Debugger User's Guide - Working with DevKits for Debugging](../Debugger-Users_Guide/working-with-dev-kits-for-debugging.html) |
| Visual Studio Integration | GUI | [Visual Studio Integration for PlayStation®5 User's Guide - Configuring Visual Studio Project Settings](../Visual_Studio_Integration_for_PS5-Users_Guide/configuring-visual-studio-project-settings.html) |

Refer to
[Workspaces Overview](../Workspaces-Overview/__document_toc.html) for more information on workspaces.