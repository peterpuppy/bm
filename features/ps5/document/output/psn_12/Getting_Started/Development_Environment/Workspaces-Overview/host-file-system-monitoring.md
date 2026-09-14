# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/host-file-system-monitoring.html

# Workspaces Overview Introduction

A workspace is an area of high speed storage on a Target that is used during development
to contain the files and directories that are available to the running process in
`/app0/`.

There are two types of workspaces available:

* [Standalone](using-standalone-workspaces.html)
  - a [Standalone](using-standalone-workspaces.html) workspace is an
  area of the
  Target's
  high speed storage that you define and manage manually. All files must exist on a
  [Standalone](using-standalone-workspaces.html) workspace before
  the process requiring them is run. You must explicitly set up a standalone
  workspace.
* [System
  Managed Host
  Mirror](system-managed-host-mirror.html)
  - A [System Managed Host Mirror](system-managed-host-mirror.html)
  workspace is an area of the
  Target's
  high speed storage that duplicates an area of the Host PC's storage.
  System Managed
  Host
  Mirror
  workspaces can be created when the process utilizing the workspace first requires
  files from the Host PC, or they can be set up beforehand using a GP5 file. Files are
  copied to the workspace from the Host PC's storage as the process requests
  them.

For
more information, refer to the **List of workspace commands**
section of [Target Manager CLI User's Guide -
Controlling
Targets Using the Command Line - Controlling Targets with
prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) and [Workspace Explorer User's
Guide](../Workspace_Explorer-Users_Guide/__document_toc.html).

Note:

Only [Standalone](using-standalone-workspaces.html)
workspaces are supported on M.2 SSD storage.

## Hardware Support

The following table shows which features are supported by DevKits and TestKits,
collectively known as Targets, when in various modes.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **DevKit** | | | **TestKit** | |
| **Development** | **Assist** | **Release** | **Assist** | **Release** |
| Fast file transfer | **Yes** | **Yes** | **No** | **No** | **No** |
| Workspace Overlay | **Yes** | **No** | **No** | **No** | **No** |

For more information on configuring DevKits and TestKits, refer to:

* [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html)
* [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html)

## Workspace Feature Support

Features supported by workspace type

| Features | System managed host mirror workspace (Console storage only) | Standalone workspace |
| --- | --- | --- |
| Auto mirroring | **Yes** | **No** |
| ★Workspace(Application launch by the system software) | **No** | **Yes** |
| AC support | **No** | **Yes** |
| Fast file transfer | **Yes** | **Yes** **(Console storage only)** |
| Workspace library | **Yes** | **Yes** |
| Workspace Management API | **No** | **Yes** |
| Workspace Overlay | **No** | **Yes** |
| Workspace Plugins | **Yes** | **Yes** |

Workspace types and features supported by storage type

| Workspace types and features | Console storage | M.2 SSD storage |
| --- | --- | --- |
| System managed host mirror workspace | **Yes** | **No** |
| Fast file transfer | **Yes** | **No** |
| Use of standalone workspaces created on other development machine by M.2 SSD relocation | **No** | **Yes** |

## Host Tool Support for Workspaces

GUI and CLI host tools are provided to manage workspaces and their contents:

* **Workspace Explorer**, is an easy-to-use GUI tool that covers most workspace
  functions.
* `prospero-ctrl workspace`, is a CLI tool that enables workspace
  support to be integrated into an asset build pipeline.

For more information on setting up and using these tools, refer to:

* [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html)
* [Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html)

Workspace support is also included in the Target Manager API to facilitate the
creation of custom tools. For more information, refer to [Target Manager API Overview](../Target_Manager_API-Overview/__document_toc.html) and [Target Manager API Reference](../Target_Manager_API-Reference/__document_toc.html).

All of the TMUI applications support launching applications from Workspaces. Refer to
[Target Management Applications UI Overview -
Loading and Launching Applications](../TM_Applications_UI-Overview/loading-and-launching-applications.html) for more information.

