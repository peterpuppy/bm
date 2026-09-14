# Kernel Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Overview/pooled-memory.html

# Memory Management

# Overview

The PlayStation®5 kernel provides an exclusive virtual address space for each process. Both programs that run on the CPU and shaders that run on the GPU will run in the same virtual address space.

## Memory Accessible by Applications (Direct Memory)

Application programs can map and access direct memory in the virtual address space. Direct memory is consecutive areas of physical memory that can be accessed by application programs. With direct memory, memory allocation/mapping with awareness of its location in the physical address space is possible, and its use is effective where you want to improve performance by considering DRAM characteristics. For details about usage, refer to "[Direct Memory](direct-memory.html)".

**Asynchronous Memory Mapper (AMM)**

Also provided in PlayStation®5 is a feature, Asynchronous Memory Mapper (AMM), that uses dedicated hardware to map and unmap memory rapidly in the virtual address space. Application programs can use the AMM library to put direct memory of a specified size under the management of the AMM and perform mapping, unmapping, and other processing of that memory rapidly and asynchronously. For details, refer to the [AMPR Libraries Overview](../AMPR-Overview/__document_toc.html) document.

**Memory Pool**

The PlayStation®5 kernel provides a scheme called the memory pool that automatically partitions a section of direct memory into 64-KiB blocks and manages them. Application programs can place memory (called "pooled memory") in units of 64 KiB onto a specified area within the virtual address space or remove memory that has been so placed without having to be aware of physical addresses. When there is no need to be aware of the physical address, pooled memory is easier to use, compared to direct manipulation of direct memory, and performs well. For details about usage, refer to "[Pooled Memory](pooled-memory.html)".

## Memory Used by the System (Flexible Memory)

In addition to direct memory, the system maps to virtual address spaces "flexible memory" that is primarily used for the following purposes:

* TEXT segments (segments that include a .text section)
* Static data areas
  + DATA segments (segments that include a .bss section or a .data section)
  + RODATA segments (segments that include a .rodata section)
  + RELRO segments (segments that include a .got section)
* Stack areas
* Other memory used internally by the system

## Memory Allocated to an Application and the Assignment of That Memory

An application is allocated 12.5 GiB of physical memory by the system.

* On Development Kits with the Release Check Mode set to Development Mode, it's possible to allocate physical memory of up to 24.25 GiB using ★Debug Settings. (Refer to the [Tool Memory Overview](../Tool_Memory-Overview/__document_toc.html) document for details.)
* In addition to the 12.5 GiB (up to 24.45 GiB in Development Mode) mentioned above, an application running in Trinity mode is further allocated with 1216 MiB of physical memory.

Memory allocated by the system to an application is assigned for the following purposes:

* Direct memory
  + The size of direct memory will be the difference between the above memory size allocated by the system minus the total size of the memory areas listed below
  + An application that is running in Trinity mode is allocated 1216 MiB more memory (as mentioned above) than an application that is running in Base mode, and the surplus memory is allocated as direct memory. For details, refer to [Programming Startup Guide - Resources That Can Be Used by Applications - Memory](../Programming-Startup_Guide/ps5-memory.html).
* Flexible memory
  + Default size: 448 MiB, maximum size: 1 GiB (for modes other than Development Mode) and 2 GiB (for Development Mode)
* The file system buffer cache dedicated to the application (fixed at 64 MiB)
* Any increase from the default amount (64 MiB) of the page table pool for the CPU
* Any increase from the default amount (64 MiB) of the page table pool for the GPU
* Any increase from the default amount (64 MiB) of the page table pool for the AMM

Memory assignment is determined by the system when the application is launched. These memory assignments can be customized with a parameter file (param.json). For details, refer to the "[Customization of Memory Assignment](customization-of-memory-assignment.html)" section. If no customization is performed, the default amounts of memory for each purpose will be assigned.

Once memory assignments have been determined at startup, there will be no changes to those assignments until the application is later terminated. Note, especially, that memory assignment does not change when calling `sceSystemServiceLoadExec()`.

For information about the amount of memory that can be used by an application, also refer to [Programming Startup Guide - Resources That Can Be Used by Applications - Memory](../Programming-Startup_Guide/ps5-memory.html). Two functions are provided for obtaining the amount of memory that is available while an application is running: `sceKernelAvailableDirectMemorySize()` and `sceKernelAvailableFlexibleMemorySize()`.

