# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-purpose-of-the-file-path-configuration-file.html

# Appendix: File Path Configuration File

This topic explains the role of the file path configuration file and how to create and use it. By using a file path configuration, you can modify folders of data files or overlay files without modifying the program itself.

# Purpose of the File Path Configuration File

A file path configuration file is a setting file for instructing the path of a working directory and overlay settings for program execution. By appropriately changing the file path configuration file and starting the program, it will be possible to change the data folder to be accessed to another directory or to load an overlaid file from a host PC without changing the program.

A file path configuration file can set the following.

* Root directory of a file set (example: working directory of an application file set)
* Save data root directory
* Additional content directories (not yet supported)
* Overlays (up to 8)
* Redirect of sce\_sys and sce\_module

For details about application and additional content file configurations, refer to the [Application Content Overview](../Application_Content-Overview/__document_toc.html) document.

For details about file structure of save data, refer to [SaveData Library Overview - Save Data - Save Data Format](../SaveData-Overview/save-data-format.html).

# Creation of the File Path Configuration File

A file path configuration file is a text file written in UTF-8. The linefeed character is CR+LF. Each line comprises an item name, the separator "`=`", and the item value (the `Parameter` section).

```
Item + "=" + Parameter + CRLF
```

When not setting a value, leave the `Parameter` section blank as shown in the following example. (However, an error will occur when values that need to be set are left blank.)

```
overlayType=
```

Use the extension ".prosperopath" for file path configuration files.

Lines starting with "`#`" will be handled as comments and will be ignored.

```
# This line is handled as a comment and ignored.
```

The file size of a file path configuration file must be within 32 KiB including comment lines.

## File Path Configuration File Example

A description example of a file path configuration file is shown in the following.

```
version=3 
rootDir=/host/C:\game\app 
savedataRootDir=/host/C:\game\savedata 
sceSysDir=/host/C:\game\sce_sys 
sceModuleDir=/host/C:\game\sce_module 
# overlay1 
overlayType=TRANSLUCENT 
overlaySrc=/host/C:\data\music 
overlayDst=/music 
# overlay2 
overlayType= 
overlaySrc=/launch/data/stage1 
overlayDst=/data/stage 
# overlay3 
overlayType=OPAQUE 
overlaySrc=/launch/data/stage2/a.txt 
overlayDst=/data/stage/a.txt
```

Note:

Another example of a file path configuration file is provided as a sample in the following path.

* target\samples\sample\_code\target\_management\api\_mappingfile\basic\app\configuration.prosperopath

## Setting Items

The items that can be set in a file path configuration file are as follows. Overlay settings will be evaluated and applied in order from the top.

| **Item** | **Description** |
| --- | --- |
| `version` | Configuration file format version  Always write this in the first line. Specify 2 or 3 for the value. |
| `rootDir` | File set root directory  Always write this in the second line.  The path must start with "`/host/`" or "`/launch/`" and be a valid path. In addition, there must be no overlap with the directory tree specified with `savedataRootDir`. |
| `sceSysDir` | sce\_sys directory  The path must start with "`/host/`" or "`/launch/`".  Supported only in Version 3. If specified in Version 2, it will cause an error. |
| `sceModuleDir` | sce\_module directory  The path must start with "`/host/`" or "`/launch/`".  Supported only in Version 3. If specified in Version 2, it will cause an error. |
| `overlayType` | Type of the first overlay  "`OPAQUE`" or "`TRANSLUCENT`" can be specified.   * `OPAQUE`: Completely replace the destination path directories/files with the source path directories/files. * `TRANSLUCENT`: When reading, the source path will first be checked, and then the specified file will be read if it exists. If it does not exist, the destination path will be checked.   `TRANSLUCENT` will be handled as the default when this specification is omitted. |
| `overlaySrc` | Source path of the first overlay (path to overlay)  The path must start with "`/host/`" or "`/launch/`".  If not setting a source path, do not set `overlayDst` either. |
| `overlayDst` | Destination path of the first overlay (path that will be overlaid)  The path must start with "`/`" but cannot be "`/`" itself.  If not setting a destination path, do not set `overlaySrc` either. |
| `overlayType`,  `overlaySrc`,  `overlayDst` | Overlay setting of the Nth overlay  Repetition of `overlayType`, `overlaySrc`, and `overlayDst`. Up to eight sets. |
| `…` |  |
| `savedataRootDir` | Save data root directory  The path must start with "`/host/`" or "`/launch/`". In addition, there must be no overlap with the directory tree specified with `rootDir`. |

## version

The current format version is 3. Format version 3 or 2 can be specified.

## rootDir

