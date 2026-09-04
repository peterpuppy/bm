# NpEntitlementAccess Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Reference/sce-np-entitlement-access-get-sku-flag.html

# Obtaining the SKU Flag

# sceNpEntitlementAccessGetSkuFlag

Gets the SKU flag (integer value)

## Definition

```
#include <np_entitlement_access.h>
typedef uint32_t SceNpEntitlementAccessSkuFlag;

int32_t sceNpEntitlementAccessGetSkuFlag(
	SceNpEntitlementAccessSkuFlag *skuFlag
)
```

## Arguments

|  |  |
| --- | --- |
| `skuFlag` | Destination to store the obtained SKU flag |

## Return Values

Stores the obtained SKU flag in `*skuFlag` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |

## Description

This function obtains the SKU flag (integer value) that has been set for the application.

For `*skuFlag`, one of the following values representing the SKU flag will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_SKU_FLAG_TRIAL` | 1 | Trial |
| `SCE_NP_ENTITLEMENT_ACCESS_SKU_FLAG_FULL` | 3 | Full |

If NULL is specified for `skuFlag`, a parameter error will occur.

## Examples

```
/* Obtain the SKU flag */
SceNpEntitlementAccessSkuFlag skuflag;
ret = sceNpEntitlementAccessGetSkuFlag( &skuflag );
```

## Notes

Refer to [NpEntitlementAccess Library Overview - Using the Library: SKU Flags - SKU Flag Update Event](../NpEntitlementAccess-Overview/entitlement-information-update-events-for-sku-flag.html) and [NpEntitlementAccess Library Overview - Using the Library: SKU Flags - Development Support Features for the SKU Flag](../NpEntitlementAccess-Overview/development-support-features-for-sku-flag.html) for details about SKU flags.

This is a blocking function. Call this function from a subthread, as processing may take time.