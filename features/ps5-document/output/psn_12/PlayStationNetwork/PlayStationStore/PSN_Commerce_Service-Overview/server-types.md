# PlayStation™Network Commerce Service Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce_Service-Overview/server-types.html

# Development Support

This section provides additional information for developers who use PlayStation™Network.

# Development Support Tools and Client Libraries

To manage access privileges in the development environment, to create and manage products and catalogs, and to set unified entitlements and service entitlements, use the tool that is described in [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

There are separate tools for creating a game package (program files, data files, and entitlement key that are encrypted and packaged in a prescribed format).

To access the Title Store from within the application, use the following utility/libraries/APIs:

* In-Game Catalog Web API
* NpCommerce library
* NpCommerceDialog library (PlayStation®5, PlayStation®4)

A function to preview the Title Store is provided from the system software menu. It is also possible to test the purchasing process using a special credit card number, by which your wallet can be charged without an actual deduction being made from your account.

To verify unified entitlements and service entitlements within the application, use the following utility/library/APIs:

* NpEntitlementAccess Library (PlayStation®5, PlayStation®4)
* Entitlements Web API (Server to Server)

To learn more about how to test the wallet charging, please see [PlayStation™Network Commerce Programming Guide - Development Support Functions - Wallet Charging](../PSN_Commerce-Programming_Guide/wallet-charging.html).

To learn more about modifying accounts and their properties in a development environment, refer to the [DevAdmin Tool User's Guide](../DevAdmin_Tool-Users_Guide/__document_toc.html).

To manage entitlements on you account(s), refer to the [Commerce Editor reference](https://p.siedev.net/resources/documents/SDK/latest/Development_Accounts-Users_Guide/0005.html#__document_toc_00000016).

# Server Types

PlayStation™Network has three environments:

* Development environment - Used by developers.
* Certification environment - Used by SIE to perform platform certification.
* Production environment - Used by end users.

Each of these servers is independent. Changes made in the development environment, for example, do not affect the Certification environment or the production environment.