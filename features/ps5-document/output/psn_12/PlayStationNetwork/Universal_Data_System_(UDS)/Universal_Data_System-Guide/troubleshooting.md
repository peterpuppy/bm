# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/troubleshooting.html

# Troubleshooting

This chapter contains troubleshooting information for errors you may encounter when
using UDS.

# UDS Configuration/Tool

This topic contains frequently asked questions you may encounter when configuring UDS or using the UDS Management Tool.

## Q. Resolving "missingParentActivity" Error From Integrity Check

If you see this error being returned after running the UDS integrity check, this is
because one or more child tasks or subtasks have no parent activity or parent task
(in the case of subtasks) assigned to them. The integrity check also details which
of these tasks or subtasks this is affecting so this can be addressed by specifying
the missing parent entities for the designated orphan children entities (tasks or
subtasks which have no parent). To repair the parent/child relationship in UDS, you
have to use the UDS Management Tool's JSON import (there is no way to add orphaned
tasks/subtasks to parent entities from the tool UI itself), UBP or the UDS Configuration
Web API.

In the case of orphaned tasks or subtasks, the issue can be addressed by re-importing
all objects by selecting the "Delete All Objects and Overwrite" option when importing a (`.json`) file and fixing the parent/child relationship of the orphaned tasks or subtasks
within the file itself (when performing this step, you must include all objects in
your UDS configuration, regardless of whether or not they are plagued by the orphaned
task/subtask issue) or by using the UDS Configuration Web API.

Examples of an orphaned activity is when one of the below happens:

1. Tasks/subtasks are imported without linked parents through JSON import or UBP.
2. Rare partial failure scenarios where tasks/subtask creation is successful but parent
   creation failed (for example, after task creation results in maxing out the number
   of activities so the parent activity creation failed).
3. Unexpected failure during tasks/subtasks move operation.

