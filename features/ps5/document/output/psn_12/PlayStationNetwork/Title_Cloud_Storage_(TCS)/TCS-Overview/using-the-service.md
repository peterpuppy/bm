# Title Cloud Storage Service Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS-Overview/using-the-service.html

# Using the Service

This topic explains the standard development process when using the Title Cloud Storage service, how to use the Title Cloud Storage Tool, and usage of prominent API features.

# Overview of the Development Process

The standard process for using the Title Cloud Storage service is as follows:

1. **Applying for Service**

   The Title Cloud Storage service can be used by applying for usage on the Developer Network (DevNet) website (<https://partners.playstation.net/>). After applying for the service, you will be able to acquire IDs and various data required for development.
2. **Development**

   Develop your application that uses the Title Cloud Storage service using the NpWebApi2 library or NpCppWebApi library, referring to references, sample code, and so forth, as necessary.

   The Title Cloud Storage Tool can be used for configuring the slots that will be used, resetting data that has been configured, and other purposes.

   Additionally, use the Title Cloud Storage Management Web API if you would like to delete data or variables or perform other such operations.
3. **Testing**

   Perform tests using the Title Cloud Storage Tool and the Title Cloud Storage Management Web API as required.
4. **Submission (Package Submission, Applying for Certification, etc.)**

   Submit the developed application to Platform Certification and Operations (CertOps).

# Using the Title Cloud Storage Tool

The Title Cloud Storage Tool is a Web tool that can be accessed from DevNet using a DevNet account that has been configured with the right privileges.

Among other actions, the Title Cloud Storage Tool can be used to set up services, set up each slot, reset registered data and variables, apply development environment (DEV or sp-int) settings to the production environment (RETAIL), and set up snapshot output schedules.

Note:

About the service state switcher in the Sandbox network architecture:

* The service state switcher will be displayed for titles that have been migrated to the PlayStation® environments of the Sandbox network architecture. The descriptions provided in the subsequent chapters are for when "Published to DEV" is specified as the service state. Refer to [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html) for details about the service states.

Note:

Correspondence Table of Environment Names

| Legacy network architecture | | Sandbox network architecture |
| --- | --- | --- |
| Environment name displayed in the tool | Environment name | Environment name and the environment name displayed in the tool |
| Development | sp-int | DEV |
| QA | prod-qa | CERT |
| Production | RETAIL | RETAIL |

## Slot Setup

Setting Up Slots Using the Title Cloud Storage Tool

Among other actions, the Title Cloud Storage Tool can be used to make privilege settings for each slot and set the maximum and minimum values to slots for variables. In addition, the settings onscreen can be applied to the development environment (DEV or sp-int) server by clicking the Send to Server button.

Note:

By default, the privilege settings for each slot are set to Empty (refuse all access). To add privileges, fill in all items and then click the + button (add button) that appears to the far right afterward, as shown in [the figure below](using-the-title-cloud-storage-tool.html#title-cloud-storage-service-overview_2_2__fig_y34_zmq_vfc). However, merely clicking the + button and changing the settings does not cause the changes to be applied on the server. By clicking the Send to Server button after making your changes, you can apply the added privileges to the server.

Slots can be newly created, changed, or deleted by selecting Edit from the Action menu of the Slot Definitions screen.

Configuration values can be imported or exported in the JSON format by selecting Import/Export from the Action menu. The revision of slot definitions for slots that haven't changed will also increase when import is carried out.

By selecting "Publish to CERT and RETAIL" or "Publish" from the Action menu, slot definitions from the development environment (DEV or sp-int) are applied to both the certification environment (CERT or prod-qa) and production environment (RETAIL) at once. Always perform this step to publish the slot configuration before starting to use the certification environment (CERT or prod-qa) and production environment (RETAIL). Services for which the Publish step has not been carried out will not function correctly.

Only slot configuration will be applied. Variables and data of the slot won't be applied.

The date when the slot configuration was applied to each environment can be checked from Last Updated.

The slot configuration in the development environment (DEV or sp-int) can be deleted if it hasn't been applied yet to other environments.

The lock status of an applied slot configuration will transition from Unlocked to Locked. A Locked slot configuration cannot be deleted or changed. Even if import is carried out, the update of a Locked slot will be skipped.

The lock status of a slot cannot be changed from Locked to Unlocked on the Title Cloud Storage Tool. Contact SIE if you want to change or delete the slot configuration after it has been applied to the QA environment or production environment.

## Services Setup

On the Manage Service Configuration screen, service usage times can be configured, and services can be temporarily suspended for maintenance.

Setting Up Services Using the Title Cloud Storage Tool

Having set up the service parameters below via Edit in the Actions menu on the Manage Service Configuration screen, you can select Update Service Configuration to apply the configured parameters on the server for the specified environment.

Configurable Service Parameters

| **Parameter Name** | **Description** |
| --- | --- |
| Service Period - Begin | The date and time at which the service comes into effect |
| Service Period - End | The date and time at which the service ends |
| Maintenance Mode | Switch the service between maintenance and in-use modes |

It is essential that services are configured for each environment. Services will not operate correctly if they have not been configured, even if slot settings have been applied across each environment.

## Snapshot Schedule Settings

Manage Snapshots can be used title-wide by browsing the history, or by backing up the "anyone" slot.

Setting Up Snapshot Schedules Using the Title Cloud Storage Tool

Having set up the snapshot schedule parameters below on the Manage Data Schedules screen ([the figure above](using-the-title-cloud-storage-tool.html#title-cloud-storage-service-overview_2_2__2cbeb91c-5770-11ee-8c99-0242ac120002)) or the Manage Variables Schedules screen (not pictured), you can then select Create Schedule/Update Schedule to apply the configured parameters on the server for the specified environment. Snapshots are output asynchronously according to the set conditions and can be downloaded in a compressed file format.

Configurable Snapshot Schedule Parameters

| **Parameter Name** | **Description** |
| --- | --- |
| Name | Arbitrary name |
| Description | Arbitrary description (e.g. usage) |
| Recurring Type | Change recurrence  Only "Once only" is supported |
| User Mode | Change snapshot user classification  Only the "anyone" user is supported |
| File Format | Change file format  JSON/CSV |
| Date/Time | Date and time that snapshots are output |
| Enabled | Change enabled/disabled |

Snapshot schedules can be set for the development environment (DEV or sp-int) and production environment (RETAIL). Up to ten schedules can be set for each environment. To create a new schedule when the maximum has already been reached, an existing schedule must be deleted or disabled.

Results of the snapshot output can be viewed on the View Data Snapshots screen.

## Operational History

The TCS Tool keeps audit logs and operational history. By clicking the [Operational History] tab, you can check the changes that have been made to a service with a particular NP communication ID.

[Operational History] Tab

There are multiple data items in the operational history list view, and these items can be sorted by each column. The data items included in the list view are provided below:

* **Date and Time** - The date and time that the operation was performed
* **Log Level** - The log level (INFO, WARN, or ERROR)
* **Actor** - The name of the person who performed the operation
* **Action** - The operation that was performed
* **Target** - The item on which the operation was performed
* **Status** - The state of progress of the operation
* **Summary** - A simple description of the operation that was performed

Logs of operations can also be displayed in JSON format. In the JSON format view, information is displayed when you click the blue arrows displayed on each row.

Operational History

## Feature Differences before and after Migration to the PlayStation® Environments of the Sandbox Network Architecture

|  |  |  |
| --- | --- | --- |
|  | Before title migration | After title migration |
| Editing slot definitions in the locked state | Not possible | Possible |
| Setting the service configuration | Required | Optional |

# Setting and Obtaining TCS Variables Using the Title Cloud Storage Web API

You can set and obtain TCS variables by using requests such as `setMultiVariablesByUser` and `getMultiVariablesByUser`. You can also obtain multiple slots of TCS variables belonging to a given user at once or batch-obtain TCS variables from specific slots belonging to multiple users who are friends or who are individually specified.

Furthermore, you can atomically update a specific TCS variable using requests such as `addAndGetVariable` and `setVariableWithConditions`.

# Uploading and Downloading TCS Data Using the Title Cloud Storage Web API

You can upload and download TCS data using requests such as `uploadData` and `downloadData`. You can also download in parts using Range and If-Match. Additionally, you can write arbitrary data to slots as supplementary data. Furthermore, you can use requests such as `getMultiDataStatusesBySlot` and `getMultiDataStatusesByUser`, which are for batch-obtaining supplementary data associated with individual pieces of TCS data, the data identifiers that consist of object IDs, latest update dates, and other status information.

You can use `X-Psn-Atomic-Operation` headers to atomically register main TCS data and supplementary data associated with it. Perform the request by following the procedure given below:

1. Specify "`X-Psn-Atomic-Operation: begin`" in the request header when running `setDataInfo` - which sets supplementary data - or otherwise beginning an atomic registration session.
2. An ID for keeping track of the atomic registration session is issued, and a response header including "`X-Psn-Atomic-Operation-Id: {UUID}`" is returned.
3. Next, when uploading the TCS data using `uploadData`, specify "`X-Psn-Atomic-Operation-Id: {UUID}`" in the request header.
4. During the final request, specify "`X-Psn-Atomic-Operation-Id: {UUID}`" and "`X-Psn-Atomic-Operation: end`" in the request header.

# Setting TCS Variables/TCS Data Using the Title Cloud Storage Management Web API

If you are distributing common TCS data and variables to all users of a title, set up the data and variables using the Title Cloud Storage Management Web API. For details, refer to the [Title Cloud Storage Management Web API Overview](../TCS_Management_WebAPI-Overview/__document_toc.html) and [Title Cloud Storage Management Web API Reference](../TCS_Management_WebAPI-Reference/__document_toc.html) documents.