# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-support-for-changes-in-ssd-read-write-speeds.html

# Basic Information on File Access

This topic provides basic information about file access and describes development support features. It discusses types and characteristics of writable storage, methods of high-speed file access using the APR library, and storage particular to the development environment. Be aware that what is described here are hardware specifications that are reinforced for development on DevKits and may differ from the specifications for TestKits and retail units.

# Writable Storage

There are four types of storage that can be written to by applications: the save data area, the download data area, the temporary data area, and StreamWrites. The maximum size and data retention period of each storage type are as follows.

| **Storage** | **Maximum size** | **Data retention period** |
| --- | --- | --- |
| Save data area | 1 GiB per user | Until deleted by the user (will not be deleted even when the application is uninstalled) |
| Download data areas | 1 GiB per application | Until the application is uninstalled |
| Temporary data area | 1 GiB per application | Until the application is terminated (there is also the possibility of deletion if another application is started) |
| StreamWrite | 2 GiB per application | Until the application is terminated |

In addition to the above, each type of storage has its own role and characteristics. For details about the storage areas, refer to the [Application Content Overview](../Application_Content-Overview/__document_toc.html) document. StreamWrites differ considerably from other storage areas and have the following characteristics:

* Not affected by SSD write throttling (described later)
* Have a ring-buffer structure
* Can be operated only using a dedicated API

For details about StreamWrites, refer to the [Kernel Overview](../Kernel-Overview/__document_toc.html) document.

There are also types of storage that can be used only during development - for these, refer to the "[File Access During Application Development](ps5-file-access-during-application-development.html)" section later in this document.

# Tips for High-Speed File Access

## APR (Asynchronous Package Reader)

The APR library provides a feature for reading files from an application package in a DevKit/TestKit's console storage/M.2 SSD storage and for executing them asynchronously and at high speed with the support of dedicated hardware. File read processing can be batch-set as commands to the command buffer, and the commands can be executed at the same time.

In addition, the APR library is equipped with a feature to easily enable coordinated operation with the AMM (Asynchronous Memory Mapper) library and the Agc library.

For details, refer to the [APR Library Overview](../APR-Overview/__document_toc.html) document.

# Support for Changes in SSD Read/Write Speeds

SSD read/write speeds vary depending on various factors, such as when access occurs and whether SSD write throttling is in effect. Applications must be implemented so that it is not a problem when the bandwidth or latency for file access fluctuates.

## SSD Write Throttling

SSD write throttling refers to a bandwidth limiting mechanism for ensuring a longer lifespan for the SSD. For details about this feature, refer to [Kernel Overview - File System - SSD Write Throttling](../Kernel-Overview/ssd-write-throttling.html).

## Slow SSD Mode

This feature reduces SSD read/write speeds to about what would be the worst-case scenario in a retail unit. For details about this feature, refer to [Kernel Overview - File System - Slow SSD Mode](../Kernel-Overview/slow-ssd-mode.html).

# File Access During Application Development

## Accessing Console Storage/M.2 SSD Storage

An application can access the console storage/M.2 SSD storage via the `/app0` mount point using the workspace described below. In addition, `/devlog/app` is provided as a directory for developing and debugging applications.

**System-Managed Host Mirror Workspaces**

When a directory on the host PC is set as the working directory, the mirroring of the system-managed host mirror workspace will automatically synchronize the files on the host PC with the console storage. An application will be able to access files in high speed and use the APR library without performing any special operation.

A working directory can be set for each Visual Studio project. Open the project's Properties window and select [Configuration Properties] > [Debugging]; the "Working Directory" setting item will be displayed. When you set a directory here, the system will mount the directory as `/app0`. The working directory will be automatically applied for the project once it is set.

Refer to the [Workspaces Overview](../Workspaces-Overview/__document_toc.html) document and [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html) document for details about system-managed host mirror workspaces.

**Standalone Workspaces**

It is possible to create a standalone workspace within the console storage/M.2 SSD storage in advance, copy data from the host PC to this standalone workspace, and specify it as the `/app0` directory. Refer to the [Workspaces Overview](../Workspaces-Overview/__document_toc.html) document and [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html) document for details about standalone workspaces.

Note:

Application file read performance depends on the workspace and package. Use a package when checking performance at the final stages of application development.

**/devlog/app**