For more information on orphaned tasks, refer to the technote [Orphan Entities Not Visible in UDS Management Tool](https://p.siedev.net/technotes/view/111/1) and [Managing Orphan Objects](configuring-the-uds-data-model.html#topic315301_5_7__managing-orphan-objects) where you can view all orphans and delete them all from the UI.

## Q. Unable to Download npconfig.zip

If you find that the GEMS tool is not letting you download the `npconfig.zip` file and the error message returned is unhelpful, the recommended solution is to
run the integrity check again via the UDS Management Tool. If the download issue is
due to misconfiguration, the integrity check generates a `.json` file indicating where the misconfiguration is.

If an integrity check passes but you are still unable to download `npconfig.zip`, contact developer support and they can investigate the cause for you.

# Trophy

This topic contains troubleshooting information for trophies.

## Q. Resolving "assetUrl in titleMetadata is not defined or invalid URL format" For Trophy Configuration

If you see this error after running the integrity check, this refers to the icon image
missing for the trophy set itself. Even though this is an optional field in sp-int,
this image must be added during submission.

Add trophy icon images from **Features** > **Trophies** > **Actions** > **Configure Trophy Set and Trophy Groups**.

## Q. Trophies Are Occasionally Not Unlocking

If trophies are occasionally not unlocking in your application, one potential reason
is `sceNpUniversalDataSystemPostEvent()` is failing with the following error, `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY`.

This can happen if you are creating objects with `sceNpUniversalDataSystemCreateEventPropertyObject()`, but not calling `sceNpUniversalDataSystemDestroyEventPropertyObject()` to do the clean up. Similarly for `sceNpUniversalDataSystemCreateEventPropertyArray()` as well.

In situations like this, calling `sceNpUniversalDataSystemGetMemoryStat()` can give you an insight into the state of UDS memory. It is recommended to test run
your application a few times to check memory usage by calling `sceNpUniversalDataSystemGetMemoryStat()` to determine the optimal memory value to pass in for `poolSize` when initializing UDS library.

For more information on memory usage, see [NpUniversalDataSystem Library Overview - Using the Library - Initialization](https://p.siedev.net/resources/documents/SDK/latest/NpUniversalDataSystem-Overview/0002.html).

## Q. UDS Management Tool Erroring While Trying To Import PS4 Trophy File (.TRP)

When importing a `.TRP` file for a brand-new NP Communication ID, you might see the error message, "An error occurred while submitting an import request." This happens if a user attempts to create a trophy before creating any other entities.

As a quick workaround, this can be fixed by creating an activity, zone, or mechanic
object. It can be deleted afterwards but it should unblock the ability to create/import
trophies.

Another situation where an error might return is due to an attempt to import `.TRP` file that has a verification error. This could be due to misconfiguration of the
`.TRP` file, for example missing images, wrong point allocation etc. To double check that
the `.TRP` is successfully verified, use the "Trophy Pack File Utility'' to do the verification.
For more details on verification steps, see [Trophy Pack File Utility User's Guide - Creating Trophy Pack Files](https://ps4.siedev.net/resources/documents/Misc/current/Trophy_Pack_File_Utility-Users_Guide/0002.html).

## Q. Trophy Icons Not Imported Successfully From PS4 Trophy File (.TRP)

When performing the `.TRP` import, note that this process does not include images provided in the `.TRP`. This is because the trophy icon sizes have changed for PlayStation®5 - from 240x240
to 512x512, therefore it doesn't import the PlayStation®4 icons included in the `.TRP` file, instead it is expected that new icons of the appropriate size are provided.

If you are performing the `.TRP` import, and you already have referenced images for some trophies uploaded to UDS,
it is important to note that the UDS Management Tool tracks the associated media file
information and automatically re-associates the relevant files upon entity creation
(in this case, upon `.TRP` import). So, for those trophies with unchanged trophy object IDs, the already uploaded
images are re-associated upon `.TRP` import completion.

## Q. The Trophy ID and Object ID Get out of Sync

If the trophy ID and object ID get out of sync, the following options exist to have
them updated:

**Option 1:**

If the number of changes is small, go to the UI, edit the trophy, and re-order trophies
using the "display order" field value to the desired order. This generates the new trophy IDs based on the
order of trophies.

**Option 2:**

Re-order using the UI bulk import/export feature. From the UI, you can export all
trophies (Action `->` Export all trophy objects (`.json`)), look for `_baseGameGroup` object in `trophyGroups` array. Locate the `trophies` array in the links property of the `_baseGameGroup` and update the "position" property to re-order the trophies. Once updated, import this back using the bulk
UI import function from UI (Action `->` Import all trophy objects (`.json`)). You can use the "Add/New Update Existing Trophies" option.

**Option 3:**

Re-order using the UBP feature. Create a `_baseGameGroup` object in the "trophyGroups" array and create the "trophies" array in the links property of the `_baseGameGroup`. Update the "position" property to re-order the trophies. Reference the sample below:

```
{
     "schemaVersion": "6.0",
     "contextType": "NPCommunicationId",
     "contextId": "XXXXXXXXX_XX",
     "entities": {
         "trophyGroups": [{
                 "objectId": "_baseGameGroup",
                 "metadata": {
                     "trophyGroupId": "0000",
                     "sortKey": "0001",
                     "isBaseGameGroup": true,
                     "name": {}
                 },
                 "links": {
                     "trophySet": [{
                             "object": {
                                 "objectId": "_trophySet"
                             }
                         }
                     ],
                     "trophies": [{
                             "object": {
                                 "objectId": "Trophy_001"
                             },
                             "position": 1
                         }, {
                             "object": {
                                 "objectId": "Trophy_002"
                             },
                             "position": 2
                         }, {
                             "object": {
                                 "objectId": "Trophy_003"
                             },
                             "position": 3
                         }, {
                             "object": {
                                 "objectId": "Trophy_004"
                             },
                             "position": 4
                         }, {
                             "object": {
                                 "objectId": "Trophy_005"
                             },
                             "position": 5
                         }, {
                             "object": {
                                 "objectId": "Trophy_006"
                             },
                             "position": 6
                         }, {
                             "object": {
                                 "objectId": "Trophy_007"
                             },
                             "position": 7
                         }
                     ]
                 }
             }
         ],
         "trophies": [{
                 "objectId": "Test_1",
                 "metadata": {
                     "name": {
                         "en-US": "testing something"
                     },
                     "description": {
                         "en-US": "testing something"
                     },
                     "hasReward": false,
                     "trophyGroupObjectId": "_baseGameGroup",
                     "hidden": false,
                     "grade": "bronze"
                 }
             }
         ]
     }
}
```

## Q. "Display name must be unique" When Updating Trophy Configuration

Occurs when a PlayStation®5 trophy configuration is imported from a PlayStation®4
`.trp` file using the UDS Management Tool. While the import is initially successful, "Display name must be unique" is returned when updating the trophy configuration.

For example, this may occur when uploading trophy icons or editing metadata if the
system finds that there are duplicate names in the configuration file.

To resolve this:

1. Export the trophy JSON file using the UDS Management Tool.
2. Open the exported JSON file and search for the problematic trophy name.
3. Compare the names to find where the duplication occurs. Make sure to check all locales
   for name duplications.

# UBP

This topic contains frequently asked questions you may encounter when using UBP.

## Q. "You do not have privilege NPCommunicationId NPWRXXXXX" When Uploading To UBP

When this error occurs, double check that the SFTP credential maps to the NpCommunicationId
are uploaded that you are trying to connect to, to reference the NpCommunicationId
during upload, it should be located in `metadata.json`, in "contextId" field. Also note that when entering the NPCommunicationId here, make sure there is
a trailing "\_00", this can sometimes be omitted quite easily and cause this error to occur.