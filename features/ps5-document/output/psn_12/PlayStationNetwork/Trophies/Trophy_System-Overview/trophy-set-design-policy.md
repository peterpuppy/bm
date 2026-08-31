# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/trophy-set-design-policy.html

# Trophy Set Design Policy

This topic describes the policy for how many trophies to make available and when to make them obtainable in the game.

# Design Policy

The trophy system is a service provided throughout the PlayStation™Network platform and does not handle titles separately. Trophy points earned by a user are aggregated across titles and used for display or comparison. Because the design of a trophy set for one title can affect the entire platform, a common design policy is defined for all titles.

# Titles That Must Support the Trophy System

Titles for PlayStation®5 belong to either of two categories: those that must support the trophy system and those that must not support the trophy system.

Titles that satisfy all of the conditions below must support the trophy system:

* The Title ID is issued as a "Full Game".
* The title will be sold at a cost or provided as a freemium game (free application that attempts to earn profit through the sale of items, subscriptions, and so forth, on the PlayStation™Store).
* Game elements are included.

Titles that do not satisfy one of the above conditions must not support the trophy system.

# Trophy Points Assignment per Title

The grade makeup of trophies that can be included in a trophy set and the total of their trophy points (trophy points assigned to the title) are predetermined to ensure that game scores are fairly calculated across titles.

* Bronze = 15 points per trophy
* Silver = 30 points per trophy
* Gold = 90 points per trophy
* Platinum = No points assigned. If you have set up this trophy, players who have obtained all the bronze, silver, and gold trophies that are platinum-linked to this trophy in the main game's trophy set will be able to earn this trophy.

## Main Game of Paid-For Games and Freemium Games

The total points of all the trophies for the main game (base game group) of a paid-for game or freemium game must be within the range of 285 to 1050 points. You must set up a minimum of four trophies based on these point ranges. In other words, set up at least 285 trophy points with three gold trophies and one other grade trophy. On the other hand, the maximum number of trophies that can be set up in the base game group is 71. This is because 70 bronze trophies will total 1050 trophy points, and games with at least 950 points will also need to include one platinum trophy.

A platinum trophy must be set up when assigning 950 trophy points or more to trophies in the main game, and the platinum link attribute of all the other non-platinum trophies must be set to "Linked". Meanwhile, titles whose total number of trophy points is less than 950 points must not have a platinum trophy set up. It is not necessary to assign 950 trophy points to a game, but it is strongly recommended that 950 or more trophy points be assigned so that a platinum trophy can be set up, as many users spend more time playing in order to acquire the platinum trophy.

Trophies for the main game can only be assigned to the base game group and cannot be assigned to an additional trophy group. It must be possible to unlock all the trophies in the base game group without installing any additional content or updates.

