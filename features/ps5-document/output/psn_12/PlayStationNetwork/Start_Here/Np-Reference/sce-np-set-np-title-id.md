# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/sce-np-set-np-title-id.html

# Various Information Settings

# sceNpSetNpTitleId

Sets the NP Title ID and NP Title Secret

## Definition

```
#include <np/np_common.h>
int sceNpSetNpTitleId(
	const SceNpTitleId *titleId,
	const SceNpTitleSecret *titleSecret
);
```

## Arguments

|  |  |
| --- | --- |
| `titleId` | NP Title ID (IN) |
| `titleSecret` | NP Title Secret (IN) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |

## Description

This function sets the NP Title ID and NP Title Secret.

The NP Title ID and NP Title Secret set with this function are only valid in a Development Kit with its Release Check Mode set to Development Mode, and they are only used when an arbitrary NP Title ID and NP Title Secret are specified from a program without using the NP Title ID and NP Title Secret stored in the nptitle.dat file.

During Release Mode or Assist Mode, the NP Title ID and NP Title Secret set by this function will be ignored; nptitle.dat will always be used. Even during Development Mode, the NP Title ID and NP Title Secret set by this function will be ignored and nptitle.dat will always be used when the system software setting item of "★Debug Settings" > "PlayStation™Network" > "Ignore NpTitleId set by API in Development Mode" is set to "On".

# sceNpSetAdditionalScope

Sets additional scope (reserved)

## Definition

```
#include <np/np_common.h>
#define SCE_NP_ADDITIONAL_SCOPE_MAX_LENGTH 512
int sceNpSetAdditionalScope(
	const char* scope
);
```

## Description

This function is reserved for future use. There is no need to use it at present. If it is mistakenly used, libraries such as NpWebApi2 will return 0x82E01039.