# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/placement-of-the-trophy-configuration-and-uds-configuration.html

# Overview of Application Development

This topic describes trophy-related processing you need to perform during the application development process.

# Process of Application Development

Process of Application Development

# Application for Service

Apply for trophy system usage on the Developer Network (<https://partners.playstation.net/hub>). If multiple titles will share trophy sets, such as when releasing the titles in multiple territories, also note this when making the request.

For information about applying for services, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) document.

# Configuration of Trophies

Trophies are configured using the UDS Management Tool. Each trophy's metadata (for example, its name and image) and the linked UDS Stat that is referenced by the trophy's unlocking condition should be set in this process. The trophy's unlocking condition can reference a UDS Stat that has been defined in advance; alternatively, a UDS Stat that is specific to the trophy can be automatically generated and referenced. The UDS Management Tool provides several methods for configuring trophies: configuration using the UI, importing configuration information as a json format file, and importing a trophy pack file (trp file) created using the PlayStation®4 SDK. Refer to [Universal Data System Guide - Using the UDS Management Tool - Trophy Tool](../Universal_Data_System-Guide/trophy-tool.html) for details.

In addition, Help information can be set for each individual trophy. Refer to [PlayStation™Network Game Help Guide - Configuring Official Hints - Creating Trophy Hints](../PSN_Game_Help-Guide/creating-trophy-hints.html) for details.

Configured trophy data can be checked via the Preview Trophy UI provided by the S2S Web API and in the system software's Online Mode. For details about the Preview Trophy UI, refer to the "[Preview Trophy UI](preview-trophy-ui.html)" section.

# Obtaining the Package Metadata File

After configuring trophies, download the package metadata file (npconfig.zip) from the Package/Disc Management Tool (GEMS) ("GEMS"). The package metadata file includes trophy configuration files and UDS configuration files generated as the result of configuring trophies.

# Placement of the Trophy Configuration and UDS Configuration Files

Extract the package metadata file downloaded from GEMS directly into the sce\_sys directory of the application binary. After extracting the file, the directory structure should be as follows:

Directory Structure

If you have modified the trophy configuration, re-download the package metadata file from GEMS and replace the old versions of the files. When you do this, existing trophy unlocking data will be retained; however, inconsistencies with the new trophy configuration data may trigger unintended behavior (such as when the rules described in the "[Upgrading the Trophy Set](upgrading-the-trophy-set.html)" section are not followed). If unexpected behavior is observed, refer to the "[Debugging Support Provided by the System Software](debugging-support-provided-by-the-system-software.html "This topic describes the debugging support features provided by the system software that are related to trophies.")" section to delete the trophy-related information on the console.

# Implementation of Trophy-Unlocking

To award a trophy to a user, you must use the NpUniversalDataSystem library to post an event that updates the UDS Stat that is linked to the unlocking condition for the trophy. Refer to the configuration data for each UDS Stat to create appropriate events to post. If the application already posts an event to update the UDS Stat, even if it is for another platform feature, there is no need to post an additional event.

If the trophy uses a dedicated, automatically generated UDS Stat that is based on its definition, you can unlock the trophy or update progress by posting either an "\_UnlockTrophy" event or an "\_UpdateTrophyProgress" event, as shown below.

## Unlocking Non-Progressive Trophies

Non-progressive trophies (those for which a dedicated UDS Stat has been automatically generated) can be unlocked by posting an "\_UnlockTrophy" event in the following format:

* Event name: "\_UnlockTrophy"
* Properties
  + "\_trophy\_id": the trophy ID (Int32)

The following is an example of code for unlocking the trophy with trophy ID 0001:

```
int ret;
SceNpUniversalDataSystemHandle handle;
SceNpUniversalDataSystemContext context;

// handle and context should be set with appropriate values

SceNpUniversalDataSystemEvent *event = NULL;
SceNpUniversalDataSystemEventPropertyObject *prop = NULL;
ret = sceNpUniversalDataSystemCreateEvent("_UnlockTrophy", NULL, &event, &prop);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemEventPropertyObjectSetInt32(prop, "_trophy_id", 1);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemPostEvent(context, handle, event, 0);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemDestroyEvent(event);
if (ret < 0) {
    // Error handling
}
```

## Updating the Progress of and Unlocking Progressive Trophies

The progress toward a progressive trophy (one for which a dedicated UDS Stat has been automatically generated) can be updated by posting an "\_UpdateTrophyProgress" event in the format shown below. The trophy is unlocked when progress toward the trophy reaches the target value.

* Event name: "\_UpdateTrophyProgress"
* Properties
  + "\_trophy\_id": the trophy ID (Int32)
  + "\_trophy\_progress": the value of the progress made (Int32)

The following is an example of code for updating a trophy with trophy ID 0001 to have a progress value of 100:

