# PlayStation™Store Content Guidelines – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayStation_Store_Content-Guidelines/entitlements-and-game-package-types.html

# PlayStation™Store Content Guidelines Overview

This chapter provides on overview of guidelines to follow when working with content in the PlayStation™Store. For example, patterns of content distribution, entitlement and game package types, and content registration.

This document describes the various combinations of packages that can be used when distributing content through the PlayStation™Store. Of the possible combinations, a number of typical release patterns are described, with details regarding the game package types, system files, content information files, user programs, and data that are appropriate for implementation of these release patterns. Follow the tips in this document to create all game package types, including add-on data, for easier handling and better manageability. The information in this document can also be used during the production and execution phase.

Other release patterns are also possible. They can have an impact on the development process or post-release usage, and potential abuse by users. Consider the release patterns and issues described in this document carefully and contact SIE in advance if another release pattern appears to be necessary.

# Patterns of Content Distribution

This topic provides an overview of several ways you can distribute content through the PlayStation™Store.

The following are basic patterns of content distribution.

## Full-game

The simplest release pattern. All programs and data are in one package, which is distributed as a full game on the PlayStation™Store.

## Upgradeable Game /Trial Version

In this release pattern, a trial version of a game is distributed for free with limited access to the full game, along with a license key that unlocks full functionality. The package to be distributed is shared between the trial version and full game which allows easy conversion of a trial to the full version on purchase of the upgrade. In addition to upgrading the trial version, users can purchase the full game on its own.

## Demo With No Restriction Unlocking

In this promotional pattern, a demo is distributed for free with restrictions so that only limited portions of the game can be played. Demos take the form of standalone package files, downloaded and accessed separately from full games. There is no functionality provided for unlocking and upgrading to the full version.

## Additional Content for Purchase

In this release pattern, data for new content/stories/stages/etc. is available for purchase separately from the game package/game disc.

There are two implementation methods.

* Providing the data to add as an additional content package.
* Including the data to add with the original game package, then providing the usage entitlements or license to unlock the additional content.

# Entitlements and Game Package Types

This topic provides information on entitlements and game package types.

All content available in the PlayStation™Store is distributed in `game package` format, which is associated with the unified entitlement type.

Refer to [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html) for details about unified entitlements. Also, refer to [Entitlements for Add-on Products Overview](https://learn.playstation.net/csh?context=EntitlementsOverview_CP) for information about how entitlements are configured in Content Pipeline.

The game package type is specified by the `<volume_type>` parameter in the GP5 file. For more information about the GP5 file, see [GP5 File Specification](../GP5-Specification/__document_toc.html).

Supported Game Packages

| **Game Package\_type** | **Description** |
| --- | --- |
| PlayStation®5 Application Package | * Game package. * Includes a boot file. Installed as a game. |
| PlayStation®5 Additional Content Package | * Additional content package (with extra data). * Includes data files and entitlement information. * Installed as additional content. |

Game packages are further classified according to the "Application DRM Type" parameter.

"Application DRM Type" Parameter

| **Application DRM Type** | **Description** |
| --- | --- |
| Standard | * Application available for purchase. |
| Upgradable | * Upgradable application. * A single package has both the trial version and the full version. |
| Demo | * Application provided for free as a demo. |

These parameters are to be specified when creating a game package with Publishing Tools.

## Required Files in the Package

A package must include the param file (`param.json`) and content information files (such as `icon0.png`).

The param file is created with Param Editor, included with Publishing Tools. The correct menu item must be selected according to the content of the package.

## User Files in the Package

User files that can be included in a game package are all access-protected. Access-protected files can be used only on consoles where the user who made the purchase has performed system activation and consoles where the user who made the purchase is logged in.

## Access Rights for Game Packages

Each game package sold in the PlayStation™Store always has matching entitlement information called a unified entitlement. A user obtains access rights for the applicable game package by purchasing a unified entitlement. The access rights for game packages are managed based on the user's account.

## Checking Entitlements to Game Packages

Because entitlement information reflects the price set in the PlayStation™Store, checking the entitlements (checking that the user paid for the content) becomes an extremely important procedure. For PlayStation®5, the application itself must check that the entitlements are owned by the user.

The entitlement check methods can be performed using the NpEntitlementAccess library which checks the SKU flag for the application and the entitlements to the additional content

If this check procedure is not correctly executed, there is a risk of allowing users to use the content even if they have not paid for it. Design and test the entitlement checking procedure carefully.

# Content Registration

This topic provides information on registering content before distribution.

The Package/Disc Management Tool (GEMS) is a system for managing the release processes for content. All content with packages like PlayStation®5 applications and PlayStation®5 Additional Content is registered through GEMS.

Packages generated with Publishing Tools are uploaded to GEMS. After uploads are successful and imported into GEMS, it is possible to publish each package in the development environment. After the publish processing in GEMS is complete, packages are imported into Content Pipeline.

## SKU Details

Unified entitlements are not directly sold on the PlayStation™Store, a unified entitlement is associated with a SKU.

Each SKU is associated with a product type and then terms of sale are created and approved for that product in Content Pipeline prior to selling on the PlayStation™Store.

Normally, a single unified entitlement is associated with a single SKU, but a single SKU can be associated with multiple unified entitlements.

For details on settings, refer to the following Content Pipeline documents:

* [Creating an Upgradable Game](https://learn.playstation.net/bundle/content-pipeline/page/PricingAvailability_UpgradeableGameCreate.html)
* [Creating a Bundle in Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/Product_BundleCreate.html)

# Reference Materials

This topic provides links to other documents you may find useful when working with PlayStation™Store content.

Refer to the following documents for more information.

* [PlayStation™Network Commerce Service Overview](../PSN_Commerce_Service-Overview/__document_toc.html)

This document provides an overview of PlayStation™Store.

* [PlayStation™Network Commerce Programming Guide](../PSN_Commerce-Programming_Guide/__document_toc.html)

This document describes the development process of programs to be distributed through PlayStation™Store.

* [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html)

This document describes the use of entitlements.

* [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html)

This document describes the files to include in a game package, and the procedure for creating a package.

* [Content Information Specifications](../Content_Information-Specifications/__document_toc.html)

This document describes the data format and multilingual support features of content information files such as `icon0.png`.

* [Getting Started with Content Pipeline](https://learn.playstation.net/bundle/content-pipeline)

These help articles contain information about various Content Pipeline topics, including configuring entitlements and creating products.

* [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html)

This document describes a library that is used to handle additional content and unlock keys for trial versions.

* [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html)

This document describes the operation of GEMS, the web application for managing the release processes for various content for PlayStation®5.

* [GP5 File Specification](../GP5-Specification/__document_toc.html)

This document describes contents of the GP5 file.