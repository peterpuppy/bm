# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-load-module-opt.html

# Dynamic Libraries

# SceKernelLoadModuleOpt

Additional data for loading a dynamic library

## Definition

```
#include <kernel.h>
typedef struct SceKernelLoadModuleOpt {
    size_t size;
} SceKernelLoadModuleOpt;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure [value of `sizeof(SceKernelLoadModuleOpt)`] |

## Description

This structure is provided to be used for storing additional data to pass when loading a dynamic library with `sceKernelLoadStartModule()`.

# SceKernelUnloadModuleOpt

Additional data for unloading a dynamic library

## Definition

```
#include <kernel.h>
typedef struct SceKernelUnloadModuleOpt {
    size_t size;
} SceKernelUnloadModuleOpt;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure [value of `sizeof(SceKernelUnloadModuleOpt)`] |

## Description

This structure is provided to be used for storing additional data to pass when unloading a dynamic library with `sceKernelStopUnloadModule()`.

# sceKernelDlsym

Get address of symbol exported by the dynamic library

## Definition

```
#include <kernel.h>
int sceKernelDlsym(
    SceKernelModule handle,
    const char *symbol,
    void **addrp
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | Identifier of the dynamic library |
| `symbol` | Symbol name |
| `addrp` | Destination to store the symbol address |

## Return Values

Stores the symbol address to `*addrp` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | `handle` is invalid, or symbol specified in `symbol` is not exported |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `symbol` or `addrp` address is invalid |

## Description

This function obtains the address of the symbol (function/variable) exported by the dynamic library. If the symbol specified in `symbol` is exported by the dynamic library specified with `handle`, the function call will succeed, and the address of the symbol will be returned in `*addrp`.

Only the identifier of a dynamic library created by a licensee or the identifier of an SDK library provided by SIE and placed within /app0/sce\_module (refer to [Sysmodule Library Overview - Package Installation](../Sysmodule-Overview/package-installation.html)) can be specified to `handle`. When an invalid identifier is specified, the `SCE_KERNEL_ERROR_ESRCH` error will be returned.

Only symbols declared for export with the \_\_`declspec(dllexport)` modifier specified in the source code, or symbols declared for export by a method with an equivalent effect, can be searched for by this function. For symbol export methods, refer to the [PRX Programming Overview](../PRX_Programming-Overview/__document_toc.html) document.

Note that addresses that correspond to TLS variable symbols cannot be obtained. `SCE_OK` will be returned when a TLS variable symbol name is specified for `symbol`, but an invalid address will be stored in `*addrp`.

## Notes

Specifying an identifier of an SIE-provided SDK library that is not placed within /app0/sce\_module is invalid. However, specifying an identifier of the C/C++ standard libraries will be valid only if the PRX file included in the system is loaded upon development. (For details, refer to the [Sysmodule Library Overview - Package Installation - PRX File Placement During Development](../Sysmodule-Overview/ps5-prx-file-placement-during-development.html).)

## See Also

`sceKernelLoadStartModule()`

[Kernel Overview - Dynamic Libraries](../Kernel-Overview/dynamic-libraries.html)

# sceKernelExtendMaximumModuleNumber

Increase the maximum number of modules that can be loaded into a process (during development only)

## Definition

```
#include <kernel_module_extension.h>
int sceKernelExtendMaximumModuleNumber(void)
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | The Release Check Mode is set to something other than Development Mode |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | This function has already been called |

## Description

This function increases the maximum number of modules that can be loaded into a process during development. For the default maximum number of modules that can be loaded and the maximum value to which that number can be increased, refer to [Kernel Overview - Dynamic Libraries - Maximum Number of Modules That Can Be Loaded](../Kernel-Overview/maximum-number-of-modules-that-can-be-loaded.html).

This function can be used only when the Release Check Mode is set to Development Mode. Additionally, it can be called only once within a given process.

## Notes

* This function is for use exclusively during development. Do not use this function in a program to be master submitted. The Publishing Tools report an error if there is an attempt to create a package that includes a program that uses this function.
* To use this function, include kernel\_module\_extension.h in the source program and link libkernel\_module\_extension\_nosubmission\_stub\_weak.a when building the program.

## See Also

`sceKernelLoadStartModule()`

# sceKernelLoadStartModule

Perform load and start processing of a dynamic library

## Definition

