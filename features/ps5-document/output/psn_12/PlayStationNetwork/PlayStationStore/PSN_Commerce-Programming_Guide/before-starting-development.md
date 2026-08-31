# PlayStation™Network Commerce Programming Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce-Programming_Guide/before-starting-development.html

# Overview of the Development Process

To develop for the PlayStation™Network commerce service, you need account access to the PlayStation®5 DevNet website and the Content Pipeline. You use these sites to create product infrastructure that the PlayStation®Store requires to register content. After content is registered, you can use it in the PlayStation™Network development environment to test commerce-related functionality that your application provides.

# Before Starting Development

Registration is required before starting development of products and applications that
use the PlayStation™Network commerce service.
For
more information, see [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

It is necessary to configure network settings correctly and to create an account for the
PlayStation™Network in order to access the PlayStation™Network server from the
Development Kit. For more information, see the [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)
document.

# Product and Application Development

To develop applications that access the PlayStation®Store for purchasing items and
entitlements, as well as to develop additional content and consumable items used by such
applications, take the following steps.

## (1) Create full game and additional content

Additional content products are of the following types: PSVC, PSCONS, PSAC and
PSAL.

* For PlayStation®5, partners can use Content Pipeline to create all these
  products.
* To create PSGD/PSAC entitlements, a package needs to be created using packaging
  tools.
* To create PSAL entitlements, a zip file needs to be created and then uploaded to
  GEMS. For more information, see the [Creating Additional Content Packages Without
  Extra Data](https://p.siedev.net/resources/documents/SDK/latest/PlayStation_Store_Content-Guidelines/0005.html#__document_toc_00000014) page.

For more information, see the following:

* For information about using Content Pipeline to set up products, see the [Content Pipeline online help
  documentation](https://learn.playstation.net/bundle/content-pipeline).
* For information about the binary submission process, see [Package/Disc
  Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html).

## (2) Test in the development environment

The application must use the In-Game Catalog Web API and NpCommerceDialog library to
implement processing to access the PlayStation®Store in order to browse and purchase
products. Test the correct implementation of this processing by browsing and
purchasing products created in the development environment.

For unified entitlements of durable items such as PSAC and PSAL, use NpEntitlement Access library to check whether the user has the right to use an item or feature. For more information, see [TRC R5116](https://p.siedev.net/resources/documents/TRC/2023.07/TRC/R5116.html). For unified entitlements of consumable items such as PSVC and PSCONS, use the Entitlement Web API to check whether the user has the right to use and item or feature. For more information, see [Entitlements Overview - Handling Consumable Entitlements](../../../WebAPI/latest/Entitlements-Overview/handling-consumable-entitlements.html). Test for the correct implementation of this processing.

Test Purchasing of Unified Entitlements

## (3) Certification

After testing by the licensee in the development environment, the product is published to the Certification environment, where SIE conducts testing.

## (4) Release

After all testing, the product is transferred to the production environment and be
made available to the end user. At this time, the final encryption process is
executed on the product.