However, if 1050 points will be exceeded when a cross-platform title allows players to obtain trophies equivalent to existing titles in the PlayStation®5 version of the main game, it is sometimes possible to set a part of the trophies that can be obtained in the main game to an additional trophy group. This also includes cases when a title is transferred from PlayStation®4 to PlayStation®5 and an attempt is made to import an additional trophy group already released in the PlayStation®4 version to the main game of the PlayStation®5 version. If you think this condition applies to a title under development or in the planning process, contact us via "Post new issue" of Private support (<https://game.develop.playstation.net/support/>). We can discuss the possibility of additional trophy groups. Please note that you may be asked to lower trophy grades in order to reduce the total number of trophy points.

## Applications Designed to Be Switchable from a Trial Version to a Product Version

A free trial-version application with limited playable game elements or limited play time, which can be played in full without limitations if its product version is purchased from the PlayStation™Store, is categorized as an application that is designed to be switchable from a trial version to a product version. An upgradable application fits this category.

For an upgradable application, include a trophy configuration file in the package and post a UDS event that satisfies a trophy unlocking condition. (Nothing will be displayed in the trophy collection until the full game is purchased.)

A trophy whose unlocking condition was satisfied while the user played the trial version will be unlocked automatically when the full game is purchased. There will be no need for the user to repeat gameplay to earn the same trophy again after purchasing the full game.

Create trophy sets for upgradable applications in the same way as for paid-for games and freemium games.

## Demo Versions

A free application that is extracted from a paid-for full game is categorized as a demo version (to be provided, for example, to try out a game at an exhibition).

The trophy system cannot be used in demo versions. Do not include the trophy configuration file in packages for demo versions.

# Trophy Group for Additional Content or Updates

Trophies can be added as part of additional content or updates that satisfy the following conditions:

* The paid-for or free additional content or update is meant to expand the scope of gameplay.

An example of expanding the scope of gameplay is to add stages or enemy opponents. Adding elements that don't affect the main game, such as adding skins or themes, does not satisfy this condition.

Regardless of whether the base game is a paid-for game or freemium game, additional content and updates that add new trophies can be paid-for or free.

A trophy group must be configured to add trophies. Trophies added by additional content or updates cannot be added to the base game group. Also, it is not possible to add trophies that can be won by playing previously released content, including the main game itself. Therefore, you cannot create an update that is only for adding trophies.

In addition, existing trophies cannot be altered or deleted using an update. If it becomes impossible to unlock trophies because of an update and you wish to change the conditions for unlocking them, contact us via "Post new issue" of Private support (<https://game.develop.playstation.net/support/>).

## Trophy Point Assignment via Additional Content or Updates

For additional content that is meant to expand the scope of gameplay, trophies of 0 to 200 trophy points can be added for each piece of paid-for additional content. When adding trophies with paid-for additional content, set up a trophy group for each piece of paid-for additional content.

For free additional content or updates, trophies of 0 to 45 points can be added for each piece of free additional content. When adding trophies with free additional content or updates, set up a trophy group for each piece of free additional content or update. It is also possible to add more trophies (up to a total of 200 points) to the last group of added trophies.

In cases where 200 points will be exceeded if a cross-platform title allows players to obtain trophies equivalent to existing additional content, it is sometimes possible to set up an additional trophy group that exceeds 200 points. If you think this condition applies to a title under development or in the planning process, contact us via "Post new issue" of Private support (<https://game.develop.playstation.net/support/>). We can discuss the possibility of additional content trophy groups. Please note that you may be asked to lower trophy grades in order to reduce the total number of trophy points.

## Platinum Link Attribute Setting

The platinum link attribute cannot be set for trophies added using additional content or an update. Set the platinum link attribute of all such added trophies to "Unlinked".

# Trophy Sets for Compilation Titles

On PlayStation®5, multiple trophy sets cannot be included in a single title due to PlayStation™Network service limitations. (For details, refer to the [PlayStation™Network Service Setup Guide - Making Service Requests](../PSN_Service_Setup-Guide/making-service-requests.html).)

Therefore, if you want to create a compilation title (remastered trilogy) that consists of a trilogy of titles, for example, the trophy set should be designed in one of the following ways. The following explanation exemplifies the creation of a remastered trilogy that consists of three titles, "Part I", "Part II", and "Part III".

## a) Create a bundle (recommended)

One method is to make a service application for each of "Part I", "Part II", and "Part III" individually and to design three independent trophy sets. By creating a "Bundle" in Content Pipeline, you can provide users with the bundle as a single title. (For details, refer to "PlayStation™Store Bundles" (<https://learn.playstation.net/bundle/policies-and-business-model-guidelines/page/PlayStationStore_Bundles.html>).) As shown below, "Part I", "Part II", and "Part III" can each have an independent trophy set, and platinum trophies can also be defined independently.

* "Part I"
  + Trophy set 1: A platinum trophy is included, which can be unlocked when "Part I" is completed
* "Part II"
  + Trophy set 2: A platinum trophy is included, which can be unlocked when "Part II" is completed
* "Part III"
  + Trophy set 3: A platinum trophy is included, which can be unlocked when "Part III" is completed

## b) Create a trophy group for each part

As shown below, another method is to create a trophy set for the remastered trilogy and to create a trophy group for each of "Part I", "Part II", and "Part III". The platinum trophy can only be defined for the part assigned to the base game group, and that part must be completed in order to earn the trophy. Put another way, the platinum trophy can be earned without having to play the other parts.

* Trophy set 1
  + Base game group
    - "Part I" trophy: Includes a platinum trophy, which can be earned when "Part I" is completed
  + Trophy group 1
    - "Part II" trophy: Does not include a platinum trophy
  + Trophy group 2
    - "Part III" trophy: Does not include a platinum trophy

When adopting this method, take notice of the upper limit of points that can be allocated to a trophy group. If the upper limit will be exceeded, consult with SIE regarding a TRC [R5013](../../../TRC/latest/TRC/R5013.html) exemption in advance via "Post new issue" of Private support (<https://game.develop.playstation.net/support/>). When doing so, please submit the list of trophies included in each trophy group together with an overview of the gameplay.

## c) Include all the trophies for each part in the base game group

As shown below, the last method is to create a trophy set for the remastered trilogy and to assign all trophies for "Part I", "Part II", and "Part III" to the base game group. Only one platinum trophy can be defined, and its unlock conditions are the completion of all of "Part I", "Part II", and "Part III".

* Trophy set 1
  + Base game group
    - "Part I", "Part II", and "Part III" trophies: A platinum trophy is included, which can be unlocked when all parts are completed

When adopting this method, take notice of the upper limit of points that can be allocated to a trophy group. If the upper limit will be exceeded, consult with SIE regarding a TRC [R5013](../../../TRC/latest/TRC/R5013.html) exemption in advance via "Post new issue" of Private support (<https://game.develop.playstation.net/support/>). When doing so, please submit the list of trophies included in each trophy group together with an overview of the gameplay.

# Upgrading the Trophy Set

Trophy sets can be upgraded. For example, trophies for additional content can be added to the trophy set of the main game, and multi-lingual support can be added to a trophy set that currently uses only the default language.

Existing trophies must not be modified when upgrading a trophy set. For example, the conditions for unlocking trophies and their difficulty cannot be changed, and trophy attributes cannot be changed or deleted. In addition, the order of existing trophies and trophy groups cannot be changed, and existing trophies and trophy groups cannot be deleted.

However, when a clear problem is found (a typo, for example), the following existing information can be changed:

* Trophy sets and trophy groups: names and icon images
* Trophies: names, details, icon images, reward names, and reward icon images

In addition, if you have created the still-image icon or name of a trophy set based on an application icon or application name, you can change the trophy set still-image icon and name of the trophy set accordingly when changes occur in the application icon and application name.

If the above information is changed, submit the changes as part of master submission. Information other than the above (for example, grades, hidden flags, and the platinum link attribute) cannot be changed.

Note: Once you have upgraded the trophy set, create new trophy configuration data, include it in an update package for your application, and release the package. Refer to the chapter "[Overview of Application Development](overview-of-application-development.html "This topic describes trophy-related processing you need to perform during the application development process.")".

## Cases in Which the Conditions for Unlocking Trophies Must Be Changed

As a general rule, trophies must be handled the same before and after application updates; players must be able to obtain the same trophy in the same event after any update.

In unavoidable circumstances such as when it becomes impossible to unlock trophies due to game design changes or their descriptions are no longer fitting, contact us via "Post new issue" of Private support (<https://game.develop.playstation.net/support/>). We can discuss changing the conditions for unlocking trophies and changing existing data.

# Notes on Designing the Trophy Set

## Conditions for Unlocking Trophies

Because trophy points earned by a user are aggregated across titles and used for display or comparison, the design of the trophy set for one title can affect the entire platform. In consideration of this fact, avoid the creation of trophies that are too simple or too complex to unlock.

Note:

Even if it is relatively easy to earn trophies compared to other titles, do not use this fact for sales promotion purposes including in the advertising of the title.

## Additional Content That Doesn't Expand Gameplay

Trophies cannot be added by additional content that only changes the appearance of the game without expanding gameplay (skins and themes, for example) .

## Unlocking Conditions for Added Trophies

For trophies added through additional content or updates, set unlocking conditions that relate to the expanded gameplay in the additional or updated content. Do not set unlocking conditions that can be met merely from the gameplay that was possible before the expansion.

## Prohibition of Viral Trophies

You cannot create trophies whose unlocking conditions require the player to interact with specific users. For example, the following are prohibited:

* A trophy that can be obtained by fighting the player of a specific account (whether an account for PlayStation™Network or an account on another platform)
* A trophy that can be obtained by fighting a player who owns a specific trophy

## Trophy Set Name and Description

Trophy information is disclosed to all users across the PlayStation™Network. Make sure configuration information of the trophy set including icons, names, and descriptions is respectful of all races, religions, ages, and genders.

## Reuse of the Trophy Set

When changing the sales channel of a game already on the market or its packaging without changing the content of the main game, you should not usually create a new trophy set. Instead, you should reuse or share the existing trophy set. This applies, for example, in the following cases:

* Selling an existing PlayStation®5 title with new packaging but without any changes to the disc content (for example, "Greatest Hits")
* Selling an existing PlayStation®5 title packaged together with free additional content or an update package (for example, a remastered package)
* Selling a game that had only been sold as a disc on the PlayStation™Store
* Selling a game in multiple territories

Note:

It is not possible to share a trophy set between the PlayStation®4 and PlayStation®5 versions of the same title. A different set of trophies must be set up for each platform.

## Earning Trophies in Games That Support Multiple Players

In games where multiple users can log in and play the game at the same time, at least one user must be able to earn trophies. Specifications where all users playing the game at the same time can earn trophies is recommended in general, but specifications such as only the user playing as a team leader being able to acquire trophies are also acceptable.

## Trophies and Cross-Platform Play/Shared Accounts

In a game that supports cross-platform play, there is no problem with enabling users to obtain trophies while playing with players on platforms other than PlayStation®5. However, "playing with a player who is not on PlayStation®5" must not be a requirement for earning the trophy.

Games that can be played on PlayStation®5 by sharing save data and account data with non-PlayStation®5 platforms and maintaining progress from those other platforms (and vice versa) can allow players to unlock trophies based on progress data on non-PlayStation®5 platforms. This means that if the conditions for unlocking a trophy are met while playing on a platform other than PlayStation®5, the trophy can be unlocked the next time the title is launched on PlayStation®5 and progress is synchronized. For details, refer to "[Retroactive Unlocking Across Platforms](retroactive-unlocking-across-platforms.html)". Note that gameplay and other actions on platforms other than PlayStation®5 must not be included in the conditions for unlocking trophies. PlayStation®5 title trophies must be obtainable only when playing on PlayStation®5.

## Trophies and Peripheral Devices

Except when required for progression in the application, trophies that can only be unlocked using a peripheral device cannot be configured in the main game. Trophies in the main game must be unlockable with just the title alone. For additional content, trophies that can only be unlocked using a peripheral device can be configured.

## Trophies and Share Play

Trophies that can only be unlocked using the Share Play feature cannot be configured.

Unlocking a trophy while the controller is passed to another player using the Share Play feature is permitted.

## Conditions for Unlocking Trophies

Events in which certain conditions are satisfied by gameplay can be set as conditions for unlocking trophies. For example, the following events are permitted as trophy unlocking conditions:

* The user collected the required amount of items
* The user cleared the required level
* The user started a specific mode (no particular operation is required before gameplay is started)
* The user completed character creation

By contrast, operations or events that aren't directly connected to gameplay cannot be set as unlocking conditions. For example, the unlocking of trophies with the following conditions is not permitted:

* The user started a game
* The user performed controller input at the title screen
* The user selected a menu item or changed settings
* A certain time passed without any user operation while the menu screen was being displayed
* The user unlocked a trophy by utilizing a social network site within the title
* The application used an independent feature provided by the system software or a library
* The user called the create controls
* The application displayed the Title Store
* The user viewed or purchased a product of the PlayStation™Store
* The user sent an invitation
* The user performed remote play
* The user used voice recognition
* The user is a PlayStation®Plus member
* The user downloaded/installed content of the PlayStation™Store

# Retroactive Unlocking Across Platforms

Although the basic idea is to unlock trophies directly based on gameplay achievements, trophies can be unlocked based on shared save data, shared online profiles, or other such data as long as it is only for the purpose of transferring the user's gameplay achievements on platforms other than PlayStation®4 or PlayStation®5 to the PlayStation®5 version of the title. Specifically, it is only possible to unlock (retroactively unlock) a trophy based on imported save data or shared online profiles between a PlayStation®5 title and a title from the PlayStation®4 or non-PlayStation® platform if all of the following conditions are met.

* Save data or an online profile is shared
* There are no differences in the trophy makeup or the unlocking conditions of specific trophies (For example, the condition "all items have been collected" will be considered the same condition only if it is the case that the number of items that must be collected is the same between the two platforms, so be careful)