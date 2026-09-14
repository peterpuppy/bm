# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/filename-restrictions-for-applications-that-support-workspaces.html

# Workspace Limits

The topics linked below describe the limits applied to the set of files contained within a workspace. If a workspace exceeds these limits, attempts to launch a process using the workspace will fail.

* [Maximum Uncompressed Data Capacity](maximum-uncompressed-data-capacity.html)
* [Diagnosing Failures Caused by Exceeding Workspace Limits](diagnosing-failures-caused-by-exceeding-workspace-limits.html)
* [Filename Restrictions for Applications that Support Workspaces](filename-restrictions-for-applications-that-support-workspaces.html)

# Maximum Uncompressed Data Capacity

Workspaces can store different maximum amounts of uncompressed file data depending on the Target's release check mode.

| Target | **Release Check Mode** | **Application file set** | **Additional content file set** |
| --- | --- | --- | --- |
| DevKit | Assist | 768 GiB | 180 GiB |
| Development | 1 TiB | 1 TiB |
| TestKit | Assist | 768 GiB | 180 GiB |

Full information on the file limits for packages can be found in the [Content Packaging and Updating Guide - Packages Overview - Restrictions Regarding Packages](../Content_Packaging_and_Updating-Guide/restrictions-regarding-packages.html).

Note:

Compressed files stored in a workspace contribute their uncompressed size towards this limit. The uncompressed size of files stored in a workspace can be retrieved using:

```
prospero-ctrl workspace list /full
```

For more information about the maximum uncompressed data capacity in different release check modes, refer to the following topics:

* [Maximum Uncompressed Data Capacity in Assist Mode](maximum-uncompressed-data-capacity-in-assist-mode.html)
* [Maximum Uncompressed Data Capacity in Development Mode](maximum-uncompressed-data-capacity-in-development-mode.html)

# Maximum Uncompressed Data Capacity in Assist Mode

The following table details the maximum amounts of uncompressed data available to a workspace on a Target in Assist mode:

| File set | Assist Mode |
| --- | --- |
| Application | 768 GiB |
| Additional content | 180 GiB |

For more information, refer to the [Changes to the maximum amounts of uncompressed data included in workspaces in Assist Mode](https://p.siedev.net/technotes/view/388) technical note on DevNet.

The following limits applied to a workspace in Assist mode match the limits specified in the [Content Packaging and Updating Guide - Packages Overview - Restrictions Regarding Packages](../Content_Packaging_and_Updating-Guide/restrictions-regarding-packages.html).

| **Parameter** | **Maximum** |
| --- | --- |
| `DataSize` | 154986 MiB |
| `FileCount` | 300,000 |

Note:

The `DataSize` and `FileCount` limitations both apply to packages and workspaces in Assist mode. However it might not be possible to build a package from an application file set that could then be launched via a workspace in Assist mode due to differences in both the compression ratio and metadata formats used. This limitation also applies to mounting an additional content file set.

For more information on Assist mode, refer to the Boot Parameters - Release Check Mode subsection of [System Software User's Guide (Settings) - Features of the ★Debug Settings Menu](../System_Software-Users_Guide_for_Settings/features-of-the-debug-settings-menu.html).

## Additional Content Workspaces

In Assist mode, the following limits are placed on workspaces mounted for additional content:

| **Parameter** | **Maximum** |
| --- | --- |
| Number of additional content workspaces mounted simultaneously | 64 |
| The total `DataSize` of additional content workspaces | 64 GiB |
| The total `FileCount` of additional content workspaces | 300,000 |

If these limits are exceeded, attempts to mount the additional content workspace will fail.

Note:

The `DataSize` and `FileCount` of additional content workspaces do not contribute to the `DataSize` and `FileCount` limits of the application workspace.

# Maximum Uncompressed Data Capacity in Development Mode

The following table details the maximum amounts of uncompressed data in Development mode workspaces in the current SDK version:

| **File set** | **Development Mode** |
| --- | --- |
| Applications | 1 TiB |
| Additional content | 1 TiB |

The limits for `DataSize`, `FileCount`, and additional content workspaces in Development mode are at least the as large as the Assist mode limits. These limits are typically significantly greater in practice as the system has more resources available to allocate to the workspace in Development mode.

For more information on Development mode, refer to the Boot Parameters - Release Check Mode subsection of [System Software User's Guide (Settings) - Features of the ★Debug Settings Menu](../System_Software-Users_Guide_for_Settings/features-of-the-debug-settings-menu.html).

## DataSize

The `DataSize` for a workspace can be retrieved using:

```
prospero-ctrl workspace list /full
```

The `DataSize` for a workspace is calculated as the sum of:

* The size of uncompressed files
* The size of compressed files

Note:

When you repeatedly modify a workspace, unnecessary data will accumulate. We call this garbage data. The amount of garbage data accumulated during hot loading counts towards the `DataSize` limit. The size of this garbage data is not included in the `DataSize` value displayed by the `prospero-ctrl` command listed above. Refer to [Workspace Garbage Collection](workspace-garbage-collection.html) for more information.

## FileCount

The `FileCount` for a workspace can be retrieved using:

```
prospero-ctrl workspace list /full
```

The `FileCount` for a workspace is calculated as the sum of:

* The number of uncompressed files
* The number of compressed files
* The number of garbage files accumulated during hot loading

# Diagnosing Failures Caused by Exceeding Workspace Limits

The following table lists error messages that are displayed due to exceeding workspace limits when launching a process:

| **Error Message** | **Action** |
| --- | --- |
| `[ERROR]: LoadProcessSuspended failed - The number of files in the Workspace exceeds the maximum number of files in a package.` | Assist mode only.  Reduce the `FileCount` of the workspace. |
| `[ERROR]: LoadProcessSuspended failed - The total workspace size is too large to launch the process.` | Reduce the `DataSize` of the workspace. |
| `[ERROR]: LoadProcessSuspended failed - Insufficient resources to mount the workspace for launch.` | Reduce the `FileCount` and/or `DataSize` of the workspace.  Note: Due to resource usage by the system, a resource shortage can occur when `DataSize` and `FileCount` do not exceed the specified limits. |

# Filename Restrictions for Applications that Support Workspaces

The applications that support workspaces will only support filenames that match the package rules. All ASCII characters are supported except the following:

* Control characters (`0x00` through `0x1F` and `0x7F`)
* `*` (asterisk)
* `:` (colon)
* `;` (semicolon)
* `?`
* `"` (double quotation mark)
* `<`
* `>`
* `|`
* `/` (slash)
* `\` (backslash)
* `%`

Note:

Case insensitive matching will fold capitals to lower-case, for example `A-Z` to `a-z`.

The host tools will also impose Windows filename restrictions. Do not use the following reserved names as the name of a file:

* `CON`
* `PRN`
* `AUX`
* `NUL`
* `COM1`
* `COM2`
* `COM3`
* `COM4`
* `COM5`
* `COM6`
* `COM7`
* `COM8`
* `COM9`
* `LPT1`
* `LPT2`
* `LPT3`
* `LPT4`
* `LPT5`
* `LPT6`
* `LPT7`
* `LPT8`
* `LPT9`

Additionally, do not end a file or directory name with a ' ' (space) or a '`.`' (period).