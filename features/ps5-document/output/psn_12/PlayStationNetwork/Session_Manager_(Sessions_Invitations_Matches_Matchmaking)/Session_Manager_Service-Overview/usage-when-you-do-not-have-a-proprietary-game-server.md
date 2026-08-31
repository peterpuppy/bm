# Session Manager Service Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Session_Manager_Service-Overview/usage-when-you-do-not-have-a-proprietary-game-server.html

# Usage Guides

# Using Player Sessions

A Player Session is a special session whose purpose is allowing a user to play with other users. Use Player Sessions in games that use invitations.

## Sending an Invitation to a Player Session

Use one of the following methods if you intend to implement seamless sending of invitations in your game.

* The application uses the PlayerInvitationDialog library to send invitations
* The application (or the game server) uses the Session Manager Web API to send invitations

Because a feature is also provided for sending invitations using the UI embedded in the system software, it is also possible to do without implementing invitation-sending features in your application. The users who can be invited to Player Sessions can be set at the time of their creation, and these settings will be reflected in the behavior of the system UI.

## Joining Processing After Receiving and Accepting an Invitation to a Player Session

If you would like to implement seamless in-game receiving and accepting of invitations, use the Session Manager Web API to implement the features for receiving and accepting invitations.

Users can also receive and accept invitations using the UI embedded in the system software. A game intent is passed to the application if an invitation is accepted using the system UI; perform the processing to have the user join the Player Session as instructed to in the game intent.

## Sharing a Player Session via a URL

Users can operate the system software or the PlayStation™ App to share the Player Session in which they are participating with other users via a URL. For information on the conditions under which this operation is possible, refer to [Session Manager Web API Overview - Types of Sessions and Their Main Properties - Player Sessions](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/player-sessions.html).

The application can also call the PlayerInvitationDialog to display a "player invitation dialog" that prompts the user to share the Player Session in which they are participating via a URL. For details, refer to [PlayerInvitationDialog Library Overview](../PlayerInvitationDialog-Overview/__document_toc.html).

The application can also use the Session Manager Web API to obtain the URL to share and prompt users to share the URL using the game's own UI. For details, refer to "Sharing Using URLs" in [Session Manager Web API Overview - Types of Sessions and Their Main Properties - Player Sessions](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/player-sessions.html).

## Joining a Player Session via the Shared URL

Users who receive a URL for sharing a Player Session can join the Player Session by launching the game via a link on the URL's web page. When a user performs the actions to "join" from a web page (and, when necessary, also signs into PlayStation™Network and selects the console to use), the game launches, and the user joins the Player Session. To provide this experience, the game must support game intents. For more information about game intents, see "Major Components of the Session Manager Service - Game Intent".

## Jumping in to Join a Player Session

The system software provides a feature for viewing the Player Sessions in which friends are currently participating. Using features such as this one, users who have not been invited can jump in to join the Player Session. (The scope of users who can participate in Player Sessions can be set at the time of their creation, and these settings will be reflected in the behavior of the system UI.) A game intent is passed to the application when a user jumps in to join; perform the processing to have the user join the Player Session as instructed.

It is also possible to implement seamless jump-in joining in games using the Session Manager Web API.

## Processing After Joining a Player Session

Make it so that users participating in the same Player Session can play the game together. The details of this may be defined as appropriate in the specifications for the application. Consider appropriate specifications that follow the intent of "playing together", for example, whether users can join in the middle of gameplay after it has commenced, whether users can temporarily participate as spectators until a break in the gameplay is reach, and so forth.

## Leaving Player Sessions

When a user terminates the multiplayer mode or is otherwise no longer using the Player Session, perform processing to have him or her leave the session. If the user is joining another Player Session, processing to leave the previous Player Session will be performed automatically when the new Player Session is joined. If the user goes offline or the application is terminated, the system will automatically perform the processing for leaving the session.

## Games That Do Not Require Player Sessions

There is no need to user Player Sessions in games in which there is no explicit invitation of other users. For example, games in which users have no control over their multiplayer opponents (such as games in which matchmaking is performed randomly in a certain area) can be implemented using only Game Sessions.

