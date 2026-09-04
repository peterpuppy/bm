# PlayStation™Network Game Help Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Help-Guide/bulk-configuration-of-hints.html

# Configuring Bulk Hints

This chapter provides information on configuring hints in bulk.

Note: A new JSON bulk configuration schema (v2.0) is available as of October 27, 2021. The new schema allows you to configure trophy hints in addition to activity hints. The v1.0 JSON bulk configuration schema is deprecated and is no longer supported for Game Help Tool bulk configuration.

For some games, it may be necessary to manage a large number of Game Help-related entities, such as official hints, and their media files (images and videos). It can be time consuming to manage large numbers of official hints and media manually using a web-based interface. Game Help supports two methods for bulk configuration of data, providing solutions to different workflows:

1. The Game Help Tool allows you to provide an entity definition file that contains metadata for multiple official hints in JSON format.

   * This method is best suited to creating the initial definitions of official hints, and to finalizing hints by providing localization support. When the entity definition file specifies entities that do not already exist, Game Help creates new entities that can then be accessed in the Game Help Tool. When the entity definition file specifies entities that already exist, their metadata is updated. The official hint metadata in the entity definition file can reference media files that have already been uploaded and processed using the Game Help Tool or uploaded through the media gallery on the console. You can review the result of creating or updating entities in the Game Help Tool after the process completes.
2. User Bucket for Partners (UBP) by supports SFTP-based bulk upload of assets and metadata to an Amazon S3 bucket. It supports the following workflows:

   * Create and submit a tar package that contains both entity metadata in an entity definition file and the associated media files. This workflow works well when both the entity definitions and associated media files are available together. If the entity definition file specifies entities that do not already exist, Game Help creates new entities that can then be accessed in the Game Help Tool. If the entity definition file specifies entities that already exist, their metadata is updated. Media files are linked to the new or edited entities and are also available to view in the Game Help Tool.
   * Create and submit a tar package that contains media files for entities that already exist. This workflow supports the bulk upload of media files for target entities that already exist in the Game Help Tool. The entity definition file specifies links between the media files in the package and pre-existing target entities. If the target entity is already associated with media files, the newly uploaded media files replace the existing ones.
   * Create and submit a tar package that contains media files for entities that will be created later. This workflow supports the bulk upload of media files for target entities that have not been created yet. In this case, the entity definition file only needs to contain metadata for a single hint, which can be placeholder. The tar package must still contain an entity definition file however, because it specifies the NP Communication ID of the game that is associated with the media files. UBP stages the uploaded media assets, which will be available to view in the Game Help Tool.

     Note:

     Unlike other UDS entities, UBP **does** support metadata-only uploads. See [Universal Data System Guide - Using the UDS Management Tool - Bulk Configuring UDS Entities](../Universal_Data_System-Guide/bulk-configuring-uds-entities.html) for more information on using UBP for other entities.

SIE recommends exporting the latest help data from the Game Help Tool, modifying the resultant JSON file, and uploading the modified JSON when bulk configuring hints. Uploading partial JSON files may result in unexpected changes. Additionally:

* Include all localization rows when using bulk configuration to update specific localizations. Omitted localizations are deleted upon import.
* Include all active hints for an activity ID when using bulk configuration to update a specific hint. Any active hints missing from the imported JSON file are deleted upon import.

## Notifications from Game Help Bulk Configuration

**Notifications from Bulk Configuration via the Game Help Tool**

Game Help sends one email notification for each submitted metadata.json file.

When metadata is submitted and schema validation succeeds, the file is processed and entities are created. At the end of the process, Game Help sends an email containing a report of the hints created or updated, along with any errors that have occurred. At this point, re-submission is required in order to address any errors found during the import process.

**Notifications from Bulk Configuration via UBP**

Game Help sends two email notifications for each submitted tar file.

When a valid tar file is uploaded, Game Help sends an email scheduling the bulk configuration job. If the tar file is not valid, it sends an email that rejects the job and reports validation feedback to the users.