```
#include <kernel.h>
SceKernelModule sceKernelLoadStartModule(
    const char *moduleFileName,
    size_t args,
    const void *argp,
    uint32_t flags,
    const SceKernelLoadModuleOpt *pOpt,
    int *pRes
)
```

## Arguments

|  |  |
| --- | --- |
| `moduleFileName` | Dynamic library file absolute path |
| `args` | Size of the argument block |
| `argp` | Pointer to the argument block |
| `flags` | Reserved (specify 0) |
| `pOpt` | Reserved (specify NULL) |
| `pRes` | Destination to store the return value of `module_start()` |

## Return Values

Stores the value returned by `module_start()` in `*pRes` and returns the handle of the dynamic library (a positive value) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `flags` or `pOpt` is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | File specified in `moduleFileName` does not exist |
| `SCE_KERNEL_ERROR_ENOEXEC` | 0x80020008 | Cannot load because of abnormal file format |
| Cannot load because the address of the symbol that is referenced after relocation processing is invalid |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Cannot load because it is not possible to allocate memory |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | File specified with `moduleFileName` is placed in a forbidden location |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `moduleFileName` points to invalid memory |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Cannot load because of insufficient resources |
| `SCE_KERNEL_ERROR_ESDKVERSION` | 0x80020063 | Version of the SDK used to build the specified dynamic library is newer than the system software version |
| Version of the SDK used to build the dynamic library does not match the SDK version used to build the application's executable file |
| `SCE_KERNEL_ERROR_ESTART` | 0x80020064 | `module_start()` returned a negative integer |
| `SCE_KERNEL_ERROR_ENODYNLIBMEM` | 0x80020076 | Unable to load because there is not enough system memory |

Workspace-specific error codes may be returned if you are using a workspace. For details, refer to [Workspaces Overview - Workspaces Overview Appendix A - Workspace Specific Errors](../Workspaces-Overview/workspaces-overview-appendix-a-workspace-specific-errors.html).

## Description

This function loads the dynamic library specified in `moduleFileName` and carries out start processing of the dynamic library by calling its `module_start()`.

Specify an absolute path for `moduleFileName`. When a value other than an absolute path is specified, `SCE_KERNEL_ERROR_ENOENT` is returned. Note that only files placed under /app0 can be specified for `moduleFileName`.

When load and start processing succeeds, the value returned by `module_start()` is stored in the area pointed to by `pRes`. If receiving the `module_start()` return value is not required, specify NULL for `pRes`. The handle returned by `sceKernelLoadStartModule()` upon success will be required when unloading the dynamic library with `sceKernelStopUnloadModule()`; store it in an appropriate variable.

If `module_start()` returns a negative integer, `sceKernelLoadStartModule()` (this function) will fail to load the dynamic library. At this time, the `module_start()` return value will be stored in `*pRes`, and `SCE_KERNEL_ERROR_ESTART` will be returned.

This function maps the specified dynamic library to a process address space, performs relocation processing, and performs initialization processing, but these are not performed together atomically. Therefore, even if the specified dynamic library is mapped to a process address space, it may not be possible to perform calls of the functions defined by the dynamic library or access of variables. If you intend to make a dynamic library function call or to access a variable from such a library in a thread other than the one in which `sceKernelLoadStartModule()` (this function) was called, make sure that the processing of this function has terminated normally before doing so.

This function returns `SCE_KERNEL_ERROR_ENOEXEC` when the file format of the PRX is abnormal. The main reason is not conforming to the correct binary format. Even if it used to be a valid file, the error may be returned if the contents become damaged due to file corruption. `SCE_KERNEL_ERROR_ENOEXEC` is also returned in cases when the address of the symbol that is referenced after relocation processing becomes invalid (for example, an address outside the range of the PRX).

If an already loaded dynamic library is loaded again one or more times, `module_start()` will not be executed for the second or any further call, and only the same handle from the first time the library was loaded will be returned. To unload the dynamic library, `sceKernelStopUnloadModule()` will then need to be called the same number of times as the original loading function was called.

If a dynamic library is in a location (such as in /app0 or in /host) that is not case-sensitive, separate calls to this function targeting the same file but capitalizing its path name differently when specifying it will each be recognized as targeting a separate file. A separate handle will be returned for each "file". You should avoid specifying the same file with its path name capitalized differently.

