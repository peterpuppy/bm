# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/synchronization-between-threads.html

# Thread Management

# Threads

The PlayStation®5 kernel provides POSIX-based threads as execution entities of a program. POSIX-compatible thread routines and attribute object routines are provided. However, note that the API feature names are changed to follow the naming rules of the PlayStation®5 SDK as in the following table.

PlayStation®5 Kernel API Features and pthread API Features

|  | PlayStation®5 Kernel API | pthread API |
| --- | --- | --- |
| Function | `scePthreadXxxYyy()` | `pthread_xxx_yyy()`, `xxx_yyy()` (POSIX semaphores) |
| Type | `ScePthreadXxx` | `pthread_xxx_t`, `xxx_t` (POSIX semaphores) |
| Value | `SCE_XXX_YYY` | `XXX_YYY` |
| Error code | `SCE_KERNEL_ERROR_XXX`  (negative value returned by a function) | `XXX`  (positive value stored in the variable `errno`) |
| Header | kernel.h | pthread.h, pthread\_np.h, semaphore.h |
| Library | Not required to link explicitly | Required to explicitly link libScePosix\_stub\_weak.a |

In addition, the behavior of functions when an error occurs is different. Note that the error code `SCE_KERNEL_ERROR_XXX` returned by PlayStation®5 kernel API functions is a negative value, but the error code `XXX` returned by pthread API functions is a positive value. 0 is returned for both at the time of normal termination.

Note:

When porting an existing program, the pthread API can be used by including pthread.h/pthread\_np.h/semaphore.h instead of kernel.h and linking libScePosix\_stub\_weak.a.

## Thread Routines

Thread routines are functions for performing thread operations such as creating threads, yielding execution rights to other threads, and waiting for the termination of other threads. A list of thread routines is shown in the following table.

Thread Routine Functions

| **Function** | **Description** |
| --- | --- |
| `scePthreadCleanupPop()` | Call a thread-termination function at the stack top |
| `scePthreadCleanupPush()` | Register a thread-termination function to the stack |
| `scePthreadCreate()` | Create a new thread |
| `scePthreadCancel()` | Send a termination request to another thread |
| `scePthreadDetach()` | Put a thread in detach mode |
| `scePthreadEqual()` | Compare threads |
| `scePthreadExit()` | Terminate the calling thread |
| `scePthreadGetthreadid()` | Get the thread ID |
| `scePthreadGetprio()` | Get thread priority |
| `scePthreadGetspecific()` | Get data from thread-specific storage |
| `scePthreadJoin()` | Wait for the termination of another thread |
| `scePthreadKeyCreate()` | Create a thread-specific storage key |
| `scePthreadKeyDelete()` | Delete a thread-specific storage key |
| `scePthreadOnce()` | Call an initialization function once |
| `scePthreadRename()` | Rename a thread |
| `scePthreadSelf()` | Get the thread object of the calling thread |
| `scePthreadSetcancelstate()` | Set whether or not to accept a termination request |
| `scePthreadSetcanceltype()` | Set the termination timing when a termination request is accepted |
| `scePthreadSetprio()` | Set thread priority |
| `scePthreadSetspecific()` | Store data to thread-specific data |
| `scePthreadTestcancel()` | Receive a termination request being held |
| `scePthreadYield()` | Yield execution rights |

## Attribute Object Routines

Attribute object routines are functions for setting/getting thread attributes such as priority and stack size. A list of attribute object routines is shown in the following table.

Attribute Object Routine Functions

