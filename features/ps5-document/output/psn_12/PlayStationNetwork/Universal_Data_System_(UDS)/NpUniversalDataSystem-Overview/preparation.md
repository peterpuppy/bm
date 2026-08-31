# NpUniversalDataSystem Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Overview/preparation.html

# Using the Library

This topic explains how to use the NpUniversalDataSystem library. It first describes how to create and where to place the configuration files that must be prepared to use the library; then it describes the procedures for configuring each type of processing, initialization, event-sending, and termination; and then it describes debug support features.

# Preparation

Applications that send events to the UDS server using the NpUniversalDataSystem library must be configured beforehand, and the resulting UDS configuration files that are generated must be placed in the designated directory. This section describes this procedure. Refer to the [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) document for information about the general development process of features that use UDS.

The preparation flow is shown in [the following figure](preparation.html#np-universal-data-system-library-overview_1_1__7534a22e-e267-11ee-bd3d-0242ac120002).

The workflow described here uses the UDS Management Tool and Package/Disc Management Tool (GEMS) ("GEMS" hereafter), but the Local Development Workflow that uses np-universal-data-system-local-tool is also supported. Refer to [Universal Data System Guide - Local Development Workflow](../Universal_Data_System-Guide/local-development-workflow.html) for details about the Local Development Workflow.

UDS Preparation Flow

1. **Make service requests**

   Make a request to use UDS on the PlayStation®5 Developer Network. Do the same for the Trophy 2 service if trophies are used.

   Refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) document for information about making service requests.
2. **Configure UDS**

   Use the UDS Management Tool to define UDS Events, Stats, Objects, and trophies. Refer to the [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) document for information about the UDS Management Tool.
3. **Obtain the package metadata file**

   The package metadata file can be obtained using the Package/Disc Management Tool (GEMS). After completing UDS configuration, follow the procedure described in the [Package/Disc Management Tool (GEMS) Overview - Downloading Configuration Files](../Package_Disc_Management_Tool_GEMS-Overview/downloading-configuration-files.html) topic to obtain the package metadata file (npconfig.zip). The package metadata file contains UDS configuration files and trophy configuration files.
