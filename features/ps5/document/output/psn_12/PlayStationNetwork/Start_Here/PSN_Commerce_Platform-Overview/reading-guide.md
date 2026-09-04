# PlayStation™Network Commerce Platform Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce_Platform-Overview/reading-guide.html

# Reference Materials

For further information, refer to the following resources.

## System Requirements

To begin adding commerce features to your application, see the following developer documents.

**Commerce Service Overview**

For an overview of the [Regional Store](new-package-types-for-new-unified-entitlements.html#psn-commerce-platform-overview_1_5__psn-commerce-platform-overview_1_5_1) and [Title Store](new-package-types-for-new-unified-entitlements.html#psn-commerce-platform-overview_1_5__psn-commerce-platform-overview_1_5_2), a walkthrough of product and catalog structure, and descriptions of countries/regions, languages and currencies that the PlayStation™Network supports, see the [PlayStation™Network Commerce Service Overview](../PSN_Commerce_Service-Overview/__document_toc.html).

**Commerce Programming Guide**

The [PlayStation™Network Commerce Programming Guide](../PSN_Commerce-Programming_Guide/__document_toc.html) developer overview describes how to begin using the Commerce platform in your game-development efforts. It also includes information on test accounts and cards that you can use to facilitate debugging and testing.

**Store Content Guidelines**

For descriptions of the various content types, and information about how to set them up for sale in the PlayStation™Store, see the [PlayStation™Store Content Guidelines](../PlayStation_Store_Content-Guidelines/__document_toc.html).

## Binary Package Submission

For an overview of submitting different package types through the GEMS tool, and for information about changes to the tool in PlayStation®5, see the [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html).

## Web APIs

To issue REST requests directly or by means of C++ bindings to the underlying RESTful API, see the following documents.

**In-Game Catalog Web API**

This is a Web API for obtaining product information in the PlayStation™Store (or an associated Title Store) related to the game title and its associated products.

* [In-Game Catalog Overview](../../../WebAPI/latest/In_Game_Catalog-Overview/__document_toc.html)

Introduces the PlayStation™Network Catalog Web API, which is a RESTful API that you can use to offer in-game commerce opportunities to the user.

* [In-Game Catalog Web API Reference](../../../WebAPI/latest/In_Game_Catalog_WebAPI-Reference/__document_toc.html)

Reference descriptions of the RESTful PlayStation™Network In-Game Catalog Web API.

**Entitlements Web API**

This is a Web API for obtaining information and operating on service entitlements and consumable entitlements. For PlayStation®5, the Entitlements Web API is available only for application servers and websites. On the PlayStation®5 console, you must use the NpEntitlementAccess Library.

* [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html)

Introduces the NpEntitlementAccess library, which provides features for accessing additional content and consumable entitlements. A feature is also provided for obtaining the SKU flag that is set for each application.

* [NpEntitlementAccess Library Reference](../NpEntitlementAccess-Reference/__document_toc.html)

Reference descriptions of NpEntitlementAccess library type definitions, classes, methods and return codes.

## Native Commerce SDKs

**NpCommerceDialog Library**

This library provides features to browse and purchase products in the PlayStation™Store (or an associated Title Store) by means of a system-provided GUI.

* [NpCommerceDialog Library Overview](../NpCommerceDialog-Overview/__document_toc.html)

Introduces the NpCommerceDialog Library, which provides the NpCommerce dialog. The NpCommerce dialog provides modes to display product page, catalog tree, voucher redemption and checkout.

* [NpCommerceDialog Library Reference](../NpCommerceDialog-Reference/__document_toc.html)

Reference descriptions of NpCommerceDialog library type definitions, classes, methods and error codes.

**NpCommerce Library**

This library provides features to show/hide PlayStation™Store icons.

* [NpCommerce Library Overview](../NpCommerce-Overview/__document_toc.html)

The NpCommerce library shows or hides PlayStation™Store icons. Applications that implement commerce with an in-game browsing format must use this API to display a PlayStation™Store icon.

* [NpCommerce Library Reference](../NpCommerce-Reference/__document_toc.html)

Reference descriptions of the NpCommerce Library.

**NpEntitlementAccess Library**

This library provides access to all entitlement information (both Unified Entitlements and Service Entitlements) and obtains a list of already-purchased additional contents on the PlayStation®5 console. The Entitlements Web API is no longer available on the PlayStation®5 console and the NpEntitlementAccess Library must be used on the console. The Entitlements Web API is still available for application servers and websites.

* [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html)

Introduces the NpEntitlementAccess library, which provides features for accessing additional content and consumable entitlements.

* [NpEntitlementAccess Library Reference](../NpEntitlementAccess-Reference/__document_toc.html)

Reference descriptions of NpEntitlementAccess library type definitions, functions and error codes.

**NpCppWebApi Library**

As an alternative to using the NpWebApi2 library to issue REST requests directly, the NpCppWebApi library enables developers to use C++ function calls and objects to work with Web APIs.

* [NpCppWebApi Library Overview](../NpCppWebApi-Overview/__document_toc.html)

Introduces the NpCppWebApi library, which provides a C++ language binding for each feature of the PlayStation™Network Web API (Web API).

* [NpCppWebApi Library Reference](../NpCppWebApi-Reference/__document_toc.html)

Reference descriptions of NpCppWebApi library type definitions, classes, methods and return codes.

## Product Setup

For more information, see [Getting Started with Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/Getting_Started.html).

## Game Hub

To learn more about a game's hub, see these documents.

* [Game and App Hubs](https://learn.playstation.net/bundle/content-pipeline/page/GameHub_Overview.html)

This guide describes the game hub features in detail, explaining core objectives, motivations and expected outcomes for the uses of game hub features.

* [PlayStation™Network Game Hub Preview Application Overview](../PSN_Game_Hub_Preview_Application-Overview/__document_toc.html)

This guide describes the core objectives and functionality of the Game Hub Preview application.

# Sample Tutorials

This topic describes the tutorials available to you to test feature gating and virtual currency implementations.

To learn how to implement PlayStation™Network Commerce Platform features in your title, see these developer tutorials that provide working code examples.

## Premium Feature Gating Tutorial

The [Premium Feature Gating Tutorial](../Premium_Feature_Gating-Tutorial/__document_toc.html) provides sample game code and developer documentation demonstrating the implementation of a premium feature gated by a subscription service like PlayStation®Plus. For complete source code, see `sample_code/playstation_network/tutorial_np_premium`.

## Virtual Currency Tutorial

The [Virtual Currency Tutorial](../Virtual_Currency-Tutorial/__document_toc.html) provides sample code and developer documentation demonstrating the implementation of a [Title Store](new-package-types-for-new-unified-entitlements.html#psn-commerce-platform-overview_1_5__psn-commerce-platform-overview_1_5_2) that uses virtual currency in the idempotent consumption pattern that the PlayStation®5 platform requires. For complete source code, see `sample_code/playstation_network/tutorial_virtual_currency`.