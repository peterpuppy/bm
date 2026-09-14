# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/asynchronous-file-access.html

# File System

# Overview

The PlayStation®5 kernel provides a file system with the concepts of files and directories for storage management. The PlayStation®5 kernel file system provides features such as hierarchical naming, attribute management, protection, locking, and buffer management.

Note:

The PlayStation®5 SDK also provides the APR (Asynchronous Package Reader) library, which allows for high-speed reading of files using dedicated hardware without any intervening processing involving the file system. This library can easily be run in coordination with the AMM library and the Agc library. For details, refer to "APR Libraries Overview".

# File Access

## Functions

File access is performed with standard read/write functions such as `sceKernelRead()` and `sceKernelWrite()`.

## Paths

Paths are stored in a tree structure namespace using hierarchical naming. Regardless of physical storage differences, all paths are stored in a single namespace with a single tree structure. The path specifications are as follows.

* The path delimiter is "/".
* The character encoding is ASCII. Uppercase/lowercase characters are differentiated (may not be differentiated for some paths).
* The path length can be up to 1024 bytes including the termination character.
* The path specified by a PlayStation®5 kernel function must be an absolute path that starts with "/".

## File Access Using the Network

Access to files or directories in /host or system-managed host mirrors (see the [Workspaces Overview](../Workspaces-Overview/__document_toc.html) document for details) may fail with one of the following errors:

* If there is no connection to the host PC:`SCE_KERNEL_ERROR_ENOTCONN` (0x80020039)
* If a file system access error occurs on the host PC:`SCE_KERNEL_ERROR_EREMOTEIO` (0x8002006F)

# Asynchronous File Access

## Overview

This feature performs file access asynchronously. With synchronous file access that uses read/write functions such as `sceKernelRead()` or `sceKernelWrite()`, after the function call, control will not return to the thread until the read/write completes; therefore, it will not be possible to perform other tasks during such periods. By contrast, since asynchronous file access allows performing read/write request submissions and completion waits separately, threads will be able to execute other tasks during such periods. In addition, by submitting multiple asynchronous file access requests in advance, optimization will be performed by the system, and thus efficient file access can be expected.

## Usage Examples

The following explains the asynchronous file access process flow using file reads as examples.

**Asynchronous I/O request submission**

To use asynchronous file access to perform a file read, first use `sceKernelAioSubmitReadCommands()` to submit an asynchronous I/O read request to the system. For the `SceKernelAioRWRequest` request structure, specify `fd` (file descriptor), `offset` (read start position), `nbytes` (read size), `buf` (read buffer), and `result` for obtaining the results. It is also possible to submit multiple requests at the same time.

When this function submits request(s) to the system, an asynchronous I/O submit ID will be assigned as the request identifier, and the function will immediately terminate. The submit ID assigned at such times is used for specifying the request(s) when hereafter calling asynchronous I/O functions, such as when waiting for completion.

**Request state transitions**

Submitted requests will be retained in the `SCE_KERNEL_AIO_STATE_SUBMITTED` state in a queue.

When the system extracts a request from the queue and starts processing, the corresponding request will make a transition to the `SCE_KERNEL_AIO_STATE_PROCESSING` state. When device access completes and the specified data read completes, the corresponding request will make a transition to the `SCE_KERNEL_AIO_STATE_COMPLETED` state.

**Request completion waiting**

Call `sceKernelAioWaitRequest()` with a submit ID specified to perform a completion wait for the submitted request(s). If one of the corresponding requests is in the `SCE_KERNEL_AIO_STATE_SUBMITTED` or `SCE_KERNEL_AIO_STATE_PROCESSING` state, this function will wait until all requests with the specified submit ID assigned make a transition to the `SCE_KERNEL_AIO_STATE_COMPLETED` state.

Note that `sceKernelAioPollRequest()` is provided as a function that returns the current request state without performing blocking.

