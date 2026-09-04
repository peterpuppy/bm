# PlayStation™Store Content Guidelines – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayStation_Store_Content-Guidelines/applied-cross-platform-additional-content.html

# Distributing PlayStation™Store Content

This chapter provides detailed information on the different ways you can distribute content through the PlayStation™Store.

You can distribute content through the for PlayStation™Store for:

* Full game packages
* Upgradeable game/trial versions
* Demos with no restriction unlocking
* Additional content for purchase
* Content based on user purchase history
* Cross-Platform additional content

# Full Game Packages

This topic describes the most basic package type, in which all programs and data are made available in a single package for purchase.

Paid-for Games (No Additional Content)

Main Features of Paid-for Games

| **Package** | **Feature** | **Description** |
| --- | --- | --- |
| Paid-for game package | Entitlement Package Type | * PSGD. |
| Program and data | * No special requirement. |
| Content information files | * No special requirement. |
| GP5 file | * `volume_type` : "`prospero_app`" (PlayStation®5 Application Package). |
| Param file | * "Application Category Type" : 0 * "Application DRM Type" : "standard" |

## Creating Paid-for Game Packages

Note the following points when creating a paid-for game package:

**Program and Data**

There are no special instructions.

**Content Information Files**

There are no special instructions.

**GP5 File**

Create the GP5 file by selecting `prospero_app` (PlayStation®5 Application Package) in `volume_type`.

**Param File**

When creating a param file for an application with Param Editor, set 0 in the "Application Category Type". In addition, select "standard" for "Application DRM Type". Refer to [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html) for more information.

## Content SKU Settings

When a package is uploaded to GEMS and published, the SKU and unified entitlement are automatically generated.

Application Type : Standard and Package Type : PSGD is displayed next to your product in Content Pipeline.

Entitlement Details

# Upgradable Game/Trial Version Packages

This topic describes the release pattern in which all programs and data are distributed as a free trial version (with some functions restricted) and which is upgradable for a fee into a game package without function restrictions (full game).

Upgradable Trial Version

Main Features of Upgradable Trial Version

| **Package** | **Feature** | **Description** |
| --- | --- | --- |
| Dual package | Entitlement Package Type | * PSGD. |
| Program and data | * Includes programs and data for all features. * Checks if license has been purchased. |
| Content information files | * Provides the files that are displayed for the full game. |
| GP5 file | * `volume_type` : "`prospero_app`" (PlayStation®5 Application Package). |
| Param file | * "Application Category Type" : 0 * "Application DRM Type" : "upgradable" |

Attribute Settings

| **SKU** | **Attribute Setting** |
| --- | --- |
| Free trial | Entitlement Flag: Trial |
| Paid-for full game | Entitlement Flag: Full |

## Creating Dual Packages

Note the following points when creating a free trial version with restriction unlock feature plus paid-for full game dual package:

**Program and Data**

Include all the programs and data for realizing all the functions in the free trial version with restriction unlock feature plus paid-for full game dual package.

The game program must be designed so that it can determine whether the user has purchased the license, runs with the restrictions if it has not been purchased, and unlocks the full version of the game if it has.

The check procedure is as follows:

1. Obtain the SKU flag of the application parameters using the NpEntitlementAccess library.
2. If the SKU flag is "Full", unlock the function restrictions and make all features usable.

Checking for Unlock Restrictions

**Content Information Files**

Do not indicate for the content information file included in a dual package that it is a free trial version and instead make it content to be displayed as a full game.

**GP5 File**

Create the GP5 file by selecting "`prospero_app`" "(PlayStation®5 Application Package)" in "`volume_type`".

**Package Type**

When creating a param file for Application with Param Editor, set 0 in the "Application Category Type". In addition, select "upgradable" for "Application DRM Type". Refer to [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html) for more information.

## Content SKU Settings

When a package is uploaded to GEMS and published, the SKU and unified entitlement are automatically generated and are displayed next to your product in Content Pipeline alongside an "Upgradable App Entitlement" flag and an upgradable tracker.

In the case of an upgradable application, a SKU for the trial version and a SKU for the full version are generated. You need to do the association of these versions with the relevant product and create two terms of sale records in Content Pipeline.

