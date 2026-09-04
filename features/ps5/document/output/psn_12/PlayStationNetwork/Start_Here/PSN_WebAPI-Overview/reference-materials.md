# PlayStation™Network Web APIs Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_WebAPI-Overview/reference-materials.html

# Overview

This topic describes the PlayStation™Network Web API's characteristics and
purposes.

The PlayStation™Network Web APIs are REST APIs for PlayStation®5 applications as well as PlayStation®4 applications - and the application servers and websites that work with these applications - to use the PlayStation™Network services.

Note: This document focuses on the usage of Web APIs on PlayStation®5, the application servers, and websites only.
For the PlayStation®4 or other platforms, refer to the documents prepared for those platforms.
Depending on the platform, the scope and usage of the provided PlayStation™Network Web APIs varies.
For details, refer to the documents and release notes for each platform.
For details regarding each API, refer to the overview and reference manuals for that specific API.

# Reference Materials

This topic provides information on reference materials users may use during
PlayStation™Network application development.

## Preparation

Refer to the following document regarding requests required in using PlayStation™Network Web APIs:

* [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html)

## PlayStation®5 Applications

Refer to the following documents for the Np library that is required for PlayStation®5 applications to use PlayStation™Network features:

* [Np Library Overview](../Np-Overview/__document_toc.html), [Np Library Reference](../Np-Reference/__document_toc.html)

Refer to the following documents for the NpWebApi2 library that is required for PlayStation®5 applications to use PlayStation™Network Web API features:

* [NpWebApi2 Library Overview](../NpWebApi2-Overview/__document_toc.html), [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html)

## Application Servers

An access token obtained using an authorization code is required for application servers and websites to use PlayStation™Network Web APIs. Refer to the following documents for details on obtaining an access token:

* [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html), [NpAuth Library Reference](../NpAuth-Reference/__document_toc.html) (PlayStation®5)
* [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html), [Auth Web API Reference](../../../WebAPI/latest/Auth_WebAPI-Reference/__document_toc.html)
* [Authentication Features for Websites Overview](../../../WebAPI/latest/Auth_for_Websites-Overview/__document_toc.html), [Authentication Features for Websites Reference](../../../WebAPI/latest/Auth_for_Websites-Reference/__document_toc.html)

## Application Servers (Client Credentials)

A client credential access token can be used by application servers to access some PlayStation™Network Web APIs. Refer to the following documents for details on obtaining an access token:

* [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html)
* [Auth Web API Reference](../../../WebAPI/latest/Auth_WebAPI-Reference/__document_toc.html)

## Back Office Servers

A client credential access token is required for back office servers to use PlayStation™Network Web APIs. Refer to the following documents for details on obtaining the access token:

* [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html)
* [Auth Web API Reference](../../../WebAPI/latest/Auth_WebAPI-Reference/__document_toc.html)

## Details on Each Web API

Refer to the following document for each API group.

**Account Closure**

* [Account Closure Overview](../../../WebAPI/latest/Account_Closure-Overview/__document_toc.html)
* [Account Closure Web API Reference](../../../WebAPI/latest/Account_Closure_WebAPI-Reference/__document_toc.html)

**Active Activities**

* [Active Activities Web API Overview](../../../WebAPI/latest/Active_Activities_WebAPI-Overview/__document_toc.html)
* [Active Activities Web API Reference](../../../WebAPI/latest/Active_Activities_WebAPI-Reference/__document_toc.html)

**Advanced Player Profile**

* [Advanced Player Profile Overview](../../../WebAPI/latest/Advanced_Player_Profile-Overview/__document_toc.html)
* [Advanced Player Profile Web API Reference](../../../WebAPI/latest/Advanced_Player_Profile_WebAPI-Reference/__document_toc.html)

**Advanced Player Profile Management**

* [Advanced Player Profile Management Web API Reference](../../../WebAPI/latest/Advanced_Player_Profile_Management_WebAPI-Reference/__document_toc.html)

**Commerce Management**

* [Commerce Management Web API Overview](../../../WebAPI/latest/Commerce_Management_WebAPI-Overview/__document_toc.html)
* [Commerce Management Web API Reference](../../../WebAPI/latest/Commerce_Management_WebAPI-Reference/__document_toc.html)

