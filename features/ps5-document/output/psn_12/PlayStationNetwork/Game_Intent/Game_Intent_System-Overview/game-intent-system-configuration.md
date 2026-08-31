# Game Intent System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Game_Intent_System-Overview/game-intent-system-configuration.html

# Game Intent System Configuration

This topic describes what game intent events are and the features and services that use game intent events.

## About Game Intent Events

The game intent system is a general scheme for notifying an application about information that directly leads a user to a specific scene in the application from various system software features or PlayStation™Network services.

The game intent system can be used for various purposes: for example, for joining a session and for starting a challenge activity. When a user operates the system software screen to join a session or to start a challenge activity, the system notifies the application of the event and passes information about the session, scene, character, etc. The application can immediately lead the user to a specific scene or state by performing the required processing based on the passed information.

Overall Flow of the Game Intent System

## Features and Services Using the Game Intent System

The following features and services use the game intent system:

* Joining a Player Session
* Joining an invitation
* Starting a challenge activity
* Starting a tournament match

For details about game intent events that support these features and services, refer to "[Game Intent Event Types and Properties](game-intent-event-types-and-properties.html "This topic describes the types of game intent events and the properties that are fixed for each type. In addition, an explanation regarding the processing to carry out after receiving a game intent event for each game intent event type is provided, along with other information.")".