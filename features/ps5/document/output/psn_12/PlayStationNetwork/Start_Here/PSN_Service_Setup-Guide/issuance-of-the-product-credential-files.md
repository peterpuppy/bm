# PlayStation™Network Service Setup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Service_Setup-Guide/issuance-of-the-product-credential-files.html

# Making Service Requests

This chapter explains the operational procedure and notes for making a PlayStation™Network service request on DevNet.

# Available Services

This topic provides information on the available PlayStation™Network services.

The table below shows the available PlayStation™Network services for PlayStation®5 , divided by product type.

For more information about PlayStation™Network services for PlayStation®4 that are available to the **App (PS4 Cross-gen)** product types, see the [PlayStation™Network Service Setup Guide](https://ps4.siedev.net/resources/documents/SDK/7.000/PSN_Service_Setup-Guide/__document_toc.html) on PlayStation®4 DevNet.

Available Services

| Services | Types of Issued ID | App (PS5) | App (PS4 Cross-Gen) | App Server | App Server (Client Credential) | Back Office Server | Authorized App Server | Tools | Shareable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Advanced Player Profile | NP Communication ID | Yes | N/A | Yes | N/A | N/A | Yes | Advanced Player Profile Editor | Yes |
| Advanced Player Profile Management | NP Communication ID | N/A | N/A | N/A | N/A | Yes[\*4](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note4) | N/A | Advanced Player Profile Editor | Yes |
| Application Launch | NP Communication ID | Yes | Yes | N/A | N/A | N/A | N/A | N/A | Yes |
| Client ID | Client ID | Yes | Yes | Yes | Yes | Yes | N/A | N/A | No |
| Commerce Catalog and Entitlement | NP Service ID[\*7](available-services.html#psn-service-setup-guide_3_1__note8) | Yes | Yes | N/A | N/A | N/A | N/A | Content Pipeline | Yes |
| Crash Report | NP Title ID | N/A | N/A | N/A | N/A | Yes | N/A | N/A | Yes |
| Leaderboards | NP Communication ID | Yes | Yes | Yes[\*1](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note1) | N/A | N/A | Yes | Leaderboards Tool | Yes |
| Leaderboard Management | NP Communication ID | N/A | N/A | N/A | N/A | Yes[\*2](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note2) | N/A | N/A | Yes |
| Package/Disc Management | NP Title ID | N/A | N/A | N/A | N/A | Yes | N/A | N/A | Yes |
| PlayStation™Store Delivered Contents | NP Service ID | Yes | Yes | Yes[\*1](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note1) | N/A | N/A | Yes | GEMS, DEV ADMIN, Content Pipeline | Yes |
| PlayStation™Store Delivered Content Management | NP Service ID | N/A | N/A | N/A | N/A | Yes[\*1](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note1) | N/A | N/A | Yes |
| Presence 2 | NP Communication ID | Yes | Yes | Yes[\*1](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note1) | N/A | N/A | Yes | N/A | Yes |
| Profanity Filter | NP Communication ID | Yes | Yes | N/A | Yes | N/A | N/A | N/A | Yes |
| Session Manager | NP Communication ID | Yes | Yes | Yes | Yes | N/A | N/A | Matchmaking Tool | Yes |
| Title Cloud Storage | NP Communication ID | Yes | Yes | Yes[\*1](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note1) | N/A | N/A | Yes[\*1](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note1) | Title Cloud Storage Tool | Yes |
| Title Cloud Storage Management | NP Communication ID | N/A | N/A | N/A | N/A | Yes[\*3](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note3) | N/A | N/A | Yes |
| Tournaments | NP Communication ID | Yes | N/A | N/A | N/A | N/A | N/A | UDS Management Tool | Yes |
| Trophy 2 | NP Communication ID[\*6](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note7) | Yes | N/A | Yes | Yes | N/A | Yes | UDS Management Tool, Package/ Disc Management Tool (GEMS) | Yes |
| Universal Data System | NP Communication ID | Yes | Yes | Yes | Yes | N/A | Yes | UDS Management Tool, Package/ Disc Management Tool (GEMS) | Yes |
| Universal Data System Management | NP Communication ID | N/A | N/A | N/A | N/A | Yes[\*5](available-services.html#psn-service-setup-guide_3_1__uuid-f043c83a-db83-f366-7b57-6e63324d6078_note6) | N/A | N/A | Yes |

1. Services used with **App (PS5)** products can be shared.
2. Requires a Leaderboards service to be configured first.
3. Requires Title Cloud Storage to be configured first.
4. Requires an Advanced Player Profile service to be configured first.
5. Requires a Universal Data
   System service to be configured first.
6. There is a system specification to not allow the use of the same NP Communication ID with PlayStation®4 Trophies and also to not share a service between PlayStation®4 Trophy and Trophy2.
7. Can only be shared from PlayStation™Store Delivered Contents on App (PlayStation®5) or App (PlayStation®4 Cross-Gen).

# Service Instance Policy for PlayStation®5 Generation PlayStation™Network Services

This topic provides information on policies you must follow for NP Communication ID-based PlayStation®5 PlayStation™Network services.

NP Communication ID-based PlayStation®5 PlayStation™Network services impose new restrictions that previous PlayStation™Network Services did not require.

## Console-type Products

The **App (PS5)** and **App (PS4 Cross-gen)** product types run on a game console. The use of NP Communication ID-based PlayStation®5 PlayStation™Network services by these product types are subject to the following rules:

* Only one instance of each PlayStation™Network Service can be used on each product. (Only Service Label 0 is available.)
* All PlayStation®5 PlayStation™Network Services must use the same NP Communication ID within a product.
* Each PlayStation®5 PlayStation™Network service can support separate instances of a service within a single NP Communication ID. It is not necessary to use multiple Service Labels and NP Communication IDs.

* The **App (PS4 Cross-gen)** can still have the different NP Communication ID used for PlayStation®4 generation PlayStation™Network Services.

For some examples, refer to the following figures.

Single NP Service Label
Different NP Communication ID

## Non-Console Type Products

**App Server**, **App Server (client credential)**, and **Back Office Server** product types run on application servers or back-office servers, rather than on a game console.

These product types should not create new service instances. Instead, they should reference existing service instances that were provisioned on a console application type, for example, App (PS5) or App (PS4 Cross-gen). Additionally, service instances should be shareable with multiple services that are configured to the product under the same title.

# Service Request Overview

This topic provides an overview of the procedure for requesting PlayStation™Network services.

In the current SDK release, "PlayStation™Network service request" refers to one of the following:

* A request to add a new PlayStation™Network service.
* A request for sharing services.
* A request to change an existing service.
* A request to enable service in production.
* A removal request.

To use a specific service in your product, submit a request for a new instance of that service. SIE then configures the server and the online tools for the requested service. Depending on the product type, there are services that are automatically be requested by default.

* App (PS5): Client ID, PlayStation™Store Delivered Contents
* App (PS4 Cross-gen): Submission, Patching, PlayStation™Store Delivered Contents and Live Item
* App Server: Client ID
* App Server (Client Credential): Client ID
* Back Office Server: Client ID

Note: An automatic request for a service may not succeed if a new product including a service request procedure is canceled before it is added completely. In this case, a service request form is shown when clicking a product detail page to complete the service request because those services are necessary for proceeding on other service requests. Also, services automatically requested are not able to be removed as those are necessary for using PlayStation™Network services.

Once a service is configured to a product, the service can be shared to another product.

In PlayStation®5, service sharing is allowed among products under the same title.

To amend or delete an existing service, make a request to change the setting or a removal request. SIE reviews the request, and the configuration of the server and online tools are modified accordingly.

# Requesting to Add a New Service for a New Product

This topic describes how to make a request to add a new service to an existing product.

A request to add a service must be made for each product.

1. In DevNet, go to **Titles** > **Titles and products**. Select the product from the titles and products list that you want to add service for.
2. Select the service you want to use and click **New service**, then enter or select required information.

   Request New Services

   If specifying an NP service label is required, select one from the drop-down list.

   Request Services

   For details on other required information, see [Appendix A: Required Parameters](appendix-a-required-parameters.html "This topic provides information on the parameters required to enable certain PlayStation™Network services.").
3. After you complete the above steps, a DevNet service thread is created. To confirm that the status of the target service is requested:

   * From the **Support** menu on DevNet, select **Private support** to view a DevNet service thread list.
   * On the product page, click on the requested service and select **View history**.

     Note:

     A DevNet service thread is created per ID related to the requested service (NP Title ID, Service ID or NP Communication ID). For example, if PlayStation™Store delivered content is requested, the requested content is displayed in the DevNet service thread created for the Service ID.

Once SIE accepts the request and completes the registration processing, configuration completion is notified in the DevNet service thread. The status of the target service on the product page changes from **Requested** to **Development** or **Production**.

# Creating a Request to Share Service

This topic describes how to make a request to share PlayStation™Network services.

To share PlayStation™Network services, do the following:

1. Complete a request to use the target service with the first product and wait for the setting to complete. If the setting is not complete, the candidates for sharing does not display in the next step.
2. Click the target service for the second product. In addition to **New service**, out of all the products using the same service on the same platform, the products for which you have *Editor* or *Owner* privileges are displayed as candidates for sharing the target service.

   If the desired product is not displayed as a candidate, for example, when you want to share a service across titles and platforms, perform a search by entering the NP Title ID, Service ID, product name, etc., in the search field.

   Product to Share

   After the product to share is selected, select the NP service label to share from the drop-down list, then click **Add service**.

   Add Service

   Note:

   If the desired product is still not displayed as a candidate after performing a search, confirm that you have *Editor/Owner* privileges. If the service ID for the desired product is not displayed, use the following procedure to contact Private Support:

   1. Log in to DevNet.
   2. Click **Ask a question** at the top of the product page.
   3. Select the service to share and post a question.

   Note:

   For sharing requests for a service which have an NP Communication ID (e.g. Trophy2, Universal Data System), be aware that the service instance policy explained in "Service Instance Policy for PlayStation®5 Generation PlayStation™Network Services" uses the same NP Communication ID within a product when you request service sharing.

   If the candidate isn't displayed, make sure that the NP Communication ID based service is configured with a different NP Communication ID for the product. In this case, request a service removal request for all of the NP Communication ID based services associated with a different NP Communication ID. Once service removal is completed, a candidate service to be shared appears.

# Requesting a Change in Requested Service

This topic describes how to make a request to change the configuration of a PlayStation™Network service.

To change the configuration of a requested service for Client ID for non-console products, perform the following procedure:

1. Open the product page, select the service to change, and click **Reconfigure service**.
2. Enter the parameter to change.
3. Confirm that the status of the target service is **Pending configuration**. When SIE completes the configuration, the status changes to **Development**. You are also notified of configuration completion in the DevNet service thread.

   Reconfigure Service

# Changing an NP Service Label

This topic describes how to make a request to change the NP service label of a PlayStation™Network service.

To change an NP Service Label of shared services for App Server, App Server (client credential) and Back Office Server, perform the following procedure:

1. Open the product page and request an NP Service Label change.
2. Select the NP service label to change on the product page, click **Edit NP Service Label**, and specify a new NP service label.

   NP service labels already being used and NP service labels that already have change requests cannot be specified. If specifying one is required, first change the NP service label so that it is no longer used (delete the service for the label or make changes so that another NP service label is used).
3. Confirm that the status of the target service is **NP Service Label (the NP service label for which the change was requested)**. When SIE completes the configuration, the NP service label changes. You are also notified of configuration completion in the DevNet service thread.

# Requesting a Service Enabling to Production

This topic describes how to make a request to enable a PlayStation™Network service in production environments.

Once a configured service for a product is confirmed to be working properly in the
development environment, it must be enabled in production. Use the following procedure to
do this. This request must be done before submitting your application for
Certification.

1. Open the product page and make a service enabling to production request.
2. Select the target service on the product page and click **Enable service in Production**.
3. Confirm that the status of the target service is **Enabling in Production in progress**. When request is completed the state changes to **Production**. You are also notified of request completion in the DevNet service thread.

   Note:

   If this request is mistakenly made and it doesn't need to be, you can still use the service in the development environment.

# Requesting a Service Removal

This topic describes how to make a request to remove a PlayStation™Network service.

To request a service removal, do the following:

1. Open the product page, select the target service, and click **Remove from this product**.
2. Confirm that the status of the target service is **Removal requested**. When SIE completes the configuration, the state changes to one where no service requests have been made. You are also notified of configuration completion in the DevNet service thread.

   Note:

   To switch an NP Communication ID service associated with a different NP Communication ID, request removal for all services associated with the same NP Communication ID in a product. You must do this to ensure compliance with the service instance policy.

   Note:

   If a removal request is made by mistake, create a support request from <https://p.siedev.net/support/newissue>.

   Generally, requests cannot be canceled, but it is possible for services to not be removed if you create the support request immediately after the removal request..

# Issuance of the Product Credential Files

This topic provides information on the types of credentials that are issued after a service request is made.

When the required information is registered and a service request is made, product credential files are issued. The following types of product credential files exist, and the issued files vary depending on the platform and product type.

* NP Title Secret / nptitle.dat
* Client Secret/Client ID
* SSH Key for User Bucket for Partners (UBP) access

The following table shows the product credential files issued for PlayStation®5, categorized by product type.

Product Credential Files for PlayStation®5

| Product Type | nptitle.dat | NP Title Secret | Client ID | Client Secret | SSH key for UBP |
| --- | --- | --- | --- | --- | --- |
| App (PS5) | Yes | Yes | - | - | - |
| App (PS4 Cross-gen) | Yes | Yes | - | - | - |
| App Server | - | - | Yes | Yes | - |
| App Server (Client Credential) | - | - | Yes | Yes | - |
| Back Office Server | - | - | Yes | Yes | Yes |

nptitle.dat and an NP Title Secret is issued when the settings are complete for any service that can be used with PlayStation®5. The Client ID and Client Secret are issued when the Client ID settings are complete.

## Access Log to Product Credential Files

Access privileges for the NP Title Secret, nptitle.dat, Client Secret, Client ID and SSH key for UBP are set per DevNet product.

When a product is created, the user who created it (Owner) is given access privileges for the product credential files. The user with Owner privileges can then grant access privileges to owners, editors, and viewers of the product.

Every access to the NP Title Secret, nptitle.dat, Client Secret, Client ID and SSH key for UBP is recorded.

Any user who can access the product page can view the access history in the following manner:

1. Open the product page and click **Show product history**.
2. Click **Show events** of the product history thread, shown below.

   Show Events
3. Access privilege settings for the product credential files, users who downloaded files, and the date/time of each download are displayed, shown in the following image.

   Privilege Settings

## Obtaining Product Credential Files

When a user with access privileges to product credential files opens the product page, download links are displayed in accordance with the product as follows.

Click the link to download the file.

* For App (PS5) and App (PS4 Cross-Gen) product: **Download NP Title Secret**.
* For an App Server, App Server (client credential) and Back Office Server product: **Download Client Secret**.

The file that can be downloaded by clicking **Download NP Title Secret** contains both the NP Title Secret and nptitle.dat. The file that can be downloaded by clicking **Download Client Secret** contains the Client Secret.

Note:

Downloaded files are not encrypted (although these files used to be encrypted using the PGP public key, they can now be downloaded as plain text given that the access privilege management feature is provided).

Product credential files contain confidential information; take care in managing access privileges and in handling files once they are obtained in order to prevent information leakage to external parties. Take enough cautionary measures, such as removing confidential information, when disclosing your source code or application package to seek PlayStation®5 DevNet support.

# Managing Access Privileges

This topic provides information on how to manage access privileges in DevNet.

## Setting Access Privileges for Tools

Access privileges for all tools which navigate from DevNet product detail page are linked to the DevNet product access privileges. For the setting procedure, refer to Setting Access Privileges.

## Setting Access Privileges for Product Credential Files (NP Title Secret, nptitle.dat, Client Secret and SSH Key for UBP)

When a product is created, the user who created it (Owner) is given access privileges for the product credential files. If you want to grant access privileges to owners, editors, or viewers of the product, operate as follows.

1. Log in to DevNet with an account with Owner privileges.
2. Click **View Collaborators** at the top of the product page.
3. Current access privileges for the product credential files are displayed for each owner, editor, and viewer who can access the product. Click the access privilege to change privileges.

## Setting Title Admin and Title Dev Privilege in the Development Environment [sp-int]

To access some functions and assets in the development environment (sp-int) from your Development Kit and Testing Kit, use an account on PlayStation™Network with either the Title Admin or Title Dev privilege on the title.

Those are functions and assets such as preview of in-game catalogs, preview of image files on PlayStation™Network objects, download of patch pkgs, and usage of the PlayStation™Network Game Hub Preview Application.

For more details on how to assign these privileges, see [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html).

# Connecting to User Bucket for Partners (UBP) from a Back Office Server

This topic describes how to connect a PlayStation™Network service to User Buckets for Partners from a Back Office server.

User Bucket for Partners (UBP) is an Amazon S3 bucket that can be used for package upload
and bulk import of UDS configuration. Additional to PlayStation® Partner Okta accounts, SSH
keys can be issued for each Back Office Servers.

The information and SSH keys required to access UBP are provided in the Product Details
Page to users having Product Credential Files privilege. Refer to the following information
to configure your SFTP connection:

* Connection method (Port): SFTP (22)
* Server: Endpoint displayed on the Product Details Page
* Username: NP Title ID of the Back Office Server (also displayed in Product Details
  Page)
* Password: None
* SSH Key: Download from Product Details Page

As for permission checks when package files and UDS configuration files are uploaded, the
service association with the following services on the Back Office Server are used:

* Package - Package/Disc Management Service (NP Title ID)
* UDS configuration - UDS Management Service (NP Communication ID)

For details on how to upload these assets, refer to the following documents:

* [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html)
* [Universal Data System Guide - Using the UDS Management
  Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html)

# Managing Consent Metadata for Authorized App Server Product Types

This topic provides information on how to enable, publish, and manage consent metadata for Authorized App server product types.

If you need to use your App Server to access a user's account information in PlayStation™Network, you must get consent from that user using a *Consent Screen*, as shown below. DevNet provides you with a tool to configure the information that is shared on the *Consent Screen* that will help the user grant an informed consent to the Authorized App.

Consent Screen Preview

## Accessing the Consent Metadata Manager

To access the Consent Metadata Manager, do the following:

1. Create your Authorized App Server product on DevNet and wait for the *Client ID* to be provisioned.
2. Once provisioned, click **Consent screen configuration** on the product page or beneath the *Client ID* service drop-down list.

Accessing the Consent Metadata Manager

## Managing and Publishing the Consent Screen

Once you've opened the tool, it provides you with detailed, step-by-step instructions for configuring the languages that your consent screen requires.

The essential information that you must provide for each language is as follows:

* App name (50 characters max)
* Logo image (sRGB, PNG Format, 512 x 512px, opaque background with no rounded corners)
* Homepage URL (2048 characters max, HTTPS recommended)
* Privacy Policy URL (2048 characters max, HTTPS recommended)
* Terms of Service URL (2048 characters max, HTTPS recommended)

After you provide the above information for each language, **Save** all the configurations to the development (sp-int) environment.

After you've tested your language configurations to confirm that they're working as expected in sp-int, you can publish them to the Certification (prod-qa) and production (np) environments.

# Notes Related to Requests

This topic provides additional information you may find useful when making requests to enable services.

Requests usually require five business days to process. Additional time may be required if, for example, SIE is on extended holiday; make sure to check for such announcements on the front page of DevNet.

Generally, requests cannot be canceled. However, in serious cases such as when a service has been mistakenly removed, contact Private Support immediately by creating a request from <https://p.siedev.net/support/newissue>.