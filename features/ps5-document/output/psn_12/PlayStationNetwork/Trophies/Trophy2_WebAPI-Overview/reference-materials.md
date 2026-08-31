# Trophy2 Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Trophy2_WebAPI-Overview/reference-materials.html

# Feature Overview

This document provides, as basic information that you should understand when using the Trophy2 Web API, the Web API's purpose and characteristics, main features, and reference materials.

# Purpose and Characteristics

The Trophy2 Web API is a Web API that can be used to enable a game application server (App Server or App Server (Client Credential)) to obtain information from the trophy system. The Trophy2 Web API can be used to obtain trophy configuration data and trophy records and to display lists of user-specific trophy unlocking statuses and other statistics on the game application server.

# Main Features

The main features of the Trophy2 Web API are as follows:

* Obtaining trophy configuration data
  + Title information
  + Trophy group information
  + Trophy information (trophy name, trophy type, icon information, etc.)
* Obtaining trophy records
  + Trophy unlock states
  + Trophy progress information
  + Statistical information on trophy obtainment on a per-title basis

With the Trophy2 Web API, it is only possible to read trophy information provided by the Trophy2 service.

Calling the Trophy2 Web API using an App Server client ID enables the reading of the trophy configuration data, current user trophy records, trophy records for other users (within the scope permitted by privacy settings), and statistical information about trophy unlocking rates.

Calling the Trophy2 Web API using an App Server (Client Credential) client ID enables the reading of the trophy configuration data, trophy records for any user, and statistical information about trophy unlocking rates.

## Protecting Trophy Assets Using Signed URLs in DEV and CERT Environments

In the Sandbox network architecture, pre-signed URLs that are valid for a limited period of time are used to access assets in the development environment (DEV) and certification environment (CERT) to prevent trophy-related assets in titles under development from being leaked.

Pre-signed URLs have an expiration date, and access is controlled by the signature information contained in the URL. Additional authentication is not required, but a new pre-signed URL will be required after the expiration date.

When using the production environment (RETAIL) of Sandbox (for commercial use), assets can be accessed without signatures. Note that pre-signed URLs are also not required in the PlayStation® environments (sp-int, prod-qa, and RETAIL) of the Legacy network architecture.

Refer to [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html) for details about Sandbox.

# Reference Materials

Refer to the following document to gain an overall sense of how the trophy system works.

* [Trophy System Overview](../../../SDK/latest/Trophy_System-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Trophy2 Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Trophy2_WebAPI-ReleaseNotes.html)