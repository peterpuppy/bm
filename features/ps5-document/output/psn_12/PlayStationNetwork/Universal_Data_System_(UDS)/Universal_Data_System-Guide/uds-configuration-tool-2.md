# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/uds-configuration-tool-2.html

# FAQ

This chapter contains frequently asked questions you may encounter when using UDS.

# UDS Configuration Tool

This topic contains frequently asked questions you may encounter when configuring UDS or using the UDS Management Tool.

## Q. How Do I Access the UDS Management Tool?

For details on how to access UDS Management Tool as well as grant additional access to
other members in your organization, see [Accessing the Tool](accessing-the-tool.html "This topic explains how to access the UDS Management Tool.").

## Q. How Do I Set Up Time Limited Activities?

You can use the `availableFrom` and `availableUntil` fields when creating your activities if you'd like to schedule your activities or only make them visible within a certain time limit. For more information, see [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html).

As these fields only allow you to set one time, it is good practice to have the activity go live around the world at the same time.

If you are wanting to change the values of the `availableFrom` and `availableUntil` fields for an activity in the production environment, then this can be done outside of a patch. You do not have to create a new NP Config Tag to make these changes to an activity. You are simply able to republish the NP Config Tag from within the UDS Management Tool after you have made the necessary changes to these fields. For details on how to republish NP Config Tags, see [Publishing NP Config Tags](publishing-np-config-tags.html "This topic provides information on publishing NP Config tags. You can publish a PlayStation®4 NP Config Tag or republish a PlayStation®5 NP Config Tag in \"In Production\" status using the UDS Management Tool.").

Although you cannot delete activities once they have been deployed to the production environment (once an activity is partially locked), you can hide these activities from the user by making them unavailable using the `availableFrom` and `availableUntil` fields.

## Q. How Do I Update Availability Date Of Activity Cards After Passing Certification?

Often with time limited activities, you must adjust the `availableFrom`
value during application or patch submission that introduces these activities, so that
the activity is visible to CertOps during the testing period. Once CertOps has finished
testing and approved the application or patch, you must edit the
`availableFrom` value of the time-limited activity to its original
time and date before pushing the configuration to the production environment again.

Both `availableFrom` and `availableUntil` can now be
edited when the status of Np Config Tag is in "In Format QA" or "In Production". If the
Np Config Tag is already in "In Production", you must republish it after the edit. For
details on how to republish NP Config Tags, see [Publishing NP Config
Tags](publishing-np-config-tags.html "This topic provides information on publishing NP Config tags. You can publish a PlayStation®4 NP Config Tag or republish a PlayStation®5 NP Config Tag in \"In Production\" status using the UDS Management Tool.").

For more details on what can be edited, see [PlayStation™Network Object
Reference](psn-object-reference.html "This topic contains PlayStation™Network object names and attribute descriptions.").

## Q. How Do I Delete Activities from a Live Environment?

You cannot delete activities once they have been deployed to the production/live environment (once an activity is partially unlocked). You can hide these activities from the user by making them unavailable using the `availableFrom` and `availableUntil` fields.

## Q. How Do I Unlock Activities In the UDS Management Tool?

The different statuses of the NP Config Tag are shown in the "Tagged", "In Format QA",
"Format QA Completed" and "In Production" sections of [The Status of the NP
Config Tag](the-status-of-the-np-config-tag.html "This topic shows the different statuses the NP Config tag can be in.").