For valid files, a second email is sent after the bulk configuration is processed. This email contains a report of the hints created or updated, and any errors that have occurred during media file transcoding or hint generation.

# Configuring Entity Definition Files

This topic covers the processes of defining entity definition files.

## Configuring an Entity Definition File in the Game Help Tool

The Actions dropdown in the Activity Hints and Trophy Hints views provides options for working with entity definition files.

The Actions Dropdown

**Downloading the Game Help Entity Definition Schema**

You can use the Actions dropdown to download the Game Help entity definition schema. Select Download Schema (.json) to download a JSON file that specifies the Game Help entity schema. The schema is also described in [Schema for Bulk Configuration of Hints](appendix-b2-schema-for-bulk-configuration.html "This topic provides the JSON schema used for the bulk configuration of hints.").

**Exporting the Hint Configuration**

You can use the Actions dropdown to export your official hint configuration as an entity definition file. Select Export Hints (.json) to download a JSON file that conforms to the Game Help entity schema. This allows you to view your current official hint configuration and provides a starting point for editing your entity definition file.

**Importing an Entity Definition File via the Game Help Tool**

When you are ready to import a new or edited entity definition file, choose the Import Hints (.json) option from the Actions menu, then follow the steps listed below.

1. Select the entity definition file either by browsing to it on your computer or by drag and drop onto the user interface. The file upload begins automatically.

   Import an Entity Definition File
2. When the entity definition file has uploaded successfully, Game Help immediately performs a schema validation on it.

   1. If the file passes schema validation, press the Import button to begin creating and editing entities in the backend.

      Successful Entity Definition File Validation
   2. If any errors occur during validation, the Game Help Tool displays them. At this point, you must address the issues and submit a new entity file to restart the import process.

      Validation Errors in Entity Definition File

      When the import process completes, Game Help sends an email to the initiating user that contains the import job's status report. The status report includes a list of all the successfully created entities and any errors that occurred during the process.

## Creating Entity Definition Files for Hints

Entity definition files contain metadata in JSON format.

This process supports both full and partial entity definitions for Game Help. This means an entity definition file can contain official hints to be created, pre-existing hints to be updated, or a combination of both.

The following example shows the JSON structure for the metadata defined in the entity definition file:

```
   { 
                    "schemaVersion" : "2.0",
                    "contextType":"NPCommunicationId",
                    "contextId":"NPWR00000_00",
                    "entities":{ 
                    "<Entity Type>":[ 
                    { 
                    <Entity Full JSON>
                    },        
                    { 
                    <Entity Full JSON>
                    }
                    ]
                    }
```

Table Entity Definition Metadata Attributes

| Attribute | Required/Optional | Description |
| --- | --- | --- |
| `schemaVersion` | Required | Version number of the entity definition schema. Current version is "2.0" |
| `contextType` | Required | The type of the context. Only the following value is currently supported:   * `NPCommunicationId` |
| `contextId` | Required | ID of the context for which entities are defined. For this release, specify the target NP Communication ID. |
| `<Entity Type>` | Required | The type of content. Only the following values are currently supported:   * `activityHints` * `trophyHints` |
| `<Entity Full JSON>` | Required | Array of full JSON definition of the entity being created or updated. Current version supports `activityHints` and `trophyHints` object types. See [Reference Materials](psn-object-references.html "This chapter contains topics with additional information that you may find useful when configuring Game Help content, such as PlayStation™Network object references and definitions.") for object definitions. |

The following example shows an entity definition file with full official activity hint and trophy hint definitions:

