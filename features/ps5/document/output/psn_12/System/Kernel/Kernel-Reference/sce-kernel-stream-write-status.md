# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-stream-write-status.html

# File System (StreamWrite)

# SceKernelStreamWriteStatus

StreamWrite status

## Definition

```
typedef struct SceKernelStreamWriteStatus {
    int64_t size;
    int64_t reserved0;
    int64_t tail_offset;
    int64_t stored_size;
    int64_t reserved1[4];
} SceKernelStreamWriteStatus;
```

## Members

|  |  |
| --- | --- |
| `size` | Maximum size in bytes of the data that can be retained by the StreamWrite |
| `reserved0` | Reserved |
| `tail_offset` | The end position (number of bytes from the beginning) of the readable data |
| `stored_size` | Size in bytes of the readable data |
| `reserved1` | Reserved |

## Description

This structure represents the status of a StreamWrite. The range of the data that is being retained by the StreamWrite at the point when the structure is obtained with `sceKernelStreamWriteStat()` and that can be read with `sceKernelStreamWriteRead()` is `stored_size` bytes from the position (`tail_offset` - `stored_size`).

# sceKernelStreamWriteActivate

Activate a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteActivate(
    int stream_id, 
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `stream_id` | StreamWrite identifier |
| `flags` | Reserved (specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Either the `stream_id` does not exist or the StreamWrite has already been activated |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Insufficient resources to activate the StreamWrite |

## Description

This function activates the StreamWrite specified with `stream_id`.

The `stream_id` must be one obtained with `sceKernelStreamWriteCreate()`.

Reading and writing are enabled when this function succeeds and the StreamWrite is activated.

## See Also

`sceKernelStreamWriteDeactivate()`

# sceKernelStreamWriteCreate

Create a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteCreate(
    size_t size, 
    int *stream_id
)
```

## Arguments

|  |  |
| --- | --- |
| `size` | Maximum size of the data that can be retained by the StreamWrite (in bytes, a positive multiple of 64 KiB, maximum of 2 GiB) |
| `stream_id` | Destination to store the StreamWrite identifier |

## Return Values

Stores the obtained StreamWrite identifier in `*stream_id` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `stream_id` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Either `size` is not a positive multiple of 64 KiB or is larger than the maximum value |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Insufficient resources to create a StreamWrite |

## Description

This function creates a StreamWrite. An identifier is obtained when this function succeeds.

To perform writing or reading with the StreamWrite that is created, it must first be activated with `sceKernelStreamWriteActivate()`.

## See Also

`sceKernelStreamWriteDelete()`

# sceKernelStreamWriteDeactivate

Deactivate a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteDeactivate(
    int stream_id, 
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `stream_id` | StreamWrite identifier |
| `flags` | Reserved (specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Either the `stream_id` does not exist, or the StreamWrite has already been deactivated |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function deactivates the StreamWrite specified with `stream_id`.

The `stream_id` must be one activated with `sceKernelStreamWriteActivate()`.

Writing to, and reading from, the StreamWrite will no longer be possible if this function succeeds.

# sceKernelStreamWriteDelete

Delete a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteDelete(
    int stream_id
)
```

## Arguments

|  |  |
| --- | --- |
| `stream_id` | StreamWrite identifier |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | `stream_id` is activated |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `stream_id` does not exist |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function deletes the StreamWrite specified with `stream_id`.

The `stream_id` must be one that was obtained with `sceKernelStreamWriteCreate()` and must have been deactivated with `sceKernelStreamWriteDeactivate()`.

# sceKernelStreamWriteRead

Read data from a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteRead(
    int stream_id,
    const void *buf,
    size_t size,
    off_t offset,
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `stream_id` | StreamWrite identifier |
| `buf` | Buffer to store the read data |
| `size` | Size of the data to read (a non-negative multiple of 64 KiB) |
| `offset` | Position to start reading (bytes from the beginning, a multiple of 64 KiB) |
| `flags` | Reserved (specify 0) |

## Return Values

Stores the read data in `*buf` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `buf` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `stream_id` does not exist |
| `size` is not a non-negative multiple of 64 KiB |
| `offset` is not a multiple of 64 KiB |
| Invalid data is included in the range specified with `size` and `offset` |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function reads data from a StreamWrite. `size` bytes of data from the position that is `offset` bytes from the beginning of the StreamWrite specified with `stream_id` are read and stored in the buffer specified with `buf`.

`stream_id` must have been activated with `sceKernelStreamWriteActivate()`.

The data can be read an indefinite number of times, as long as it is valid. Invalid data in ranges that have been deleted due to new writes or in ranges that have yet to be written cannot be read.

## See Also

`sceKernelStreamWriteWrite()`

# sceKernelStreamWriteStat

Obtain the status of a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteStat(
    int stream_id,
    SceKernelStreamWriteStatus *status
)
```

## Arguments

|  |  |
| --- | --- |
| `stream_id` | StreamWrite identifier |
| `status` | Destination to store the status of the StreamWrite |

## Return Values

Stores the obtained StreamWrite status in `*status` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `status` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `stream_id` does not exist |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function obtains the status of a StreamWrite.

The `stream_id` must be one that was obtained with `sceKernelStreamWriteCreate()`. However, it does not need to have been activated with `sceKernelStreamWriteActivate()`.

# sceKernelStreamWriteWrite

Write data to a StreamWrite

## Definition

```
#include <kernel.h>
int sceKernelStreamWriteWrite(
    int stream_id,
    const void *buf,
    size_t size,
    int flags,
    off_t *written_offset,
    size_t *stored_size
)
```

## Arguments

|  |  |
| --- | --- |
| `stream_id` | StreamWrite identifier |
| `buf` | Buffer that stores the data to write |
| `size` | Size of the data to write (a non-negative multiple of 64 KiB) |
| `flags` | Reserved (specify 0) |
| `written_offset` | Destination to store the position (number of bytes from the beginning) where writing started |
| `stored_size` | Destination to store the size (in bytes) of the readable data that is retained in the StreamWrite |

## Return Values

Stores the position where writing started in `*written_offset` and the readable data size in `*stored_size` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `buf`, `written_offset`, or `stored_size` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `stream_id` does not exist |
| Either `size` is not a non-negative multiple of 64 KiB or exceeds the size of the StreamWrite |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function writes data to a StreamWrite. The data specified with `buf` and `size` is written to the StreamWrite specified with `stream_id`.

`stream_id` must have been activated with `sceKernelStreamWriteActivate()`.

If writing succeeds, then `*stored_size` will increase, unless the maximum data size that can be retained, as specified with `sceKernelStreamWriteCreate()`, has been reached. If the maximum is exceeded, data will be deleted in order from oldest to newest, and the size of `*stored_size` will be identical to the maximum. `size` bytes of data will be placed sequentially from `*written_offset`.

After writing has succeeded, the range readable with `sceKernelStreamWriteRead()` will be `*stored_size` bytes from the position given by (`*written_offset` + `size` - `*stored_size`).

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.