After a completion wait completes, the results will be stored in the request structure that was specified upon request submission. Specifically, the data will be read into `buf`, the number of bytes read will be stored in `result->returnValue`, and `SCE_KERNEL_AIO_STATE_COMPLETED` will be stored in `result->state`. If an error occurs during the data read, the corresponding error code will be stored in `result->returnValue`, and `SCE_KERNEL_AIO_STATE_COMPLETED` (same value as for wait success) will be stored in `result->state`.

**Request cancellation**

By calling `sceKernelAioCancelRequest()` with a submit ID specified, it will be possible to cancel request(s) in the queue. Only requests where the state is `SCE_KERNEL_AIO_STATE_SUBMITTED` can be cancelled. A request for which processing has already started and whose state is `SCE_KERNEL_AIO_STATE_PROCESSING` cannot be cancelled.

A cancelled request will make a transition to the `SCE_KERNEL_AIO_STATE_ABORTED` state. When `sceKernelAioWaitRequest()` is executed on a cancelled request, `SCE_KERNEL_AIO_STATE_ABORTED` will be stored in the argument `state`.

**Submit ID deletion**

Use `sceKernelAioDeleteRequest()` to delete an assigned submit ID. Note that `sceKernelAioWaitRequest()` or `sceKernelAioPollRequest()` must be used in advance to confirm that the request(s) with the submit ID assigned is in the `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED` state before the submit ID can be deleted.

## Scheduling and Optimization Parameters

The system provides queues with three levels of priority to applications, and when multiple asynchronous I/O requests have been submitted, they will be retained in the queue of the corresponding priority and will wait for execution. The three levels of priority are `SCE_KERNEL_AIO_PRIORITY_HIGH`, `SCE_KERNEL_AIO_PRIORITY_MID`, and `SCE_KERNEL_AIO_PRIORITY_LOW`.

When there are multiple requests with different priority levels, they will be processed in order starting with the highest level.

In principle, requests with the same priority will be processed in FIFO order, but the system will perform optimization in order to reduce seek times, and thus the order of execution may change. In cases where the file reading is frequently performed using synchronous I/O functions in multiple threads, by using asynchronous I/O functions instead to submit multiple requests at the same time, the system optimization will operate more effectively, increasing the overall throughput.

Queue States and Submission of Asynchronous I/O Requests with Different Priority Levels

By using `sceKernelAioInitialize()`, it will be possible to change the values related to system optimization for each queue level.

The targets for optimization by the system will be `schedulingWindowSize` number of requests from the start of the queue. Non-target requests will wait in the order that they were submitted. The greater the `schedulingWindowSize` value, the more optimization target requests increase and the more reductions in file access time can be expected, but the time required for optimization will increase. The smaller the `schedulingWindowSize` value, the fewer reductions in file access time, but the time required for optimization will decrease.

`delayedCountLimit` can be used to set the maximum number of times a target request for optimization will be skipped. While optimization can be performed more effectively by increasing the `delayedCountLimit` value, there is a possibility that the requests submitted afterward will be executed earlier, and it may take time until the requests submitted first are processed. By decreasing the `delayedCountLimit` value, the possibility of taking time until the requests submitted are processed due to order-of-execution changes will decrease, but there is a possibility that effective optimization cannot be performed.

When a request with a higher priority level is submitted while a request with a large size is being processed, there is a feature for splitting large sized requests in order to prevent the higher priority requests from being made to wait for a long time. The split feature will be enabled by setting `SCE_KERNEL_AIO_ENABLE_SPLIT` for `enableSplit`. When the request size is greater than `splitSize`, the request will be split into `splitChunkSize` sizes before it is processed by the system. The smaller the `splitChunkSize` value, the less time higher priority requests will wait, but the request processing efficiency will decrease due to the size decreasing for the data that can be consecutively processed by the system. The greater the `splitChunkSize` value, the longer higher priority requests will be made to wait, but the request processing efficiency will increase. If the split feature will not be used, set `SCE_KERNEL_AIO_DISABLE_SPLIT` for `enableSplit`. In such cases, the `splitSize` and `splitChunkSize` values will be ignored.

Visual Depiction of Scheduling Optimization

## Number of Asynchronous I/O Submit IDs Corresponding to Asynchronous I/O Requests