`/devlog/app` is provided as a directory for developing and debugging applications. Only when the Release Check Mode is Development Mode or Assist Mode, it is possible to write, read, and delete from the application, and to read and delete from the host PC, at this directory. This directory can be used, for example, to write data for debugging to it from the application and to have this data read by the host PC.

Note:

The following restriction applies regarding timestamps of files and directories created under the `/devlog` directory.

* The last access time (`st_atime`) will always indicate the same time as whichever is newer of the two: the last data change time (`st_mtime` or the last file status change time (`st_ctime`).

Given this restriction, when only the last access time is specified when calling `sceKernelUtimes()` or `sceKernelFutimes()`, the last access time won't be updated. In addition, when the last access time and last data change time are specified to `sceKernelUtimes()` or `sceKernelFutimes()`, the last access time will be updated to the same time as whichever is newer of the two: the updated final data change time or the final status change time.

Use `/app0` or `/host` to write data from the host PC and have this data read by the application, opposite to `/devlog/app`.

Note:

The bandwidth of the console storage/M.2 SSD storage will be limited when the application is running in the background. (Refer to [Kernel Overview - File System - Notes Specific to the PlayStation®5](../Kernel-Overview/notes-specific-to-the-ps5.html) for details.)

## Accessing Storage on the Host PC

Applications can access files on the host PC via the `/host` mount point.

Access to `/host` is restricted to debugging purposes and is possible only when the Release Check Mode is set to Development Mode or Assist Mode. `/host` can correspond to both an absolute path and a relative path on the host PC.

* Absolute path example
  + `/host/C:\data\myvideo.dat` (points to `c:\data\myvideo.dat` regardless of the `fsroot` setting)
* Relative path example
  + `/host/mymusic.dat` (relative path from `fsroot`; for example, points to `c:\data\mymusic.dat` if "`c:\data`" is set to `fsroot`)

Note:

An environment variable can be specified after `/host/` as follows.

```
sceKernelStat("/host/%SystemDrive%/logfile.txt", &sb);
```

For example, if "C:" is set to the `SystemDrive` environment variable, this specification will be replaced as follows.

```
sceKernelStat("/host/C:/logfile.txt", &sb);
```

## Accessing USB Drives

Applications can access FAT32- or exFAT-formatted USB drives connected to a DevKit/TestKit. Using this method to access USB drives is restricted to application development and debugging purposes and is possible only when the Release Check Mode is set to Development Mode or Assist Mode.

A USB drive will be automatically mounted by the system to one of the mount points `/usb0` to `/usb7`. When the Release Check Mode is set to Development Mode or Assist Mode, unmounted mount points will appear to applications as empty directories. When the Release Check Mode is set to Release Mode, the mount points themselves will not exist.

## GP5 File

A GP5 file can be created and used during development to define how files will be mapped from the host file system to `/app0` and `/addcont*`. You can specify a layout of files and directories within `/app0` and `/addcont*` of your choosing with this file. For details about using GP5 files during development, refer to the [Workspaces Overview](../Workspaces-Overview/__document_toc.html) and the [GP5 File Specification](../GP5-Specification/__document_toc.html).

## File Path Configuration Files

On a DevKit/TestKit with the Release Check Mode set to Development Mode or Assist Mode, you can use a file path configuration file to permit flexible placement of files during development. By writing a file path configuration file in the predetermined format, operations such as the following will be possible.

* Setting the root directory to a file set or save data
* Redirecting working directory or save data root directory (shared parent directory for `/savedata0` to `/savedata15`) access to an arbitrary directory under `/host`
* Overlaying an arbitrary directory or file under `/host` onto an arbitrary directory or file under `/app0`. Up to eight overlays can be set, and it is possible to select `OPAQUE` (directory content will be completely replaced) or `TRANSLUCENT` (directory content will be merged) for each.
* The above redirect and overlay can be specified with a relative path by using a `/launch` that is based on the executable file.

By using these features, it will be possible to change data sets accessed by an application without changing programs, merge files split over multiple directories without moving/copying for testing, and more.

For details, refer to "[Appendix: File Path Configuration File](ps5-appendix-file-path-configuration-file.html "This topic explains the role of the file path configuration file and how to create and use it. By using a file path configuration, you can modify folders of data files or overlay files without modifying the program itself.")".