4. **Place UDS configuration files in the correct directory**

   Extract the package metadata file downloaded from GEMS to right inside the sce\_sys directory of the application binary that will be launched. After extraction, the directory structure should be as shown in [the following figure](preparation.html#np-universal-data-system-library-overview_1_1__fig_an1_cwy_bbc).

   Directory Structure

# Initialization

1. **Initialize the UserService library**

   Initialize the UserService library. For details, refer to [UserService Library Overview - Using the Library - Basic Procedure](../UserService-Overview/basic-procedure.html).
2. **Set the NP Title ID and NP Title Secret**

   To use the NpUniversalDataSystem library, set the NP Title ID and NP Title Secret. For details, refer to [Np Library Overview - Using the Library - Basic Procedure](../Np-Overview/basic-procedure.html).
3. **Load the NpUniversalDataSystem module**

   Call `sceSysmoduleLoadModule()` with `SCE_SYSMODULE_NP_UNIVERSAL_DATA_SYSTEM` specified as the module ID and load the PRX module.
4. **Initialize the NpUniversalDataSystem library**

   First, create a structure of the `SceNpUniversalDataSystemInitParam` type as the initialization parameter for the NpUniversalDataSystem library, and set the sizes of the structure and of the memory pool used by the NpUniversalDataSystem library.

   Afterward, call `sceNpUniversalDataSystemInitialize()` to initialize the NpUniversalDataSystem library.

   ```
   SceNpUniversalDataSystemInitParam param;
   memset(&param, 0, sizeof(param));
   param.size = sizeof(SceNpUniversalDataSystemInitParam);
   param.poolSize = 128 * 1024;

   ret = sceNpUniversalDataSystemInitialize(&param);
   if (ret < 0) {
       // Error handling
   }
   ```

   Note:

   The size of the memory pool used by the NpUniversalDataSystem library depends on the sizes and number of events created by the application that exist at the same time. The size of the memory used by the NpUniversalDataSystem library can be checked using `sceNpUniversalDataSystemGetMemoryStat()`; therefore, conduct several tests and refer to the values that you obtain to help determine the value to specify for the initialization parameter.
5. **Create a context**

   A context must be created to send an event. Call `sceNpUniversalDataSystemCreateContext`() to create a context for each user. Normally, a call is made when a user logs in and joins a game. Specify the NP service label and the user ID for the user in question when this happens. Use the NP service label that you specified when you applied for the service.

   Note that, as described in the "[Preparation](preparation.html)" section, the UDS configuration files corresponding to the specified NP service label must be placed in the correct directory.

   ```
   SceUserServiceUserId userId;    // Be sure to store an appropriate user ID
   SceNpServiceLabel serviceLabel = 0;
   SceNpUniversalDataSystemContext context = SCE_NP_UNIVERSAL_DATA_SYSTEM_INVALID_CONTEXT;
   ret = sceNpUniversalDataSystemCreateContext(&context, userId, serviceLabel, 0);
   if (ret < 0) {
       // Error handling
   }
   ```

   Note:

   The only NP service label that can be used on UDS at the present time is 0.
6. **Create a handle**

   Create a variable of type `SceNpUniversalDataSystemHandle` and call `sceNpUniversalDataSystemCreateHandle()` to create a handle.

   ```
   SceNpUniversalDataSystemHandle handle = SCE_NP_UNIVERSAL_DATA_SYSTEM_INVALID_HANDLE;
   ret = sceNpUniversalDataSystemCreateHandle(&handle);
   if (ret < 0) {
       // Error handling
   }
   ```
7. **Register a context**

   Call `sceNpUniversalDataSystemRegisterContext()` to register a context. An event cannot be sent using an unregistered context.

   ```
   ret = sceNpUniversalDataSystemRegisterContext(context, handle, 0);
   if (ret < 0) {
       // Error handling
   }
   ```

   Because processing in this function takes time, try to call it from a subthread. The specific processing that happens is as follows:

   * For each user, either a new UDS Stats data file is created, or an existing file is opened
   * If the UDS configuration information is of a newer version, the existing UDS Stats data file is updated
   * Related features linked to UDS (for example, trophies), are set up
8. **Destroy the handle**

   Call `sceNpUniversalDataSystemDestroyHandle()` to destroy the handle.

   ```
   ret = sceNpUniversalDataSystemDestroyHandle(handle);
   if (ret < 0) {
       // Error handling
   }
   ```

## When to Create/Register/Destroy Contexts

Creation and registration of a context must be performed for each user. For ordinary use-cases, create and register a context when a logged-in user joins the game, and destroy that context when the user logs out.

## When UDS Configuration Information Is Installed

An application supporting UDS must create a UDS configuration file and include it on a disc or in a package in the designated manner. UDS configuration information will be automatically installed on the internal SSD of the console by the system software before the application is launched.

When the application is launched from the debugger or the workspace during development, the information will be installed on the internal SSD at the when `sceNpUniversalDataSystemRegisterContext()` is called. In addition to `sceNpUniversalDataSystemRegisterContext()`, there are other functions that result in internal UDS setup processing (e.g., `sceNpTrophy2RegisterContext()` in the NpTrophy2 library) that can be used to perform the same task.

UDS configuration information installed on the internal SSD will be shared by all users.

## When UDS Stats Data Is Installed

In contrast to UDS configuration information, which is automatically installed and shared among users, UDS Stats data is created on the internal SSD for each user when the application calls `sceNpUniversalDataSystemRegisterContext()`. In addition to `sceNpUniversalDataSystemRegisterContext()`, there are other functions that result in internal UDS setup processing (e.g., `sceNpTrophy2RegisterContext()` in the NpTrophy2 library) that can be used to perform the same task.

# Sending Events

1. **Create a handle**

   Create a variable of type `SceNpUniversalDataSystemHandle` and call `sceNpUniversalDataSystemCreateHandle()` to create a handle.
2. **Create events**

   The methods to create several feature events are shown below as typical usage examples. Although it is possible to customize event names and property names, their default values are used for the explanation without changes.

   Note:

   In addition to the examples below, examples for creating an event to unlock a trophy and for creating an event to update a trophy's progress are introduced in the [Trophy System Overview - Overview of Application Development - Implementation of Trophy-Unlocking](../Trophy_System-Overview/implementation-of-trophy-unlocking.html) topic.

   * **activityStart**

     This event indicates that a user started an activity. An activity with "Quest1" as the ID is started in the example below.

     First, call `sceNpUniversalDataSystemCreateEvent()` to create an empty event and obtain a reference to the event's properties.

     ```
     SceNpUniversalDataSystemEvent *event = NULL;
     SceNpUniversalDataSystemEventPropertyObject *prop = NULL;
     ret = sceNpUniversalDataSystemCreateEvent("activityStart", NULL, &event, &prop);
     if (ret < 0) {
         // Error handling
     }
     ```

     Next, use a property operating function to add the `activityId` property, which represents the activity's ID, to the event properties' reference that was obtained in the previous step.

     ```
     ret = sceNpUniversalDataSystemEventPropertyObjectSetString(prop, "activityId", "Quest1");
     if (ret < 0) {
         // Error handling
     }
     ```
   * **activityEnd**

     This event indicates that an activity ended. An activity with "Quest1" as the ID successfully ends in the example below.

     First, call `sceNpUniversalDataSystemCreateEvent()` to create an empty event and obtain a reference to the event's properties.

     ```
     SceNpUniversalDataSystemEvent *event = NULL;
     SceNpUniversalDataSystemEventPropertyObject *prop = NULL;
     ret = sceNpUniversalDataSystemCreateEvent("activityEnd", NULL, &event, &prop);
     if (ret < 0) {
         // Error handling
     }
     ```

     Next, use a property operating function to add the `activityId` property, which represents the activity's ID, and the `outcome` property, which represents the result, to the event properties' reference that was obtained in the previous step.

     ```
     ret = sceNpUniversalDataSystemEventPropertyObjectSetString(prop, "activityId", "Quest1");
     if (ret < 0) {
         // Error handling
     }
     ret = sceNpUniversalDataSystemEventPropertyObjectSetString(prop, "outcome", "completed");
     if (ret < 0) {
         // Error handling
     }
     ```
   * **activityAvailabilityChange**

     This event indicates a change for each activity regarding whether the activity can be started. The transition to a state where activities with IDs "Quest2" and "Quest3" can be started and other activities cannot be started is shown in the example below.

     First, call `sceNpUniversalDataSystemCreateEvent()` to create an empty event and obtain a reference to the event's properties.

     ```
     SceNpUniversalDataSystemEvent *event = NULL;
     SceNpUniversalDataSystemEventPropertyObject *prop = NULL;
     ret = sceNpUniversalDataSystemCreateEvent("activityAvailabilityChange", NULL, &event, &prop);
     if (ret < 0) {
         // Error handling
     }
     ```

     Next, use a property operating function to add the `availableActivities` property, which represents an array of IDs of activities that can be started, and add the IDs of activities that can be started as elements of the property to the event properties' reference that was obtained in the previous step.

     ```
     SceNpUniversalDataSystemEventPropertyArray *idArray;
     ret = sceNpUniversalDataSystemEventPropertyObjectSetArray(prop, "availableActivities", NULL, &idArray);
     if (ret < 0) {
         // Error handling
     }
     ret = sceNpUniversalDataSystemEventPropertyArraySetString(idArray, "Quest2");
     if (ret < 0) {
         // Error handling
     }
     ret = sceNpUniversalDataSystemEventPropertyArraySetString(idArray, "Quest3");
     if (ret < 0) {
         // Error handling
     }
     ```
3. **Post the event**

   Call `sceNpUniversalDataSystemPostEvent()` to post an event. Try to call this function from a subthread because its processing may take time. Specify a context, a handle, and an event as the arguments.

   ```
   ret = sceNpUniversalDataSystemPostEvent(context, handle, event, 0);
   if (ret < 0) {
       // Error handling
   }
   ```
4. **Destroy the event**

   Call `sceNpUniversalDataSystemDestroyEvent()` to destroy the event.

   ```
   ret = sceNpUniversalDataSystemDestroyEvent(event);
   if (ret < 0) {
       // Error handling
   }
   ```
5. **Destroy the handle**

   Call `sceNpUniversalDataSystemDestroyHandle()` to destroy the handle.

## Aborting Processing

To abort processing of a function of the NpUniversalDataSystem library that is taking time, such as a function for posting events, call `sceNpUniversalDataSystemAbortHandle()`.

Note:

When processing is aborted with `sceNpUniversalDataSystemAbortHandle()`, the used handle should be destroyed with `sceNpUniversalDataSystemDestroyHandle()`. The handle can then be created again with `sceNpUniversalDataSystemCreateHandle()`, and the execution of the aborted processing can be reattempted.

# Termination

1. **Destroy the context**

   When a context is no longer necessary due to user log-out, etc., call `sceNpUniversalDataSystemDestroyContext()` to destroy the context.

   ```
   int ret;
   SceNpUniversalDataSystemContext ctxId;

   // Assuming that an appropriate value is stored in ctxId

   ret = sceNpUniversalDataSystemDestroyContext(ctxId);
   if (ret < 0) {
       // Error handling
   }
   ```
2. **Terminate the NpUniversalDataSystem library**

   Call `sceNpUniversalDataSystemTerminate()` to terminate the NpUniversalDataSystem library.

   ```
   ret = sceNpUniversalDataSystemTerminate();
   if (ret < 0) {
       // Error handling
   }
   ```
3. **Unload the NpUniversalDataSystem module**

   Call `sceSysmoduleUnloadModule()` with `SCE_SYSMODULE_NP_UNIVERSAL_DATA_SYSTEM` specified for the module ID to unload the PRX module.

## Handling the Contexts of Logged-Out Users

When a user logs out, the relevant context is invalidated by the system software and can no longer be used. Furthermore, even if the same user logs back in, the context will not be revalidated; you must first destroy the context for the user and then recreate/re-register a new context.

# Debug Support Through the System Software

The following is an explanation of features provided by the system software for developing UDS-compatible applications. These features can be accessed from "★Debug Settings" in the system software. The features in "Universal Data System data" that delete UDS-related data can also be executed from the command line on a host PC using the prospero-ctrl utility (prospero-ctrl.exe). For details about the prospero-ctrl utility, refer to "Target Manager CLI User's Guide - Controlling Targets using the command line - Controlling Targets with prospero-ctrl".

## Displaying the UDS Debug Log

The UDS debug log is a feature that outputs to Console Output the states of NpUniversalDataSystem function calls made from a game, UDS events posted from a game, and the data of UDS Stats and UDS States that have been updated by those events. By using this log, you can easily confirm - without needing to use the UDS Management Tool - whether function calls are being made, whether UDS events are being posted from a game as expected, and whether the UDS configuration taken from a downloaded npconfig.zip is applied as expected. To enable the UDS debug log, set the Release Check Mode to Development Mode and then select "★Debug Settings" > "PlayStation Network" > "Universal Data System Debug Log" > "ON" from "Settings" in the system software.

When the UDS debug log is enabled, information about each NpUniversalDataSystem function call made from a game is output to the USER8 channel of Console Output. The output timing is at the start and end of each function call, and an error code is also output if processing fails. In addition, when `sceNpUniversalDataSystemPostEvent()` posts an event, the posted UDS event and the associated UDS Stats and UDS State information are output. This output happens at the point when a UDS event is posted from a game and saved to the console. Because this log is output without waiting for data to be transferred to the UDS server, the log can be checked even when a user is not signed in to the PlayStation™Network or when the user is offline. Be aware, however, that this means that the feature cannot be used for confirming that UDS events are reaching the UDS server.

Note that the contents and format of what is output to the UDS debug log may change with updates to the system software.

**NpUniversalDataSystem Functions**

Information is output as follows for each NpUniversalDataSystem function that is called by a game.

```
[UDS][API] sceNpUniversalDataSystemInitialize() start
[UDS][API] sceNpUniversalDataSystemInitialize() success
[UDS][API] sceNpUniversalDataSystemCreateContext() start
[UDS][API] sceNpUniversalDataSystemCreateContext() success
[UDS][API] sceNpUniversalDataSystemCreateHandle() start
[UDS][API] sceNpUniversalDataSystemCreateHandle() success
[UDS][API] sceNpUniversalDataSystemRegisterContext() start
[UDS][API] sceNpUniversalDataSystemRegisterContext() success
[UDS][API] sceNpUniversalDataSystemCreateEvent() start
[UDS][API] sceNpUniversalDataSystemCreateEvent() success
[UDS][API] sceNpUniversalDataSystemEventPropertyObjectSetString() start
[UDS][API] sceNpUniversalDataSystemEventPropertyObjectSetString() success
[UDS][API] sceNpUniversalDataSystemPostEvent() start
[UDS][API] sceNpUniversalDataSystemPostEvent() error(0x80553100)
```

**UDS Events**

For each UDS event posted from a game, information concerning the event is output as shown in the example provided below:

```
[UDS][Event] =================================================
[UDS][Event] UDS Event
[UDS][Event]     eventId: 2cd55677-6a3c-11ed-890c-78c88198168f
[UDS][Event]     eventName: myActivityStart
[UDS][Event]     eventType: activityStart
[UDS][Event]     timestamp: 2022-11-22T08:03:40.000000000Z
[UDS][Event]     properties:
[UDS][Event]         {
[UDS][Event]             "myActivityId": "activity1",
[UDS][Event]         }
[UDS][Event]     mappedProperties:
[UDS][Event]         {
[UDS][Event]             "activityId": "activity1",
[UDS][Event]         }
[UDS][Event] =================================================
[UDS][Event] =================================================
[UDS][Event] UDS Event
[UDS][Event]     eventId: 4c983692-6a3c-11ed-890c-78c88198168f
[UDS][Event]     eventName: myCustom
[UDS][Event]     eventType: custom
[UDS][Event]     timestamp: 2022-11-22T08:04:33.000000000Z
[UDS][Event]     properties:
[UDS][Event]         {
[UDS][Event]             "value1": 100 (Int32),
[UDS][Event]         }
[UDS][Event]     mappedProperties:
[UDS][Event]         {
[UDS][Event]         }
[UDS][Event]     warnings:
[UDS][Event]         - missingProperty: "value2"
[UDS][Event] =================================================
```

The information that is output includes the following information added within the system software (in addition to the event name and properties set by the game):

* Event type
* Event ID
* Timestamp
* Mapped property
* Warnings, such as inconsistencies with definitions

**UDS Stats**

If UDS Stats are linked to the definition of a posted UDS event, the Stat ID, Stat Name, value, and data type of each UDS Stat is shown, as in the example provided below:

```
[UDS][Stats] =================================================
[UDS][Stats] UDS Stat
[UDS][Stats]     statId: 1
[UDS][Stats]     statName: myLatestValue
[UDS][Stats]     value:100 (int32)
[UDS][Stats] =================================================
[UDS][Stats] =================================================
[UDS][Stats] UDS Stat
[UDS][Stats]     statId: 2
[UDS][Stats]     statName: myMaxValue
[UDS][Stats]     value:1000 (int32)
[UDS][Stats] =================================================
[UDS][Stats] =================================================
[UDS][Stats] UDS Stat
[UDS][Stats]     statId: 3
[UDS][Stats]     statName: myMinValue
[UDS][Stats]     value:0 (int32)
[UDS][Stats] =================================================
```

**UDS State**

If a posted UDS event is a feature event, a list of applicable PlayStation™Network object names is displayed for each related UDS State:

```
[UDS][State] =================================================
[UDS][State] Ever Played Activities
[UDS][State]     activity1
[UDS][State]     activity2
[UDS][State]     activity3
[UDS][State] =================================================
```

## Detecting When the UDS Event Posting Rate Limit Has Been Exceeded

The system provides a feature that monitors the rate at which UDS events are posted and that displays a notification if it detects that the maximum rate limit has been exceeded. This feature is enabled by default, but it can be disabled by selecting "★Debug Settings" → "PlayStation Network" → "Universal Data System Rate Limit Notification" → "OFF".

The feature counts calls to `sceNpUniversalDataSystemPostEvent()` and displays a notification when there have been 300 or more calls in the past 5 minutes. The count is reset to 0 when a notification is displayed, and another notification is displayed if there are 300 or more calls again over a subsequent period of 5 consecutive minutes.

## Deleting UDS-Related Data for All Users on the Console

First, terminate any game application that might be running.

Afterward, from "Settings" in the system software, select "★Debug Settings" > "PlayStation Network" > "Universal Data System data" > "Delete data of all users (console)". Alternatively, you can run prospero-ctrl with the arguments shown below:

```
prospero-ctrl application delete-data uds console
```

All unsent events temporarily saved to the internal SSD for all users and all titles, as well as all UDS configuration information and UDS Stats data installed on the internal SSD, will be deleted. This operation does not delete any data on the PlayStation™Network server or other consoles. Therefore, the deleted UDS Stats data will be restored using data on the server the next time the console synchronizes with the server.

## Deleting UDS-Related Data for a Specific User on the Console

First, terminate any game application that might be running.

Afterward, from "Settings" in the system software, select "★Debug Settings" > "PlayStation Network" > "Universal Data System data" > "Delete data of this user (console)". Alternatively, you can run prospero-ctrl with the arguments shown below:

```
prospero-ctrl application delete-data uds console /user:<User>
```

Unsent events temporarily saved to the internal SSD, as well as UDS Stats on the internal SSD, relating to the foreground user for all titles that the user has participated in will be deleted. UDS configuration information installed on the internal SSD will not be deleted by this operation, because this information might be shared among multiple users. Additionally, data on the PlayStation™Network server and data on other consoles will not be deleted. Therefore, the deleted UDS Stats data will be restored using data on the server the next time the console synchronizes with the server.

Note:

Use "Delete data of all users (console)" or "Delete data of this user (console)" if you only want to delete data on the console as in the following cases:

* When you want to delete invalid data or corrupted data during development
* When you want to delete past data because you want to replace configuration information with one that does not maintain compatibility

## Deleting UDS-Related Data for a Specific User on the Console and on the Server

First, terminate any game application that might be running.

Afterward, from "Settings" in the system software, select "★Debug Settings" > "PlayStation Network" > "Universal Data System data" > "Delete data of this user (console and server)". Alternatively, you can run prospero-ctrl with the arguments shown below:

```
prospero-ctrl application delete-data uds all /user:<User>
```

Unsent events temporarily saved to the internal SSD, as well as UDS Stats data on the internal SSD and on the PlayStation™Network server, relating to the foreground user for all titles that the user has participated in will be deleted. UDS configuration information installed on the internal SSD will not be deleted by this operation, because this information might be shared among multiple users. However, because UDS Stats data on the PlayStation™Network server will be deleted, the UDS Stats data for that user on other consoles will also be deleted once the consoles synchronize with the server. Unsent events temporarily saved on other consoles will not be deleted.

Note:

Be aware that, even if UDS-related data is deleted, the data of features that use UDS (e.g., trophy acquisition data generated using UDS Stats) will not be deleted at the same time. You must use the debugger support features that each such feature provides to delete those data.