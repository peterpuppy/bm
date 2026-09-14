# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/basic-information-on-programming-environments.html

# Basic Information on Programming Environments

This topic provides basic information about the programming environments needed for application development on a DevKit. Concepts covered include source code file formats, standard libraries, error handling, and points to note about libraries for development only. Some information also applies to TestKits that have been set to Assist Mode.

# File Format

The format of source files provided by the SDK is as follows.

* Character encoding: UTF-8 with BOM
* Linefeed encoding: CR+LF

Because the host tools provided by SIE, including the compiler, support only UTF-8 encoding, also use UTF-8 encoding for the source code of applications.

# ABI

Refer to the [CPU Compiler ABI Overview](../CPU_Compiler_ABI-Overview/__document_toc.html) document regarding the PlayStation®5 ABI.

# TTY

Applications can use standard TTY input/output as well as standard error output (STDIN/STDOUT/STDERR).

# Standard Libraries

Two versions of the C++ standard library are provided. Version 1 (v1) supports C++14 and C++17 (some features), and version 2 (v2) supports C++20 and C++23 (some features). The version that is used corresponds to the C++ language mode specified to the compiler. For details, refer to [C++ Standard Library v2 Migration Guide](../Cpp_Standard_Library_V2-Migration_Guide/__document_toc.html).

A common implementation is used for the C standard library regardless of the C++ language mode.

## Heap Management

Heap management is implemented using dlmalloc (<http://gee.cs.oswego.edu/dl/html/malloc.html>) with additional proprietary features. For details about the features, refer to the [C and C++ Standard Libraries: Overview and Reference](../C_and_Cpp_standard_libraries/__document_toc.html) document.

## Restrictions

The C/C++ standard library specifications have been scaled down in regard to the following points. This is not expected to change in the future.

* The locale is set to C locale by default and can be set only to C locale.
* If another locale is set, the C/C++ standard library will return an error, or an exception will occur.
* fenv.h does not exist.

# Libraries for Development Only

Some of the libraries included in the SDK are provided strictly for application development/debugging purposes and cannot be used in applications for end users. The "nosubmission" string is included in the filenames of such libraries; do not link the files of such libraries in a program to be master submitted.

Example: libSceDeci5\_nosubmission\_stub\_weak.a

# Error Handling During Execution

## Error Processing

As a general rule, applications are requested to properly handle errors that occur during execution and restore appropriate processing. If an error occurs that is impossible or difficult to recover from, the application is required to notify users of the error and stop processing according to the requirements in the TRC.

To notify users of errors, use the ErrorDialog library. By passing the hexadecimal error code returned by an SDK library function to the relevant ErrorDialog library function, an appropriate message and the short error code will be displayed.

## Error Code Structure

The errors that occur in libraries included in the SDK and in the system software are each allocated a hexadecimal error code with a macro constant for handling by applications, as well as a short error code to display for users.

| **Macro constant** | **Hexadecimal error code** | **Short error code** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | CE-100002-3 |

The error codes returned by libraries and the system software are hexadecimal error codes. The hexadecimal error codes are 32-bit negative numbers with the upper 16 bits representing the library or module where the error occurred. Short error codes are character strings consisting of a two-letter facility group ("CE", "NW", "NP", etc.) and a 6+1-digit short error number connected by hyphens.

| **Short error code** | **Facility group** | **Short error number** |
| --- | --- | --- |
| CE-100002-3 | CE | 100002-3 |

Exceptional errors that are not allocated a short error number will be displayed for users as short error codes using "E2" and the hexadecimal error code connected by a hyphen.

| **Short error code** | **Facility group** | **Short error number** |
| --- | --- | --- |
| E2-80000000 | E2 | 80000000 |

Errors may be newly added with each SDK update; however, once a code structure is determined for an error, it will be carried over as-is for SDK version upgrades.

# Self-Termination of an Application

To maintain consistency in system behavior, it is prohibited for an application to self-terminate (TRC [R5093](../../../TRC/latest/TRC/R5093.html)). Although self-termination is not a problem when the Release Check Mode is Development Mode or Assist Mode, the program will stop and a core dump will be generated when an application self-terminates in Release Mode. The following processing applies as a self-termination of an application.

* Returning from `main()`
* Calling `exit()`
* Calling `_Exit()`
* Calling `quick_exit()`

When an application abnormally terminates, the cause of the abnormal termination will be displayed on the debugger screen if a debugger is connected; if not, there will be a notification about the cause within the core dump. The following processing applies as an abnormal termination of an application.

* Calling `abort()`
* Calling `assert()`
* Calling `terminate()` (termination handler will be called in Development Mode/Assist Mode)
* Calling `unexpected()` (unexpected exception handler will be called in Development Mode/Assist Mode)
* Calling a pure virtual function
* Calling `sceSystemServiceReportAbnormalTermination()`

# SIE Dialogs

The SDK contains libraries that perform various dialog displays. Because these SIE dialog libraries can be called using a nearly unified procedure, provide multilingual support, and are designed in compliance with the TRC, user interface development work can be greatly reduced by using them as appropriate. In some specific situations, the use of SIE dialogs is required.

## Common Dialogs

Many of the SIE dialog libraries are implemented based on the CommonDialog library, and the CommonDialog library must be initialized before they can be used. These dialogs are commonly referred to as the "common dialogs".

Some SIE dialogs are not common dialogs (not implemented based on the CommonDialog library). Although these dialogs are designed to be used in a similar manner as the common dialogs, there will be cases where differences with the common dialogs should be noted. Refer to each dialog library document regarding specific points to note.

# Other Information Concerning Programming

The following is an explanation on points to note regarding program creation methods and programming environments.

## Compiler Exceptions and RTTI Settings

If options are not explicitly specified, C++ exceptions and various RTTI features will be disabled. To enable exceptions, specify the `-fexceptions` option; to enable RTTI, specify the `-frtti` option.

## 32-bit Program Porting

PlayStation®5 is a 64-bit environment; the sizes of the basic datatypes may differ when porting programs that were created in a 32-bit environment. For example, uintptr\_t in a 32-bit environment is 32 bits (4 bytes), but it is 64 bits (8 bytes) in a 64-bit environment. Ensure that such differences do not cause problems.

## Building from the Command Line

vs\*build (%SCE\_ROOT\_DIR%\Common\SceVSI-VS\*\bin\vs\*build.exe, with the asterisk representing the Visual Studio version number) is provided as a tool for building a program from the command line. By using this tool, it is possible to specify and build a Visual Studio solution file from the command line. For example, a Debug build of a solution file "xxx.sln" can be performed using the following command.

```
% vs*build xxx.sln Debug /build
```

It is also possible to create ELF files by directly calling the compiler from the command prompt without using Visual Studio. The following is an example of creating program.elf by building %SRCDIR%\foo.cpp, %SRCDIR%\bar.cpp, and %LIBDIR%\libbaz.a.

```
% prospero-clang.exe -c %SRCDIR%\foo.cpp %SRCDIR%\bar.cpp 
% prospero-clang.exe foo.o bar.o -L %LIBDIR% -lbaz -o program.elf
```

Note that the libraries included in the SDK and header search path will be automatically specified by the compiler. Therefore, the following folders do not need to be specified in the command line.

* %SCE\_PROSPERO\_SDK\_DIR%\target\include
* %SCE\_PROSPERO\_SDK\_DIR%\target\include\_common
* %SCE\_PROSPERO\_SDK\_DIR%\target\lib