# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/project-settings-in-visual-studio.html

# Configuring Visual Studio Project Settings

The build settings for projects can be set for individual projects or globally. The following topics describe the available settings:

* [Configuring Build Settings for Projects and Files in Visual Studio](configuring-build-settings-for-projects-and-files-in-visual-studio.html)
* [Project Settings in Visual Studio](project-settings-in-visual-studio.html)
* [Configuring Global Build Settings in Visual Studio](configuring-global-build-settings-in-visual-studio.html)
* [Determining Build Settings Used in Visual Studio](determining-build-settings-used-in-visual-studio.html)

# Configuring Build Settings for Projects and Files in Visual Studio

You can specify the build settings for a project configuration by using the project Property Pages.

To open the project **Property Pages:**

1. Select one or more projects in the **Solution Explorer**.
2. On the **Project** menu, click **Properties**.
3. In the left pane, select a group of properties.
4. In the right pane, configure properties, and then click **OK**.

# Project Settings in Visual Studio

Project Property Pages display different options depending on the project type that was selected in Solution Explorer. The following topics describe the options that are available when a PlayStation®5 project configuration is selected:

* [VSI Project Settings - General](vsi-project-settings-general.html)
* [VSI Project Settings - Advanced](vsi-project-settings-advanced.html)
* [VSI Project Settings - Debugging](vsi-project-settings-debugging.html)
* [VSI Project Settings - VC++ Directories](vsi-project-settings-vc-plus-plus-directories.html)
* [VSI Project Settings - C/C++](vsi-project-settings-c-c-plus-plus.html)
* [VSI Project Settings - Linker](vsi-project-settings-linker.html)
* [VSI Project Settings - Librarian](vsi-project-settings-librarian.html)
* [VSI Project Settings - Custom Build Steps and Build Events](vsi-project-settings-custom-build-steps-and-build-events.html)
* [VSI Project Settings - Wave Compiler](vsi-project-settings-wave-compiler.html)
* [VSI Project Settngs - Intel® Implicit SPMD Program Compiler (ISPC)](vsi-project-settings-intel-implicit-spmd-program-compiler-ispc.html)

For more information on the settings available when building with the LLVM toolchain, refer to the [C/C++ Compiler Reference](../C_Cpp_Compiler-Reference/__document_toc.html).

# VSI Project Settings - General

The General section contains settings for files, executable and library projects. The settings pane contains two categories, **General** and **Sanitizers**.

* [VSI Project Settings - General (Projects)](vsi-project-settings-general-projects.html)
* [VSI Project Settings - General (Files)](vsi-project-settings-general-files.html)
* [Specifying SDK Location in Visual Studio](specifying-sdk-location-in-visual-studio.html)

# VSI Project Settings - General (Projects)

## General

These settings are appear when opening the **Property Pages** window for a project.

