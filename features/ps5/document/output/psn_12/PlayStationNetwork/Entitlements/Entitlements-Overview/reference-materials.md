# Entitlements Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Entitlements-Overview/reference-materials.html

# Entitlements Web API Overview

This chapter provides an overview of the Entitlements Web API.

An entitlement is a rule granting conditional access for a user to protected resources associated with an SKU. The Entitlements Web API gives developers the ability to retrieve and update entitlement information. Entitlements grant access to various resources such as:

* Games
* Downloadable Content
* Demos
* Themes

Or any other items that you would want to grant a user permission to use, for either temporary or permanent use.

Entitlements can be granted on the following bases:

* Date. You can specify when access begins, and when it ends. For example, a company may wish to allow access to a beta product for short duration, specifying when beta access begins and ends, and for whom.
* Limited use. You can set a specific count of how many times you grant access. For example, a game demo allowing a user five uses before they no longer can run the software. Limited use entitlements are referred to as *consumable*.
* Permanent access. You can also set access to be permanent. For example, if a user purchases an item in a game.

Entitlements can be both retrieved and updated. The API can consume limited use entitlements, as well as to retrieve all entitlements a user has, or just a specific entitlement, based on an entitlement ID.

Note:

It is recommended that entitlement validity be checked at the following times:

* When the game launches.
* When a user selects a specific menu such as **Confirm Validity Period** within the game.
* When a user purchases a product within the game.
* When an entitlement update occurs.

The Entitlements Web API is available for game servers and websites.

# Entitlement Types

This topic provides information on entitlement types.

The Entitlements Web API manages *service* and *unified* entitlements. Service entitlements are deprecated in PlayStation®5 and appear only when defined with PlayStation®4 titles and shared using the PlayStation™Store Delivered Content (PSSDC) mechanism. The functionality previously provided by service entitlements is now part of unified entitlements.

## Unified Entitlement

A Unified Entitlement is a product element that gives certain privileges to the user. It can be game content, subscription to game play, or the rights to use a certain item in a game. The system manages entitlements on PlayStation™Network servers. It is possible to set validity periods (the number of days a user can use the entitlement after the purchase) or the number of usable times. These restrictions are not associated with the unified entitlement itself, but to the SKU linked with it.

Each unified entitlement has a `packageType` field that specifies the role that the entitlement fulfills. The table below enumerates its possible values. For details, refer to the [PlayStation™Network Service Setup Guide](../../../SDK/latest/PSN_Service_Setup-Guide/__document_toc.html).

| **Supported Format** | **Package Type** | **Description** |
| --- | --- | --- |
| PlayStation®5 | `PSGD` | PlayStation®5 game download. |
| `PSAC` | PlayStation®5 additional content. |
| `PSAL` | PlayStation®5 additional unlockable feature. |
| `PSIL` | PlayStation®5 individual license. |
| PlayStation®5 and PlayStation®4 | `PSCONS` | PlayStation™Store consumable (non-virtual currency). |
| `PSVC` | PlayStation™Store virtual currency. |
| `PSSUBS` | PlayStation™Store game developer subscription. |
| `PSTRACK` | PlayStation™Store tracker. |
| PlayStation®4 | `PS4GD` | PlayStation®4 game download. |
| `PS4AL` | PlayStation®4 unlockable feature. |
| `PS4AC` | PlayStation®4 additional content. |
| `PS4MISC` | PlayStation®4 miscellaneous use. |

Use the `activeFlag` parameter to check for expired entitlements in `getEntitlement` or `listEntitlements` requests. This parameter shows whether an entitlement is active. If there is no entitlement information at all, it has never been granted.

See the [PlayStation™Network Commerce Service Overview](../../../SDK/latest/PSN_Commerce_Service-Overview/__document_toc.html) for further information.

Note:

You must use the NpEntitlementAccess library (which is available in the PlayStation®5 SDK and the PlayStation®4 Cross-Gen SDK) to handle the newly introduced PlayStation®5 package types in an application. Avoid using the new package types for applications that use the base PlayStation®4 SDK.

# Service Labels

This topic provides information on Np service labels.

NP Service Labels are numeric identifiers that specify a single service instance of a given NP Title ID which span across multiple service instances. Some Entitlement Web API requests allow passing a NP Service Label as an optional parameter. For details, refer to the [PlayStation™Network Service Setup Guide](../../../SDK/latest/PSN_Service_Setup-Guide/__document_toc.html).

# Entitlement Labels

This topic provides information on entitlement labels and how they are defined in your application.

An Entitlement Label is a string that identifies an entitlement of a specific resource; for example, an in-game item. For Service Entitlements, it is specified in Content Pipeline and is 6 digits, this is deprecated for use of PlayStation®5. For Unified Entitlements based on the package type the entitlement can be specified in Content Pipeline or Param Editor (where it is known as the Content Label), it is 16 digits.

Here is the table outlining where the entitlement label can be specified for Unified entitlement per package type.

| **Package Type** | **Entitlement label creation** |
| --- | --- |
| `PSGD`, `PSAC`, `PSAL` | PlayStation®5 GEMS |
| `PSVC`, `PSCONS`, `PSSUBS` | Content Pipeline |

For more information, see [Param Editor User's Guide](../../../SDK/latest/Param_Editor-Users_Guide/__document_toc.html).

Entitlement Labels are unique to a specific title. For example, if title A has a Service ID of `US1234-EXDG10001_00` and title B has a Service ID `EU1234-EXDG10002_00`, then Entitlements ID `US1234-EXDG10001_00-1234567890ABCDEF` and `EU1234-EXDG10002_00-1234567890ABCDEF` have the same logical meaning (they are associated with the same in-game item) for both titles. This allows you to use a common implementation to check for the Entitlement Label (in this case, "`1234567890ABCDEF`") for both titles even though the Service IDs are different.

# API Group Entitlement Base URL

This topic provides information on how to make calls to the Entitlements Web API.

All calls to the Entitlements Web API require the use of an API Group `entitlementsBaseUrl` as the root path to the API. For a description of how to obtain and use `entitlementsBaseUrl`, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

# Usage Notes

This topic provides extra details you may find useful when using the Entitlements Web API.

* Depending on the use of the mandatory and optional parameters used with the Entitlements Web API, the responses can vary. Use caution in specifying the proper parameters to ensure you get an appropriate response.
* Updating the "use count" for an entitlement significantly affects end users. Understand both mandatory and optional parameters carefully before updating use count. For details, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).
* You must obtain an access and ID token to access any PlayStation™Network Web APIs. For details, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

# Reference Materials

This topic provides links to other documents you might reference when using the Entitlements Web API.

* To execute the API or obtain/update a resource, the correct permission is required. For details, refer to the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).
* Each API may have restrictions on access frequency. For details about rate limiting, refer to the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).
* For further details on the API, including required headers, query parameters, structures returned, and errors, refer to the [Entitlements Web API Reference](../Entitlements_WebAPI-Reference/__document_toc.html).
* For further details on commerce and the PlayStation™Store, see the [PlayStation™Network Commerce Service Overview](../../../SDK/latest/PSN_Commerce_Service-Overview/__document_toc.html).
* For additional information on using entitlements within a PlayStation®5 application, refer to the [NpEntitlementAccess Library Overview](../../../SDK/latest/NpEntitlementAccess-Overview/__document_toc.html).

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Entitlements Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Entitlements_WebAPI-ReleaseNotes.html)