# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-map-direct-memory.html

# Memory Management

# SCE\_KERNEL\_MAIN\_DMEM\_SIZE

Size of direct memory

## Definition

```
#include <kernel.h>
#define SCE_KERNEL_MAIN_DMEM_SIZE (sceKernelGetDirectMemorySize())
```

## Description

This macro definition represents the size of direct memory. This macro is equivalent to calling `sceKernelGetDirectMemorySize()`.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# SCE\_KERNEL\_PAGE\_SIZE

Logical page size

## Definition

```
#include <kernel.h>
#define SCE_KERNEL_PAGE_SIZE 16384
```

## Description

This macro definition represents the number of bytes in a logical page.

# SceKernelBatchMapEntry

Mapping information to specify when batch performing mapping/unmapping/protection changing/memory type changing on multiple areas

## Definition

```
#include <kernel.h>
typedef struct {
    void *start;
    off_t offset;
    size_t length;
    char protection;
    char type;
    short pad1;
    int operation;
} SceKernelBatchMapEntry;
```

## Members

|  |  |
| --- | --- |
| `start` | Start virtual address of the operation target area |
| `offset` | Start physical address of the direct memory to map |
| `length` | Size of the operation target area (bytes) |
| `protection` | Memory protection to set for the operation target area (see details below) |
| `type` | Memory type to set for the operation target area |
| `operation` | Operation to perform (see details below) |

## Description

This structure indicates a mapping/unmapping/protection changing/memory type changing operation. By assigning an array of instances of this structure to the argument `entries` of `sceKernelBatchMap()`/`sceKernelBatchMap2()`, batch mapping/unmapping/protection changing/memory type changing can be performed on multiple areas.

For `operation`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MAP_OP_MAP_DIRECT` | 0 | Map a direct memory area |
| `SCE_KERNEL_MAP_OP_UNMAP` | 1 | Unmap a virtual address space area |
| `SCE_KERNEL_MAP_OP_PROTECT` | 2 | Change protection for a virtual address space area |
| `SCE_KERNEL_MAP_OP_TYPE_PROTECT` | 4 | Change protection and memory type for a direct memory area. |

* `SCE_KERNEL_MAP_OP_MAP_DIRECT` indicates an operation where a direct memory area starting from `offset` and of the size `length` bytes is mapped to the virtual address `start`, and `protection` is set for the protection. The `type` value is ignored.
* `SCE_KERNEL_MAP_OP_UNMAP` indicates an operation where the virtual address space area (`start`, `start`+`length`) is unmapped. The `protection`, `offset`, and `type` values are ignored.
* `SCE_KERNEL_MAP_OP_PROTECT` indicates an operation where the protection for the virtual address space area (`start`, `start`+`length`) will be changed to `protection`. The `offset` and `type` values are ignored.
* `SCE_KERNEL_MAP_OP_TYPE_PROTECT` indicates an operation where the protection for the virtual address space area (`start`, `start`+`length`) will be changed to `protection` and the memory type of the direct memory mapped to that area will be changed to `type`. The `offset` value is ignored.

When setting `protection`, specify the bitwise OR of the following values. Note that you cannot specify a protection that permits access from the ACP.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |
| `SCE_KERNEL_PROT_AMPR_READ` | 0x40 | Permit reads from the AMPR |
| `SCE_KERNEL_PROT_AMPR_WRITE` | 0x80 | Permit writes from the AMPR |
| `SCE_KERNEL_PROT_AMPR_RW` | 0xc0 | Permit writes and reads from the AMPR |

When setting `type`, specify one of the enum constants defined with `SceKernelMemoryType`.

Note the following points when performing an `SCE_KERNEL_MAP_OP_PROTECT` or `SCE_KERNEL_MAP_OP_TYPE_PROTECT` operation using this structure.

* The area that is specified in an `SCE_KERNEL_MAP_OP_PROTECT` or `SCE_KERNEL_MAP_OP_TYPE_PROTECT` operation must be aligned to a 16 KiB boundary if it is a memory area that is not designated for pooled memory. If it is a pooled memory designated area, it must be aligned to a 64 KiB boundary. The error `SCE_KERNEL_ERROR_EINVAL` is returned if these restrictions are violated.
* Even if you specify a protection that would permit access from the AMPR while performing an `SCE_KERNEL_MAP_OP_PROTECT` or `SCE_KERNEL_MAP_OP_TYPE_PROTECT` operation on a pooled memory designated area, doing so will not enable access from the AMPR.

## Notes

It is not possible to modify protections, change memory types, or perform unmapping for areas mapped with the AMPR library.

# SceKernelDirectMemoryQueryInfo

Information about the allocated direct memory area

## Definition

```
#include <kernel.h>
typedef struct {
    off_t start;
    off_t end;
    int memoryType;
} SceKernelDirectMemoryQueryInfo;
```

## Members

|  |  |
| --- | --- |
| `start` | Start physical address of the area |
| `end` | End physical address of the area (this address is not included in the area) |
| `memoryType` | Memory type |

## Description

This structure is used for obtaining information about the directory memory area existing at the specified physical address with `sceKernelDirectMemoryQuery()`.

## See Also

`sceKernelDirectMemoryQuery()`, `SceKernelMemoryType`

# SceKernelMemoryType

Memory type of direct memory

## Definition

```
#include <kernel.h>
typedef enum {
    (omitted: see below)
} SceKernelMemoryType;
```

## Description

This constant represents the cache operation mode. One of the following memory types can be specified for the main memory.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
|  | 0 | Same operation as `SCE_KERNEL_MTYPE_C_SHARED` |
| `SCE_KERNEL_MTYPE_C` | 11 | CPU: write-back mode  GPU GL2 MTYPE: cached, R/W, not shared |
| `SCE_KERNEL_MTYPE_C_SHARED` | 12 | CPU: write-back mode  GPU GL2 MTYPE: cached, R/W, shared |

## Notes

* The use of `SCE_KERNEL_MTYPE_C_SHARED` is recommended.
* The memory type for each segment of executable files and of PRX files is fixed at 0.

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`, `sceKernelMapDirectMemory2()`, `sceKernelMtypeprotect()`, `SceKernelBatchMapEntry`, `sceKernelMemoryPoolCommit()`, `SceKernelMemoryPoolBatchEntry`

# SceKernelMemoryPoolBatchEntry

Information to specify when batch performing committing/de-committing/protection changing/memory type changing/moving on a pooled memory designated area

## Definition

```
#include <kernel.h>
typedef struct {
    unsigned op;
    unsigned flags;
    union {
        struct {
            void *addr;
            size_t len;
            unsigned char prot;
            unsigned char type;
        } commit;
        struct {
            void *addr;
            size_t len;
        } decommit;
        struct {
            void *addr;
            size_t len;
            unsigned char prot;
        } protect;
        struct {
            void *addr;
            size_t len;
            unsigned char prot;
            unsigned char type;
        } typeProtect;
        struct {
            void *dst;
            void *src;
            size_t len;
        } move;
        uintptr_t padding[3];
    };
} SceKernelMemoryPoolBatchEntry;
```

## Members

|  |  |
| --- | --- |
| `op` | Operation to perform (see details below) |
| `flags` | Reserved (specify 0) |
| `commit.addr` | Start virtual address of the commit destination area (aligned to 64 KiB) |
| `commit.len` | Size of memory to commit (bytes, multiple of 64 KiB) |
| `commit.prot` | Memory protection to set for the memory to commit (see details below) |
| `commit.type` | Memory type to set for the memory to commit (see details below) |
| `decommit.addr` | Start virtual address of the area to de-commit (aligned to 64 KiB) |
| `decommit.len` | Size of the area to de-commit (bytes, multiple of 64 KiB) |
| `protect.addr` | Start virtual address of the area to change protection (aligned to 64 KiB) |
| `protect.len` | Size of the area to change protection (bytes, multiple of 64 KiB) |
| `protect.prot` | Memory protection to set (see details below) |
| `typeProtect.addr` | Start virtual address of the area to change protection and memory type (aligned to 64 KiB) |
| `typeProtect.len` | Size of the area to change protection and memory type (bytes, multiple of 64 KiB) |
| `typeProtect.prot` | Memory protection to set (see details below) |
| `typeProtect.type` | Memory type to set (see details below) |
| `move.dst` | Start virtual address of the move destination area (aligned to 64 KiB) |
| `move.src` | Start virtual address of the move source area (aligned to 64 KiB) |
| `move.len` | Size of memory to move (bytes, multiple of 64 KiB) |

## Description

This structure indicates a committing/de-committing/protection changing/memory type changing/moving operation. By assigning an array of instances of this structure to the argument `entries` of `sceKernelMemoryPoolBatch()`, multiple operations can be performed as a batch on one pooled memory designated area.