```
{
                    "schemaVersion": "2.0",
                    "contextType": "NPCommunicationId",
                    "contextId": "NPWR00000_00",
                    "entities": {
                    "activityHints": [
                    {
                    "objectId": "tutorialStep1-shooting",
                    "name": {
                    "en-US": "How to Shoot",
                    "ja-JP": "撮影方法"
                    },
                    "description": {
                    "en-US": "Hold the trigger to shoot. The longer you hold, the farther the arrow will travel.",
                    "ja-JP": "トリガーを押して発射します。 長く押すほど、矢印は遠くまで移動します。"
                    },
                    "activeStatus": {
                    "active": true,
                    "order": 1
                    },
                    "links": {
                    "associatedObject": {
                    "objectId": "tutorialStep1"
                    },
                    "associatedMedia": {
                    "en-US": {
                    "fileName": "shooting-tutorial_en.mp4",
                    "segmentTimecode": {
                    "start": "00:05:00",
                    "end": "00:10:00"
                    }
                    },
                    "ja-JP": {
                    "fileName": "shooting-tutorial_jp.mp4"
                    }
                    }
                    }
                    }
                    ],
                    "trophyHints": [
                    {
                    "objectId": "tutorialStep2-shooting",
                    "name": {
                    "en-US": "How to Shoot (2)",
                    "ja-JP": "撮影方法 (2)"
                    },
                    "description": {
                    "en-US": "Hold the trigger to shoot. The longer you hold, the farther the arrow will travel.",
                    "ja-JP": "トリガーを押して発射します。 長く押すほど、矢印は遠くまで移動します。"
                    },
                    "activeStatus": {
                    "active": true,
                    "order": 1
                    },
                    "links": {
                    "associatedObject": {
                    "objectId": "tutorialStep2"
                    },
                    "associatedMedia": {
                    "en-US": {
                    "fileName": "shooting-tutorial2_en.mp4",
                    "segmentTimecode": {
                    "start": "00:05:00",
                    "end": "00:10:00"
                    }
                    },
                    "ja-JP": {
                    "fileName": "shooting-tutorial2_jp.mp4"
                    }
                    }
                    }
                    }
                    ]
                    }
                    }
```

**Referencing Leaf Activities and Trophies**

Official hints are linked to leaf activities or trophies. Each activity or trophy object has its own `objectId` that is used to refer to it. See [Universal Data System Guide - Reference - PlayStation™Network Object Reference](../Universal_Data_System-Guide/psn-object-reference.html) for more information on activities.

**Referencing Media Files**

Game Help only supports references to processed media files or, in the case of UBP, references to new media files that are included in the same tar file as the `metadata.json` file. Your hint entity can reference a successfully processed file via the link property. Files are identified by filename. The combination of filenames and NP Communication ID must be unique.

Multiple official hints can reference a single video file. Entity definition files also support the `segmentTimecode` property, which allows each hint to use a different clip from a single video. The ability to set and edit `segmentTimecode` values is not currently supported in the Game Help Tool, but will be made available at a later time.

**objectId**

To align to PlayStation™Network Object data model standards, each hint object supports a unique, developer-defined `objectId`. The `objectId` must be unique within the context (in this case, the context is the NP Communication ID). Game Help uses the `objectId` specified in the entity definition file to determine whether the specified object already exists. If the file specifies an incorrect `objectId`, an unintended object could be created or an unexpected object could be updated. Ensure that the entity definition metadata contains the correct `objectId`s.

Note:

The Game Help Tool web interface does not currently support the creation of unique, developer-defined `objectId`s for trophy hints. Support for defining unique `objectId`s for trophy hints will be added in a future tool update. Unique `objectId`s can be defined for trophy hints when creating hints through bulk configuration.

**Creating Entity Definition Files for Media-Only tar Packages**

You can use UBP to upload a tar package that contains media files for hints that have not been created yet (see [Configuring Bulk Hints](bulk-configuration-of-hints.html "This chapter provides information on configuring hints in bulk.")). In this case, the tar package must still include an entity definition file that specifies the NP Communication ID of the associated game. The Game Help Tool uses the NP Communication ID to associate the files with the correct game and to check that the user who uploads the file has permission to modify the help assets for that game.

Note:

The entity definition file must include at least one hint definition. A placeholder hint definition is acceptable, as long as all required fields are provided.

# Configuring a tar Package for Upload using User Bucket for Partners (UBP)

This topic provides details on how to configure a .tar package to upload using UBP.

