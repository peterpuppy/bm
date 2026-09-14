# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/workspaces-hot-loading-support-update-phase.html

# Hot Loading Support for Workspaces

Hot loading is a file operation that enables a process to access modified file data while the process is running. Hot loading consists of two phases: [Update](workspaces-hot-loading-support-update-phase.html) and [Apply](workspaces-hot-loading-apply-phase.html).

Also refer to the following topics for more information about hot loading in workspaces:

* [Data Eligible for Hot Loading](data-eligible-for-hot-loading.html)
* [Using Hot Loading with On-Demand Mirror Mode](using-hot-loading-with-on-demand-mirror-mode.html)
* [Considerations when Using Hot Loading for Workspaces](considerations-when-using-hot-loading-for-workspaces.html)

# Workspaces Hot Loading - Update Phase

The **Update** phase of a hot loading operation enables new file data to be transferred to the Target while a workspace is mounted and in use by a running process.

When using a Standalone workspace, the updated files must be manually pushed to the Target.

When using a System Managed Host Mirror workspace, the update phase happens automatically when the files are updated on the Host PC.

## Potential Timing Issues

When using a System Managed Host Mirror workspace, the **Update** phase may take some time to complete after a file has been modified on the Host PC. This delay in updating the files on the Target could lead to a race condition between the time when the file modification is made on the Host PC and the time when the updated file is visible to the process on the Target.

You can avoid this issue by checking the "update pending" status using the Workspace Library to reliably identify when files are updated on the Target after being modified on the Host PC's filesystem. Refer to [Workspace Library Overview - Reference Information - Obtaining the Status of Pending Hot Loading Updates](../Workspace_Library-Overview/obtaining-the-status-of-pending-hot-loading-updates.html) for more information.

# Workspaces Hot Loading - Apply Phase

The **Apply** phase of a hot loading operation switches the old file data for the new file data transferred from the Host PC during the **Update** phase. Once this switch has been performed, the running process can access the updated files.

The **Apply** phase of hot loading can only be initiated for files that have been successfully transferred during the **Update** phase.

