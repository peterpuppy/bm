# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/uds-stats.html

# UDS Data Model

UDS standardizes data required by each platform feature and defines it in the UDS data model. By doing so, it prevents the duplication of data received from a game application and realizes single input multi-use. A UDS data model is composed of a PlayStation™Network object and a UDS event (feature event).

The following figure shows the layout of the UDS Data Model.

UDS Data Model

# Example Scenario

This topic provides an example of a game application sending information to a player using PlayStation™Network objects.

The following figure shows an example scenario of a game sending the `startMission` event when the player starts "Tutorial".

Example Scenario

# Relationships Between Platform Features and UDS Data Models

This topic shows the relationship between platform features and associated UDS data models.

Relationships Between Platform Features and UDS Data Models

|  | **Data Model** | |
| --- | --- | --- |
| **Platform Feature** | **PlayStation™Network Object** | **UDS Event (Feature Event)** |
| Trophy | Required | Required |
| Game Help | Required | Required |
| Matches | Required | Not required |
| Media Auto-Tagging | Required | Required |
| Spoiler Block | Required | Required |

# PlayStation™Network Objects

PlayStation™Network objects represent static information used in a game such as the
story's missions and locations. A game can use feature events associated with PlayStation™Network
objects to send an in-game event or player activity to the platform.

The following
table describes PlayStation™Network objects.

PlayStation™Network Objects

| **Object Type** | **Description** | Package for Release |
| --- | --- | --- |
| `activity` | A mission, task, goal, chapter, quest, game mode, level, etc. that can be played by the player. Activity is also used as a "Match" definition for multi-player game matches. For details, refer to the [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html). | Required |
| `subCategory` | Classification of activity. Up to 64 subcategories can be defined. | Required |
| `zone` | A place (zone) that the player is or can be. | Required |
| `mechanic` | An item, ability, skill or effect that can be used by the player or the game to impact gameplay (e.g. bow, arrow, stealth attack, fire damage). | Required |
| `actor` | An entity with behaviors in the game. Can be player-controlled or game-controlled, and this can change dynamically during gameplay. | Required |
| `tournament` | An online game event that you can configure. | Not Required |
| `subCategoryForTournament` | Classification of the tournament. Up to 64 subcategories can be defined. | Not Required |

Note:

If `Package for Release` is `Required`, the object must prepare a package for release. If it's `Not Required`, the object can be published without a package. See [Preparing a Package for Release](preparing-a-package-for-release.html "This topic covers the procedure for preparing a release package.") for details.

PlayStation™Network objects are defined according to the needs of platform features,
and object types are added in the future according to platform feature extensions.
There are no PlayStation™Network objects that can be freely customized by game developers
and there are also no plans to provide such PlayStation™Network objects in the future.
Up to 2,560 activity objects can be defined and 512 zone, mechanic and actor objects
can be defined.

Note:

In order to add activities, zones, actors or mechanics to your game after release,
you will need to release a game patch to include the new object definitions in the
npconfig.zip file. You can do this with a delta patch, using the Rapid Patch process,
which is fully automatable with the exception of the manual step required for the
liability form signature. If the package validation checks pass, this process is expected
to complete in a few hours, after submission.