# Usage When You Do Not Have a Proprietary Game Server

If you do not set up a proprietary game server, you will provide any use of online multiplayer gameplay using the features provided by PlayStation™Network. Usage examples are given below.

* A Player Session is used to form an in-game party
  + Use voice chat and P2P communications if required
* Game Sessions are used for battling users outside of the user's party or as a place for users to communicate with one another
  + Use voice chat and P2P communications if required
* Use matchmaking to look for other users to play against, and use Player Sessions as the place for the actual competitive gameplay
* Creation and reporting of matches are performed via the application running on the system of any one of the players who played against one another

There is no need to use Game Sessions if multiplayer gameplay will only occur among the members of a Player Session.

# Usage When You Have a Proprietary Game Server

## When Using a Player Session That Only Users of the PlayStation™Network Can Join

If you are able to provide online multiplayer gameplay using a proprietary game server, use only the features provided by PlayStation™Network that you require. However, be sure to use the Player Sessions of PlayStation™Network as the feature for inviting other users.

Usage examples are given below.

* Reflect game server sessions in Player Sessions
  + Synchronize the member information on the game server with a Player Session to use the invitation features of PlayStation™Network
* Do not use Game Sessions provided by PlayStation™Network (use the features of the game server)
* Do not use matchmaking provided by PlayStation™Network (use the features of the game server)
* The game server creates and reports matches

Note that an access token obtained using an authentication feature for websites cannot be used when calling a Session Manager Web API feature from the game server. Refer to [PlayStation™Network Web APIs Overview - Usage - Obtaining Access Tokens](../PSN_WebAPI-Overview/obtaining-access-tokens.html) for how to obtain access tokens.

## When Using a Player Session That Both Users of the PlayStation™Network and Non-users Can Join

To realize online multiplayer gameplay between users of the PlayStation™Network and users of other platforms using a session managed by the game server, create a Player Session at one of the following times.

* When a session managed by the game server is created
* When a user of the PlayStation™Network joins a session managed by the game server and that session has not yet been linked to a Player Session
* When an invitation is sent to a user of the PlayStation™Network to join a session managed by the game server and that session has not yet been linked to a Player Session

Make sure that information about the session is displayed correctly in system software screen by syncing the lifecycle of the session managed by the game server with that of the Player Session and by updating Player Session information to match changes that occur in the session managed by the game server. The Session Manager Web API is used to update Player Session information. The main methods of performing updates are displayed in the table. Consider the features that the session managed by the game server has and select the an appropriate method.

Note that when a Session Manager Web API request is called with a user of another platform as the caller of the request, the product type of the game server must be application server (client credential).

How to Update a Player Session

| **Changes to a session managed by a game server** | **How to Update a Player Session** |
| --- | --- |
| The number of members increased | `joinPlayerSessionAsPlayer`, `joinPlayerSessionAsSpectator` `postPlayerSessionsMemberNonPsnPlayers`, `putPlayerSessionsMemberNonPsnPlayers` |
| The number of members decreased | `leavePlayerSession`, `deletePlayerSessionsMemberNonPsnPlayer`, `putPlayerSessionsMemberNonPsnPlayers` |
| Leader has been changed | `changePlayerSessionLeader`, `putPlayerSessionsNonPsnLeader` |
| Name of the session changed | `setPlayerSessionProperties``(localizedSessionName)` |
| Maximum number of members changed | `setPlayerSessionProperties``(maxPlayers)`, `setPlayerSessionProperties``(maxSpectators)` |
| The session has become joinable/unjoinable | `setPlayerSessionProperties``(joinDisabled)` |
| The users who can join have changed | `setPlayerSessionProperties``(joinableUserType)`, `addPlayerSessionJoinableSpecifiedUsers`, `deletePlayerSessionJoinableSpecifiedUsers` |
| The custom data for the session has changed | `setPlayerSessionProperties``(customData1)`, `setPlayerSessionProperties``(customData2)` |
| The custom data of a member has changed | `setPlayerSessionMemberSystemProperties`, `patchPlayerSessionsMemberNonPsnPlayer`, `putPlayerSessionsMemberNonPsnPlayers` |