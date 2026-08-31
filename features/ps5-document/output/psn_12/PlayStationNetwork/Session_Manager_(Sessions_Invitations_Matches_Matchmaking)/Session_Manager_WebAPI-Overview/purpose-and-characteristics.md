# Session Manager Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Session_Manager_WebAPI-Overview/purpose-and-characteristics.html

# Web API Overview

# Purpose and Characteristics

The Session Manager Web API is a Web API that controls sessions to support multiplayer gameplay. By using the Session Manager Web API, applications can bring users together in sessions and assist them in playing together.

# Main Features

The main features provided by the Session Manager Web API are as follows:

* A feature for creating Player Sessions/Game Sessions
* A feature for modifying the properties of sessions
* A feature for obtaining session data
* A feature for allowing users to join sessions
* A feature for allowing users to leave sessions
* A feature for synchronizing the information of non-PlayStation™Network users
* A feature for sending data among users within sessions
* A feature for obtaining a list of sessions in which users are participating
* A feature for obtaining a list of Player Sessions in which friends are participating
* A feature for sending invitations to other users (Player Sessions only)
* A feature for obtaining a list of invitations a user has received (Player Sessions only)
* A feature for obtaining a list of sessions that match the specified conditions (Game Sessions only)

# Sample Program

Sample programs using the Session Manager Web API are as follows:

## sample\_code/playstation\_network/api\_webapi\_session\_manager

This sample exemplifies basic usage of Player Sessions/Game Sessions and the Matches Web API.

## sample\_code/playstation\_network/api\_webapi\_game\_session\_search

This sample exemplifies basic usage of the Game Session Search feature.

# Reference Materials

For common rules for Web APIs, how to use them, and so forth, refer to the following document:

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

For how to use Web APIs with applications for PlayStation®5, refer to following documents:

* [NpWebApi2 Library Overview](../../../SDK/latest/NpWebApi2-Overview/__document_toc.html)
* [NpCppWebApi Library Overview](../../../SDK/latest/NpCppWebApi-Overview/__document_toc.html)

For more about multiplayer gameplay and an overview of the Session Manager Service, refer to the following document.

* [Session Manager Service Overview](../../../SDK/latest/Session_Manager_Service-Overview/__document_toc.html)

For how Matchmaking operates, refer to the following document:

* [Matchmaking Overview](../Matchmaking-Overview/__document_toc.html)

If you intend to allow invitations to be sent from within the game but do not want to prepare a dedicated screen for the game, refer to the following documents:

* [PlayerInvitationDialog Library Overview](../../../SDK/latest/PlayerInvitationDialog-Overview/__document_toc.html), [PlayerInvitationDialog Library Reference](../../../SDK/latest/PlayerInvitationDialog-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Session Manager Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Session_Manager_WebAPI-ReleaseNotes.html)