| **Function** | **Description** |
| --- | --- |
| `scePthreadAttrDestroy()` | Destroy an attribute object |
| `scePthreadAttrGet()` | Get an attribute object of a thread |
| `scePthreadAttrGetaffinity()` | Get the set CPU affinity mask |
| `scePthreadAttrGetinheritsched()` | Get the set scheduling inheritance flag |
| `scePthreadAttrGetschedparam()` | Get the set scheduling parameter (priority) |
| `scePthreadAttrGetschedpolicy()` | Get the set scheduling policy |
| `scePthreadAttrGetsolosched()` | Get the set Solo thread attribute |
| `scePthreadAttrGetstacksize()` | Get the set stack size |
| `scePthreadAttrGetstackaddr()` | Get the set stack address |
| `scePthreadAttrGetdetachstate()` | Get the set detach state |
| `scePthreadAttrInit()` | Initialize an attribute object |
| `scePthreadAttrSetaffinity()` | Set the CPU affinity mask |
| `scePthreadAttrSetinheritsched()` | Set the scheduling inheritance flag |
| `scePthreadAttrSetschedparam()` | Set the scheduling parameter (priority) |
| `scePthreadAttrSetschedpolicy()` | Set the scheduling policy |
| `scePthreadAttrSetsolosched()` | Set the Solo thread attribute |
| `scePthreadAttrSetstacksize()` | Set the stack size |
| `scePthreadAttrSetstackaddr()` | Set the stack address |
| `scePthreadAttrSetdetachstate()` | Set the detach state |
| `scePthreadGetaffinity()` | Get the CPU affinity mask |
| `scePthreadSetaffinity()` | Set the CPU affinity mask |

# Thread Scheduling

## Priority and CPU Affinity

In order to adjust the scheduling of threads, it is possible to set the priority and "CPU affinity" for each thread. The priority is a numerical value in the range shown in "[Priority range](thread-scheduling.html#kernel-overview_5_2__p_nj5_wrv_42c)". Smaller values represent higher priorities. The CPU affinity is information that indicates which of the multiple CPUs in the system the thread is to be executed on. (For details, refer to "[CPU Affinity Handling](thread-scheduling.html#kernel-overview_5_2__kernel-overview_5_2_3)".)

For each of the CPUs, the scheduler assigns the thread with the highest priority from a set of threads which can be executed on that CPU, and lets the CPU execute that thread. Threads are preemptive. When a thread runs on a CPU and another thread with a higher priority than the running thread is to be executed, the running thread is preempted. Preempted threads may be re-allocated to other CPUs.

When the execution of a high priority thread completes or is put to sleep, the next highest priority thread will be executed from among the lower priority threads.

When a thread that can be executed on multiple CPUs becomes executable, the scheduler will assign the thread to an available CPU among those that can execute the thread. If all the CPUs that can execute the thread are being used and the thread that became executable has a higher priority than the threads that are running on these CPUs, the thread running with the lowest priority on these CPUs will be preempted by the executable thread.

However, if using the Solo thread attribute, the thread with the lowest priority will not necessarily be preempted. For details, refer to "[Efficiently Improving CPU Core Sharing and Single-thread Performance via SMT](thread-scheduling.html#kernel-overview_5_2__kernel-overview_5_2_5)".

## Scheduling Policy

`SCE_KERNEL_SCHED_FIFO` with fixed priority and FIFO for same-priority threads or `SCE_KERNEL_SCHED_RR` with fixed priority and round-robin for same-priority threads can be specified as the scheduling policy of each thread.

**`SCE_KERNEL_SCHED_FIFO`: FIFO scheduling policy**

In this scheduling policy, threads will be executed in the order of priority, with threads (normally) executed in the order they become executable if they have the same priority.

Even when a FIFO scheduling policy thread is executable, it will not be executed if there is no room in the CPUs from being occupied by threads with higher priority. Such threads that are executable but cannot be executed will be managed in first-in first-out (FIFO) queues for each priority level. In other words, when a thread becomes executable and there is no room in the CPUs, the thread will be added to the end of the queue, and then when a thread with higher priority yields a CPU, the first thread in the queue will be removed, allocated to the CPU, and then executed.

Threads being executed may be preempted by threads with higher priority, but they will not be preempted by threads with the same priority. When a thread being executed is preempted, the thread will be added to the beginning of the queue for its priority.

A thread being executed will yield the CPU to another thread when it is preempted by a thread with higher priority or when it calls a function that yields the CPU (many I/O, various sleep, synchronous primitive, termination, and CPU delegate functions).

`scePthreadYield()` is a function that explicitly yields the CPU to another executable thread with the same priority. A thread that calls `scePthreadYield()` will yield the CPU and then will be added to the end of the queue for its priority. If there are no other threads in the queue (when there are no other executable threads with the same priority that have not been allocated to the CPU), the `scePthreadYield()` call will have no effect on the scheduling.

FIFO order by priority is not guaranteed for application suspends/resumes, including system suspensions and stops/resumes with the debugger. If one of these occurs, FIFO order may be disrupted. Because application suspends/resumes can occur any time asynchronous to application operation, do not design/implement your application with the assumption that threads with the same priority will be executed in the order they become executable.