There are libraries that, upon being used (loaded), allocate direct or flexible memory that has been allocated to an application; be aware of this when estimating the amount of memory that an application will use.

# Memory Mapping in the Virtual Address Space

Memory mapping in the virtual address space is shown in the following figure.

Memory Mapping in the Virtual Address Space

The system determines memory placement within the system managed area. Although the system manages placement, this memory is for application programs. Memory will be placed in this area when 0 is specified to the `addr` argument of `sceKernelMapDirectMemory()`.

Memory required for system program operation is placed in the system reserved areas. Examples of this include the system's dynamic libraries (excluding those included in application packages). Application programs must not directly access memory within these areas.

Application programs can freely place memory in the user area. Unless the application explicitly instructs it, libraries provided by SIE will not place memory in this area. The `SCE_KERNEL_APP_MAP_AREA_START_ADDR` and `SCE_KERNEL_APP_MAP_AREA_END_ADDR` macros are provided to represent the start address and end address of this area, respectively.

# Logical Pages

The PlayStation®5 kernel manages memory in 16-KiB memory units called logical pages. A logical page consists of four physical pages (4 KiB) supported by the CPU and bundled together.

Note:

In this document and the [Kernel Reference](../Kernel-Reference/__document_toc.html) document, unless there is a need to distinguish from a physical page, a logical page is simply described as a "page". Assume that, unless otherwise specified, expressions such as "page boundary" and "page unit" refer to logical pages.

# Direct Memory

## Physical Address Space and Direct Memory Areas

Direct memory assigned to application programs exists in consecutive areas in a physical address space. In addition, the beginning of these areas is guaranteed to be aligned to a 2 MiB boundary.

Direct memory comprises a single consecutive area beginning from physical address 0. The size is defined with the `SCE_KERNEL_MAIN_DMEM_SIZE` macro.

## Allocating Direct Memory

Direct memory is allocated by calling `sceKernelAllocateDirectMemory()`.

The basic usage entails searching for free memory and allocating direct memory by specifying the direct memory range, the size to allocate, and the alignment. The following specification example shows how to search the entire main memory for free memory and allocate 1 MiB of direct memory that is aligned to a 128 MiB boundary.

```
const size_t mem_size = 1 * 1024 * 1024; // Size: 1 MiB
const size_t align = 128 * 1024 * 1024; // Alignment: 128 MiB
const int mem_type = SCE_KERNEL_MTYPE_C_SHARED;
int32_t ret = sceKernelAllocateDirectMemory(0,
        SCE_KERNEL_MAIN_DMEM_SIZE, 
        mem_size, align, mem_type, &dmem_start);
```

If you want to explicitly manage direct memory allocation, it is possible to narrow the specification range.

```
const size_t align = 16 * 1024; // Alignment: 16 KiB
int32_t ret = sceKernelAllocateDirectMemory(0,
        mem_size, 
        mem_size, align, mem_type, &dmem_start);
```

## Mapping Direct Memory

To access direct memory allocated with `sceKernelAllocateDirectMemory()`, it is necessary to call `sceKernelMapDirectMemory()` and map the memory in a virtual address space.

```
void* start_addr = 0;
int32_t ret = sceKernelMapDirectMemory(&start_addr, map_size, prot, 0,
        dmem_start, align);
```

Memory allocated by one `sceKernelAllocateDirectMemory()` call is not necessarily mapped by one `sceKernelMapDirectMemory()` call. It is also possible to map only a section of the direct memory or map direct memory allocated with multiple calls at one time.

## Releasing Direct Memory

To release direct memory, call `sceKernelCheckedReleaseDirectMemory()`.

```
int32_t ret = sceKernelCheckedReleaseDirectMemory(start, len);
```

The beginning/end of the direct memory to be released does not have to match the beginning/end when it was allocated. If the released direct memory was mapped in a virtual address space, it will all be unmapped.

## Efficiency Using Batch Functions

`sceKernelBatchMap()` and `sceKernelBatchMap2()` are both functions that execute multiple operations in a batch. Operations that can be processed as a batch are listed below; it is more efficient to use these functions rather than a group of functions corresponding to each operation.

* Map direct memory (equivalent to `sceKernelMapDirectMemory()`)
* Unmap (equivalent to `sceKernelMunmap()`)
* Change protection (equivalent to `sceKernelMprotect()`)
* Change protection and memory type (equivalent to `sceKernelMtypeprotect()`)

