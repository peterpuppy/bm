# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/cpu-resources-and-cpu-management-during-foreground-execution.html

# CPU Management

# Overview of CPU Resources and CPU Management During Foreground Execution

During foreground execution, applications can use the following CPUs depending on the operation mode. (For details about application operation modes, refer to [Programming Startup Guide - Basic Information on Application Execution Environments - Application Operation Modes](../Programming-Startup_Guide/ps5-application-operation-modes.html).)

* When the operation mode is Base mode or Trinity mode: Up to 13 CPUs can be used, CPU#0 to CPU#12.
* When the operation mode is low energy mode: Up to eight CPUs can be used, CPU#0 to CPU#7.

An application can obtain which CPUs it can use based on its operation mode using `sceKernelGetAvailableCpumask()`.

CPUs Available for Use During Foreground Execution

CPU#*n* (*n* being an even number) and CPU#*n*+1 - for example, CPU#0 and CPU#1 - share one CPU core, because of the simultaneous multithreading (SMT) feature. Therefore, processing on one member of such a pair of CPUs affects the other member of the pair.

Four CPU cores (eight CPUs) constitute a grouping and share an L3 cache. Such a grouping is called a Core Complex (CCX). CPU#0 through CPU#7 belong together to one CCX. CPU#8 through CPU#12, along with the CPUs used by the system, belong to another CCX.

To properly distribute the processing load of an application among the usable CPUs, set CPU affinities for threads. For details, refer to the "[Thread Scheduling](thread-scheduling.html)" section.

# CPU Resources During Background Execution Status

When user operation causes an application to transition to background execution status, the system uses 90% of the specified CPU, and the application can use only the remaining 10%. The CPUs that are subject to this allocation differ depending on the operation mode of the application as follows:

* When the operation mode is Base mode or Trinity mode: CPU#9 and CPU#11 are affected.
* When the operation mode is low energy mode: CPU#5 and CPU#7 are affected.

This allocation is performed in cycles of 5.33 milliseconds, during which the system uses those CPU resources for periods of approximately 4.80 milliseconds and the application uses them for periods of approximately 0.53 milliseconds.

Foreground Execution and Background Execution (in Base Mode or Trinity Mode)
Foreground Execution and Background Execution (in Low Energy Mode)

# Effective Use of Application-side CPU Resources by the System

