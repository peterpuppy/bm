# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/managing-publications-in-uds-management-to.html

# Managing Publications in UDS Management Tool

This chapter describes NP Config Tag management, running an integrity check dry run,
and viewing the publishing history.

For additional details on the publication of UDS
entities, refer to the [UDS Data Model](uds-data-model.html "UDS standardizes data required by each platform feature and defines it in the UDS data model. By doing so, it prevents the duplication of data received from a game application and realizes single input multi-use. A UDS data model is composed of a PlayStation™Network object and a UDS event (feature event).").

# User Permissions and Limitations

If you are a "Viewer" title collaborator, you can view existing NP Config Tag definitions. In order to create, edit, or delete NP Config Tags, you must have either "Editor" or "Owner" title collaborator roles.

# Editing NP Config Tag

This topic explains how to edit NP Config tags.

Specify the NP Config Tag to edit by selecting the **more options** icon for the NP Config Tag from the list page. Then select the **Edit NP Config Tag Attributes** option. This option displays the NP Config Tag edit view for the selected tag. Only
Tag Name and Notes can be edited.

# Creating NP Config Tag

This topic explains how to create NP Config tags.

You can create a new NP Config Tag by selecting the **Create NP Config Tag** button from the NP Config Tag list view page. NP Config Tag creation page is displayed
as shown in the following figure. Specify Tag ID, Tag Name, and optional Notes for
the tag.

Creating a New NP Config Tag

## Creating a PlayStation®4 NP Config Tag

For Match use cases, PlayStation®4 games can use activity objects defined in the UDS
Management Tool. A PlayStation®4 NP Config Tag is only applicable when the PlayStation®4
version of a game is released without a PlayStation®5 counterpart. To create a PlayStation®4
NP Config Tag, select the **PS4** option under **Platform** in the NP Config Tag Creation page. Once selected, the **Entities** section of the creation page updates to display the activities applicable to the
PlayStation®4 NP Config Tag, as shown in the following figure. Only "Competitive" activities with the **Is Online Multiplayer** property set to "true" are added to the PlayStation®4 NP Config Tag. Review the list and select the **Create** button. Since NP Config Tag creation may take time, email notification is sent when
the creation process completes.

List of Included PlayStation®4 Entities

## Creating a PlayStation®5 NP Config Tag

To create a PlayStation®5 NP Config Tag, select the **PS5 & PS4** option under **Platform** on the NP Config Tag Creation page. Once selected, the **Entities** section of the creation page updates to display the number of entities included in
this tag as shown in the following figure. A PlayStation®5 NP Config Tag includes
all currently defined entities. As the number of included entities are large, the
UI only shows the summary number of the included entities. Review the list and select
the **Create** button. Since NP Config Tag creation may take time, email notification is sent when
the creation process completes.

List of Included PlayStation®5 Entities

Note:

Once a NP Config Tag is created for a NP Communication ID, any new NP Config Tag must
include all the entities included in all previous NP Config Tags. This implies that
once a PlayStation®5 NP Config Tag is created, the PlayStation®4 NP Config Tag can
no longer be created (the PlayStation®4 NP Config Tag can only include a subset of
activity objects) until all existing PlayStation®5 NP Config Tags are deleted.

# Deleting NP Config Tag

This topic explains how to delete an NP Config tag.

Specify the NP Config Tag to edit by selecting the **more options** icon for the NP Config Tag from the list page. Then select the **Delete** option. Only the NP Config Tags in "Tagged" status can be deleted.

# NP Config Tag List View

This topic covers how to view a list of NP Config tags for a given NP Communication ID.

To view the list of NP Config Tags for a given NP Communication ID click the **Publishing** tab and click on **NP Config Tags**. The list of NP Config Tags appears as shown in the following figure. The list displays
the following information

* **Tag ID:** Developer defined identifier of the NP Config Tag.
* **Tag Name:** Developer defined name of the NP Config Tag.
* **Note:** Developer added notes of the NP Config Tag.
* **Platform:** Platform supported by the NP Config Tag. Can either be "PS4" or "PS5 & PS4".
* **Requires Pkg Update:** Whether or not publishing the NP Config Tag requires re-creating the game package.
* **Created Date:** NP Config Tag creation date.
* **Last Updated Date:** NP Config Tag last updated date.
* **Publish Status:** Publication Status of the NP Config Tag. Valid values are: "In Production", "Format QA Completed", "In Format QA", and "Tagged".
* **Lock Status:** Lock status of the NP Config Tag. Once a tag is created, the status is locked until
  the tag is in production. "Partially Unlocked" status implies that limited fields in the entities included in the tags can be edited
  and is applicable when the Publish Status is "In Production".

  Note:

  You can designate a game submission as either "Full Submission" or "Pre-submission". NP Config Tags associated with "Pre-submission" submissions are marked for clarify. Unlike "Full submission" NP Config Tags, "Pre-submission" NP Config Tags can be deleted while in "In Format QA" status. This feature is useful when UDS related development must continue and entities
  must be unlocked during the pre-submission process.

  List of NP Config Tags