**`SCE_KERNEL_SCHED_RR`: Round-robin scheduling policy**

The round-robin scheduling policy is the same as the FIFO scheduling policy except that a maximum time is determined for threads occupying the CPUs.

A thread with the round-robin scheduling policy whose execution time in a CPU exceeds the round-robin time quantum will be deallocated from the CPU then added to the end of the queue for threads with the same priority that are executable but cannot be executed.

By only allocating threads with the round-robin scheduling policy for a particular priority, threads in numbers that exceed the number of usable CPUs can be executed in alternate orders without a particular thread occupying a CPU and preventing other threads from operating. (Note that there is a possibility of a thread continually occupying a CPU if a thread with the FIFO scheduling policy is assigned the same priority as the round-robin scheduling policy threads.)

The round-robin time quantum is common to the system and is set to 4 milliseconds.

**Priority range**

The priority ranges for each scheduling policy are as follows:

Scheduling Policy and Priority Range

| **Scheduling policy** | **Scheduler behavior** | **Priority range** |
| --- | --- | --- |
| `SCE_KERNEL_SCHED_FIFO` | FIFO for threads with the same priority | 256 to 767 |
| `SCE_KERNEL_SCHED_RR` | Round-robin for threads with the same priority | 256 to 767 |

Smaller values for priority represent higher priorities.

If the priority is not explicitly specified when creating a new thread, the new thread will inherit the priority of the thread that created it.

The default priority when the application is started is 700. This value is defined as `SCE_KERNEL_PRIO_FIFO_DEFAULT`. The highest priority and lowest priority values are defined as `SCE_KERNEL_PRIO_FIFO_HIGHEST` and `SCE_KERNEL_PRIO_FIFO_LOWEST`, respectively.

## CPU Affinity Handling

Use `scePthreadSetaffinity()` to set the CPU affinity to a thread. It is also possible to use `scePthreadAttrSetaffinity()` to set it to an attribute object.

To get the set CPU affinity, use `scePthreadGetaffinity()` or `scePthreadAttrGetaffinity()`.

If the CPU affinity is not explicitly specified when creating a new thread, the new thread will inherit the CPU affinity of the thread that created it.

The default CPU affinity at application startup is all CPUs that can be used by an application. (Refer to "[Overview of CPU Resources and CPU Management During Foreground Execution](cpu-resources-and-cpu-management-during-foreground-execution.html)".) Macros are defined according to the application's operation mode: `SCE_KERNEL_CPUMASK_13CPU` is set for Base or Trinity mode, and `SCE_KERNEL_CPUMASK_8CPU` is set for low energy mode.

## Relationship of the CPU Affinity and CPUs/CPU Cores

Each bit of the CPU affinity corresponds to a CPU. From the lowest bit as 0, the position of each bit represents the number of a CPU. In other words, bit 0 represents CPU#0, bit 1 represents CPU#1, bit 2 represents CPU#2, and so forth.

The scheduler assigns threads to CPUs in accordance with the constraints placed by CPU affinities. During this assignment, threads will be assigned with priority given to CPU cores for which both CPUs are currently free. Applicable CPU cores are assigned in the order of priority illustrated below. Threads are first assigned to the even-numbered CPUs starting at the lowest number, and then to odd-numbered CPUs starting at the highest number.

* If the application operation mode is Base Mode or Trinity Mode:

  CPU#0 → #2 → #4 →...→ #12 → #11 → #9 →...→ #1
* If the application operation mode is low energy mode:

  CPU#0 → #2 → #4 →...→ #6 → #7 → #5 →...→ #1

Use `sceKernelGetCurrentCpu()` to obtain the number of the CPU that is currently running. The number of the CPU that executed the rdtscp instruction is also stored in IA32\_TSC\_AUX that can be obtained with the rdtscp instruction.

## Efficiently Improving CPU Core Sharing and Single-thread Performance via SMT

As also described in the "[CPU Management](cpu-management.html)" chapter, two CPUs share a single CPU core through the SMT feature. Thus, two threads running on a CPU core simultaneously compete for the computational resources of the CPU core shared using SMT and, therefore, affect one another's operations.

