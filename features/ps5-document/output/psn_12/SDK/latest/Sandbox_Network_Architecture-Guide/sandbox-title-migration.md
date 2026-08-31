# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-title-migration.html

# Titles in Sandbox

This topic outlines the options available for getting titles into the Sandbox network architecture. It covers migrating existing titles and creating titles directly in Sandbox.

Titles must be in the Sandbox network architecture. You can either migrate existing titles or create new ones in Sandbox.

## Migrating Existing Titles

When your title is migrated to Sandbox, your configurations for PlayStation™Network features such as the Universal Data System (UDS), Trophy, and Leaderboards are exported from Legacy and copied into Sandbox. Products, concepts, and entitlements that you've configured through Content Pipeline are also copied.

SIE aims to migrate all eligible titles by the conclusion of the 2026 calendar year. SIE will provide guidance and support to ensure a smooth transition and will be in direct communication with you regarding the specific timing and logistics of your title migrations.

To request the migration of a title, submit a ticket via DevNet. SIE will review these requests and work with you to accommodate your project's needs wherever possible.

Note: Migration is one-way. Once complete, all future development work must occur in Sandbox. You are no longer able to use Legacy PlayStation® environments for migrated titles.

**Preparing for Migration**

To prepare a title for migration, do the following:

1. Ensure there are no scheduled patches for the title set in GEMS.
2. Ensure there are no upcoming submissions during the two week period following the migration.
3. If you have not already done so, request NP Communication ID based services for the title such as UDS.
4. Ensure that the title is eligible for migration:

   **Titles Eligible for Migration**

   * PlayStation®5 titles and PlayStation®4 titles using cross-gen SDKs.
   * Partner-managed servers such as App Server, App Server (Client Credentials), Authorized App, or Back Office Server. The migration process for these specialized NP Title IDs does not trigger the movement of any configuration data. It signals to SIE that requests from these clients to Legacy endpoints should be automatically sent to Sandbox. Therefore, you should only migrate your client credentials if you have also migrated all of the game titles that access the server. SIE can work with you to migrate all of the titles and the server together.

   **Titles Not Eligible for Migration**

   * Legacy PlayStation®4 APIs that are not included in the cross-gen SDK, such as NpMatching2 and NpScore.
   * Titles that are scheduled for, or are in the process of, certification. If you are planning to submit a patch release, or have an unpublished patch that is ready to release, complete that process before migrating the title.

**Title Migration Process**

After you've completed the steps above, SIE will migrate your title. After your tile is migrated, [make any necessary code updates](game-and-server-code.html "This topic provides guidance on adapting game and server code to accommodate the Sandbox network architecture changes. It highlights changes to network API requests and access token modifications.").

Migration is conducted in batches to accommodate dependencies between titles. If titles are interdependent, they are migrated together within the same batch. A batch can include a single game, a group of related games, or all titles, servers, and products belonging to your organization.

Migration takes approximately 1 hour. During this time, the following functions are temporarily disabled:

* Title privilege assignment for accounts for PlayStation™Network
* Service configuration
* Packing publication

Access to these functions is restored once migration is finalized. Don't make any changes to the affected titles while migration is in progress. Once migration is complete, do the following:

1. Download a new copy of *npconfig.zip* and rebuild your game package.
2. Republish packages that were previously published in Legacy into Sandbox to facilitate post-migration testing.
3. Log into your DevKit or TestKit with your migrated account.
4. Switch your DevKits and TestKits to Sandbox mode.
5. Ensure that the title launches as expected on your DevKit or TestKit in Sandbox mode.

If any blocking issues arise during migration, you will receive a notification indicating that migration was not completed. In such cases, SIE will investigate and arrange for a subsequent migration attempt.

## Creating New Titles in Sandbox

See [PlayStation™Network Service Setup Guide - Registering Titles - Creating a New Product](../PSN_Service_Setup-Guide/creating-a-new-product.html) for information on how to create new titles in Sandbox.