# PlayStation™Network Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN-Overview/commerce-platform.html

# Commerce Platform

The Commerce Platform enables the sale and provisioning of digital game content and services to accounts for PlayStation™Network. The platform connects players quickly with the content and play experiences they want, and provides effortless in-game browsing, direct connection to the digital store, PlayStation®Plus flows for multiplayer access, and checkout experiences.

The commerce platform provides a wide range of features including pre-order, sales, and
discounting and subscription capabilities, supported by payment technology that achieves a
successful, risk-free transaction.

## NpCommerceDialog Library

The NpCommerceDialog library provides features for implementing in-game browsing. In-game browsing allows the user to buy digital content and services, such as additional items or additional scenarios, from the Title Store, using the user interface provided by the library. Users can also download content that they have already purchased. For details, refer to the following documents:

* [NpCommerceDialog Library Overview](../NpCommerceDialog-Overview/__document_toc.html)
* [NpCommerceDialog Library Reference](../NpCommerceDialog-Reference/__document_toc.html)

## NpCommerce Library

The NpCommerce library provides features for showing or hiding the PlayStation™Store icon. The PlayStation™Store icon must be continuously displayed during in-game browsing. For details, refer to the following documents:

* [NpCommerce Library Overview](../NpCommerce-Overview/__document_toc.html)
* [NpCommerce Library Reference](../NpCommerce-Reference/__document_toc.html)

## In-Game Catalog Web API

The In-Game Catalog Web API can obtain product information in the PlayStation™Store Title Store of the game title, and browse the products. For details, refer to the following documents:

* [In-Game Catalog Overview](../../../WebAPI/latest/In_Game_Catalog-Overview/__document_toc.html)
* [In-Game Catalog Web API Reference](../../../WebAPI/latest/In_Game_Catalog_WebAPI-Reference/__document_toc.html)

## NpEntitlementAccess Library

The NpEntitlementAccess library is for use by applications that run on the PlayStation®5 console. It provides access to all Entitlement information, and can obtain a list of the additional content that the user has already purchased. This replaces the Entitlements Web API, which is no longer available to applications that run on the PlayStation®5 console. The Entitlements Web API is still available for application servers and websites. For details, refer to the following documents:

* [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html)
* [NpEntitlementAccess Library Reference](../NpEntitlementAccess-Reference/__document_toc.html)

## Entitlements Web API

The Entitlements Web API is for use by application servers and websites only. It obtains entitlement information and operates on service entitlements and consumable entitlements. The same functionality is available to applications that run on the PlayStation®5 console in the NpEntitlementAccess Library. For details, refer to the following documents:

* [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html)
* [Entitlements Web API Reference](../../../WebAPI/latest/Entitlements_WebAPI-Reference/__document_toc.html)

## AppContent Library

The AppContent library provides various features for mounting and accessing game-related content including additional content, downloaded data and temporary data. For details, refer to the following documents:

* [AppContent Library Overview](../AppContent-Overview/__document_toc.html)
* [AppContent Library Reference](../AppContent-Reference/__document_toc.html)