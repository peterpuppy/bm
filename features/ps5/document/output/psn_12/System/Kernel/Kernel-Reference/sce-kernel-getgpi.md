# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-kernel-getgpi.html

# Development Support

# sceKernelGetGPI

Get GPI switch value

## Definition

```
#include <kernel.h>
uint64_t sceKernelGetGPI(void)
```

## Arguments

None

## Return Values

Returns the value stored in the GPI switch.

## Description

This function reads the value of the GPI (General Purpose Input) switch retained in the system. The GPI switch is a 64-bit non-volatile area that can be used for arbitrary purposes during development.

This function is only valid when the Release Check Mode is set to Development Mode or Assist Mode. In other cases, 0 will always return regardless of a value being stored in the GPI switch.

# sceKernelSetGPO

Turn on/turn off LEDs at the front panel of the Development Kit

## Definition

```
#include <kernel.h>
void sceKernelSetGPO(
    uint32_t uiBits
 )
```

## Arguments

|  |  |
| --- | --- |
| `uiBits` | Bit pattern to set each LED on/off (only the lower 8 bits are valid) |

## Return Values

None

## Description

This function controls the GPO (General Purpose Output) to turn on/turn off each of the eight LEDs at the front panel of the Development Kit. These LEDs can be used for arbitrary purposes during development.

Each of the eight LEDs correspond to each bit of the lower 8 bits of `uiBits` with the farthest right LED corresponding to the lowest bit. To turn on the LED, specify 1 to the corresponding bit; specify 0 to turn off the LED.

This function is valid only when the Release Check Mode of a Development Kit is set to Development Mode. In other cases, it will terminate normally without doing anything.

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.