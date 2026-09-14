# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/overview-4.html

# Dynamic Libraries

# Overview

The PlayStation®5 kernel provides features for loading/unloading a program (dynamic library) stored in the file system to/from the virtual address space.

A program comprises an execution entity and a dynamic library. The execution entity is loaded to the virtual address space when a game process is created and remains there until the process is terminated. By contrast, the dynamic library can be loaded to, and unloaded from, the virtual address space at any time. The load destination address for the dynamic library is dynamically allocated by the PlayStation®5 kernel.

The PlayStation®5 kernel adopts the PRX re-locatable object file format for the implementation of dynamic libraries.

Note:

PRX may be used in reference to a file in the PRX format, a program module loaded to the virtual address space, and a dynamic library in the PRX format regardless of its state.

Many of the libraries provided in the SDK are dynamic libraries. Load/Unload of such libraries can be carried out using functions of the Sysmodule library. However, a dynamic library created by a licensee should be loaded/unloaded using functions of the kernel, as explained in this chapter.

Note:

For instructions on building a PRX file, refer to the [PRX Programming Overview](../PRX_Programming-Overview/__document_toc.html) document.

# Main Module

The application comprises multiple program modules. Of them, the program module created as the main body of the application is called the main module. The main module must satisfy the following requirements.

* Only one `main()` is defined
* Upon program module link, a link is made without specifying `-oformat=prx` (when building the module via VSI, "Project Settings" > "ELF project" is selected from the project wizard)

When a process is created, in addition to the main module, several PRX modules required for execution of the process will be implicitly loaded onto the process space. When process creation processing by the kernel completes, execution moves to the main module and the following processing will be executed on the main thread.

1. Initializing of the process overall (carried out within the process space)
2. Load of PRX modules required for main module execution and the execution of their initialization codes
3. Execution of the initialization code of the main module
4. Call of `main()`

# Maximum Number of Modules That Can Be Loaded

By default, a maximum total of 256 modules can be loaded into one process. This number includes the main module and the system-sourced PRX modules that are implicitly loaded by the system.

When attempting to load modules exceeding the maximum limit, `sceKernelLoadStartModule()` returns `SCE_KERNEL_ERROR_EAGAIN`.

During development, you can increase the maximum number of modules that can be loaded into one process to 768 by calling `sceKernelExtendMaximumModuleNumber()` on a Development Kit whose Release Check Mode is set to Development Mode.

# Program Module Handles

Program modules loaded in memory have handles assigned as follows:

* A value equal to 0 is always assigned as the handle for the main module.
* Undefined `SceKernelModule`-type values that are unique within the process are assigned as the handles for PRX modules. The values assigned may change each time the process is started up. When unloading this PRX module, use this handle to specify the unload target.

# PRX Library Load and Start

Starting use of the PRX library entails load processing (placing the program code stored in the PRX file to the virtual address space) and start processing (disclosing the library and processing the dynamic link). The kernel provides `sceKernelLoadStartModule()`, which carries out both the load and start processing.

Only paths under /app0 can be specified as PRX file load paths. However, paths below /host can also be specified during development. For details, refer to the explanation of `sceKernelLoadStartModule()` in the [Kernel Reference](../Kernel-Reference/__document_toc.html) document.

```
#include <kernel.h>
static SceKernelModule load_prx(const char *path)
{
    return sceKernelLoadStartModule(path, 0, 0, 0, NULL, NULL);
}
```

# PRX Library Stop and Unload

Ending use of the PRX library entails stop processing (deleting the library and unlinking) and unload processing (freeing memory). The kernel provides `sceKernelStopUnloadModule()`, which carries out both the stop and unload processing.

```
#include <kernel.h>
static int unload_prx(SceKernelModule handle)
{
    return sceKernelStopUnloadModule(handle, 0, 0, 0, NULL, NULL);
}
```

# Entry Functions

For a PRX library requiring unique processing upon starting or ending its use, it is possible to define a function (entry function) to be called at the start processing and at the stop processing.

* `int module_start(size_t, const void*)` : entry function called upon start processing
* `int module_stop(size_t, const void*)` : entry function called upon stop processing

`module_start()` is called within the start processing for the PRX library. The argument block specified with the `args` and `argp` arguments of `sceKernelLoadStartModule()` is directly passed to `module_start()`. The value returned by `module_start()` will be stored in the area pointed to by the `pRes` argument of `sceKernelLoadStartModule()` and returned to the application.

`module_stop()` is called within the stop processing for the PRX library. The argument block specified with the `args` and `argp` arguments of `sceKernelStopUnloadModule()` is passed directly to `module_stop()`. The value returned by `module_stop()` will be stored in the area pointed to by the `pRes` argument of `sceKernelStopUnloadModule()` and returned to the application.

The entry functions will only be called if they are defined within the PRX library. These entry functions cannot be renamed.

# Stub File and Load Order

A PRX library comprises the PRX file and its pairing stub file. As mentioned earlier, the PRX file is dynamically loaded and used. The stub file must be statically linked in advance to the caller execution entity or PRX library for use.

There are two types of stub files.

* <*libname*>\_stub.a: stub file for safe import (safe link)
* <*libname*>\_stub\_weak.a: stub file for loose import (loose link)

The difference between the two is whether there is a limitation on the load order of PRX libraries with dependency relationships.

To exemplify, assume the use of PRX library A and PRX library B where a function of PRX library B is called within PRX library A, meaning PRX-A is dependent on PRX-B.

When the stub file for safe import (safe link) of PRX-A is statically linked, PRX-B (on which PRX-A is dependent) must be loaded before loading PRX-A. When attempting to load PRX-A without loading PRX-B first, `sceKernelLoadStartModule()` will fail with an error. By contrast, when the stub file for loose import (loose link) of PRX-A is statically linked, `sceKernelLoadStartModule()` will succeed even if PRX-B is not loaded before PRX-A. Since there is no dynamic linking, however, functions and variables of PRX-A cannot be accessed yet. PRX-B must be loaded before functions and variables of PRX-A can be accessed.

When a function that is not dynamically linked is called and a debugger is not connected (upon execution of the `prospero-run` command, for example), an error message starting with "=== Call to unpatched function is detected!!! ===" will be displayed at the end of the crash log that is output by the kernel. If a debugger is connected, "Software breakpoint encountered at 0x0000000A000*XXXXX* (specific address) in libkernel.sprx" will be displayed on the debugger. Check the debugger's "Call Stack" when this message is displayed; the call in the second row represents the call of the function that is not dynamically linked. Thus, it can be identified that this call is causing a problem.

When accessing a variable that is not dynamically linked, an invalid memory access exception for the 0x840000000 address will occur.

Note:

In the current SDK, only the stub files for loose import (loose link) are supported.

# Version Checking PRX Files

In the main module and in PRX modules, the version of the SDK used to build each module is recorded. In system software 11.00.00 and later, checks are performed to determine whether the recorded SDK versions match between the main module in the application (such as eboot.bin) and the PRX modules.

This version check occurs when a PRX module is loaded. If the versions of the main module and the PRX module that is about to be loaded do not match, an error is detected. Specifically, `sceKernelLoadStartModule()` returns `SCE_KERNEL_ERROR_ESDKVERSION`.

During development, these version checks can be disabled by setting "★Debug Settings" > "System" > "Ignore PRX SDK Version Check" to "On" (default). If set to "On", no error is detected even if the versions do not match, and the loading process continues.

To have version checks work correctly when the Release Check Mode is set to Development Mode or Assist Mode, set "Ignore PRX SDK Version Check" to "Off". Note that version checking is always enabled when the Release Check Mode is set to Release Mode.