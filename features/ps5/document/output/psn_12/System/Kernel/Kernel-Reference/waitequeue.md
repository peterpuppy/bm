# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/waitequeue.html

# Block Reason Codes

## Kernel Primitives

# WAIT\_EQUEUE

Waiting for an event queue

## Description

This block reason code is signaled when the thread is waiting for an event queue.

# WAIT\_EVENTFLAG

Waiting for an event flag

## Description

This block reason code is signaled when the thread is waiting for an event flag.

# WAIT\_INTERNAL

Waiting for a system shared resource

## Description

This block reason code is signaled when the thread is waiting for a system shared resource.

Normally, waiting for system shared resources will end in an extremely short amount of time. If a block lasts for a long time due to this reason, there is a possibility that a thread calling an SDK function that uses the same shared resource is being preempted.

# WAIT\_IO

Processing a request

## Description

This block reason code is signaled when the thread is waiting for device I/O (or an I/O equivalent) operation.

Such waits have the possibility of lasting for a long time due to external factors. It may be beneficial to adjust the SDK function calls so that such waits do not occur in timing-sensitive threads.

# WAIT\_NONE

No wait reason

## Description

This block reason code is signaled when there is no reason whatsoever for thread operation to be blocked.

# WAIT\_OTHER

Unknown block reason

## Description

This block reason code is signaled when the reason of thread operation being blocked cannot be identified.

Waits with this code are not abnormal.

# WAIT\_SEMAPHORE

Waiting for a semaphore

## Description

This block reason code is signaled when the thread is waiting for a semaphore.

# WAIT\_SLEEP

Sleeping

## Description

This block reason code is signaled when the thread is sleeping by using a function such as `sceKernelSleep()`.

# WAIT\_THREAD\_SUSPEND

The thread is paused due to a suspend reason

## Description

This block reason code is signaled when the thread cannot be executed due to debug suspension or process suspension.

## SDK API

# WAIT\_PTHREAD\_BARRIER

Waiting for a barrier

## Description

This block reason code is signaled when the thread is waiting for a barrier.

# WAIT\_PTHREAD\_CONDVAR

Waiting for a condition variable

## Description

This block reason code is signaled when the thread is waiting for a condition variable.

In cases where a wait for a condition variable is ended using a function such as `scePthreadCondSignal()` and a wait for the associated mutex occurs, `WAIT_PTHREAD_MUTEX` will be signaled instead.

# WAIT\_PTHREAD\_JOIN

Waiting for another thread to terminate

## Description

This block reason code is signaled when the thread is waiting for another thread to terminate using a function such as `scePthreadJoin()`.

# WAIT\_PTHREAD\_MUTEX

Waiting for a mutex

## Description

This block reason code is signaled when the thread is waiting for a mutex.

# WAIT\_PTHREAD\_RUNTIME

Updating thread information

## Description

This block reason code is signaled when the thread runtime is updating the thread information. This wait will normally end in an extremely short amount of time.

If a block lasts for a long time due to this reason, there is a possibility that a thread calling another thread function is being preempted for a long time.

# WAIT\_PTHREAD\_RWLOCK\_RD

Waiting for a reader/writer lock (for reading)

## Description

This block reason code is signaled when the thread is waiting for a reader/writer lock for reading.

# WAIT\_PTHREAD\_RWLOCK\_WR

Waiting for a reader/writer lock (for writing)

## Description

This block reason code is signaled when the thread is waiting for a reader/writer lock for writing.

# WAIT\_USER

Waiting for a user object

## Description

This block reason code is signaled when the thread is waiting for a user land object.

## System Software

# WAIT\_SERVICE

Communicating with the system software

## Description

This block reason code is signaled when the thread is communicating with the system software.

Such waits have the possibility of lasting for a long time due to external factors. It may be beneficial to adjust the SDK function calls so that such waits do not occur in timing-sensitive threads.

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.