For `op`, specify one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MEMORY_POOL_OP_COMMIT` | 1 | Commit |
| `SCE_KERNEL_MEMORY_POOL_OP_DECOMMIT` | 2 | De-commit |
| `SCE_KERNEL_MEMORY_POOL_OP_PROTECT` | 3 | Change protection |
| `SCE_KERNEL_MEMORY_POOL_OP_TYPE_PROTECT` | 4 | Change protection and memory type |
| `SCE_KERNEL_MEMORY_POOL_OP_MOVE` | 5 | Move |

* `SCE_KERNEL_MEMORY_POOL_OP_COMMIT` indicates an operation where a memory range of size `commit.len` bytes starting from the virtual address `commit.addr` within the pooled memory designated area is committed - in other words, unused physical memory (pooled memory) is allocated from the memory pool and placed onto the virtual address space - with `commit.prot` set for the protection and `commit.type` set for the memory type.
* `SCE_KERNEL_MEMORY_POOL_OP_DECOMMIT` indicates an operation where a memory range of size `decommit.len` bytes starting from the virtual address `decommit.addr` within the pooled memory designated area is de-committed - in other words, physical memory (pooled memory) placed onto the virtual address space is removed and returned to the memory pool.
* `SCE_KERNEL_MEMORY_POOL_OP_PROTECT` indicates an operation where the protection of a memory range of size `protect.len` bytes starting from the virtual address `protect.addr` within the pooled memory designated area is changed to `protect.prot`.
* `SCE_KERNEL_MEMORY_POOL_OP_TYPE_PROTECT` indicates an operation where the protection and memory type of a memory range of size `typeProtect.len` bytes starting from the virtual address `typeProtect.addr` within the pooled memory designated area is changed to `typeProtect.prot` and `typeProtect.type`, respectively.
* `SCE_KERNEL_MEMORY_POOL_OP_MOVE` indicates an operation where the physical memory (pooled memory) placed on an area of size `move.len` bytes starting from the virtual address `move.src` within the pooled memory designated area is moved to an area starting from the virtual address `move.dst`.

When setting `commit.prot`/`protect.prot`/`typeProtect.prot`, specify the bitwise OR of the following values, or 0 (= do not permit accesses from the CPU or GPU). Note that you cannot specify a protection that permits access from the AMPR or ACP.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |

When setting `commit.type`/`typeProtect.type`, specify one of the enum constants defined with `SceKernelMemoryType`.

## See Also

`sceKernelMemoryPoolBatch()`

# SceKernelMemoryPoolBlockStats

Pooled memory usage

## Definition

```
#include <kernel.h>
typedef struct {
    int availableFlushedBlocks;
    int availableCachedBlocks;
    int allocatedFlushedBlocks;
    int allocatedCachedBlocks;
} SceKernelMemoryPoolBlockStats;
```

## Members

|  |  |
| --- | --- |
| `availableFlushedBlocks` | Number of free blocks that have never been allocated since being added to the memory pool |
| `availableCachedBlocks` | Number of free blocks that can be allocated from the memory pool, which had the memory type 0 specified upon being last committed |
| allocatedFlushedBlocks | Always 0 |
| `allocatedCachedBlocks` | Number of blocks allocated from the memory pool and committed to the pooled memory designated area with the memory type 0 specified |

## Description

This structure is used for obtaining information about the usage of pooled memory blocks (in other words, physical memory blocks managed by the memory pool) with `sceKernelMemoryPoolGetBlockStats()`.

## See Also

`sceKernelMemoryPoolGetBlockStats()`, `sceKernelMemoryPoolExpand()`, `sceKernelMemoryPoolCommit()`

# SceKernelVirtualQueryInfo

Information about the memory area mapped to a virtual address

## Definition

```
#include <kernel.h>
typedef struct {
    void *start;
    void *end;
    off_t offset;
    int protection;
    int memoryType;
    unsigned isFlexibleMemory:1;
    unsigned isDirectMemory:1;
    unsigned isStack:1;
    unsigned isPooledMemory:1;
    unsigned isCommitted:1;
    unsigned isGpuPrt:1;
    unsigned ammUsage:1;
    char name[32];
    uint8_t gpuMaskId;
} SceKernelVirtualQueryInfo;
```

## Members

|  |  |
| --- | --- |
| `start` | Start virtual address of the area |
| `end` | End virtual address of the area (this address is not included in the area) |
| `offset` | The physical address corresponding to the virtual address `start` if direct memory is mapped |
| `protection` | Memory protection set for the specified area |
| `memoryType` | Memory type |
| `isFlexibleMemory` | 1 if flexible memory is mapped, 0 otherwise |
| `isDirectMemory` | 1 if direct memory is mapped, 0 otherwise |
| `isStack` | 1 if the area is a stack area automatically mapped by the system, 0 otherwise |
| `isPooledMemory` | 1 if the area is a pooled memory designated area, 0 otherwise |
| `isCommitted` | 1 if physical memory is mapped/committed, 0 otherwise |
| `isGpuPrt` | In the case of an area mapped with `sce::Ampr::AmmCommandBuffer::mapAsPrt()` from the AMM library, 1; otherwise, 0 (even if the area was not mapped using the AMM library) |
| `ammUsage` | If physical memory allocated with `sce::Ampr::Amm::Usage::kAuto` is being used by an area mapped with the AMM library, 1; if physical memory allocated with `sce::Ampr::Amm::Usage::kDirect` is being used, 0 (even if the area was not mapped using the AMM library) |
| `name` | Name of memory set with `sceKernelSetVirtualRangeName()` |
| `gpuMaskId` | GPU mask ID of the area mapped with the AMM library (If it is not an area mapped with the AMM library, then 0) |

## Description

This structure is used for obtaining information about the memory area mapped to the specified virtual address with `sceKernelVirtualQuery()`.

## See Also

`sceKernelVirtualQuery()`, `SceKernelMemoryType`

# sceKernelAllocateDirectMemory

Allocate direct memory

## Definition

```
#include <kernel.h>
int32_t sceKernelAllocateDirectMemory(
    off_t searchStart,
    off_t searchEnd,
    size_t len,
    size_t alignment,
    int memoryType,
    off_t *physAddrOut
)
```

## Arguments

|  |  |
| --- | --- |
| `searchStart` | Start physical address of the search range |
| `searchEnd` | End physical address of the search range |
| `len` | Size of memory to allocate (bytes, value larger than 0 and a multiple of 16 KiB) |
| `alignment` | Alignment of memory to allocate (bytes, 0 or a multiple of 16 KiB and a power of 2) |
| `memoryType` | Memory type of direct memory |
| `physAddrOut` | Destination to store start physical address for the allocated memory |

## Return Values

Stores the start physical address of the allocated memory in `*physAddrOut` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Memory cannot be allocated |

## Description

This function searches for and allocates direct memory.

For `searchStart` and `searchEnd`, specify a range to search for free direct memory. The physical addresses of the memory to be allocated are equal to or greater than `searchStart` and less than `searchEnd`. (Note that `searchEnd` is not included in the range.) The start physical address of direct memory is 0 and the end physical address can be referenced using `SCE_KERNEL_MAIN_DMEM_SIZE`.

For `len`, specify the memory size you want to allocate. The size must be larger than 0 and a multiple of 16 KiB. This size must also be within the range specified with `searchStart` and `searchEnd`.

For `alignment`, specify the alignment of the memory you want to allocate. It must be 0 or a multiple of 16 KiB and a power of 2.

For `memoryType`, specify the memory type of the allocated direct memory, in other words, the cache operation mode. For details, refer to `SceKernelMemoryType`.

## Examples

```
size_t memLen = 2 * 1024 * 1024; // Length: 2 MiB
size_t memAlign = 64 * 1024; // Alignment: 64 KiB

// Allocate 2 MiB direct memory
off_t memStart;
if ( sceKernelAllocateDirectMemory( 0,
    SCE_KERNEL_MAIN_DMEM_SIZE, memLen, memAlign,
    SCE_KERNEL_MTYPE_C_SHARED, &memStart) < 0 ) {
        // Error handling
}
```

## See Also

`SceKernelMemoryType`, `sceKernelCheckedReleaseDirectMemory()`, `sceKernelReleaseDirectMemory()`, `sceKernelMapDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelAllocateMainDirectMemory

Allocate direct memory

## Definition

```
#include <kernel.h>
int32_t sceKernelAllocateMainDirectMemory(
    size_t len,
    size_t alignment,
    int memoryType,
    off_t *physAddrOut
)
```

## Arguments

|  |  |
| --- | --- |
| `len` | Size of memory to allocate (bytes, value larger than 0 and a multiple of 16 KiB) |
| `alignment` | Alignment of memory to allocate (bytes, 0 or a multiple of 16 KiB and a power of 2) |
| `memoryType` | Memory type of direct memory |
| `physAddrOut` | Destination to store start physical address for the allocated memory |

## Return Values

Stores the start physical address of the allocated memory in `*physAddrOut` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| `SCE_KERNEL_ERROR_EAGAIN` | 0x80020023 | Memory cannot be allocated |

## Description

This function searches for and allocates direct memory.

Other than the difference of not specifying a range to search for free direct memory, this function has the same feature as `sceKernelAllocateDirectMemory()`. Refer to the explanation of `sceKernelAllocateDirectMemory()`.

## See Also

