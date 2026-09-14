# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/performing-a-distributed-command-line-build.html

# Building Projects from the Command Line

The following topics explain how to perform a local and distributed command line build:

* [Performing a Local Command Line Build](performing-a-local-command-line-build.html)
* [Performing a Distributed Command Line Build](performing-a-distributed-command-line-build.html)

# Performing a Local Command Line Build

You can build projects from the command line. This is performed by calling devenv,
specifying the solution file (`.sln`), and other options.

In Visual Studio 2026, devenv is located in the following default path:

```
%PROGRAMFILES%\Microsoft Visual Studio\18\{Enterprise|Professional}\Common7\IDE
```

In Visual Studio 2022, devenv is located in the following default path:

```
%PROGRAMFILES%\Microsoft Visual Studio\2022\{Enterprise|Professional}\Common7\IDE
```

In Visual Studio 2019, devenv is located in the following default path:

```
%PROGRAMFILES(x86)%\Microsoft Visual Studio\2019\{Enterprise|Professional}\Common7\IDE
```

## Syntax

```
devenv [Path]SolutionFile /{build|rebuild|analyze[:{plist|html}]} SolutionConfig
```

## Arguments

Arguments

| Argument | Description |
| --- | --- |
| `/build` | Builds the solution. |
| `/rebuild` | Rebuilds the solution. |
| `/analyze` | Invokes Clang Static Analysis. By default, this will produce PLIST files. By specifying `/analyze:html`, HTML analysis files will be produced. |

## Remarks

When the argument value contains spaces, you must enclose it in double quotation
marks ("").

## Example

```
devenv "\MySolutions\MySolution.sln" /build "Debug|Prospero"
```

This example builds the solution `MySolution` using the **Debug**
solution configuration, on the `Prospero` platform.

For more information about command line options supported by devenv, refer to the
Visual Studio documentation.

# Performing a Distributed Command Line Build

Visual Studio Integration provides tools to build projects from the command line by using
either SN-DBS or IncrediBuild for Dev Tools. This tool accepts similar command line
options to devenv.

In Visual Studio 2026, the tool is called `vs18build` and is located in the following path:

```
%SCE_ROOT_DIR%\Common\SceVSI-VS18\bin
```

In Visual Studio 2022, the tool is called
`vs17build`
and is located in the following path:

```
%SCE_ROOT_DIR%\Common\SceVSI-VS17\bin
```

In Visual Studio 2019, the tool is called `vs16build` and is located in the following path:

```
%SCE_ROOT_DIR%\Common\SceVSI-VS16\bin
```

## Syntax

```
[vs16build|vs17build|vs18build] [Path]SolutionFile [/{build|rebuild|clean|analyze[:{plist|html}]}] SolutionConfig [/projectprojectfile] [/projectconfigname]  [/{distrib|sn-dbs|incredi}]  [/useenv] [/msbuild commandline]
```

## Arguments

Arguments

| Argument | Description |
| --- | --- |
| `/build` | Ignored, provided for compatibility with devenv. |
| `/rebuild` | Rebuilds the solution or project. |
| `/analyze` | Invokes Clang Static Analysis. By default, this will produce PLIST files. By specifying `/analyze:html`, HTML analysis files will be produced. |
| `/clean` | Cleans the solution or project. |
| `/project projectfile` | Specify the project to build, using the path to a `.vcxproj` file. |
| `/projectconfig name` | Specify the project to build, using the project name from within the solution. |
| `/distrib` | Use any available distributed build system. |
| `/sn-dbs` | Use SN-DBS for builds. |
| `/incredi` | Use IncrediBuild for builds. |
| `/useenv` | Use the PATH environment variable instead of IDE VC++ Directories. |
| `/msbuild` | Any text following this argument will be passed directly to MSBuild. |

## Remarks

When the argument value contains spaces, you must enclose it in double quotation
marks ("").

## Example

```
vs16build "\MySolutions\MySolution.sln" "Debug|Prospero" /sn-dbs
```

This example uses SN-DBS to build the solution `MySolution`, using the
**Debug** solution configuration, on the `Prospero`
(PlayStation®5) platform.