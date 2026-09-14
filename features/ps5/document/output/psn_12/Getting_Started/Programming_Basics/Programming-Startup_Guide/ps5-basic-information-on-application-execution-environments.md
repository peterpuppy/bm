# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-basic-information-on-application-execution-environments.html

# Basic Information on Application Execution Environments

This topic explains application operation modes and runtime modes on PlayStation®5. The resources available for use by an application differ depending on the three operation modes of Base mode, Trinity mode, and low energy mode, and these modes also give rise to differences in the features of the SDK libraries. Therefore, an understanding of operation modes is required at each of the following stages: specification design, development, and optimization.

# Application Operation Modes

There are three application operation modes: Base mode, Trinity mode, and low energy mode. An application must support at least Base mode and Trinity mode; support for low energy mode is voluntary.

An application must check in which mode it has been started up and perform processing in accordance with that mode. (Refer to "[Determining the Operation Mode with the Boot Program (eboot.bin)](ps5-determining-the-operation-mode-with-the-boot-program-ebo.html)" for details.)

When creating the param.json file, declare that the application supports Trinity mode by setting the attribute3 parameter to the appropriate value. For an application that supports low energy mode, declare that the application supports low energy mode by setting the attribute4 parameter to the appropriate value.

Refer to the [Param.json File Specification](../Param_Json-Specification/__document_toc.html) document for more information about the specifications of the param.json file.

Details about each mode are provided below.

## Base Mode

Base mode is the mode in which an application runs on the following hardware:

* Trinity Development Kit with the Force PS5 Base Mode feature (described later) enabled
* Standard PlayStation®5
* PS5 Base Development Kit/Testing Kit

## Trinity Mode

Trinity mode is the mode in which an application that supports Trinity mode runs on the following hardware:

* Trinity Development Kit with the Force PS5 Base Mode feature (described later) disabled
* PlayStation®5 Pro
* Trinity Testing Kit

## Low Energy Mode

Low energy mode is a mode in which the resources that an application can use are limited and where, in return, it operates with low power consumption.

A user can enable or disable the "Power Saver" individually for each application that supports low energy mode in the system software menu. An application that supports low energy mode will operate in low energy mode when launched if the user has enabled the "Power Saver". Whether an application is in low energy mode is determined when the application launches; an application never switches between being in low energy mode and not being in low energy mode while it is running.

An application developer can enable low energy mode on a PS5 Base Development Kit/Testing Kit or Trinity Development Kit/Testing Kit using [★Debug Settings] > [Game] > [Enable Low Energy Mode]. Applications that support low energy mode will run in that mode if this setting is enabled.

Low energy mode is enabled if either the "Power Saver" setting has been enabled by the user or the developer has enabled the relevant debug setting.

Except for the limitations on the resources that can be used, low energy mode is the same as Base mode. In other words, when an application is running in low energy mode it cannot use dedicated PlayStation®5 Pro features even if the hardware supports Trinity mode. In addition, low energy mode and VR mode cannot coexist.

**Resources that Are Limited in Low Energy Mode**

In low energy mode, resources are limited as follows:

| Resource | Limitations |
| --- | --- |
| CPUs (foreground execution) | Limited to 8 CPUs. Only CPUs 0 to 7 can be used.  The mask that allows the maximum number of CPUs to be used is defined as `SCE_KERNEL_CPUMASK_8CPU`. |
| CPUs (background execution) | Limited to 8 CPUs. CPUs 0 to 7 can be used, but only 10% of CPU5 and CPU7 can be used. |
| GDDR6 bandwidth | Limited to around half of PS5 Base mode. |
| GFX clock | Fixed to the lowest frequency of PS5 Base mode. |
| ACP | Limited to around 75% of PS5 Base mode. |
| Number of WGPs | Identical to PS5 Base mode. |

## Priority of Modes

Low energy mode is prioritized more than any other mode. When an application that supports both low energy mode and Trinity mode is launched on hardware on which low energy mode is enabled at the time, the application runs in low energy mode. The relevant relationships are as provided below.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | PS5 Base Development Kit/Testing Kit | | Trinity Development Kit/Testing Kit | |
| Low energy mode disabled | Low energy mode enabled | Low energy mode disabled | Low energy mode enabled |
| Application that does not support Trinity mode | Base mode | Base mode | Base mode | Base mode |
| Application that supports Trinity mode | Base mode | Base mode | Trinity mode | Trinity mode |
| Application that supports low energy mode | Base mode | **Low Energy Mode** | Trinity mode | **Low Energy Mode** |
| Application that does not support Trinity mode but supports low energy mode (\*1) | Base mode | **Low Energy Mode** | Base mode | **Low Energy Mode** |

