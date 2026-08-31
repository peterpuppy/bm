# PlayStation™Network Commerce Platform Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce_Platform-Overview/content-pipeline.html

# New Commerce Features in PlayStation®5

This chapter describes the different features that are available when using the PlayStation™Network Commerce Platform.

The PlayStation™Network Commerce Platform adds new features for PlayStation®5 and enhances existing features to enable a richer user experience, while maintaining backwards compatibility with previous workflows, APIs, and consoles.

# Game Hub

This topic describes the Game Hub feature.

On PlayStation®5, a game's hub provides a single destination that evolves based on the player's changing goals and needs in varying stages of the game lifecycle and associated states of purchase or gameplay. A single game's hub dedicated to a particular title enables easy access to all products related to that title, such as a variety of game editions, demos, betas, add-ons, virtual currencies, avatars, and more. The title's game hub also presents all of the conversion options for which the gamer is eligible, coupled with customized "call to action" promotions, to facilitate a confident conversion decision that meets the individual player's commitment level.

For example, the figure below depicts an example of the kind of content that a game hub could display when a game has been announced but is not yet available; each of the **Wishlist** and **Follow** buttons provide a "call to action" that the player can take at this stage of the game lifecycle.

Concept-Announce Cover Page

At each stage of the game lifecycle, a game's hub caters to marketing and retail needs that drive awareness, game research, purchase, download, play, and new content drops. A game's hub introduces new and improved features that excite players to invest in a new game, provide information that they need to make a confident decision, and keep them engaged as they progress through the game. These features include the Game Media Strand, Game Highlights, Premium Version Upsell, News Cover Takeover, Activity, Cover Takeover, Activities Strand, and more. For more information, see the [Game and Hub Overview](https://learn.playstation.net/bundle/content-pipeline/page/GameHub_Overview.html).

# Game Hub Preview

This topic describes the Game Hub Preview feature.

The ability to preview a game's hub assets and metadata before publishing content to the live PlayStation™Network Commerce Platform environment is crucial for identifying potential issues and refining the quality of the overall look and feel of a game hub. Previous console generations do not provide this functionality; as a result, product details page assets may not always be updated regularly, and the content may be somewhat limited. PlayStation®5 supports our publishers' need to update live services content frequently and to present it in a rich format. The Game Hub Preview App can increase publisher's confidence level when pushing new assets and metadata to customers, and it can speed up the content-provisioning process. These improvements should increase the freshness and richness of a game's hub content throughout the lifecycle of a game.

Game Hub Preview App

# Content Pipeline

This topic describes the Content Pipeline feature.

PlayStation®5 introduces a new Content Pipeline tool that you can use to set up and publish PlayStation®4/PlayStation®5 digital content to the PlayStation™Store. Content Pipeline includes the following features:

* Globally aligned publishing process that simplifies the submission of data to regional tools
* Integration with Certification Center (previously known as Global FQAweb) for testing
* Integration with TPRnet for publishing
* [Title Store](new-package-types-for-new-unified-entitlements.html#psn-commerce-platform-overview_1_5__psn-commerce-platform-overview_1_5_2) setup and publishing

Content Pipeline

# New Hierarchical Structure in Content Pipeline

This topic describes the hierarchical structure products in of Content Pipeline.

The Content Pipeline of the PlayStation®5 platform introduces a new hierarchical data structure composed of new entities that include **Concepts**, **Product Groups** and **Products**.

The Content Pipeline Product Hierarchy

## Concepts

A *concept* is a single entity that refers to multiple content items for a specific game release. Usually, these content items are related in some way, and they can include avatars or themes. A concept replaces and expands upon the Global Product Proposal as a way of introducing, organizing, and managing an evolving body of content.

A concept contains one or more product groups.

## Product Groups

*Product groups* are specific offerings related to a concept. Product groups within a concept may be related in several ways. For example, a concept may contain all the product groups (full games, demos, add-ons, and so on) related to a specific full game. Alternatively, it may contain a range of different, non-game-related avatars or themes sold by a single publisher.

A product group is offered to customers in the PlayStation™Store.

## Products

A *product* is an individual item for sale in the PlayStation™Store. A product comprises metadata and assets, age ratings, pricing and availability information, and a unique code item. Often, a product is a platform-specific or region-specific version of a product group.

As the single entity that associates all of the items required to make content available on the PlayStation™Store, the *concept* is fundamental to the game's hub experience, providing a way for users to access a set of related product offerings conveniently. For more information, see the Content Pipeline online help [documentation](https://learn.playstation.net/bundle/content-pipeline).

# New Package Types for New Unified Entitlements

This topic describes the new types of entitlement packages available on PlayStation®5.

Because so many platform features or content items may be gated by entitlements, simply using the existing set of PlayStation®4-specific entitlements can make it difficult to understand the particular items that an entitlement manages. To make it easier to understand the specific content and features that new entitlements add to the PlayStation®5 platform, PlayStation®5 introduces new kinds of entitlement packages.

PlayStation®5 introduces the PSGD, PSAC, PSAL, PSVC, PSSUBS and PSCONS package types.

## Regional Store

The "PlayStation™Store" item in the system software menu displays the Regional Store, which presents products that are available for the user's platform in the user's region or country. The Regional Store has no dependency on the application. The Regional Store is appropriate for selling downloadable games and for distributing demos or trial versions of games.

Regional Store

## Title Store

A *title store* is an optional in-game commerce implementation that sells PlayStation™Store content for the game that implements the title store. The Title Store Preview application on PlayStation®5 enables you to preview and test your title store setup. You can enter the Title ID and service label to preview the root category. You can also use this application to test the redemption of a voucher code.

Each title can be previewed and tested only by admin accounts for that title. This feature is known as *title separation*.

Title Store

# New In-Game System Browse and Direct Checkout

This topic describes the System Browse and direct checkout features.

You can use the System Browse application on PlayStation®5 to render your [Title Store](new-package-types-for-new-unified-entitlements.html#psn-commerce-platform-overview_1_5__psn-commerce-platform-overview_1_5_2) with category and product pages.

In-Game Store

To provide an easier, less-intrusive commerce experience, the PlayStation®5 checkout process replaces the PlayStation®4 platform's full-screen takeover with a half-panel system modal dialog overlay.

This less-intrusive overlay enables the user to initiate a purchase at any time without losing game context; the user can easily return to the game immediately after the purchase. PlayStation®4 titles can also take advantage of this feature.

Checkout Application

Alternatively, you can implement your own custom in-game store, known as a [Title Store](new-package-types-for-new-unified-entitlements.html#psn-commerce-platform-overview_1_5__psn-commerce-platform-overview_1_5_2); for more information, see the [Virtual Currency Tutorial](../Virtual_Currency-Tutorial/__document_toc.html) document.

# Entitlements Access Library

This topic describes the NpEntitlementAccess library.

Accessing and consuming service and unified entitlements in the PlayStation®5 platform are now consolidated under the NpEntitlementAccess library.

The NpEntitlementAccess library provides features for accessing additional content and consumable entitlements. A feature is also provided for obtaining the SKU flag that is set for each application.

You can use the NpEntitlementAccess library to perform the following main tasks:

* Obtain the SKU flag
* Access additional content
* Obtain a list of additional content for which the entitlement is valid
* Access an entitlement
* Obtain a valid entitlement
* Consume a consumable entitlement

# Virtual Currency

This topic describes how virtual currencies work on PlayStation®5.

The PlayStation®5 platform changes the virtual currency model and the workflow for consuming virtual currency in order to address difficulties related to PlayStation®4 platform inconsistencies.

PlayStation®5 defines a new unified entitlement type and package type PSVC specifically for virtual currency, separate from the Consumable Service Entitlement in the PlayStation®4 platform. On the PlayStation®5 platform, virtual currency can be consumed only by the licensee game server in a single transaction and must be managed by the licensee thereafter. This model differs fundamentally from that used on the PlayStation®4 platform.

When consuming virtual currency on PlayStation®5, it is important to observe the following guidelines:

* After purchase, all virtual currency must be consumed from PlayStation™Network in a single transaction.
* After consumption from the PlayStation™Network, the licensee's game server must handle all subsequent management of the currency.
* Implement initial consumption of the currency from the PlayStation™Network as an idempotent operation:

  + Licensee game server generates a globally unique identifier (GUID) and sends it with the consume request.
  + If the game server receives a transient error, it should retry with the same GUID. The PlayStation™Network platform will not debit any GUID more than once. The PlayStation™Network consumption interface now guarantees an idempotent response if the calling client uses the API correctly.

For a detailed, end-to-end, example implementation of this consumption pattern, see the [Virtual Currency Tutorial](../Virtual_Currency-Tutorial/__document_toc.html) sample.

In PlayStation®5, the Consumption API is now idempotent; that is, calling the API multiple times has the same outcome as calling it once. Previously, the PlayStation™Network consumption API did not provide an idempotent implementation. A PlayStation™Network client could not retry a consumption request without the risk of accidentally re-consuming an entitlement or receiving a "no funds left" response if, for example, the transaction was processed successfully by the PlayStation™Network server but the response was not received in time by the client.

# Transaction History API

This topic introduces the Transaction History API.

PlayStation®5 introduces a new Transaction History API that is available upon request.

Previously, licensees could not view a PlayStation™Network user's entitlement consumption history, making it difficult for customer-support agents to investigate customer queries regarding missing entitlement consumptions. The new transaction history API retrieves a historical record of customer entitlement consumption transactions. This information can help customer support agents to understand customer actions more clearly, and to resolve these kinds of support requests more efficiently.