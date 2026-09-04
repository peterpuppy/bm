# PlayStation™Network Service Setup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Service_Setup-Guide/registering-titles.html

# Registering Titles

Understanding DevNet *products* and *product types* is necessary for requesting PlayStation™Network services. This chapter provides an explanation of these concepts.

# Title Management on DevNet

This topic provides information on how to manage titles and products in DevNet.

This document uses the term *DevNet* to refer to the SIE Developer Network web portal.

For each PlayStation® platform, the SIE DevNet portal presents a separate web application that has a platform-specific name and URL. PlayStation™Network documentation refers to each platform-specific web app as a unique *DevNet site*. The DevNet site for PlayStation®4 is called "PlayStation®4 DevNet" and it appears at the <https://ps4.siedev.net> URL. For PlayStation®5, it's "PlayStation®5 DevNet" at <https://p.siedev.net>.

Each DevNet site enforces its own access controls. When you log in, the PlayStation™Partners global header shows you the list of DevNet sites that you can access (see figure below).

Select "PlayStation®5 DevNet" to access.

PlayStation™Partners Global Header

## Products in DevNet

Each client program that uses a PlayStation™Network service is a *product* in DevNet, including applications that run on a PlayStation® console or on a game server. Each product must have an NP Title ID that identifies the product uniquely. The NP Title ID is generated when the product is registered on Content Pipeline (for PlayStation®5 and PlayStation®4, after getting Content Pipeline access for PlayStation®4) or TPRnet (for PlayStation®4, before getting Content Pipeline access for PlayStation®4 and other PlayStation® platforms).

A client program that runs on a PlayStation® console must be managed and registered in each platform specific DevNet site that it supports. For example, a PlayStation®4 product having an NP Title ID that begins with the CUSA prefix is registered on the PlayStation®4 DevNet site.

However, this workflow changes for PlayStation®4 products that use the PlayStation®4 Cross-Gen SDK. Any product that uses the PlayStation®4 Cross-Gen SDK must be registered and managed on the PlayStation®5 DevNet site, which appears at the <https://p.siedev.net> URL.

To migrate PlayStation®4 products registered on the PlayStation®4 DevNet over to PlayStation®5 DevNet, see [Migrating a PlayStation®4 Product to PlayStation®5 DevNet](migrating-a-ps4-product-to-ps5-dev-net.html "This topic provides information on how to migrate a product registered on PlayStation®4 DevNet to PlayStation®5 DevNet.").

## DevNet Title/Product Hierarchy

On DevNet, products have a hierarchical structure where they belong to *franchise* and *title* categories.

The franchise category is the most external container. A franchise typically corresponds to a *game series*, and inside a franchise, there can be one or multiple titles. Titles are usually different games that belong to the same franchise.

Each title contains one or multiple products (North American version, European version, related server applications, etc.) of the same game. See figure below.

Product Configuration on DevNet

## Registering Products on Content Pipeline and DevNet

Content Pipeline and DevNet are separate systems at this time. You must register titles and products in both systems separately. To do so, take the following steps:

