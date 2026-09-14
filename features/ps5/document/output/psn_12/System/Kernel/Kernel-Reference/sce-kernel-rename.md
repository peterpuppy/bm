# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-rename.html

# File System

# SceKernelDirent

Directory entry

## Definition

```
#include <kernel.h>
typedef struct {
    u_int32_t d_fileno;
    u_int16_t d_reclen;
    u_int8_t d_type;
    u_int8_t d_namlen;
    char d_name[SCE_KERNEL_MAXNAMLEN + 1];
} SceKernelDirent;
```

## Members

|  |  |
| --- | --- |
| `d_fileno` | File number |
| `d_reclen` | Directory record length (bytes) |
| `d_type` | File type |
| `d_namlen` | Filename length |
| `d_name` | Filename (NULL-terminated) |

## Description

This structure represents a directory entry in a format that is not dependent on a file system. This structure is used for receiving the directory entry read with `sceKernelGetdents()`/`sceKernelGetdirentries()`.

`d_fileno` is a unique number in a file system that indicates individual files. The value 0 indicates a deleted directory entry.

`d_reclen` is the directory record length (units: bytes). It represents space required when storing the directory entry in a buffer.

`d_type` is the format of the file indicated by this directory entry. It takes one of the following values: `SCE_KERNEL_DT_UNKNOWN` (type unknown), `SCE_KERNEL_DT_DIR` (directory), or `SCE_KERNEL_DT_REG` (regular file).

`d_name` is the filename of the file indicated by this directory entry and is NULL-terminated. `d_namlen` is the length of the filename excluding the NULL-terminator character.

## See Also

`sceKernelGetdents()`, `sceKernelGetdirentries()`

# SceKernelIovec

Divided input/output buffer specification

## Definition

```
typedef struct SceKernelIovec {
    void *iov_base; 
    size_t iov_len; 
} SceKernelIovec;
```

## Members

|  |  |
| --- | --- |
| `iov_base` | Buffer address |
| `iov_len` | Buffer size |

## Description

This structure is used to specify individual input/output buffers. An array of the structures is assigned as arguments to the functions such as `sceKernelReadv()` and `sceKernelWritev()` that perform divided input/output.

## See Also

`sceKernelPreadv()`, `sceKernelPwritev()`, `sceKernelReadv()`, `sceKernelWritev()`

# SceKernelStat

File status

## Definition

```
#include <kernel.h>
typedef struct {
    ...
    mode_t st_mode;
    ...
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    off_t st_size;
    blkcnt_t st_blocks;
    blksize_t st_blksize;
    ...
    struct timespec st_birthtim;
    ...
} SceKernelStat;
```

## Members

|  |  |
| --- | --- |
| `st_mode` | Access mode |
| `st_atim` | Last access time |
| `st_mtim` | Last data change time |
| `st_ctim` | Last file status change time |
| `st_size` | File size |
| `st_blocks` | Number of blocks allocated to the file |
| `st_blksize` | File alignment size appropriate for I/O |
| `st_birthtim` | Time when the file was created |

## Description

This structure indicates the file status. It is used when obtaining file information with `sceKernelStat()` or `sceKernelFstat()`. The above only lists members that have significant values.