Razor CPU Live supports launching applications from Workspaces. Refer to [Razor CPU Live User's Guide - Launching an ELF File or Installed Application](../Razor_Live-Users_Guide/launching-an-elf-or-package-file.html) for more information.

Razor CPU supports launching applications from Workspaces. Refer to [Razor CPU User's Guide - Performing Razor CPU Captures](../Razor_CPU-Users_Guide/performing-cpu-traces.html) for more information.

The Debugger, using Visual Studio Integration, supports launching applications from Workspaces. Refer to [Visual Studio Integration for PlayStation®5 User's Guide](../Visual_Studio_Integration_for_PS5-Users_Guide/__document_toc.html) for more information.

# Using Standalone Workspaces

Using a Standalone workspace requires you to manually manage the files on the workspace to support the process.

All required files must be manually pushed to the Target, destroyed and updated using the
CLI or GUI tools.
Refer
to the **List of workspace commands** section of
[Target Manager CLI User's Guide -
Controlling
Targets Using the Command Line - Controlling Targets with
prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) and [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html) for more information.

Note:

Files to be used by a process via `/app0/` and `/addcont*` on a Standalone workspace must exist on the Target before being accessed.

Note:

Host PC filesystem reparse points and hard links are supported with some limitations. Refer to
[Appendix C - Reparse Points and Hard Links Support](workspaces-overview-appendix-c-reparse-points-and-hard-links-support.html) for more information.

Note:

If the required assets are not stored on the Host PC but on a server such as a database, you can still organize `/app0/` and `/addcont*` into a Standalone workspace by using Workspace plugins. Refer to [Workspace Plugins Reference](../Workspace_Plugins-Reference/__document_toc.html) for more information.

# System Managed Host Mirror

When a process is run against a
System
Managed
Host
Mirror
workspace, files are transferred from the Host PC to the workspace as they are
requested.

Using a System Managed Host Mirror workspace requires a **host working directory** or **GP5 File** to be specified at process launch time. Because files used by a process via `/app0/` must exist on the workspace, any files accessed via `/app0/` will automatically be mirrored to the Target file system. The mirroring process detects when a file is present on the Host PC but not on the Target, and then automatically transfers the file to the Target. Any transferred files will remain on the Target until they are either updated or deleted on the Host PC.

A System Managed
Host
Mirror
workspace is created at process launch time if it does not already exist. The workspace
is named using the Target's GUID value. You will need the GUID value to use certain CLI
`prospero-ctrl workspace` commands.
Refer
to the **List of workspace commands** section of [Target Manager
CLI User's Guide -
Controlling
Targets Using the Command Line - Controlling Targets with
prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) for more information.

There are two mirroring modes available: "Whole file mode" and "On-demand mode". Refer to
[Mirroring Modes](mirroring-modes-for-system-managed-host-mirror-workspaces.html) for more information.

Files can also be pushed or deployed to the Target in advance of running the process:

| Method | Description | For information |
| --- | --- | --- |
| Mirror push files | Pre-populate the System Managed Host Mirror workspace with the files/folders selected in the **Local file system** view of Workspace Explorer or via the command line. | Refer to [Workspace Explorer User's Guide - Using Workspace Explorer - Mirror Push Files Using Workspace Explorer](../Workspace_Explorer-Users_Guide/mirror-push-files-using-workspace-explorer.html) and the `prospero-ctrl workspace mirror-push` command in the **List of workspace commands** section of [Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) for more information. |
| Mirror deploy files | Populates the selected workspace directory with files and directories defined in a specified GP5 File. | Refer to [Workspace Explorer User's Guide - Using Workspace Explorer - Deploy Files Using Workspace Explorer](../Workspace_Explorer-Users_Guide/deploy-files-using-workspace-explorer.html) and the `prospero-ctrl workspace mirror-deploy` command in the **List of workspace commands** section of [Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) for more information. |

A System Managed Host Mirror workspace can be viewed in Workspace Explorer where it is displayed as a read-only workspace named "**System Managed Host Mirror**". Refer to [Workspace Explorer User's Guide - Using Workspace Explorer - Deploy Files Using Workspace Explorer](../Workspace_Explorer-Users_Guide/deploy-files-using-workspace-explorer.html) for an example.

Note:

The mirroring process can only transfer files stored on the Host PC. Files stored on network drives cannot be mirrored to the Target.

Note:

System Managed Host Mirror workspaces cannot use M.2 SSD storage.

Note: To view the GUID of the current System Managed Host Mirror workspace, use `prospero-ctrl workspace mirror-guid`. Refer to the **List of workspace commands** section of [Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html) for more information.

Note:

When calling APR resolve APIs such as `resolveFilePathsToFileIds()`, performance can be improved by passing multiple paths instead of making separate API calls for each individual path. This is particularly useful when using System Managed Host Mirror workspaces because communication between the Host PC and the Target is reduced. Refer to
[APR Library Reference](../APR-Reference/__document_toc.html) for more information on how to change your code to support multiple paths in each resolve call.

Note:

If the connection with the Host PC is interrupted, subsequent attempts to mirror data from the Host PC will fail, resulting in a `SCE_KERNEL_ERROR_EWSMIRROR` error. The process needs to be terminated to recover from the error. Refer to
[Appendix A - Workspace Specific Errors](workspaces-overview-appendix-a-workspace-specific-errors.html) for more information.

Note:

Host PC filesystem reparse points and hard links are supported with some limitations. Refer to
[Appendix C - Reparse Points and Hard Links Support](workspaces-overview-appendix-c-reparse-points-and-hard-links-support.html) for more information.

Note:

If the required assets are not stored on the Host PC but on a server such as a database, you can still synchronize `/app0/` by using workspace plugins. Refer to [Workspace Plugins Reference](../Workspace_Plugins-Reference/__document_toc.html) for more information.

# Host File System Monitoring

Target Manager Server monitors the set of files on the Host PC that have been mirrored to the Target workspace. Differences between the Host PC file system and the Target are reconciled before a process is spawned. Updated file content can be made visible to a running process using [hot loading](hot-loading-support-for-workspaces.html).

Note:

Changes made to the Host PC file system through `/host/` by a process running on the Target are not monitored by Target Manager Server. Differences between files caused by such an update will not be reconciled.

# Mirroring Modes for System Managed Host Mirror Workspaces

There are two mirroring modes available for a System Managed Host Mirror workspace:

* [Whole file mode](mirroring-modes-for-system-managed-host-mirror-workspaces.html#workspaces-overview_0_2_2__section_xld_jxy_ygc) (default)
* [On-demand mode](mirroring-modes-for-system-managed-host-mirror-workspaces.html#workspaces-overview_0_2_2__section_psg_kxy_ygc)

The mirroring mode can be specified when a process is launched. Refer to
[Host Tool Support for Workspaces](workspaces-overview-introduction.html#workspaces-overview_0__section_ktf_shy_ygc) for further information.

## Whole File Mode

When a file that requires mirroring to the Target is either opened by `sceKernelOpen()` or resolved using APR, the entire contents of the file will be transferred to the Target before the `sceKernelOpen()` or the APR resolve operations return.

Whole file mode ensures that file read performance reflects the capabilities of the Target storage by caching all the file data on the Target before the first read occurs.

## On-Demand Mode

When a file that requires mirroring is either opened by `sceKernelOpen()` or resolved using APR, only the metadata of the file is transferred to the Target before the `sceKernelOpen()` or the APR resolve operations return.

Subsequent APR reads or calls to SDK functions, for example `sceKernelRead()` and asynchronous I/O read, will only transfer the portion of the file's contents to the Target required to fulfill the read request. This data is cached on the Target and further reads to this portion of the file do not require a round-trip to the Host PC.

On-demand mode reduces the initial time spent transferring file data to the Target by spreading the cost of mirroring a file across several file read operations. This mode is suited to workspaces containing large files that do not need to be read in their entirety during every execution of a process, for example when the data read by the process is packed into archive files.