1. Register your PlayStation®5 concept, product, and title in Content Pipeline. Refer to [Concepts, Products Groups, and Products in Content Pipeline](https://learn.playstation.net/csh?context=ConceptProductsProductsGroups_CP) for more information about this process.
2. Register your PlayStation®5 title and product on the PlayStation®5 DevNet site as the table below describes.

Content Pipeline Registration Information

| Entity on DevNet | Entity on Content Pipeline |
| --- | --- |
| Franchise | Use the Franchise Name from Content Pipeline as the Franchise Name in DevNet. |
| Title | Use the Concept Name from Content Pipeline as the Title name in DevNet. |
| Product | Use the Product Name from Content Pipeline with a suffix that indicates the platform on which the product runs and the variation of the product.  For example, if the Product Name in Content Pipeline is "Sample Shooting" and the product runs on PlayStation®4 with an English translation, you would enter "Sample Shooting (PS4 - English)" as its Product Name value in DevNet. |

# Supported Product Types

This topic provides information on product types and how they are used in DevNet.

There are various categories for products on DevNet, and these categories are called product types.

Provided services differ by product type. Select the appropriate product type according to the product to create.

The table below describes the appropriate product type to request when registering your product on the PlayStation®5 DevNet site.

Product Types

| Product Type | Description |
| --- | --- |
| **App (PS5)** | Use the **App (PS5)** product type for your PlayStation®5 game or application that is to be submitted to Platform Certification and Operations. This product type includes upgradable applications and trial/demo versions.  You can also use this product type for prototype and testing purposes, like the Test product type previously available. The Test product type has been deprecated.  When registering this product type, you must use the NP Title ID that is issued in Content Pipeline when creating a "Full Game", "App" or "Demo" product. For more information, see [Creating a Full Game Product in Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/ProductGroup_FullGameCreate.html). |
| **App (PS4 Cross-gen)** | Use the **App (PS4 Cross-gen)** product type for your Cross-gen-SDK-built PlayStation®4 game or application to be submitted to Platform Certification and Operations. This product type includes upgradable applications and trial/demo versions.  When registering this product type, you must use the NP Title ID that is issued in Content Pipeline when creating a "Full Game", "App" or "Demo" product. For more information, see [Creating a Full Game Product in Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/ProductGroup_FullGameCreate.html).  Any product that uses the PlayStation®4 Cross-Gen SDK must be registered and managed on the PlayStation®5 DevNet site. PlayStation®4 DevNet over to PlayStation®5 DevNet, see Migrating a PlayStation®4 Product to PlayStation®5 DevNet. |
| **App Server** | For products that use the PlayStation™Network Web API to present a user access token. |
| **App Server (Client Credential)** | For products that use the PlayStation™Network Web API with a client-credential access token. |
| **Back Office Server** | For products that use the administrative PlayStation™Network Web API with a client-credential access token. |
| **Authorized App Server** | For products that allow users to consent to sharing their PlayStation™Network data with your services. Consent is required for non-operational purposes, in other words, usage beyond what's required to run your application on PlayStation® consoles. For further details, see [Customer Data](https://learn.playstation.net/bundle/policies-and-business-model-guidelines/page/Customer_Data.html). The server uses an access token, (rotating refresh token for offline access), to call the PlayStation™Network Web API. You can enter any value for franchise name and title name. Registration of a franchise and concept in Content Pipeline is not required. |

Note:

Some services previously had a limitation of not being able to be used for prototyping and testing purposes. This policy has been changed.

The **App (PS5)** product type can be used for testing purposes and **Test (PS5)** has been deprecated.

# Creating a New Product

This topic provides information on how to create a new product in DevNet.

To create a new product on DevNet, take the following steps:

1. Open the **Add a new product** form.
2. Click **Titles** > **Titles and Products**.
3. Click **+ New product**.

   Adding a New Product
4. Set the franchise and title to which the product belongs in order to match the product's hierarchy between Content Pipeline and DevNet in the same structure.
5. To use an existing franchise in DevNet for creating a new title or a new product, select **Select an existing franchise**. To create a new franchise, select **Enter a new franchise name** and enter the required information.
6. To use an existing title in DevNet, select **Select an existing title**. To create a new title, select **Enter a new title Name** and enter the required information.

   Set the Franchise and Title

   Franchise and title names can be shown in Content Pipeline, as shown in the figure below.

   Content Pipeline Concept and Franchise Name
7. Enter product information.

   The items required to be entered are displayed in accordance with the product type. In accordance with the screen display, enter the information.

   If the product type is **App (PS5)** or **App (PS4 Cross-gen)**, information must be matched in Content Pipeline.

   Required Product Information

   | Input Items | Mandatory/Optional | Expected Information to be Entered |
   | --- | --- | --- |
   | Product Name | Mandatory | Product name registered in Content Pipeline adding platform information and region. For example : "Sample Shooting ( PS5 - English)". |
   | NP Title ID | Mandatory | NP Title ID generated by Content Pipeline. |
   | Content Pipeline URL | Either **Content Pipeline URL** or **Publisher Name** is mandatory | Content Pipeline URL of a product page |
   | Publisher Name | Either **Content Pipeline URL** or **Publisher Name** is mandatory | Publisher name where to be displayed in PlayStation™Store. |
8. Click **Add product** to complete the process and add your product.

   Product Information Page

# Product Access Privileges

This topic provides information on product access privileges in DevNet, and what type of access is granted for each type.

The user who created the product is considered the product owner. Owners can add access privileges for products to other users. A user who has access to the product is called a *collaborator* in PlayStation®5 DevNet. The table below describes access privilege roles.

Access Privilege Roles

| Role | Description |
| --- | --- |
| Viewer | A Viewer can see all other users with access privileges for the same product, its product information, and the setup statuses for any PlayStation™Network services. This role can be assigned to any user who has DevNet access. |
| Editor | In addition to Viewer privileges, an Editor can also change product information and make requests for PlayStation™Network services. This role can be assigned to any user who has DevNet access. |
| Owner | In addition to Editor privileges, an Owner can also add, change, and delete access privileges for products. This role can be assigned to any user who has DevNet access. |
| Content Creator | A Content Creator has limited privileges to configure content for some PlayStation™Network services on assigned products, such as Game Help. You can assign this role to any user with a PlayStation Partners account. |

There are privileges managed as a subset of the collaborator role (Owner, Editor, Viewer). The following table describes the subset privileges.

These privileges do not apply to a Content Creator collaborator.

Subset Privileges

| Additional Privileges | Description |
| --- | --- |
| Crash reporting access | Access to the Crash Reporting Service (CRS) for the product.  This is only available on App Server, App Server (Client Credential) and Back Office Server. |
| Product credential files | Access to the following credential files for the product:   * NP Title Secret / nptitle.dat * Client Secret/Client ID * SSH Key for User Bucket for Partners (UBP) access   Note that available files are different depending on the product type. |

# Setting Access Privileges

This topic provides information on how to set access privileges in DevNet.

To add access privileges for a DevNet product (and for the DevNet Service Thread of that product) for another user, use the following procedure:

1. Log in to DevNet with an account with Owner privileges. Owner privileges are set for the user that created the product on DevNet.
2. Click **View Collaborators** > **Add a collaborator**.

   View Collaborators Menu
3. To add access privileges for a user whose account is visible to you, select the **Add DevNet Colleagues** tab. Enter their username and click **Set permissions**. On the next page, set **Owner, Editor or Viewer** privileges.

   To add access privileges for a user whose account is not visible to you, select the **Add Other Users** tab. Enter their e-mail address, select the **Owner, Editor or Viewer** privileges to be added, select the range of products for setting privileges, then click **Submit request**.

SIE checks the request content and set privileges for the requested user.

Note:

A user with access privileges to a product can view the DevNet service thread of the service requested for the product.

If the DevNet service thread cannot be viewed even when the user has appropriate access privileges, or if the DevNet service thread can be viewed after access privileges are revoked, use the <https://p.siedev.net/support/newissue> page to create a new private support issue.

# Adding Content Creator Collaborator

This topic provides information on how to add a content creator collaborator to a product in DevNet.

A Content Creator collaborator has limited privileges to configure content for PlayStation™Network services, such as Game Help, that are associated with a DevNet product. However, these collaborators do not have access to the DevNet product itself or for the DevNet service thread of that product.

To add these collaborators, follow the steps mentioned in [Setting Access
Privileges](setting-access-privileges.html "This topic provides information on how to set access privileges in DevNet.") and select "Content Creator" as the Role.

# Moving a Product to a Different Title

This topic provides information on how to move a product to a different title.

If your product was created under the wrong title, you can move it to a different title. To do this:

1. Log in to DevNet with an account with *Owner* or *Editor* privileges.
2. Click **Move to Another Title** on the product page, then select the new title to move the product to.

   Note:

   The account must have *Owner* or *Editor* privileges for the product to move and the product under the title where you are moving it to. If candidate titles are not shown, ensure you have correct product privileges.

   Move Product Menu

# Migrating a PlayStation®4 Product to PlayStation®5 DevNet

This topic provides information on how to migrate a product registered on PlayStation®4 DevNet to PlayStation®5 DevNet.

In order to use the PlayStation®4 Cross-Gen SDK on an existing PlayStation®4 product that
has already been registered on PlayStation®4 DevNet, you must migrate the product to
PlayStation®5 DevNet.

## Required User Privileges

You must have the following privileges to migrate a product:

* Access to both PlayStation®4 DevNet and PlayStation®5 DevNet.
* Owner or editor collaborator permission on one product that appears under the
  PlayStation®5 DevNet title to which you intend to migrate the PlayStation®4
  product.
* Owner or editor collaborator permission on the PlayStation®4 product to
  migrate.

## Product Types Eligible for Migration

You can migrate the following product types:

* App
* App Server/Website
* Back Office Website

Each product to be migrated must meet the following criteria:

* No service requests are pending on the product.
* No TRC waiver request are pending on the product.
* No products in PlayStation®5 DevNet have the same product name.

  Note:

  There is no way to distinguish a migrated product from one that is newly
  created on PlayStation®5 DevNet. If you need to distinguish migrated products
  from those which are created new in PlayStation®5 DevNet, you can put
  distinguishing information in the product name. You should use this naming
  convention for **App Server**, **App Server (Client Credential)**, and
  **Back Office** product types.

## Migrating the Product

**IMPORTANT:** Before you migrate a product from PlayStation®4 DevNet to
PlayStation®5 DevNet, consider the following:

* **Migration of a product cannot be undone.**
* Migration creates a new service thread on PlayStation®5 DevNet for any PlayStation™Network service that was requested for the product.
* The collaborators of the product and the subscribers of the service thread remain unchanged. However, any user who does not have access to PlayStation®5 DevNet cannot access the new service thread; the username appears on the service thread in strikeout text. When the user is granted access to PlayStation®5 DevNet, they can access the service thread with the same permissions they used to have.

To migrate a product registered in PlayStation®4 DevNet to PlayStation®5 DevNet, take
the following steps:

1. Log in to PlayStation®5 DevNet.
2. Open the product detail page of any product that belongs to a title that is the
   intended destination of the migration.
3. Click **Migrate Product to PS5**.

   Button to Migrate Product to PlayStation®5
4. Select the product on PlayStation®4 DevNet by searching for its NP Title ID or product name.

   Selecting Product by NP Title ID
5. For App or App Server/Website products, complete the Client ID service request,
   which is required to use the PlayStation™Network Web APIs on PlayStation®4 Cross-Gen
   SDK.