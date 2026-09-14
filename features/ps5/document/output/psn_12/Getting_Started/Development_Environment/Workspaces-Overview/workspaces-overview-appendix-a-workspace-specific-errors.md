# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/workspaces-overview-appendix-a-workspace-specific-errors.html

# Workspaces Overview Appendix A - Workspace Specific Errors

Unlike packages, files and directories can be added to workspaces after the launch of a process. This means that errors that may not occur on packages will now occur on workspaces.

This topic lists error codes that may be returned by APIs when accessing files and directories on workspaces, or via the Workspace Library.

In the table below, `sce::Ampr::Apr::resolveFilepaths*()` will have an error code set in the return value or in the results[] argument.

| **Value** | **Number** | **Description** | **APIs** |
| --- | --- | --- | --- |
| `SCE_KERNEL_ERROR_EWSMIRROR` | `0x80020068` | The workspace failed to mirror.  The network connection to the Host PC was interrupted while a game was running on a System Manager Host Mirror Workspace. This error code will persist until the process is terminated. | * `sceKernelOpen()` * `sceKernelStat()` * `sceKernelRead()` * `sceKernelReadv()` * `sceKernelPread()` * `sceKernelPreadv()` * `sceWorkspaceMirrorBarrier()`  * `sce::Ampr::Apr::resolveFilepaths*()` |
| `SCE_KERNEL_ERROR_EWSHOSTBUSY` | `0x8002006E` | Because a file or a directory on the Host PC are in-use, the Host PC cannot respond to a request. | * `sceKernelOpen()` * `sceKernelStat()` * `sceKernelGetdents()` * `sceKernelGetdirentries()` * `sceWorkspaceMirrorBarrier()`  * `sce::Ampr::Apr::resolveFilepaths*()` |
| `SCE_KERNEL_ERROR_ENOSPC` | `0x8002001c` | The workspace cannot store files because of insufficient free space. | * `sceKernelOpen()` * `sceKernelStat()` * `sceKernelGetdents()` * `sceKernelGetdirentries()` * `sceWorkspaceMirrorBarrier()`  * `sce::Ampr::Apr::resolveFilepaths*()` |
| `SCE_KERNEL_ERROR_ENOTCONN` | `0x80020039` | The Host PC is not connected. | * `sceKernelOpen()` * `sceKernelStat()` * `sceKernelRead()` * `sceKernelReadv()` * `sceKernelPread()` * `sceKernelPreadv()` * `sceWorkspaceMirrorBarrier()` * `sce::Ampr::Apr::resolveFilepaths*()`   result of:   * `SceAprResultBuffer`   returnValue of:   * `SceKernelAioResult` |
| `SCE_KERNEL_ERROR_ESTALE` | `0x80020046` | The corresponding file on the Host PC is modified or removed. | * `sceKernelRead()` * `sceKernelReadv()` * `sceKernelPread()` * `sceKernelPreadv()`   result of:   * `SceAprResultBuffer` * `sce::Ampr::Apr::resolveFilepaths*()`   returnValue of:   * `SceKernelAioResult` |
| `SCE_KERNEL_ERROR_EINVAL` | `0x80020016` | `flags` or `pOpt` is invalid. |  |
| `SCE_KERNEL_ERROR_ENOENT` | `0x80020002` | File specified in `moduleFileName` does not exist. |  |
| `SCE_KERNEL_ERROR_ENOEXEC` | `0x80020008` | Cannot load because of abnormal file format. |  |
| Cannot load because the address of the symbol that is referenced after relocation processing is invalid. |  |
| `SCE_KERNEL_ERROR_ENOMEM` | `0x8002000c` | Cannot load because it is not possible to allocate memory. |  |
| `SCE_KERNEL_ERROR_EACCES` | `0x8002000d` | File specified with `moduleFileName` is placed in a forbidden location. |  |
| `SCE_KERNEL_ERROR_EFAULT` | `0x8002000e` | `moduleFileName` points to invalid memory. |  |
| `SCE_KERNEL_ERROR_EAGAIN` | `0x80020023` | Cannot load because of insufficient resources. |  |
| `SCE_KERNEL_ERROR_ESDKVERSION` | `0x80020063` | Version of the SDK used to build the specified dynamic library is newer than the system software version. |  |
| `SCE_KERNEL_ERROR_ESTART` | `0x80020064` | `module_start()` returned a negative integer. |  |
| `SCE_KERNEL_ERROR_ENODYNLIBMEM` | `0x80020076` | Unable to load because there is not enough system memory. |  |