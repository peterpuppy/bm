# PlayStation™Network Tournaments System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Tournaments_System-Overview/overview.html

# PlayStation™Network Tournaments System Overview

This chapter provides an overview of the PlayStation™Network tournaments system and its related services.

Tournaments are PlayStation™Network objects that are tied to existing competitive activities that allow you to create and schedule automated tournaments. This document explains how to integrate and test tournaments using the Debug UI, which is available from the **Debug** menu.

For more information on tournaments, see [PlayStation®5 Tournaments Guide](../PS5_Tournaments-Guide/__document_toc.html).

## Requesting Services

To enable tournaments, you must request the Tournament and UDS services for your product. For information on requesting PlayStation™Network services, see [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

## Implementation

Tournaments use the [Matches Web API Reference](../../../WebAPI/latest/Matches_WebAPI-Reference/__document_toc.html) and samples referenced from the [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html) documents.

Use the sample programs provided by the Matches Web API as well as other relevant documentation to start a tournament match and report the results to the server. The Tournament service uses this information to advance the player to the next bracket or end the tournament.

## Testing and Debugging

Test and debug tournaments from **Debug Settings**. You can also use **Debug Settings** > **PlayStation™Network** > **Tournaments** > **Card Preview** to check the appearance and behavior of activities that are displayed on the system software.

## Reference Materials

Refer to the following document for an overall look at the features of the PlayStation™Network:

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)

Refer to the following documents for an overview of the Universal Data System (UDS) and the procedure for developing applications that use it:

* [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html)
* [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html)
* [Universal Data System Configuration Web API Reference](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Reference/__document_toc.html)

Refer to the following document for information on defining Activity and Tournament objects:

* [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html)
* [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html)

Refer to the following document for how to obtain UDS configuration files:

* [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html)

Refer to the following document for additional information on the tournament feature and related services:

* [PlayStation®5 Tournaments Guide](../PS5_Tournaments-Guide/__document_toc.html)
* [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html)
* [Matches Web API Reference](../../../WebAPI/latest/Matches_WebAPI-Reference/__document_toc.html)

Refer to the following document for Game SDK functionality related to tournaments:

* [SystemService Library Overview](../SystemService-Overview/__document_toc.html)
* [SystemService Library Reference](../SystemService-Reference/__document_toc.html)