Upon using `sceKernelBatchMap()`/`sceKernelBatchMap2()`, prepare an array of the operations to carry out. In the example below, an area of `size1` bytes starting from the `ptr1` variable and an area of `size2` bytes starting from the `ptr2` variable are unmapped.

```
SceKernelBatchMapEntry entries[2];
SceKernelBatchMapEntry *entp = entries;

entp->operation = SCE_KERNEL_MAP_OP_UNMAP;
entp->start = ptr1;
entp->length = size1;
++entp;

entp->operation = SCE_KERNEL_MAP_OP_UNMAP;
entp->start = ptr2;
entp->length = size2;
++entp;

int count;
int32_t error = sceKernelBatchMap(entries, entp - entries,
&count);
```

To maximize the effects of batch processing, make specifications so that the same operation is placed in succession within the array as much as possible. This will enable optimization by skipping the processing to invalidate the CPU/GPU TLB and optimization of the CPU cache invalidation using the wbinvd instruction.

## Process Termination and Direct Memory

When a process terminates, all direct memory allocated by the process will be released.

# Pooled Memory

A [memory pool](overview-2.html#kernel-overview_3_1__p_dhr_l13_hgc), which is a scheme that manages pooled memory, is provided per process. Various types of memory pool functions can be called to perform operations on a memory pool, as exemplified below.

* Expanding the memory pool (direct memory is allocated and added under the management of the memory pool)
* Committing pooled memory (unused memory under the management of the memory pool is searched for and placed onto a virtual address space)
* De-committing pooled memory (memory placement onto the virtual address space is canceled and the memory is returned to be under the management of the memory pool again)

Note that the AMPR and the ACP do not support reading from, and writing to, pooled memory.

## Expanding the Memory Pool

The memory pool is empty immediately after process startup. Call `sceKernelMemoryPoolExpand()` to add physical memory under memory pool management. Specify the range of direct memory, size to allocate, and the alignment; free memory within that range will be searched for and allocated.

The following specification example shows how to search the entire main memory for free memory and add 4 GiB of direct memory that is aligned to a 64 KiB boundary to the memory pool.

```
off_t searchStart = 0; // Start physical address of the direct memory
off_t searchEnd = SCE_KERNEL_MAIN_DMEM_SIZE; // End physical address of the direct memory
size_t len = 4UL * 1024 * 1024 * 1024; // Allocate 4 GiB
size_t alignment = 64 * 1024; // Align to 64 KiB boundary
off_t startOff; // Start physical address of the direct memory area added to the memory pool

int32_t error = sceKernelMemoryPoolExpand(searchStart, searchEnd, len, alignment, &startOff);
```

Note that pooled memory - in other words, direct memory added to the memory pool - cannot be used as normal direct memory until the process terminates.

Memory pool expansion entails a large cost compared to the committing/de-committing of pooled memory. In addition, it is an operation for which execution time is often prolonged because it is affected by processing being executed by another CPU. Thus, prepare sufficient amount of pooled memory upon initialization processing, for example, and avoid having to perform expansion at sections where real-time processing is required.

## Reserving a Pooled Memory Designated Area

`sceKernelMemoryPoolReserve()` must be called before committing pooled memory to reserve an area for placing the pooled memory (in other words, a pooled memory designated area) onto the virtual address space.

The following specification example shows how to search for 16 GiB of free space from the start of the user area and reserve it as the pooled memory designated area.

```
void *searchStart = (void *)SCE_KERNEL_APP_MAP_AREA_START_ADDR; // Start of the user area
size_t len = 16UL * 1024 * 1024 * 1024; // Reserve 16 GiB
size_t alignment = 0; // Default alignment (2 MiB)
void *areaPtr;

int32_t error = sceKernelMemoryPoolReserve(searchStart, len, alignment, /* flags */ 0, &areaPtr);
```

A page table is not required for reserving an area; however, memory will be required for managing pooled memory placement. For this memory, 1 block (64 KiB) will be allocated from the memory pool for each 1 GiB of pooled memory designated area to reserve.

Pooled memory designated area reservation entails a large cost compared to the committing/de-committing of pooled memory. In addition, it is an operation for which execution time is often prolonged because it is affected by processing being executed by another CPU. Thus, reserve a sufficient amount of pooled memory designated area upon initialization processing and avoid having to perform reservation at sections where real-time processing is required.

## Committing Pooled Memory

`sceKernelMemoryPoolCommit()` can be called to search the memory pool for unused physical memory blocks and they can be placed (committed) to the virtual address space reserved as the pooled memory designated area. At this time, the protection mask and memory type can be specified.

The following specification example shows how to allocate 16 blocks (total 1 MiB) from the memory pool and place them within 1 MiB from the start of the user area on the virtual address space. It is assumed that pooled memory designated area of a sufficient size is reserved from the start of the user area.

```
size_t len = 1UL * 1024 * 1024; // Size is 1 MiB (16 blocks)
int type = SCE_KERNEL_MTYPE_C_SHARED;
int prot = SCE_KERNEL_PROT_CPU_RW | SCE_KERNEL_PROT_GPU_RW; // Read/write-enabled from the CPU and GPU
void *addr = (void *)SCE_KERNEL_APP_MAP_AREA_START_ADDR; // Start of the user area

int32_t error = sceKernelMemoryPoolCommit(addr, len, type, prot, /* flags */ 0);
```

`sceKernelMemoryPoolCommit()` prioritizes the search for a free block that matches the specified memory type and allocates it. If such a block does not exist, a block of the required type will be created by flushing the CPU cache.

Note that an error will occur if a committed area already exists within the specified virtual address range.

## De-committing Pooled Memory

`sceKernelMemoryPoolDecommit()` can be called to cancel the placement (committing) of the physical memory block onto the virtual address space within the pooled memory designated area.

The following specification example shows how to de-commit an area of 1 MiB from the start of the user area.

```
size_t len = 1UL * 1024 * 1024; // Size is 1 MiB (16 blocks)
void *addr = (void *)SCE_KERNEL_APP_MAP_AREA_START_ADDR; // Start of the user area
int32_t error = sceKernelMemoryPoolDecommit(addr, len, /* flags */ 0);
```

The range to de-commit does not have to match the committed range as long as the area is aligned to a 64 KiB boundary. For example, it is possible to commit an area of 1 MiB and to de-commit just the final 64 KiB of that area. Additionally, even if an area that has not been committed is included, a de-committing operation for the specified range can be carried out as long as the target area is within one pooled memory designated area.

## Efficiency Using a Batch Function

`sceKernelMemoryPoolBatch()` is a function that executes multiple operations in a batch. Operations that can be processed as a batch are listed below; it is more efficient to use this function rather than a group of functions corresponding to each operation.

* Commit (equivalent to `sceKernelMemoryPoolCommit()`)
* De-commit (equivalent to `sceKernelMemoryPoolDecommit()`)
* Change protection (equivalent to `sceKernelMprotect()`)
* Change protection and memory type (equivalent to `sceKernelMtypeprotect()`)
* Move (equivalent to `sceKernelMemoryPoolMove()`)

Upon using `sceKernelMemoryPoolBatch()`, prepare an array of the operations to carry out. In the example below, an area of `size1` bytes starting from the `ptr1` variable and an area of `size2` bytes starting from the `ptr2` variable are committed.

```
SceKernelMemoryPoolBatchEntry entries[2];
SceKernelMemoryPoolBatchEntry *entp = entries;

entp->op = SCE_KERNEL_MEMORY_POOL_OP_COMMIT;
entp->flags = 0;
entp->commit.addr = ptr1;
entp->commit.len = size1;
entp->commit.prot = SCE_KERNEL_PROT_CPU_RW;
entp->commit.type = SCE_KERNEL_MTYPE_C_SHARED;
++entp;

entp->op = SCE_KERNEL_MEMORY_POOL_OP_COMMIT;
entp->flags = 0;
entp->commit.addr = ptr2;
entp->commit.len = size2;
entp->commit.prot = SCE_KERNEL_PROT_CPU_RW;
entp->commit.type = SCE_KERNEL_MTYPE_C_SHARED;
++entp;

int count;
int32_t error = sceKernelMemoryPoolBatch(entries, entp - entries,
&count, /* flags */ 0);
```

To maximize the effects of batch processing, make specifications so that the same operation is placed in succession within the array as much as possible. This will enable optimization by skipping the processing to invalidate the CPU/GPU TLB and optimization of the CPU cache invalidation using the wbinvd instruction.

## Operation on a Pooled Memory Designated Area by Other Memory Management Functions

It is possible to use memory management functions other than `sceKernelMemoryPool*()` on a pooled memory designated area. However, the pooled memory designated area has the following restrictions that differ from the restrictions of other virtual address areas, in addition to not being accessible from the AMPR or from the ACP:

* It is not possible to remove just a part of the pooled memory designated area. Make sure that all of the area reserved in one call of `sceKernelMemoryPoolReserve()` is removed.

  For example, attempting to use `sceKernelMunmap()` and unmap a part of the area that was reserved at once will result in an error. It is also not possible to use `sceKernelMapDirectMemory()` with the `SCE_KERNEL_MAP_FIXED` flag specified to replace a part of the area that was reserved at once with a direct memory map.
* The range to change protection or memory type must be aligned to a 64 KiB boundary.

# Memory Access Control by the CPU/GPU/AMPR

## Protection

The PlayStation®5 kernel memory protection mechanism is a GPU expansion provided in addition to the memory protection mechanism that POSIX is equipped with.

For POSIX, the following protection masks can be set for each page.

* `SCE_KERNEL_PROT_CPU_READ`: can be read by the CPU
* `SCE_KERNEL_PROT_CPU_RW`: can be written and read by the CPU

For the PlayStation®5 kernel, the following protection masks can be set in addition to those above.

* `SCE_KERNEL_PROT_GPU_READ`: can be read by the GPU
* `SCE_KERNEL_PROT_GPU_WRITE`: can be written by the GPU
* `SCE_KERNEL_PROT_GPU_RW`: can be written and read by the GPU
* `SCE_KERNEL_PROT_AMPR_READ`: can be read by the AMPR
* `SCE_KERNEL_PROT_AMPR_WRITE`: can be written by the AMPR
* `SCE_KERNEL_PROT_AMPR_RW`: can be written and read by the AMPR
* `SCE_KERNEL_PROT_ACP_READ`: can be read by the ACP
* `SCE_KERNEL_PROT_ACP_WRITE`: can be written by the ACP
* `SCE_KERNEL_PROT_ACP_RW`: can be written and read by the ACP

The memory protection can be set/changed by specifying the bitwise OR of these protection mask values using a function such as `sceKernelMapDirectMemory()`, `sceKernelMprotect()`, or `sceKernelMemoryPoolCommit()`.

## Memory Types

The memory type indicates the cache operation mode.

There are two methods for memory access by the CPU: WB (write-back) and WC (write-combining); however, the current SDK only supports WB. Additionally, you can specify GL2 MTYPE values in regard to memory access by the GPU.

These combinations are defined as the `SceKernelMemoryType` enumeration as follows. For details about memory types, refer to [GPU Overview - GPU Cache Hierarchy - GL2 Cache and Memory Types](../GPU-Overview/gl2-cache-and-memory-types.html).

```
typedef enum {
  SCE_KERNEL_MTYPE_C = 11,           // CPU: WB, GL2 MTYPE: cached, R/W, not shared
  SCE_KERNEL_MTYPE_C_SHARED,    // CPU: WB, GL2 MTYPE: cached, R/W, shared
} SceKernelMemoryType;
```

The memory type can be set/changed by making the specification using a function such as `sceKernelAllocateDirectMemory()`, `sceKernelMapDirectMemory2()`, `sceKernelMtypeprotect()`, or `sceKernelMemoryPoolCommit()`.

The use of `SCE_KERNEL_MTYPE_C_SHARED` is recommended.

The memory type for each segment of executable files and PRX files is fixed at 0 and cannot be changed. Memory type 0 behaves the same as `SCE_KERNEL_MTYPE_C_SHARED`.

## PRT Aperture

The PRT (partially resident texture) aperture is a virtual address space where the page faults that occur during texture fetching by the GPU are restricted.

Application programs can use up to three PRT apertures. PRT apertures can be set with a desired range for the user area in a virtual address space (defined as `SCE_KERNEL_APP_MAP_AREA_{START_ADDR, SIZE}`) by calling `sceKernelSetPrtAperture()`.

```
// Set PRT aperture to [addr, addr + len)
int32_t ret = sceKernelSetPrtAperture(apertureId, addr, len);
```

The argument `apertureId` specifies which of the three PRT apertures will be used. Specify a value from 0 to 2. The virtual address and size must be multiples of the logical page size (16 KiB).

# Note Regarding Memory Access Performance in Each of the Application's Operation Modes

The performance characteristics of the page table differ somewhat between an application that is running in Trinity mode and an application that is running in Base mode. Consequently, an application can achieve memory access performance equivalent to or better than Base mode in most use cases. However, there are rare cases in which mapping processing is performed more slowly than in Base mode. An example of processing to which this caveat applies is processing to map an area that is not aligned to 2 MiB to a broad range.

It is likely that this will almost never cause any practical issues, but you should be pay attention to this fact when implementing an application with particular awareness of the differences in performance compared to Base mode.

# How to Calculate the Memory Consumption of a Program

The PlayStation®5 kernel allocates the memory required by each segment of an execution entity or dynamic library in 16-KiB increments. The memory size required to load an execution entity/dynamic library can be calculated from the information obtained by executing the `prospero-llvm-readelf` command.

When the ELF file for an execution entity/dynamic library is specified for `prospero-llvm-readelf --program-headers`, segment information for the ELF file is displayed. The amount of memory consumed by the ELF file and any dynamic libraries is the value equal to the total of the sizes of the segments, aligned to 16 KiB, that are displayed in the MemSiz column and that match all the following conditions.

* The Type column is LOAD or GNU\_RELRO
* The Flg column is one of E, R, or RW
* The virtual address range of the segment is not included in any other segments

Thus, the value of this total is the required flexible memory size, which is the memory size required to load the execution entity and any dynamic libraries.

For details about the `prospero-llvm-readelf` command, refer to the "prospero-llvm-readelf User's Guide" document.

**Example: Results of Displaying Segments for a "Hello World" Program with the prospero-llvm-readelf Command**

Memory is consumed when the segments marked with "<==THIS" are executed. Total memory consumption is 16 KiB + 16 KiB + 16 KiB + 16 KiB = 64 KiB.

```
f:\>prospero-llvm-readelf -l hello.elf
Elf file type is SCE_DYNEXEC
Entry point 0x70
There are 14 program headers, starting at offset 64
Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  LOAD           0x004000 0x0000000000000000 0x0000000000000000 0x0001ac 0x0001ac   E 0x4000 <== THIS
  LOAD           0x008000 0x0000000000004000 0x0000000000004000 0x000083 0x000083 R   0x4000 <== THIS
  GNU_EH_FRAME   0x008000 0x0000000000004000 0x0000000000004000 0x00001c 0x00001c R   0x4
  LOAD           0x00c000 0x0000000000008000 0x0000000000008000 0x000338 0x000338 RW  0x4000
  GNU_RELRO      0x00c000 0x0000000000008000 0x0000000000008000 0x000338 0x004000 R   0x1    <=== THIS
  TLS            0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 R   0x0
  SCE_PROCPARAM  0x00c2d8 0x00000000000082d8 0x00000000000082d8 0x000060 0x000060 R   0x8
  LOAD           0x010000 0x000000000000c000 0x000000000000c000 0x000021 0x000021 RW  0x4000 <=== THIS
  LOAD           0x010030 0x000000000000c030 0x000000000000c030 0x000550 0x000550     0x4000
  NOTE           0x010328 0x000000000000c328 0x000000000000c328 0x000024 0x000024     0x4
  DYNAMIC        0x010350 0x000000000000c350 0x000000000000c350 0x000230 0x000230 RW  0x8
  SCE_COMMENT    0x010580 0x0000000000000000 0x0000000000000000 0x00002c 0x000000     0x10
  SCE_LIBVERSION 0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000     0x0
  NOTE           0x0105ac 0x0000000000000000 0x0000000000000000 0x000018 0x000000     0x4
```

# Customization of Memory Assignment

As described in "[Memory Allocated to an Application and the Assignment of That Memory](overview-2.html#kernel-overview_3_1__kernel-overview_3_1_3)", the assignment of physical memory allocated to an application is determined by the system when the application program is launched; however, this assignment can be customized by setting parameters within param.json. Specifically, the memory sizes below can be set.

* [Flexible Memory Size](customization-of-memory-assignment.html#kernel-overview_3_9__kernel-overview_3_9_1)
* [CPU Page Table Pool Size](customization-of-memory-assignment.html#kernel-overview_3_9__kernel-overview_3_9_2)
* [GPU Page Table Pool Size](customization-of-memory-assignment.html#kernel-overview_3_9__kernel-overview_3_9_3)
* [AMM Page Table Pool Size](customization-of-memory-assignment.html#kernel-overview_3_9__kernel-overview_3_9_4)

The set values are applied by the system when the application is launched, and the size of direct memory is modified accordingly.

In addition to the above, [Size of the AMM Virtual Address Space](customization-of-memory-assignment.html#kernel-overview_3_9__kernel-overview_3_9_5) is also customizable.

The parameters that can be used for customization and examples of how they might be set in param.json are provided below.

## Flexible Memory Size

```
{
    ....
    "kernel": {
       "flexibleMemorySize": 402653184
    }
}
```

kernel/flexibleMemorySize is a parameter that specifies the size of flexible memory. The size is in byte units. The maximum value is 1073741824 (1024 MiB) for modes other than the Development Mode and 2147483648 (2048 MiB) for the Development Mode. The minimum value is 2097152 (2 MiB). A multiple of 2 MiB must be specified. If the parameter is omitted (or 0 is specified), it will be interpreted as though the default size of 469762048 (448 MiB) was specified.

## CPU Page Table Pool Size

```
{
    ....
    "kernel": {
        "cpuPageTableSize": 134217728
    }
}
```

kernel/cpuPageTableSize is a parameter that specifies the size of the CPU page table pool used for a non-AMM area. The unit is bytes, the maximum value is 268435456 (256 MiB), and the minimum value is 67108864 (64 MiB). A multiple of 2 MiB must be specified. If the parameter is omitted (or 0 is specified), it will be interpreted as though the default size of 67108864 (64 MiB) was specified.

For every 2 MiB that the CPU page table pool is increased, 512 page table entries are added. This is equivalent to the page table volume required for mapping 1 GiB of memory.

## GPU Page Table Pool Size

```
{
    ....
    "kernel": {
        "gpuPageTableSize": 134217728
    }
}
```

kernel/gpuPageTableSize is a parameter that specifies the size of the GPU page table pool used for a non-AMM area. The unit is bytes, the maximum value is 268435456 (256 MiB), and the minimum value is 67108864 (64 MiB). A multiple of 2 MiB must be specified. If the parameter is omitted (or 0 is specified), it will be interpreted as though the default size of 67108864 (64 MiB) was specified.

For every 2 MiB that the GPU page table pool is increased, 512 page table entries are added. This is equivalent to the page table volume required for mapping 1 GiB of memory.

## AMM Page Table Pool Size

```
{
    ....
    "amm": {
        "pagetableMemorySizeInMib": 64
    }
}
```

amm/pagetableMemorySizeInMib is a parameter that specifies the size of the AMM page table pool used for an AMM area. The unit is mebibytes, the maximum value is 256, and the minimum value is 64. A multiple of 2 MiB must be specified. If the parameter is omitted (or 0 is specified), it will be interpreted as though the default size of 64 MiB was specified.

For every 2 MiB that the AMM page table pool is increased, approximately 327 (2 MiB/6400 B) page table entries are added. Applications can map a maximum of 2 MiB of virtual address space memory for each page table entry.

## Size of the AMM Virtual Address Space

```
{
    ....
    "amm": {
        "vaRangeInGib": 512,
        "multimapVaRangeInGib": 256
    }
}
```

amm/vaRangeInGib is a parameter that specifies the size of the virtual address space used by the AMM. The unit is gibibytes, and either 512 or 1024 is a valid value. If the parameter is omitted, it will be interpreted as though the default size of 512 GiB was specified. The specified value is reflected in the `vaStart` and `vaEnd` fields of the `sce::Ampr::AmmVirtualAddressRanges` structure.

amm/multimapVaRangeInGib is a parameter that specifies the size of the virtual address space used by the AMM multimap. The unit is gibibytes, and a valid value consists of an integer of 0 or greater. A smaller size than that specified for amm/vaRangeInGib must be specified because the virtual address space for the multimap is reserved as part of the latter portion of the virtual address space used by the AMM. If the parameter is omitted, it will be interpreted as though the default size of 0 GiB was specified, that is, as though the multimap was disabled. The specified value is reflected in the `multimapVaStart` and `multimapVaEnd` fields of the `sce::Ampr::AmmVirtualAddressRanges` structure.

For information about the virtual address space used by the AMM, refer to [AMM Library Overview - Reference Information - Virtual Address Space](../AMM-Overview/virtual-address-space.html).