Specify the root directory of the file set. A valid directory must always be specified for this item. The directory specified here for an application file set will be set as the working directory and will be the root directory accessed by the program with "`/app0/`". A working directory can be specified with Target Manager, prospero-run, Razor CPU, and the Visual Studio debugger, but the root directory specified with this item will be prioritized when a file path configuration file is used. (When neither is specified, the same directory as the executable file will be set as the working directory.)

## sceSysDir

By specifying this item, it is possible to replace the sce\_sys directory ("/app0/sce\_sys"). The system reads files such as param.json from this directory and applies them to the application that has launched.

## sceModuleDir

By specifying this item, it is possible to replace the sce\_module directory ("/app0/sce\_module"). System libraries are loaded from this directory.

## Path Describing

When specifying a path on the host PC file system, write the absolute path in Windows style.

Example: "`/host/C:\data\video`"

The length of any file path must be `SCE_KERNEL_PATH_MAX - 1` bytes or less on the target after any Windows-style environment variables included in the path have been expanded. Similarly, the lengths of file names must be `SCE_KERNEL_NAME_MAX` or shorter. If a file path that exceeds these lengths is provided, the program will fail to start. File path descriptions that relatively indicate a parent directory with "..\" or indicate the current directory with ".\" cannot be used as file path descriptors.

Windows environment variables can be included when specifying a path on the host PC file system. Environment variables are applied once upon program startup. There will be no effect on the program when environment variables are modified after they have been applied.

Note:

Even if a path can be used in a file path configuration file, there are cases where the path cannot be used during package creation. For details, refer to [GP5 File Specification - Specifications of the GP5 File (\*.gp5) - Path Restrictions](../GP5-Specification/path-restrictions.html).

## Save Data Root Directory

Save data directories are data save areas accessed by programs as "`/savedata0/`" to "`/savedata15/`". The actual path is as follows.

`Save data root directory\user ID directory\savedata\save data title ID directory\save data directory`

When `savedataRootDir` is specified in a file path configuration file, the specified directory will be the save data root directory (parent directory of the user ID directories), and the SaveData library will write save data to the above path in that root directory. (For the write destination when a specification is not made with the file path configuration file, refer to [SaveData Library Overview - Handling of Save Data during Development - Save Data Write Destinations](../SaveData-Overview/save-data-write-destinations.html).)

Note:

A directory belonging to a lower tree of the directory specified in `rootDir` cannot be specified for `savedataRootDir`. In turn, a lower directory of the directory specified in `savedataRootDir` cannot be specified for `rootDir`. If one is specified, the behavior is undefined.

## Overlay

There are two overlay methods: replacing the content of a directory with the content of another directory (`OPAQUE`) and overlaying the content of a directory with the content of another directory (`TRANSLUCENT`). Up to 8 overlays can be set. An error will occur if 9 or more are set.

For the overlay settings, specify the type of overlay with overlayType, and a source path and destination path for that type with overlaySrc and overlayDst, respectively. An overlay included earlier in the file path configuration file will be prioritized. The settings must consist of the type, the source path, and the destination path. The order of these three items is fixed.

## "/launch/" Virtual Device

To improve the portability of file path configuration files, it is possible to use a "`/launch/`" virtual device in configuration files. The path where the executable file is located will be assigned for `/launch/`. For example, if an executable file is "`/host/C:\project\game.self`", "`/launch/assets`" will be extracted in "`/host/C:\project\assets`".

The file path size restriction will be applied after the extraction of `/launch/` has been performed.

## Restrictions

* In cases where a Windows environment variable is used (for example) to access the same file in the host file system through another path, unexpected problems such as data inconsistencies may occur.
* Additional overlays cannot be applied for a directory with an overlay already applied; the same is true for its parent or subdirectory.

  For example, if "`/app0/data/asset1`" is overlaid with "`/host/C:\data\asset1`", it will not be possible to apply another overlay to its parent directory, "`/app0/data`". Another overlay also cannot be applied if an overlay is already applied to "`/app0/data/asset1`" itself.

# File Path Configuration File Usage

A file path configuration file will be automatically loaded upon program start when a file with the filename "configuration.prosperopath" exists in the same directory as the executable file.

In addition, when a program is started from Target Manager, prospero-run, or the Visual Studio debugger, you can specify a file path configuration file from an arbitrary location with each of the following methods.

## Specifying with Target Manager

1. Select [Load Executable]
2. Specify a configuration file in [Mapping file path] at the bottom of the [Load Executable] window

## Specifying with prospero-run

Specify a configuration file with the `/mappingFile:<path>` option

## Specifying with the Visual Studio debugger

1. Select [Properties] for the project to configure
2. Select [Debugging] in [Configuration Properties]
3. Specify a configuration file in [Mapping File]

Note that program load will fail if there is an error in the configuration file. The cause and location of the error will be output to the console.