## Notes

* Files placed under /host can also be specified when the Release Check Mode is set to Development Mode or Assist Mode. Files at these paths cannot be specified when using a retail unit or a Development Kit /Testing Kit in Release Mode. Even if these paths are mapped to paths under /app0 using overlay settings, loading is not possible when using a retail unit or a Development Kit/Testing Kit in Release Mode. `SCE_KERNEL_ERROR_ENOENT` is returned in such cases.

  In addition, `SCE_KERNEL_ERROR_EACCES` is returned when a file placed in a location other than /app0 or /host is specified.
* The system reserves a fixed amount of system memory for managing modules that are loaded. A sufficient amount of memory is allocated for the execution of a typical program, but this amount may be insufficient depending on the structure of the program. If this memory cannot be allocated when loading a module, this function returns the error `SCE_KERNEL_ERROR_ENODYNLIBMEM`. If this error occurs, contact SIE via the "Post new issue" page in Private Support (<https://game.develop.playstation.net/support>).

  During development, this error can be avoided by calling `sceKernelExtendMaximumModuleNumber()` in Development Mode. In that case, the system allocates memory used for managing modules from system memory that is available only in Development Mode and that is exclusively for dynamic libraries. If this error is returned despite `sceKernelExtendMaximumModuleNumber()` having been called, contact Private Support.

## See Also

[Kernel Overview - Dynamic Libraries](../Kernel-Overview/dynamic-libraries.html)

# sceKernelStopUnloadModule

Perform stop and unload processing of the dynamic library

## Definition

```
#include <kernel.h>
int sceKernelStopUnloadModule(
    SceKernelModule handle,
    size_t args,
    const void *argp,
    uint32_t flags,
    const SceKernelUnloadModuleOpt *pOpt,
    int *pRes
)
```

## Arguments

|  |  |
| --- | --- |
| `handle` | Identifier of the dynamic library |
| `args` | Size of the argument block |
| `argp` | Pointer to the argument block |
| `flags` | Reserved (specify 0) |
| `pOpt` | Reserved (specify NULL) |
| `pRes` | Destination to store the return value of `module_stop()` |

## Return Values

Stores the value returned by `module_stop()` in `*pRes` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `flags` or `pOpt` is invalid |
| `SCE_KERNEL_ERROR_ESRCH` | 0x80020003 | `handle` is invalid (specified dynamic library is not loaded) |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Specified dynamic library is referenced by a thread other than the thread that called this function |

## Description

This function calls `module_stop()` of the dynamic library specified in `handle` to perform stop processing and then carries out unload processing.

For `handle`, specify the value returned by `sceKernelLoadStartModule()`.

When stop and unload processing succeeds, the value returned by `module_stop()` is stored in the area pointed to by `pRes`. If receiving the `module_stop()` return value is not required, specify NULL for `pRes`.

If a non-POD-type TLS variable is defined for the target dynamic library to unload and there is a thread in the process that has not called the destructor for this non-POD-type TLS variable, the target dynamic library to unload is considered to be referenced. In such cases, calls to this function fail, and `SCE_KERNEL_ERROR_EBUSY` is returned. Such states can be resolved by forcing the destructor calls for these TLS variables in all threads using these TLS variables. For details about forcing destructor calls, refer to the description of `sceLibcForceTlsDestructor()` in the [C and C++ Standard Libraries: Overview and Reference](../C_and_Cpp_standard_libraries/__document_toc.html) document.

If the same dynamic library is loaded more than once, this function needs to be called the same number of times that `sceKernelLoadStartModule()` was called to unload the dynamic library. `module_stop()` is executed only when the library is actually unloaded.

## Notes

* When this function returns `SCE_KERNEL_ERROR_EBUSY`, a message that starts with the following will be displayed.

  sceKernelStopUnloadModule: cannot unload *module name*

  TLS variable in the module is still referred to from thread(s):
* It may take some time for the unload processing to complete when the following two conditions are satisfied. Therefore, do not call this function from threads with strict time constraints (such as rendering threads).
  + An executable file or PRX is referencing a function or a variable of a PRX to be unloaded
  + An executable file or PRX that satisfies the above condition is referencing many functions or variables of other executable files or PRXes

## See Also

[Kernel Overview - Dynamic Libraries](../Kernel-Overview/dynamic-libraries.html)

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.