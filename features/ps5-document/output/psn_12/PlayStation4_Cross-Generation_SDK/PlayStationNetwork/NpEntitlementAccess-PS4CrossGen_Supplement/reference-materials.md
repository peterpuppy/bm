# NpEntitlementAccess Library Cross-Generation Supplement – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-PS4CrossGen_Supplement/reference-materials.html

# Additional Information for the Cross-Generation SDK

The PlayStation®4 Cross-Generation SDK ("Cross-Gen SDK") is an SDK for making some of the SDK features provided for PlayStation®5 usable on PlayStation®4. For more information about the Cross-Gen SDK as a whole, please refer to the [Cross-Generation Overview](../Cross_Generation-Overview/__document_toc.html).

This document provides information required for a PlayStation®4 application to use PlayStation®5 NpEntitlementAccess library features using the Cross-Gen SDK.

# Reference Materials

Refer to the following PlayStation®5 documents for features of the NpEntitlementAccess library provided by the PlayStation®5 SDK:

* [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html)
* [NpEntitlementAccess Library Reference](../NpEntitlementAccess-Reference/__document_toc.html)

# Restrictions

Compared to when a PlayStation®5 application uses the NpEntitlementAccess library, the following restrictions exist when a PlayStation®4 application uses features of the PlayStation®5 NpEntitlementAccess library with the Cross-Gen SDK:

Note:

In addition to the restrictions described below, overall performance deterioration may also occur given the difference between the PlayStation®5 hardware performance and the PlayStation®4 hardware performance.

## Obtaining the package type

One of the following values will be stored to `packageType` of `SceNpEntitlementAccessAddcontEntitlementInfo` for PlayStation®4 applications. (Refer to the [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html) document for details on package types.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_NONE` | 0 | Undefined type |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PS4GD` | 1 | Application |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PS4AC` | 2 | Additional content with extra data |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PS4AL` | 3 | Additional content without extra data |

Note:

Specification-wise, PSGD, PSAC, and PSAL, which are package types for PlayStation®5, cannot be obtained by PlayStation®4 applications.

# Other Notes

## Sample Program

In the Cross-Gen SDK, the sample program for the NpEntitlementAccess library is stored in the following directory. (Only where the sample is stored differs from the PlayStation®5 SDK; there are no differences in terms of features.)

* sample\_code/playstation\_network/api\_np\_cross\_gen/api\_np\_entitlement\_access