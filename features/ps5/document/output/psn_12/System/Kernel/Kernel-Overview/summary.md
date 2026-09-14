# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/summary.html

# Time Management

# Overview

The PlayStation®5 kernel provides three types of time: process time, process time counter with high-speed readability and fine granularity, and timestamps (current timestamp and network timestamp). In addition, system start time and monotonic time are also provided; however, these time types are for maintaining POSIX compatibility and their use is not recommended.

# Process Time

Process time is initialized to 0 upon process startup and incremented while the process is in operation. While the process is in operation - in context of this explanation - refers to the time other than when the process is suspended. Process suspension includes both process (application) suspension and system suspension, but not suspension by the debugger. In other words, process time is incremented during suspension by the debugger.

Process time can be obtained with `sceKernelGetProcessTime()`. The obtained time is in microsecond units and monotonic (only increasing and never decreasing).

Timeouts of synchronized objects and various sleeps (`sceKernelSleep()`, `sceKernelUsleep()`, `sceKernelNanosleep()`) are all synchronized with this process time. Timer events and high precision timer events are exceptions and are synchronized with actual time.

# Process Time Counter

The process time counter is a monotonic 64-bit counter that is initialized to 0 upon process startup and synchronized with the process time. It can be obtained with `sceKernelGetProcessTimeCounter()`.

The process time counter is provided for the purpose of replacing the CPU time stamp counter. Like the time stamp counter, the process time counter can be obtained without calling a system call. Its frequency is also equivalent to that for the time stamp counter and can be obtained with `sceKernelGetProcessTimeCounterFrequency()`.

Note that the CPU time stamp counter can be obtained with the rdtsc and rdtscp instructions; however, its use is not recommended. The reason for this is that the value upon process start is not constant; and because it is incremented during process suspension, the counter can advance greatly even when values are obtained in short intervals if a process suspension is included.

# Time

Time includes the current time that can be set on each console and the network time.

The current time is handled by `time()` of libc, as well as by `sceKernelGettimeofday()` and `sceRtcGetCurrentTick()` of the Rtc library. This current time is UTC. `localtime()` functions of libc and `sceRtcGetCurrentClockLocalTime()` of the Rtc library are provided for the obtainment of the local time, for which a time zone is added to UTC.

Note that the current time can be asynchronously changed by the setting of the console.

The network time is not dependent on the setting of the console. The network time is synchronized with the server upon sign-in to the PlayStation™Network and can be obtained with `sceRtcGetCurrentNetworkTick()`.

Note that the network timestamp may also be changed non-consecutively upon synchronization with the server.

Note:

For an explanation of the network time, refer to the [Rtc Library Overview](../Rtc-Overview/__document_toc.html) document. The Rtc library also provides functions required for calculating time, such as the time information formatting functions.

When requiring synchronization with time, make sure to use the current time or network time. When calculating time using another type of time or counter, make sure application design is carried out with careful consideration for the fact that the value may differ from the current time or network time due to process suspensions.

## Notes on Using POSIX-compatible API Features for Which Time is Specified for Timeout

As mentioned earlier, the current time can be changed by console settings. Regarding POSIX-compatible API features for which time is specified for timeout, timeout may become misaligned as in the following cases when the current time is changed during a wait.

* When the current time is set in the past: A timeout will occur earlier than the specified time
* When the current time is set in the future: A timeout will occur later than the specified time

For example, when setting the timeout time to 12:01 when the current time is 12:00, behavior may become as follows when the current time is changed.

* When the current time is set to 11:00: A timeout will occur at 11:01 (1 minute later)
* When the current time is set to 13:00: A timeout will occur at 13:00 (1 minute later)

In addition, if the application sets a timeout in consideration of a time relative to the current time and the current time is changed between the application's obtainment of the current time and the call of the API feature, the timeout time will not become misaligned, but operation may not be as the application intended.

For example, when setting the timeout time to 12:01 when the current time is 12:00 with the intention of causing a timeout after 1 minute, behavior may be as follows.

* When the current time is set to 11:00: A timeout will occur 1 hour and 1 minute later
* When the current time is set to 13:00: A timeout will occur immediately

As explained so far, whether the specified timeout time is intended to be a specific time or a time relative to the current time, operation may not be as intended. Note that the application is not allowed to prevent or predict changes in the current time that is dependent on console settings.

Therefore, the use of POSIX-compatible API features for which time is specified for timeout is not recommended. Instead, use the PlayStation®5 kernel API features indicated in the table below for which relative time is specified for timeout.

POSIX-compatible API Features for Which Time Is Specified for Timeout and PlayStation®5 Kernel API Features for Which Relative Time Is Specified

| **POSIX-compatible API features for which time is specified for timeout (not recommended)** | **PlayStation®5 kernel API features for which relative time is specified for timeout (recommended)** |
| --- | --- |
| `pthread_cond_timedwait()` | `scePthreadCondTimedwait()` |
| `pthread_mutex_timedlock()` | `scePthreadMutexTimedlock()` |
| `pthread_rwlock_timedrdlock()` | `scePthreadRwlockTimedrdlock()` |
| `pthread_rwlock_timedwrlock()` | `scePthreadRwlockTimedwrlock()` |
| `sem_timedwait()` | `sceKernelWaitSema()` |

# POSIX-compatible Times

The system start time (CLOCK\_UPTIME) and monotonic time (CLOCK\_MONOTONIC) are provided for maintaining compatibility with POSIX and with systems like POSIX.

The use of these types of time is not recommended. The reason for this is that the value upon process start is not constant; and because it is incremented during process suspension, the time can advance greatly even when values are obtained in short intervals if a process suspension is included. If these types of time are used, limit their use to the initial stages of transporting a program from the POSIX system and use the other types of time in other areas. In most cases, these time types can be replaced by the process time.

# Summary

Characteristics of time are summarized in the table below.

Characteristics of Time

| **Name** | **Granularity** | **Calling cost** | **Synchronization** | **During process suspension** | **Notes** |
| --- | --- | --- | --- | --- | --- |
| Process time | Microseconds | System call | Process operation | Stops |  |
| Process time counter | Nanoseconds | Function call | Process operation | Stops |  |
| Current time | Microseconds | System call | Console settings | Advances |  |
| Network time | Microseconds | System call | PlayStation™Network | Advances |  |
| Time stamp counter | Nanoseconds | CPU instruction |  | Advances | Not recommended |
| POSIX-compatible time | Nanoseconds | System call | System time | Advances | Not recommended |