# Session Manager Service Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Session_Manager_Service-Overview/reference-materials.html

# What Is the Session Manager Service?

# Features Provided by the Session Manager Service

The Session Manager service of the PlayStation™Network supports online multiplayer games. In this context, a "session" refers to the idea of a "place where users gather together for online multiplayer gameplay". The Session Manager service provides features to support sessions and services connected to those features. The main features are as follows.

* Player Sessions:

  This session feature has a special purpose, intended for users playing together, as with in-game parties. The invitation feature is also included here. It is also possible for users to use the system software UI to invite other users, join sessions, and perform other operations.
* Game Sessions:

  This session feature can be used however the developer chooses in a game application.
* Matchmaking:

  This feature is for finding competitors for online multiplayer gameplay. It can be used along with Game Sessions.
* Game Session search:

  This feature is for searching Game Sessions with specific attributes by specifying arbitrary conditions.

In addition, the following features that work with sessions are provided.

* Voice chat
* Signaling

Although independent from sessions, the following feature also supports online multiplayer gameplay.

* Matches:

  This feature is a part of the Universal Data System service. It records gameplay statuses and results. It supports single player gameplay in addition to online multiplayer gameplay. Recorded information can be used in various platform features, for example, recorded information can be reflected on a user's profile screen.

Applications can select and use these features as required. For example, if the feature for inviting users to online multiplayer gameplay is used, a Player Session must be used; however, if online multiplayer sessions and matchmaking are provided using a proprietary game server, there is no need to use Game Sessions or the matchmaking feature.

# Reference Materials

Applications use the features that the Session Manager service provides via the Web APIs of PlayStation™Network. Refer to the following documents.

* [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html)
* [NpWebApi2 Library Overview](../NpWebApi2-Overview/__document_toc.html)
* [NpCppWebApi Library Overview](../NpCppWebApi-Overview/__document_toc.html)

If you will be using Player Sessions and Game Sessions, refer to the following documents.

* [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html), [Session Manager Web API Reference](../../../WebAPI/latest/Session_Manager_WebAPI-Reference/__document_toc.html)

If you will be using the matchmaking feature, refer to the following documents.

* [Matchmaking Overview](../../../WebAPI/latest/Matchmaking-Overview/__document_toc.html), [Matchmaking Web API Reference](../../../WebAPI/latest/Matchmaking_WebAPI-Reference/__document_toc.html)

If you would like to use the system default dialog for inviting other users, refer to the following documents.

* [PlayerInvitationDialog Library Overview](../PlayerInvitationDialog-Overview/__document_toc.html), [PlayerInvitationDialog Library Reference](../PlayerInvitationDialog-Reference/__document_toc.html)

If you will be using matches, refer to the following documents.

* [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html), [Matches Web API Reference](../../../WebAPI/latest/Matches_WebAPI-Reference/__document_toc.html)
* [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Session Manager Web API](../ReleaseNotes/PlayStation_Network-Session_Manager_WebAPI-ReleaseNotes.html)