Regarding the access rights, the bitwise OR of the following values representing the access mode will be stored in `st_mode`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_S_INONE` | 0000000 | No access right |
| `SCE_KERNEL_S_IRU` | 0000555 | Permit read |
| `SCE_KERNEL_S_IRWU` | 0000777 | Permit read and write |
| `SCE_KERNEL_S_IFDIR` | 0040000 | Directory |
| `SCE_KERNEL_S_IFREG` | 0100000 | Regular file |
| `SCE_KERNEL_S_IFMT` | 0170000 | Mask of the file type |

The following macros are provided for checking the `st_mode` value to see if the file is a directory or a regular file.

* `SCE_KERNEL_S_ISDIR(st_mode)`: Return non-0 if a directory, 0 if not
* `SCE_KERNEL_S_ISREG(st_mode)`: Return non-0 if a regular file, 0 if not

As the time stamp, the following information will be stored.

* `st_atim`: Time of last access (most recent date and time when the file data was accessed using `sceKernelFutimes()`, `sceKernelRead()`, `sceKernelReadv()`, or `sceKernelUtimes()`) (To improve performance of the file system, this time may not always be updated.)
* `st_mtim`: Time of last data change (most recent date and time when the file data was changed using `sceKernelMkdir()`, `sceKernelFutimes()`, `sceKernelUtimes()`, `sceKernelWrite()`, or `sceKernelWritev()`)
* `st_ctim`: Time of last file status change (most recent date and time when the inode data was changed using `sceKernelChmod()`, `sceKernelFutimes()`, `sceKernelMkdir()`, `sceKernelRename()`, `sceKernelRmdir()`, `sceKernelTruncate()`, `sceKernelUnlink()`, `sceKernelUtimes()`, `sceKernelWrite()`, or `sceKernelWritev()`)
* `st_birthtim`: Date and time when inode was created

Regarding the file size, the following information will be stored.

* `st_size`: File size in bytes
* `st_blocks`: Number of blocks allocated to the file
* `st_blksize`: File alignment size appropriate for I/O

  I/O efficiency can be improved by specifying a multiple of `st_blksize` as the file offset upon calling file I/O functions.

## See Also

`sceKernelStat()`, `sceKernelFstat()`

# sceKernelCheckReachability

Check whether a path actually exists

## Definition

```
#include <kernel.h>
int sceKernelCheckReachability(
    const char *path
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Path to check |

## Return Values

Returns `SCE_OK` (=0) when the specified path exists.

Returns one of the following error codes (a negative value) when existence could not be confirmed.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | File or directory does not exist for the specified path |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Failed to allocate memory for the check processing |

## Description

This function checks whether a path, for which validity has not been guaranteed, can be used safely.

To quickly open a file, some read-only file systems are designed with the assumption that only existing files and directories will be accessed. Such file systems may not be able to correctly interpret nonexistent paths and may interpret such a path as pointing to an unintended file. For example, when passing a nonexistent path to `sceKernelOpen()`, an error (`SCE_KERNEL_ERROR_ENOENT`) may not be returned and an unintended file may be opened.

If `SCE_OK` is obtained when checking a path with this function, it is guaranteed that the above-described misinterpretations will not occur in subsequent operations.

The distinction of upper case/lower case in the string specified to `path` will be appropriately processed according to whether upper case and lower case are distinguished in the target file system.

## Notes

* Of the paths accessed by an application, those that require a safety check are in the following directories.
  + `/app0/` (application file set)
  + `/addcont0/` to `/addcont63/` (additional content file sets)
* The safety of paths not included in the directories mentioned above may not be checked reliably.
* The safety of paths on host PCs may not be checked reliably, even if those paths are included in the directories mentioned above.
* There is no need to perform safety checks if the directories mentioned above are in a workspace.
* Because the processing of this function may require a long time, minimize its use.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

# sceKernelChmod

Change file access rights (by specifying a path)

## Definition

```
#include <kernel.h>
int sceKernelChmod(
    const char *path, 
    SceKernelMode mode
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the file to change |
| `mode` | New access rights |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error. (In such cases, the file access rights will not change.)

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of the path is not a directory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Specified file does not exist |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the path |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Changing rights not held |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` points to invalid memory |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `path` is invalid |

## Description

This function changes the access rights of the file specified with `path`. Changing is performed after confirming that the process owner (user program) is the target file's owner.

For `mode`, specify one of the following values that indicate the access rights after the change.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_S_INONE` | 0000000 | No access right |
| `SCE_KERNEL_S_IRU` | 0000555 | Permit read |
| `SCE_KERNEL_S_IRWU` | 0000777 | Permit read and write |

## Notes

* `sceKernelFchmod()` is provided as a function that performs operations equivalent to this function but specifies a descriptor of a file that is already open.
* The current access rights can be obtained using `sceKernelStat()`.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`sceKernelFchmod()`, `sceKernelStat()`

# sceKernelClose

Close a file

## Definition

```
#include <kernel.h>
int sceKernelClose(
    int d
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the file to close |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Close of `d` is not permitted  \* SLV detection target error |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not an active descriptor |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Cached data would not fit in the underlying object and was lost |

## Description

This function closes the specified file. Specifically, the kernel deletes the specified descriptor from the object reference table that exists per process, and if the other descriptors referencing the same file as this descriptor do not exist, the file will be closed.

In addition, the read/write position of the file will be lost.

## Notes

* All descriptors will be deleted when the process terminates, even if this function is not called. However, there is a limit to the number of active descriptors for each process, so explicitly delete file descriptors using this function as is appropriate for programs handling many files.
* When a file is closed, the cached data will not always be written to storage. To explicitly write data left in the cache to storage, use `sceKernelSync()` or use `sceKernelFsync()`/`sceKernelFdatasync()` with an active descriptor specified.
* This function returns the `SCE_KERNEL_ERROR_EPERM` error when descriptor 0/1/2 is specified.

## See Also

`sceKernelSync()`, `sceKernelFsync()`, `sceKernelFdatasync()`

# sceKernelFchmod

Change file access rights (by specifying a descriptor)

## Definition

```
#include <kernel.h>
int sceKernelFchmod(
    int fd, 
    SceKernelMode mode
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the file to change |
| `mode` | New access rights |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid descriptor |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function changes the access rights of the file referenced by the descriptor specified with `fd`. Changing is performed after confirming that the process owner (user program) is the target file's owner.

For `mode`, specify one of the following values that indicate the access rights after the change.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_S_INONE` | 0000000 | No access right |
| `SCE_KERNEL_S_IRU` | 0000555 | Permit read |
| `SCE_KERNEL_S_IRWU` | 0000777 | Permit read and write |

## Notes

* `sceKernelChmod()` is provided as a function that performs operation equivalent to this function but specifies a file pathname.
* The current access rights can be obtained using `sceKernelFstat()`.

## See Also

`sceKernelChmod()`, `sceKernelFstat()`

# sceKernelFcntl

Set/get file flags

## Definition

```
#include <kernel.h>
int sceKernelFcntl(
    int fd, 
    int cmd,
    ... /* int arg (on setting) */
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target file |
| `cmd` | `SCE_KERNEL_F_GETFL` (get) or `SCE_KERNEL_F_SETFL` (set) |
| `arg` | Flag values to set (for setting only) |

## Return Values

For normal termination, returns the flag values if `SCE_KERNEL_F_GETFL` was specified for `cmd` and returns a value (of 0 or greater) other than an error code in other cases.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid already-open file descriptor |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | An unsupported value is specified for `cmd` |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | A socket is specified for `fd` |

## Description

This function obtains or sets the flags (the read/write option specifications) for the file specified with `fd`.

For `cmd`, specify `SCE_KERNEL_F_GETFL` when obtaining the flags and specify `SCE_KERNEL_F_SETFL` when setting the flags.

`arg` is valid only when setting the flags. Specify the bitwise OR of the following flag values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_O_NONBLOCK` | 0x0004 | Non-blocking I/O (the error `SCE_KERNEL_ERROR_EAGAIN` occurs when waiting is required for a read/write operation within the kernel) |
| `SCE_KERNEL_O_APPEND` | 0x0008 | Append write (all writes are added to the end of the file) |
| `SCE_KERNEL_O_DIRECT` | 0x00010000 | Minimized cache (reading/writing is performed with minimal cache usage) |

## Notes

* The flags that can be specified with this function are some of the flags that can be specified when opening a file using `sceKernelOpen()`.
* Note that when `SCE_KERNEL_O_DIRECT` is inappropriately set, performance may decrease greatly.
* A socket cannot be specified for `fd`. If you want to set a non-blocking behavior for a socket, set the `SCE_NET_SO_NBIO` socket option using `sceNetSetsockopt()`.

## See Also

`sceKernelOpen()`

# sceKernelFdatasync

Synchronize file content and storage

## Definition

```
#include <kernel.h>
int sceKernelFdatasync(
    int fd
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target file |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid descriptor |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function synchronizes the content of the file or directory specified in `fd` with the storage.

This function is the same as `sceKernelFsync()` in that it synchronizes file content and storage; however, it differs in that it does not synchronize metadata changes with storage as long as there is no change required to correctly read the file content so that storage accesses can be decreased.

For example, the changes to last access time, last data change time, and/or last file status change time (`st_atim`, `st_mtim`, `st_ctim`, respectively) are sometimes not synchronized, but metadata is synchronized if write entailing a file extension is carried out or if the file size (`st_size`) is changed by `sceKernelFtruncate()`.

## Notes

* Depending on the file system, this function will behave exactly the same as `sceKernelFsync()`.
* When `SCE_KERNEL_O_DSYNC` is specified to the `flags` argument upon opening a file with `sceKernelOpen()`, a synchronization equivalent to this function will be carried out upon changing the content of the file or directory.

## See Also

`sceKernelFsync()`

# sceKernelFstat

Get file status (by specifying a descriptor)

## Definition

```
#include <kernel.h>
int sceKernelFstat(
    int fd, 
    SceKernelStat *sb
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target file |
| `sb` | Destination to store the obtained file status |

## Return Values

Stores the obtained file status in `*sb` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid already-open file descriptor |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `sb` points to an invalid address |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EOVERFLOW` | 0x80020054 | File size (bytes) overflowed |

## Description

This function obtains various information about the file referenced by the descriptor specified with `fd`. For details on the information that can be obtained, refer to the `SceKernelStat` structure.

## Notes

`sceKernelStat()` is provided as a function that performs operation equivalent to `sceKernelFstat()` but specifies a file pathname.

## See Also

`SceKernelStat`, `sceKernelStat()`

# sceKernelFsync

Synchronize the file and storage (by specifying a descriptor)

## Definition

```
#include <kernel.h>
int sceKernelFsync(
    int fd
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target file |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid descriptor |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |

## Description

This function synchronizes the file specified with `fd` with the storage (writes out the data written to the file that has been left in the cache to the storage).

## Notes

* `sceKernelSync()` is provided as a function that performs operation equivalent to this function for all file systems.
* When `SCE_KERNEL_O_FSYNC` or `SCE_KERNEL_O_SYNC` is specified to the `flags` argument upon opening a file with `sceKernelOpen()`, a synchronization equivalent to this function will be carried out upon changing the content of the file or directory.

## See Also

`sceKernelSync()`, `sceKernelFdatasync()`

# sceKernelFtruncate

Truncate or expand a file (by specifying a descriptor)

## Definition

```
#include <kernel.h>
int sceKernelFtruncate(
    int fd, 
    off_t length
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target file |
| `length` | File size after the change (bytes) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid descriptor |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `fd` is not a file descriptor open for writing |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Writing is not permitted for the specified file |
| `SCE_KERNEL_ERROR_EFBIG` | 0x8002001b | `length` exceeds the file size limit |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Insufficient free space |

## Description

This function changes the size of the file referenced by `fd` to `length` bytes. If a value smaller than the current file size is specified for `length`, the file will be truncated with the data at the end discarded. Conversely, if a value larger than the current file size is specified for `length`, the end of the file will be expanded.

## Notes

* Even if the file size is changed with this function, the file read/write position will not change.
* `sceKernelTruncate()` is provided as a function that performs operation equivalent to this function but specifies a file pathname.

## See Also

`sceKernelTruncate()`

# sceKernelFutimes

Set a time stamp (by specifying a descriptor)

## Definition

```
#include <kernel.h>
int sceKernelFutimes(
    int fd, 
    const SceKernelTimeval *times
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target file |
| `times` | Time stamp to set (`SceKernelTimeval` array with two elements), or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid descriptor |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Process is not the file's owner, and writing is not permitted (when a time stamp is not specified) |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `times` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The value of microseconds set to `SceKernelTimeval` is less than 0 or greater than 999999 |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Process is not the file's owner (when a time stamp is specified) |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system |

## Description

This function explicitly changes the time stamp of the file referenced by `fd`.

To set the current time for the time stamp, specify NULL for `times`. Both the time of last access and the time the data was last modified will change to the current time when this function is called. In such cases, the process must be the file's owner or writing must be permitted.

To change the time stamp to a time other than the current time, prepare an array with two `SceKernelTimeval` structure elements and specify a pointer to this array for `times`. The time of the last access will change to the value of the first element, and the time the data was last modified will change to the value of the second element. In addition, if the value of the second element is a time before the time when the file was created, the time the file was created will also change to the value of the second element. In such a case, the process must be the file's owner.

In either case, the time of the last file status modification will change to the current time when this function is called.

## Notes

* To change the file creation time and the time the data was last modified to different times, this function must be called twice. Set the time of that the file was created with the first call, and set the (more recent) time that the data was last modified with the second call.
* `sceKernelUtimes()` is provided as a function that performs operation equivalent to this function but specifies a file pathname.
* The current time stamp can be obtained using `sceKernelFstat()` or `sceKernelStat()`.

## See Also

`sceKernelUtimes()`, `sceKernelFstat()`, `sceKernelStat()`

# sceKernelGetdents

Get directory entries

## Definition

```
#include <kernel.h>
int sceKernelGetdents(
    int fd, 
    char *buf, 
    int nbytes
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target directory |
| `buf` | Buffer to store the obtained directory entries |
| `nbytes` | Size of the buffer specified with `buf` (bytes) |

## Return Values

Stores the obtained directory entries in `*buf` and returns the number of bytes written to `*buf` for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid file descriptor open for reading |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `buf` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | File referenced by `fd` is not a directory, or `nbytes` is too small, or the read/write position is invalid |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EWSHOSTBUSY` | 0x8002006e | Unable to respond to a processing request because a file or directory on the host PC is in use |

## Description

This function reads directory entries from the directory specified with `fd`.

The read directory entries are written to the buffer pointed to by `buf` up to `nbytes` as a series of `SceKernelDirent` structures that are not dependent on a file system.

A value equal to or larger than the block size associated with this file must be specified for `nbytes`. The block size can be obtained with `sceKernelFstat()` or `sceKernelStat()` as `st_blksize` in the `SceKernelStat` structure.

The `SceKernelDirent` structures in the buffer may be shortened in alignment to the filename length or be in a sequence with extra space in between. The `d_reclen` member indicates the length of the current directory record in bytes. If another directory record follows it, it will be used as an offset for the `SceKernelDirent` structure. Thus, `d_reclen` will not always match the size of the `SceKernelDirent` structure and can be a smaller/larger value.

The value returned by this function is the number of bytes actually written to the buffer including the spaces in between. If there are no directory entries read when the end of the directory specified with `fd` is reached, this function will return 0. Thus, to read all directory entries from the directory specified with `fd`, specify a buffer of the block size or more and call this function repeatedly until it returns 0.

The `fd` read/write position will be updated to point to the next position of the last read directory entry. It will not always advance to the value returned by the function.

Follow the procedure below to read all directory entries from the directory specified with `fd`.

1. Call this function, and end the read of directory entries if the return value satisfies one of the following conditions. (Proceed to [2](sce-kernel-getdents.html#kernel-reference_15_14__li_rnt_hjt_42c) if none of the conditions are satisfied.)
   * 0 or an error
   * Larger than the specified buffer size (`nbytes`)
2. End the read of directory entries if the read `SceKernelDirent` structure satisfies one of the following conditions. (Proceed to [3](sce-kernel-getdents.html#kernel-reference_15_14__li_ip5_3jt_42c) if none of the conditions are satisfied.)
   * `d_reclen` is less than 8 (the total size of `d_fileno`, `d_reclen`, `d_type`, and `d_namlen`)
   * `d_reclen` exceeds the remaining buffer size
   * `d_namlen` is a positive number and it exceeds (`d_reclen`-9)
3. If the read `SceKernelDirent` structure satisfies one of the following conditions, skip it and return to [2](sce-kernel-getdents.html#kernel-reference_15_14__li_rnt_hjt_42c) to process the next `SceKernelDirent`. (Proceed to [4](sce-kernel-getdents.html#kernel-reference_15_14__li_ubs_mkt_42c) if none of the conditions are satisfied.)
   * `d_fileno` is 0
   * `d_type` is a value other than `SCE_KERNEL_DT_DIR` or `SCE_KERNEL_DT_REG`
4. Process the `SceKernelDirent` structure that passed steps [2](sce-kernel-getdents.html#kernel-reference_15_14__li_rnt_hjt_42c) and [3](sce-kernel-getdents.html#kernel-reference_15_14__li_ip5_3jt_42c) as a valid directory entry. If data remains in the buffer, return to [2](sce-kernel-getdents.html#kernel-reference_15_14__li_rnt_hjt_42c) and process the next `SceKernelDirent`. (Return to [1](sce-kernel-getdents.html#kernel-reference_15_14__li_lhz_wkt_42c) if no data remains.)

## Notes

* It is possible to change the `fd` read/write position using `sceKernelLseek()`, but note that the read/write position after the change must point to a certain directory entry. Specifically, it must be one of the read/write positions directly after this function was called earlier, or 0.
* `sceKernelGetdirentries()` is provided as a function that performs operation equivalent to `sceKernelGetdents()` and returns the directory entry position.

## See Also

`SceKernelDirent`, `sceKernelFstat()`, `sceKernelStat()`, `sceKernelGetdirentries()`

# sceKernelGetdirentries

Get directory entries and the read/write position

## Definition

```
#include <kernel.h>
int sceKernelGetdirentries(
    int fd, 
    char *buf, 
    int nbytes, 
    long *basep
)
```

## Arguments

|  |  |
| --- | --- |
| `fd` | Descriptor of the target directory |
| `buf` | Buffer to store the obtained directory entries |
| `nbytes` | Size of the buffer specified with `buf` (bytes) |
| `basep` | Destination to store the read/write position of the obtained directory entries, or NULL |

## Return Values

Stores the obtained directory entries in `*buf` and the read/write position in `*basep` and returns the number of bytes written to `*buf` for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fd` is not a valid file descriptor open for reading |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `buf` points to invalid memory, or `basep` is not NULL and points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | File referenced by `fd` is not a directory, or `nbytes` is too small, or the read/write position is invalid |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EWSHOSTBUSY` | 0x8002006e | Unable to respond to a processing request because a file or directory on the host PC is in use |

## Description

This function reads directory entries from the directory specified with `fd`.

This function has the same feature as `sceKernelGetdents()` except that it stores the value that points to the start of the read directory entries will be stored in `*basep` (unless NULL is specified to `basep`). Refer to the description of `sceKernelGetdents()`.

## Notes

* It is possible to change the `fd` read/write position using `sceKernelLseek()`, but note that the read/write position after the change must point to a certain directory entry. Specifically, it must be one of the read/write positions directly after `sceKernelGetdirentries()` was called earlier, one of the read/write positions returned to `*basep` when this function was called earlier, or 0.

## See Also

`SceKernelDirent`, `sceKernelFstat()`, `sceKernelStat()`, `sceKernelGetdents()`

# sceKernelLseek

Move the read/write position

## Definition

```
#include <kernel.h>
off_t sceKernelLseek(
    int fildes, 
    off_t offset, 
    int whence
)
```

## Arguments

|  |  |
| --- | --- |
| `fildes` | Descriptor of the target file |
| `offset` | Offset from the base position specified with `whence` |
| `whence` | Base position for the move (see details below) |

## Return Values

For normal termination, returns the read/write position after the move in the number of bytes from the start of the file.

Returns one of the following error codes (a negative value) for an error (without moving the read/write position).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `fildes` is not an already-open file descriptor |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `whence` is invalid, or the calculated read/write position is a negative value |
| `SCE_KERNEL_ERROR_EOVERFLOW` | 0x80020054 | Move destination offset became a value that could not be properly expressed with off\_t |

## Description

This function moves the read/write position of the file specified with `fildes`.

For `whence`, specify the position that will be the base for the move with one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_SEEK_SET` | 0 | File start |
| `SCE_KERNEL_SEEK_CUR` | 1 | Current read/write position |
| `SCE_KERNEL_SEEK_END` | 2 | File end |

The position with the offset specified with `offset` added to the base position specified with `whence` will be the move destination.

It is also possible to move the read/write position to a position beyond the current file end. If writing data to a position beyond the file end, zeros will be read when the gap between the file end and this position is read (if read before data is written to the gap).

Some devices cannot move the read/write position. The read/write position value for files in such devices is undefined.

## Notes

The read/write position directly after a file is opened can be set with flags assigned to `sceKernelOpen()`.

## See Also

`sceKernelOpen()`

# sceKernelMkdir

Create a directory

## Definition

```
#include <kernel.h>
int sceKernelMkdir(
    const char *path, 
    SceKernelMode mode
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the directory to create |
| `mode` | Mode of the directory to create |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error (without creating the directory).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of `path` is not a directory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Path component does not exist |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Searching is not permitted for part of the path, or writing is not permitted for the parent directory of the directory to create |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified directory is in a read-only file system |
| `SCE_KERNEL_ERROR_EMLINK` | 0x8002001f | Limit on the number of subdirectories has been reached |
| `SCE_KERNEL_ERROR_EEXIST` | 0x80020011 | Specified directory already exists |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Insufficient free space |
| No free inodes |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `path` is invalid |

## Description

This function creates the directory specified with `path`. The calling process will become the owner of the directory.

For `mode`, specify one of the following values that indicate the access rights for the directory.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_S_IRU` | 0000555 | Permit read |
| `SCE_KERNEL_S_IRWU` | 0000777 | Permit read and write |

## Notes

Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

# sceKernelOpen

Open a file

## Definition

```
#include <kernel.h>
int sceKernelOpen(
    const char *path,
    int flags,
    SceKernelMode mode
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the target file |
| `flags` | Flags |
| `mode` | Access rights (Only valid when `SCE_KERNEL_O_CREAT` is specified for `flags` and the file specified for `path` does not already exist. For details, refer to this "[Description](sce-kernel-open.html#kernel-reference_15_18__li_uys_3lt_42c)".) |

## Return Values

Returns the descriptor for the opened file (non-negative integer) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of the pathname is not a directory |
| Specified file is not a directory (when `SCE_KERNEL_O_DIRECTORY` is specified) |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | File with the specified name does not exist (when `SCE_KERNEL_O_CREAT` is not specified) |
| Part of a path that should exist does not exist |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the path |
| Reading/writing is not permitted (according to the specified flags) |
| Writing is not permitted (when `SCE_KERNEL_O_TRUNC` is specified) |
| Specified file does not exist, but writing is not permitted for the directory (when `SCE_KERNEL_O_CREAT` is specified) |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | Specified file is a directory (when a flag that modifies a file is specified) |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system (when a flag that modifies a file is specified) |
| Specified file is in a read-only file system (when `SCE_KERNEL_O_CREAT` is specified) |
| `SCE_KERNEL_ERROR_EMFILE` | 0x80020018 | Limit on the number of file descriptors that can be open has been reached |
| `SCE_KERNEL_ERROR_ENFILE` | 0x80020017 | System file table is full |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Specified file does not exist, but empty space or empty inode does not exist (when `SCE_KERNEL_O_CREAT` is specified) |
| Not enough free space in the workspace to store the file or directory |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` points to invalid memory |
| `SCE_KERNEL_ERROR_EEXIST` | 0x80020011 | Specified file exists (when `SCE_KERNEL_O_CREAT` and `SCE_KERNEL_O_EXCL` are specified) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `SCE_KERNEL_O_WRONLY` and `SCE_KERNEL_O_RDWR` are specified at the same time |
| `path` is invalid |
| `SCE_KERNEL_ERROR_ENOBLK` | 0x8002005f | Data block required for opening the specified file does not exist |

Workspace-specific error codes may be returned if you are using a workspace. For details, refer to [Workspaces Overview - Workspaces Overview Appendix A - Workspace Specific Errors](../Workspaces-Overview/workspaces-overview-appendix-a-workspace-specific-errors.html).

## Description

This function opens the file specified with `path` and returns the descriptor. The returned descriptor will be passed to functions that perform processing for files (such as reading/writing) as an argument that specifies the target file.

For `flags`, specify the read/write operation to perform for the opened file with one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_O_RDONLY` | 0x0000 | Open as read-only |
| `SCE_KERNEL_O_WRONLY` | 0x0001 | Open as write-only |
| `SCE_KERNEL_O_RDWR` | 0x0002 | Open for reading and writing |

For `flags`, the following values can also be added by bitwise ORing.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_O_NONBLOCK` | 0x0004 | Perform non-blocking operation |
| `SCE_KERNEL_O_APPEND` | 0x0008 | Write by appending to the end of the file |
| `SCE_KERNEL_O_FSYNC` | 0x0080 | Perform synchronized writing |
| `SCE_KERNEL_O_SYNC` | 0x0080 | Perform synchronized writing |
| `SCE_KERNEL_O_CREAT` | 0x0200 | Create a file (overwrite if it already exists) |
| `SCE_KERNEL_O_TRUNC` | 0x0400 | Truncate the file size to 0 (discard data if it already exists) |
| `SCE_KERNEL_O_EXCL` | 0x0800 | Error will occur if the file to create already exists |
| `SCE_KERNEL_O_DSYNC` | 0x1000 | Perform synchronized writing of the file content (only synchronize metadata if there is a change that directly affects content) |
| `SCE_KERNEL_O_DIRECT` | 0x00010000 | Use cache as little as possible |
| `SCE_KERNEL_O_DIRECTORY` | 0x00020000 | Error will occur if not a directory |

* When `SCE_KERNEL_O_NONBLOCK` is specified, an error will occur immediately if it takes time to open a file for some reason. Operations after a file is opened such as reading/writing will also be non-blocking operations.
* When `SCE_KERNEL_O_APPEND` is specified, writes for the file will all be added to the end of the file (regardless of the read/write position).
* When `SCE_KERNEL_O_FSYNC` or `SCE_KERNEL_O_SYNC` is specified, writes to the file will all be immediately written to storage. In addition, functions that perform write operations will not return until the writing has completed.
* When `SCE_KERNEL_O_DSYNC` is specified, behavior is the same as `SCE_KERNEL_O_FSYNC` or `SCE_KERNEL_O_SYNC` regarding changes made to the file content; however, regarding the file's metadata, write will not be made to storage unless there is a change that is required for reading the file content. The operation is equivalent to `sceKernelFdatasync()`; refer to its description for details.
* When `SCE_KERNEL_O_CREAT` is specified, the file specified with `path` will be newly created. For `mode`, specify the access rights to assign to the file. (Refer to the explanation of `sceKernelChmod()`.) If the specified file exists, it will be overwritten; however, the specified `mode` value will not be reflected. To prevent an overwrite, specify together with `SCE_KERNEL_O_EXCL` to return an error.

  Note that when `SCE_KERNEL_S_INONE` is specified to `mode` upon specifying `SCE_KERNEL_O_CREAT` to `flags`, a file that cannot be read/written will be created. Because `mode` will be ignored as long as `SCE_KERNEL_O_CREAT` is not specified to `flags`, it is not a problem to specify `SCE_KERNEL_S_INONE`.
* When `SCE_KERNEL_O_TRUNC` is specified, if the file already exists the file will be opened after the file length is truncated to 0 (existing content completely discarded).
* When `SCE_KERNEL_O_DIRECT` is specified, the cache will be used as little as possible for reading/writing for the file. If this flag is used inappropriately, performance may decrease greatly.
* When `SCE_KERNEL_O_DIRECTORY` is specified, an error will occur if the specified file is not a directory, and the returned descriptor will be guaranteed to reference the directory.

## Notes

* The number of file descriptors that can be open at one time by a single process is restricted.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`sceKernelClose()`, `sceKernelLseek()`, `sceKernelWrite()`

# sceKernelPread

Read data from the specified file position

## Definition

```
#include <kernel.h>
ssize_t sceKernelPread(
    int d, 
    void *buf, 
    size_t nbytes, 
    off_t offset
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `buf` | Buffer to store the read data |
| `nbytes` | Size of the data to read (bytes) |
| `offset` | Position of the data to read (number of bytes from the file start) |

## Return Values

For normal termination, stores the read data in the buffer specified with `buf` and returns the actual number of bytes read.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor for reading |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `buf` points to invalid memory |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Data that can be immediately read does not exist (when a non-blocking file) |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | Data is in a file system where directory reads are not permitted (when a directory) |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | Specified file is a file type where reads are not permitted with its file system |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `nbytes` is greater than `INT_MAX` |
| `offset` is a negative number |
| `SCE_KERNEL_ERROR_EWSMIRROR` | 0x80020068 | Failed to mirror a workspace |
| `SCE_KERNEL_ERROR_ESTALE` | 0x80020046 | The specified file on the host PC has been updated or deleted |

## Description

This function reads data from the specified file position. The data after the position in `offset` bytes up to `nbytes` bytes from the start of the file specified with `d` will be read and stored in the buffer specified with `buf`. The read/write position pointer for the file will not move.

The value returned by this function is the number of bytes that was actually read and stored in the buffer. If it is a regular file and there is a sufficient volume of data left until the end of the file, data in the number of bytes specified will always be read, but in other cases data smaller than specified may be read, and a value smaller than the specified size may return. In particular, when the position specified with `offset` is the file end or thereafter, 0 will be returned.

## Notes

`sceKernelRead()` is provided as a function that reads data pointed to by the read/write position pointer. In addition, `sceKernelPreadv()` is provided as a function that partitions and stores the read data.

## See Also

`sceKernelRead()`, `sceKernelPreadv()`

# sceKernelPreadv

Read and partition data from the specified file position

## Definition

```
#include <kernel.h>
ssize_t sceKernelPreadv(
    int d, 
    const SceKernelIovec *iov, 
    int iovcnt, 
    off_t offset
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `iov` | Array to specify the destination to store the read data |
| `iovcnt` | Number of `iov` elements |
| `offset` | Position of the data to read (number of bytes from the file start) |

## Return Values

For normal termination, stores the read data in the buffers specified with each `iov` element and returns the actual number of bytes read.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor for reading |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Data that can be immediately read does not exist (when a non-blocking file) |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | Data is in a file system where directory reads are not permitted (when a directory) |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | Specified file is a file type where reads are not permitted with its file system |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `iovcnt` is a negative number, or is greater than `SCE_KERNEL_IOV_MAX` |
| `iov_len` for one of the elements in the `iov` array is a negative number |
| The total `iov_len` of each element in the `iov` array will overflow a 32-bit integer |
| `offset` is a negative number |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `iov_base` for one of the elements in `iov` points to invalid memory |
| `SCE_KERNEL_ERROR_EWSMIRROR` | 0x80020068 | Failed to mirror a workspace |
| `SCE_KERNEL_ERROR_ESTALE` | 0x80020046 | The specified file on the host PC has been updated or deleted |

## Description

This function reads data from the specified file position, partitions/stores the data in multiple buffers. The data after the position in `offset` bytes from the start of the file specified with `d` will be read according to the size specified with each element (`iov[0]`, `iov[1]`, ..., `iov[iovcnt-1]`) in the array specified with `iov` and stored in the buffers specified with each element. The read/write position pointer for the file will not move.

The value returned by this function is the total number of bytes that was actually read and stored in the buffers. If it is a regular file and there is a sufficient volume of data left until the end of the file, data in the number of bytes specified will always be read, but in other cases data smaller than specified may be read, and a value smaller than the specified size may return. In particular, when the position specified with `offset` is the file end or thereafter, 0 will be returned.

## Notes

`sceKernelReadv()` is provided as a function that reads and partitions data pointed to by the read/write position pointer. In addition, `sceKernelPread()` is provided as a function that stores the read data in a single buffer.

## See Also

`sceKernelReadv()`, `sceKernelPread()`

# sceKernelPwrite

Write data to the specified file position

## Definition

```
#include <kernel.h>
ssize_t sceKernelPwrite(
    int d, 
    const void *buf, 
    size_t nbytes, 
    off_t offset
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `buf` | Buffer that stores the data to write |
| `nbytes` | Size of the data to write (bytes) |
| `offset` | Position where the data will be written (number of bytes from the file start) |

## Return Values

Returns the number of bytes written to the file (=`nbytes`) for normal termination.

Returns one of the following error codes (a negative value) for an error (without changing the file content and read/write position).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor open for writing |
| `SCE_KERNEL_ERROR_EFBIG` | 0x8002001b | A write that exceeds the file size limit was attempted |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | The address of the data to write points to invalid memory |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | No empty areas remain in the file system |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | An immediate write could not be performed (if a non-blocking file) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The read/write position of `d` is a negative number |
| `nbytes` is greater than `INT_MAX` |
| `offset` is a negative number |

## Description

This function writes data to a file. The data specified with `buf` and `nbytes` will be written after the position in `offset` bytes from the start of the file specified with `d`. The read/write position will not change.

## Notes

`sceKernelPwritev()` is provided as a function that writes data partitioned to multiple buffers to the specified file position. In addition, `sceKernelWrite()` is provided as a function that writes data to the file's current read/write position.

## See Also

`sceKernelPwritev()`, `sceKernelWrite()`

# sceKernelPwritev

Write partitioned data to the specified file position

## Definition

```
#include <kernel.h>
ssize_t sceKernelPwritev(
    int d, 
    const SceKernelIovec *iov, 
    int iovcnt, 
    off_t offset
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `iov` | Array to specify the address and size of each partitioned data |
| `iovcnt` | Number of `iov` array elements |
| `offset` | Position where the data will be written (number of bytes from the file start) |

## Return Values

Returns the number of bytes written for normal termination.

Returns one of the following error codes (a negative value) for an error (without changing the file content).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor open for writing |
| `SCE_KERNEL_ERROR_EFBIG` | 0x8002001b | A write that exceeds the file size limit was attempted |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | The `iov` array or the data address points to invalid memory |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | No empty areas remain in the file system |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | An immediate write could not be performed (if a non-blocking file) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The read/write position of `d` is a negative number |
| `iovcnt` is a negative number, or is greater than `SCE_KERNEL_IOV_MAX` |
| `iov_len` for one of the elements in the `iov` array is a negative number |
| The total `iov_len` of each element in the `iov` array will overflow a 32-bit integer |
| `offset` is a negative number |

## Description

This function writes data to a file. Data will be written at the position in `offset` bytes from the start of the file specified with `d` in order according to the address and size specified with each `iov` array element (`iov[0]`, `iov[1]`, ..., `iov[iovcnt-1]`). The file's read/write position will not change.

## Notes

`sceKernelPwrite()` is provided as a function that writes data in a single buffer to the specified file position. In addition, `sceKernelWritev()` is provided as a function that writes partitioned data to the file's current read/write position.

## See Also

`sceKernelPwrite()`, `sceKernelWritev()`

# sceKernelRead

Read data from a file

## Definition

```
#include <kernel.h>
ssize_t sceKernelRead(
    int d, 
    void *buf, 
    size_t nbytes
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `buf` | Buffer to store the read data |
| `nbytes` | Size of the data to read (bytes) |

## Return Values

For normal termination, stores the read data in the buffer specified with `buf` and returns the actual number of bytes read.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor for reading |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `buf` points to invalid memory |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Data that can be immediately read does not exist (when a non-blocking file) |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | Data is in a file system where directory reads are not permitted (when a directory) |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | Specified file is a file type where reads are not permitted with its file system |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The read/write position of `d` is a negative number |
| `nbytes` is greater than `INT_MAX` |
| `SCE_KERNEL_ERROR_EWSMIRROR` | 0x80020068 | Failed to mirror a workspace |
| `SCE_KERNEL_ERROR_ESTALE` | 0x80020046 | The specified file on the host PC has been updated or deleted |

## Description

This function reads data from the specified file position. The data up to `nbytes` bytes will be read from the file specified with `d` and stored in the buffer specified with `buf`.

With seekable files, reading will start from the current read/write position for `d`. When this function returns, the read/write position will have advanced for the actual number of read bytes.

With non-seekable files, reading will always be performed from the current position. (The read/write position is not defined for such files.)

The value returned by this function is the number of bytes that was actually read and stored in the buffer. If it is a regular file and there is a sufficient volume of data left until the end of the file, data in the number of bytes specified will always be read, but in other cases data smaller than specified may be read, and a value smaller than the specified size may return. In particular, when the read/write position at the time of the function call is the file end or thereafter, 0 will be returned.

## Notes

`sceKernelPread()` is provided as a function that reads data at the specified position. In addition, `sceKernelReadv()` is provided as a function that partitions and stores the read data.

## See Also

`sceKernelPread()`, `sceKernelReadv()`

# sceKernelReadv

Read and partition data from a file

## Definition

```
#include <kernel.h>
ssize_t sceKernelReadv(
    int d, 
    const SceKernelIovec *iov, 
    int iovcnt
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `iov` | Array to specify the destination to store the read data |
| `iovcnt` | Number of `iov` elements |

## Return Values

For normal termination, stores the read data in the buffers specified with each `iov` element and returns the actual number of bytes read.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor for reading |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Data that can be immediately read does not exist (when a non-blocking file) |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | Data is in a file system where directory reads are not permitted (when a directory) |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | Specified file is a file type where reads are not permitted with its file system |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The read/write position of `d` is a negative number |
| `iovcnt` is a negative number, or is greater than `SCE_KERNEL_IOV_MAX` |
| `iov_len` for one of the elements in the `iov` array is a negative number |
| The total `iov_len` of each element in the `iov` array will overflow a 32-bit integer |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `iov_base` for one of the elements in `iov` points to invalid memory |
| `SCE_KERNEL_ERROR_EWSMIRROR` | 0x80020068 | Failed to mirror a workspace |
| `SCE_KERNEL_ERROR_ESTALE` | 0x80020046 | The specified file on the host PC has been updated or deleted |

## Description

This function reads data from a file and partitions/stores the data in multiple buffers. The data after the read/write position of the file specified with `d` will be read according to the size specified with each element (`iov[0]`, `iov[1]`, ..., `iov[iovcnt-1]`) in the array specified with `iov` and stored in the buffers specified with each element. The read/write position will advance for the number of bytes read.

With seekable files, reading will start from the current read/write position for `d`. When this function returns, the read/write position will have advanced for the actual number of read bytes.

With non-seekable files, reading will always be performed from the current position. (The read/write position is not defined for such files.)

The value returned by this function is the total number of bytes that was actually read and stored in the buffers. If it is a regular file and there is a sufficient volume of data left until the end of the file, data in the number of bytes specified will always be read, but in other cases data smaller than specified may be read, and a value smaller than the specified size may return. In particular, when the read/write position at the time of the function call is the file end or thereafter, 0 will be returned.

## Notes

`sceKernelRead()` is provided as a function that stores the read data in a single buffer. In addition, `sceKernelPreadv()` is provided as a function that reads and partitions data from the specified position rather than the read/write position.

## See Also

`sceKernelRead()`, `sceKernelPreadv()`

# sceKernelRename

Change a filename or move a file

## Definition

```
#include <kernel.h>
int sceKernelRename(
    const char *from, 
    const char *to
)
```

## Arguments

|  |  |
| --- | --- |
| `from` | Pathname before the change |
| `to` | Pathname after the change |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error (without changing either file).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Part of the `from` path does not exist or the directory above `to` does not exist |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the path |
| Writing is not permitted |
| Writing to the `from` directory is not permitted (when moving a directory to another parent directory) |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of the pathname is not a directory |
| `from` is a directory but `to` is not a directory |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | `to` is a directory but `from` is not a directory |
| `SCE_KERNEL_ERROR_EXDEV` | 0x80020012 | `to` and `from` are in separate file systems |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Insufficient free space |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | `from` or `to` is in a read-only file system |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `from` or `to` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `from` is the parent directory of `to` (when moving a directory to another parent directory) |
| `from` or `to` is "." or ".." |
| `from` or `to` is invalid |
| `SCE_KERNEL_ERROR_ENOTEMPTY` | 0x80020042 | `to` is not empty (when `to` is a directory) |

## Description

This function changes the name of a file or directory or moves a file or directory to another directory.

For `from`, specify the pathname of the current file/directory. For `to`, specify the pathname after the change. `from` and `to` must be the same file type. (Both must be regular files, or both must be directories.) In addition, they must exist in the same file system.

If the file/directory specified with `to` already exists, it will be deleted. In such cases, even if the system crashes during processing, the file/directory specified with `to` will not disappear.

## Notes

Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

# sceKernelRmdir

Delete a directory

## Definition

```
#include <kernel.h>
int sceKernelRmdir(
    const char *path
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the directory to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error (without deleting the directory).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of the path is not a directory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Specified directory does not exist |
| `SCE_KERNEL_ERROR_ENOTEMPTY` | 0x80020042 | Specified directory is not empty (has a file other than "." or "..") |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the path |
| Writes are not permitted for the parent directory of the specified directory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The last part of the path is "." or ".." |
| `path` is invalid |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | A file system is mounted to the specified directory |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified directory is in a read-only file system |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` points to invalid memory |

## Description

This function deletes the directory specified with `path`.

The directory cannot be deleted when it contains entries other than "." or "..".

## Notes

* To delete a regular file, use `sceKernelUnlink()`.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`sceKernelUnlink()`

# sceKernelStat

Get file status (by specifying a path)

## Definition

```
#include <kernel.h>
int sceKernelStat(
    const char *path, 
    SceKernelStat *sb
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the target file |
| `sb` | Destination to store the obtained file status |

## Return Values

Stores the obtained file status in `*sb` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of `path` |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `sb` or `path` points to an invalid address |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Specified file does not exist |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of `path` is not a directory |
| `SCE_KERNEL_ERROR_EOVERFLOW` | 0x80020054 | File size (bytes) overflowed |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `path` is invalid |
| `SCE_KERNEL_ERROR_EWSHOSTBUSY` | 0x8002006e | Unable to respond to a processing request because a file or directory on the host PC is in use |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Not enough free space in the workspace to store the file or directory |
| `SCE_KERNEL_ERROR_EWSMIRROR` | 0x80020068 | Failed to mirror a workspace |

## Description

This function obtains various information about the file specified with `path`. For details on the information that can be obtained, refer to the `SceKernelStat` structure.

## Notes

* There will be no problems if reading/writing is not permitted for the file specified with `path`. However, all of the directories included in the pathname must be searchable.
* `sceKernelFstat()` is provided as a function that performs operation equivalent to this function but with a file descriptor that is already open specified.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`SceKernelStat`, `sceKernelFstat()`

# sceKernelSync

Synchronize files and storage

## Definition

```
#include <kernel.h>
void sceKernelSync(void)
```

## Arguments

None

## Return Values

None

## Description

This function synchronizes all files with the storage (writes out the data written to the file that has been left in the cache to the storage).

## Notes

`sceKernelFsync()` is provided as a function that synchronizes a single file with storage.

## See Also

`sceKernelFsync()`

# sceKernelTruncate

Truncate or expand a file (by specifying a path)

## Definition

```
#include <kernel.h>
int sceKernelTruncate(
    const char *path, 
    off_t length
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the target file |
| `length` | File size after the change (bytes) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of the pathname is not a directory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Specified file does not exist |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the specified path |
| Writing is not permitted for the specified file |
| `SCE_KERNEL_ERROR_EISDIR` | 0x80020015 | Specified file is a directory |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system |
| `SCE_KERNEL_ERROR_EFBIG` | 0x8002001b | `length` exceeds the file size limit |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `length` is less than 0 |
| `path` is invalid |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` points to invalid memory |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | Insufficient free space |

## Description

This function changes the size of the file specified with `path` to `length` bytes.

If a value smaller than the current file size is specified for `length`, the file will be truncated with the data at the end discarded. Conversely, if a value larger than the current file size is specified for `length`, the file will be expanded.

## Notes

* If the specified file is not a directory or a regular file, this function will terminate normally without doing anything.
* `sceKernelFtruncate()` is provided as a function that performs operation equivalent to this function but with a file descriptor that is already open specified.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`sceKernelFtruncate()`

# sceKernelUnlink

Delete a file

## Definition

```
#include <kernel.h>
int sceKernelUnlink(
    const char *path
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the file to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of the path is not a directory |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Specified file does not exist |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the path |
| Writes are not permitted for the directory where the specified file exists |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Deleting is not permitted for the directory |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `path` is invalid |

## Description

This function deletes the file specified with `path`. If the file is not open, all of the resources allocated to the file will be released. If it is open, the resources will be released when it is closed.

## Notes

* Directories cannot be deleted with this function. (There are cases where the `SCE_KERNEL_ERROR_EISDIR` error occurs and cases where the `SCE_KERNEL_ERROR_EPERM` error occurs.) To delete a directory, use `sceKernelRmdir()`.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`sceKernelRmdir()`

# sceKernelUtimes

Set a time stamp (by specifying a path)

## Definition

```
#include <kernel.h>
int sceKernelUtimes(
    const char *path, 
    const SceKernelTimeval *times
)
```

## Arguments

|  |  |
| --- | --- |
| `path` | Pathname of the target file |
| `times` | Time stamp to set (`SceKernelTimeval` array with two elements), or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Search is not permitted for part of the path |
| Process is not the file's owner, and writing is not permitted (when a time stamp is not specified) |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `path` or `times` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `path` is invalid |
| The value of microseconds set to `SceKernelTimeval` is less than 0 or greater than 999999 |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | The length of the directory name or filename in the file path exceeds `SCE_KERNEL_NAME_MAX`, or the length of the entire pathname including the null character is greater than `SCE_KERNEL_PATH_MAX` |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Specified file does not exist |
| `SCE_KERNEL_ERROR_ENOTDIR` | 0x80020014 | Part of `path` is not a directory |
| `SCE_KERNEL_ERROR_EPERM` | 0x80020001 | Process is not the file's owner (when a time stamp is specified) |
| `SCE_KERNEL_ERROR_EROFS` | 0x8002001e | Specified file is in a read-only file system |

## Description

This function explicitly changes the time stamp of the file specified with `path`.

To set the current time for the time stamp, specify NULL for `times`. Both the time of last access and the time the data was last modified will change to the current time when this function is called. In such cases, the process must be the file's owner or writing must be permitted.

To change the time stamp to a time other than the current time, prepare an array with two `SceKernelTimeval` structure elements and specify a pointer to this array for `times`. The time of the last access will change to the value of the first element, and the time the data was last modified will change to the value of the second element. In addition, if the value of the second element is a time before the time when the file was created, the time the file was created will also change to the value of the second element. In such a case, the process must be the file's owner.

In either case, the time of the last file status modification will change to the current time when this function is called.

## Notes

* To change the file creation time and the time the data was last modified to different times, this function must be called twice. Set the time of that the file was created with the first call, and set the (more recent) time that the data was last modified with the second call.
* `sceKernelFutimes()` is provided as a function performs operation equivalent to this function but with a file descriptor that is already open specified.
* The current time stamp can be obtained using `sceKernelStat()` or `sceKernelFstat()`.
* Only an absolute path can be used in PlayStation®5 kernel functions. A relative path is not supported.

## See Also

`sceKernelFutimes()`, `sceKernelStat()`, `sceKernelFstat()`

# sceKernelWrite

Write data to a file

## Definition

```
#include <kernel.h>
ssize_t sceKernelWrite(
    int d, 
    const void *buf, 
    size_t nbytes
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `buf` | Buffer that stores the data to write |
| `nbytes` | Size of the data to write (bytes) |

## Return Values

Returns the number of bytes written to the file (=`nbytes`) for normal termination.

Returns one of the following error codes (a negative value) for an error (without changing the file content and read/write position).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor open for writing |
| `SCE_KERNEL_ERROR_EFBIG` | 0x8002001b | A write that exceeds the file size limit was attempted |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | The buffer address points to invalid memory |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | No empty areas remain in the file system |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | An immediate write could not be performed (if a non-blocking file) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The read/write position of `d` is a negative number |
| `nbytes` is greater than `INT_MAX` |

## Description

This function writes data to a file. The data specified with `buf` and `nbytes` will be written to the file specified with `d`.

If the specified file is seekable, the data will be written at the current read/write position. When this function returns, the read/write position will have advanced for the number of written bytes.

With non-seekable files, writing will always be performed to the current position. (The read/write position is not defined for such files.)

## Notes

`sceKernelWritev()` is provided as a function that writes data partitioned to multiple buffers. In addition, `sceKernelPwrite()` is provided as a function that writes data to the specified file position.

## See Also

`sceKernelWritev()`, `sceKernelPwrite()`

# sceKernelWritev

Write partitioned data to a file

## Definition

```
#include <kernel.h>
ssize_t sceKernelWritev(
    int d, 
    const SceKernelIovec *iov, 
    int iovcnt
)
```

## Arguments

|  |  |
| --- | --- |
| `d` | Descriptor of the target file |
| `iov` | Array to specify the address and size of each partitioned data |
| `iovcnt` | Number of `iov` array elements |

## Return Values

Returns the number of bytes written to the file for normal termination.

Returns one of the following error codes (a negative value) for an error (without changing the file content and read/write position).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBADF` | 0x80020009 | `d` is not a valid file descriptor open for writing |
| `SCE_KERNEL_ERROR_EFBIG` | 0x8002001b | A write that exceeds the file size limit was attempted |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | The `iov` array or the data address points to invalid memory |
| `SCE_KERNEL_ERROR_ENOSPC` | 0x8002001c | No empty areas remain in the file system |
| `SCE_KERNEL_ERROR_EIO` | 0x80020005 | I/O error occurred |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | An immediate write could not be performed (if a non-blocking file) |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | The read/write position of `d` is a negative number |
| `iovcnt` is a negative number, or is greater than `SCE_KERNEL_IOV_MAX` |
| `iov_len` for one of the elements in the `iov` array is a negative number |
| The total `iov_len` of each element in the `iov` array will overflow a 32-bit integer |

## Description

This function writes data to a file. Data will be written to the file specified with `d` in order according to the address and size specified with each `iov` array element (`iov[0]`, `iov[1]`, ..., `iov[iovcnt-1]`).

If the specified file is seekable, the data will be written at the current read/write position. When this function returns, the read/write position will have advanced for the number of written bytes.

With non-seekable files, writing will always be performed to the current position. (The read/write position is not defined for such files.)

## Notes

`sceKernelWrite()` is provided as a function that writes data in a single buffer to a file. In addition, `sceKernelPwrite()` is provided as a function that writes data to the specified file position.

## See Also

`sceKernelWrite()`, `sceKernelPwrite()`

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.