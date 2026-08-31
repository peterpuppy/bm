# PlayStation™Network Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN-Overview/online-multiplayer.html

# Multiplayer Platform

The Multiplayer Platform is an interconnected set of features and services that improves the experience of players and developers of multiplayer games. When used in its entirety, the Multiplayer Platform creates a cohesive experience from discovery of multiplayer play opportunities all the way to completing gameplay objectives.

The Multiplayer Platform provides the following main features:

* **Online Multiplayer** helps game developers to create games that find and facilitate real time groupings of players and enables the core communication paths between them. When used, multiplayer groupings appear throughout the console experience, bringing players together and allowing players to manage their play experience. It also enables you to send data between players and to set up system backed voice chat channels.
* **Game Intent** enables players to transition from the system to the game's context in the fastest way possible. It uses information about the game that is provided by Session Manager, Events, and the Data Platform.
* **Advanced Player Profile** is a common record of gameplay data that can be accessed by titles in real time and aggregated across the platform.

# Online Multiplayer

This topic provides information on APIs and libraries related to developing
multiplayer experiences.

The PlayStation™Network provides a session server to create and share the following information for online sessions:

* Session name (lobby name, room name, map name).
* Metadata required for joining or referencing the session (such as the session ID from the matching system).
* Details of a session.
* Member list.

The system software uses information from the session server to do the following:

* Display information about sessions that friends are currently participating in.
* If the user reacts to a session notification, the system software can start the applicable application, pass session information to the application, and enable the application to join that session.
* Notify or invite other users to join the session.

An application can also obtain session information that relates to itself.

## PlayerInvitationDialog Library

The PlayerInvitationDialog Library provides a dialog that allows a player to select other players and send them an invitation to join a session. For details, refer to the following documents:

* [PlayerInvitationDialog Library Overview](../PlayerInvitationDialog-Overview/__document_toc.html)
* [PlayerInvitationDialog Library Reference](../PlayerInvitationDialog-Reference/__document_toc.html)

## Session Manager Web API

The Session Manager Web API manages session information, and sends and receives invitations to join sessions. It also enables platform supported voice chat. For details, refer to the following documents:

* [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html)
* [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html)
* [Session Manager Web API Reference](../../../WebAPI/latest/Session_Manager_WebAPI-Reference/__document_toc.html)

## Matches Web API

The Matches Web API uploads the player's match results or progress in an online multiplayer game (not only online PvP and cooperative play, but also playing with CPU) progress or results of online matches to PlayStation™Network. Game applications can surface online match information (member, progress and results) on PlayStation® Systems. For details, refer to the following documents:

* [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html)
* [Matches Web API Reference](../../../WebAPI/latest/Matches_WebAPI-Reference/__document_toc.html)

## NpSessionSignaling Library

The NpSessionSignaling library performs the communication processing required for peer-to-peer (P2P) communication. It also provides the NAT Traversal feature for communicating across a NAT router. For details, refer to the following documents:

* [NpSessionSignaling Library Overview](../NpSessionSignaling-Overview/__document_toc.html)
* [NpSessionSignaling Library Reference](../NpSessionSignaling-Reference/__document_toc.html)

## Rudp Library

The Rudp library supports reliable data transmission (RUDP) over UDP. For details, refer to the following documents:

* [Rudp Library Overview](../Rudp-Overview/__document_toc.html)
* [Rudp Library Reference](../Rudp-Reference/__document_toc.html)

## VoiceChat Library

You can use the VoiceChat library to implement online voice chat easily for multiplayer use. In addition to providing basic features for realizing voice chat (such as signaling, audio-device detection, encoding, decoding, and sending/receiving voice data), this library also provides additional features, such as the ability to alter voices to match the game content. To simplify the API set for starting voice chat, the library itself processes all basic features necessary to provide voice chat. For details, refer to the following documents:

* [VoiceChat Library Overview](../VoiceChat-Overview/__document_toc.html)
* [VoiceChat Library Reference](../VoiceChat-Reference/__document_toc.html)

## Matchmaking Web API

The Matchmaking Web API provides queue-based Matchmaking, in which players searching for a match are added to a queue while waiting to find a match. When the matchmaker finds groups of players that satisfy a specific ruleset, it moves those players into a game session that facilitates the gameplay experience. Queue-based matchmaking allows for flexible growth of matchmaking pools and is the current industry standard. For details, refer to the following documents:

* [Matchmaking Overview](../../../WebAPI/latest/Matchmaking-Overview/__document_toc.html)
* [Matchmaking Web API Reference](../../../WebAPI/latest/Matchmaking_WebAPI-Reference/__document_toc.html)

## Matchmaking Tool

The Matchmaking tool offers configuration functionality that games can use to create rulesets and configure matchmaking parameters. For details, refer to the following document:

* [Matchmaking Tool User's Guide](../Matchmaking_Tool-Users_Guide/__document_toc.html)

# Game Intent

Game Intent is a generic mechanism to bring users into specific game scenes directly
from PlayStation® system software screens or features.

For details of Game Intent system, refer to the following document:

* [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html)

## NpGameIntent Library

The NpGameIntent library receives Game Intent information from the PlayStation® system software. Game applications can use this library to obtain data from Game Intent events. For details, refer to the following documents:

* [NpGameIntent Library Overview](../NpGameIntent-Overview/__document_toc.html)
* [NpGameIntent Library Reference](../NpGameIntent-Reference/__document_toc.html)

# Advanced Player Profile

This topic links to resources for learning more about the Advanced Player Profile Web
API.

The Advanced Player Profile is a common record of gameplay data that can be accessed by titles in real time and aggregated across the platform; refer to the following document:

* [Advanced Player Profile Overview](../../../WebAPI/latest/Advanced_Player_Profile-Overview/__document_toc.html)

## Advanced Player Profile Web API

Advanced Player Profile Web API provides the aggregated data in real time for gameplay purposes such as matchmaking and host selection, personalizing the player experience, and providing suggestions relevant to the player. It also provides management features for back office websites. Using this API, developers can register fake data for Advanced Player Profile, retrieve the currently configured fake data, and delete the fake data. The fake data is stored per account and per title.

* [Advanced Player Profile Web API Reference](../../../WebAPI/latest/Advanced_Player_Profile_WebAPI-Reference/__document_toc.html)