**Communication Restriction Status**

* [Communication Restriction Status Web API Overview](../../../WebAPI/latest/Communication_Restriction_Status_WebAPI-Overview/__document_toc.html)
* [Communication Restriction Status Web API Reference](../../../WebAPI/latest/Communication_Restriction_Status_WebAPI-Reference/__document_toc.html)

**Crash Reporting System**

* [Crash Reporting System Overview](../Crash_Reporting_System-Overview/__document_toc.html)
* [Crash Reporting System Web API Overview](../Crash_Reporting_System_WebAPI-Overview/__document_toc.html)
* [Crash Reporting System Web API Reference](../Crash_Reporting_System_WebAPI-Reference/__document_toc.html)

**Entitlements**

* [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html)
* [Entitlements Web API Reference](../../../WebAPI/latest/Entitlements_WebAPI-Reference/__document_toc.html)

**In-Game Catalog**

* [In-Game Catalog Overview](../../../WebAPI/latest/In_Game_Catalog-Overview/__document_toc.html)
* [In-Game Catalog Web API Reference](../../../WebAPI/latest/In_Game_Catalog_WebAPI-Reference/__document_toc.html)

**Leaderboards**

* [Leaderboards Overview](../../../WebAPI/latest/Leaderboards-Overview/__document_toc.html)
* [Leaderboards Web API Reference](../../../WebAPI/latest/Leaderboards_WebAPI-Reference/__document_toc.html)

**Leaderboards Management**

* [Leaderboards Management Web API Overview](../../../WebAPI/latest/Leaderboards_Management_WebAPI-Overview/__document_toc.html)
* [Leaderboards Management Web API Reference](../../../WebAPI/latest/Leaderboards_Management_WebAPI-Reference/__document_toc.html)

**Matches**

* [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html)
* [Matches Web API Reference](../../../WebAPI/latest/Matches_WebAPI-Reference/__document_toc.html)

**Matchmaking**

* [Matchmaking Overview](../../../WebAPI/latest/Matchmaking-Overview/__document_toc.html)
* [Matchmaking Web API Reference](../../../WebAPI/latest/Matchmaking_WebAPI-Reference/__document_toc.html)

**Package/Disc Management**

* [Package/Disc Management Web API Overview](../Package_Disc_Management_WebAPI-Overview/__document_toc.html)
* [Package/Disc Management Web API Reference](../Package_Disc_Management_WebAPI-Reference/__document_toc.html)

**Profanity Filter**

* [Profanity Filter Web API Overview](../../../WebAPI/latest/Profanity_Filter_WebAPI-Overview/__document_toc.html)
* [Profanity Filter Web API Reference](../../../WebAPI/latest/Profanity_Filter_WebAPI-Reference/__document_toc.html)

**Session Manager**

* [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html)
* [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html)
* [Session Manager Web API Reference](../../../WebAPI/latest/Session_Manager_WebAPI-Reference/__document_toc.html)

**Subscription Status**

* [Subscription Status Web API Overview](../../../WebAPI/latest/Subscription_Status_WebAPI-Overview/__document_toc.html)
* [Subscription Status Web API Reference](../../../WebAPI/latest/Subscription_Status_WebAPI-Reference/__document_toc.html)

**Title Cloud Storage**

* [Title Cloud Storage Service Overview](../../../WebAPI/latest/TCS-Overview/__document_toc.html)
* [Title Cloud Storage Web API Reference](../../../WebAPI/latest/TCS_WebAPI-Reference/__document_toc.html)

**Title Cloud Storage Management**

* [Title Cloud Storage Management Web API Overview](../../../WebAPI/latest/TCS_Management_WebAPI-Overview/__document_toc.html)
* [Title Cloud Storage Management Web API Reference](../../../WebAPI/latest/TCS_Management_WebAPI-Reference/__document_toc.html)

**Universal Data System Configuration**

* [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html)
* [Universal Data System Configuration Web API Reference](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Reference/__document_toc.html)

**User Profile**

* [User Profile Overview](../../../WebAPI/latest/User_Profile-Overview/__document_toc.html)
* [User Profile Web API Reference](../../../WebAPI/latest/User_Profile_WebAPI-Reference/__document_toc.html)