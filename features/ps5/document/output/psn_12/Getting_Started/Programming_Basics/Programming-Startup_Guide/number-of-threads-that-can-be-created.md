# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/number-of-threads-that-can-be-created.html

# Resources That Can Be Used by Applications

This topic explains the various resources that can be used by applications. It provides the quantities that can be used for CPUs, GPUs, memory, file descriptors, threads, and event queues. Be aware that what is described here are specifications that are reinforced for development on DevKits and may differ from the specifications for TestKits and retail units.

# CPU

The DevKit CPU block comprises eight AMD64 architecture cores. Cores are equipped with the simultaneous multithreading (SMT) feature, and there are two hardware threads provided for each core. (Hardware threads are sometimes referred to as "CPUs"; this is because each hardware thread can be viewed as an independent CPU from a software.)

Refer to [Kernel Overview - CPU Management](../Kernel-Overview/cpu-management.html) for CPU resources that can be used by applications. Refer to [Kernel Overview - Thread Management - Thread Scheduling](../Kernel-Overview/thread-scheduling.html) for how to properly distribute the processing load of an application among the CPUs.

CPU and GPU frequencies dynamically change according to the load of the running application. Refer to [Kernel Overview - CPU Management](../Kernel-Overview/cpu-management.html) for details.

# GPU

## Compute Units

An application can use 36 compute units.

## Time the Application Can Use the GPU in One Frame (16.6 Milliseconds)

The system software uses the GPU once every 16.6 msec immediately after Vsync. Because of this, the times when an application can use the GPU are restricted as shown below based on whether the application is running in the foreground or in the background. (For details about the times when the system software uses the GPU, refer to the "[Specifications for Rendering Performed by the System Software During Application Execution](specifications-for-rendering-performed-by-the-system-softwar.html "This topic provides the specifications for, and points to note about, rendering performed by the system software during application execution.")" chapter.)

| **Application State** | **Period When the GPU Can Be Used (\*)** |
| --- | --- |
| Running in the foreground | Approximately 16.1 msec ([When the Application Is Running in the Foreground](ps5-gpu.html#programming-startup-guide_5_2__a4158d42-e267-11ee-bd3d-0242ac120002))  (However, the period will be approximately 15.6 ms to 16.1 ms when a play area and the system software UI are being rendered simultaneously in VR mode) |
| Running in the background | Approximately 8.3 msec ([When the Application Is Running in the Background](ps5-gpu.html#programming-startup-guide_5_2__a4158e3c-e267-11ee-bd3d-0242ac120002)) |

(\*) When the application is using GPU resources, GPU resources will be used for rendering by the system software in order whenever they become available and will be returned to the application in order whenever rendering by the system software is done. Thus, the overall volume of GPU resources used will not change, but the period during which they will be used will be reduced.

When the application is in the background state, rendering commands of the application will be made to wait up to 8.3 msec while the system software is being rendered.

When the Application Is Running in the Foreground
When the Application Is Running in the Background

# Memory

The memory that can be used by applications is as follows. For details about each type of memory, refer to [Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html).

## Flexible Memory

Flexible memory is for storing program code and stacks. The application can use up to 2 GiB of flexible memory on DevKits with the Release Check Mode set to Development Mode and up to 1 GiB in other cases.

## Direct Memory

Direct memory is guaranteed to be physically continuous, and it is explicitly allocated, released, and mapped by the application.

The application running in Base mode can use up to approximately 24.4 GiB of direct memory on DevKits depending on the setting of the Target Settings application or the ★Debug Settings menu of the system software. The application can use up to approximately 12.5 GiB of direct memory on TestKits and retail units. For details, refer to the [Tool Memory Overview](../Tool_Memory-Overview/__document_toc.html) document.

The application running in Trinity mode can use 1216 MiB more direct memory compared to an application that is running in Base mode.

The maximum values for the amount of direct memory that is available for use in each operation mode are provided below.

| **Application Operation Mode** | **Development Kit** | **Testing Kit or Retail Unit** |
| --- | --- | --- |
| Trinity mode | 26192 MiB | 13952 MiB |
| Base mode | 24976 MiB | 12736 MiB |

## AMPR - AMM Memory

The AMPR - AMM (Asynchronous Memory Mapper) memory is managed by dedicated hardware that processes mapping/un-mapping in high speed. The application can use the AMM library to batch-set multiple memory-operating commands to the command buffer, and to execute them asynchronously and at the same time.

In addition, the AMM library is equipped with a feature to easily enable coordinated operation with the APR library and Agc library. For details, refer to the "AMPR Library Overview" document.

## Pooled Memory

Pooled memory is a section of direct memory that is partitioned in units of 64 KiB for more efficient use for use by an application.

# Number of File Descriptors That Can Be Open at the Same Time

The number of file descriptors that an application can have open at the same time is 255. Note that the number of file descriptors opened by SDK libraries will be subtracted from this number.

# Number of Threads That Can Be Created

The number of threads that an application can create at the same time is 512 including the main thread. Note that the number of threads created by SDK libraries will be subtracted from this number.

# Number of Synchronous Objects That Can Be Created/Number of Asynchronous I/O Requests That Can Be Issued

The number of synchronous objects that an application can create at the same time is 4096. This restriction applies to objects named and created as `ScePthreadMutex`, `ScePthreadCond`, `ScePthreadRwlock`, `ScePthreadBarrier`, `SceKernelSema`, and `SceKernelEventFlag`; unnamed objects will not be included in this number. Note every time an asynchronous I/O request is issued, one of the above 4096 objects will be consumed. Also note that the number of synchronous objects created by SDK libraries will similarly be subtracted from the total.

# Number of Sockets That Can Be Created

The number of sockets that an application can create at the same time is 128. Note that the number of sockets created by SDK libraries will be subtracted from this number.

# Number of Event Queues That Can Be Created

The number of event queues that an application can create at the same time is 256. Note that the number of event queues created by SDK libraries will be subtracted from this number. For details about event queues, refer to [Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html).

## Number of Events That Can Be Added to Event Queues

An application can add up to 20,000 events to event queues. Note that this value is not the maximum for each individual event queue but the maximum value for the sum of all events added to all event queues in an application. For details about event queues, refer to [Kernel Overview - Thread Management - Event Queues](../Kernel-Overview/event-queues.html).