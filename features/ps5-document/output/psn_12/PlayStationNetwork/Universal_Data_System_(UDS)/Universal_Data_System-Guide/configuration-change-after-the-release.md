# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/configuration-change-after-the-release.html

# Preparing a Package for Release

This topic covers the procedure for preparing a release package.

The steps for preparing a release package is shown in the following figure and explained
below.

Preparing a Release Package

1. Run the Integrity Check.

   To create the NP Config Tag, it is important to ensure that both the referential integrity
   and compatibility checks are performed. These checks are run at various points of
   the publishing processes.

   Referential integrity checks ensure that all referenced entities actually exist. For
   example, if a stats extraction rule references a UDS event and one or more of its
   properties, the integrity check ensures that the event and its properties are actually
   defined. Compatibility check ensures that all entities included in the previous NP
   Config Tag is included in the newer NP Config Tags.

   If there are errors, you will see the integrity check error screen. In addition, all
   the errors and suggested actions will be provided via a JSON file.

   Note:

   If you are going to publish an object that is not related to a package for release,
   you can skip the following steps and publish without a package after running an integrity
   check. For a detailed list of all objects, see [PlayStation™Network Objects](psn-objects.html "PlayStation™Network objects represent static information used in a game such as the story's missions and locations. A game can use feature events associated with PlayStation™Network objects to send an in-game event or player activity to the platform.").
2. Create the NP Config Tag.

   In order to create a package for submission, you are required to create an NP Config
   Tag. The NP Config Tag is used for marking a specific point in UDS configuration (including
   Trophy) and any release including metadata update is based on the NP Config Tag. Once
   the NP Config Tag is created, the entities are locked, and the edit is restricted
   in order to guarantee the integrity of data. For restriction details, refer to [Action Depending on Status](configuring-the-uds-data-model.html#topic315301_5_7__action-depending-on-status_html).

   Note:

   The NP Config Tag can be deleted when the status is "Tagged".
3. Download the configuration file.

   Select the NP Config Tag for the game package you plan release when downloading the
   configuration file.

   Note:

   When you want to use the latest configuration during the development phase, do not
   select NP Config Tag. The latest configuration is included in the configuration file.
4. Create a game package using the configuration file you downloaded in the previous step. For details, refer to the [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html).
5. Upload the package to Package/Disc Management Tool (GEMS). For details, refer to the [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html).

# The Status of the NP Config Tag

This topic shows the different statuses the NP Config tag can be in.

The status of the NP Config Tag is shown in the following figure and table. These
statuses are further explained within [Pre-Master Submission / TRC Verification (TRC "Sweep") Support](pre-master-submission-trc-verification-trc.html "SIE offers services that review the disc and digital based title and identifies the issues before the master submission. In order to continue the development and testing during pre-master submission / TRC verification (TRC \"Sweep\"), you can delete the np config when the status of NP Config Tag is \"inFormatQa\" and its submission type is \"pre-submission\".").

NP Config Tag Status Diagram (Master Submission)

Status of NP Config Tag

| **Status** | **Description** |
| --- | --- |
| Tagged | When the NP Config Tag is newly created or the Platform Certification and Operations process has failed, the status is set as "Tagged". When the status is "Tagged", the NP Config Tag can be deleted. |
| In Format QA  (Master Submission) | Status where SIE has received a content and is preparing to start certification or certification is being performed. |
| Format QA Completed | Platform Certification and Operations process is completed, and the configuration is ready to publish. |
| In Production | The NP Config Tag is published to the production along with all the configuration associated with the NP Config Tag. |

# Pre-Master Submission / TRC Verification (TRC "Sweep") Support

SIE offers services that review the disc and digital based title and identifies the issues before the master submission. In order to continue the development and testing during pre-master submission / TRC verification (TRC "Sweep"), you can delete the np config when the status of NP Config Tag is "inFormatQa" and its submission type is "pre-submission".

This allows the entities to become unlocked.

## Pre-Master Submission

Allows submissions of feature-complete disc and digital based titles for review to
identify serious issues before submitting for the master submission.

## TRC Verification (TRC "Sweep")

Offered as a focused testing option to evaluate disc and digital based titles for
compliance with the relevant TRC prior to the master submission. For
details, please refer to the [CertOps Guide](https://learn.playstation.net/bundle/certops-guide/page/home.html).

The status of the NP Config Tag (pre-master submission / TRC Verification) is shown
in the following figure, and each status is explained in the following table.

NP Config Tag Status Diagram (TRC Verification/ Pre-Master Submission)

Status of NP Config Tag (TRC Sweep or Pre-Master Submission)

| **Status** | **Description** |
| --- | --- |
| Tagged | When the NP Config Tag is newly created or the Platform Certification and Operations process has failed, the status is set as "Tagged". When the status is "Tagged", the NP Config Tag can be deleted. |
| In Format QA  (Pre-Submission) | Status where SIE has received a content and TRC Verification/Pre-Master Submission is being performed. When the status is "In Format QA" and the submission type is "Pre-Submission", the NP Config Tag can be deleted so that the UDS entities are unlocked for modification. |

# Configuration Change After the Release

The UDS configuration (including trophy configuration) can be changed after a game
release. Depending on the configuration change, the required action is different.

Note:

This explanation is for objects related to a package for release. If the objects are
not related to a package for release, you can publish your updates for both **In Development** and **Published**  objects without publishing a Patch Package and creating a new NP Config Tag.

* One or more PSN objects is updated after the game release.

  You can re-publish metadata changes from the UDS Management Tool without preparing
  the patch package.

  |  |  |
  | --- | --- |
  | Patch Package : | Not Required |
  | New NP Config Tag : | Not Required |
* One or more PSN objects or events are newly added after the game release.

  You must publish the patch package to reflect a change to production. Create the NP
  Config Tag and use it to prepare the patch package.

  |  |  |
  | --- | --- |
  | Patch Package : | Required |
  | New NP Config Tag : | Required |
* Trophy configuration that has already been released is updated.

  You must publish the patch package to reflect a change to production. Create the NP
  Config Tag and use it to prepare the patch package.

  |  |  |
  | --- | --- |
  | Patch Package : | Required |
  | New NP Config Tag : | Required |
* One or more Trophy Groups/Trophies added to the trophy set are already published.

  You must publish the patch package to reflect a change to production. Create the NP
  Config Tag and use it to prepare the patch package.

  |  |  |
  | --- | --- |
  | Patch Package : | Required |
  | New NP Config Tag : | Required |
* Added a new supported language and set localization.

  You must publish the patch package to reflect a change to production. Create the NP
  Config Tag and use it to prepare the patch package.

  |  |  |
  | --- | --- |
  | Patch Package : | Required |
  | New NP Config Tag : | Required |

# Integrity Check Dry Run

This topic covers how to perform a dry run of integrity checks before publishing entities.

Use **Publishing > Integrity Check** to access the integrity check dry run function, shown in the following figure. Refer to
[Preparing a Package for Release](preparing-a-package-for-release.html "This topic covers the procedure for preparing a release package.") for details about the UDS integrity check.

Integrity Check

Note:

The integrity check dry run always checks the latest data. The UDS Management Tool
also supports running integrity check against a specific NP Config Tag. Please refer
to the [Running Integrity Check Against NP Config Tag](running-integrity-check-against-np-config.html "This topic provides guidance on running integrity checks for specific NP Config tags.") section for more information.