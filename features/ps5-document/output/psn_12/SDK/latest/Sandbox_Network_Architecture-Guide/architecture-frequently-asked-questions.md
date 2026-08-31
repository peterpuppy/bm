# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/architecture-frequently-asked-questions.html

# Sandbox Network Architecture FAQ

This chapter covers frequently asked questions about developing titles in the Sandbox network architecture, the migration process of existing titles and accounts for development, and access and title privilege roles.

# Sandbox Architecture

This topic covers frequently asked questions about general Sandbox usage, including when Sandbox will be available, how to access Sandbox on PlayStation®5 development hardware, and what software updates are required.

## When Will Sandbox Be Available?

Sandbox documentation will be released with the next major SDK update, currently targeted for Spring 2026. PlayStation®5 system software that enables access to the Sandbox is currently scheduled to release July 2026. If your title is migrated before this date, we will provide additional guidance on how to access Sandbox using PlayStation®5 system software through our migration communication channel.

## Is a New SDK Required to Use Sandbox?

No. Updating the SDK is not required to access Sandbox.

## Is a System Software Update Required to Use Sandbox?

Yes. A new system software update is required to configure development hardware to connect to Sandbox PlayStation® environments.

## How Do I Access Sandbox on PlayStation®5 Development Hardware?

After updating to the latest system software, you can switch between Legacy and Sandbox network architectures from \*Debug Settings, similar to how you currently switch between development (sp-int) and certification (prod-qa) environments.

For more information, see [Managing Sandboxes in DevKit and TestKit](sandbox-management-on-devkit-testkit.html "This topic provides an overview of managing PlayStation® environments on DevKits and TestKits. It details the differences between sandboxed and global data management, configuration of network architectures, and considerations when downgrading system software.").

## Can Multiple Sandboxes Be Created for a Single Title in DEV Sandbox?

At launch, the DEV sandbox will not support multiple sandboxes per title. Our initial focus is to provide a stable Sandbox foundation with tools and workflows that closely mirror Legacy development (sp-int) and certification (prod-qa) environments, enabling smooth title migration while minimizing disruptions for partners.

Support for multiple sandboxes may be introduced in a future phase. If you have any specific requests related to Sandbox, submit a feature request on DevNet to discuss them with SIE. This will help SIE better understand your needs and prioritize upcoming enhancements.

## Does Sandbox Support Maintaining Multiple Versions of Store Metadata?

This capability is not supported in the initial Sandbox release for the same reasons outlined above. If this feature is important to your workflow, submit a feature request on DevNet to help SIE understand your requirements and prioritize Sandbox-related enhancements.

## Are Code Changes Required on the Game Client Side to Support Sandbox?

No code changes are required for migration. However, in the long term, we recommend updating your code to natively detect Sandbox ID and type to take advantage of future Sandbox enhancements.

## Are Code Changes Required on the Game Server Side to Support Sandbox?

It depends on your game server configurations and whether the server needs to support titles running in Legacy and Sandbox PlayStation® environments at the same time. If support for both architectures is required from the game server, some code changes will be necessary.