For System Managed Host Mirror, the **Update** phase may take some time to complete after a file has been modified on the Host PC. Refer to
[Potential Timing Issues](workspaces-hot-loading-support-update-phase.html#workspaces-overview_1_1__section_cng_qyy_ygc) for more information.

The **Apply** phase of hot loading has two modes - Automatic mode and Manual mode.

## Automatic Mode (default)

In Automatic mode the updated file data becomes available to be read by the process when either:

* All opened file descriptors of a modified file are closed.

OR

* A modified file is re-resolved using APR.

Until these requirements are met, the original file data will continue to be read by the process.

Note:

APR resolves for a particular path will always resolve to the same ID for a given execution of the process. ID values are not guaranteed to be the same after closing and re-launching the process.

## Manual Mode

In Manual mode, updated file data only becomes available to the process when it is explicitly applied using the Workspace Library. For further information about manual mode, refer to [Workspace Library Overview](../Workspace_Library-Overview/__document_toc.html).

# Data Eligible for Hot Loading

The following data in workspaces is eligible for hot loading:

* [File
  contents](data-eligible-for-hot-loading.html#workspaces-overview_1_3__section_ekc_f5g_zgc)
* [Directory
  contents](data-eligible-for-hot-loading.html#workspaces-overview_1_3__section_jdh_f5g_zgc)
* [Stat
  information](data-eligible-for-hot-loading.html#workspaces-overview_1_3__section_lkn_f5g_zgc)

## File Contents

Hot loading modified file content is handled as described in the [Update](workspaces-hot-loading-support-update-phase.html) and [Apply](workspaces-hot-loading-apply-phase.html) sections.

## Directory Contents

Files and directories can be created and deleted from a directory as part of the hot
loading process:

* When using
  Standalone
  workspaces, newly created files will be immediately accessible once the file has
  been pushed to the Target.
* When using System Managed Host Mirror workspaces, newly created files on the
  Host PC file system will be immediately accessible to a running process

Depending on the mode used during the Apply phase, the following limitations
apply:

* When using [Automatic mode](workspaces-hot-loading-apply-phase.html#workspaces-overview_1_2__section_xsx_lsg_zgc), files can only be deleted if they are not referenced
  by open file descriptors, and have not been resolved by the running process
  using APR.
* When using [Manual mode](workspaces-hot-loading-apply-phase.html#workspaces-overview_1_2__section_em3_msg_zgc), files cannot be deleted from a workspace while a
  running process has that workspace mounted.

## Stat Information

Status (Stat) information displays the current status of the files:

* When using
  Standalone
  workspaces, the stat information for files will be the Target's view of the file
  data.
* When using System Managed Host Mirror workspaces:

  + The stat information for files that have been cached on the workspace
    will be the Target's view of the file data.
  + The stat information for files that have not been cached on the
    workspace will be the Host PC's view of the file data.

Note:

Where stat information is drawn from the Target's view of the file data, there
could be inconsistencies between Target and Host PC versions of the files. For
example, if the [Update](workspaces-hot-loading-support-update-phase.html) phase of the hot loading operation has completed but the
[Apply](workspaces-hot-loading-apply-phase.html) phase has yet to start, the stat information will display the
old file data.

Note:

It is not recommended to compare the times contained in the stat information with
the times from data on your Host PC. To ensure that data hot loaded is
synchronized between the Host PC and the Target, use the appropriate method for
your Workspace type:

| Workspace type | Method |
| --- | --- |
| System Managed Host Mirror | Call `sceWorkspaceMirrorBarrier()` |
| Standalone | Wait for either `prospero-ctrl workspace deploy` or `prospero-ctrl workspace push` to complete. |

# Using Hot Loading with On-Demand Mirror Mode

When using a System Managed Host Mirror workspace in [On-demand mode](mirroring-modes-for-system-managed-host-mirror-workspaces.html#workspaces-overview_0_2_2__section_psg_kxy_ygc), a read request for an unmirrored portion of a file will not be fulfilled if the file has been modified or deleted on the Host PC.

Should this situation occur, the behavior of the SDK APIs used are listed below:

| **API** | **Behavior** |
| --- | --- |
| SDK functions for reading files, such as `sceKernelRead()` and asynchronous I/O read | Triggers `SCE_KERNEL_ERROR_ESTALE` error. |
| APR reads submitted by `sce::Ampr::Apr::submitCommandBufferAndGetResult()` | Triggers `SCE_KERNEL_ERROR_ESTALE` error. |
| APR reads submitted by `sce::Ampr::Apr::submitCommandBuffer()` | Process is terminated with an exception. |

Refer to
[Appendix A - Workspace Specific Errors](workspaces-overview-appendix-a-workspace-specific-errors.html) for more information.

Note:

The same behavior will occur if files with unmirrored portions are manually pushed to the Target during process execution.

# Considerations when Using Hot Loading for Workspaces

File contents will be applied even if there are file descriptors open when:

* Resolving a file using APR with hot loading in [Automatic mode](workspaces-hot-loading-apply-phase.html#workspaces-overview_1_2__section_xsx_lsg_zgc).
* Applying updated file content using the Workspace library.

Should you apply the file contents with file descriptors open, calls to SDK functions such as `sceKernelRead()`, `sceKernelFstat()`, `sceKernelStat()` and asynchronous I/O read, will return `SCE_KERNEL_ERROR_ESTALE` error for the updated file.

Once all open descriptors for the updated file have been closed, newly opened descriptors for the file will reflect the updated content.

Files and directories cannot be deleted from the workspace if they:

* Are referenced by open descriptors.
* Have been remapped by a GP5 File.
* Have been resolved using APR.

In these cases, it will be necessary to close the process on the Target before attempting to delete the files or directories.

Files or directories deleted from the Host PC at the same time as being resolved by a process on the Target may temporarily fail with a `SCE_KERNEL_ERROR_EWSMIRROR` error.