In general, you can increase overall computational throughput by adding more parallelism to your program and actively using SMT. However, there are some programs for which it is difficult to increase parallelism and some cases in which optimizing single-thread performance, rather than using SMT, is desirable. In such cases, one method is to use the setting of CPU affinities to make it so that additional threads are not assigned to (CPUs shared by) SMT that would compete with the threads whose single-thread performance you are trying to increase. Using this method, however, means that, even when such threads are not running, the other threads that would have been running on the CPUs managed by SMT and that thus would have caused competition will not run on those CPUs; consequently, the CPUs will end up unutilized.

**Improving Single-Thread Performance Using the Solo Thread Attribute**

The "Solo thread" attribute is available so that other threads will not be allowed to run on a potentially competing SMT-managed CPU only when a specific thread whose single-thread performance you want to optimize is running.

Use `scePthreadAttrSetsolosched()` to give a thread the Solo thread attribute. When a thread to which the Solo thread attribute has been given is scheduled, a Companion thread of the same priority as that thread is simultaneously scheduled to the SMT-managed CPU that would have caused competition. Companion threads, like idle threads, are threads that do nothing and do not consume CPU resources of any kind that would interfere with operations of competing CPUs.

When a Solo thread is descheduled, the "competing" Companion thread is descheduled simultaneously.

When a Solo thread and a Companion thread are running together on the same CPU core and a higher-priority thread that can be executed by any of the CPUs that share that CPU core is scheduled, the Companion thread will be given priority for preemption. In this situation and others, when a Companion thread is preempted by a higher-priority thread (and only then) a Solo thread will end up running simultaneously with another thread that is not a Companion thread on the competing SMT-managed CPU, and competition for CPU resources will occur.

**Solo Thread Scheduling**

Solo thread scheduling prioritizes the selection of CPUs that can simultaneously execute a Companion thread on the same CPU core. For example, assume that threads are assigned to every CPU of two CPU cores as follows.

* CPU#0: Idle thread
* CPU#1: 600-priority thread
* CPU#2: 750-priority thread
* CPU#3: 700-priority thread

In this case, if a 650-priority Solo thread that has been given affinity for CPU#0 through #3 is scheduled, CPU#2 will be selected, not CPU#0. This will enable a Companion thread with the same priority (650) to preempt the thread running on CPU#3 and be executed simultaneously with the Solo thread.