UBP requires all related files to be packaged into a tar file (.tar or .tar.gz). A package (tar file) must contain a `metadata.json` file and may contain any associated media files. The `metadata.json` file describes the properties of the included entities along with the references to packaged media files. The structure of the `metadata.json` file is entity and use case dependent. Note that the filename is case sensitive (the filename `metadata.json` contains only lower-case letters). The filename of the tar file must not contain any spaces.

Media Package

Note:

Media asset files should all be flat siblings of the `metadata.json` file and the tar file should not contain any folder structure. Media files must also follow the same specifications as media files uploaded via the tool.

## Obtaining the SSH Private Key for SFTP

The UBP used for Game Help is shared with UDS and the Package/Disc Management Tools (GEMS). Access GEMS for the list of SFTP endpoints, and your username for connecting to the endpoint. GEMS is also used to manage your private SSH key for connecting to the SFTP endpoint. Refer to [Package/Disc Management Tool (GEMS) Overview - Access and Basic Operation - Admin Menu](../Package_Disc_Management_Tool_GEMS-Overview/admin-menu.html) for more information.

## Uploading Your tar Package Through SFTP

Use the SFTP endpoint information obtained from GEMS to upload the tar files to the **hints** subfolder under your home directory. Game Help is processed only via this subfolder. Uploading a Game Help tar file to another subfolder causes a process failure.

# Frequently Asked Questions about Bulk Configuration

This topic provides answers to commonly asked questions you may encounter when configuring hints in bulk.

## How does Game Help handle partial failures?

In both the Game Help Tool and UBP workflows, Game Help processes as many objects as possible. If there are problems with an included entity (for example invalid metadata, or media files that do not meet the specifications), Game Help logs the error and processes the rest of the entities. When processing completes, the email notification includes the error information.

## What should I do if my file has a partial failure and I want to re-submit?

The bulk upload process is re-entrant. Simply update the erroneous records or files and re-submit the file. You do not need to upload the whole file of complete object definitions for Game Help, though we recommend always uploading the whole file of complete object definitions to avoid unanticipated changes (see [Configuring Bulk Hints](bulk-configuration-of-hints.html "This chapter provides information on configuring hints in bulk.")). Instead, you can submit a partial delta file that contains only the required updates or additions.

## What happens if the entity definition file does not contain all the existing entities?

Note:

We strongly recommend always exporting the latest help data from the Game Help Tool, modifying the resultant JSON file, and uploading the modified JSON when bulk configuring hints. Uploading piecemeal or partial JSON files may result in unanticipated changes.

* Include **all** localization rows when using bulk configuration to update specific localizations. Omitted localizations will be **deleted** upon import.
* Include **all** active hints for an activity ID when using bulk configuration to update a specific hint. Any active hints missing from the imported JSON file will be **deactivated** upon import.

## How does Game Help update existing entities?

Game Help entity updates by merge replacement. Properties that are already defined in the Game Help Tool, but are not mentioned in the imported entity definition file, should not be updated. This allows for partial or delta updates, as updates can occur without explicit deletion.

However, please note the exceptions above regarding updating specific localizations or modifying an active hint.

## Can I reference the same media file from multiple entities?

Multiple entities in the entity definition file can reference the same media files. Media files are referenced by filename, so you can specify the same filename in multiple official hint definitions.

## Are there any limitations on the package (tar file) size?

UBP restricts neither the number of entities defined in a metadata.json file nor the package (tar) file size. However, Game Help may reject media files that do not satisfy the required specifications in [Uploading Media Assets](uploading-media.html "This topic provides information on the types of media assets you can upload to use for custom Game Help content."), even if the upload succeeds.

## How long will JSON imports take in the Game Help Tool?

It is not possible to guarantee a specific time, but bulk configuration via the Game Help Tool (entity definition file only) is relatively fast.

## How long will UBP uploads take for my tar file?

The UBP interface uses SFTP, so this depends on your internet speed and the size of the package (tar) file being uploaded.

## How long will it take for UBP to process my package?

It is not possible to guarantee a specific time, but bulk configuration via UBP is proportional to the size of the media files being uploaded. Media files are processed in our backend, transcoded and optimized for streaming to players, which is not an instant process.