`SceKernelMemoryType`, `sceKernelCheckedReleaseDirectMemory()`, `sceKernelReleaseDirectMemory()`, `sceKernelMapDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelAvailableDirectMemorySize

Query size and physical address of empty direct memory area

## Definition

```
#include <kernel.h>
int32_t sceKernelAvailableDirectMemorySize(
    off_t searchStart,
    off_t searchEnd,
    size_t alignment,
    off_t *physAddrOut,
    size_t *sizeOut
)
```

## Arguments

|  |  |
| --- | --- |
| `searchStart` | Start physical address of the search range |
| `searchEnd` | End physical address of the search range |
| `alignment` | Alignment of search target empty area (bytes, 0 or a power of 2) |
| `physAddrOut` | Destination to store physical start address of largest empty area that fulfills the specified conditions |
| `sizeOut` | Destination to store size of largest empty area that fulfills the specified conditions (bytes) |

## Return Values

Stores the size of the largest empty direct memory area that fulfills the specified conditions in `*sizeOut`, stores the physical start address of the area in `*physAddrOut`, and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Empty area that fulfills the specified conditions does not exist |

## Description

This function searches for the largest empty direct memory area and returns its size and physical address.

For `searchStart` and `searchEnd`, specify a range to search for free direct memory. The physical addresses of the memory to be searched are equal to or greater than `searchStart` and less than `searchEnd`. (Note that `searchEnd` is not included in the range.) The start physical address of direct memory is 0 and the end physical address can be referenced using `SCE_KERNEL_MAIN_DMEM_SIZE`.

For `alignment`, specify the alignment of the search target area. It must be 0 or a power of 2. If less than 16 KiB is specified, 16 KiB will be considered to be specified.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelAvailableFlexibleMemorySize

Query size of unused flexible memory

## Definition

```
#include <kernel.h>
int32_t sceKernelAvailableFlexibleMemorySize(
    size_t *sizeOut
)
```

## Arguments

|  |  |
| --- | --- |
| `sizeOut` | Destination to store size of unused flexible memory (bytes) |

## Return Values

Stores the size of unused flexible memory in `*sizeOut` and returns `SCE_OK` (=0).

## Description

This function returns the size of unused flexible memory.

Note that fractional amounts will be rounded down to the nearest MiB.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelBatchMap

Batch perform mapping/unmapping/protection changing/memory type changing on multiple areas

## Definition

```
#include <kernel.h>
int32_t sceKernelBatchMap(
    SceKernelBatchMapEntry *entries,
    int numberOfEntries,
    int *numberOfEntriesOut
)
```

## Arguments

|  |  |
| --- | --- |
| `entries` | Mapping information array |
| `numberOfEntries` | Number of elements for `entries` |
| `numberOfEntriesOut` | Destination to store the number of elements from among the `entries` elements that have actually been processed, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `entries` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| Unsupported operation was requested |
| Specified size is 0 or negative |

In addition, error codes may return for causes that are the same as for the functions equivalent to each operation specified in `entries`. Refer to the return values of `sceKernelMapDirectMemory()`, `sceKernelMunmap()`, `sceKernelMprotect()`, and `sceKernelMtypeprotect()` for details.

Regardless of normal termination or an error, the number of elements actually processed will be stored in `*numberOfEntriesOut` as long as a value other than NULL is specified to `numberOfEntriesOut`.

## Description

This function batch performs mapping/unmapping/protection changing/memory type changing on multiple areas. Efficiency is increased relative to calling functions such as `sceKernelMapDirectMemory()` multiple times.

For each element of the array `entries`, specify the target area and the operation to perform onto that area. Each element will be processed in order. Specifying the same operation in succession makes optimization of batch processing more effective. If all `entries` elements are processed normally or if the processing fails partway through, this function call will result in all GPU TLB entries becoming invalid.

For the restrictions that apply to each operation and for other information, refer to the explanation of `sceKernelMapDirectMemory()`. Also refer to the explanations of `sceKernelMapDirectMemory()`, `sceKernelMunmap()`, `sceKernelMprotect()`, and `sceKernelMtypeprotect()`.

When the protection is changed with this function, the behavior when the following conditions are satisfied differs from that of `sceKernelMprotect()` and `sceKernelMtypeprotect()`.

* The target memory is not a pooled memory designated area
* The target memory address is not aligned to a 16 KiB boundary

Behavior at such times of each function is as follows.

* When this function is used: `SCE_KERNEL_ERROR_EINVAL` will be returned
* When `sceKernelMprotect()` or `sceKernelMtypeprotect()` is used: an error will not be returned, and processing will be carried out by rounding to a page boundary

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelBatchMap2

Batch perform mapping/unmapping/protection changing/memory type changing on multiple areas

## Definition

```
#include <kernel.h>
int32_t sceKernelBatchMap2(
    SceKernelBatchMapEntry *entries,
    int numberOfEntries,
    int *numberOfEntriesOut,
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `entries` | Mapping information array |
| `numberOfEntries` | Number of elements for `entries` |
| `numberOfEntriesOut` | Destination to store the number of elements from among the `entries` elements that have actually been processed, or NULL |
| `flags` | Flags for mapping operations, or 0 |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `entries` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| Unsupported operation was requested |
| Specified size is 0 or negative |
| `flags` is not 0, not a correct flag value, nor the bitwise OR of correct flag values |

In addition, error codes may return for causes that are the same as for the functions equivalent to each operation specified in `entries`. Refer to the return values of `sceKernelMapDirectMemory()`, `sceKernelMunmap()`, `sceKernelMprotect()`, and `sceKernelMtypeprotect()` for details.

Regardless of normal termination or an error, the number of elements actually processed will be stored in `*numberOfEntriesOut` as long as a value other than NULL is specified to `numberOfEntriesOut`.

## Description

This function batch performs mapping/unmapping/protection changing/memory type changing on multiple areas. Efficiency is increased relative to calling functions such as `sceKernelMapDirectMemory()` multiple times. This function is the same as `sceKernelBatchMap()` in terms of batch performing the applicable operation on multiple areas, but it differs in that flags can be specified for mapping operations to `flags`.

For each element of the array `entries`, specify the target area and the operation to perform onto that area. Each element will be processed in order. Specifying the same operation in succession makes optimization of batch processing more effective. If all `entries` elements are processed normally or if the processing fails partway through, this function call will result in all GPU TLB entries becoming invalid.

`flags` is only applied to mapping operations. Specify the bitwise OR of the following flags. Specify 0 if not required.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MAP_FIXED` | 0x0010 | Fix map destination to `*start` |
| `SCE_KERNEL_MAP_NO_OVERWRITE` | 0x0080 | Prohibit mapping when an area that is being used is included between `*start` and `*start`+`length` |
| `SCE_KERNEL_MAP_NO_COALESCE` | 0x400000 | Instruct `sceKernelVirtualQuery()` not to merge neighboring areas |
| `SCE_KERNEL_MAP_ALIGNED_16KB` | 0x0e000000 | Align map destination to a 16-KiB boundary when `SCE_KERNEL_MAP_FIXED` is not specified |
| `SCE_KERNEL_MAP_ALIGNED_64KB` | 0x10000000 | Align map destination to a 64-KiB boundary when `SCE_KERNEL_MAP_FIXED` is not specified |
| `SCE_KERNEL_MAP_ALIGNED_2MB` | 0x15000000 | Align map destination to a 2-MiB boundary when `SCE_KERNEL_MAP_FIXED` is not specified |

(`start` and `length` are members of the `SceKernelBatchMapEntry` structure.)

* If `SCE_KERNEL_MAP_FIXED` is specified, the specified direct memory will be mapped to the virtual address area from `*start` to `*start`+`length`. When mapping/reserving/locking has already been performed within this area, the `SCE_KERNEL_ERROR_ENOMEM` error will occur if `SCE_KERNEL_MAP_NO_OVERWRITE` is specified. If that value is not specified, the overlapping portion will be automatically unmapped/unreserved/unlocked, and mapping of the specified area will then be performed.
* If `SCE_KERNEL_MAP_FIXED` is not specified, `*start` will be interpreted as the virtual address where a search will begin for free space in `length` bytes, and the area selected by the system according to the `SCE_KERNEL_MAP_ALIGNED_*` specification will be the map destination. (If `SCE_KERNEL_MAP_ALIGNED_*` is not specified, the map destination will be aligned to a 16-KiB boundary.) If specifying a map destination is not required, specify 0 for `*start`.
* If `SCE_KERNEL_MAP_NO_COALESCE` is specified, areas will not be merged (neighboring areas with the same characteristics will not be handled as one area) upon the call of `sceKernelVirtualQuery()`.

For the restrictions that apply to each operation and for other information, refer to the explanation of `sceKernelMapDirectMemory()`. Also refer to the explanations of `sceKernelMapDirectMemory()`, `sceKernelMunmap()`, `sceKernelMprotect()`, and `sceKernelMtypeprotect()`.

When the protection is changed with this function, the behavior when the following conditions are satisfied differs from that of `sceKernelMprotect()` and `sceKernelMtypeprotect()`.

* The target memory is not a pooled memory designated area
* The target memory address is not aligned to a 16 KiB boundary

Behavior at such times of each function is as follows.

* When this function is used: `SCE_KERNEL_ERROR_EINVAL` will be returned
* When `sceKernelMprotect()` or `sceKernelMtypeprotect()` is used: an error will not be returned, and processing will be carried out by rounding to a page boundary

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelCheckedReleaseDirectMemory

Release direct memory

## Definition

```
#include <kernel.h>
int32_t sceKernelCheckedReleaseDirectMemory(
    off_t start,
    size_t len
)
```

## Arguments

|  |  |
| --- | --- |
| `start` | Start physical address of the direct memory to release (aligned to 16 KiB) |
| `len` | Size of the direct memory to release (bytes, multiple of 16 KiB) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | There is an area where memory has not been allocated in the range specified with `start` and `len` |

## Description

This function releases contiguous direct memory allocated with `sceKernelAllocateDirectMemory()`/`sceKernelAllocateMainDirectMemory()`.

The range of memory from `start` to `start`+`len` will be released.

The range to be released does not have to match the range allocated with `sceKernelAllocateDirectMemory()`/`sceKernelAllocateMainDirectMemory()`; however, there must not be any unallocated area. It is not a problem if memory mapped with `sceKernelMapDirectMemory()` is included. In this case, the area will be unmapped.

## Examples

```
size_t memLen = 2 * 1024 * 1024; // Length: 2 MiB
size_t memAlign = 64 * 1024; // Alignment: 64 KiB

// Allocate 2 MiB direct memory
off_t memStart;
if ( sceKernelAllocateDirectMemory( 0,
    SCE_KERNEL_MAIN_DMEM_SIZE, memLen, memAlign,
    SCE_KERNEL_MTYPE_C_SHARED, &memStart) < 0 ) {
        // Error handling
}

// Release 2MiB direct memory
if ( sceKernelCheckedReleaseDirectMemory( memStart, memLen ) < 0 ) {
        // Error handling
}
```

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`, `sceKernelReleaseDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelClearVirtualRangeName

Delete the name of the memory area mapped to a virtual address

## Definition

```
#include <kernel.h>
int32_t sceKernelClearVirtualRangeName(
    const void *addr,
    size_t len
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Target virtual address |
| `len` | Size of the target area (bytes) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Range specified with `addr` and `len` is outside the virtual address space range |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Attempted to set a number of name entries exceeding 4096 to the AMM virtual address space |

## Description

This function deletes the name set to the memory mapped in the range of `len` bytes from the `addr` virtual address. Name deletion is performed in logical page units, and the name set to the logical pages including the specified range will be deleted. This function is equivalent to `sceKernelSetVirtualRangeName(addr, len, "")` (in other words, `sceKernelSetVirtualRangeName()` without a name specification).

It's also possible to delete a name set to an area where memory has not been mapped by calling this function for the AMM virtual address space that can be obtained using `sce::Ampr::Amm::getVirtualAddressRanges()`. In addition, one name entry can be divided into multiple entries when this function is called with a part of a named area specified. When the number of name entries within the AMM virtual address space exceeds the limit of 4096 as a result, `SCE_KERNEL_ERROR_ENOMEM` will be returned.

## See Also

`sceKernelVirtualQuery()`, `SceKernelVirtualQueryInfo`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelConfiguredFlexibleMemorySize

Query the total size of flexible memory

## Definition

```
#include <kernel.h>
int32_t sceKernelConfiguredFlexibleMemorySize(
    size_t *sizeOut
)
```

## Arguments

|  |  |
| --- | --- |
| `sizeOut` | Destination to store the total size of flexible memory (bytes) |

## Return Values

Stores the total size of flexible memory in `*sizeOut` and returns `SCE_OK` (=0).

## Description

This function returns the total size of flexible memory. The default size will be returned.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelDirectMemoryQuery

Get information about the allocated direct memory area

## Definition

```
#include <kernel.h>
int32_t sceKernelDirectMemoryQuery(
    off_t offset,
    int flags,
    void *info,
    size_t infoSize
)
```

## Arguments

|  |  |
| --- | --- |
| `offset` | Start physical address of the direct memory to obtain information (aligned to 16 KiB) |
| `flags` | 0 or `SCE_KERNEL_DMQ_FIND_NEXT` |
| `info` | Destination to store the obtained direct memory area information (pointer to an `SceKernelDirectMemoryQueryInfo` structure) |
| `infoSize` | Information size. Specify `sizeof(SceKernelDirectMemoryQueryInfo)` |

## Return Values

Stores the obtained information in `*info` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Direct memory area does not exist at `offset` (when 0 is specified for `flags`), or direct memory area does not exist at `offset` and onwards (when `SCE_KERNEL_DMQ_FIND_NEXT` is specified for `flags`) |

## Description

This function obtains the start, end, and memory type of the allocated direct memory area at the specified physical address.

When `SCE_KERNEL_DMQ_FIND_NEXT` is specified for `flags`, and if there is no direct memory area at the physical address of `offset` but a subsequent direct memory area does exist, this function will not return the `SCE_KERNEL_ERROR_EACCES` error and will return information of the subsequently existing area.

Note that this function may recognize neighboring memory areas of the same memory type as one area and return results accordingly.

## Examples

```
SceKernelDirectMemoryQueryInfo info;

// Get info of the first memory area.
if ( sceKernelDirectMemoryQuery( 0, SCE_KERNEL_DMQ_FIND_NEXT, &info, sizeof(SceKernelDirectMemoryQueryInfo)) < 0 ) {
        // Error handling
}
```

## See Also

`SceKernelDirectMemoryQueryInfo`, `sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelGetDirectMemorySize

Get size of direct memory

## Definition

```
#include <kernel.h>
size_t sceKernelGetDirectMemorySize(void)
```

## Arguments

None

## Return Values

Returns the size of direct memory (same value as `SCE_KERNEL_MAIN_DMEM_SIZE`).

## Description

This function obtains the size of direct memory.

`SCE_KERNEL_MAIN_DMEM_SIZE` is a macro that calls this function.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelGetDirectMemoryType

Get memory type of direct memory

## Definition

```
#include <kernel.h>
int32_t sceKernelGetDirectMemoryType(
    off_t start,
    int *memoryTypeOut,
    off_t *regionStartOut,
    off_t *regionEndOut
)
```

## Arguments

|  |  |
| --- | --- |
| `start` | Physical address of the target direct memory |
| `memoryTypeOut` | Destination to store the currently set memory type |
| `regionStartOut` | Destination to store start physical address of the allocated direct memory containing the address specified with `start` |
| `regionEndOut` | Destination to store end physical address of the allocated direct memory containing the address specified with `start` |

## Return Values

Stores the memory type in `*memoryTypeOut`, the start physical address in `*regionStartOut`, the end physical address in `*regionEndOut`, and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_ENOENT` | 0x80020002 | Direct memory specified with `start` is not allocated |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |

## Description

This function obtains the memory type of direct memory.

For `start`, specify the physical address for the memory type you want to look up. Any position can be specified as long as the target direct memory is already allocated. (There are no restrictions such as 16 KiB alignment.)

For `memoryTypeOut`, specify a pointer to the variable for receiving the memory type.

For `regionStartOut` and `regionEndOut`, specify a pointer to the variable for receiving the start and end physical addresses of the direct memory. (Do not specify a NULL pointer.)

## Examples

```
size_t memLen = 2 * 1024 * 1024; // Allocation length: 2 MiB
size_t memAlign = 64 * 1024; // Alignment: 64 KiB

// Allocate 2 MiB direct memory
off_t memStart;
if ( sceKernelAllocateDirectMemory( 0,
    SCE_KERNEL_MAIN_DMEM_SIZE,
    memLen, memAlign,
    SCE_KERNEL_MTYPE_C_SHARED, &memStart) < 0 ) {
        // Error handling
}

// Get the memory type of the direct memory
int memType;
off_t regionStart, regionEnd;
if ( sceKernelGetDirectMemoryType( memStart, &memType, &regionStart,
    &regionEnd) < 0 ) {
        // Error handling
}
```

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`, `SceKernelMemoryType`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelGetPageTableStats

Get page table usage statuses

## Definition

```
#include <kernel.h>
int32_t sceKernelGetPageTableStats(
    int *cpuTotal,
    int *cpuAvailable,
    int *gpuTotal,
    int *gpuAvailable
)
```

## Arguments

|  |  |
| --- | --- |
| `cpuTotal` | Destination to store the number of CPU page tables retained by the system |
| `cpuAvailable` | Destination to store the number of unused CPU page tables |
| `gpuTotal` | Destination to store the number of GPU page tables retained by the system |
| `gpuAvailable` | Destination to store the number of unused GPU page tables |

## Return Values

Stores the previously mentioned information in the variables specified for each argument and returns `SCE_OK` (=0).

## Description

This function returns the CPU and GPU page table memory usage statuses.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelGetPrtAperture

Get PRT aperture

## Definition

```
#include <kernel.h>
int32_t sceKernelGetPrtAperture(
    int apertureId,
    void **addr,
    size_t *len
)
```

## Arguments

|  |  |
| --- | --- |
| `apertureId` | Aperture ID (0 to 2) |
| `addr` | Destination to store the start virtual address of the obtained aperture area |
| `len` | Destination to store the size of the obtained aperture area (bytes) |

## Return Values

Stores the start virtual address in `**addr`, stores the size in `*len`, and returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Invalid aperture ID is specified |

## Description

This function obtains the start virtual address and size of the PRT (partially resident texture) aperture specified in `apertureId`. For `apertureId`, specify the ID of the aperture for which the range of the virtual address space has been set in advance with `sceKernelSetPrtAperture()`. When the ID of an aperture for which the range of the virtual address space has not been set is specified, an undefined address or size may return.

A PRT aperture is an area where page faults are restricted during texture fetching by the GPU. Of the four hardware PRT apertures, the PlayStation®5 kernel provides three to the application program.

## See Also

`sceKernelSetPrtAperture()`

# sceKernelIsStack

Check whether or not the specified address is in the stack

## Definition

```
#include <kernel.h>
int32_t sceKernelIsStack(
    void *addr,
    void **start,
    void **end
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Target virtual address |
| `start` | Destination to store start virtual address for the stack area |
| `end` | Destination to store end virtual address for the stack area |

## Return Values

Stores the start virtual address and end virtual address of the stack area in `*start` and `*end` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Memory is not mapped to `addr` |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `addr` is outside the virtual address space range |

## Description

This function searches the stack area including the virtual address `addr`.

When a pointer that is not NULL is specified for `start` and `end`, and if `addr` is included in the stack area, the start virtual address/end virtual address will be stored in `*start` and `*end`. If `addr` is not included in the stack area, 0 will be stored in `*start` and `*end`.

When NULL is specified for one or both `start` and `end`, an error will not occur for the function call, and the results will not be stored in the argument with NULL specified.

Note that this function can only search stack areas automatically allocated by the system.

# sceKernelMapDirectMemory

Map direct memory to virtual address space

## Definition

```
#include <kernel.h>
int32_t sceKernelMapDirectMemory(
    void **addr,
    size_t len,
    int prot,
    int flags,
    off_t directMemoryStart,
    size_t alignment
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Input: start virtual address of the map destination or virtual address to begin searching for free space (aligned to 16 KiB, see details below)  Output: start virtual address of the mapped area |
| `len` | Size of memory to map (bytes, multiple of 16 KiB) |
| `prot` | Memory protection to set for the mapped area (see details below) |
| `flags` | Flags (see details below), or 0 |
| `directMemoryStart` | Start physical address of the direct memory to map (aligned to 16 KiB) |
| `alignment` | Alignment of the map destination (only valid when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`; multiple of 16 KiB and a power of 2), or 0 |

## Return Values

Stores the start virtual address of the mapped area in `*addr` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Access is prohibited for the area specified as the map destination |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `*addr` is not aligned to the page boundary, or a virtual address outside of the usable area is specified (only when `SCE_KERNEL_MAP_FIXED` is specified for `flags`) |
| `len` is not a multiple of 16 KiB, or it is 0 |
| `flags` is not 0, not a correct flag value, nor the bitwise OR of correct flag values |
| `directMemoryStart` is not a multiple of 16 KiB |
| `alignment` is not a multiple of 16 KiB and a power of 2, nor is it 0 |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | An area that is being used is included between `*addr` and `*addr`+`len` (when `SCE_KERNEL_MAP_FIXED` and `SCE_KERNEL_MAP_NO_OVERWRITE` are specified for `flags`) |
| No free space found (when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`) |
| Insufficient page table  * The size of the page table pool can be increased in 2 MiB increments using a setting in the parameter file (param.json). For details about the setting and the default size, refer to [Kernel Overview - Memory Management - Customization of Memory Assignment](../Kernel-Overview/customization-of-memory-assignment.html). * The page table usage statuses can be obtained using `sceKernelGetPageTableStats()`. |

## Description

This function maps direct memory that is already allocated to a virtual address space.

Specify the direct memory to map using `directMemoryStart` and `len`.

For `flags`, specify the bitwise OR of the following flags. Specify 0 if not required.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MAP_FIXED` | 0x0010 | Fix map destination to `*addr` |
| `SCE_KERNEL_MAP_NO_OVERWRITE` | 0x0080 | Prohibit mapping when an area that is being used is included between `*addr` and `*addr`+`len` |
| `SCE_KERNEL_MAP_NO_COALESCE` | 0x400000 | Instruct `sceKernelVirtualQuery()` not to merge neighboring areas |

* If `SCE_KERNEL_MAP_FIXED` is specified, the specified direct memory will be mapped to the virtual address area from `*addr` to `*addr`+`len`. When mapping/reserving/locking has already been performed within this area, the `SCE_KERNEL_ERROR_ENOMEM` error will occur if `SCE_KERNEL_MAP_NO_OVERWRITE` is specified. If that value is not specified, the overlapping portion will be automatically unmapped/unreserved/unlocked, and mapping of the specified area will then be performed.
* If `SCE_KERNEL_MAP_FIXED` is not specified, `*addr` will be interpreted as the virtual address where a search will begin for free space in `len` bytes, and the area selected by the system according to the `alignment` specification will be the map destination. If specifying a map destination is not required, specify 0 for `*addr`.
* If `SCE_KERNEL_MAP_NO_COALESCE` is specified, areas will not be merged (neighboring areas with the same characteristics will not be handled as one area) upon the call of `sceKernelVirtualQuery()`.

For `prot`, specify the protection to set for the mapped area with the bitwise OR of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |
| `SCE_KERNEL_PROT_AMPR_READ` | 0x40 | Permit reads from the AMPR |
| `SCE_KERNEL_PROT_AMPR_WRITE` | 0x80 | Permit writes from the AMPR |
| `SCE_KERNEL_PROT_AMPR_RW` | 0xc0 | Permit writes and reads from the AMPR |
| `SCE_KERNEL_PROT_ACP_READ` | 0x100 | Permit reads from the ACP |
| `SCE_KERNEL_PROT_ACP_WRITE` | 0x200 | Permit writes from the ACP |
| `SCE_KERNEL_PROT_ACP_RW` | 0x300 | Permit writes and reads from the ACP |

## Examples

```
size_t memLen = 2 * 1024 * 1024; // Allocation length: 2 MiB
size_t mapLen = 1 * 1024 * 1024; // Map length: 1 MiB
size_t memAlign = 64 * 1024; // Alignment: 64 KiB

// Allocate 2 MiB direct memory
off_t memStart;
if ( sceKernelAllocateDirectMemory( 0,
    SCE_KERNEL_MAIN_DMEM_SIZE, memLen, memAlign,
    SCE_KERNEL_MTYPE_C_SHARED, &memStart) < 0 ) {
        // Error handling
}

// Map 1MiB direct memory to the virtual address space
void* addr = 0;
if ( sceKernelMapDirectMemory( &addr, mapLen, 
    SCE_KERNEL_PROT_GPU_RW, 0, memStart, memAlign ) < 0 ) {
        // Error handling
}
```

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`, `sceKernelMunmap()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMapDirectMemory2

Map direct memory to a virtual address space and set the memory type

## Definition

```
#include <kernel.h>
int32_t sceKernelMapDirectMemory2(
    void **addr,
    size_t len,
    int memoryType,
    int prot,
    int flags,
    off_t directMemoryStart,
    size_t alignment
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Input: start virtual address of the map destination or virtual address to begin searching for free space (aligned to 16 KiB)  Output: start virtual address of the mapped area |
| `len` | Size of memory to map (bytes, multiple of 16 KiB) |
| `memoryType` | Memory type to set for the direct memory to map, or -1 |
| `prot` | Memory protection to set for the mapped area |
| `flags` | Flags, or 0 |
| `directMemoryStart` | Start physical address of the direct memory to map (aligned to 16 KiB) |
| `alignment` | Alignment of the map destination (only valid when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`; multiple of 16 KiB and a power of 2), or 0 |

## Return Values

Stores the start virtual address of the mapped area in `*addr` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Access is prohibited for the area specified as the map destination |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `*addr` is not aligned to the page boundary, or a virtual address outside of the usable area is specified (only when `SCE_KERNEL_MAP_FIXED` is specified for `flags`) |
| `len` is not a multiple of 16 KiB, or it is 0 |
| `flags` is not 0, not a correct flag value, nor the bitwise OR of correct flag values |
| `directMemoryStart` is not a multiple of 16 KiB |
| `alignment` is not a multiple of 16 KiB and a power of 2, nor is it 0 |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | An area that is being used is included between `*addr` and `*addr`+`len` (when `SCE_KERNEL_MAP_FIXED` and `SCE_KERNEL_MAP_NO_OVERWRITE` are specified for `flags`) |
| No free space found (when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`) |
| Insufficient page table  * The size of the page table pool can be increased in 2 MiB increments using a setting in the parameter file (param.json). For details about the setting and the default size, refer to [Kernel Overview - Memory Management - Customization of Memory Assignment](../Kernel-Overview/customization-of-memory-assignment.html). * The page table usage statuses can be obtained using `sceKernelGetPageTableStats()`. |

## Description

This function maps direct memory that is already allocated to a virtual address space.

Other than being able to specify a memory type for `memoryType` to set for direct memory to map, this function has the same feature as `sceKernelMapDirectMemory()`. Refer to the explanation of `sceKernelMapDirectMemory()`.

When changing the memory type, for `memoryType`, specify one of the enum constants defined with `SceKernelMemoryType`. When not changing the memory type, specify -1 for `memoryType`.

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`, `sceKernelMunmap()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMapNamedDirectMemory

Map direct memory to virtual address space

## Definition

```
#include <kernel.h>
int32_t sceKernelMapNamedDirectMemory(
    void **addr,
    size_t len,
    int prot,
    int flags,
    off_t directMemoryStart,
    size_t alignment,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Input: start virtual address of the map destination or virtual address to begin searching for free space (aligned to 16 KiB)  Output: start virtual address of the mapped area |
| `len` | Size of memory to map (bytes, multiple of 16 KiB) |
| `prot` | Memory protection to set for the mapped area |
| `flags` | Flags, or 0 |
| `directMemoryStart` | Start physical address of the direct memory to map (aligned to 16 KiB) |
| `alignment` | Alignment of the map destination (only valid when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`; multiple of 16 KiB and a power of 2), or 0 |
| `name` | Name to set for the mapped area (up to 32 bytes including the NULL-terminator character) |

## Return Values

Stores the start virtual address of the mapped area in `*addr` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Access is prohibited for the area specified as the map destination |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `*addr` is not aligned to the page boundary, or a virtual address outside of the usable area is specified (only when `SCE_KERNEL_MAP_FIXED` is specified for `flags`) |
| `len` is not a multiple of 16 KiB, or it is 0 |
| `flags` is not 0, not a correct flag value, nor the bitwise OR of correct flag values |
| `directMemoryStart` is not a multiple of 16 KiB |
| `alignment` is not a multiple of 16 KiB and a power of 2, nor is it 0 |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory or is NULL |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | An area that is being used is included between `*addr` and `*addr`+`len` (when `SCE_KERNEL_MAP_FIXED` and `SCE_KERNEL_MAP_NO_OVERWRITE` are specified for `flags`) |
| No free space found (when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`) |
| Insufficient page table  * The size of the page table pool can be increased in 2 MiB increments using a setting in the parameter file (param.json). For details about the setting and the default size, refer to [Kernel Overview - Memory Management - Customization of Memory Assignment](../Kernel-Overview/customization-of-memory-assignment.html). * The page table usage statuses can be obtained using `sceKernelGetPageTableStats()`. |

## Description

This function maps direct memory that is already allocated to a virtual address space.

Other than being able to specify a name to set for the area mapped to `name`, this function has the same feature as `sceKernelMapDirectMemory()`. Refer to the explanation of `sceKernelMapDirectMemory()`.

The set name can be obtained with `sceKernelVirtualQuery()`.

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolBatch

Batch perform committing/de-committing/protection changing/memory type changing/moving on a pooled memory designated area

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolBatch(
    const SceKernelMemoryPoolBatchEntry *entries,
    int n,
    int *indexOut,
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `entries` | Array of operation information to apply |
| `n` | Number of elements for `entries` |
| `indexOut` | Destination to store the number of elements from among the `entries` elements that have actually been processed, or NULL |
| `flags` | Reserved (specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `n` is less than 0 |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | One of the `op` in `entries` is invalid |

In addition, error codes may return for causes that are the same as for the functions equivalent to each operation specified in `entries`. Refer to the return values of `sceKernelMemoryPoolCommit()`, `sceKernelMemoryPoolDecommit()`, `sceKernelMprotect()`, `sceKernelMtypeprotect()`, and `sceKernelMemoryPoolMove()` for details.

Regardless of normal termination or an error, the number of elements actually processed will be stored in `*indexOut` as long as a value other than NULL is specified to `indexOut`.

## Description

This function batch performs committing/de-committing/protection changing/memory type changing/moving on one pooled memory designated area. Efficiency is increased relative to calling functions such as `sceKernelMemoryPoolCommit()` multiple times.

For each element of the array `entries`, specify the target area within the pooled memory designated area and the operation to perform onto that area. Each element will be processed in order. Specifying the same operation in succession makes optimization of batch processing more effective. All operations within the array `entries` must be for a pooled memory designated area created with one `sceKernelMemoryPoolReserve()` call. Moreover, the start address and size of the operation target area must be aligned to a 64 KiB boundary. In addition to these restrictions, restrictions exist for each operation; refer to each of the explanations for `sceKernelMemoryPoolCommit()`, `sceKernelMemoryPoolDecommit()`, `sceKernelMprotect()`, `sceKernelMtypeprotect()`, and `sceKernelMemoryPoolMove()`.

If all `entries` elements are processed normally or if the processing fails partway through, this function call will result in all GPU TLB entries becoming invalid.

## See Also

`SceKernelMemoryPoolBatchEntry`, `sceKernelMemoryPoolCommit()`, `sceKernelMemoryPoolDecommit()`, `sceKernelMprotect()`, `sceKernelMtypeprotect()`, `sceKernelMemoryPoolMove()`, `sceKernelMemoryPoolReserve()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolCommit

Place (commit) pooled memory onto a pooled memory designated area

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolCommit(
    void *addr,
    size_t len,
    int type,
    int prot,
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Start virtual address of the commit destination area (aligned to 64 KiB) |
| `len` | Size of memory to commit (bytes, multiple of 64 KiB) |
| `type` | Memory type to set for the memory to commit |
| `prot` | Memory protection to set for the memory to commit (see details below) |
| `flags` | Reserved (specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified virtual address range includes an address outside of the pooled memory designated area, or it spans over multiple pooled memory designated areas |
| `addr` is not aligned to a 64 KiB boundary |
| `len` is not a multiple of 64 KiB |
| `type` is an undefined value |
| `prot` is invalid |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | There is an area with pooled memory already committed within the specified virtual address range |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Failed to allocate memory from the memory pool |
| Insufficient page table  * The size of the page table pool can be increased in 2 MiB increments using a setting in the parameter file (param.json). For details about the setting and the default size, refer to [Kernel Overview - Memory Management - Customization of Memory Assignment](../Kernel-Overview/customization-of-memory-assignment.html). * The page table usage statuses can be obtained using `sceKernelGetPageTableStats()`. |

## Description

This function allocates an unused physical memory (pooled memory) block from the memory pool and places (commits) it onto the pooled memory designated area that has been reserved on the virtual address space with `sceKernelMemoryPoolReserve()`.

Specify the pooled memory designated area to commit the pooled memory to using `addr` and `len`. This function will fail if an already committed area exists within the specified range.

For `type`, specify the memory type of the pooled memory to commit, in other words, the cache operation mode. For details, refer to `SceKernelMemoryType`.

For `prot`, specify the protection to set for the pooled memory to commit using the bitwise OR of the following values. Note that you cannot specify a protection that permits access from the AMPR or ACP.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |

## Notes

* This function does not clear memory with 0's. It is often the case that memory is cleared with 0's when this function is called immediately after process startup; however, note that this is just a coincidence and not the doing of this function.
* When batch performing committing/de-committing/protection changing/memory type changing/moving on one pooled memory designated area, use `sceKernelMemoryPoolBatch()` to carry out processing in a shorter time.

## See Also

`SceKernelMemoryType`, `sceKernelMemoryPoolReserve()`, `sceKernelMemoryPoolDecommit()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolDecommit

Cancel placement of (de-commit) pooled memory

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolDecommit(
    void *addr,
    size_t len,
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Start virtual address of the area to de-commit (aligned to 64 KiB) |
| `len` | Size of the area to de-commit (bytes, multiple of 64 KiB) |
| `flags` | Reserved (specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified virtual address range includes an address outside of the pooled memory designated area, or it spans over multiple pooled memory designated areas |
| `addr` is not aligned to a 64 KiB boundary |
| `len` is not a multiple of 64 KiB |
| `flags` is not 0 |

## Description

This function de-commits an area of `len` bytes from the virtual address `addr` within the pooled memory designated area - in other words, placed physical memory (pooled memory) is removed and returned to the memory pool.

## Notes

When batch performing committing/de-committing/protection changing/memory type changing/moving on one pooled memory designated area, use `sceKernelMemoryPoolBatch()` to carry out processing in a shorter time.

## See Also

`sceKernelMemoryPoolCommit()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolExpand

Allocate direct memory and add to memory pool

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolExpand(
    off_t searchStart,
    off_t searchEnd,
    size_t len,
    size_t alignment,
    off_t *physAddrOut
)
```

## Arguments

|  |  |
| --- | --- |
| `searchStart` | Start physical address of the search range |
| `searchEnd` | End physical address of the search range |
| `len` | Size of memory to allocate (bytes, multiple of 64 KiB) |
| `alignment` | Alignment of memory to allocate (bytes, 0 or a multiple of 64 KiB and a power of 2) |
| `physAddrOut` | Destination to store start physical address for the allocated memory |

## Return Values

Stores the start physical address of the allocated memory in `*physAddrOut` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Memory cannot be allocated |

## Description

This function searches for and allocates direct memory and adds it under memory pool management as pooled memory.

For `searchStart` and `searchEnd`, specify a range to search for free direct memory. The physical addresses of the memory to be allocated are equal to or greater than `searchStart` and less than `searchEnd`. (Note that `searchEnd` is not included in the range.) The start physical address of direct memory is 0 and the end physical address can be referenced using `SCE_KERNEL_MAIN_DMEM_SIZE`.

For `len`, specify the memory size you want to allocate. The size must be a multiple of 64 KiB. This size must also be within the range specified with `searchStart` and `searchEnd`.

For `alignment`, specify the alignment of the memory you want to allocate. It must be 0 or a multiple of 64 KiB and a power of 2.

Note that pooled memory - in other words, direct memory added to the memory pool - cannot be freed until the process terminates.

Operation carried out by this function entails a relatively large cost and is often prolonged by being affected from processing being executed by another CPU. Because of this, prepare a sufficient amount of pooled memory upon initialization processing, for example, and avoid having to use this function in sections where real-time processing is required.

## See Also

`sceKernelAllocateDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolGetBlockStats

Get pooled memory usage

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolGetBlockStats(
    SceKernelMemoryPoolBlockStats *output,
    size_t outputSize
)
```

## Arguments

|  |  |
| --- | --- |
| `output` | Destination to store obtained usage |
| `outputSize` | Size of destination to store usage (bytes). Specify `sizeof(SceKernelMemoryPoolBlockStats)` |

## Return Values

Stores the usage in `*output` and returns `SCE_OK` (=0).

## Description

This function obtains information about the usage of pooled memory - in other words, physical memory managed by the memory pool.

Pooled memory usage is partitioned into 64 KiB blocks and managed. The number of blocks corresponding to each usage will be stored in the fields of the `SceKernelMemoryPoolBlockStats` structure, which is the destination for storing the obtained results.

## See Also

`SceKernelMemoryPoolBlockStats`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolMove

Move the memory placed (committed) on a pooled memory designated area

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolMove(
    void *dst,
    void *src,
    size_t len,
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `dst` | Start virtual address of the move destination area (aligned to 64 KiB) |
| `src` | Start virtual address of the move source area (aligned to 64 KiB) |
| `len` | Size of memory to move (bytes, multiple of 64 KiB) |
| `flags` | Reserved (specify 0) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified virtual address range includes an address outside of the pooled memory designated area, or it spans over multiple pooled memory designated areas |
| `dst` or `src` is not aligned to a 64 KiB boundary |
| `len` is not a multiple of 64 KiB |
| `flags` is not 0 |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | Move destination virtual address range includes an area where a memory other than the move source pooled memory is committed |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Insufficient page table  * The size of the page table pool can be increased in 2 MiB increments using a setting in the parameter file (param.json). For details about the setting and the default size, refer to [Kernel Overview - Memory Management - Customization of Memory Assignment](../Kernel-Overview/customization-of-memory-assignment.html). * The page table usage statuses can be obtained using `sceKernelGetPageTableStats()`. |

## Description

This function moves the physical memory (pooled memory) placed (committed) within the pooled memory designated area.

Specify the move source area with `src` and `len`, and specify the move destination area with `dst` and `len`. Both areas must be within the same pooled memory designated area. It is not a problem if the move source area and move destination area overlap. This function will fail if an already committed area other than the move source area exists in the move destination area.

## Notes

When batch performing committing/de-committing/protection changing/memory type changing/moving on one pooled memory designated area, use `sceKernelMemoryPoolBatch()` to carry out processing in a shorter time.

## See Also

`sceKernelMemoryPoolCommit()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMemoryPoolReserve

Reserve pooled memory designated area on the virtual address space

## Definition

```
#include <kernel.h>
int32_t sceKernelMemoryPoolReserve(
    void *addrIn,
    size_t len,
    size_t alignment,
    int flags,
    void **addrOut
)
```

## Arguments

|  |  |
| --- | --- |
| `addrIn` | Start virtual address of the area to allocate (aligned to 2 MiB), virtual address to begin searching for free space, or NULL (see details below) |
| `len` | Size of the area to allocate (bytes, multiple of 2 MiB) |
| `alignment` | Alignment of the start virtual address (bytes, 2 MiB or more and a power of 2, only valid when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`), or 0 |
| `flags` | Flags (see details below), or 0 |
| `addrOut` | Destination to store start virtual address for the allocated area |

## Return Values

Stores the start virtual address of the allocated area in `*addrOut` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `*addrIn` is not aligned to a 2 MiB boundary, or a virtual address outside of the usable area is specified (only when `SCE_KERNEL_MAP_FIXED` is specified for `flags`) |
| `len` is not a multiple of 2 MiB, or it is 0 |
| `flags` is not 0, not a correct flag value, nor the bitwise OR of correct flag values |
| `alignment` is not 2 MiB or more and a power of 2, nor is it 0 |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Failed to allocate memory for pooled memory designated area management from the memory pool |
| Area that is being used is included in the range specified with `*addrIn` and `len` (when `SCE_KERNEL_MAP_FIXED` and `SCE_KERNEL_MAP_NO_OVERWRITE` are specified for `flags`) |
| No free space found (when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`) |

## Description

This function reserves an area on virtual address space where physical memory within the memory pool (pooled memory) can be placed.

Specify the virtual address area to reserve as the pooled memory designated area using `addrIn` and `len`.

For `flags`, specify the bitwise OR of the following flags. Specify 0 if not required.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MAP_FIXED` | 0x0010 | Fix reserve destination to `*addrIn` |
| `SCE_KERNEL_MAP_NO_OVERWRITE` | 0x0080 | Prohibit reserving when an area that is being used is included in the range specified with `*addrIn` and `len` |

* If `SCE_KERNEL_MAP_FIXED` is specified, the virtual address area from `*addrIn` to `*addr`+`len` will be reserved as the pooled memory designated area. When reserving/mapping/locking has already been performed within this area, the `SCE_KERNEL_ERROR_ENOMEM` error will occur if `SCE_KERNEL_MAP_NO_OVERWRITE` is specified. If that value is not specified, the overlapping portion will be automatically unreserved/unmapped/unlocked, and reserving of the specified area will subsequently be performed.
* If `SCE_KERNEL_MAP_FIXED` is not specified, `*addrIn` will be interpreted as the virtual address where a search will begin for free space in `len` bytes, and the area selected by the system according to the `alignment` specification will be reserved as the pooled memory designated area. If specifying a pooled memory designated area reserve destination is not required, specify NULL for `*addrIn`.

This function allocates memory required for pooled memory designated area management from the memory pool. The required size is 1 block (64 KiB) for each 1 GiB of pooled memory designated area. 1 block will still be allocated for managing any remaining pooled memory designated area that does not amount to 1 GiB.

Immediately after the execution of this function, the entire area will be in a non-committed state (state where pooled memory is not placed). To use as a memory area, call `sceKernelMemoryPoolCommit()` and commit (place) pooled memory.

To free the area reserved using this function, use `sceKernelMunmap()`. Unlike direct memory, the entire reserved area must be freed with one function call; it is not possible to free just a part of the reserved area.

Operation carried out by this function entails a relatively large cost and is often prolonged by being affected from processing being executed by another CPU. Because of this, reserve a sufficient amount of pooled memory designated area upon initialization processing and avoid having to use this function in sections where real-time processing is required.

## See Also

`sceKernelMemoryPoolCommit()`, `sceKernelMunmap()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMprotect

Set protection

## Definition

```
#include <kernel.h>
int sceKernelMprotect(
    const void *addr, 
    size_t len, 
    int prot
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Start virtual address of the area to set protection |
| `len` | Size of the area to set protection (bytes) |
| `prot` | Protection to set (see details below) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified virtual address range is invalid |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | `prot` is invalid |

## Description

This function changes memory protection.

For `addr` and `len`, specify the virtual address range. For `prot`, specify the protection.

Memory protection is performed in logical page units, and the specified protection will be applied for the logical pages including the specified range. Thus, an error will not be returned even if the specified range is not aligned to a 16 KiB boundary, and processing will be carried out by rounding to a page boundary.

For `prot`, specify the bitwise OR of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |
| `SCE_KERNEL_PROT_AMPR_READ` | 0x40 | Permit reads from the AMPR |
| `SCE_KERNEL_PROT_AMPR_WRITE` | 0x80 | Permit writes from the AMPR |
| `SCE_KERNEL_PROT_AMPR_RW` | 0xc0 | Permit writes and reads from the AMPR |
| `SCE_KERNEL_PROT_ACP_READ` | 0x100 | Permit reads from the ACP |
| `SCE_KERNEL_PROT_ACP_WRITE` | 0x200 | Permit writes from the ACP |
| `SCE_KERNEL_PROT_ACP_RW` | 0x300 | Permit writes and reads from the ACP |

Note the following points when changing the protection of a part of the pooled memory designated area using this function.

* A pooled memory designated area specified with this function must be aligned to a 64 KiB boundary. The error `SCE_KERNEL_ERROR_EINVAL` is returned if this restriction is violated.
* Even if a protection that would permit access from the AMPR or ACP is specified with this function for a pooled memory designated area, doing so does not enable access from the AMPR/ACP.

## Notes

It is not possible to modify protections for areas mapped with the AMPR library using this function.

## See Also

`sceKernelMsync()`, `sceKernelMunmap()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMsync

Synchronize flexible memory with a backing store

## Definition

```
#include <kernel.h>
int sceKernelMsync(
    void *addr, 
    size_t len, 
    int flags
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Start virtual address of the area to synchronize |
| `len` | Size of the area to synchronize (bytes) |
| `flags` | Flag (see details below) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EBUSY` | 0x80020010 | `SCE_KERNEL_MS_INVALIDATE` is specified for `flags` |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `addr` is not aligned to the page boundary |
| `len` is too big |
| `flags` is invalid |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Flexible memory is not mapped to the ranged specified by `addr` and `len`. |

## Description

This function synchronizes flexible memory mapped to the specified virtual address area with a backing store, in other words saves flexible memory content to a backing store if it is changed.

For `addr` and `len`, specify the virtual address range you want to synchronize. `addr` must be aligned to the page boundary. By specifying 0 for `len`, the whole flexible memory area including `addr` will be specified.

For `flags`, specify the details of the function behavior with one of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MS_SYNC` | 0x0 | Return after saving to the backing store completes |
| `SCE_KERNEL_MS_ASYNC` | 0x1 | Return immediately without waiting for saving to the backing store |

* When `SCE_KERNEL_MS_SYNC` and `SCE_KERNEL_MS_ASYNC` are specified at the same time, only `SCE_KERNEL_MS_ASYNC` will be valid.
* Note that the value `SCE_KERNEL_MS_INVALIDATE` is defined in addition to the above values, but it cannot be used. When specified, an error will be returned.

## See Also

`sceKernelMprotect()`, `sceKernelMunmap()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMtypeprotect

Set protection and memory type

## Definition

```
#include <kernel.h>
int32_t sceKernelMtypeprotect(
    const void *addr, 
    size_t len,
    int type, 
    int prot
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Start virtual address of the area to set protection and memory type |
| `len` | Size of the area to set protection and memory type (bytes) |
| `type` | Memory type to set |
| `prot` | Protection to set (see details below) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | A more lenient protection than the access rights that previously have been permitted was specified |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Specified virtual address range is invalid |
| `type` or `prot` is invalid |
| `SCE_KERNEL_ERROR_EOPNOTSUPP` | 0x8002002d | A flexible memory area was specified |

## Description

This function changes memory protection and memory type.

For `addr` and `len`, specify the virtual address range. For `prot` and `type`, specify the protection and memory type.

Memory protection is performed in logical page units, and the specified protection (and memory type) will be applied for the logical pages including the specified range. Thus, an error will not be returned even if the specified range is not aligned to a 16 KiB boundary, and processing will be carried out by rounding to a page boundary.

For `prot`, specify the bitwise OR of the following values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |
| `SCE_KERNEL_PROT_AMPR_READ` | 0x40 | Permit reads from the AMPR |
| `SCE_KERNEL_PROT_AMPR_WRITE` | 0x80 | Permit writes from the AMPR |
| `SCE_KERNEL_PROT_AMPR_RW` | 0xc0 | Permit writes and reads from the AMPR |
| `SCE_KERNEL_PROT_ACP_READ` | 0x100 | Permit reads from the ACP |
| `SCE_KERNEL_PROT_ACP_WRITE` | 0x200 | Permit writes from the ACP |
| `SCE_KERNEL_PROT_ACP_RW` | 0x300 | Permit writes and reads from the ACP |

For `type`, specify one of the enum constants defined with `SceKernelMemoryType`.

Note the following points when changing the protection or memory type of a part of a pooled memory designated area using this function.

* A pooled memory designated area specified with this function must be aligned to a 64 KiB boundary. The error `SCE_KERNEL_ERROR_EINVAL` is returned if this restriction is violated.
* Even if a protection that would permit access from the AMPR or ACP is specified with this function for a pooled memory designated area, doing so does not enable access from the AMPR/ACP.

## Notes

It is not possible to modify protections or memory types for areas mapped with the AMPR library using this function.

## See Also

`sceKernelMsync()`, `sceKernelMunmap()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelMunmap

Unmap and release virtual address area

## Definition

```
#include <kernel.h>
int sceKernelMunmap(
    void *addr, 
    size_t len
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Start virtual address of the area to unmap (aligned to 16 KiB) |
| `len` | Size of the area to unmap (bytes) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `addr` is not aligned to the page boundary |
| 0 is specified for `len` |
| Invalid address is included in the specified virtual address area |
| Attempted to unmap a part of the pooled memory designated area that was reserved at once |

## Description

This function unmaps and releases a virtual address area. An area can be unmapped by calling this function, no matter the method used to map the area.

For `addr` and `len`, specify the virtual address range you want to unmap. `addr` must be aligned to the page boundary.

When unmapping a pooled memory designated area, all of the area reserved with one `sceKernelMemoryPoolReserve()` call must be unmapped. Automatic de-committing will also be performed on the entire unmapped area.

## Notes

* Do not use this function when performing another map without releasing the virtual address area; call a mapping function such as `sceKernelMapDirectMemory()`, with the `SCE_KERNEL_MAP_FIXED` flag specified. Also do not use this function when unmapping without releasing the virtual address area; call `sceKernelReserveVirtualRange()` with the `SCE_KERNEL_MAP_FIXED` flag specified. Because both of these processing are carried out atomically, there is no risk for the area to be mapped by another thread immediately after it is unmapped.
* When an area is accessed after unmapping, the "invalid memory access" error will occur.
* It is not possible to unmap areas mapped with the AMPR library using this function.

## See Also

`sceKernelMapDirectMemory()`, `sceKernelReserveVirtualRange()`, `sceKernelMemoryPoolReserve()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelQueryMemoryProtection

Get protection

## Definition

```
#include <kernel.h>
int32_t sceKernelQueryMemoryProtection(
    void *addr,
    void **start,
    void **end,
    int *prot
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Target virtual address |
| `start` | Destination to store start virtual address of the area with the same protection including `addr`, or NULL |
| `end` | Destination to store end virtual address of the area with the same protection including `addr`, or NULL |
| `prot` | Destination to store the obtained protection, or NULL |

## Return Values

For normal termination, stores the protection set for the virtual address `addr` in `*prot`, stores the start virtual address/end virtual address of the area set for the same protection including `addr` in `*start` and `*end`, and returns `SCE_OK` (=0).

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Memory is not mapped to `addr` |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `addr` is outside the virtual address space range |

## Description

This function queries the protection for the virtual address `addr`.

When a pointer that is not NULL is specified for `prot`, the protection set in `addr` will be stored in `*prot` as the bitwise OR of the following flags.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_PROT_CPU_READ` | 0x01 | Permit reads from the CPU |
| `SCE_KERNEL_PROT_CPU_RW` | 0x02 | Permit writes and reads from the CPU |
| `SCE_KERNEL_PROT_CPU_WRITE` | 0x02 | Permit writes and reads from the CPU (value for preserving compatibility) |
| `SCE_KERNEL_PROT_CPU_EXEC` | 0x04 | Permit instruction execution from the CPU |
| `SCE_KERNEL_PROT_GPU_READ` | 0x10 | Permit reads from the GPU |
| `SCE_KERNEL_PROT_GPU_WRITE` | 0x20 | Permit writes from the GPU |
| `SCE_KERNEL_PROT_GPU_RW` | 0x30 | Permit writes and reads from the GPU |
| `SCE_KERNEL_PROT_AMPR_READ` | 0x40 | Permit reads from the AMPR |
| `SCE_KERNEL_PROT_AMPR_WRITE` | 0x80 | Permit writes from the AMPR |
| `SCE_KERNEL_PROT_AMPR_RW` | 0xc0 | Permit writes and reads from the AMPR |
| `SCE_KERNEL_PROT_ACP_READ` | 0x100 | Permit reads from the ACP |
| `SCE_KERNEL_PROT_ACP_WRITE` | 0x200 | Permit writes from the ACP |
| `SCE_KERNEL_PROT_ACP_RW` | 0x300 | Permit writes and reads from the ACP |

When a pointer that is not NULL is specified for `start` and `end`, the start virtual address/end virtual address for the area with the same protection as `addr` set including `addr` will be stored in `*start` and `*end`.

When NULL is specified for one or all of `prot`, `start`, and `end`, an error will not occur for the function call, and the results will not be stored in the argument with NULL specified. For example, if only the protection value is required, it is possible to specify a pointer that is not NULL for `prot` with NULL specified for `start` and `end`.

## Notes

* The protection set for the virtual address (`*start` - 1) and the protection set for `*start` are not always different.
* It is not possible to use this function on areas mapped with the AMPR.

## See Also

`sceKernelMprotect()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelReleaseDirectMemory

Release direct memory

## Definition

```
#include <kernel.h>
int32_t sceKernelReleaseDirectMemory(
    off_t start,
    size_t len
)
```

## Arguments

|  |  |
| --- | --- |
| `start` | Start physical address of the direct memory to release (aligned to 16 KiB) |
| `len` | Size of the direct memory to release (bytes, multiple of 16 KiB) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | One of the arguments is invalid |

## Description

This function releases direct memory allocated with `sceKernelAllocateDirectMemory()`/`sceKernelAllocateMainDirectMemory()`.

The range of memory from `start` to `start`+`len` will be released (without checking whether or not an unallocated area is included).

The range to be released does not have to match the range allocated with `sceKernelAllocateDirectMemory()`/`sceKernelAllocateMainDirectMemory()`. It is also possible for memory mapped with `sceKernelMapDirectMemory()` to be included. In this case, the area will be unmapped.

## Examples

```
size_t memLen = 2 * 1024 * 1024; // Length: 2 MiB
size_t memAlign = 64 * 1024; // Alignment: 64 KiB

// Allocate 2 MiB direct memory
off_t memStart;
if ( sceKernelAllocateDirectMemory( 0,
    SCE_KERNEL_MAIN_DMEM_SIZE, memLen, memAlign,
    SCE_KERNEL_MTYPE_C_SHARED, &memStart) < 0 ) {
        // Error handling
}

// Release 2 MiB direct memory
if ( sceKernelReleaseDirectMemory( memStart, memLen ) < 0 ) {
        // Error handling
}
```

## See Also

`sceKernelAllocateDirectMemory()`, `sceKernelAllocateMainDirectMemory()`, `sceKernelCheckedReleaseDirectMemory()`

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

# sceKernelReserveVirtualRange

Reserve virtual address area

## Definition

```
#include <kernel.h>
int sceKernelReserveVirtualRange(
    void **addr,
    size_t len,
    int flags,
    size_t alignment
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Input: virtual address to begin searching for free space  Output: start virtual address of the reserved area |
| `len` | Size of the area to reserve (bytes, multiple of 16 KiB) |
| `flags` | Flags (see details below), or 0 |
| `alignment` | Alignment of the reserve destination (only valid when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`; multiple of 16 KiB and a power of 2), or 0 |

## Return Values

Stores the start virtual address in `*addr` and returns `SCE_OK` (=0) for normal termination.

If the virtual memory area reserving succeeds but an access rights violation occurs when storing the start address in `*addr`, the program will abnormally terminate.

Returns one of the following error codes (a negative value) for other errors.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `*addr` is not aligned to the page boundary, or a virtual address outside of the usable area is specified (only when `SCE_KERNEL_MAP_FIXED` is specified for `flags`) |
| `len` is not a multiple of 16 KiB, or it is 0 |
| `flags` is not 0, not a correct flag value, nor the bitwise OR of correct flag values |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Area that is being used is included in the range specified with `*addr` and `len` (when `SCE_KERNEL_MAP_FIXED` and `SCE_KERNEL_MAP_NO_OVERWRITE` are specified for `flags`) |
| No free space found (when `SCE_KERNEL_MAP_FIXED` is not specified for `flags`) |
| Insufficient memory |

## Description

This function allocates a virtual address area without mapping memory. After allocating a virtual address area with this function, call `sceKernelMapDirectMemory()` with the `SCE_KERNEL_MAP_FIXED` flag specified to map memory to the area.

For `flags`, specify the bitwise OR of the following flags. Specify 0 if not required.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_MAP_FIXED` | 0x0010 | Fix reserve destination to `*addr` |
| `SCE_KERNEL_MAP_NO_OVERWRITE` | 0x0080 | Prohibit reserving when an area that is being used is included in the range specified with `*addr` and `len` |
| `SCE_KERNEL_MAP_NO_COALESCE` | 0x400000 | Instruct `sceKernelVirtualQuery()` not to merge neighboring areas |

* If `SCE_KERNEL_MAP_FIXED` is specified, the virtual address area from `*addr` to `*addr`+`len` will be reserved. When reserving/mapping/locking has already been performed within this area, the `SCE_KERNEL_ERROR_ENOMEM` error will occur if `SCE_KERNEL_MAP_NO_OVERWRITE` is specified. If that value is not specified, the overlapping portion will be automatically unreserved/unmapped/unlocked, and reserving of the specified area will subsequently be performed.
* If `SCE_KERNEL_MAP_FIXED` is not specified free space of the size `len` bytes and aligned to the page boundary will be searched in the upward direction starting with the virtual address pointed to by `*addr` according to the value specified for `alignment`; and the first area found will be reserved. If specifying a reserve destination is not required, specify 0 for `*addr`.
* If `SCE_KERNEL_MAP_NO_COALESCE` is specified, areas will not be merged (neighboring areas with the same characteristics will not be handled as one area) upon the call of `sceKernelVirtualQuery()`.

## See Also

`sceKernelMunmap()`

# sceKernelSetPrtAperture

Set PRT aperture

## Definition

```
#include <kernel.h>
int32_t sceKernelSetPrtAperture(
    int apertureId,
    void *addr,
    size_t len
)
```

## Arguments

|  |  |
| --- | --- |
| `apertureId` | ID of the aperture to set (0 to 2) |
| `addr` | Start virtual address of the aperture area (aligned to 16 KiB) |
| `len` | Size of the aperture area (bytes, multiple of 16 KiB) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Invalid aperture ID is specified |
| Invalid area is specified |
| Start or end of the area is not aligned to the page boundary |

## Description

This function sets the start virtual address and size of a PRT (partially resident texture) aperture. An arbitrary range within the user area of the virtual address space can be set as the PRT aperture.

A PRT aperture is an area where page faults are restricted during texture fetching by the GPU. Of the four hardware PRT apertures, the PlayStation®5 kernel provides three to the application program.

## Notes

* The start address and size of the user area are defined with `SCE_KERNEL_APP_MAP_AREA_START_ADDR` and `SCE_KERNEL_APP_MAP_AREA_SIZE`.
* It is not possible to use this function on areas mapped with the AMPR.

# sceKernelSetVirtualRangeName

Set name to the memory area mapped to a virtual address

## Definition

```
#include <kernel.h>
int32_t sceKernelSetVirtualRangeName(
    const void *addr,
    size_t len,
    const char *name
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Target virtual address |
| `len` | Size of the target area (bytes) |
| `name` | Name to set (up to 32 bytes including the NULL-terminator character) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | Range specified with `addr` and `len` is outside the virtual address space range |
| `SCE_KERNEL_ERROR_ENOMEM` | 0x8002000c | Attempted to set a number of name entries exceeding 4096 to the AMM virtual address space |
| `SCE_KERNEL_ERROR_ENAMETOOLONG` | 0x8002003f | `name` character string exceeds 32 bytes |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `name` points to invalid memory or is NULL |

## Description

This function sets a name to the memory mapped in the range of `len` bytes from the `addr` virtual address. A name change is performed in logical page units, and a name will be set for the logical pages including the specified range. The set name can be obtained with `sceKernelVirtualQuery()`.

When calling this function for the AMM virtual address space that can be obtained with `sce::Ampr::Amm::getVirtualAddressRanges()`, a name can be set to the specified range even if memory has not been mapped. If memory is mapped to an area with a name already set, that name can be obtained with `sceKernelVirtualQuery()`.

An error will not occur even if an area where memory other than that of the virtual address space is not mapped, but a name will not be set to such an area.

## See Also

`SceKernelVirtualQueryInfo`, `sceKernelClearVirtualRangeName()`

# sceKernelVirtualQuery

Obtain information about the memory area mapped to a virtual address

## Definition

```
#include <kernel.h>
int32_t sceKernelVirtualQuery(
    const void *addr,
    int flags,
    SceKernelVirtualQueryInfo *info,
    size_t infoSize
)
```

## Arguments

|  |  |
| --- | --- |
| `addr` | Target virtual address |
| `flags` | Flag (see details below) |
| `info` | Destination to store the obtained information |
| `infoSize` | Information size. Specify `sizeof(SceKernelVirtualQueryInfo)` |

## Return Values

Stores the information about the memory mapped to the virtual address `addr` in `*info` and returns `SCE_OK`(=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EACCES` | 0x8002000d | Memory is not mapped to `addr` |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `info` points to invalid memory |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `addr` is outside the virtual address space range |

## Description

This function queries the memory mapped to the virtual address `addr`.

Information about the mapped memory will be stored in `info`.

For `flags`, specify one of the following values that indicate the details of the function behavior.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
|  | 0 | If memory is not mapped to the virtual address `addr`, immediately return the `SCE_KERNEL_ERROR_EACCES` error |
| `SCE_KERNEL_VQ_FIND_NEXT` | 1 | If memory is not mapped to the virtual address `addr`, obtain information about the next memory area. When the next memory area does not exist, return the `SCE_KERNEL_ERROR_EACCES` error |

When the characteristics of an area containing the specified virtual address match the characteristics of a neighboring area, this function may handle these areas as one area and return a result for the combined area. If this behavior is not preferable, specify the `SCE_KERNEL_MAP_NO_COALESCE` flag upon mapping the area.

In addition, this function only returns information of the area explicitly mapped by the application or the SDK library and information of the stack area created by the system. Because some SDK APIs may consume memory without entailing a map to the accessible area, it is not possible to precisely obtain the total size of memory being consumed by the application with this function. To obtain the remaining size of available flexible memory and direct memory, use `sceKernelAvailableFlexibleMemorySize()` and `sceKernelAvailableDirectMemorySize()`.

## See Also

[Kernel Overview - Memory Management](../Kernel-Overview/memory-management.html)

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.