\*1 Released application that does not support Trinity mode but supports low energy mode given an update

## SDK Patch for Supporting Low Energy Mode

Low energy mode is supported in SDK 11.00 and later, but an SDK patch is available to make released applications built with SDKs earlier than 11.00 support low energy mode. For more information on this SDK patch, including its features and how to obtain it, refer to <https://game.develop.playstation.net/technotes/view/726>.

# Application Runtime Modes

While there are three application operation modes, there are four runtime modes for the environments in which the applications actually run.

## Trinity Mode

This is the runtime mode in which a Trinity mode-compatible application runs on the hardware provided below. (These are the same conditions as for Trinity mode the operation mode.) All enhanced features for PlayStation®5 Pro can be used.

* Trinity Development Kit with the Force PS5 Base Mode feature (described later) disabled
* PlayStation®5 Pro
* Trinity Testing Kit

## PS5 Base Mode

This is the runtime mode in which an application runs on the hardware provided below. The operation mode used is Base mode.

* Trinity Development Kit with the Force PS5 Base Mode feature (described later) enabled
* Standard PlayStation®5
* PS5 Base Development Kit/Testing Kit

## PS5 Boost Mode

This is the runtime mode in which a Trinity mode-incompatible application runs on the hardware provided below. The operation mode used is Base mode. However, to maximize execution performance, the CPU/GPU clock speeds and the number of GPU WGPs that can be used utilize the hardware's performance. However, actual CPU/GPU clock speeds and performance will differ from Trinity mode.

* Trinity Development Kit with the Force PS5 Base Mode feature (described later) disabled
* PlayStation®5 Pro
* Trinity Testing Kit

The relationships that give rise to each runtime mode up to now are shown below.

| **Application** | **Trinity Development Kit** | |
| --- | --- | --- |
| **Force PS5 Base Mode disabled** | **Force PS5 Base Mode enabled** |
| Trinity mode-compatible | Trinity mode | PS5 Base mode |
| Trinity mode-incompatible | PS5 Boost mode | PS5 Base mode |

## Low Energy Mode

This is the operation mode in which an application that supports low energy mode runs when low energy mode is enabled on the hardware. The conditions for an application to run in this mode are the same as for the low energy mode operation mode.

## Force PS5 Base Mode Feature

The Trinity Development Kit provides the Force PS5 Base Mode feature, which forces Trinity mode-compatible applications to run in Base mode. By enabling [★Debug Settings] > [Game] > [Force PS5 Base Mode], you can use the Trinity Development Kit to develop Trinity mode-compatible applications that run in Base mode.

