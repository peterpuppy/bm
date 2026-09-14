# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-uuid-create.html

# UUID

# SceKernelUuid

Structure representing the UUID

## Definition

```
#include <kernel.h>
typedef struct {
    uint32_t timeLow;
    uint16_t timeMid;
    uint16_t timeHiAndVersion;
    uint8_t clockSeqHiAndReserved;
    uint8_t clockSeqLow;
    uint8_t node[6];
} SceKernelUuid;
```

## Members

|  |  |
| --- | --- |
| `timeLow` | Low field of the timestamp (value of offset 0 to 3 bytes of the UUID) |
| `timeMid` | Middle field of the timestamp (value of offset 4 to 5 bytes of the UUID) |
| `timeHiAndVersion` | High field of the timestamp and version number (value of offset 6 to 7 bytes of the UUID) |
| `clockSeqHiAndReserved` | High field of the clock sequence and variant (value of offset 8 bytes of the UUID) |
| `clockSeqLow` | Low field of the clock sequence (value of offset 9 bytes of the UUID) |
| `node` | Spatially unique node identifier (value of offset 10 to 15 bytes of the UUID) |

## Description

This structure is used upon creating a UUID with `sceKernelUuidCreate()`.

# sceKernelCreateUuidV1

Create UUID version 1

## Definition

```
#include <kernel.h>
int sceKernelCreateUuidV1(
    unsigned char outUuid[16]
)
```

## Arguments

|  |  |
| --- | --- |
| `outUuid` | Destination to store the generated UUID version 1 |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `outUuid` is NULL |

## Description

This function generates an RFC 4122-format UUID version 1. It generates a UUID version 1 using the console's MAC address and time. Although the format of what is generated differs, the contents of what is generated are the same as those of `sceKernelUuidCreate()`.

The generated UUID contains the MAC address; use it in accordance with TRC [R5081](../../../TRC/latest/TRC/R5081.html).

# sceKernelCreateUuidV4

Create UUID version 4

## Definition

```
#include <kernel.h>
int sceKernelCreateUuidV4(
    unsigned char outUuid[16]
)
```

## Arguments

|  |  |
| --- | --- |
| `outUuid` | Destination to store the generated UUID version 4 |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `outUuid` is NULL |

## Description

This function generates an RFC 4122-format UUID version 4. It generates a UUID version 4 using random values.

# sceKernelCreateUuidV7

Create UUID version 7

## Definition

```
#include <kernel.h>
int sceKernelCreateUuidV7(
    unsigned char outUuid[16]
)
```

## Arguments

|  |  |
| --- | --- |
| `outUuid` | Destination to store the generated UUID version 7 |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `outUuid` is NULL |

## Description

This function generates an RFC 4122-format UUID version 7. It generates a UUID version 7 using the time elapsed since midnight on January 1, 1970, and using a random numeric value.

# sceKernelUuidCreate

Create UUID

## Definition

```
#include <kernel.h>
int sceKernelUuidCreate(
    SceKernelUuid *outUuid
)
```

## Arguments

|  |  |
| --- | --- |
| `outUuid` | Destination to store the created UUID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_KERNEL_ERROR_EINVAL` | 0x80020016 | `outUuid` is NULL |
| `SCE_KERNEL_ERROR_EFAULT` | 0x8002000e | `outUuid` points to invalid memory |

## Description

This function creates a DCE 1.1 format UUID. It creates a UUID using the console's MAC address and time.

The created UUID will contain the MAC address; use it in accordance with TRC [R5081](../../../TRC/latest/TRC/R5081.html).

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.