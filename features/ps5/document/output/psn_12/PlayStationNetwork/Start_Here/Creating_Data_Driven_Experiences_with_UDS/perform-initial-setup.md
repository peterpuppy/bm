# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/perform-initial-setup.html

# Perform Initial Setup

This phase entails the basic setup tasks that you must perform before you can design, implement, and test data-driven experiences.

# Register Concepts and Products

This topic links to information about registering concepts and products. Concepts and products are created in Content Pipeline. In Content Pipeline, a concept is a grouping of typically related products and content, whereas a product represents the content that customers can download in the PlayStation™Store.

Creating a concept, product groups, and products within those product groups is required
before you can request PlayStation™Network services. Content Pipeline provides the
required NP Title ID necessary to request services. You can find the NP Title ID on
the Product Details page of Content Pipeline after creating your products.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Concepts, Product Groups, and Products in Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/Concept_Products_ProductsGroups.html) | Defines concepts, product groups, and products and describes how they relate to each other. |
| [Creating a Game Concept in Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/Concept_FullGameCreate.html) | Explains the process for creating a game concept. |
| [Creating a Full Game in Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/ProductGroup_FullGameCreate.html) | Explains the process for creating product groups and adding additional regional products within each product group. |

# Set up Title Privileges

Accounts for PlayStation™Network are assigned to individuals who will be debugging or testing experiences.
Title privileges ensure that sensitive details about your game are not exposed during
development.

To achieve this, some PlayStation®5 features, such as activities, can
only be viewed or accessed from PlayStation™Network accounts that have a Title Dev
or Title Admin role assigned. Activity cards and related features, such as Game Help,
will not display if the user's account does not have the proper title privileges.
As you set up your accounts for PSN for development and testing, be sure to also configure
title privileges as appropriate. See the document listed below for more information.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Overview](../PSN-Overview/__document_toc.html) | Contains information under [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html) about configuring title privileges for accounts. |

# Set up PlayStation™Network Services

This topic links to information about setting up PlayStation™Network services for your
products via DevNet.

"PlayStation™Network services" refer to a broad range of functionality that is available
for your products.

While Content Pipeline and DevNet are separate systems, you must separately register titles
and products in both systems. To enable the data-driven experiences described in the
Data-Driven Experiences section, you will need to request, at a minimum, the following
services:

* Universal Data System - or all experiences
* Trophy 2 - for trophies
* Leaderboards - for challenge activities

  Note:
  Other services may be required for developing, packaging, and publishing your product.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) | Explains the service request process and provides instructions for creating products on DevNet and making service requests on DevNet.  While this document covers requesting all types of services, for the data-driven experiences described in this document you will need to request the services mentioned above. |