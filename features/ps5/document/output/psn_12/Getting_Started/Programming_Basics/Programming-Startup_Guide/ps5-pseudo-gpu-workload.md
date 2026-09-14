# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-pseudo-gpu-workload.html

# Specifications for Rendering Performed by the System Software During Application Execution

This topic provides the specifications for, and points to note about, rendering performed by the system software during application execution.

# Rendering by the System Software

On PlayStation®5, the frame buffer rendered by the system software and the frame buffer rendered by the application are combined for final output to a display. The system software normally runs 60 fps, and a rendering command is issued once per frame to the GPU from a graphics pipe dedicated to the system software.

# Graphics Pipe Dedicated to the System Software

Rendering commands issued by the system software are issued from a dedicated graphics pipe that differs from the graphics pipe for an application. Because of this, the application can issue rendering commands independent of the system software.

Rendering commands issued from the graphics pipe are entered to the GPU command processor. When a rendering command of the application and a rendering command of the system software are entered to the command processor at the same time, the execution of the system software's rendering command will be prioritized.

# Timing When Rendering Commands Are Issued by the System Software

The system software issues a rendering command right after Vsync. Doing so ensures that there is sufficient time until the next Vsync and that the system and application can both use GPU hardware resources efficiently.

Because GPU resources are shared by the application and the system software as explained in the "[GPU](ps5-gpu.html)" section of the "[Resources That Can Be Used by Applications](resources-that-can-be-used-by-applications.html "This topic explains the various resources that can be used by applications. It provides the quantities that can be used for CPUs, GPUs, memory, file descriptors, threads, and event queues. Be aware that what is described here are specifications that are reinforced for development on DevKits and may differ from the specifications for TestKits and retail units.")" chapter, the rendering time of each can be extended due to competition. However, it is realistically unlikely for the application to always use GPU resources 100%, and GPU resources in the idle state can speedily be allocated for rendering by the system software even when rendering commands of the application and the system software overlap.

# System Software Rendering Frame Rate Decreases

As mentioned previously, rendering commands from the system software are processed in the GPU with higher priority than rendering commands from applications. However, if rendering commands from an application are dispatched before those from the system software and the graphics pipeline and Work Group Processor (WGP) resources are occupied with these commands, rendering by the system software may be stalled for a long period until that processing is complete. Examples of this are provided below.

* When a large number of draw calls without context rolls or a large number of draw calls that do not include synchronization commands in the command processor are submitted all at once, occupying the graphics pipeline for a long period
* When pixel processing is executed for a long period, such as in post processing, and the large number of wavefronts that are generated occupy all WGP resources

If the rendering load from the application is larger than the GPU time that the application can use during one frame and the rendering by the system software is stalled as described above, the result is that the system frame rate is lowered. It is likely that this is more liable to happen during high frame rate (HFR) output or during VR output, when Vsync intervals are shorter, than during ordinary output.

If a decrease of the frame rate of system software rendering is observed, you might consider revising the way in which your application issues rendering commands.

# Pseudo GPU Workload

The amount of rendering performed by the system software varies depending on the existence or lack of system UI rendering (for example). However, a drastic change in processing time will affect the application's rendering processing and may cause irregular frame skips. To avoid this, a pseudo GPU workload is created on the system side so that there is a GPU load even when the system UI is not displayed.

Limited to development, the GPU load of the system software when the application is running in the foreground can be changed. You can set this using either [★Debug Settings] > [Graphics] > [System Load Control] in the DevKit system software or `sceSystemServiceSetGpuLoadEmulationMode()`. Select "Off" when you want to exclude effects of the system software, for example, when you want to analyze performance. Select "On" to perform final application adjustments.

# VR Mode GPU Workload Emulation

When all the following conditions are met simultaneously, the amount of GPU time that the application can use per frame is reduced.

* The application is running in the foreground
* VR mode is enabled
* The system is simultaneously rendering the play area and the system software UI

When developing on a DevKit (and only then), this state can be emulated. If you would like to see how your application runs when the amount of GPU time is reduced, set [★Debug Settings] > [PlayStation VR2] > [Emulate Max VR System Load] to "On". Select "Off" when you are making the final adjustments to your application.

Note that when [★Debug Settings] > [Graphics] > [System Load Control] is "Off", [Emulate Max VR System Load] will treated as "Off" regardless of which option it is set to.

| **System Load Control** | **Emulate Max VR System Load** | **The Amount of Time that the GPU Can Use Within the Duration of 1 Frame (16.6 msec) When an Application Is in the Foreground** |
| --- | --- | --- |
| Off | Off | Approximately 16.6 msec |
| On | Off | Approximately 16.1 msec |
| Off | On | Approximately 16.6 msec |
| On | On | Approximately 15.6 msec |

# Refresh Rate Fixing by the System During VRR Output

Even if all conditions for VRR output have been met, the system software will perform UI rendering at a fixed refresh rate in the following circumstances:

* When the application is running in the foreground, the system UI is rendered as an overlay, and input from the controller is being unconditionally redirected to the system software (e.g., while the Control Center, a common dialog, the onscreen keyboard, or something else from the system UI is being displayed)
* When the recording feature is being used by remote play, the live streaming feature, Share Play, the user, or the game application
* When the system software is displaying something in Multitasking mode (picture-in-picture, displaying other content on the side of the screen, etc.)
* When the application is in the background (while the home screen is being displayed, etc.)

However, this behavior is subject to possible change in a future version of the system software.

Because many of these operations are performed by the user, the application is incapable of predicting when the system software will keep the refresh rate fixed. The application developer must take care so that the application can remain stable when switched to running at a fixed refresh rate at unforeseen times.

You can use [VRR Debug Peg to Fixed Rate] when performing operational tests during development. For details, refer to [VideoOut Library Overview - VRR - System Settings](../VideoOut-Overview/system-settings.html).

# Exception Detection and GPU Cache Flushing

Typically, the system software dispatches rendering commands to the GPU once every 16.6 msec to render the system UI and to detect application exceptions. This performs a cache flush of the GPU.

When pseudo GPU workloads have been set to disabled, an application is in the foreground state, and the system UI is not being rendered, rendering commands are dispatched once every 500 msec for the detection of exceptions.