Multiple asynchronous I/O requests can be submitted by an application program with a single function call, but there are functions that return a single asynchronous I/O submit ID as the identifier of the request(s) received by the system, and there are functions that return submit IDs for the number of requests.

`sceKernelAioSubmitReadCommands()` and `sceKernelAioSubmitWriteCommands()` assign a single submit ID for all requests received. Meanwhile, `sceKernelAioSubmitReadCommandsMultiple()` and `sceKernelAioSubmitWriteCommandsMultiple()` assign a submit ID for each request received. For cancel functions, completion wait functions, etc., (called after requests are submitted) that receive submit ID(s) as an argument, use the former two functions ([sceKernelAioSubmitReadCommands()](../Kernel-Reference/sce-kernel-aio-submit-read-commands.html) and [sceKernelAioSubmitWriteCommands()](../Kernel-Reference/sce-kernel-aio-submit-write-commands.html)) to handle requests together. Use the latter two functions ([sceKernelAioSubmitReadCommandsMultiple()](../Kernel-Reference/sce-kernel-aio-submit-read-commands-multiple.html) and [sceKernelAioSubmitWriteCommandsMultiple()](../Kernel-Reference/sce-kernel-aio-submit-write-commands-multiple.html)) to handle each request separately.

Number of Asynchronous I/O Submit IDs Corresponding to Asynchronous I/O Requests

## Functions Where Multiple Asynchronous I/O Submit IDs Can Be Specified

Among the features provided by the asynchronous I/O functions, there are both functions that specify a single asynchronous I/O submit ID as an argument and functions that specify multiple asynchronous I/O submit IDs as an argument. These functions can be used regardless of the type of asynchronous I/O request submission function with which the submit ID was assigned. For example, it is possible to call `sceKernelAioSubmitReadCommands()` repeatedly to obtain multiple submit IDs, specify these submit IDs for `sceKernelAioWaitRequests()` (which specifies multiple submit IDs as an argument), and perform waits for these submit IDs.

## SCE\_KERNEL\_AIO\_STATE\_NOTIFIED and Completion Waits

`sceKernelAioWaitRequest()` is provided as a function that waits for completion of an asynchronous I/O submit ID (waits for completion of the asynchronous I/O request(s) with the submit ID assigned). Completion refers to a transition to the final state, which is `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED`.

If a submit ID is already complete when this function is called, this function will return immediately. Otherwise, this function will perform blocking until the submit ID completes. When this function is called multiple times for the same submit ID, the kernel will return `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED` for the first call, but for the second and following calls, a bitwise OR of one of these values and `SCE_KERNEL_AIO_STATE_NOTIFIED` (which indicates that a wait is already being performed) will be returned. In other words, when this function is called by multiple threads at the same time for the same submit ID, `SCE_KERNEL_AIO_STATE_COMPLETED`/`SCE_KERNEL_AIO_STATE_ABORTED` will be returned in one of the threads, and a bitwise OR of one of these values and `SCE_KERNEL_AIO_STATE_NOTIFIED` will be returned in the other threads.

Waiting for Completion of the Same Asynchronous I/O Submit ID in Multiple Threads

By using `sceKernelAioWaitRequests()`, it will also be possible to wait for multiple submit IDs at the same time.

At such times, the completion wait mode can be specified with the argument `mode`. When `mode` is `SCE_KERNEL_AIO_WAIT_AND`, waiting will be performed until all of the specified submit IDs complete. When `mode` is `SCE_KERNEL_AIO_WAIT_OR`, waiting will be performed until one of the submit ID newly completes. When all of the specified submit IDs complete when calling this function, this function will immediately return.

## Deleting Asynchronous I/O Submit IDs

Assigned asynchronous I/O submit IDs must ultimately be deleted. Before deleting a submit ID, `sceKernelAioWaitRequest()` or `sceKernelAioPollRequest()` must be called in advance to confirm that the submit ID is in the `SCE_KERNEL_AIO_STATE_COMPLETED` or `SCE_KERNEL_AIO_STATE_ABORTED` state.

