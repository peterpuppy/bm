# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/reference-materials.html

# The Matchmaking Service

# Purpose and Characteristics

The Matchmaking service for PlayStation™Network searches for other players against whom to play online multiplayer gameplay. Because the service is provided as part of the Session Manager service, it is available if a request to use the Session Manager service has been completed. The service operates in tandem with Game Sessions of the Session Manager service; players who undergo matchmaking by the Matchmaking service and are matched with one another are eventually made to join the same Game Session.

Use of the Matchmaking service can be thought about divided into two phases: initial preparation by the developer and processing by the application.

During the initial preparation phase, developers use the "Matchmaking Tool" to define "rulesets" and register them to the server. A ruleset sets up conditions used during the selection of players against whom to play, such as how many players will be playing and how close in skill level the players are required to be. It is possible to define multiple rulesets corresponding to each game mode that the application has, for example, a two-player competition mode and a four-player competition mode.

The application creates a "matchmaking ticket" that includes, along with a specification of a ruleset, information required for matchmaking - such as the player's skill level - and uses the Matchmaking Web API to submit a matchmaking request to the server. The server compares the tickets submitted by multiple players against one another in accordance with the ruleset. When a suitable combination of tickets is found, the server creates a Game Session, puts all players included in those tickets in reserved-to-join status, and issues a Push notification ("matchmaking offer") to the application. The application that receives the offer has the players join the Game Session and initiates gameplay with each player together with the others.

# Sample Program

A sample program using the Matchmaking Web API is provided below. Refer to [Sample Program Overview](../../../SDK/latest/Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

## sample\_code/playstation\_network/api\_webapi\_matchmaking

This sample exemplifies basic usage of the Matchmaking Web API.

# Reference Materials

The Sandbox network architecture has been newly implemented for the PlayStation® environments. Refer to this technote for details: <https://game.develop.playstation.net/technotes/view/740>.

Refer to the following documents for an overview of the Sandbox network architecture, how to use it, and how to migrate to it.

* [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html)
* [NP Service Config User's Guide](../../../SDK/latest/NP_Service_Config-Users_Guide/__document_toc.html)

For common rules for Web APIs, how to use them, and so forth, refer to the following document:

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

For how to use Web APIs with applications for PlayStation®5, refer to the following documents:

* [NpWebApi2 Library Overview](../../../SDK/latest/NpWebApi2-Overview/__document_toc.html)
* [NpCppWebApi Library Overview](../../../SDK/latest/NpCppWebApi-Overview/__document_toc.html)

For information concerning the operation of Game Sessions, refer to the following documents:

* [Session Manager Service Overview](../../../SDK/latest/Session_Manager_Service-Overview/__document_toc.html)
* [Session Manager Web API Overview](../Session_Manager_WebAPI-Overview/__document_toc.html)

For how to use the NpSessionSignaling library, refer to the following documents:

* [NpSessionSignaling Library Overview](../../../SDK/latest/NpSessionSignaling-Overview/__document_toc.html)
* [NpSessionSignaling Library Reference](../../../SDK/latest/NpSessionSignaling-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Matchmaking Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Matchmaking_WebAPI-ReleaseNotes.html)