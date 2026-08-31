# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/accounts-for-development-for-sandbox.html

# Accounts for Development in Sandbox

This topic outlines the process for creating new accounts for development in Sandbox and explains the migration process of accounts for development in the Legacy architecture.

To set up a Sandbox development account, you must either create a new account or use an existing account that SIE has migrated from Legacy.

## Creating Accounts for Development in Sandbox

Create Sandbox development accounts using Host Tools or *Quick Sign-Up* within DevKit and TestKit. You can't create Sandbox development accounts using other methods.

If given the appropriate permissions, you can use the same development account for both DEV and CERT.

For instructions on creating a new account, see [PlayStation™Network Overview - Reference Information - Creating an Account for Development](../PSN-Overview/creating-an-account-for-development.html).

## Migrating Accounts for Development in the Legacy Architecture

SIE migrated existing accounts for development in the Legacy architecture to Sandbox, copying account information from sp-int into DEV.

The following are key points to understand about the migration process which may have impacted data on the account:

* If the sign-in ID already existed in the destination environment, "+SB" was added to the sign-in ID of the Legacy account, just before the "@" symbol. For example, "tester@sony.com" would have become "tester+SB@sony.com". If adding "+SB" put the sign-in ID over the 64 character limit, the account was not migrated.
* If the online ID already existed in the destination environment, a new online ID was generated and assigned to the account.
* If the account ID already existed in the destination environment, the account was not migrated.
* Phone numbers on the Legacy account were not migrated to the new account.
* Accounts that used 2SV authentication in Legacy were changed to use standard authentication in DEV.
* Entitlements associated with the account were not copied over. To add necessary Entitlements, see [PlayStation™Network Commerce Programming Guide - Development Support Functions - PlayStation™Network - In-Game Commerce Debug](../PSN_Commerce-Programming_Guide/psn-in-game-commerce-debug.html).
* The account password was migrated as-is.
* Title privileges granted through DevNet and the Development Accounts Tool (DAT) in Legacy are automatically applied to corresponding Sandbox development accounts when the titles themselves are migrated.

The table below describes what data was migrated:

| **Data Category** | **Was Migrated** | **Exceptions** |
| --- | --- | --- |
| Core account data (name, email, password, etc) | Yes | * Phone numbers were not migrated. * If a migrated account's online ID and/or sign-in ID already existed in Sandbox, the migrated account's online ID and/or sign-in ID were updated. |
| Entitlements | No | N/A |
| Friends and block list | Yes | N/A |
| Game play data | No | N/A |
| Title permissions | Yes | * Title permissions are not migrated until the title is migrated to Sandbox. |

## Managing Access Control for Content and Services in Sandbox

Sandbox introduces a modern access control model that combines certificate and OAuth access tokens. This ensures that only authorized developers and systems can access specific titles and services.

In the Legacy architecture, title separation was enforced through Network Platform Management Tool (NPMT) roles. In Sandbox, this is replaced by a certificate-based model that encodes access control directly in the OAuth access token.

Each developer or DevKit / TestKit authenticates using:

* Certificates managed by the Certificate Management Service (CMS).
* Authorization logic provided by the Sandbox Auth Service.
* Access tokens issued by OAuth, which now include:

  + Title access lists
  + Cross-title restriction flags
  + Sandbox identifiers (for example, DEV or CERT)

**Role Permissions**

Partner accounts that already have access to a title can assign that title to an account for PlayStation™Network through DevNet/DAT. This replaces the role–based title assignment workflow. With Sandbox, title associations are handled through certificates.