# StreamWrite

## Overview

The file system of the PlayStation®5 kernel provides methods of accessing StreamWrites. A StreamWrite is a ring buffer allocated to the long-lifespan area of the SSD. It can continue to write without being impacted by "[SSD Write Throttling](ssd-write-throttling.html)" (see below), the mechanism that restricts bandwidth for writing to low-lifespan areas. For example, it may be used to write at a constant bandwidth, such as when saving a video stream for a particular application.

A StreamWrite has the structure of a ring buffer, but it is not storage to which data can be appended without limit. An upper limit to the data size that can be retained must be set; when data in excess of the upper limit is written, data is deleted from oldest to newest.

Mechanism of a StreamWrite

## Usage

Usage of StreamWrites is described in simple terms below.

First, call `sceKernelStreamWriteCreate()` to create a StreamWrite. When doing so, specify an upper limit for the data size that the StreamWrite can retain. Next, activate the StreamWrite that was created with `sceKernelStreamWriteActivate()`. This enables writing to, and reading from, the StreamWrite.

Writing to a StreamWrite is done using `sceKernelStreamWriteWrite()`. The data to be written must be of a size (`size`) that is a non-negative multiple of 64 KiB. When writing succeeds, the number of bytes from the beginning of the StreamWrite indicating the position where the write started (`*written_offset`) and the size of the readable data (`*stored_size`) are obtained. At this point, the relationships among `size`, `*written_offset`, and `*stored_size` are similar to those shown in the figure below.

Relationships Among size, \*written\_offset, and \*stored\_size

Therefore, the range of the data that can be read with `sceKernelStreamWriteRead()` is `*stored_size` bytes from the position given by (`*written_offset` + `size` - `*stored_size`). Note that, although `*written_offset` monotonically increases, it will become negative once 8 EiB - 1 byte are exceeded. (However, exceeding this value is not realistically possible.)

Reading from a StreamWrite is done with `sceKernelStreamWriteRead()`. As long as the data in the range specified by the offset and the size is valid, the data can be read an indefinite number of times. Reading of invalid data in ranges deleted due to new writes or in ranges that have yet to be written to is not possible. The offset must be a multiple of 64 KiB, and the size must be a non-negative multiple of 64 KiB.

Additionally, the status of a StreamWrite can be obtained with `sceKernelStreamWriteStat()`. This status is obtainable regardless of whether the StreamWrite has been activated. Using the member variables of the `SceKernelStreamWriteStatus` structure obtained when this function succeeds, the range of data that is readable at that point can be expressed as `stored_size` bytes from the position given by (`tail_offset` - `stored_size`).

To terminate usage of a StreamWrite and to deactivate it, call `sceKernelStreamWriteDeactivate()`. If this function succeeds, writing to, and reading from, the StreamWrite will no longer be possible.

Finally, call `sceKernelStreamWriteDelete()` to delete the no-longer-needed StreamWrite.

## Resource Restrictions

StreamWrites have the following resource restrictions:

* Maximum number of StreamWrites an application can create: 1
* Maximum value for the upper-limit size (specified when the StreamWrite is created) of the data that a StreamWrite can retain: 2 GiB

## Lifespan of a StreamWrite

A StreamWrite that has been created will only continue to exist while its application is running (including when suspended). Therefore, a StreamWrite will not exist at the time of application launch, even if the application created one in the past; a new one must be created.

## Sample Program

A sample program using the StreamWrite functions is as follows:

* **sample\_code/system/api\_stream\_write**

  This sample exemplifies basic usage of the StreamWrite functions.

# Slow SSD Mode

This feature emulates a state in which the system is accessing the SSD to the greatest possible extent and read/write processing by the application involving the SSD is slow. This feature can be set to "On" from "★Debug Settings" > "Game" > "Slow SSD Mode". Use this feature to confirm that dropped frames, audio cutting out, and other problems do not occur.

# SSD Write Throttling

## Overview

