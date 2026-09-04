# NpEntitlementAccess Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Reference/sce-np-entitlement-access-initialize.html

# Initialization

# SceNpEntitlementAccessBootParam

Boot parameters

## Definition

```
#include <np_entitlement_access.h>
typedef struct SceNpEntitlementAccessBootParam {
	char reserved[32];
} SceNpEntitlementAccessBootParam;
```

## Members

|  |  |
| --- | --- |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is specified for the `bootParam` (second) argument of `sceNpEntitlementAccessInitialize()`, which is used for initializing the NpEntitlementAccess library.

# SceNpEntitlementAccessInitParam

Library initialization parameters

## Definition

```
#include <np_entitlement_access.h>
typedef struct SceNpEntitlementAccessInitParam {
	char reserved[32];
} SceNpEntitlementAccessInitParam;
```

## Members

|  |  |
| --- | --- |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is specified for the `initParam` (first) argument of `sceNpEntitlementAccessInitialize()`, which is used for initializing the NpEntitlementAccess library.

# sceNpEntitlementAccessInitialize

Initializes the library and gets boot parameters

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessInitialize(
	const SceNpEntitlementAccessInitParam *initParam,
	SceNpEntitlementAccessBootParam *bootParam
)
```

## Arguments

|  |  |
| --- | --- |
| `initParam` | Initialization parameters |
| `bootParam` | Destination to store the obtained boot parameters |

## Return Values

Stores the obtained boot parameters in `*bootParam` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Library is already initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |

## Description

This function performs initialization processing for the entire NpEntitlementAccess library according to the parameters specified in `initParam`. Boot attributes of the application will be stored in `bootParam`.

Call this function only once when the application is started.

If an attempt is made to use other functions of the NpEntitlementAccess library before initialization has been performed, the `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` error will occur.

## Examples

```
SceNpEntitlementAccessInitParam initParam;
SceNpEntitlementAccessBootParam bootParam;

/* Clear with 0's */
memset( &initParam, 0, sizeof(SceNpEntitlementAccessInitParam) );
memset( &bootParam, 0, sizeof(SceNpEntitlementAccessBootParam) );

/* Initialize the NpEntitlementAccess library */
ret = sceNpEntitlementAccessInitialize( &initParam, &bootParam );
```

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.