For more information, see [Is Migration Required for App Servers (Client Credential), Back Office Servers, and Authorized App Servers?](migration-frequently-asked-questions.html#migration_frequently_asked_questions__section_a25_nw2_m3c), [Updating Game and Server Code](game-and-server-code.html "This topic provides guidance on adapting game and server code to accommodate the Sandbox network architecture changes. It highlights changes to network API requests and access token modifications."), and [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html) for more information.

If you need further clarification or guidance on implementation, contact SIE on DevNet.

## The App Server Currently Routes Requests Based on the Issuer ID. After Migrating to Sandbox, What Issuer ID Value Will Be Returned?

The behavior remains unchanged from the current implementation. The Issuer ID returned depends on the Sandbox PlayStation® environment being accessed:

* DEV sandbox: Same value as the current development environment (sp-int).
* CERT sandbox: Same value as the current certification environment (prod-qa).
* RETAIL sandbox: Same value as the current production environment (np).

As a result, if the App Server is migrated to Sandbox at the same time as the full game, it should generally be possible to validate behavior in Sandbox without requiring code changes.

See [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html) for more information.

## Will Legacy PlayStation® Environments Continue to Be Available?

Yes. The Legacy PlayStation® environments development (sp-int) and certification (prod-qa) will remain available. However, for migrated titles, all new changes can only be published to Sandbox PlayStation® environments. Migrated titles will experience connectivity issues when run in development environment (sp-int), including when connecting from an App Server or Authorized App Server used by a title on a PlayStation®5 development hardware if the server has been migrated. For these reasons, migrated titles must only be run in Sandbox architecture environments. Additionally, changes made in sp-int will not be reflected in the DEV Sandbox.

## When Will Sandbox Be Supported on PlayStation®4 Development Hardware?

Support for PlayStation®4 development hardware is currently TBD. Timelines will be shared once they are confirmed.

## How Can Cross-Play Between PlayStation®4 and PlayStation®5 Be Tested Before PlayStation®4 Sandbox Support Is Available?

SIE recommends running PlayStation®4 titles on PlayStation®5 development hardware to test cross-gen features. Contact SIE on DevNet if you encounter any issues.

## Will OAuth Tokens, SSL Certs, Client IDs, or Secrets Change?

No. Existing credentials will remain unchanged. A new field will be added to ID token claims to identify the Sandbox ID, but use of this field is not required for migration.

The authorization code format itself will change slightly. Client applications must not assume or rely on a specific authorization code format; no changes should be required in this case.

## Can Save Data Be Imported Between Legacy and Sandbox PlayStation® Environments?

Yes. You can import save data created in Legacy PlayStation® environments into Sandbox PlayStation® environments. However, you can't load save data created on retail machines.

For more information, see [SaveData Library Overview - Handling of Save Data during Development - Handling of Save Data in the Sandbox Network Architecture](../SaveData-Overview/handling-of-save-data-during-sandbox-sdk.html).

## Does Sandbox Support the Development Accounts Feature?

Yes. You can use the Development Accounts feature to change online IDs, reset passwords, and more in Sandbox PlayStation® environments. However, changes are environment specific, meaning, changes made in Sandbox PlayStation® environments do not affect corresponding accounts for development in Legacy PlayStation® environments.

For more information, see [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html).

# Migration

This topic covers frequently asked questions about title and account migration to Sandbox.

See [Titles in Sandbox](sandbox-title-migration.html "This topic outlines the options available for getting titles into the Sandbox network architecture. It covers migrating existing titles and creating titles directly in Sandbox.") and [Migrating Accounts for Development in the Legacy Architecture](accounts-for-development-for-sandbox.html#general_api_topic__section_mnm_jrl_4hc) for general information regarding title and account migration.

## How and When Will We Be Notified About Our Title Getting Migrated?

Partners are not required to perform the migration themselves; the migration will be executed by SIE. The exact timing and communication channels are still being finalized. However, SIE will provide at least 4-6 weeks of advance notice before your title is migrated. Detailed guidance on what to do before, during, and after migration will be shared closer to the migration date.

## How Long Does It Take to Migrate a Title to Sandbox?

We will coordinate the title migration carefully to avoid disrupting your development work, with completion expected within one business day at most.

## Can We Continue Working on Our Product During Migration?

To preserve title configuration integrity, SIE recommends avoiding any service configuration changes relating to the title during the migration period. This includes changes to UDS, Trophies, Leaderboards, Content Pipeline, and similar services. Additionally, some tools will be temporarily unavailable during the migration. Further details will be shared at a later date.

## Does Migration Impact the Retail Environment?

No. Migration does not affect the retail environment. For example, if your title has already been released, migration will not impact retail users. The impact is limited to development and certification environments.

## Is Title Migration Mandatory?

Migration is mandatory for PlayStation®5 titles. For PlayStation®4 cross-gen titles that share services with a PlayStation®5 title, such as PlayStation®Store Delivered Content, Title Cloud Storage, UDS, Leaderboards, Session Manager, Presence 2, Profanity Filter, or Application Launch, migration is optional but will likely be included when SIE performs the migration. This ensures that shared services can be tested between PlayStation®4 and PlayStation®5 within Sandbox PlayStation® environments. PlayStation®4 titles that do not share any of the cross-gen services listed above are not included in the migration.

SIE understands that the assigned migration window may not always align with tight submission deadlines. If this occurs, contact SIE on DevNet to discuss alternative timing.

## My Title Is Still Under Development. Will It Also Be Included in Migration?

Yes. Titles that are still in development will be included in the migration, provided they have a concept and product registered in Content Pipeline and DevNet. Prior to migration, ensure that all Communication ID based services such as UDS, Trophy, Leaderboards and Session Manager are properly registered in DevNet.

## My Title Is Already Released. Will It Also Be Included in Migration?

Yes. Released titles will also be included in the migration. The migration will not impact end users, and no action is required from partners unless there are plans to release patch updates for the title after the migration.

## Is Migration Required for App Servers (Client Credential), Back Office Servers, and Authorized App Servers?

For App Servers (Client Credential) and Back Office Servers, migration is not strictly required, but it is recommended depending on how your servers obtain access tokens. Authorization codes obtained by a PlayStation®5 development hardware already include sandbox context when the development hardware is configured to run in Sandbox.

Migration is required for Authorized App Servers.

For non-migrated servers, when redeeming authorization codes to obtain an access token, the game server should call Auth/ PlayStation™Network Web API using the production (np) domain, rather than the development (sp-int) or certification (prod-qa) environments. For non-migrated servers, servers that use access tokens obtained through client credentials (using client ID and client secret) for use in Sandbox, such as "Back Office Server" and "App Server (Client Credential)" must do the following:

* Specify the production (np) domain
* Include the Sandbox ID in the `X-Psn-Sandbox-Id` header

Migrating an App Server (Client Credentials), Back Office Server, or Authorized App Server to Sandbox applies these requirements automatically, so no code changes are needed. However, once migrated, the server can no longer obtain access tokens for Legacy PlayStation® environments. This is an important consideration for servers that support multiple titles across both Legacy and Sandbox network architectures. In such cases, you may choose not to migrate and instead handle domain selection dynamically.

Do not migrate a Back Office Server product if you have requested the Package/Disc Management service for it. For more information, see [Package/Disc Management Web API Overview - Feature Overview - Changes in Behavior Due to Sandbox Migration](../Package_Disc_Management_WebAPI-Overview/sandbox-migration.html).

Let SIE know your preference once you are contacted regarding the migration of your titles. If you are unsure, contact SIE to discuss available options.

## Does Sandbox Support Registering New Title and Communication IDs?

Yes. See [PlayStation™Network Service Setup Guide - Registering Titles - Creating a New Product](../PSN_Service_Setup-Guide/creating-a-new-product.html) for information on creating new titles in Sandbox.

## Can Multiple Related Products Be Migrated Together?

Although migration is performed on a per-title basis, SIE strongly recommends migrating titles and App Servers that share services together as a cluster. This helps ensure PlayStation™Network services function correctly in Sandbox.

## Will IP Allowlists Be Migrated?

Yes. Access to Sandbox will continue to require IP allowlisting, similar to current requirements to access development environment (sp-int). IP allowlists are shared between Legacy and Sandbox PlayStation® environments, so only a single allowlist needs to be maintained.

## Will Development Environment (sp-int) Accounts Be Migrated?

Yes. Bulk migration of all development environment (sp-int) accounts is currently scheduled for March 2026. All accounts will be migrated to the DEV sandbox prior to the start of the initial title migration process to ensure accounts are ready for use, which is currently planned to be completed in March 2026. There are a few caveats to this process. Refer to the "Introduction to the Sandbox Architecture" level up video presentation for more details.

For clarity, migration does not mean the account is deleted from development environment (sp-int). The development environment (sp-int) account will continue to exist and remain usable in sp-int.

## What Account Data Is Migrated From Development Environment (sp-int) to the DEV Sandbox?

Core account details such as name, email, and password are migrated, along with social data including friend and block lists. Gameplay related data is not migrated. This includes sessions, UDS, user scores and data from leaderboards (including Title Cloud Storage data and variables), and trophies data, as well as any entitlements previously purchased in the development environment (sp-int).

Refer to [Accounts for Development in Sandbox](accounts-for-development-for-sandbox.html "This topic outlines the process for creating new accounts for development in Sandbox and explains the migration process of accounts for development in the Legacy architecture.") for more information on how account data is migrated to Sandbox.

# Account and Access

This chapter covers frequently asked questions about accounts for development in Sandbox and title privilege roles.

See [Accounts for Development in Sandbox](accounts-for-development-for-sandbox.html "This topic outlines the process for creating new accounts for development in Sandbox and explains the migration process of accounts for development in the Legacy architecture.") for general information about how accounts for development in Sandbox function.

## Can Legacy Development Environment (sp-int) Accounts Be Used in DEV Sandbox?

No. Legacy accounts are not compatible for use in the DEV sandbox. However, to ease the transition, all development environment (sp-int) accounts will be migrated to the DEV sandbox ahead of time.

To use an account for PlayStation™Network in the DEV Sandbox, partners may either use one of the migrated accounts or create a new account directly within the DEV sandbox.

You can continue to use original accounts in Legacy PlayStation® environments. After migration, these are now separate accounts and any changes you make in them are not reflected in the corresponding account in Sandbox.

For more information, see [Will Development Environment (sp-int) Accounts Be Migrated?](migration-frequently-asked-questions.html#migration_frequently_asked_questions__section_inj_nw2_m3c) and [What Account Data Is Migrated From Development Environment (sp-int) to the DEV Sandbox?](migration-frequently-asked-questions.html#migration_frequently_asked_questions__section_o2g_nw2_m3c).

## How Do I Create a DEV Sandbox Account?

The account creation process itself has not changed; however, DEV Sandbox accounts cannot currently be created using the website in development environment (sp-int), and full account creation on PlayStation®5 development hardware is not yet available. Use Quick Sign-Up option to create accounts until full support is rolled out in a later phase.

## Can Retail Accounts for PlayStation™Network Be Used in DEV Sandbox?

No. DEV sandbox accounts cannot be used in the retail environment, and retail accounts for PlayStation™Network cannot be used in the DEV sandbox.

## Are the Title Admin/Title Dev Roles Still Required to Access Title Information in DEV Sandbox?

The DEV sandbox is a shared environment across all titles, similar to development environment (sp-int). Title privilege roles like Title Admin/Title Dev are therefore required to prevent unauthorized access. The mechanism for managing title privilege roles (adding accounts to a title) remains unchanged and can be performed on DevNet and with the Development Account Tool.

In addition, existing title privilege role configurations will be migrated from development environment (sp-int) to the DEV sandbox, so no reconfiguration is required.