Depending on the status of your PlayStation™Network objects (such as your activities),
you can perform different actions on your UDS configuration. [Action Depending on Status](configuring-the-uds-data-model.html#topic315301_5_7__action-depending-on-status_html) shows the different actions you can take depending
on the status of the object/entity.

If the NP Config Tag is in "Tagged" status, it is possible to fully unlock the
configuration by deleting the Np Config Tag, to delete, see [Deleting NP Config Tag](deleting-np-config-tag.html "This topic explains how to delete an NP Config tag.").

## Q. How Do I Add Additional Supported Languages In UDS Management Tool For Activities/Trophies After Passing Certification?

It is possible to add additional supported languages once the Np Config Tag is in the
"In Production" status, however this change requires a new Np Config Tag to be created
and a patch package to be deployed for the new supported languages to be reflected in
live environment. For more information on what configuration change is possible after
the release, as well as whether a patch is required or not, see [Configuration
Change After the Release](configuration-change-after-the-release.html "The UDS configuration (including trophy configuration) can be changed after a game release. Depending on the configuration change, the required action is different.").

To add additional supported languages, in the UDS Management Tool, navigate to [Define
Data] `->` [Metadata] `->` [Update Languages]. For
more details on this configuration, see [Configuring Metadata](configuring-metadata.html "This chapter describes configuring various types of metadata.").

Once additional supported languages are added, and UDS objects' localization has been
updated using new additional supported languages, follow the steps described in [Preparing a Package for
Release](preparing-a-package-for-release.html "This topic covers the procedure for preparing a release package.") to generate Np Config Tag to be included in the patch.

## Q. How Do I Remove Additional Supported Languages From PlayStation™Network Objects and Trophies?

Removing supported languages from NP Communication ID metadata does not automatically
remove localized data defined in PlayStation™Network objects or trophies. In order to
remove the localized data from PlayStation™Network objects and trophies, you must use
the JSON import function in the UDS management tool.

When removing localization data from PlayStation™Network objects:

1. Export PlayStation™Network objects in JSON format from the UDS management tool.
2. Remove the desired localization data from the JSON file.
3. Re-import the objects using the UDS management tool.

When removing localization data from trophies:

1. Remove localization data from Trophies and TrophyGroups, then import the JSON. Do
   not remove the language from TrophySet at this time.
2. Remove localization data from TrophySet, then import the JSON.

If all localization languages are removed from JSON files and imported at once,
localization data is not removed from TrophySet. This can result in failures when
updating trophy data or integrity check errors. To fix this:

1. Add the removed localization data back to TrophySet in the JSON file and import the
   data.
2. Repeat steps 1 and 2 for removing localization data from trophies.

## Q. Can I Make Changes to UDS Configuration While My Game Is In Submission?

This depends on the type of submission your title is going through:

* For Pre-Master or TRC Sweep type of submission, it is possible to make changes while
  the Np Config Tag is in "In Format QA (Pre-Submission)" status, by first deleting the
  associated NP Config Tag in the UDS Management Tool. This then unlocks the associated
  PlayStation™Network objects, allowing you to make edits. The intention here is for
  your development team to keep iterating towards the final submission, while the other
  game build is going through Pre-master or TRC Sweep submission.
* For final submission where Np Config Tag is in "In Format QA (Master Submission)",
  it is not possible to make any changes.

## Q. How Do I Publish UDS Config To a Certification Environment?

Publishing of Np Config Tag to Prod-QA is performed automatically as part of a package
submission process. An example of the process is:

* In the UDS management tool, perform the integrity check.
* Create an updated Np Config Tag.
* In the GEMS tool, download the `npconfig.zip` file that is associated
  with the Np Config Tag created in the UDS management tool.
* Include the downloaded configuration file (`npconfig.zip`) in your
  application and package up your application.
* Upload the application package to GEMS.
* Once the package is in test, Np Config Tag is published to Prod-QA for you.

For more details of how to prepare an app for submission, see [Preparing a Package for
Release](preparing-a-package-for-release.html "This topic covers the procedure for preparing a release package.").

## Q. How Do I Publish UDS Config To a Live Environment?

Similar to above, publishing of the Np Config Tag to the live environment is also done automatically once the application has passed Certification and the application is published to live environment via the GEMS tool. Np Config Tag should have "Format QA Completed" once the application has been approved; in this status, Np Config Tag is ready to be published. In GEMS once the application is scheduled to be published to the environment, the process of publishing Np Config Tag also kicks in. If successful, Np Config Tag has "In Production" as its status. This also applies to Np Config Tag included in a patch as well. For these cases, you do not have to worry about publishing Np Config Tag separately.

Another option is being able to republish Np Config Tag, while the Np Config Tag is
already in "In Production" status. This situation only applies if the UDS configuration
change does not require a new Np Config Tag and a patch package. To learn what kind of
UDS configuration change requires or does not require a new Np Config Tag and package,
see [Configuration Change After the Release](configuration-change-after-the-release.html "The UDS configuration (including trophy configuration) can be changed after a game release. Depending on the configuration change, the required action is different.").

To republish Np Config Tag to the live environment, see [Publishing NP Config
Tags](publishing-np-config-tags.html "This topic provides information on publishing NP Config tags. You can publish a PlayStation®4 NP Config Tag or republish a PlayStation®5 NP Config Tag in \"In Production\" status using the UDS Management Tool.").

## Q. How Do I Delete All UDS-Related Data?

[Deleting UDS-Related Data](https://p.siedev.net/resources/documents/SDK/latest/NpUniversalDataSystem-Overview/0002.html) functionality can
delete unsent events temporarily saved to the internal SSD, as well as UDS Stats data on
the internal SSD and on the servers of PlayStation™Network. However, this does not
delete data for Trophies, Challenges and History of Completed Activities. To delete that
data, you must use the debugger support features that each such feature provides to
delete the data. To delete Trophy data, see [Trophy System Overview - Debugging Support
Provided by the System Software](../Trophy_System-Overview/debugging-support-provided-by-the-system-software.html).

There is currently no way to delete Challenge data for individual accounts. To delete the Challenge leaderboard see [PlayStation™Network Challenge Activities Guide - Managing Leaderboards](../PSN_Challenge_Activities-Guide/leaderboard-management.html).

There is currently no way to delete data for History of Completed Activities.

## Q. Can npconfig.zip Be Downloaded Programmatically?

If you are interested in downloading `npconfig.zip` programmatically as
part of an automated packaging/submission pipeline, the `npconfig.zip`
can be downloaded programmatically by using the Package/Disc Management Web API.

For more information on this API including its usage, see the [Package/Disc Management Web API Overview](https://p.siedev.net/resources/documents/SDK/latest/Package_Disc_Management_WebAPI-Overview/0001.html).

# UBP

This topic contains frequently asked questions you may encounter when using UBP.

## Q. How does the image auto-mapping works in UDS Management Tool and UBP?

Each media asset uploaded through the UDS media API, UDS Management Tool, or UBP will
have a unique asset ID. The asset ID can be either user-specified or auto-generated.
When the assets are uploaded, corresponding CDN URLs are assigned for the asset .
 A developer can use this URL in a particular UDS object's metadata.

Once the user associates the URL with a UDS object, the UDS management tool creates
a mapping between the URL, the UDS object, and the respective field to which the user
has applied the media asset (e.g., activity rewards images, 512x512). The UDS Management
Tool can later use this mapping to auto-associate URLs with UDS Objects when appropriate.
For example, if the partner performs a bulk import from the UDS tool without specifying
images in the object metadata.

## Q. How Do I Preserve the Already Associated Images in UBP Import Without Retrieving the URL from the UDS Management Tool?

When image assets are associated with various properties of UDS entities, the UDS
management tool generates image URLs. When submitting the metadata update through
UBP, it is cumbersome to set image URL properties to the URLs generated in the previous
UBP update (or any other way of image association to UDS entities). You can pass the
blank URL link in the property to signal UBP to automatically re-associate the currently
assigned images without re-uploading images or specifying the generated URL. Refer
to the sample below.

```
"zones": [{
                 "objectId": "silly_ubp",
                 "metadata": {
                     "name": {
                         "en-US": "UBP Update"
                     },
                     "hidden": false,
                     "images": [{
                             "type": "864x1040",
                             "url": ""
                         }
                     ]
                 }
             }
         ],
```

## Q. How Do I Avoid Duplicating the Stats Extraction Rules When Importing Stats Information through UBP?

UDS Management Tool uses the stats extraction `ruleId` property as a unique identifier for the stats extraction rules. If stats extraction
`ruleId` is not included in the `metadata.json`, the extraction rules are considered new and results in a new rule added to the target
stats definition. To avoid this, specify the stats extraction `ruleId` for the corresponding existing stats extraction in the `metadata.json`.

The following results in an addition of new stats extraction rule because `ruleId` is not specified.

```
{
     "schemaVersion": "6.0",
     "contextType": "NPCommunicationId",
     "contextId": "XXXXXXXX_XX",
     "entities": {
         "statDefinitions": [
             {
                 "statName": "SampleStat",
                 "origin": "console",
                 "definitionGroup": "custom",
                 "dataType": "int32",
                 "aggregation": "latest",
                 "maxValue": "10000",
                 "minValue": "0",
                 "initialValue": "0"
             }
         ],
         "statExtractions": [
             {
                 "definitionGroup": "custom",
                 "condition": {
                     "eventName": "SampleActivityEnd",
                     "property": {
                         "path": "$.score",
                         "comparator": ">",
                         "value": "1"
                     }
                 },
                 "action": {
                     "input": "$.score",
                     "output": {
                         "statName": "SampleStat"
                     }
                 }
             }
         ]
     }
}
```

The following results in updating existing stats extraction rule because `ruleId` is specified

```
{
     "schemaVersion": "6.0",
     "contextType": "NPCommunicationId",
     "contextId": "XXXXXXXX_XX",
     "entities": {
         "statDefinitions": [
             {
                 "statName": "SampleStat",
                 "origin": "console",
                 "definitionGroup": "custom",
                 "dataType": "int32",
                 "aggregation": "latest",
                 "maxValue": "10000",
                 "minValue": "0",
                 "initialValue": "0"
             }
         ],
         "statExtractions": [
             {
                 "ruleId" : 1000,
                 "definitionGroup": "custom",
                 "condition": {
                     "eventName": "SampleActivityEnd",
                     "property": {
                         "path": "$.score",
                         "comparator": ">",
                         "value": "1"
                     }
                 },
                 "action": {
                     "input": "$.score",
                     "output": {
                         "statName": "SampleStat"
                     }
                 }
             }
         ]
     }
}
```

## Q. Where Can I Download JSON Schemas and Samples for UBP?

Schemas for bulk uploading various objects can be downloaded from SDK Manager. For
more details on where it is located, see [JSON Structure for Importing & Exporting Objects](bulk-configuring-uds-entities.html#topic315301_5_8__json-structure-for-importing-exporting-objects_html).

Similarly, sample JSON files for bulk upload can be downloaded from SDK Manager as
well. For more information, see [Additional User Bucket for Partners Sample Metadata Provided in the SDK Manager](bulk-configuring-uds-entities.html#topic315301_5_8__uuid-ec2b751e-86d1-830f-6b0f-2affa59d7d27).