Allocation of CPUs to application and system threads is essentially as illustrated in the figure above ([in Base Mode/Trinity Mode](cpu-resources-during-background-execution-status.html#kernel-overview_4_2__f8bcac7e-eb25-1f02-8ffc-23c653bc0002), [in Low Energy Mode](cpu-resources-during-background-execution-status.html#kernel-overview_4_2__f8bcac7e-eb25-1f02-8ffc-23c653bc0003)). However, in some exceptional cases, some high-priority system threads may make temporary use of application-side CPU resources. System thread operation time is extremely short in these cases, but these system threads may cause the application-side threads to be preempted.

# Notes Regarding When Applications Support Low Energy Mode

As shown in the figure above ([in Base Mode/Trinity Mode](cpu-resources-during-background-execution-status.html#kernel-overview_4_2__f8bcac7e-eb25-1f02-8ffc-23c653bc0002), [in Low Energy Mode](cpu-resources-during-background-execution-status.html#kernel-overview_4_2__f8bcac7e-eb25-1f02-8ffc-23c653bc0003)), the usable CPU resources differ depending on whether the application is in Base mode or Trinity mode, or if it is in low energy mode. If the application supports low energy mode, note the following points regarding CPU resources and thread counts.

While 13 CPUs are usable when an application is running in Base mode or Trinity mode, the number of usable CPUs is reduced to 8 in low energy mode, which reduces the number of threads executed in parallel. If the number of frequently operating worker threads, or otherwise critical threads, created is the same as for 13 CPUs, there may be cases in which threads are preempted and not given the opportunity to run on 8 CPUs, even though they all would run without fail on 13 CPUs. If a thread continues to be preempted while holding any locks and then fails to execute, this may lead to the application stalling.

Adjust the number of threads created for each operation mode as required, especially when newly adding low energy mode support to an application already implemented with Base mode or Trinity mode in mind.

# Power Management Through Control of Frequencies

To obtain better performance with limited power consumption on the PlayStation®5, the frequencies of the CPUs and GPU are dynamically changed based on application load during execution.

Note:

Unlike fixed-frequency platforms, there is a trade-off between performance improvements and the power consumption of speculative processing.

## Characteristics of Frequency Control

The frequency control mechanism has the following characteristics:

**Only CPU and GPU Frequencies Are Variable**

CPUs and the GPU maintain their maximum frequencies within the TDP (Thermal Design Power) range. The frequencies of SDF (Scalable Data Fabric) and memory are fixed. Additionally, surplus power external to the GPU is used by the GPU. For example, if CPU power use is low, the GPU will be able to use slightly more power.

However, this characteristic does not apply when an application is running in low energy mode. For details about the low energy mode, refer to [Programming Startup Guide - Basic Information on Application Execution Environments - Application Operation Modes](../Programming-Startup_Guide/ps5-application-operation-modes.html).

**Identical Processing Performance**

Power consumption is calculated as counts performed for each unit internally while in a state of operation; frequency is determined based on the time elapsed while power is consumed. Therefore, frequency changes are identical across the Development Kit, Testing Kit, and retail units, and thus processing performance is identical. Determination of frequency is unaffected by differences between individual units, environmental temperature, or other external factors.

**Gradual Frequency Changes**

Power consumption calculations based on operational status are conducted on a per-millisecond basis, and as they pass through a filter and are summed up, they are reflected in the frequency. For example, even if there is a switch to a high-load scene, it will be several hundred milliseconds before this is reflected in the frequency. (The value that can be seen in "Power Trends" that is displayed when the Razor CPU capture option "Power Management Trace" is enabled is the value used to determine the frequency.)

## Frequency Control by Trinity Mode-Compatible Applications

By default, an application running in Trinity mode is configured to run with a setting that provides for CPU performance equivalent to that of an application running on a standard PlayStation®5 and GPU graphics performance that is enhanced compared to such an application. For most applications, this default setting is optimal.

However, also available is a setting that increases the maximum CPU frequencies above those of a standard PlayStation®5 (trading-off with GPU performance) for applications that prioritize CPU performance over graphics performance. These settings can be configured by setting the appropriate value to attribute3 in the parameter file (param.json).

The details of each setting are provided below. For details, refer to [Param.json File Specification - Param File (param.json) Specifications](../Param_Json-Specification/param-file-paramjson-specifications.html).

* **Standard**

  This is the default setting. No special additional implementation is required in the application. Absent any special circumstances, you should use this setting.

  With this setting, the CPUs run with maximum frequencies and performance equivalent to those of standard PlayStation®5, and the GPU runs with the standard power consumption and performance provided on PlayStation®5 Pro.
* **High CPU Frequency**

  This setting increases the maximum CPU frequencies above those of a standard PlayStation®5.

  When an application runs with this setting selected, the amount of power supplied to the GPU is decreased compared to when set to Standard, and that power is instead allocated to the CPUs. Because of this, GPU performance tends to decrease compared to when Standard is set. This setting should be used only in special circumstances in which you would like to prioritize CPU performance over GPU performance.

Note that, when a value other than "Default (same as a retail)" is selected for "★Debug Settings" > "Game" > "CPU/GPU Frequency" during development, that setting takes priority, and the High CPU Frequency setting is ignored. (For details about the values that can be set for CPU/GPU Frequency, refer to "[Controlling Frequencies During Development](power-management-through-control-of-frequencies.html#kernel-overview_4_5__kernel-overview_4_5_3)".)

## Controlling Frequencies During Development

It is difficult to work to optimize an application when frequencies change in tandem with application load. To facilitate optimization work, the following three frequency control modes are provided under "★Debug Settings" > "Game" > "CPU/GPU Frequency" on Development Kits on which the Release Check Mode has been set to Development Mode: The mode in which an application is executed is determined by the mode setting when the application is launched.

* **Default (same as a retail)**

  The frequencies of the CPUs and the GPU will change in response to application load up to their maximums. This is the same behavior as on a retail unit. Use this mode for development under normal circumstances.
* **Mostly Fixed Frequency**

  This mode limits the maximum frequencies of the CPUs and the GPU to lower values than in the Default mode. There is a narrower range of frequency changes in this mode than in Default mode. Additionally, surplus power is no longer transferred from the CPUs to the GPU. In most cases, there will be almost no frequency fluctuations in this mode. Use this mode to optimize applications without needing to worry about the effects of frequency changes and to evaluate the performance of libraries and middleware to be run simultaneously with applications' other components.
* **Fixed Frequency**

  This mode limits the maximum frequencies of the CPUs and the GPU to even lower values than in Mostly Fixed Frequency mode. Additionally, as with Mostly Fixed Frequency mode, surplus power is no longer transferred from the CPUs to the GPU. Frequency fluctuation is low even when working on special applications with very high loads. Use this mode if frequency changes enough to hinder application optimization even in Mostly Fixed Frequency mode.

Note that, if a value other than "Default (same as a retail)" is selected, that setting takes priority, and the High CPU Frequency setting in param.json is ignored. (For details about High CPU Frequency, refer to "[Frequency Control by Trinity Mode-Compatible Applications](power-management-through-control-of-frequencies.html#kernel-overview_4_5__kernel-overview_4_5_2)".)