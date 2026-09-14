# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/using-gp5-files-in-workspaces.html

# Using GP5 Files in Workspaces

## Purpose of the GP5 File

A GP5 File can be used during development to describe how files are mapped from the Host PC file system into `/app0/` and `/addcont*`. The GP5 File can specify arbitrary layouts of files and directories within `/app0` and `/addcont*`.

The publishing tools for package creation accept a GP5 File as input. This enables the same GP5 File used in development to be used for package creation.

For more detail on GP5, refer to [GP5 File Specification](../GP5-Specification/__document_toc.html).

If the required assets are not stored on the Host PC but on a server such as a database, you can still organize `/app0/` and `/addcont*` into a workspace by using Workspace plugins. Refer to [Workspace Plugins Reference](../Workspace_Plugins-Reference/__document_toc.html) for more information.

## Formatting of GP5 Files

A GP5 File is an XML document that uses the extension "`.gp5`".

## GP5 File Example

An example GP5 File is shown below.

```
<psproject fmt="gp5" version="1000">
  <volume>
    <volume_type>prospero_app</volume_type>
  </volume>
  <rootdir src_path="/">
    <dir dst_path="assets" src_path="c:\game\assets"/>
  </rootdir>
</psproject>
```

A sample program is included in the SDK that demonstrates GP5 usage and can be found in the `%SCE_PROSPERO_SDK_DIR%\target\samples\sample_code\target_management\demo_gp5file\` directory.

For further details about the XML structure of GP5 Files, refer to [GP5 File Specification - Specifications of the GP5 File (\*.gp5)](../GP5-Specification/specifications-of-the-gp5-file-gp5.html).

## /app0/ Layout

The layout of `/app0/` is specified by the `<rootdir>` element and its children.

Each element in the `<rootdir>` tree maps a path on the Host PC filesystem (`src_path`) to a path within `/app0/ (dst_path)`. The files within `src_path` are recursively mapped into the `dst_path`.

The `dst_path` of `<rootdir>` is implicitly set to `/app0/`. The `dst_path` of other elements are relative to their parent element's `dst_path`.

Files and directories that are implicitly included from one mapping may be hidden by its child mappings. When a child mapping explicitly uses a `dst_path` that overlaps with an implicitly included file or directory, the explicit mapping takes precedence.

## Specifying a GP5 File when Launching a Process

A GP5 File can be specified when a process is launched.

To specify a configuration file when launching a process using `prospero-run` or `prospero-ctrl`, use the `/gp5File:<GP5_File>` option.

For information on how to specify a GP5 File at launch from within the application, refer to the following user's guides:

| **Tool** | **Type** | **Link** |
| --- | --- | --- |
| Workspace Explorer | GUI | [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html) |
| Target Manager API | CLI | * [Target Manager API Overview](../Target_Manager_API-Overview/__document_toc.html) * [Target Manager API Reference](../Target_Manager_API-Reference/__document_toc.html) |
| * Console Output * Controller Capture and Playback * Memory Analyzer * Remote Viewer * Screen Capture | GUI | [Target Management Applications UI Overview - Loading and Launching Applications](../TM_Applications_UI-Overview/loading-and-launching-applications.html) |
| Razor CPU Live | GUI | [Razor CPU Live User's Guide - Launching an ELF File or Installed Application](../Razor_Live-Users_Guide/launching-an-elf-or-package-file.html) |
| Razor CPU | GUI | [Razor CPU User's Guide - Performing Razor CPU Captures](../Razor_CPU-Users_Guide/performing-cpu-traces.html) |
| * Debugger * Visual Studio Integration | GUI | [Debugger User's Guide - Working with DevKits for Debugging](../Debugger-Users_Guide/working-with-dev-kits-for-debugging.html) |

## Limitations

* GP5 Files support up to 256 different `<file>` or `<dir>` mappings.
* The `src_path` attribute of a `<dir>` element cannot specify the same path on the Host PC as the `src_path` attribute of its parent element.
* GP5 Files cannot be used with File Path Configuration files because they both handle folder remapping. For more information, refer to [Programming Startup Guide - Appendix: File Path Configuration File](../Programming-Startup_Guide/ps5-appendix-file-path-configuration-file.html).
* When a parent element implicitly includes a directory, an explicit `<file>` element cannot be used to hide it. Likewise a `<dir>` element cannot be used to hide a file.
* The `content_config_label` attribute is not configurable when launching a process with the System Managed Host Mirror. The `primary` label will always be used.