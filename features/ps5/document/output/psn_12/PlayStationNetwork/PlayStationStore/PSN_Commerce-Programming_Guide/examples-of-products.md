# PlayStation™Network Commerce Programming Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce-Programming_Guide/examples-of-products.html

# Product Configuration and Handling

The PlayStation®Store makes products and content available to users by means of entitlements.

# Product Types and Attributes

Products for PlayStation®5 distributed through the PlayStation®Store are configured using a combination of the following two types of product elements.

* **Unified entitlement:** Product element incorporated from PlayStation®5, PlayStation®4. Entitlement integrating DRM content (the product elements prior to PlayStation®4) and service entitlement.
* **Service entitlement:** Entitlement data managed on the server of PlayStation™Network to which the number of usable times or a validity period can be set. For PlayStation®5, service entitlements are migrated to unified entitlement fully, and unified entitlements must be used for all purposes going forward. However, already created service entitlements are still usable.

Product attributes can be used for setting eligibility rules which manage purchasability of products in the PlayStation®Store according to a user's past purchases.

Product types and attributes are described in more detail in the [PlayStation™Network Commerce Service Overview](../PSN_Commerce_Service-Overview/__document_toc.html).

# Examples of Products

The most typical examples of products that can be realized using the PlayStation™Network commerce service are described below, along with their technical points. More examples and a more detailed explanation are provided in the [PlayStation™Store Content Guidelines](../PlayStation_Store_Content-Guidelines/__document_toc.html) document; refer to it as necessary.

## Downloadable Games

Distribute stand-alone, full-set applications (downloadable games) as unified
entitlements. It is also possible to distribute free demos or trial editions of
subset applications.

## Additional Content

There are two types of additional content, one is additional content with extra data
that has game packages distributed from the PlayStation®Store, and the other is
additional content without extra data where only entitlement information is
associated with it.

Note:

Additional Content should be linked using the PlayStation®Store Delivered Content
service. Products linked by the Commerce Catalog and Entitlements services are
not accessible through AppContent or the NpEntitlementAccess library and
therefore will be unable to be mounted during gameplay.

**Additional Content with Extra Data**

Data or usage entitlement of additional items, characters, and scenarios used in a
game can be distributed as unified entitlements. Place such data in the Title Store
so that it is available for purchase only from the applicable application.

Create a game package with data for distribution and the content information files
(required for game data), or with an entitlement key and content information, and
register this package as a PSAC
unified
entitlement.

When such data is purchased, it is automatically installed to system storage by the
user's selection. The application can reference a file or an entitlement key in the
additional content directory by using the AppContent library and the
NpEntitlementAccess library. The application must be programmed to check if a file
or an entitlement key exists, and then use it if found.

**Additional Content Without Extra Data**

Distribute usage entitlement of items without data, for example, unlocking a feature
to be used in a game, as PSAL
unified
entitlements. Similar to additional content with extra data,
place such data in the Title Store so that it is available for purchase only from
the applicable application.

There is no need of a package for additional content without extra data. Set an
entitlement key and content information when creating a unified entitlement.

Although no data is installed to storage, the application can reference an
entitlement key by using the NpEntitlementAccess library. The application must be
programmed to check if an entitlement key exists, and then use it if found.

## Consumable Items

Ammunition and fuel are examples of consumable items, which can be used only a
certain number of times in a game. Such items can be realized using PSCONS
unified
entitlements, which have the right to consume an item a certain
number of times. When a unified entitlement is purchased, the number of times that
the user can use the item is increased.

When attaching a unified entitlement for a consumable item to a SKU, set the number
of usable times.

Before using an item, the application must use the NpEntitlementAccess library to
check the number of usable times left in the item. This information is available on
the PlayStation™Network server. When the item is consumed, the application must
again use the NpEntitlementAccess library to notify the PlayStation™Network server
of this event.

## Subscription Network Services

Fee-based subscription services can be provided on the game server using PSSUBS
unified
entitlements with expiration times. Such services can be realized
as described above, or the game server (instead of the client application) can be
used to verify the validity of the user's entitlement.

When using the game server for verifying the validity, use the Entitlements Web API
to obtain entitlement information from the server of PlayStation™Network, verify the
entitlement information and control accesses to the server according to the result
of the verification.

## Virtual Currency

Realize virtual currency using a PSVC
unified
entitlement. The amount of virtual currency that the user gets
when the user purchases virtual currency is not associated with the unified
entitlement itself, but to the SKU linked with the unified entitlement. Each unified
entitlement has a package type field that specifies the role that the entitlement
fulfills. Consumption of virtual currency and management of the remaining balance of
virtual currency should be done on the game server. Virtual currency policy also
requires transfer of virtual currency purchased from PlayStation™Network server to
the game server. Refer to the [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html) for more details on
consumption. Refer to the [Virtual Currency Tutorial](../Virtual_Currency-Tutorial/__document_toc.html) for an end to end
implementation of virtual currency including transfer of entitlements to the game
server.

# Product Browsing and Purchasing

## In-Game Browsing

In in-game browsing, the product browsing feature is provided within the application by a uniquely developed user interface, with the purchase processing carried out by the system. More specifically, the application uses the In-Game Catalog Web API to obtain product information from the PlayStation™Network server, displays that information onscreen in a unique browsing format, and enables the user to select a product. When the user selects a product to purchase, the application opens the NP Commerce Dialog in checkout mode, whereby purchase processing is carried out by the user interface provided by the system software.

## System Browsing

In system browsing, the product browsing feature is carried out by the user interface provided by the system software in addition to purchase processing. More specifically, the application opens the NP Commerce Dialog in the category browser mode or product browser mode. Purchase processing is automatically called from this user interface.