```
int ret;
SceNpUniversalDataSystemHandle handle;
SceNpUniversalDataSystemContext context;

// handle and context should be set with appropriate values

SceNpUniversalDataSystemEvent *event = NULL;
SceNpUniversalDataSystemEventPropertyObject *prop = NULL;
ret = sceNpUniversalDataSystemCreateEvent("_UpdateTrophyProgress", NULL, &event, &prop);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemEventPropertyObjectSetInt32(prop, "_trophy_id", 1);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemEventPropertyObjectSetInt32(prop, "_trophy_progress", 100);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemPostEvent(context, handle, event, 0);
if (ret < 0) {
    // Error handling
}
ret = sceNpUniversalDataSystemDestroyEvent(event);
if (ret < 0) {
    // Error handling
}
```

## Generating the Source Code to Build and Post UDS Events

A tool is provided that automatically generates the source code for building and posting UDS events based on the UDS configuration data (np-universal-data-system-codegen). If trophies have been defined with Quick Configuration and the related UDS configuration has been automatically generated, np-universal-data-system-codegen generates an .h file and a .c file containing functions like those below when you enter the automatically generated UDS event definitions.

```
// Post an "_UnlockTrophy" event
int
sceNpUniversalDataSystemCodegenPost_UnlockTrophyEvent(
    SceNpUniversalDataSystemContext context,
    SceNpUniversalDataSystemHandle handle,
    int32_t _trophy_id);

// Post an "_UpdateTrophyProgress" event
int
sceNpUniversalDataSystemCodegenPost_UpdateTrophyProgressEvent(
    SceNpUniversalDataSystemContext context,
    SceNpUniversalDataSystemHandle handle,
    int32_t _trophy_id,
    int32_t _trophy_progress);
```

These functions internally perform the building, posting, and destroying of the event; therefore, you will be able to unlock or update the progress of a trophy just by embedding the generated source code in the program and calling a single, simple function.

Refer to [NpUniversalDataSystem Library Overview - NpUniversalDataSystem Code Generation Tool](../NpUniversalDataSystem-Overview/np-universal-data-system-code-generation-tool.html) for details about np-universal-data-system-codegen.

Also refer to the sample (sample\_code/playstation\_network/api\_np\_trophy2) of the NpTrophy2 library, which uses np-universal-data-system-codegen to implement trophy unlocking.

# Master Creation and Submission

Place the trophy configuration and UDS configuration files in the appropriate directories within the master package when creating the package. For the directories in which to place these files, refer to the "[Placement of the Trophy Configuration and UDS Configuration Files](placement-of-the-trophy-configuration-and-uds-configuration.html)" section.

For details about creating master packages, refer to [Content Packaging and Updating Guide - Packages Overview](../Content_Packaging_and_Updating-Guide/packages-overview.html).

## NP Config Tag

Prior to submission, create an NP Config Tag for the trophy and UDS settings configured using the UDS Management Tool. Creating an NP Config Tag restricts subsequent configuration changes, preventing conflicts between server-based configurations and those included in released packages.

Different operations can be performed on trophy configurations based on the state of the NP Config Tag. For details about the operations that can be performed, refer to "[Appendix A: Configuration Changes That Can Be Made Based on the NP Config Tag State](appendix-a-configuration-changes-that-can-be-made-based-on-t.html)". For details about the NP Config Tag and the relationship between the NP Config Tag and the UDS configuration, refer to [Universal Data System Guide - Managing Publications in UDS Management Tool](../Universal_Data_System-Guide/managing-publications-in-uds-management-to.html).

Note:

If multiple applications share a trophy configuration, the restrictions described above are also shared.

## Publication of Trophy Configuration Data

The configured trophy data is uploaded to the trophy server according to the date and time of the application's release (set upon submission). The date and time can be changed after testing by SIE ends if there is still time before the data's actual publication.

If updating an application, the trophy configuration data is uploaded to the trophy server at the same time the update is published.

For details, refer to [Package/Disc Management Tool (GEMS) Overview - Application Management](../Package_Disc_Management_Tool_GEMS-Overview/application-management.html).

# Local Development Workflow

In addition to the procedures described in this chapter, there is also support for the Local Development Workflow. With the Local Development Workflow, you can easily try processing equivalent to that described in "[Configuration of Trophies](configuration-of-trophies.html)", "[Obtaining the Package Metadata File](obtaining-the-package-metadata-file.html)", and "[Placement of the Trophy Configuration and UDS Configuration Files](placement-of-the-trophy-configuration-and-uds-configuration.html)" by using np-universal-data-system-local-tool. For details about the Local Development Workflow, refer to [Universal Data System Guide - Local Development Workflow](../Universal_Data_System-Guide/local-development-workflow.html). Also refer to the sample for Local Mode (sample\_code/playstation\_network/api\_np\_trophy2\_local\_mode), which includes trophy configuration using np-universal-data-system-local-tool. Additionally, refer to the description of trophy debugging features for Local Mode that is provided in the chapter "[Debugging Support Provided by the System Software](debugging-support-provided-by-the-system-software.html "This topic describes the debugging support features provided by the system software that are related to trophies.")".