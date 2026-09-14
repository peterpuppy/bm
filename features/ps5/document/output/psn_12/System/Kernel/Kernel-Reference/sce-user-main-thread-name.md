# Kernel Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Kernel-Reference/sce-user-main-thread-name.html

# Process Management

# sceUserMainThreadName

Main thread name

## Definition

```
#include <kernel.h>
extern const char sceUserMainThreadName[] __attribute__ ((weak));
```

## Description

This API feature is used to specify a name for debugging to the main thread.

Specify a character string up to 32 bytes including the NULL-terminator character. If not specified, the first 31 characters of the name of the process' source executable file will be the main thread name.

## See Also

[Kernel Overview - Process Management - Initial Settings for the Main Thread](../Kernel-Overview/initial-settings-for-the-main-thread.html)

# sceUserMainThreadPriority

Main thread scheduling priority

## Definition

```
#include <kernel.h>
extern int sceUserMainThreadPriority __attribute__ ((weak));
```

## Description

This API feature is used to specify the scheduling priority of the main thread. If not specified, the priority will be the default priority. (Refer to [Kernel Overview - Process Management - Initial Settings for the Main Thread](../Kernel-Overview/initial-settings-for-the-main-thread.html).)

---

© 2025 Sony Interactive Entertainment Inc.

[Copyright](../About_this_SDK/0004.html) 1994-2012 The FreeBSD Project. All rights reserved.