However, note that there will be differences in performance from the Standard PlayStation®5 given SoC differences. Regarding operation as well, there may be differences in out-of-spec behavior. In addition, the primitive and mesh shaders of the Standard PlayStation®5 have hardware limitations that the primitive and mesh shaders of PlayStation®5 Pro do not have. Refer to [Shader Programming User's Guide - Shader Specification - Hardware Limitations for Primitive and Mesh Shaders](../Shader_Programming-Users_Guide/hardware-limitations-for-primitive-and-mesh-shaders.html) for details.

Use the PS5 Base Development Kit if you want to address these differences in detail in your development work.

In addition, use the PS5 Base Testing Kit that is set to Release Mode for checking the operation of Trinity mode-compatible applications running in Base mode.

## How the Operation Mode Is Determined

An application's operation mode is determined as follows.

**Application with a param.json file that includes a declaration that Trinity mode is supported**

| **Hardware on which the application is running** | **Runtime mode** |
| --- | --- |
| * Trinity Development Kit (Force PS5 Base Mode feature enabled) * Standard PlayStation®5 * PS5 Base Development Kit/Testing Kit | PS5 Base mode |
| * Trinity Development Kit (Force PS5 Base Mode feature disabled) * PlayStation®5 Pro * Trinity Testing Kit | Trinity mode |

**Application with a param.json file that does not include a declaration that Trinity mode is supported**

| **Hardware on which the application is running** | **Runtime mode** |
| --- | --- |
| * Trinity Development Kit (Force PS5 Base Mode feature enabled) * Standard PlayStation®5 * PS5 Base Development Kit/Testing Kit | PS5 Base mode |
| * Trinity Development Kit (Force PS5 Base Mode feature disabled) * PlayStation®5 Pro * Trinity Testing Kit | PS5 Boost mode |

**Application without a param.json file (during development only)**

| **Hardware on which the application is running** | **Runtime mode** |
| --- | --- |
| * Trinity Development Kit (Force PS5 Base Mode feature enabled) * PS5 Base Development Kit/Testing Kit | PS5 Base mode |
| * Trinity Development Kit (Force PS5 Base Mode feature disabled) * Trinity Testing Kit | Trinity mode |

**Application with a param.json file that includes a declaration that low energy mode is supported (when low energy mode is enabled in the hardware settings)**

| **Hardware on which the application is running** | **Runtime mode** |
| --- | --- |
| * Trinity Development Kit/Testing Kit * PS5 Base Development Kit/Testing Kit * Standard PlayStation®5/PlayStation®5 Pro | Low energy mode |

# Determining the Operation Mode with the Boot Program (eboot.bin)

The same eboot.bin file is executed when the system launches an application, regardless of if the operating mode is Trinity mode, Base mode, or low energy mode. Therefore, an application must determine the current operation mode in eboot.bin before performing processing based on the operation mode. Use `sceKernelGetOperationMode()` to determine the current operating mode. For an application that does not support low energy mode, `sceKernelIsTrinityMode()` can also be used, because it is sufficient to check only whether the operation mode is Trinity mode or Base mode.

# Differences in the SDK Libraries Based on the Operation Mode

The features of the SDK libraries differ among operation modes. The major differences are provided below.

## Differences Between Trinity Mode and Base Mode

Between Trinity mode and Base mode, there are differences in the following libraries.

**Agc Library**

The Agc library has features that can be used only in Trinity mode. For details, refer to the [Agc Programming Guide](../Agc-Programming_Guide/__document_toc.html) document.

**Psr Library**

The Psr library provides separate features for Base mode and for Trinity mode. An application's code must be modified to make use of the enhanced ray tracing performance on PlayStation®5 Pro. For details, refer to [Ray Tracing Programming Guide - [PS5 Pro] Migrating a Base-Only Codebase to a Trinity-Enabled Codebase](../Ray_Tracing-Programming_Guide/trinity-migrating-a-base-only-codebase-to-a-trinity-enabled.html).

**ContentExport Library**

There are additional image formats supported by the ContentExport library when an application is running in Trinity mode. For details, refer to the [ContentExport Library Overview](../ContentExport-Overview/__document_toc.html) document.

**ContentSearch Library**

The resolutions of still images that can be referenced by the ContentSearch library differ between Base mode and Trinity mode; an application must support higher-resolution images in Trinity mode. For details, refer to the [ContentSearch Library Overview](../ContentSearch-Overview/__document_toc.html) document.

**VideoOut Library**

An application running in Trinity mode can use the VideoOut library to output higher-resolution images than in Base mode. For details, refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) document.

**Share Library**

Higher-resolution screenshots can be taken in Trinity mode. For details, refer to the [Share Library Overview](../Share-Overview/__document_toc.html) document.

## Differences Between Low Energy Mode and Base Mode

Between low energy mode and Base mode, there are no differences other than the amounts of resources that can be used. However, because of the limitations on the amounts of resources that can be used, there are differences in the following libraries.

**Kernel Library**

In low energy mode, the values that can be set as CPU masks are different because of the difference in the number of CPUs that can be used There are also points to be aware of because of this. For details, refer to the [Kernel Overview](../Kernel-Overview/__document_toc.html) document.

**VR-Related libraries**

In low energy mode, it is not possible to switch to VR mode, and VR-related libraries cannot be used. API features of VR-related libraries return errors at the initialization stage. For details, refer to the [Virtual Reality System Overview](../Virtual_Reality_System-Overview/__document_toc.html) document.

**Ajm Library and Auidodec Library**

In low energy mode, the number of streams that can be decoded simultaneously is limited to around 75% of that in PS5 Base mode. For details, refer to the [Ajm Library Overview](../Ajm-Overview/__document_toc.html) and [Audiodec Library Overview](../Audiodec-Overview/__document_toc.html) documents.

**Vdecsw Library and Videodec2 Library**

In low energy mode, video decoding performance may be lower because of the limitations on the resources that can be used. For details, refer to the [Vdecsw Library Overview](../Vdecsw-Overview/__document_toc.html) and [Videodec2 Library Overview](../Videodec2-Overview/__document_toc.html) documents.

**VideoOut Library**

In low energy mode, the OVERLAY port cannot be used. It is also not possible to switch to HFR output mode.

In addition, frame rates may be lower. To deal with this, you should consider utilizing VRR. For details, refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) document.

# Running Trinity Mode-Incompatible Applications on the Trinity Development Kit

You can install and run a Trinity-incompatible application package that was built with a version of the SDK earlier than 9.00 on the Trinity Development Kit. When you do so, the application's runtime mode is PS5 Boost mode.