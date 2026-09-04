# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/development-process-overview.html

# Development Process Overview

This topic provides on overview of the general development process of a feature that uses UDS.

General Development Process

1. **Request to use services.** To use a service based on UDS, such as the trophy service, you need to submit a request
   to use that service as well as the UDS service.
2. **Define PlayStation™Network objects.** Use the UDS Management Tool and/or the configuration Web API to define PlayStation™Network
   objects. For required PlayStation™Network objects and metadata, refer to the document
   of the service you want to use. There are some services that do not require the defining
   of PlayStation™Network objects. When a definition is not required, this step can be
   skipped. For details on the configuration API, refer to the [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html).
3. **Define events.** Use the UDS Management Tool and/or the configuration Web API and define UDS events
   to be sent by your game. For details on the configuration API, refer to the [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html).
4. **Define stats.** Use the UDS Management Tool and/or the configuration Web API to define stats. For
   required stats and their properties, refer to the document of the service you want
   to use. Note that events that correspond to stats must be defined in advance. For
   details on the configuration API, refer to the [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html).
5. **Configure the service.** Depending on the service, configuration unique to the service may be required in
   addition to UDS definition. Use the tool provided by the service to perform configuration
   that is unique to the service.
6. **Download configuration file.** Download the configuration file from Package/Disc Management Tool (GEMS) and place
   the configuration file in the root directory. For details, refer to the [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html).
7. **Implement.** Once you complete definitions and configuration for using the service, implement
   your program. Some services (for example, matches) provide a library or API unique
   to the service; refer to the document of each service. You can generate both a code
   and a header file using Codegen.
8. **Debug and test.** Various features are provided for debugging and testing. Provided debugging and testing
   features are as follows:

**Features to Delete UDS-Related Data**

UDS-related data created and configured on the console while developing, debugging,
and testing can be deleted from the system software menu.

* Delete UDS-related data of all users on the console.
* Delete UDS-related data of a specific user on the console.
* Delete UDS-related data of a specific user on the console and on the server.

For details on the features, refer to the [NpUniversalDataSystem Library Reference](../NpUniversalDataSystem-Reference/__document_toc.html).

**The UDS Management Tool**

The UDS Management Tool is a web-based tool that enables the viewing of data sent
from a game application during developing, debugging, and testing, as well as the
viewing of data processed from the sent data. This tool has the following features:

* Event log viewer.
* Stats viewer.
* State viewer.

For details on the UDS Management Tool, refer to [Using the UDS Management Tool](using-the-uds-management-tool.html "The Universal Data System Management Tool allows you to define PlayStation™Network Objects, UDS Events and UDS stats definitions.").