(If CPU#0 were selected here, it would not be able to preempt the 600-priority thread running on CPU#1, making simultaneous execution impossible.)

# Thread States

Threads have the following states. These states can be observed on the debugger.

* INITIALIZED:

  State in which the thread has been created but execution cannot yet be started (state during `scePthreadCreate()`)
* RUN QUEUED:

  State in which the thread can be executed but is waiting for an executable CPU to become available (being queued)
* RUNNING:

  State in which the thread is being executed on a CPU
* WAITING:

  State in which the thread is waiting for the release of a synchronous object or timer ignition
* SUSPENDED:

  State in which the thread is being stopped by a process suspension
* TERMINATED:

  State in which the thread terminated with `scePthreadExit()` but thread resources remain because `scePthreadJoin()` has not been executed

Thread states transition as shown in the below figure.

Thread State Transitions

# Synchronization Between Threads

The PlayStation®5 kernel provides the following mechanisms for inter-thread exclusive control and synchronization.

* Mutexes (`scePthreadMutexXxx`)
* Condition variables (`scePthreadCondXxx`)
* Reader/writer locks (`scePthreadRwlockXxx`)
* Barriers (`scePthreadBarrierXxx`)
* Event flags (`sceKernelXxxEventFlag`)
* Semaphores (`sceKernelXxxSema`)
* POSIX semaphores (`scePthreadSemXxx`)

# Event Queues

The PlayStation®5 kernel provides a mechanism called event queues for notifying application programs of events that have occurred in the kernel, libraries, or otherwise within the system.

By creating an event queue and adding an event to be monitored to the queue, it will be possible for the application to wait for the event to arrive. It is possible to wait for multiple events in a single event queue.

There are various types of events called filters. Functions for adding or deleting events to be monitored in the event queue are provided for each filter.

When adding an event to an event queue, specify an ID for identifying events with the same filter, filter-specific data, and user data that can be freely used by the application. Events in a single event queue are identified by filter and ID. When attempting to add an event with the same filter and ID as one already added to the event queue, the already added event will be overwritten.

Information about an event that has occurred will be maintained in the event queue. When the same event arrives multiple times, the content will be overwritten.

To obtain the events that have arrived in an event queue, call `sceKernelWaitEqueue()`. If events have already arrived at that time, they can be obtained as an event array. If no events have arrived, this function will wait until arrival, but it is possible to cause a timeout after a specified time or to specify no waiting at all.

It is possible to determine which of the events (that were added as monitoring targets) has been obtained by obtaining the filter and ID from the event. To obtain the filter from an event, use `sceKernelGetEventFilter()`. To obtain the ID, use `sceKernelGetEventId()`. Functions for obtaining filter-specific data, user data, etc., are also provided.

There are two kinds of events: those that operate as level triggers and those that operate as edge triggers.

* For an event that operates as a level trigger, the event will continue to be in an arrived state while the monitoring target phenomena are occurring. This state will not change even when an event is obtained.
* For an event that operates as an edge trigger, the event will arrive when monitoring target phenomena occur, the event will be reset when obtained, and it will enter a not arrived state.

The PlayStation®5 kernel provides the following filters. (In addition to these, there are also filters provided by drivers and libraries.)

## Timer event filter

With this filter, an event occurs when a specified time elapses. Add it to the event queue with `sceKernelAddTimerEvent()` and delete it with `sceKernelDeleteTimerEvent()`. This event occurs periodically every time the specified time elapses. The event occurrence will not stop even when the event is obtained with `sceKernelWaitEqueue()` and will continue until the event is deleted. The number of times the event occurred can be determined with `sceKernelGetEventData()` upon obtaining the event.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_TIMER`.
* Timer events operate as edge triggers.

## High precision timer event filter

With this filter, an event occurs when a specified time elapses. In comparison with timer events, it is possible to specify high precision times with nanosecond granularity from a minimum of 100 microseconds. Add it to the event queue with `sceKernelAddHRTimerEvent()` and delete it with `sceKernelDeleteHRTimerEvent()`. Unlike the timer event, this event does not occur periodically. In other words, this event only occurs once.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_HRTIMER`.
* High precision timer events operate as edge triggers.

## Read event filter

With this filter, an event occurs when a file or socket becomes readable. Add it to the event queue with `sceKernelAddReadEvent()` and delete it with `sceKernelDeleteReadEvent()`.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_READ`.
* Read events operate as level triggers.

## Write event filter

With this filter, an event occurs when a file or socket becomes writable. Add it to the event queue with `sceKernelAddWriteEvent()` and delete it with `sceKernelDeleteWriteEvent()`.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_WRITE`.
* Write events operate as level triggers.

## File event filter

With this filter, an event occurs when a file status is changed. Add it to the event queue with `sceKernelAddFileEvent()` and delete it with `sceKernelDeleteFileEvent()`.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_FILE`.
* File events operate as level triggers.

## AMPR event filter

This is a filter for receiving events generated by the AMPR libraries. Add it to the event queue with `sceKernelAddAmprEvent()` and delete it with `sceKernelDeleteAmprEvent()`.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_AMPR`.
* AMPR events operate as edge triggers.

## AMPR system event filter

This is a filter for receiving events generated by the system in relation to use of the AMPR. Add it to the event queue with `sceKernelAddAmprSystemEvent()` and delete it with `sceKernelDeleteAmprSystemEvent()`.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_AMPR_SYSTEM`.
* AMPR system events operate as edge triggers.

## User event filter

This filter can make the application cause an event to occur for an arbitrary purpose. Add it to the event queue with `sceKernelAddUserEvent()` or `sceKernelAddUserEventEdge()` and delete it with `sceKernelDeleteUserEvent()`. After adding it to the event queue, the event can be triggered by calling `sceKernelTriggerUserEvent()`.

* The value that can be obtained with `sceKernelGetEventFilter()` is `SCE_KERNEL_EVFILT_USER`.
* User events added with `sceKernelAddUserEvent()` operate as level triggers, and they will continue to be in an arrived state from the time `sceKernelTriggerUserEvent()` is called until the time `sceKernelDeleteUserEvent()` is called.
* User events added with `sceKernelAddUserEventEdge()` operate as edge triggers, and they will be in a not arrived state when the events are obtained with `sceKernelWaitEqueue()`. When `sceKernelTriggerUserEvent()` is called in this state, the event can be caused to occur again.

## Resource Restrictions on Event Queues

An application has a restriction on the number of event queues that it can generate simultaneously. For details, refer to "Number of Event Queues That Can Be Created" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html). If there is an attempt to generate more event queues in excess of the number that can be generated, `sceKernelCreateEqueue()` returns `SCE_KERNEL_ERROR_EMFILE`.

There are also restrictions on the number of events that an application can add to event queues. For details, refer to "Number of Events That Can Be Added to Event Queues" in [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html). If there is an attempt to add more events in excess of the number that can be added, the following functions return `SCE_KERNEL_ERROR_EAGAIN`:

* `sceKernelAddAmprEvent()`
* `sceKernelAddAmprSystemEvent()`
* `sceKernelAddFileEvent()`
* `sceKernelAddHRTimerEvent()`
* `sceKernelAddReadEvent()`
* `sceKernelAddTimerEvent()`
* `sceKernelAddUserEvent()`
* `sceKernelAddUserEventEdge()`
* `sceKernelAddWriteEvent()`

# Threads and Memory Resources

Upon thread creation/termination, the thread runtime library dynamically allocates/releases memory resources. This section describes the types of resources that are allocated/released, as well as the timing and manner of the allocation/release.

## Memory Related to Threads

When a thread is created, the thread runtime library, which manages threads, allocates a thread management object, a stack area, and a TLS area to use for managing the created thread.

These memory resources become unnecessary upon thread deletion; however, memory release is carried out with a delay. In other words, the thread runtime library does not return these memory resources to the kernel and caches them whenever possible, attempting to reuse them for the thread that is created next. Because of this, thread creation/deletion and the increase/decrease of memory consumption by a thread are not always synchronized.

## Thread Management Objects

Thread management objects store information required for thread execution, synchronization, and management. When a thread is newly created, a single thread management object is allocated for that thread from the system's reserved area.

## Stack Areas

A stack area is allocated upon thread creation from the user's process space.

The default size of a stack area differs by whether or not the thread is the main thread. The stack size of a main thread is 2 MiB. The default stack size for a non-main thread is 64 KiB; this can be changed to page size units by calling `scePthreadAttrSetstacksize()` or `scePthreadAttrSetstack()`.

For both the main thread and non-main threads, the address to place the stack area is undefined.

## TLS Areas

TLS areas are categorized into the following three types.

* TLS management object: data structure for managing and accessing TLS
* Main module TLS block: area storing TLS variables and corresponding to the TLS segment defined by the file image of the main module
* Other TLS blocks: area storing TLS variables and corresponding to the TLS segment defined by the file image of a module that is not the main module

A TLS management object is allocated upon thread creation from the system's reserved area. It has the same lifetime as the thread management object, is a cache target and is released with a delay.

A main module TLS block is allocated upon thread creation from the heap area or from the heap area that has been replaced for TLS. It has the same lifetime as the thread management object, is a cache target and is released with a delay. However, note that the main module TLS block for the main thread is not released.

The size of the main module TLS block differs according to whether it is for the main thread or for other threads. Each size is calculated as follows.

```
SZmain = ROUNDUP(SZseg + 192, PAGE_SIZE)
SZother = ROUNDUP(SZseg + 192, 32)
```

* `SZmain`: size of the main module TLS block for the main thread
* `SZother`: size of the main module TLS block for a non-main thread
* `SZseg`: TLS segment size of the main module
* `PAGE_SIZE`: page size
* `ROUNDUP(X, Y)`: function that returns a value for X rounded up to an integer multiple of Y

Other TLS blocks are areas for storing the TLS variables that are defined by the PRX modules. After a module is loaded, an area will be allocated upon first accessing one of the TLS variables that are defined by the module.

Memory areas to allocate to other TLS blocks differ by whether the module is of the system or user-created. TLS blocks corresponding to system modules are allocated from the system's reserved area. TLS blocks corresponding to a user-created module are allocated from the heap area or from the heap area that has been replaced for TLS.

When a module that defines TLS variables is unloaded from a process, the TLS blocks defined by that module will be released. However, this release processing will be carried out with a delay. The TLS runtime library will check whether it is appropriate to carry out release processing using access to a TLS variable as a trigger; and if there is a TLS block that should be released, the library will carry out release processing as part of the processing to access the TLS variable.

## Areas for Non-POD Type TLS Variables

When a TLS variable has a non-POD type, the constructor for the TLS variable will be executed when it is first used in each thread, and information for post-processing will be recorded upon success. (In other words, a destructor for the non-POD type TLS variable will be registered.) 48 bytes will be allocated from the heap area for this purpose. This 48-byte area will be freed upon thread termination or an `sceLibcForceTlsDestructor()` call.

Note that upon first using a non-POD type TLS variable after each thread creation, an additional 32 bytes will be allocated for post-processing, and it will be freed upon thread termination.

When a TLS variable is a POD type, these areas will not be allocated.

## Releasing Memory for Threads

Memory resources allocated for the main thread are not returned.

The release of memory allocated to non-main threads are, as described earlier, carried out with a delay. Once allocated, memory will not be immediately returned to the kernel and will be temporarily cached by the thread runtime library.

In the current system, a cache check is carried upon thread termination. If the number of threads that have been cached exceeds a certain number, memory for the terminated thread is returned to the kernel. This condition may be changed in the future - do not create your program to be dependent on this condition.

## Thread Attribute Objects

Thread attribute objects are allocated from the system's reserved area when calling `scePthreadAttrInit()`. They can be released by calling `scePthreadAttrDestroy()`.

Processing to delay the allocation/release is not carried out for the thread attribute objects.

## Summary

The above content is summarized in the table below ("[Memory Resources of the Main Thread](threads-and-memory-resources.html#kernel-overview_5_6__f8bcac7e-eb25-1f02-8ffc-23c653bc0009)" and "[Memory Resources of Non-main Threads](threads-and-memory-resources.html#kernel-overview_5_6__f8bcac7e-eb25-1f02-8ffc-23c653bc000a)").

Memory Resources of the Main Thread

| **Usage** | **Allocation location/ method** | **Size** | **Allocation timing** | **Release timing** |
| --- | --- | --- | --- | --- |
| Stack area | Process space | 2 MiB | Upon process creation | Not released |
| Thread management object | System reserved area | Not disclosed | Upon process creation | Not released |
| TLS management object | System reserved area | Not disclosed | Upon process creation | Not released |
| Main module TLS block | Flexible memory | Dependent on the TSL segment size | Upon process creation | Not released |
| Other TLS block | `malloc()` or `malloc()` replaced for TLS | Dependent on the TSL segment size | Upon first accessing the TLS variable | Determined by the thread runtime library |
| Registration of a destructor for a non-POD type TLS variable | `malloc()` | 32 bytes | Upon first using a non-POD type TLS variable after thread creation | Upon thread termination |
| 48 bytes per constructor call for a non-POD type TLS variable | Upon first accessing the TLS variable | Upon thread termination or `sceLibcForceTlsDestructor()` call |

Memory Resources of Non-main Threads

| **Usage** | **Allocation location/ method** | **Size** | **Allocation timing** | **Release timing** |
| --- | --- | --- | --- | --- |
| Stack area | Process space | 64 KiB | Determined by the thread runtime library | Determined by the thread runtime library |
| Thread management object | System reserved area or cache within the thread runtime library | Not disclosed | Determined by the thread runtime library | Determined by the thread runtime library |
| TLS management object | System reserved area or cache within the thread runtime library | Not disclosed | Determined by the thread runtime library | Determined by the thread runtime library |
| Main module TLS block | `malloc()` or `malloc()` replaced for TLS | Dependent on the TSL segment size | Determined by the thread runtime library | Determined by the thread runtime library |
| Other TLS block | `malloc()` or `malloc()` replaced for TLS | Dependent on the TSL segment size | Upon first accessing the TLS variable | Determined by the thread runtime library |
| Registration of a destructor for a non-POD type TLS variable | `malloc()` | 32 bytes | Upon first using a non-POD type TLS variable after thread creation | Upon thread termination |
| 48 bytes per constructor call for a non-POD type TLS variable | Upon first accessing the TLS variable | Upon thread termination or `sceLibcForceTlsDestructor()` call |