# Running Integrity Checks

This topic describes the procedure for running integrity checks. To successfully create NP Config Tags and publish defined UDS entities, it is important
to ensure that both referential integrity check and compatibility integrity checks
are performed.

These checks are run at various points of publishing processes:

* When a new NP Config Tag is created.
* When a `npconfig.zip` file is downloaded from Package/Disc Management Tool (GEMS).
* When a game package is imported for Platform Certification and Operations submission.

Referential integrity checks ensure that all referenced entities actually exist. For
example, if a stats extraction rule references an UDS event and one or more if its
properties, the integrity check ensures that the event and its properties are actually
defined. Compatibility check ensures that all entities included in the previous NP
Config Tag is included in the newer NP Config Tags.

You can check to see if your UDS entities are ready for publishing by performing the
Integrity/Compatibility check dry runs. To perform a dry run, click the **Publishing** tab and select the **Integrity Check** menu option. The entity selection page is displayed as shown in the following figure.
You can select one or more types of UDS entities against which the integrity/compatibility
checks are run. Select one or more entities and click on **Execute Process** to run the tests.

Integrity Check Entity Selection Page

These checks can take some time depending on the number of entities defined in a currently
selected NP Communication ID. Once the tests start executing, progress screens appear
as shown in the following figure.

Integrity Check Progress

If all the checks pass, the integrity check success screen appears, shown in the following
figure. If you want to re-execute the check again, select the **Re-Execute Process** button.

Integrity Check Success

If there are errors or warnings, the integrity check error screen appears. Because
the number of errors or warnings can be large, actual errors are not displayed in
the UI. Instead, a JSON file with all the errors, warnings, and suggested actions
are downloaded automatically as shown in the following figure. If you want to re-execute
the check again, select the **Re-Execute Process** button. Warnings indicates problems with a current configuration that may require
a TRC waiver.

Integrity Check Errors and Warnings

# Selecting Entity Types and NP Configuration Tag to Compare

This topic provides an overview of how to compare entity types and NP Configuration tags.

To specify the entity types and NP Configuration Tag to compare, click the **Publishing** tab and click on **Diff Check**.

On the displayed page, select the NP Config Tag (or the latest data), target entity
types, and target environment and click **Execute Process**.

Select Target To Compare

Once the UDS Management Tool completes the comparison, the tool displays the number
of changed entities of each selected type and required actions to reflect the changes
in the production environment. The potential required actions are

* **Pkg Update Required**: New game package must be created and submitted through GEMS.
* **Republish Required**: Republish the NP Communication ID through UDS Management Tool.
* **No Update Required**: Production environment is up to date and no action is required.

# Running Integrity Check Against NP Config Tag

This topic provides guidance on running integrity checks for specific NP Config tags.

Specify the target NP Config Tag for integrity check by selecting the more options
icon for the NP Config Tag from the list page. Then select the **Run Integrity Check** option. Integrity check is not available for PS4 NP Config Tags. If there are existing
published tags in the NP Communication ID, integrity check is available for the latest
published NP Config Tag and for any NP Config Tags created subsequently. If none of
the NP Config Tags are published in the NP Communication ID, integrity check is available
for all NP Config Tags.

# Publishing NP Config Tags

This topic provides information on publishing NP Config tags. You can publish a PlayStation®4 NP Config Tag or republish a PlayStation®5 NP Config Tag in "In Production" status using the UDS Management Tool.

All other publication scenarios are performed through the Package/Disc Management Tool
(GEMS). Refer to the [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) for details.

## Publishing a PlayStation®4 NP Config Tag

Specify the PlayStation®4 NP Config Tag to publish by selecting the **more options** icon for the NP Config Tag from the list page. Then select the **Publish** option. This option only appears for the PlayStation®4 NP Config Tags.

## Republishing NP Config Tags

If one or more objects' metadata is updated after a game is released (published to
the production environment), the metadata change can be republished to production
from the UDS Management Tool without re-creating the game package.

Specify the NP Config Tag to publish by selecting the **more options** icon for the NP Config Tag from the list page. Then select the **Publish** option. This option only appears for the latest NP Config Tag in "In Production" status.