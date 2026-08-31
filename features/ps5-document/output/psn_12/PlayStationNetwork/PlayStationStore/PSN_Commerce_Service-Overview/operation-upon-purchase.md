# PlayStation™Network Commerce Service Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce_Service-Overview/operation-upon-purchase.html

# PlayStation®Store

PlayStation®Store is the online store of PlayStation™Network's commerce service. The products provided in PlayStation®Store are a combination of programs or data to be downloaded and entitlement data managed on PlayStation™Network.

# Regional Store and Title Store

PlayStation®Store includes the Regional Store, which can be accessed from the system software menu, and the Title Store, which can be accessed from an application.

The Regional Store is organized by country/region and platform. When the user selects "PlayStation®Store" from the system software menu, the Regional Store of the user's country/region of residence is accessible. A list of products offered for the platform in that region is displayed. The Regional Store can be used without any dependency on the application, for example, it can be used for selling downloadable games or distributing demos and trial versions of games.

The Title Store is unique to an application. It cannot be accessed from the system software screen or from a different application unless requesting shared PlayStation®Store Delivered Content or Commerce Catalog and Entitelements service linked content. For more details, see [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html). The product purchasing workflow includes obtaining the product list from PlayStation™Network within the application and having the end user select a product to make a purchase. The Title Store is ideal for selling and distributing additional items used in the application.

Note:

A library exists to carry out the entire process of displaying a list of products to
the user, having the user select a product, and processing the purchase. If a unique
user interface is not required and the system-defined user interface is sufficient,
see [NpCommerce Library Overview](../NpCommerce-Overview/__document_toc.html) for guidance.

# In-Game Catalog

In-Game Catalog manages the products and categorization information of products displayed in the Title Store. For PlayStation®5, the In-Game Catalog structure can have a mixture of products and categories under the root category as well as subcategories, as shown in the sample tree structures in the figure below.

The categories to which a product belongs are configurable as necessary.

In-Game Catalog Structure

The products can be published to the Development environment using the Product Preview option in Content Pipeline. The products can then be previewed using the Regional Store option in the Store Preview application provided by the system.

