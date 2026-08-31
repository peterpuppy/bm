# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/game-and-server-code.html

# Developing and Publishing with Sandbox

This chapter highlights the updates to development and publishing workflows brought on by the introduction of Sandbox. It focuses on IP allowlist management, account setup, service configuration, and submission processes.

Development and certification submission workflows in Sandbox are similar to the workflows in Legacy, with differences in a few key areas. Ensure to understand and incorporate these differences into your workflows after migrating to Sandbox.

## Development Workflow Changes

Keep the following development areas and their Sandbox specific processes in mind as you develop titles in Sandbox:

* **PlayStation™Network IP Allowlist** - To protect PlayStation™Network platforms from the public internet, Sandbox is protected with the IP Allowlist. Company and organization admins in DevNet register IP addresses through the organization admin page. Legacy and Sandbox share the allowlist, meaning there is no need to manage the list separately. For more information, see [IP Allowlisting For PlayStation™Network Services](https://learn.playstation.net/bundle/playstation-partners-getting-started/page/PSP_DevNetAnywhere.html).
* **Development Accounts** - You can't use test accounts from Legacy with Sandbox. [Use a migrated Legacy development account or create a new one](accounts-for-development-for-sandbox.html "This topic outlines the process for creating new accounts for development in Sandbox and explains the migration process of accounts for development in the Legacy architecture.").
* **Connecting DevKit/TestKit to Sandbox** - To develop and test a title that has been migrated to Sandbox, [connect your development hardware to the DEV environment in the Sandbox.](sandbox-management-on-devkit-testkit.html "This topic provides an overview of managing PlayStation® environments on DevKits and TestKits. It details the differences between sandboxed and global data management, configuration of network architectures, and considerations when downgrading system software.")
* **Configuring PlayStation™Network Services** - In Legacy, depending on the service, you conducted service configuration in the service's related GUI tool (for example, the Universal Data System (UDS) Management Tool), the service's related management web API for Back Office Server, or the User Bucket for Partners (UBP). In Sandbox, [you can update service configuration using either a CLI-based tool or a web-based tool](service-configuration.html "This topic explains the two methods of configuring PlayStation™Network Services in Sandbox: using the CLI-based tool np-service-config and using a web-based tool such as the Title Cloud Storage Tool.").
* **Integrating Game and Server Code with PlayStation™Network** - PlayStation® system software handles routing requests based on your device settings, so there is no need to change your client-side code. SIE provides [support to automatically proxy server requests from Legacy to Sandbox](game-and-server-code.html#general_api_topic__section_hlq_ldl_4hc).

## Submission Workflow Changes

Keep the following certification submission concepts in mind as you submit titles for certification in Sandbox:

* **Downloading the npconfig.zip to create the package** - In Legacy, you were required to generate the NP Config Tag which defined a certain snapshot revision of your trophy and UDS configuration. Sandbox is always managing revisions of every service configuration, so you don't need to explicitly create an NP Config Tag. Download the *npconfig.zip* by specifying a Config ID that is issued when you configured the service. Download *npconfig.zip* through the following methods:
  + [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html)
  + [Package/Disc Management Web API Overview](../Package_Disc_Management_WebAPI-Overview/__document_toc.html)
  + PubTool (GUI/CLI)
* **Enabling Game Services in CERT and RETAIL** - Prior to submitting your game to certification, you must enable the service in CERT and RETAIL and publish the game service configuration to CERT and RETAIL environments. For details on how to enable services in CERT and RETAIL, see [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).
* **Submitting for Certification** - The process in Certification Center is the same as with Legacy PlayStation® environments. The MDT form displays the last date and time the service configuration was published for the services listed in the PlayStation™Network Features section so that you can verify that the service configuration has been updated and published in the way expected. For details, see [Certification Center](https://learn.playstation.net/bundle/level-up/page/CertOps.html).
* **Patch publishing and PlayStation®Store Submission** - Publishing certified content is the same as with Legacy. If you are publishing a patch to your app or add-on content, manage the release timing in the Package/Disc Management Tool (GEMS) or Package/Disc Management Web API. For details, see [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) or [Package/Disc Management Web API Overview](../Package_Disc_Management_WebAPI-Overview/__document_toc.html). After a title is migrated to Sandbox, you must download a new *npconfig.zip*. This is required even if there have not been any modifications to Trophy or UDS since the title was released in Legacy. If you are releasing your content as a PlayStation®Store product, use the PlayStation®Store's Content Pipeline submission workflow. For details, see [Getting Started with Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/Getting_Started.html).

## PlayStation®4 Title Development

Titles that are only on PlayStation®4 and any titles that use Legacy PlayStation™Network services for PlayStation®4 such as Matching2 and Ranking, are not supported in Sandbox. Continue to use Legacy to develop these titles.

Cross-gen titles that do not use Legacy PlayStation®4 services are supported, but PlayStation®4 DevKits can't connect to DEV. You can use sp-int for PlayStation®4 testing. Platform Certification & Operations (CertOps) uses prod-qa to test your PlayStation®4 build.

# Updating Game and Server Code

This topic provides guidance on adapting game and server code to accommodate the Sandbox network architecture changes. It highlights changes to network API requests and access token modifications.

## PlayStation™Network API Requests in Sandbox

The DEV, CERT, and RETAIL environments are implemented in the same physical network, meaning separate domain names are not required to distinguish between them. Rather than switching domains, API requests in Sandbox use the production domain for all requests and distinguish between environments using sandbox context. This context, added as a claim in the access token, determines which sandbox to use for each request.

These updates may require you to either update your game and server code or migrate your servers to Sandbox, depending on your server type:

| Client | Code Change Required | Migration Required |
| --- | --- | --- |
| App Server | No | No |
| Authorized App Server | No | Yes |
| Back Office Server | Yes | No. While migration is not required, [it is recommended](migration-frequently-asked-questions.html#migration_frequently_asked_questions__section_a25_nw2_m3c). |
| App Server (Client Credential) | Yes | No. While migration is not required, [it is recommended](migration-frequently-asked-questions.html#migration_frequently_asked_questions__section_a25_nw2_m3c). |
| App (PS5 & PS4 Cross-gen) | No | Yes |

Note: After provisioning a new Back Office Server or App Server (Client Credential) directly in Sandbox, it may take up to one hour before you are able to use sp-int endpoints to make API calls for the DEV sandbox.

## App Servers

Requests from App Servers are automatically routed to the production domain so do not require you to make a code change or migrate the server to Sandbox.

Authorization codes sent from a PlayStation®5 console to your game server include access information from the console that generated the code, including the sandbox context.

Requests to PlayStation™Network from an App Server

## Authorized App Servers

Requests from Authorized App Servers do not require a code change, but servers must be migrated to Sandbox before they are able to handle Sandbox requests.

## Back Office Servers and App Servers (Client Credential)

Requests from Back Office Servers and App Servers (Client Credential) require you to either update your code or migrate the servers to Sandbox.

To update your code:

1. Update Sandbox requests to use the same base URL as production requests:

   ```
   https://s2s.np.playstation.net/api/
   ```
2. Include sandbox context when requesting a client credential based access token. To generate an access token with sandbox context, pass the header `X-Psn-Sandbox-Id`, to the Auth Web API.

If you instead migrate your servers to Sandbox, the above changes are automatically applied to incoming requests from your server; however, migration prevents you from obtaining access tokens in Legacy.

Do not migrate a Back Office Server product if you have requested the Package/Disc Management service for it. For more information, see [Package/Disc Management Web API Overview - Feature Overview - Changes in Behavior Due to Sandbox Migration](../Package_Disc_Management_WebAPI-Overview/sandbox-migration.html).

Requests to PlayStation™Network from an App Server (Client Credential) or Back Office Server

## App (PS5 & PS4 Cross-gen)

Requests to PlayStation™Network directly from a game application do not require you to make a code change.

PlayStation® environment switching is handled by the PlayStation® system software. You control which environment your DevKit or TestKit uses by changing the sandbox in *★Debug Settings*  in the system software. This means you don't need to change client-side code in applications on PlayStation®5. Network requests always use the correct URL and have the expected context embedded in the access token.

Requests to PlayStation™Network Directly from an App

## Handling Access and Refresh Tokens

Access and refresh tokens in Sandbox are 36 characters long but can't be parsed into a UUID. As long as your server code does not make any assumptions about the token other than its length, there is no change required to support this.

Both game server and client code can use the `env_iss_id` field of an ID token to determine the console's environment. See [Auth Web API Overview - Appendix - ID Token Claims](../../../WebAPI/latest/Auth_WebAPI-Overview/id-token-claims.html) for more information.

Although DEV and CERT are hosted in RETAIL, ID tokens use the same `env_iss_id` value as sp-int and prod-qa respectively to support backwards compatibility.

ID tokens for Sandbox also include a new claim, `sbid`, which is a six-character string that uniquely identifies the sandbox.

# Publishing Products to PlayStation® Environments

This topic provides a detailed overview of the steps involved in deploying game products to PlayStation® environments. It covers processes such as enabling titles, integrating in-game catalogs, creating and uploading entitlements, and testing in cloud streaming, alongside submission and certification workflows.

Follow the steps below to publish products to PlayStation® environments:

1. Have SIE migrate your title to Sandbox. For information on the title migration process, see [Titles in Sandbox](sandbox-title-migration.html "This topic outlines the options available for getting titles into the Sandbox network architecture. It covers migrating existing titles and creating titles directly in Sandbox.").
2. [Set up your product and the in-game catalog for add-on content integrations](publishing-products-to-sandbox.html#general_api_topic__section_v4m_dll_4hc).
3. Create and upload entitlements for add-on content integrations. Fake wallets and funds are not supported for commerce transactions. Instead, you can make purchases in PlayStation® environments without requiring funds. For details on creating entitlements, see [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html). For information on uploading add-on content, see [Package/Disc Management Tool (GEMS) Overview - Additional Content Management](../Package_Disc_Management_Tool_GEMS-Overview/additional-content-management.html).
4. [Upload the game package](publishing-products-to-sandbox.html#general_api_topic__section_kpm_dll_4hc).
5. [Test and debug the title in cloud streaming](publishing-products-to-sandbox.html#general_api_topic__section_ppm_dll_4hc).
6. Submit the product for certification. For more information, see [Submission Workflow Changes](developing-and-publishing-workflow.html#general_api_topic__section_q5x_vcl_4hc).
7. [Publish the in-game catalog to CERT](publishing-products-to-sandbox.html#general_api_topic__section_wpm_dll_4hc).
8. [Submit Pricing and Availability (PAR) and finalize going-live details](publishing-products-to-sandbox.html#general_api_topic__section_bqm_dll_4hc).
9. Use the GEMS tool to release the title to the RETAIL environment. For more information, see [Package/Disc Management Tool (GEMS) Overview - Application Management](../Package_Disc_Management_Tool_GEMS-Overview/application-management.html).

## Setting Up Add-On Content

To set up add-on content integrations, do the following:

1. Create the in-game catalog. The process is the same as creating an in-game catalog in Content Pipeline. For instructions, see [Package/Disc Management Tool (GEMS) Overview - Application Management](../Package_Disc_Management_Tool_GEMS-Overview/application-management.html) and [Creating and Editing an In-Game or In-App Catalog](https://learn.playstation.net/bundle/content-pipeline/page/InGameCatalog_CreateCatalog.html).
2. From Content Pipeline, navigate to **Store Structures**.
3. Select **Publish to Environment** from the drop-down menu.
4. Select **DEV**.

In-Game Catalog Store Structures Tab

**Related Documentation**

Explore the related documentation listed below for more information on creating, editing, and managing in-game commerce content:

* [In-Game Catalog Overview](../../../WebAPI/latest/In_Game_Catalog-Overview/__document_toc.html)
* [PlayStation™Network Commerce Platform Overview - New Commerce Features in PlayStation®5 - Content Pipeline](../PSN_Commerce_Platform-Overview/content-pipeline.html)
* [AppContent Library Overview](../AppContent-Overview/__document_toc.html)

## Uploading Game Packages

A game package contains:

* The game executable code, also referred to as the game binary
* Game media assets
* The *npconfig.zip* file, which contains everything from the title configuration that is required locally

Uploading game packages to PlayStation® environments is the same as with Legacy PlayStation® environments. Uploading generates a *package tag* that uniquely identifies the package.

For more information on game packages, see [Content Packaging and Updating Guide - Packages Overview](../Content_Packaging_and_Updating-Guide/packages-overview.html). For information on creating game packages, see [Publishing Tools GUI User's Guide - Operating Publishing Tools GUI - Publishing Tools GUI Create View](../Publishing_Tools_GUI-Users_Guide/publishing-tools-gui-create-view.html).

For information on uploading game packages, see [PlayStation™Network Service Setup Guide - Making Service Requests - Connecting to User Bucket for Partners (UBP) from a Back Office Server](../PSN_Service_Setup-Guide/connecting-to-user-bucket-for-partners-ubp.html) and [Package/Disc Management Tool (GEMS) Overview - Uploading Packages and Downloading Packages/ISO Images](../Package_Disc_Management_Tool_GEMS-Overview/uploading-packages-and-downloading-packages-iso-images.html).

## Testing and Debugging in Cloud Streaming

To test a game in cloud streaming, do the following:

1. Upload your binary, select the tag for Sandbox, and specify your service manifest.
2. Set your DevKit to the sandbox you want to use for testing, then launch the Cloud Streaming Preview application.
3. run your game in the Cloud, and debug.

For more information on testing games in cloud streaming, see [PlayStation™Network Cloud Streaming Overview](../PSN_Cloud_Streaming-Overview/__document_toc.html).

## Publishing an In-Game Catalog to CERT

Once the in-game catalog is ready for certification testing by SIE, publish the catalog to CERT:

1. In Content Pipeline, navigate to **Concepts**.
2. Select the in-game catalog content you want to publish.
3. Select **Publish to CERT/Prod-QA**.

Publishing to CERT

## Submitting PAR and Going Live

Finalizing products developed in Sandbox is a similar process to finalizing products developed in Legacy PlayStation® environments.

When you are ready, publish the in-game catalog to RETAIL:

1. From the **Concepts** tab, select the in-game catalog content you want to publish.
2. Select **Publish to RETAIL**.

Publishing to RETAIL

For more information on publishing in-game catalog content, see [Publishing an In-Game or In-App Catalog to the Live (Production) Environment](https://learn.playstation.net/bundle/content-pipeline/page/InGameCatalog_LivePublish.html).