For instructions on configuring PlayStation™Network objects, see [Configuring Objects](configuring-the-uds-data-model.html#topic315301_5_7__configuring-objects_html).

# UDS Events

UDS events are used to track game progress and a player's actions in the game. For example, these include game state management, trophy unlocking, data set of Game Help for machine learning, etc. Up to 512 UDS events can be defined.

There are two types of UDS events:

* Feature events.
* Custom events.

## Feature Event

A feature event represents the main actions of a player in a game. The event type
and properties for the feature event are defined in advance, and are sent by a game
application based on a player's action. There are required properties and optional
properties. If required, you can define custom properties to add additional information
to a feature event. The following figure shows the general layout of a feature event.

Feature Event

The following table describes defined event types.

Defined Event Types

| **Event Type** | **Description** |
| --- | --- |
| `activityStart` | The event indicates that the player started an activity. |
| `activityEnd` | The event indicates that the player ended an activity. |
| `activityAvailabilityChange` | The event indicates that an activity or activities became playable/unplayable. |
| `activityPriorityChange` | The event is used for setting a priority value for an activity. This event is not used by the system at this time. |
| `activityResume` | This event can be used to resume an activity by specifying the status of its tasks and sub-tasks. |
| `activityTerminate` | The event can be used to clear all activities in the *In-Progress* state. |
| `locationChange` | The event indicates that the player changed the zone/location. |
| `mechanicUse` | The event indicates that the player used the mechanic. |
| `mechanicUseBy` | The event indicates that a mechanic has been used by the game (e.g. a non-player character). |
| `mechanicImpact` | The event indicates that a mechanic that the player used had an impact on gameplay. |
| `mechanicImpactBy` | The event indicates that a mechanic used by the game (e.g. a non-player character) had an impact on gameplay. |
| `mechanicMitigate` | The event indicates that the player effectively used a mechanic to mitigate a mechanic used by the game on the player. |
| `mechanicAvailabilityChange` | The event indicates that the mechanics are available to the player. Available means that the mechanic is available in the game for the player to use, but may require the player to go through some steps to acquire it into inventory (e.g. buy from a shop) before using it. |
| `mechanicInventoryChange` | The event indicates that the player's inventory has changed. |
| `mechanicLoadoutChange` | The event indicates that the player's loadout has changed. |
| `actorChange` | The event indicates that the player's actor(s) have changed. |

## Custom Event

This event is freely customizable. Game applications send it according to the player's
action. Use the custom event to post updates to UDS Stats that cannot be sent using
feature events. The following figure shows the layout of a custom event.

Custom Event

For instructions on configuring UDS events, see [Configuring Events](configuring-the-uds-data-model.html#topic315301_5_7__configuring-events).

# UDS Stats

UDS Stats is a scheme for extracting and aggregating information from UDS events that are sent by a game application and for storing the information as statistics. UDS Stats data are used by various platform features.

The UDS Stats concept is shown in the following figure.

UDS Stats Concept

For example, let us assume you want to aggregate the best times in a racing game.
In this case, design the game to post a UDS event containing time information when
a race completes in the game. You can configure UDS Stats to aggregate the minimum
time value for each race. Given the two, you can aggregate the best race times. In
addition, you can use UDS Stats for various purposes such as for storing match records
of a player versus player game, and for storing the number of defeated opponents in
a RPG game.

## Extraction and Aggregation

Extraction refers to extracting information from UDS events to send to UDS Stats.
Aggregation refers to the method applied when entering information to UDS Stats. The
following figure shows extraction and aggregation.

Extraction and Aggregation

## Stats Components (Stats Definition)

UDS Stats is a collection of data units called "stat". Each stat has components. The definition of UDS Stats is called Stats Definition.

Up to 1512 stats can be defined per service label (you can define 512 max stats as
custom stats, and you can define 1000 max auto-generated stats for Trophy). Note that
a title uses a single service label. The following table describes UDS Stats components.

UDS Stats Components

| **Item** | **Description** |
| --- | --- |
| Stat Name | Name of each stat. The stat name is a string of 1 to 64 characters comprising alphanumeric characters with an "`_`" (underscore) and a "`-`" (hyphen). Names starting with an "`_`" (underscore) are reserved for the system and cannot be used. |
| Stat ID | ID of each stat. Automatically assigned by the system when a stat is configured. |
| Data Type | Data type of each stat. The following data types can be used:   * Int32 * Int64 * Uint32 (Unsigned Int32) * Uint64 (Unsigned Int64) * Float32 * Float64 |
| Aggregation | Aggregation method of each stat:   * Latest: Use the value with the latest update time. When the system cannot obtain the   correct time information, the value of latest stat is not updated. For example, the   value before the time when the console accesses the PlayStation™Network for the first   time. * Max: Use the maximum value. * Min: Use the minimum value. * Sum: Add the values entered in stat. When the sum value exceeds the maximum value   or minimum value of data type, the value is clamped to the maximum value/minimum value   (no overflow). * Count: counter that counts up starting from 0 up to the maximum value of Uint64.   Aggregation methods that can be specified for data types are:   * For Int32: Latest, Max, Min * For Int64: Latest, Max, Min * For Uint32: Latest, Max, Min, Sum * For Uint64: Latest, Max, Min, Sum, Count * For Float32: Latest, Max, Min * For Float64: Latest, Max, Min  Note: The initial value is the target of the aggregation process. For example, if you set   "100" as the initial value of a stat and its aggregation as "max", the stats value put in that stat is compared to 100. |
| Max Value | Maximum value of each stat. This value is set, for example, when the maximum number of golds that can be carried by a player in a game is 9999. It can only be set when the Data Type is Int32, Int64, Uint32, Uint64, Float32, or Float64, and you can specify it within the range of the maximum value and minimum value of each Data Type. |
| Min Value | Minimum value of each stat. This value is set, for example, when the number of golds that can be carried by a player in a game does not go below 0. It can only be set when the Data Type is Int32, Int64, Uint32, Uint64, Float32, or Float64, and can be specified within the range of the maximum value and minimum value of each Data Type. |
| Initial Value | An initial value can be set to stat. For example, when you want to represent a character's level using stats, set 1 if the initial value is 1. When you do not explicitly make a setting, the initial value is 0 when the data type is Int32, Int64, Uint32, Uint64, Float32, Float64. |

Note:

Using Float32 or Float64 may give you unexpected results.

The following figure shows an example stats definition.

Stats Definition Example

## Stats Extraction

Stats Extraction is a rule for extracting information from UDS events to send to UDS
Stats.

Each rule has a condition and an action. An action only activates when a condition
is satisfied. Up to 3048 rules can be set (you can set max 2048 rules for custom stats,
and you can set max 1000 auto-generated rules for Trophy). The following figure shows
an example of stats extraction.

Stats Extraction

## Condition

The following items can be set as a condition:

**eventName Value of a UDS Event**

This is a required setting item. Select the `eventName` for the condition that triggers aggregation.

**Value of a Specific Event Property of a UDS Event**

This is an optional setting item. The following operators can be specified as a comparison
operator:

* `==` … Equal
* `!=` … Not equal
* `<=` … Equal to or less than
* `<` … Less than
* `>` … Greater than
* `>=` … Equal to or greater than

The Property Data Type of a UDS event that each comparison operator can apply is defined
as follows:

* When it cannot be applied, it is handled as if that Condition was not satisfied.

  `==`, `!=` … Int32, Int64, Uint32, Uint64, Float32, Float64, String, boolean

  `<`, `<=`, `>`, `>=` … Int32, Int64, Uint32, Uint64, Float32, Float64
* When an event property condition is set in addition to an `eventName` condition, the action is executed when both conditions are satisfied.

For example, let us assume you want to execute an action when a stage is cleared.
In this case, program your application so that an event with `eventName` as "stageClear" is posted. In addition, use the UDS Management Tool and set the condition of `eventName` as "stageClear".

In another example, let us assume you want to execute an action when stage "A" is cleared. In this case, program your application so that an event with `eventName` as "stageClear" and containing "stage": "A" as a property is posted. In addition, use the UDS Management Tool and set the condition
of `eventName` as "stageClear", set the condition of `eventProperty` as the `propertyName` being "stage", the value "A", and the comparison operator "==".

## Action

This sets which property value (input) of a UDS event to input to which stat (output).

Further, when aggregation is "count", there is no need to specify input.

For example, when you want to input a race game's lap time to UDS Stats, define a
stat with stat name `latestLapTime` to properties of a UDS event with the property name "lapTime". Then, set "lapTime" as the input for the action and set "latestLapTime" as the output for the action.

## Scope of Stats

UDS Stats can be set per service label, and data is stored per service label and per
user. The following figure shows a diagram of the scope of stats.

Scope of Stats

## Behavior Online and Offline

When the console is offline, UDS Stats are stored on the console by the system software.
Synchronization processing is carried with the server and other consoles when the
console goes online again. Synchronization processing is carried out periodically
when the console is online. The following figure shows behavior online and offline.

Behavior Online and Offline

For instructions on configuring stats, see [Configuring Stats](configuring-the-uds-data-model.html#topic315301_5_7__configuring-stats).

## Revision Management and Backward Compatibility

Stats definition and stats extraction have revisions. The version is incremented every
time there is an update. When you want to change the configuration of the stats definition
in the development environment, the stat value of a stat for which a change was made
that doesn't have backward compatibility (for example, changing the data type) is
not inherited upon a revision change. For a detailed explanation on when each stat
value does not match the latest configuration, refer to the [Synchronization with the Server and Other Consoles](uds-stats.html#topic315301_4_5__synchronization-with-the-server-and-other-consoles_html) section.

## Synchronization with the Server and Other Consoles

Because configuration changes that do not maintain backward compatibility is possible
in the development environment, each stat value may not match the latest configuration.
Such a state is called a conflict; the following cases are possible:

* Data type doesn't match.
* The limit is exceeded.
* Aggregation is the latest, but there is no time information.

When the system detects a conflict state, it removes the console with that stat as
a synchronization target. The following figure shows a diagram of synchronization
exclusion due to a conflict.

Synchronization Exclusion Because of a Conflict

**Synchronization Timing**

The synchronization timing is automatically controlled by the system.

# UDS State

UDS State is a scheme to track the player's in-game actions (for example, the activities the player has ever played, the zone the player is currently in, etc.).

The PlayStation™Network object is extracted from the UDS event sent from a game and stored
to the state according to predefined rules. This information can then be utilized to
provide helpful information and tips to the player in a game and to realize platform
features such as "Spoiler Block".

UDS State is realized using the stats scheme. The difference from stats is configuration.
Because state is automatically tracked by the system software, there is no need for
the game developer to perform configuration for state.

## Behavior Online and Offline

Like stats, when the console is offline, data is stored on the console by the system
software and synchronization is performed with the server and other consoles when
the console goes online again. Synchronization processing is periodically carried
out when the console is online.

## UDS State Management

UDS States tracked by the platform are as follows:

**Activity**

The following table describes activity states.

Activity States

| **Activity State** | **Description** |
| --- | --- |
| Ever Played Activities | All the activities that the player ever started or ended is stored. |
| Ever Completed Activities | Activities that the player successfully ended is stored. |
| Available Activities | Activities that the player can play is stored. |
| Unavailable Activities | Activities that the player cannot play is stored. |
| Ever Available Activities | All the activities that ever become available is stored. |
| Ever Unavailable Activities | All the activities that ever become unavailable is stored. |

Note:

An activity started or ended by the Matches Web API is stored as Ever Played Activities
only.

**Mechanic**

The following table shows mechanic states.

Mechanic States

| **Mechanic State** | **Description** |
| --- | --- |
| Latest Equipped Mechanics | The latest mechanics loadout. |
| Latest Inventory Mechanics | The latest mechanics in the inventory. |
| Available Mechanics | Mechanics that are available for the player. |
| Unavailable Mechanics | Mechanics that are unavailable for the player. |
| Ever Used Mechanics | All the mechanics that the player has ever used. |
| Ever Seen Mechanics | All the mechanics that the player has ever seen (including the player has ever used). |

**Actor**

The following table shows actor states.

Actor States

| **Actor State** | **Description** |
| --- | --- |
| Latest Primary Actor | The actor that the player recently selected. |
| Latest Secondary Actors | The secondary actors that player recently selected. |
| Ever Selected Actors | The actors the player has ever selected. |
| Ever Seen Actors | The actors the player has ever seen in the game. |

**Zone**

The following table shows zone states.

Zone States

| **Zone State** | **Description** |
| --- | --- |
| Latest Zone | The zone that the player most recently visited is stored. |
| Ever Been Zones | All zones that the player ever visited is stored. |