For more details on In-Game and Store Catalog, see [In-Game Catalog Overview](../../../WebAPI/latest/In_Game_Catalog-Overview/__document_toc.html). For more information on product and catalog setup guides for regional and title stores, see the [Content Pipeline User Guide](https://learn.playstation.net/bundle/content-pipeline).

The Regional Store Preview option in the Store Preview application is for development purposes only and is not representative of how your product appears when displayed on PlayStation®Store.

# Wallet

Payments in PlayStation®Store are processed by deducting the price of a product from the user's wallet.

You must set the product price in the currency of the country/region where the product is to be provided. See [Additional Information](additional-information.html) for more details.

A wallet can only be held by a master account (parent user). The price of a product purchased from a sub account (child user) is deducted from the wallet of the master account. If it is necessary to set a limit of monthly spending, a system exists for doing so.

# Operation upon Purchase

When a user purchases downloadable products from PlayStation®Store, the system downloads the content and installs it after processing the payment. Entitlements associated with the product are acquired by the user in the checkout process. The application knows if entitlements are owned by the user and processes them as needed.

# Types of Products Distributed in PlayStation®Store

The products distributed in PlayStation®Store are configured from the following three types of product elements:

* **DRM content:** Software and data downloaded by the user and saved to
  storage.
* **Service entitlement:** Entitlement data managed on PlayStation™Network that can
  have a set validity period or a limited number of usage times. Service entitlements
  are integrated into unified entitlements for PlayStation®5.
* **Unified entitlement:** Entitlements integrating Digital Rights Management (DRM)
  content and service entitlement products for PlayStation®5 are comprised of unified
  entitlements only, however, they can include service entitlements that were created
  for existing PlayStation®4 products.

## Product Examples

The following are examples of product types sold on PlayStation®Store:

* **Downloadable Applications:** Applications that are booted from storage.
  They can be full titles or demos/trial editions of game packages. The
  application is downloaded and installed by the system, so there is no need for
  the application to take note of the download and installation processing.
* **Additional Items:** Data of additional scenarios, characters, and items to
  be used in the application can be distributed as products. Multiple additional
  items can be provided for a single application. Additionally, you can distribute
  a flag that corresponds to the applicable data, rather than distributing the
  actual data itself. Data is stored to storage as additional content, meaning it
  is stored within the application-specific game data directory. The subdirectory
  and file name must be specified in advance.
* **Applications Upgradable from a Trial Version to a Product
  Version:**Mechanisms referred to as "paid key packages" and "upgradable
  applications". These mechanisms can be used to distribute free trial versions of
  applications with restrictions in functionality, with keys to unlock the
  restrictions later.
* **Consumable Items:** Gives users the right to consume an item a certain
  number of times. Consumable items can be realized using unified entitlements.
  For example, ammunition in a game that can only be used a certain number of
  times. The number of times a unified entitlement has been used is managed on
  PlayStation™Network. The application is only required to find out the number of
  usable times left in an item and to notify the server of the number consumed. If
  data on storage is lost due to hardware problems or user operation, the number
  of times an item has been used can be managed safely.
* **Subscription:**Monthly billing of game server access for fee-based
  subscription services can be realized using unified entitlements with validity
  periods. It is also possible to provide subscription services without a validity
  period or to set automatic updates for services that reach their expiration
  date. There are two ways to determine whether a service is available to a user.
  The first is for the application to obtain information from PlayStation™Network.
  The second is for the game server to obtain the relevant information from
  PlayStation™Network. Use the Entitlements Web API for subscription products on
  PlayStation®4 and PlayStation®5 platforms, and S2S for subscription products for
  other platforms.
* **Virtual Currency:**Virtual currency can be realized using a unified
  entitlement. The amount of virtual currency that the user gets when the user
  purchases is not associated with the unified entitlement itself, but with the
  SKU linked with the unified entitlement. Each unified entitlement has a "package
  type" field that specifies the role that the entitlement fulfills. The remaining
  user's balance of virtual currency must be managed on the game server. See
  [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html) for more details.

## Eligibility Rules

PlayStation®Store makes use of eligibility rules that control what products a user can purchase depending on the user's purchase history. For example, it is possible to only allow users that have purchased the base game to purchase an expansion pack, or to allow users to choose from two possible expansion packs. To learn more, see the [Eligibility Rules guide](https://learn.playstation.net/bundle/content-pipeline/page/PricingAvailability_EligibilityRules.html).

# Product Structure

The figure below shows the product-setup structures for PlayStation®4 and PlayStation®5 products.

Data Hierarchy

The Content Pipeline of the PlayStation®5 platform introduces a new hierarchical data structure composed of new entities that include Concepts, Product Groups, and Products. This hierarchy in Content Pipeline replaces the older hierarchy of Titles and Products that the Product Management Tool uses for PlayStation®4 products. Instead of creating SKUs in the Product Management Tool, publishers of PlayStation®5 products create Pricing & Availability Record in Content Pipeline. For more information, see the [Content Pipeline online help documentation](https://learn.playstation.net/bundle/content-pipeline).

## Service Entitlement

A service entitlement is a legacy product element that gives certain privileges to the user. This type of entitlement should only be used if an existing PlayStation®4 functionality that uses this type of entitlement needs to be extended to PlayStation®5. For PlayStation®5, all functionality of service entitlements is migrated to unified entitlements. Use unified entitlements for new products in PlayStation®5, including consumable items and virtual currency.

## Unified Entitlement

A unified entitlement is a product element incorporated for PlayStation®5 and PlayStation®4. It integrates DRM content and service entitlements. Use unified entitlement for all product elements for PlayStation®5 and PlayStation®4.

One unified entitlement can correspond to one "package", for example, program files, data files, and entitlement keys that are encrypted and packaged in a prescribed format. Note that several types which don't correspond to a package also exist. The types of packages available according to usage are as follows.

* Application package
* Additional content package

  + [PSAL](https://p.siedev.net/resources/documents/SDK/latest/PlayStation_Store_Content-Guidelines/0005.html#__document_toc_00000014)
    No extra data (only entitlement information)
  + [PSAC](https://p.siedev.net/resources/documents/SDK/latest/PlayStation_Store_Content-Guidelines/0005.html#__document_toc_00000012) With extra data (entitlement information and downloadable data)
* PSVC Unified entitlement used for virtual currency (no package required)
* PSCONS unified entitlement used for consumables (no package required)

When a user purchases and downloads a unified entitlement, the corresponding game package content is installed in storage by the user's selection. Access privilege to the installed file is managed based on the user account. It is not possible to access a file that has just been copied without following the proper installation process.

Entitlement information included in a unified entitlement can be confirmed by the application using the NpEntitlementAccess library API. A method is provided for the game server to send a query to PlayStation™Network using the Entitlements Web API to determine the existence of or lack of a privilege.

For more information, see [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html).

## Digital Rights Management (DRM)

The DRM of PlayStation™Network's commerce service is carried out in PlayStation®5 as follows:

* Unified entitlement purchases are recorded per PlayStation™Network account.
* In a PlayStation®5 activated as "Console Sharing and Offline Play" for the account that made the purchase, the user who made the purchases as well as any other users logging into the PlayStation®5 can also use unified entitlements. It is not necessary to sign in with the account that made the purchase. Downloading can only be performed by the user who made the purchase.
* In a PlayStation®5 which is not activated as "Console Sharing and Offline Play" for the purchased account that made the purchase, unified entitlements can be downloaded and used when the user who made the purchases is logged in and signed in with the account. Other members sharing the PlayStation®5 can also use unified entitlements, but only while the user who made the purchases is logged in and signed in with the account. If a unified entitlement is an application, starting the application is limited to the user logged in and signed in with the account that made the purchase.
* In a PlayStation®5 console, any user can start a media application and doesn't need to go through a purchase or download to get the entitlement for the application on their account.
* In PlayStation®5, the home shareable entitlement types are PSGD, PSAC, PSAL, PSMEDIA, PS4GD, PS4AL, and PS4AC.

When allowing users who have not made a purchase to use unified entitlements for a limited time, particular care is required in complying with the [Technical Requirements Checklist for PlayStation®5](https://p.siedev.net/resources/documents/TRC/latest/TRC/__toc.html) (TRC) [[R5116](https://p.siedev.net/resources/documents/TRC/latest/TRC/R5116_testcase.html)] regarding invalidation of an additional content. For details, refer to [[R5116](https://p.siedev.net/resources/documents/TRC/latest/TRC/R5116_testcase.html)].

# Promotion Codes

Promotion codes are codes that can be exchanged for specific products in PlayStation®Store. Codes are strings formatted as three sets of 4-digit alphanumeric characters joined by hyphens, for example, `AAAA-A111-111A`. Users can enter promotion codes in the code input form on devices that support PlayStation™Network to purchase the products associated with the promotion codes.

You can request vouchers from Content Pipeline. Voucher type SKUs do not appear in PlayStation®Store and they can only be obtained by entering a promotion code.

Promotional codes can be ordered using the Codes application. For more information, see [Getting Started with Codes](https://learn.playstation.net/bundle/3p-codes-guide_partner-3p_codes/page/3P-GettingStarted.html). The number of times a promotion code can be issued, the number of promotion codes that can be issued, and the distribution methods and conditions vary depending on the region. Contact SIEJA/SIEA/SIEE before ordering promotion codes.

Note:

In addition to promotion codes for product versions, it is also possible to make requests for obtaining promotion codes for development or testing. See [Voucher Code Redemption Testing](https://learn.playstation.net/bundle/content-pipeline/page/Product_BundleVoucherSubmit.html) for details.

The NpCommerceDialog library for PlayStation®5/PlayStation®4 allows you to customize how users input codes. See [NpCommerceDialog Library Overview](../NpCommerceDialog-Overview/__document_toc.html) for more details.