There is a physical upper limit regarding the number of writes to the SSD and writes exceeding this upper limit are not possible. In addition, the SSD has areas with a long lifetime where a relatively large number of writes is possible and areas with a short lifetime where the number of writes is limited to several writes.

Of the areas that an application can write to, all areas other than the aforementioned "[StreamWrite](stream-write.html)" are areas with a short lifetime. The bandwidth is limited for writes to areas with a short lifetime in order to guarantee the lifetime of the SSD. This mechanism for limiting the bandwidth is called "SSD write throttling". (It does not limit bandwidth for writing to the /devlog directory or any of its subdirectories, which can only be used during development.)

## SSD Write Throttling Operation

SSD write throttling limits the bandwidth over a long period of time so as to not lower performance, even when unexpected writes to the SSD occur. Specifically, it will be possible to perform a write of 2400 MiB in 20 minutes under default settings.

Amounts that can be written will be managed based on this value as the initial "budget" value. This initial budget value (2400 MiB) will be given upon application startup and reduced according to the amount written. In addition, independent of the reduction due to writes, the budget will be increased by 2 MiB every second with the initial budget value as the upper limit. The budget will be deleted when the application terminates.

The bandwidth's limit value will be calculated every second based on the budget at the time and applied on the bandwidth. The limit value varies as shown in the table below, with boundaries such as 100%, 50%, 25%, 12%, and 6% in comparison to the initial budget value.

Bandwidth will not be limited within the range of 50% to 100%. Bandwidth and the amount that can be written will be limited step by step below 50%.

The operation of SSD write throttling is determined by the actual amount of data written to the SSD. Be aware that writes to the SSD are performed in units of 64 KiB, so any writes smaller than 64 KiB or that are not aligned to 64 KiB are rounded up to the next multiple of 64 KiB for the purpose of calculation.

Ratio of the Budget and the Bandwidth Limit Value

| **Ratio of the Initial Budget Value (%)** | **Bandwidth Limit Value (MiB/Second)** |
| --- | --- |
| 50 to 100 | Not applied |
| 25 to 49 | 25 |
| 12 to 24 | 10 |
| 6 to 11 | 1 |
| Less than 6 | 0.5 |

## Settings During Development

The operation and state of SSD write throttling can be changed using the configuration items under "★Debug Settings" > "Game" > "SSD Write Throttling".

* **Debug Notification**

  When this is turned "On", the notification provided below is displayed if there is any change to the bandwidth limit value. ("XX" is replaced with the bandwidth limit value after the change or with "No Limit".)

  Kernel: SSD write throttling level has been changed (XX)
* **Mode** (Not available in Release Mode)

  This sets the method of limiting bandwidth. Choose one of the following.

  + Default

    Standard SSD write throttling will be performed as on retail units. Bandwidth will be limited based on the budget.
  + Force Throttling

    The lowest level bandwidth will be applied regardless of the budget value.
  + Disabled

    Limits on the bandwidth will not be applied regardless of the budget value. When this item is set, other configuration items will be ignored.
* **Reset Write Count** (Not available in Release Mode)

  This item is for resetting the initial budget value of the running application.

# Notes Specific to the PlayStation®5

## Access to Application File Sets and Additional Content File Sets

Of the areas that can be accessed from the application, the behavior of functions that specify a path string for the argument differs in application file sets and additional content file sets than in other areas.

A hash table is used in these areas to search for a file/directory from a path; this implementation is optimized under the assumption that the path specified to the argument always exists. Because of this, there is no guarantee that the search will be correctly carried out when a path that does not exist is specified. If paths exist for which hash values collide, the specified path may be confused with another path and there is a danger of unintended processing being carried out.

In a case where a path - that may or may not exist - has to be specified, use `sceKernelCheckReachability()` to evaluate the safety of the path. For an existing path, appropriate processing will be carried out, including the case when hash values collide, and there is no need to take other precautionary measures. Bandwidth Restrictions When Running in the Background

## Internal storage bandwidth will be restricted when the application is running in the background.

When an application is running in the background, the minimum guaranteed bandwidth of console storage/M.2 SSD storage will be restricted to half of what it would be when running in the foreground.