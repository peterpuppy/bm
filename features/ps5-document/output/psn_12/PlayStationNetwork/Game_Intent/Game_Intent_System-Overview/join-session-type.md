# Game Intent System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Game_Intent_System-Overview/join-session-type.html

# Game Intent Event Types and Properties

This topic describes the types of game intent events and the properties that are fixed for each type. In addition, an explanation regarding the processing to carry out after receiving a game intent event for each game intent event type is provided, along with other information.

There are various types of game intent events with properties that are fixed for each type. The type, property names, and property values will be passed to an application as strings in the designated format. An application can specify in advance the types of game intent events it wants to receive. The processing to be carried out by an application when it receives game intent information is determined for each game intent event type.

Game intent event types are defined across features and services so that the parameters for jumping into a specific scene in an application can be commonly used as much as possible. Note that a specific type of game intent event may not completely correspond to a specific system software feature or to a user experience one to one.

Game intent types that are currently available are defined as follows:

* [Game Intent Events of the Join Session Type](join-session-type.html "This topic provides details about the properties of the Join Session type and the processing that should be performed by the application after receiving a game intent event of this type, along with other information.")
* [Game Intent Events of the Launch Activity Type](launch-activity-type.html "This topic provides details about the properties of the Launch Activity type and the processing that should be performed by the application after receiving a game intent event of this type, along with other information.")
* [Game Intent Events of the Launch Tournament Match Type](launch-tournament-match-type.html "This topic provides details about the properties of the Launch Tournament Match type and the processing that should be performed by the application after receiving a game intent event of this type, along with other information.")

# Game Intent Events of the Join Session Type

This topic provides details about the properties of the Join Session type and the processing that should be performed by the application after receiving a game intent event of this type, along with other information.

## Game Intent Event of the Join Session Type

This game intent event represents joining a session.

## Type String

`joinSession`

## Properties

| **Name** | **Value** | **Maximum value size (including the NULL terminator)** | **Description** |
| --- | --- | --- | --- |
| `playerSessionId` | Session ID string | 37 bytes | Player Session ID |
| `memberType` | "`player`" or "`spectator`" | 17 bytes | Member type |

## Processing After Receiving Game Intent Information

Perform processing using the Session Manager Web API to join the Player Session specified with the `playerSessionId` property as the type of member specified with the `memberType` property.

Refer to the explanation of Player Sessions in [Session Manager Service Overview - Usage Guides - Using Player Sessions](../Session_Manager_Service-Overview/using-player-sessions.html) for details about the processing to join a Player Session.

## Related System Software Features

A game intent event of the Join Session type is used from the following system software features:

* Joining a session from a Player Session invitation notification or the details screen for the invitation
* Joining a Player Session from session information displayed in the Control Center or elsewhere

## Test Procedure Overview

A game intent event can be received by using the Session Manager Web API to create a Player Session and performing operations such as the following:

* Joining a session from a Player Session invitation notification or the details screen for the invitation
* Joining a Player Session from session information displayed in the Control Center or elsewhere

## Sample Program

Refer to the following sample program that features the Join Session game intent event type. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

* Session Manager Web API sample (sample\_code/playstation\_network/api\_webapi\_session\_manager)

# Game Intent Events of the Launch Activity Type

This topic provides details about the properties of the Launch Activity type and the processing that should be performed by the application after receiving a game intent event of this type, along with other information.

## Game Intent Event of the Launch Activity Type

This game intent event represents launching a challenge activity.

## Type String

`launchActivity`

## Properties

| **Name** | **Value** | **Maximum value size (including the NULL terminator)** | **Description** |
| --- | --- | --- | --- |
| `activityId` | Activity ID string | 33 bytes | Activity ID |

## Processing After Receiving Game Intent Information

Perform the processing to launch the activity specified with the `activityId` property using the NpUniversalDataSystem library.

For details about the processing to launch an activity, refer to the explanation of activities in [Universal Data System Guide - UDS Data Model - PlayStation™Network Objects](../Universal_Data_System-Guide/psn-objects.html).

## Related System Software Features

A game intent event of the Launch Activity type is used from the following system software features:

* Launching a challenge activity from "★Debug Settings" > "PlayStation Network" > "Show Activity Configuration" (Development Kit/Testing Kit only)
* Launching a challenge activity from an activity card displayed in Control Center or elsewhere in the system software

For information about the "Show Activity Configuration" feature, refer to "[Debugging Support for Developing Game Intent-Compatible Applications](debugging-support-using-the-system-software.html "This topic describes the debugging feature provided by the system software for supporting the development of game intent-compatible applications.")".

## Test Procedure Overview

A game intent event can be received by using the Universal Data System Management Tool to create a challenge activity and performing the operations to launch the challenge activity from the system software screen.

For details about the Universal Data System Management Tool, refer to [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html).

# Game Intent Events of the Launch Tournament Match Type

This topic provides details about the properties of the Launch Tournament Match type and the processing that should be performed by the application after receiving a game intent event of this type, along with other information.

## Game Intent of the Launch Tournament Match Type

This game intent event represents launching a tournament match.

## Type String

`launchTournamentMatch`

## Properties

| **Name** | **Value** | **Maximum value size (including the NULL terminator)** | **Description** |
| --- | --- | --- | --- |
| `activityId` | Activity ID string | 33 bytes | Activity ID |
| `matchId` | Match ID string | 37 bytes | Match ID |

## Processing After Receiving Game Intent Information

The system launches the activity corresponding to the `activityId` property and creates a match corresponding to the activity. Perform processing to join the match specified with the `matchId` property.

For the details of the processing for joining a match, refer to [Matches Web API Overview - Using the Web API](../../../WebAPI/latest/Matches_WebAPI-Overview/using-the-web-api.html).

## Related System Software Features

A game intent event of the Launch Tournament Match type is used from the following system software features:

* Joining a tournament from "Join Now" within the debug UI found in "★Debug Settings" > "PlayStation Network" > "Tournaments" (Development Kit/Testing Kit only)
* Joining a tournament from a tournament activity card displayed in Control Center or elsewhere in the system software

For information about the "Tournaments" screen mentioned above, refer to [PlayStation™Network Tournaments System Overview - Configuring Tournaments - Testing Using the Debug UI](../PSN_Tournaments_System-Overview/testing-using-the-debug-ui.html).

## Test Procedure Overview

A game intent event can be received by using the Universal Data System Management Tool to create an activity that supports tournaments and performing the "Join Now" operation from the debug UI found in "★Debug Settings" > "PlayStation Network" > "Tournaments".

For details about the Universal Data System Management Tool, refer to [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html).

## Sample Program

Refer to the following sample program that features the Launch Tournament Match game intent event type. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

* Tournament Match Sample
* (sample\_code/playstation\_network/api\_tournament\_match)