| **Setting** | **Description** |
| --- | --- |
| **Output Directory** | Specifies the directory where tools, for example the linker and librarian, place all final output files from the build process. |
| **Intermediate Directory** | Specifies the directory where tools, for example the compiler and assembler, place all intermediate files from the build process. |
| **Target Name** | Specifies the filename this project will generate. |
| **Configuration Type** | Specifies the type of output this configuration generates.  For example:   * Makefile * Application (`.elf`) * Dynamic library (`.prx`) * Static library (`.a`) * Utility |
| **SDK Version** | Specifies which SDK to use.  Note: This property is ignored if the SDK has been specified using the `$(ProsperoSdkFolder)` property. Refer to [Specifying SDK location](specifying-sdk-location-in-visual-studio.html) for more information. |
| **Platform Toolset** | Specifies the toolset used for building the current configuration. |
| **Enable Just My Code Debugging** | Enables support for Just My Code debugging. For more information, refer to [Debugger User's Guide - Customizing the Debugger](../Debugger-Users_Guide/customizing-the-debugger.html). |
| **SN-DBS Options** | Specifies additional command line options to pass to SN-DBS, if used during the build. |

## Sanitizers

The Sanitizers section enables you to enable various runtime checks for dangerous or incorrect behavior. A diagnostic message will be generated when a check fails while your executable is running on the Target.

Note:

Enabled checking will have a runtime performance penalty.

| **Setting** | **Description** |
| --- | --- |
| **Undefined Behavior Sanitizer** | Enables Clang's Undefined Behavior Sanitizer checking.  Select from:   * **Off** * **Recover** * **Fatal**   When enabled, error reports will be added to VSI's [Issues Window](using-the-visual-studio-issues-window.html) during debugging when failures are detected.  Refer to [Sanitizers Overview - Overview of the UndefinedBehaviorSanitizer](../Sanitizers-Overview/overview-of-the-undefined-behavior-sanitizer.html) for further details on how this feature is implemented. |
| **Enable Address Sanitizer** | Enable Clang's Address Sanitizer checking. Select from:   * **Off** * **Recover** * **Fatal**   When enabled, error reports will be added to VSI's [Issues Window](using-the-visual-studio-issues-window.html) during debugging when failures are detected.  Refer to [Sanitizers Overview - Overview of the AddressSanitizer](../Sanitizers-Overview/overview-of-the-address-sanitizer.html) for further details on how this feature is implemented.  For the full list of errors trapped by Address Sanitizer, refer to [Appendix D - Address Sanitizer Errors](vsi-appendix-d-address-sanitizer-errors.html). |
| **Enable Thread Sanitizer** | Enable Clang's Thread Sanitizer checking. Select from:   * **Off** * **On**   When enabled, error reports will be written to console output during debugging when failures are detected.  Refer to [Sanitizers Overview - Overview of the ThreadSanitizer](../Sanitizers-Overview/overview-of-the-thread-sanitizer.html) for further details on how this feature is implemented. |

# VSI Project Settings - General (Files)

These settings are visible when opening the **Property Pages** window for a file.

| **Setting** | **Description** |
| --- | --- |
| **Excluded From Build** | Excludes the selected files in the build for the current configuration. |
| **Content** | Specifies whether the file is deployable content. |
| **Item Type** | Determines the build tool for the selected files. |

# Specifying SDK Location in Visual Studio

When a PlayStation®5 SDK is installed using SDK Manager, the installer program will perform the following actions:

* Installs the SDK in a folder named after the version being installed under `C:\Program Files (x86)\SCE\Prospero SDKs`.
* Sets the `%SCE_PROSPERO_SDK_DIR%` environment variable to point to this SDK location.

The `C:\Program Files (x86)\SCE\Prospero SDKs`\ folder can contain multiple SDK versions. We refer to this as the **SDK Repository**.

The `%SCE_PROSPERO_SDK_DIR%` environment variable is required for some Toolchain components and other development applications to find files in the SDK. `%SCE_PROSPERO_SDK_DIR%` is also used to ensure that all applications, for example the build system, use the tools and libraries contained in the latest SDK by default.

This means that you are able to build and run a PlayStation®5 application using the latest SDK without needing to change anything.

## Temporarily Changing SDKs

It is also possible to build your application using a specific SDK from your SDK Repository.

To change the SDK version:

1. In Visual Studio, open your project, then open the Project Properties.
2. Select General from the left pane.
3. Click on the **SDK Version** value drop-down list to see a list of all the available SDKs in the SDK repository, and select your desired SDK.

Note:

The current active SDK, meaning the SDK version currently set in `%SCE_PROSPERO_SDK_DIR%`, will be listed in the drop-down list as **Default**.

Choosing an SDK Version other than the Default will temporarily replace the value held in the `%SCE_PROSPERO_SDK_DIR%` environment variable with that of the selected SDK Version during the build process.

Note:

If an SDK Version is selected that is not installed on the PC, then the build will fail and an Error message will be displayed.

## Permanently Adding SDK Repository to Project

If `%SCE_PROSPERO_SDK_DIR%` has not been defined on the PC, VSI will assume the location of the SDK Repository is at the location defined in `$(SCE_ROOT_DIR)\Prospero SDKs` where `$(SCE_ROOT_DIR)` is a project property. If `$(SCE_ROOT_DIR)` and `%SCE_PROSPERO_SDK_DIR%` are both undefined, the SDK Repository will be set to the location of the Solution. In these cases the "SDK Version" value will be set to "sdk".

You can avoid changing the value of `%SCE_PROSPERO_SDK_DIR%` when specifying an SDK other than the Default SDK by manually instructing VSI of the path to the SDK Repository using the `$(ProsperoSdkRepository)`property.

When %SCE\_PROSPERO\_SDK\_DIR% is undefined, using `$(ProsperoSdkRepository)` prevents Visual Studio from assuming the location of the SDK Repository is always `$(SCE_ROOT_DIR)\Prospero SDKs`.

## Permanently Setting SDK to Project

You can override the default SDK and any temporary SDK set using the "SDK Version" parameter by specifying a path manually using the property `$(ProsperoSdkFolder)`.

Once set, any build of the project will use the SDK found on the path defined in `$(ProsperoSdkFolder)` and will generate a warning when used in combination with an SDK specified by the "SDK Version" parameter.

Alternatively, MSBuild enables you to specify that the "SDK Version" parameter should be used across all project files in the project. If a file called `Directory.Build.props` is placed alongside or in a directory above a project, then the contents of that file are incorporated into the project.

# VSI Project Settings - Advanced

## Advanced Properties

| **Setting** | **Description** |
| --- | --- |
| **Target Extension** | Specifies the file extension this project will generate. |
| **Extensions to Delete on Clean** | Deletes files with the specified extensions in the intermediate directory and all build output when you perform a clean or rebuild. You can specify wildcard characters. |
| **Build Log File** | Specifies the build log file to write to when build logging is enabled. |
| **Enable Unity (JUMBO) Build** | Enables a build process where many C++ source files are combined into one or more "unity" files before compilation to improve build performance.  Note: This is unrelated to the Unity® software game engine. |

## IntelliSense Properties

| **Setting** | **Description** |
| --- | --- |
| **Enable Extra Builtins** | Provide IntelliSense with declarations for built-in intrinsic functions not included in Visual Studio's Clang support. Enabling this option may cause the default 32-bit IntelliSense implementation to run out of memory. 64-bit IntelliSense support can be enabled via **Tools**->**Options**->**Text Editor**->**C/C++**->**IntelliSense**->**Enable 64-bit IntelliSense**. |
| **Clang Mode** | Force IntelliSense to work in **Clang Mode**. Disable this option to revert IntelliSense to using the default MSVC x64 mode. |

# VSI Project Settings - Debugging

The debugging section enables you to specify options for debugging your project, such as the path to the executable to debug and the arguments to be passed to it.

| **Option** | **Description** | |
| --- | --- | --- |
| **Debugger to launch** | Specifies the debugger to use when debugging the project. For the PlayStation®5 platform, this will default to **PS5 Standard Debugger**. | |

There are three pages of debugger settings chosen from the **Debugger to launch** drop-down list:

* **[PS5 Standard Debugger](vsi-project-settings-ps5-standard-debugger.html)**
* **[PS5 Application Debugger](vsi-project-settings-ps5-application-debugger.html)**
* **[PS5 Launch File Debugger](vsi-project-settings-ps5-launch-file-debugger.html)**

# VSI Project Settings - PS5 Standard Debugger

| **Setting** | **Description** |
| --- | --- |
| **Target Name** | Specifies the DevKit to debug. Refer to [Debugging with Multiple DevKits](building-running-and-debugging-an-application-in-visual-studio.html#visual-studio-integration-for-ps5-users-guide_3__section_qhj_wpv_xgc). |
| **Executable Arguments** | Specify any command line arguments to be passed to the application. |
| **Host Executable** | The path to the executable to debug on the Host PC. |
| **Working Directory (/app0)** | Selects how the Working Directory is defined. Either using a local directory path or mapping file, a Workspace, or a GP5 File.  Options are:   * Use Local Path * Use Workspace * Use GP5 File   Note: UI will update based on the choice made in this list box. |
| **Local Path** | Specifies the local directory path to use for the [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory). This setting is overridden if a working directory is specified in the optional mapping file.  Note: Only displayed when [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory) option is set to **Use Local Path**. |
| **Workspace** | Specifies the name of the Standalone Workspace.  Note: Only displayed when the [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory) option is set to **Use Workspace**. |
| **Workspace Storage** | Specifies the Workspace storage type.  Options are:   * Auto (default) * Internal * External (M.2 SSD) |
| **GP5 File** | Specifies the GP5 File path that defines the layout of the [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory)  Note: Only displayed when the [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory) option is set to **Use GP5 File**. |
| **Content Config Label** | Specifies the `content_config_label` value from the GP5 file to use instead of the primary content config. If blank, the GP5 file will use the primary content config.  Note: Only displayed when the [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory) option is set to **Use GP5 File**. |
| **Mapping File** | Specifies the path to the optional Mapping File.  Note: Only displayed when the [Working Directory (/app0)](vsi-project-settings-ps5-standard-debugger.html#visual-studio-integration-for-ps5-users-guide_2_2_3_1__0workingdirectory) option is set to **Use Local Path**. |
| **Mirroring Mode** | Specifies whether the game process waits for the whole file to be transferred from the host on reads or instead blocks when data is not yet available.  Not used when the **Workspace** option is selected. |
| **Save Data Root Directory** | Specifies an override of the Save Data Root Directory. Not used when a **Mapping File** is specified, or the **Workspace** option is selected. |
| **System Library Verification** | Performs argument validation for specific SDK functions. When debugging, an Exception dialog will be displayed on failure. When running, "Warn" will generate a console message, and "Abort" will also exit the process. |
| **Override Flexible Memory Size** | Override the value of `flexibleMemorySize` parameter given in the `param.json`, with the specified size in MiB. |
| **Extended Direct Memory Size** | Override the value of the 'Extended DMEM size setting' in the Target Settings application. |

# VSI Project Settings - PS5 Application Debugger

| **Setting** | **Description** |
| --- | --- |
| **Target Name** | Specifies the DevKit to debug. Refer to [Debugging with Multiple DevKits](building-running-and-debugging-an-application-in-visual-studio.html#visual-studio-integration-for-ps5-users-guide_3__section_qhj_wpv_xgc). |
| **Title ID** | Specifies the Title ID of the installed package to debug. |
| **Executable Arguments** | Specify any command line arguments to be passed to the application. |
| **Executable Load Location** | Specifies where to load the application's executable from.  Options are:   * Auto (Working Directory) * Host * Package   When set to **Auto** the system will load the executable from the working directory of the application  When set to **Host**, the Host Executable option will be displayed.  When set to **Package**, the Package Executable option will be displayed. |
| **Host Executable** | The path to the executable to debug. Used when **Executable Load Location** is set to "Host". |
| **Package Executable** | The path to the executable to debug. Used when **Executable Load Location** is set to "Package". |
| **Executable overlay directory** | Optionally specifies the host directory path to be used when the game process loads an executable. For example when calling `sceSystemServiceLoadExec()` or `sceKernelLoadStartModule()`. The directory path is substituted for `/app0`. |
| **Workspace Overlay** | Optionally specifies the name of a Workspace to overlay the installed application when debugging. |
| **Workspace Overlay Storage** | Specifies the storage type for the Workspace Overlay when given. Options are:   * Auto * Internal * External (M.2 SSD) |
| **Override Param File (param.json)** | Optionally specifies a host file path to a parameter overrides JSON file. Application launch parameters specified in this file will override those of the installed Package's param.json file.  Note: Not all sce\_sys/param.json parameters can be overridden. Refer to [Param.json File Specification - Using the Param File (param.json) - Overriding the Param File of the Application Package (Application Development Support)](../Param_Json-Specification/overriding-the-param-file-of-the-application-package-applica.html) for the full list of possible parameters. |
| **System Library Verification** | Performs argument validation for specific SDK functions. When debugging, an Exception dialog will be displayed on failure. When running, "Warn" will generate a console message, and "Abort" will also exit the process. |
| **Override Flexible Memory Size** | Override the value of the `flexibleMemorySize` parameter given in the `param.json`, with the specified size in MiB. |
| **Extended Direct Memory Size** | Override the value of the 'Extended DMEM size setting' in the Target Settings application. |

# VSI Project Settings - PS5 Launch File Debugger

| **Setting** | **Description** |
| --- | --- |
| **Target Name** | Specifies the DevKit to debug. Refer to [Debugging with Multiple DevKits](building-running-and-debugging-an-application-in-visual-studio.html#visual-studio-integration-for-ps5-users-guide_3__section_qhj_wpv_xgc). |
| **Launch File** | The path to the PlayStation®5 launch file to use for debugging settings. For details of the launch file format, refer to [Target Management Applications UI Overview - Appendix A - .ps5launch File Format](../TM_Applications_UI-Overview/appendix-a-ps-5launch-file-format.html). |
| **Executable Arguments** | The command line arguments to pass to the application. Note: Supplying command line arguments from both this property and from the Launch File will cause an error. |

# VSI Project Settings - VC++ Directories

The VC++ section enables you to specify the paths important to the build system, for example executable and library locations.

| **Setting** | **Description** |
| --- | --- |
| **Executable Directories** | Specify the paths to search for executable files required by the build process. Corresponds to the PATH environment variable. |
| **Include Directories** | Specify the paths to search for include files required by the build process. Corresponds to the INCLUDE environment variable. |
| **Library Directories** | Specify the paths to search for library files required by the build process. Corresponds to the LIB environment variable. |
| **Source Directories** | Specify the paths to search for source files to use for IntelliSense. |

# VSI Project Settings - C/C++

The C/C++ section enables you to specify settings to control the compiler during the build process for projects and files. It is split into the following categories:

* [General](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_vbc_fqq_ygc)
* [Optimization](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_avj_fqq_ygc)
* [Code Generation](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_zwr_fqq_ygc)
* [Language](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_v3y_fqq_ygc)
* [Precompiled Headers](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_bb2_gqq_ygc)
* [Code Coverage](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_sym_gqq_ygc)
* [Advanced](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_z1x_gqq_ygc)
* [Static Analyzer](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_ify_hqq_ygc)
* [Command Line](vsi-project-settings-c-c-plus-plus.html#visual-studio-integration-for-ps5-users-guide_2_2_5__section_xmf_3qq_ygc)

## General

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Additional Include Directories** | Specifies one or more directories to add to the include path; use a semi-colon delimited list if more than one. | `-IPath[;Path2 … ]` |
| **Preprocessor Definitions** | Specifies one or more preprocessor defines; use a semi-colon delimited list if more than one. | `-Dname=value[;value … ]` |
| **Forced Include Files** | Specifies one or more forced include files. | `-include Path` |
| **Generate Debug Information** | Specifies if the compiler will generate debugging information. | `-g` |
| **Inline Function Debug Information** | Select whether to generate debug information for inlined functions. Debug information with optimized code is improved, but executable size and compile time are increased.  Default is Enabled. | `-ginlined-scopes | -gno-inlined-scopes` |
| **Warnings** | Selects the extent of warnings issued during compilation. Note that errors are always displayed. | `-Wall` |
| **Extra Warnings** | Generates extra warnings for certain events not included when using the `-Wall` switch. | `-Wextra` |
| **Enable Specific Warnings** | Specifies the names of specific warnings to enable; in a semi-colon delimited list. | `-W[warning]` |
| **Disable Specific Warnings** | Specifies the names of specific warnings to disable; in a semi-colon delimited list. | `-Wno-[warning]` |
| **Promote Specific Warnings to Errors** | Specifies the names of specific warnings to be promoted to errors; in a semi-colon delimited list. | `-Werror=[warning]` |
| **Treat Warnings As Errors** | Enables the compiler to treat warnings as errors. | `-Werror` |
| **Enable Fix-It hints** | Enable the compiler to provide hints for possible fixes for warning and error diagnostic messages. | `-fdiagnostics-parseable-fixits` |
| **Extended Diagnostic Messages** | Displays the line of source code related to each error or warning message. In addition, a caret (^) character points to the position of the problem in the line of source code. | `-fcaret-diagnostics | -fno-caret-diagnostics` |
| **Object File Name** | Specifies a name to override the default object file name; can be file or directory name. | `-o [Path]FileName` |
| **Multi-processor Compilation** | Enables multiple source files to be compiled in parallel, limited by the value specified in **Max Compilations**. |  |
| **Max Compilations** | Specifies the maximum number of concurrent compiles to use for this project. If no value is given the value of the global setting **Maximum concurrent C++ compilations** is used. |  |
| **Allow Distributed Compilation** | Specifies if distributed compilation is allowed during a distributed build. Source files will always be compiled locally if disallowed. |  |

## Optimization

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Optimization Level** | Specifies the code optimization level. | `-O{0|1|2|3|g|2g|s|z}` |
| **Extend Lifetimes** | Keeps local variables and function parameters alive throughout scopes, trading some performance for improved debugging. Also enables `-fextend-this-ptr`.  Enabled with `-Og` and `-O2g`. | `-fextend-lifetimes` |
| **Extend This Pointer** | Keeps the '`this`' pointer alive throughout the entire life of a member function and makes its value visible in the debugger throughout the entire function's scope.  Enabled with `-Og` and `-O2g`. | `-fextend-this-ptr` |
| **Fast Math** | Turns on a number of switches that may speed up floating point math.  Warning: Uses possibly unsafe assumptions for arguments and results, and may violate IEEE or ANSI standards. | `-ffast-math` |
| **No Strict Aliasing** | Do not use the strictest aliasing rules. Assume objects of different types may reside at the same address. Trades code performance for safety. | `-fno-strict-aliasing` |
| **Unroll Loops** | Specifies whether to enable or disable unrolling loops whose iterations can be determined at compile time, or upon loop entry. Trades code size for potentially faster code. | `-funroll-loops | -fno-unroll-loops` |
| **Enable Support for LTO** | Delay analysis and optimization until link time. This enables optimizations to be performed across multiple compilation units. May significantly increase link time. Not compatible with Edit and Continue. | `-flto` |

## Code Generation

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Enable C++ Exceptions** | Enable Exception handling in C++ code. | `-fexceptions` |
| **Enable Data Sections** | Generate a separate named section for each data item. Unused data sections can be stripped by the linker. | `-fdata-sections | -fno-data-sections` |
| **Enable Function Sections** | Generate a separate named section for each function defined. Unused function sections can be stripped by the linker. | `-ffunction-sections | -fno-function-sections` |

## Language

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Enable Run-Time Type Information** | Adds code for checking C++ object types at run time (runtime type information). Automatically enabled with Exceptions usage. | `-frtti | -fno-rtti` |
| **C++ Language Standard** | Specifies the language standard to use for C++ source. | `-std=c++14 | -std=gnu++14 | -std=c++17 | -std=gnu++17 | -std=c++20 | -std=gnu++20` |
| **C Language Standard** | Specifies the language standard to use for C source. | `-std=c89|gnu89|c99|gnu99|c11|gnu11|c17|gnu17` |
| **Check ANSI Compliance** | Checks C/C++ code for ANSI compliance. | `-ansi` |

## Precompiled Headers

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Precompiled Header** | Enables creation or use of a precompiled header during the build. No object file will be generated when creating a PCH file. | `-x c++-header -include-pch` |
| **Precompiled Header Output File** | Specifies the path and/or name of the generated precompiled header file. |  |
| **PCH Instantiate Templates** | Instantiate templates when creating the Precompiled Header file. Source files using this PCH will not duplicate these instantiations, improving build speed. | `-fpch-instantiate-templates` |
| **PCH Code Generation** | Perform code generation when creating the Precompiled Header file. Source files using this PCH will share the generated code, improving build speed. A separate object file will be created and automatically linked. | `-fpch-codegen` |
| **PCH Debug Information** | Generate Debug Information for types when creating the Precompiled Header file. A separate object file will be created and automatically linked. | `-fpch-debuginfo` |

## Code Coverage

| **Setting** | **Description** | **Command Line Equivalent** |
| --- | --- | --- |
| **Enable Code Coverage** | Enables instrumented generation of code coverage data at runtime. Instrumented code will have a performance penalty.  Note: Use both switches. | `-fcoverage-mapping -fprofile-instr-generate=[file]` |
| **Code Coverage Output File** | Specifies the Target-side file path to where raw profile data will be written when Code Coverage has been enabled. |  |

## Advanced

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Ignore Standard Include Paths** | Do not search the standard system directories for system header files. Only the include directories specified using -I will be searched. | `-nostdinc` |
| **Compile As** | Specifies the compile language option for `.c` and `.cpp`files. | `-x language` |
| **Default Char Unsigned** | Sets whether the unqualified char type is treated as signed or unsigned.  Note: This option is not ABI compliant and should not be used for submissions. | `-funsigned-char` |
| **Enable MS Extensions** | Enables some non-standard MS VC++ extensions.  Note: This option is not ABI compliant and should not be used for submissions. | `-fms-extensions` |

## Static Analyzer

The Static Analyzer section provides settings to control static analysis for projects and files. These settings only have an effect during Analysis when initiated from the Issues Window. Unlike the other settings for C/C++, they are not used as part of a normal build. Refer to [Clang Static Analysis](clang-static-analysis.html) for further details on using the static analysis with your projects.

| **Setting** | **Description** |
| --- | --- |
| **Analyzer Checkers** | Specifies the checker packages or individual checkers to use during static analysis; use a semi-colon delimited list if more than one.  Additional checker packages can be added, or defaults removed, by supplying a new set of checker packages.  For C/C++ Static Analysis the default set of checkers is `core`, and `cplusplus`. Refer to Static Analyzer Reference for more information. |
| **Disable Checkers** | Specifies one or more individual checkers to disable from those currently enabled; use a semi-colon delimited list if more than one. |
| **Analysis Level** | Specifies the level for static analysis. Deeper levels perform more exhaustive searching to find potential defects.  The default analysis level, `'Standard'`, is a good compromise between speed and analysis depth. |
| **Allow Static Analysis** | Specifies whether static analysis is allowed. It can be disabled for individual source files, or for whole projects.  Default is for all files to be included. |

## Command Line

| **Setting** | **Description** |
| --- | --- |
| **Additional Options** | Specify additional compiler command line options not provided by the other properties. The options format must be valid. |

# VSI Project Settings - Linker

The Linker section of the Configuration Properties enables you to specify settings to control the linker during the build process.

## General

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Output File** | Specifies the output file name. | `-o FileName` |
| **Additional Library Directories** | Specifies one or more additional paths to search when looking for libraries specified either as a file name, or when using the `-l[namespec]`switch notation. For more than one additional path, use a semi-colon delimited list. | `-L Path` |
| **Enable Edit and Continue** | Generates additional data required for Edit and Continue (EnC) debugger support. Enabling this switch may increase link time. Refer to [Debugger User's Guide - Debugging Using Edit and Continue](../Debugger-Users_Guide/debugging-using-edit-and-continue.html) for more information. | `--enc` |
| **Debug Info and Symbol Stripping** | Enables debugging information stripping and symbol stripping from the output ELF file. | `-S | -s` |
| **Unused Function and Data Stripping** | Enables the stripping of unused function code and also data from the output elf file. | `--gc-sections` |
| **Duplicate Function and Data Stripping** | Enables the additional stripping of identical function code and read-only data sections from the output ELF file. | `--icf=all`  `--ignore-data-address-equality` |
| **Generate Map File** | Enables the generation of a map file. | `--Map` |
| **Map File Name** | Specifies a path and filename for the map file. |  |
| **Addressing** | Specifies Address Space Layout Randomization (ASLR) usage. | `--addressing=non-aslr` |
| **Additional Dependencies** | Specifies additional items to add to the link line; configuration specific.  Use library file names, library paths, or use `-l` with LibraryName for system libraries. LibraryName is the filename of a system library, without "`lib`" and "`.a`". For example, to add `libPerf.a` as an additional dependency, enter "`-lPerf`". | `-l LibraryName | PathToLibraryFile | FileName` |
| **Link Library Dependencies** | Specifies whether library outputs from project dependencies are automatically linked in. |  |
| **Use Library Dependency Inputs** | Specifies whether inputs to the librarian tools are used rather than the library file itself when linking in library outputs of project dependencies. |  |

## Optimization

| **Setting** | **Description** | **Command Line Equivalent** |
| --- | --- | --- |
| **Link Time Optimization** | Select the mode to use when linking source compiled with Link Time Optimization enabled.  Options available are:   * **Full**(default) * **Thin** * **Thin using SN-DBS**   If set to *Full*, this provides the highest level of optimization.  If set to *Thin*, this provides less optimization for a shorter link time.  If set to *Thin using SN-DBS*, distributed build support will be leveraged. | `--lto={full|thin} [--thinlto-distribute]` |
| **Enable Thin LTO Caching** | Use caching for Thin LTO compiles to improve incremental link times.  Options available are:   * **No** * **Yes**   Cached files will be stored under the directory `$(IntDir)$(ProjectName).lto` and removed on **Clean** or **Rebuild**. | `-lto-thin-cache=<dir>` |
| **Limit Cache by Size** | When pruning the Thin LTO cache, limit it to the specified size. You must include a unit postfix of '`k`' for KiB, '`m`' for MiB, or '`g`' for GiB. eg '`500m`'. | `--thinlto-cache-policy=cache_size_bytes=<size>{k|m|g}` |
| **Limit Cache by % Disk Space** | When pruning the Thin LTO cache, limit it to the percentage of available disk space specified. You must postfix your value with a '`%`'. eg '`10%`'. | `--thinlto-cache-policy=cache_size=<percentage>%` |
| **Limit Cache by File Count** | When pruning the Thin LTO cache, limit it to the specified number of files. | `--thinlto-cache-policy=cache_size_files=<count>` |
| **Cache Pruning Interval** | Specify the length of time that needs to elapse before the Thin LTO cache is pruned. You must include a unit postfix of '`s`' for seconds, '`m`' for minutes, or '`h`' for hours. eg '`30m`'. | `--thinlto-cache-policy=prune_interval=<time>{s|m|h}` |
| **Cache Pruning Expiry** | Specify the length of time since an entry in the Thin LTO cache was last accessed before it is pruned. You must include a unit postfix of '`s`' for seconds, '`m`' for minutes, or '`h`' for hours. eg '`1h`'. | `--thinlto-cache-policy=prune_after=<time>{s|m|h}` |

## Advanced (ELF Projects)

| **Setting** | **Description** | **Command Line Equivalent** |
| --- | --- | --- |
| **Output Format** | Select the output format for the linker to generate. | `--oformat=[format]` |
| **Export Library** | Specify the name of the export library generated by this project. When this project is specified as a dependency of another, the export library will be linked in. |  |
| **Ignore Export Library** | Specifies that the export library generated by this configuration should not be imported into dependent projects. |  |

## Advanced (PRX Projects)

| **Setting** | **Description** | **Command Line Equivalent** |
| --- | --- | --- |
| **Output Format** | Select the output format for the linker to generate. | `--oformat=prx` |
| **PRX Stub Output Directory** | Specify the directory for the PRX Stub generated by this project. When this project is specified as a dependency of another, the export library will be linked in. | `--prx-stub-output-dir` |
| **Ignore PRX Stub Library** | Specifies that the PRX stub generated by this configuration should not be imported into dependent projects. |  |

## Command Line

| **Setting** | **Description** |
| --- | --- |
| **Additional Options** | Specify additional linker command line options not provided by the other properties. The options format must be valid. |

# VSI Project Settings - Librarian

The Librarian section enables you to specify settings to control building of static library configurations.

From SDK 0.85, VSI will default to using `prospero-llvm-ar` instead of `prospero-snarl` if installed. `prospero-snarl` has been deprecated. You are able to revert to using `prospero-snarl` by hand-editing your projects to enable backwards compatibility with previous SDKs.

Note:

The librarian section will only appear when a static library project configuration is selected.

## General

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Output File** | Specifies the output file name. | -o `FileName` |
| **Additional Dependencies** | Specifies additional items to add to the link line; configuration specific. |  |
| **Disable Specific Warnings** | Comma-delimited list of warning numbers to be disabled. | -`-disable-warning=num1 [,num2, …]` |
| **Generate Thin Archive** | Specifies the project will output a "Thin Archive" file. This library type stores references to its members rather than embedding them. They are faster to create compared to normal libraries, but are not portable. |  |
| **Link Library Dependencies** | Specifies whether library outputs from project dependencies are automatically linked in. |  |

# VSI Project Settings - Custom Build Steps and Build Events

You can specify additional build steps for a configuration using the **Build Events**, **Custom Build Step** and **Custom Build Tool** sections of the project property pages.

For more information on these sections, refer to [Understanding Custom Build Steps and Build Events](http://msdn.microsoft.com/en-us/library/e85wte0k.aspx) in the Visual Studio help pages.

# VSI Project Settings - Wave Compiler

You can specify settings to control the Wave Compiler during the build process for projects and files.

Files added to the project with a `.pssl` extension will be compiled using VSI Wave support.

## General

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Additional Include Directories** | Specifies one or more directories to add to the include path; use semi-colon delimited list if more than one. | -I[path] |
| **Forced Include Files** | Specifies one or more forced include files. | `-include [path]` |
| **Entry Point** | Specifies the function name to use for the entry point. The default is 'main'. | `-entry [function]` |
| **Profile** | Specifies the profile to use for the shader. | `-profile [profile]` |
| **Preprocessor Definitions** | Specifies one or more preprocessor defines; use semi-colon delimited list if more than one. | `-D[name[=value]]` |
| **Treat Warnings as Errors** | Enables the compiler to treat warnings as errors. | `-Werror` |
| **Performance Warnings** | Enables warnings about potential performance hazards. | `-Wperf` |
| **Localization** | Select the language to use for warning and error messages. | `-lang [en|jp]` |
| **Multi-processor Compilation** | Enables multiple source files to be compiled in parallel limited by the value specified in **Max Compilations**. |  |
| **Max Compilations** | Specifies the maximum number of concurrent compiles to use for this project. If no value is given, the global VC++ setting for **Maximum concurrent C++ compilations** is used. |  |
| **Allow Distributed Compilation** | Specifies if distributed compilation is allowed during a distributed build. Source files will always be compiled locally if disallowed. |  |

## Optimization

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Optimization Level** | Select option for code optimization. | `-O0..4` |
| **Fast Math** | Enable algebraic transforms (for example, use 'a \* 2' in place of 'a + a'). | `-fastmath | -nofastmath` |

## Output

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Output File Name** | Specifies a name to override the default output file name. | `-o` [`file`] |
| **Generate Symbol Cache File** | Specifies if a symbol cache file should be output for shader association and debugging. | `-debug-info` |
| **Symbol Cache Directory** | Specifies the directory to be used for the symbol cache. |  |
| **Embed Shader Binaries** | Embed shader binaries into the executable or archive. |  |

## Deprecated

| **Setting** | **Description** | **Command Line Equivalent** |
| --- | --- | --- |
| **Generate Header File** | Use the bin2h tool to generate a C Header File from the shader binary created by compilation. |  |
| **Header File Name** | Specifies the name for the generated header file. |  |
| **Additional Options for bin2h** | Specify additional command line options to be passed to the bin2h tool when generating the header file. |  |

## Command Line

| **Setting** | **Description** | Command Line Equivalent |
| --- | --- | --- |
| **Additional Options** | Specify additional compiler command line options not provided by the other properties. The options format must be valid. |  |

# VSI Project Settngs - Intel® Implicit SPMD Program Compiler (ISPC)

New ISPC files can be added to the project by selecting **PS5** from the **New Item** file templates. Afterwards, the ISPC section will be available in the project. This enables you to specify settings to control the ISPC compiler during the build process.

## General

| Setting | Description | Command Line Equivalent |
| --- | --- | --- |
| **Additional Include Directories** | Specifies one or more directories to add to the include path; use a semi-colon delimited list if specifying more than one directory. | `-IPath[;Path2 … ]` |
| **Preprocessor Definitions** | Specifies one or more preprocessor defines; use a semi-colon delimited list if specifying more than one preprocessor define. | `-Dname=value[;value … ]` |
| **Generate Debug Information** | Specifies whether the compiler will generate debugging information. You must also change linker settings appropriately to match this setting. | `-g` |
| **Warnings** | Selects the extent of warnings issued during compilation; errors are always displayed. | `--wno-perf, --woff` |
| **Treat Warnings as Errors** | Enables the compiler to treat warnings as errors. | `--werror` |
| **Object File Name** | Specifies a name to override the default object file name; this can be a file name or directory name. | `-o[file path]` |
| **Multi-processor Compilation** | Enables multiple source files to be compiled in parallel, limited by the value specified in **Max Compilations**. |  |
| **Max Compilations** | Specifies the maximum number of concurrent compiles to use for this project. If no value is given, the global VC++ setting for **Maximum concurrent C++ compilations** is used. |  |
| **Allow Distributed Compilation** | Specifies whether distributed compilation is allowed during a distributed build. If disallowed, source files will always be compiled locally. |  |

## Optimization

| Setting | Description | Command Line Equivalent |
| --- | --- | --- |
| **Optimization Level** | Select option for code optimization. | `-O{0|1|2|3}` |
| **Fast Math** | Activates a number of switches that may speed up floating point math. Uses possibly unsafe assumptions for arguments and results, and may violate the IEEE 754 standard. | `--opt=fast-math` |
| **Unroll Loops** | Unroll loops whose iterations can be determined at compile time, or upon loop entry. Potentially improves code performance at the cost of increased code size. | `--opt=disable-loop-unroll` |
| **Assertions** | Specifies whether to retain `assert` statements in the output. | `--opt=disable-assertions` |
| **Fused Multiply-Add** | Specifies whether to enable fused multiply-add (FMA) instructions. | `--opt=disable-fma` |
| **Faster Masked Vector Loads** | Enable faster masked vector loads by removing per-element mask checks. There is a risk of invalid memory access unless you account for the full range of a vector, excluding its mask. | `--opt=fast-masked-vload` |
| **Force Aligned Vector Loads/Stores** | Always issue aligned vector load and store instructions. | `--opt=force-aligned-memory` |
| **Reset FTZ/DAZ Flags** | Reset FTZ/DAZ flags on ISPC extern function entrance / restore on return. | `--opt=reset-ftz-daz` |
| **Enable Support for LTO** | Delay analysis and optimization until link time. This enables optimizations to be performed across multiple compilation units. May significantly increase link time. Not compatible with "Edit and Continue". | `--lto` |

## Code Generation

| Setting | Description | Command Line Equivalent |
| --- | --- | --- |
| **Force Memory Alignment** | Force alignment in memory allocations routine. | `--force-alignment=[n]` |

## Output

| Setting | Description | Command Line Equivalent |
| --- | --- | --- |
| **Generate Header Output File** | Generate a header file containing declarations of callable functions and defined types. You can then include the generated header file in C/C++ source with a #include. | `-h [file path]` |
| **Header Output File Path** | Specifies the path and name of the generated header file. |  |

## Command Line

| Setting | Description |
| --- | --- |
| **Additional Options** | Specify additional compiler command line options not provided by the other properties. The options format must be valid. |

# Configuring Global Build Settings in Visual Studio

Note:

If you have also installed a version of **VSI for PlayStation®4** SDK 7.000 or earlier, then the options left pane will show **ProDG VSI** instead of **PlayStation**. This can be resolved by updating **VSI for PlayStation®4** to a newer version when released.

To configure global build settings for projects:

1. On the **Tools** menu, click **Options**.
2. In the left pane, expand **PlayStation**, and then select a group of settings.
3. In the right pane, configure settings, and then click **OK**.

The PlayStation section contains the following settings for projects:

* [Distributed Building](vsi-global-build-settings-distributed-building.html). Configure distributed builds for SN-DBS or IncrediBuild.
* [General](vsi-global-build-settings-general.html). Display console output in the **Output** window when not debugging.

# VSI Global Build Settings - Distributed Building

The Distributed Building section contains the following settings:

## General

| **Setting** | **Description** |
| --- | --- |
| **Always perform a distributed build for PlayStation projects** | Builds all PlayStation projects by using the selected distributed build system. |
| **Max number of projects to build in parallel for distributed builds** | Specifies the number of projects in a solution that can be built in parallel for an SN-DBS build. This value can typically be higher than local builds. |
| **Distributed build preference** | Specifies SN-DBS or IncrediBuild for building projects if both are installed. |

## IncrediBuild for Dev Tools

| **Setting** | **Description** |
| --- | --- |
| **Enable IncrediBuild for Dev Tools support** | Specifies if VSI should offer distributed build support using IncrediBuild. IncrediBuild offers its own menu items and keyboard shortcuts for building PlayStation®5 projects. If VSI support is disabled, it will not add its own menu items for performing distributed builds when SN-DBS is not installed. |
| **Profile XML file path** | Specifies a custom Profile XML file for IncrediBuild to distribute custom tools. For more information, refer to the [IncrediBuild user guide](https://docs.incredibuild.com/win/latest/windows/index.html). |

# VSI Global Build Settings - General

The General section contains the following settings:

| **Setting** | **Description** |
| --- | --- |
| **Disassembly output mode** | Specifies whether to annotate disassembly code with source in Disassembly mode.  Available options are **Plain Disassembly only** or **Mixed Assembly with Source**. |

# Determining Build Settings Used in Visual Studio

The settings used during a build can be output to a log file, stored in the intermediate directory. The compiler and linker command line options can be written to the log, as well as any pre-build and post-build events.

To output the build setting to the log file, the Visual Studio log verbosity setting needs to be "Detailed" or "Diagnostic."

To set the Visual Studio log verbosity:

1. On the **Tools** menu, click **Options**.
2. In the left pane, expand **Projects and Solutions**, and then click **Build and Run**.
3. In the right pane, set **MSBuild** project build log file verbosity to **Normal**, **Detailed**, or **Diagnostic**, and then click **OK**.

The location of the log file is set in the **Build Log File** project property, and defaults to:

```
\<Platform>_<Config>\<ProjectName>
```

For example:

```
\Prospero_Debug\single_user.log
```