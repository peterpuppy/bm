# Universal Data System Configuration Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Universal_Data_System_Configuration_WebAPI-Overview/about-the-uds-configuration-web-api.html

# Universal Data System Configuration Web API Overview

This chapter provides an overview of how to use the Universal Data System Configuration Web API.

The Universal Data System (UDS) Configuration Web API is a management feature for back office servers. It provides abilities that allow you to configure PlayStation™Network objects, UDS events and UDS stats. This Web API aids in flexibility in the development pipeline. For example, you can embed the API into your own system to configure them.

The API is provided to complement the configuration of the Universal Data System service by the target application. Therefore, use it within the scope of the target application's use of the Universal Data System service.

Note: The Universal Data System Configuration Web API is not supported in the Sandbox Network Architecture. To configure PlayStation™Network objects in Sandbox, you must use the `np-service-config` CLI tool or the UDS Management Tool. For more information, see [NP Service Config User's Guide](../../../SDK/latest/NP_Service_Config-Users_Guide/__document_toc.html) and [Universal Data System Guide - Using the UDS Management Tool](../../../SDK/latest/Universal_Data_System-Guide/using-the-uds-management-tool.html).

Note:

The licensee is fully responsible for the following results occurring due to the use of the Universal Data System Configuration Web API:

* Creation, change, and deletion of universal data system configuration information stored on the server and any effects these actions may have on the application.
* Any effects on users using the target application (provide appropriate user support).

SIE shall not be responsible for any of the above, including the responsibility to restore universal data system information stored on the server.

Note:

SIE may take any measures as it sees fit without prior notice, including terminating the use of the Universal Data System Configuration Web API, if the licensee acts as follows:

* Causes a server overload.
* Violates any of the points to note.
* Is inappropriate/insufficient in providing user support regarding universal data system information.
* Is otherwise not using the Universal Data System Configuration Web API in an appropriate manner.

In such a case, SIE may notify users that there is a problem with the Universal Data System information of the target application.

## Main Features

Back office servers (servers used mainly for development and operation support) can use the Universal Data System Configuration Web API to:

* List, create and update, and delete custom stats definitions and extractions.
* List, create and update, and delete PlayStation™Network Objects and UDS events.
* List, create and update, and delete `npConfigTag`.
* List, create, and update media assets.
* Provide a diagnostic report on configurations.

Note: The diagnostics report is in JSON format. However, it is strongly recommended to not parse the report with software since it may change in the future.

## Reference Materials

Refer to the following document for information about the Universal Data System:

* [Universal Data System Guide](../../../SDK/latest/Universal_Data_System-Guide/__document_toc.html)

For details about how to set up configuration using the UDS Management tool, refer to:

* [Universal Data System Guide - Using the UDS Management Tool](../../../SDK/latest/Universal_Data_System-Guide/using-the-uds-management-tool.html)

## Related Information

In addition to this document, SIE also provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements. You can refer to the release notes below:

* [Release Notes - Universal Data System Configuration Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Universal_Data_System_Configuration_WebAPI-ReleaseNotes.html)