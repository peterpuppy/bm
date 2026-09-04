# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/displaying-the-trophy-collection-in-the-application.html

# Game Play and the Trophy System

This topic provides an overview of the trophy system. The configuration and behavior of the system will be explained in relation to game play.

# Configuration of the Trophy System

The configuration of the trophy system is shown in the [following figure](configuration-of-the-trophy-system.html#trophy-system-overview_1_1__fd8f59e8-e267-11ee-bd3d-0242ac120002).

Configuration of the Trophy System

## The Trophy System and the Universal Data System

The trophy system is built using the features of the Universal Data System ("UDS"). UDS is a data platform that provides internal game information to various platform features.

UDS tabulates and accumulates information from UDS events as UDS Stats, with applications posting these events based on users' gameplay. For example: if an application posts score information every time a stage is cleared, the UDS can use it to calculate high scores; and if the application posts the number of defeated enemies every time enemies are defeated, the UDS can calculate the cumulative total number of enemies defeated. In-game progress and status information accumulated as UDS Stats can be used with various platform features, including the trophy system.

The trophy system references UDS Stats information as conditions for unlocking trophies. The developer defines the conditions that must be met to earn a trophy, for example "a high score of at least a certain value" or "a cumulative number of enemies defeated that is at least a certain value". The trophy system compares UDS Stats information with these conditions and automatically unlocks trophies when the UDS Stats meet those conditions. Additionally, the trophy system uses UDS Stats to calculate the remaining progress required to unlock a trophy. For example, the trophy system would refer to the UDS Stat representing the cumulative number of defeated enemies to calculate the number of enemies the player must still defeat before they earn a trophy.

Developers can configure trophy unlocking conditions based on UDS Stats using either of the following two methods:

**Quick Configuration**

The quick configuration method defines trophy-specific UDS Stats. While this provides the benefit of being easy to deal with because you can define UDS Stats without considering platform features other than the trophy system, you must be aware that there are downsides: the application must post UDS events that are only for unlocking trophies and it is difficult to use UDS Stats with other platform features.

The quick configuration method can be useful if trophy unlocking conditions are complex and hard to express in terms of UDS Stats. In this case, you could define a UDS Stat that indicates "whether this trophy can be unlocked or not". The application must then contain the logic that determines whether the unlocking condition has been met based on gameplay results. When the condition is met, the application posts a UDS event saying that the trophy can be unlocked. Similarly, if calculating the progress toward a trophy is complex, you could define a UDS Stat that indicates only the rate of completion, which must then be calculated and posted by the application. In addition to cases in which unlocking conditions and progress are complex, this method may be useful when porting titles that use the "Trophy Unlock API" provided by the old trophy system.

To make it easier to define UDS Stats when using this method, a mechanism is available for automatically generating UDS Stat definitions from trophy definitions. UDS Stats for both progressive and non-progressive trophies can be defined. Automatically generated UDS Stats are also reflected in the UDS Management Tool. However, these UDS Stat definitions cannot be modified or used with other platform features. Additionally, you must send UDS events in a pre-determined format to update the UDS Stats that have been automatically generated with this method. Refer to the "[Implementation of Trophy-Unlocking](implementation-of-trophy-unlocking.html)" section for details.

**Advanced Configuration**

With this method, you follow the standard UDS workflow and define the player's in-game states as UDS Stats at the start. You then reference those UDS Stats to define trophies. Defining UDS Stats ahead of time with the intention of using them with various platform features makes supporting additional platform features easy and can help you utilize the full potential of UDS. With UDS Stats defined originally for trophies, you would later be able to use the same UDS Stats with other platform features, and you would be able to use existing data with future extensions to UDS-based platform features.

Another benefit of this method is that the application no longer needs to perform processing that only unlocks trophies. For example, if you use one UDS Stat linked both to displaying Game Stats and to a trophy unlocking condition, you can simply post a single UDS event to update the UDS Stat and thereby simultaneously display information on the user's profile and unlock a trophy.

## Trophy Configuration File

Trophy configuration data consists of attributes for each trophy, such as its grade, unlocking condition, trophy images, names, and descriptions, as well as group and trophy set images and names. This trophy configuration data is eventually included in the application package as a trophy configuration file, which is installed on the console. In the development environment, before the package is created, you must place the trophy configuration file in the appropriate directory before launching the application.

Because the trophy system has multi-lingual support, you can include trophy configuration data in multiple languages. The data specifications for trophy configuration data, how to create the trophy configuration file, and where to place the file during development will be explained later in this document.

## UDS Configuration File

To use UDS Stats, a UDS configuration file that defines update conditions and attributes is required. Like the trophy configuration file, the UDS configuration file is eventually included in an application package and installed on a console. In the development environment, before the package is created, you must place the UDS configuration file in the appropriate directory before launching the application.

How to set up UDS and where to place UDS-related files during development to enable the use of trophies will be explained later in this document. (Refer to the "[Overview of Application Development](overview-of-application-development.html "This topic describes trophy-related processing you need to perform during the application development process.")" chapter.)

## NpTrophy2 Library

The NpTrophy2 library provides functions that allow applications to obtain trophy configuration data and trophy records. Because functions for unlocking trophies are not included, it is not necessary to use the NpTrophy2 library if there is no need to use trophy configuration data or records within the application.

## NpUniversalDataSystem Library

The NpUniversalDataSystem library provides features that allow applications to post UDS events. Because trophies are unlocked when the posted aggregated UDS events fulfill the trophy unlocking conditions, an application that supports trophies must use the NpUniversalDataSystem library.

## S2S Web API

The S2S Web API is a Web API used by application servers/back-office servers to obtain trophy configuration data and trophy records. Refer to the [Trophy2 Web API Overview](../../../WebAPI/latest/Trophy2_WebAPI-Overview/__document_toc.html) and [Trophy2 Web API Reference](../../../WebAPI/latest/Trophy2_WebAPI-Reference/__document_toc.html) documents for details.

# Installation of Trophy Configuration Data

For applications supporting the trophy system, you must create a trophy configuration file that defines the trophy configuration data and include it in a disc or package in the appropriate manner. The trophy configuration data is automatically installed by the system software in the console storage before the application is launched.

The trophy configuration file must be placed in the appropriate directory when launching the application from the debugger or workspace during development. In this case, trophy configuration data will be installed when the application first calls `sceNpTrophy2RegisterContext()` or `sceNpUniversalDataSystemRegisterContext()` after its launch.

Trophy configuration data installed on the internal SSD is shared among all users.

# Installing the Trophy Record

The trophy configuration data is automatically installed and shared among users, whereas the trophy records are created in the console storage for each user by calling `sceNpTrophy2RegisterContext()` or `sceNpUniversalDataSystemRegisterContext()`.

# Displaying the Trophy Collection in the Application

The following functions are available for displaying the user's trophy collection in the application. These functions are used to obtain the installed trophy configuration data and the user's trophy record.

* `sceNpTrophy2GetGameInfo()`
* `sceNpTrophy2GetGroupInfo()`
* `sceNpTrophy2GetGroupInfoArray()`
* `sceNpTrophy2GetTrophyInfo()`
* `sceNpTrophy2GetTrophyInfoArray()`

The application will be able to display the user's trophy collection based on the information obtained with these functions.

Note:

Trophy records are managed by the trophy system. Always use the above functions to obtain the data as necessary, and do not save this information in the application as save data, for example.

# Unlocking Trophies

Use `sceNpUniversalDataSystemPostEvent()` to post UDS events based on the user's gameplay. When a UDS event that fulfills a preset update condition is posted, the UDS Stat is updated. Whenever the UDS Stat enters a state in which it meets the trophy unlocking condition, the trophy is automatically unlocked.

## Trophy Unlocking Conditions and UDS Stats

With the exception of platinum trophies, each trophy is linked to a single UDS Stat. When a UDS Stat is updated, the trophy system compares and evaluates the new value against the trophy unlocking condition and unlocks the trophy if the condition is met. For details about the UDS Stats that can be used, refer to "[Appendix B: UDS Stats That Can Be Used as Trophy Unlocking Conditions](appendix-b-uds-stats-that-can-be-used-as-trophy-unlocking-co.html)".

**Non-Progressive Trophies**

Non-progressive trophies have states: unlocked and locked. For non-progressive trophies, there is no information indicating how much more progress is required to unlock a trophy that is locked. Non-progressive trophies will be unlocked when the value of the linked UDS Stat satisfies the trophy unlocking condition. The unlocking condition will be one of the following:

* The UDS Stat value is equal to or greater than the target value
* The UDS Stat value is greater than the target value
* The UDS Stat value is equal to or less than the target value
* The UDS Stat value is less than the target value

**Progressive Trophies**

Progressive trophies have information that indicates how much more progress is required to unlock a trophy that is locked. To define a progressive trophy, its unlocking condition must be "the UDS Stat value is equal to or greater than the target value".

The value of the linked UDS Stat for such a trophy indicates the current progress, and the trophy will be unlocked when the target value is reached.

Be aware that the system software always displays progress based on the user's best score for a progressive trophy.

Because the system software retains the best scores, progress values will not be reset even if UDS Stats have been reset, for example, because the user loaded old save data or restarted a game by selecting "New Game". Therefore, a higher progress value than what would be typically expected, compared to the in-game state, may be displayed. However, this is the same as how, once earned, a trophy never returns to being unearned; a progress value that has been reached not being rolled back follows the same logic.

It is recommended that displaying of progress be enabled even when UDS Stats relating to progress have been reset.

**Notes About Using UDS Stats for Individual Playthroughs (Instances of Save Data)**

Currently, the UDS Stats system cannot tabulate a UDS Stat for individual playthroughs (instances of save data). Thus, if, for example, you were to make a trophy unlocking condition along the lines of "collect specific items during a single playthrough", you would have to do the following:

* Set the Aggregation of the UDS Stat to Latest
* Retain the data recorded for the Stat in save data
* Update the stat when save data is read or when a new playthrough is started

When Count or Sum is set for its Aggregation, a Stat is always tabulated at the account level, and it is thus not possible to reset the value at the required times.

Even in a game that does not create multiple instances of save data, the need would arise to reset the Stat when the save data was deleted by the user or overwritten with save data from online storage; therefore, the steps described above would still be necessary.

For details about Aggregation, refer to [Universal Data System Guide - UDS Data Model - UDS Stats](../Universal_Data_System-Guide/uds-stats.html).

## Conditions for Earning Platinum Trophies

The trophy set of a normal game includes one special trophy called the "platinum trophy". Unlike other trophies, the platinum trophy is not directly linked to a UDS Stat. It is automatically earned when the user earns all the other trophies in the trophy set.

Specifically, every time a trophy is unlocked, the trophy system checks to see if the user has earned all the trophies required to earn the platinum trophy. If all of them have been earned, the trophy system unlocks the platinum trophy.

# Display of the Trophy Collection in the System Software

The display of trophy collections in the system software has two modes: Online Mode and Offline Mode. Online Mode references and displays trophy configuration data and trophy records that are on the trophy server. Offline Mode references and displays trophy configuration data and trophy records that are installed on the console. For details about each mode, refer to the "[Debugging Support Provided by the System Software](debugging-support-provided-by-the-system-software.html "This topic describes the debugging support features provided by the system software that are related to trophies.")" chapter.

Images of trophies that have not yet been earned are marked as unearned. The application can specify whether to show or hide the name and details of trophies that have not yet been earned.