# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/limitations-of-workspace-overlay.html

# Workspace Overlay

Workspace Overlay enables you to temporarily apply changes to an application package
without having to re-build the application package or build a patch package.

Note: Workspace Overlay is only supported on DevKits in Development
Mode.

When Workspace Overlay is selected at application launch, a
Standalone
workspace is given priority and the file read destination is chosen from either the
application package or the
Standalone
workspace on a file-by-file basis.

  
  

Workspace Overlay supports directories and the file read destination is selected
according to the same rules.

  
  

Note:

You can overlay all files and directories in the application package except
`/app0/sce_sys`.

Even with Workspace Overlay active, the file reading speed is the same as that of a single
application package, and there is no overhead. However directory and file path access
has the overhead of accessing both the Standalone workspace and the application
package.

The maximum amount of uncompressed data supported by Workspace Overlay is the same as the upper limit supported by workspaces in [Development mode](maximum-uncompressed-data-capacity-in-development-mode.html).

# Configuring Workspace Overlay

Before applying a Workspace Overlay to an application package you must push or deploy all the files and directories you wish to use to a Standalone workspace using Workspace Explorer or the command line. For more information,
refer to:

* [Workspace Explorer User's Guide - Using Workspace Explorer - Deploy Files Using Workspace Explorer](../Workspace_Explorer-Users_Guide/deploy-files-using-workspace-explorer.html).
* [Workspace Explorer User's Guide - Using Workspace Explorer - Push Files to a Target Workspace Using Workspace Explorer](../Workspace_Explorer-Users_Guide/push-files-to-a-target-workspace-using-workspace-explorer.html).
* `workspace deploy` and `workspace push` commands
  in the **List of workspace commands** section of [Target Manager CLI User's
  Guide - Controlling Targets
  Using
  the
  Command
  Line
  - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html).

# Applying Workspace Overlay

When the files and directories you wish to use have been successfully added to the Standalone workspace, you can then instruct the
**Launch Application** process to overlay content from the workspace when launching the packaged application.

For more information on applying Workspace Overlay when launching applications, refer to:

* **Advanced Launch Application Options** under [Target Manager GUI User's Guide - Using Target Manager to Manage Files and Targets - Loading and Launching Applications](../Target_Manager_GUI-Users_Guide/004_loading-and-launching-applications.html).
* `/storage` and `/workspaceOverlay` commands in
  **List of Options** section of [Target Manager CLI User's Guide -
  Controlling Targets
  Using
  the
  Command
  Line
  - Running Executables with prospero-run](../Target_Manager_CLI-Users_Guide/running-executables-with-prospero-run.html).
* `application start` command in **List of application
  commands** section of [Target Manager CLI User's Guide - Controlling
  Targets
  Using
  the
  Command
  Line
  - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html).
* **VSI Project Settings - PS5 Application Debugger** in **VSI Project Settings - Debugging** section of [Visual Studio Integration for PlayStation®5 User's Guide - Configuring Visual Studio Project Settings - Project Settings in Visual Studio](../Visual_Studio_Integration_for_PS5-Users_Guide/project-settings-in-visual-studio.html)
* `--storage` and `--workspace-overlay` commands in
  **Capture Arguments** section of [Memory Analyzer User's Guide - Launching Memory Analyzer via the Command Line - Using the prospero-mat Command Line Tool](../Memory_Analyzer-Users_Guide/using-the-prospero-mat-command-line-tool.html).

# Logging and Debugging with Workspace Overlay

By default the `STDOUT` of the application will not show the file paths for any files overlaid from the Standalone workspace.

To pass the Workspace Overlay files to `STDOUT`:

1. Open **Target Settings** application
2. In the **Target Settings** application, change the **★Debug Settings - System - Enable Workspace Overlay path remapping log** setting to **On**.

Note: Enabling the logging of the Workspace Overlay files may
adversely impact performance.

# Limitations of Workspace Overlay

* Workspace Overlay only supports Development Kits in Development Mode.
* Media Apps are not supported.
* When running an application with Workspace Overlay, you cannot update any files in the associated Standalone workspace.
* The PlayGo feature does not affect files that exist only in a Standalone workspace because those files are always accessible.
* Workspace Overlay cannot be used with the "`/app0/sce_sys`" directory. If the `/sce_sys` directory exists in the associated Standalone workspace, then the **Launch Application** process will fail.
  + To apply system parameters when launching applications, edit the param.json file being used by the **Launch Applications** process. Refer to [Param Editor User's Guide](../Param_Editor-Users_Guide/__document_toc.html) for more information.