For more information on how to set up trial and upgrade in Content Pipeline, refer to [Creating an Upgradable Game (Trials)](https://learn.playstation.net/bundle/content-pipeline/page/PricingAvailability_UpgradeableGameCreate.html).

Checking for Unlock Restrictions

Note: In the development environment it is not possible to create Terms of Sale (TOS) for a trial version until the package has been approved. In order to test this in development contact SIE.

# Free Demo Packages

This topic describes packages for distributing a free demo version of a game. It is assumed that upgrade licenses are not available for purchase.

Free Demos With No Restriction Unlocking

Main Features of Free Demos With No Restriction Unlocking

| **Package** | **Feature** | **Description** |
| --- | --- | --- |
| Free demo package (no unlocking) | Entitlement Package Type | * PSGD. |
| Program and data | * No special requirement. |
| Content information files | * No special requirement. |
| GP5 file | * `volume_type` : "`prospero_app`" (PlayStation®5 Application Package). |
| Param file | * "Application Category Type" : 0 * "Application DRM Type" : "demo" |

## Creating Free Demo Packages

Note the following points when creating a free demo package with no restriction unlocking:

**Program and Data**

The trophy system must not be used. Trophy pack files must not be included in the package, and processing that creates contexts or unlocks trophies must not be performed in programs.

**Content Information Files**

There are no special instructions.

**GP5 File**

Create the GP5 file by selecting `prospero_app` (PlayStation®5 Application Package) in `volume_type`.

**Package Type**

When creating a param file for the application with Param Editor, set 0 in the "Application Category Type". In addition, select "demo" for "Application DRM Type". Refer to [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html) for more information.

## Content SKU Settings

When a package is uploaded to GEMS and published, the SKU and unified entitlement are automatically generated.

Application Type and Package Type are displayed next to your product in Content Pipeline.

Application and Package Type

# Additional Content

This topic describes the release process for when additional stages/storylines for a game are made available for purchase as additional content.

The following describes an example where the game itself is sold as a paid-for game package but distributing as an upgradable trial version is similar.

For selling additional content, there are several methods:

* Additional content is contained and distributed in the additional content package associated to PSAC unified entitlement.
* Additional data is stored in the paid-for game package from the beginning with just the entitlement information distributed as additional content associated to PSAL unified entitlement.
* Consumable entitlements distributed as PSCONS unified entitlement.
* Virtual currency distributed as PSVC unified entitlement.

Paid-for Game Plus Paid-for Additional Content With Extra Data

Main Features of Additional Content for Purchase

| **Package** | **Feature** | **Description** |
| --- | --- | --- |
| Paid-for game package | Entitlement Package Type | * PSGD. |
| Program and data | * Program checks additional data entitlements before usage. |
| Content information files | * No special requirement. |
| GP5 file | * `volume_type` : "`prospero_app`" (PlayStation®5 Application Package). |
| Param file | * "Application Category Type" : 0 * "Application DRM Type" : "standard" |
| Additional content package (with extra data) | Entitlement Package Type | * PSAC. |
| Data | * No special requirement. |
| Content information files | * Indicates clearly that it is additional content. |
| GP5 file | * `volume_type` : "`prospero_ac`" (PlayStation®5 Additional Content Package). * Specify "Entitlement Key". |
| Param file | * Create param file for Additional Content. |
| Additional content package (without extra data) | Entitlement Package Type | * PSAL. |
| Data | * None. |
| Param file | * Create param file for Additional Content. |
| Metadata | * Still-image icon files. * Specify "Entitlement Key". |
| Consumable entitlement | Entitlement Package Type | * PSCONS. |
| Data | * None. |
| Metadata | * Specify `useLimit`. |
| Virtual currency | Entitlement Package Type | * PSVC. |
| Data | * None. |
| Metadata | * Specify `useLimit`. |

Note:
When providing the game itself as an upgradable trial version, set "Application DRM Type" to "upgradable".

## Creating Paid-for Game Packages

Note the following points when creating a paid-for game package that allows the purchase of additional content:

**Program**

The game program must be designed so that it determines whether the user has purchased additional content and uses the additional content if it has been purchased and runs without it if it has not.

To determine whether a user has made a purchase or not, use the following procedure.

1. Use the NpEntitlementAccess library to obtain entitlement information for the additional content.
2. If an entitlement exists, perform processing that uses the additional content.

In addition, there may be cases where additional content with extra data has been purchased but the data does not exist. If additional content has not been installed, it is required to re-download the additional content. To check if data exists, use the NpEntitlementAccess library to obtain the status of the data. The status is included in the entitlement information that was obtained with the library.

Note:

There are a number of ways for obtaining entitlements using the NpEntitlementAccess library. For details, refer to the explanations for the procedures for accessing additional content in [NpEntitlementAccess Library Overview](../NpEntitlementAccess-Overview/__document_toc.html).

Checking if Additional Content Has Been Purchased or Not (Additional Content with Extra Data)
Checking if Additional Content Has Been Purchased or Not (Additional Content Without Extra Data)

**Content Information Files**

There are no special instructions.

**GP5 File**

Create the GP5 file by selecting "`prospero_app`" "(PlayStation®5 Application Package)" in "`volume_type`".

**Param File**

When creating a param file for Application with Param Editor, set 0 in the "Application Category Type". In addition, select "standard" for "Application DRM Type". Refer to [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html) for more information.

Note:
When providing the game itself as an upgradable trial version, set "Application DRM Type" to "upgradable".

**Content SKU Settings**

When a package is uploaded to GEMS and published, the SKU and unified entitlement are automatically generated.

Application Type and Package Type are displayed next to your product in Content Pipeline.

Application and Package Types

## Creating Additional Content Packages with Extra Data

Note the following points when creating a package of additional content that includes extra data such as additional stages.

**Data**

There are no special instructions.

**Content Information Files**

Content information must indicate clearly that they are additional content.

**GP5 File**

Create the GP5 file by selecting "`prospero_ac`" "(PlayStation®5 Additional Content Package)" in "`volume_type`".

In addition, set the "Entitlement Key". When a user purchases additional content, the application is able to obtain the entitlement key.

Note:

For details on setting entitlement keys, refer to the [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html).

**Param File**

When creating a package with Publishing Tools GUI, select "Additional Content Package with Extra Data" from "New Project" in the "File" menu.

Create the param file for Additional Content. Refer to the [Param Editor User's Guide](../Param_Editor-Users_Guide/__document_toc.html) for details.

**Content SKU Settings**

When additional content package is uploaded to GEMS and published, the SKU and unified entitlement are automatically generated.

SKU and Unified Entitlements

## Creating Additional Content Packages without Extra Data

Create PSAL entitlement with setting the "Entitlement Key" with GEMS.

**Data**

No data is required for PSAL.

**Content SKU Settings**

When a zip file that contains the files for creating PSAL is uploaded to GEMS and published, the SKU and unified entitlement are automatically generated.

SKU and Unified Entitlements

Application Type and Package Type are displayed next to your product in Content Pipeline.

Note:
When the package upload processing completes for an additional content package, it is automatically published in the development environment.

## Creating Virtual Currency and Other Consumables

Entitlements for virtual currency and other consumable content types that have a limited usage allowance for the game such as ammunition can also be realized using a unified entitlement. The entitlements for these content types can be generated within Content Pipeline itself and linked to the product. No separate upload to GEMS is needed to generate entitlements for these content types.

In case of consumable content types, the game application is responsible for retrieving the number of usable times for the item and notifying PlayStation™Network of the number consumed. Thus, even if data on storage is lost due to hardware problems or user operation, the number of times an item has been used can be managed safely. The game application uses NpEntitlementAccess library for this.

Virtual currency is managed differently from other consumable content types. For PSVC entitlement type, the consumption is to be fully managed on game servers. The game application is required to transfer the virtual currency entitlements from PlayStation™Network on purchase in a single transaction and thereafter manage usage and count through the game's own servers. For a detailed, end-to-end, example implementation of this consumption pattern, see [Virtual Currency Tutorial](../Virtual_Currency-Tutorial/__document_toc.html).

**Content SKU Settings**

The SKU and unified entitlement settings are shown below.

SKU and Unified Entitlements

# Content Based on Purchase History

This topic provides information on the release process that uses eligibility rules to provide the user with an appropriate selection of content according to the user's own purchase history.

Eligibility rules are provided in the PlayStation™Store so that SKUs are only displayed to users who satisfy preset conditions. In the example below, only users who have purchased a certain paid-for game package are shown the additional content package for that game, preventing other users from buying the additional content. It is also possible to prevent users who have purchased a complete set of additional content from purchasing the individual (redundant) contents. This method can also be used to exclusively provide a discount for a new game to users who have purchased the previous game in the series.

When considering the use of eligibility rules, contact SIE in advance.

Content Distribution Based on Purchase History

## Creating Game Packages and Additional Content

There are no special points to note for creating content when using eligibility rules.

**Content SKU Settings in Content Pipeline**

Eligibility rules are assigned per "Pricing and Availability" record in Content Pipeline.

Note:
Eligibility rules cannot restrict any downloads from the download list after the purchase of the content. For example, suppose that eligibility rules prevent users who have purchased the paid-for unlock key from obtaining the free trial version. The user is still able to download and install the free trial version from the download list, so it is not possible to prevent the re-installation of the free trial package.

# Cross-Platform Additional Content

This topic describes the release of additional content for both the PlayStation®4 and PlayStation®5 platforms.

The following three examples show typical usage:

1. Additional content is created for both platforms and released as a set consisting of a single SKU (when releasing for both platforms at the same time).
2. Additional content is created for both platforms, and a user who purchases one is provided with the other for free by setting eligibility rules (when releasing additional content for the other platform when it has already been released for one platform).
3. Setting service entitlements and the applications for both platforms references entitlement information (when various restrictions can be conceded).

## Releasing Additional Content for Both Platforms as a Set

In this method, additional content is created for both platforms, then they are released under the same SKU. Purchasing a single SKU allows the entitlements for using both additional content packages to be obtained, and the additional content is seen by the user as being shared. This method is typical when releasing additional content for both platforms at the same time.

Set Released Cross-Platform Content

**Creating Game Packages**

Paid-for game packages must be created for both respective platforms.

The procedure for creating paid-for game packages for PlayStation®5 is the same as that described in [Full Game Packages](full-game.html "This topic describes the most basic package type, in which all programs and data are made available in a single package for purchase.").

**Creating Additional Content Packages**

Additional content packages must be created for both respective platforms.

The procedure for creating additional content packages for PlayStation®4 is the same as that described in [Additional Content](additional-content-for-purchase.html "This topic describes the release process for when additional stages/storylines for a game are made available for purchase as additional content.").

**Content SKU Settings (Shared Additional Content)**

Register the additional content packages for both platforms in Content Pipeline, create a single SKU, and associate the additional content packages for both platforms with the SKU.

## Setting Eligibility Rules and Providing Purchasers of One Version with the Other Version for Free

When additional content that has already been released for one platform is then released for the other platform, support for users who have already purchased the released additional content becomes a problem. Even if new additional content is associated with an existing SKU, users who have not yet purchased the existing additional content obtains the entitlement to use both when they purchase the SKU, but it is not possible to provide users who have already purchased the existing additional content with the new additional content.

This problem can be solved by using eligibility rules to provide purchasers of the existing additional content with the new additional content for free.

Cross-Platform Release for Past Purchasers of Additional Content

**Creating Additional Content Packages**

There are no special points to note for creating additional content packages.

**Content SKU Settings (Past Purchasers)**

Create a SKU for past purchasers, associate the new additional content, and set it to be released for free. In addition, use eligibility rules to set the SKU so that it only displays for purchasers of the existing content.

# Additional Distribution of Trial Versions

This topic explains the additional distribution of a trial version after a paid-for game has already been released.

In such cases, rather than the method of separately creating/distributing a free trial version as explained in [Free Demo Packages](free-demos-with-no-restriction-unlocking.html "This topic describes packages for distributing a free demo version of a game. It is assumed that upgrade licenses are not available for purchase."), using an update to change an existing paid-for game to an upgradable trial version is recommended.

When an update is released, whenever the paid-for game package is thereafter downloaded, the latest package is downloaded. In other words, new users can obtain the upgradable trial version with the latest downloaded package from the start.

On the other hand, the update is distributed to users who already purchased the paid-for game. Since these users already have licenses, when the update is applied, the upgradable trial version is in the already upgraded state.

Therefore, trial versions can be easily added by using an update to change an existing paid-for game to an upgradable trial version.

In regard to development/management processes, a different NP Title ID is assigned when separately creating a free demo, but with an update the NP Title ID of the existing paid-for game can be used as-is, and it is not required to make another request for usage of the services of PlayStation™Network. In addition, when updating the game in the future, the trial version and paid-for version game can be updated with the same update, therefore upgradable trial versions have additional advantages.

Trial Versions That Are Upgradable with an Update

Main Features for Changing an Already Released Paid-For Game to an Upgradable Trial Version

| **Package** | **Feature** | **Description** |
| --- | --- | --- |
| Update package | Entitlement Package Type | * PSGD. |
| Program and data | * No special requirement. |
| Content information files | * No special requirement. |
| GP5 file | * `volume_type` : `"prospero_app"` (PlayStation®5 Application Package). |
| Param file | * "Application Category Type" : `0` * "Application DRM Type" : "upgradable". |

Table 9

| **SKU** | **Attribute Setting** |
| --- | --- |
| Free demo | Entitlement Flag: Trial |

## Creating Update Packages

Additional Create an update package for changing an already released paid-for game to an upgradable trial version. Note the following points:

* Programs and Additional Data

The game program must be designed so that it determines whether or not the user has purchased the license, runs with the restrictions if it has not been purchased, and unlocks the full version of the game if it has.

For details, refer to [Upgradable Game/Trial Version Packages](upgradable-game-trial-version.html "This topic describes the release pattern in which all programs and data are distributed as a free trial version (with some functions restricted) and which is upgradable for a fee into a game package without function restrictions (full game)."). In addition, refer to the "Patch and Remaster Overview" document as necessary.

* GP5 File

Create the GP5 file by selecting `"prospero_app"` "(PlayStation®5 Application Package)" in `"volume_type"`.

* Package Type

When creating a param file for Application with Param Editor, set 0 in "Application Category Type". In addition, select "upgradable" for "Application DRM Type". Refer to [Publishing Tools GUI User's Guide](../Publishing_Tools_GUI-Users_Guide/__document_toc.html) for more information.

* Content SKU Settings in Content Pipeline

After a patch package is released, create a new "Pricing and Availability" record from "Add Global Availability". Select the "Trial" option. It is not necessary to change the "Pricing and Availability" record of an existing paid-for full game.

Note:

A SKU set to "Trial" can be created after the release of a patch.