# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/create-the-np-config-tag.html

# Prepare for Platform Certification and Operations Submission

After creating packages files, you can distribute them to internal testing and verification
teams who can test, among other things, your data-driven experiences. Whereas the
"debug" task mentioned previously is mostly focused on engineering teams who iterate as they
develop and refine the UDS configuration, this preparation for Platform Certification and Operations submission
step is typically performed by dedicated QA teams using packages that correspond to
release builds that closely resemble the finished product.

# Create the NP Config Tag

This topic outlines the procedure for creating NP Config Tags. The purpose of an NP
Config Tag is to mark a specific version of the UDS configuration that is included in your
package file.

Once you create an NP Config Tag for a specific NP Communication ID, any new NP Config Tag
must include all of the entities that were included in all previous NP Config Tags. In
addition, certain properties of UDS entities are locked to ensure integrity with previous
version once the NP Config Tag is created. You can find more information about these entity
statuses in the document linked below.

You can delete an NP Config Tag up until your product is submitted for Platform Certification and Operations review.
Once it passes the review, the NP Config Tag is ready to be published to production
along with your game package. At this point, the NP Config Tag can be updated and
republished but cannot be deleted and replaced.

Table Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) | See [Universal Data System Guide - Preparing a Package for Release](../Universal_Data_System-Guide/preparing-a-package-for-release.html), which applies to creating a package for testing in preparation of uploading for Platform Certification and Operations review. |
| [Universal Data System Guide - Using the UDS Management Tool - Configuring the UDS Data Model](../Universal_Data_System-Guide/configuring-the-uds-data-model.html) | The Action Depending on Status section Contains a table of UDS entities that indicates which entities can be edited based on the status of your NP Config Tag. |

# Create the Package

This topic provides an overview of the procedure for internal QA testing of your
data-driven experiences. This workflow assumes you are creating a release-ready version of
your game's package file.

The basic steps in this process are:

1. Run an integrity check in the UDS Management Tool.

   This ensures referential integrity for referenced entities and compatibility checks
   for entities included in previous NP Config Tags.
2. Create an NP Config Tag in the UDS Management Tool.

   See [Create the NP Config Tag](create-the-np-config-tag.html "This topic outlines the procedure for creating NP Config Tags. The purpose of an NP Config Tag is to mark a specific version of the UDS configuration that is included in your package file.").
3. Download the configuration files (`npconfig.zip`) from the Package/Disc Management Tool (GEMS).

   The `npconfig.zip` file is downloaded for a specific NP Config Tag. Therefore, a new `npconfig.zip` file must be downloaded for each new UDS configuration that you create.
4. Create a package file (`.pkg`) using the applicable publishing tools.

   During package creation, you will supply the `npconfig.zip` file.
5. Distribute the package file to TestKits for testing.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) | Contains a section on preparing a package for release, which applies to creating a package for testing in preparation of uploading to Platform Certification and Operations review. |
| [Content Packaging and Updating Guide](../Content_Packaging_and_Updating-Guide/__document_toc.html) | Describes the information contained in package files. Explains the shared binary format, which lets you submit a single package for all of the countries and regions that you intend to sell in. |
| [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html) | Contains a section about package creation, which explains the procedure for creating packages. |
| [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) | Contains a section titled [Package/Disc Management Tool (GEMS) Overview - Downloading Configuration Files](../Package_Disc_Management_Tool_GEMS-Overview/downloading-configuration-files.html), which pertains to the `npconfig.zip` file that is required for package creation. |

# Test the Package

This topic provides guidance on what tools you can use to perform QA tests on packages
you create.

After creating the package file, you can distribute it via Target Manager to TestKits
for internal QA. Note that it's advisable to perform final checks on your TestKit
with "Release Check Mode" set to "Release".

The development accounts used for such testing activities must have the proper title
privileges. Activity cards and related features, such as Game Help, will not display
if the user's account does not have the proper title privileges. See [Set up Title Privileges](set-up-title-privileges.html "Accounts for PlayStation™Network are assigned to individuals who will be debugging or testing experiences. Title privileges ensure that sensitive details about your game are not exposed during development.") for more information.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Target Manager GUI User's Guide](../Target_Manager_GUI-Users_Guide/__document_toc.html) | Explains how to use Target Manager, which among other things lets you install game packages on DevKits or TestKits ("Targets"). |
| [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html) | Covers how to check and set the "Release Check Mode" for testing. |
| [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html) | For testing, read the following section: [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html). This section explains how to delete UDS-related data (for example unsent UDS events and UDS stats) from the system for debugging and testing purposes. |
| [PlayStation™Network Overview](../PSN-Overview/__document_toc.html) | Contains information under [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html) about configuring title privileges for accounts. |