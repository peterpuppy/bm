# Session Manager Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Session_Manager_WebAPI-Overview/game-sessions.html

# Types of Sessions and Their Main Properties

# Player Sessions

A Player Session is a session created for the purpose of users playing together, for example, by forming in-game parties. Conventionally, the members participating in a session might play competitively against the members of other sessions. It could be used with the Player Session being maintained even after the conclusion of one battle, with the members next fighting against the members of yet another session.

## Main Properties of Player Sessions

Main Properties of Player Sessions

| **Property** | **Description** |
| --- | --- |
| `maxPlayers` | Maximum number of players who can join a session (total number of players who are PlayStation™Network users and players who are not PlayStation™Network users) |
| `maxSpectators` | Maximum number of spectators who can participate in the session |
| `joinDisabled` | Flag to temporarily disallow joining of the session |
| `supportedPlatforms` | PlayStation® platforms that can join the session |
| `localizedSessionName,`  `sessionName` | Name of the session. Also displayed in the system software.  Multiple languages can be set for `localizedSessionName`, and one session name in the language based on Accept-Language will be returned when `sessionName` is obtained. |
| `joinableUserType` | Users who can join without invitations   * `NO_ONE`: No one can join without an invitation * `FRIENDS`: Friends of the leader can join * `FRIENDS_OF_FRIENDS`: Friends of friends of the leader can join * `SPECIFIED_USERS`: Members who are registered in the `joinableSpecifiedUsers` list can join * `ANYONE`: Anyone can join |
| `joinableSpecifiedUsers` | A list of members who can join that becomes valid when `joinableUserType` is set to `SPECIFIED_USERS` |
| `invitableUserType` | Members who can send invitations   * `NO_ONE`: No one can invite others * `LEADER`: Only the leader can invite others * `MEMBER`: All participating members can invite others |
| `exclusiveLeaderPrivileges` | Items excluded from the privileges that the leader has by default.  The following items can be specified (multiple selection possible). The specified items will become inoperable from both the system software and the game.   * `KICK`: Privilege to kick out members (force them to leave) * `UPDATE_JOINABLE_USER_TYPE`: Privilege to modify `joinableUserType` * `UPDATE_INVITABLE_USER_TYPE`: Privilege to modify `invitableUserType` * `PROMOTE_TO_LEADER`: Privilege to transfer the position of leader   When creating a Player Session, the same item cannot be specified for `exclusiveLeaderPrivileges` and `disableSystemUiMenu`. |
| `disableSystemUiMenu` | Of the privileges that the leader has by default, items whose operation from the system software UI is to be disabled.  The following items can be specified (multiple selection possible). The specified items will become inoperable from the system software but will remain operable from the game as long as they are not specified in `exclusiveLeaderPrivileges`.   * `KICK`: Privilege to kick out members (force them to leave) * `UPDATE_JOINABLE_USER_TYPE`: Privilege to modify `joinableUserType` * `UPDATE_INVITABLE_USER_TYPE`: Privilege to modify `invitableUserType` * `PROMOTE_TO_LEADER`: Privilege to transfer the position of leader   When creating a Player Session, the same item cannot be specified for `disableSystemUiMenu` and `exclusiveLeaderPrivileges`. |
| `customData1,`  `customData2` | Data areas that the game can use as the developer sees fit as session properties |
| `member.players.customData1,`  `member.spectators.customData1,`  `member.nonPsnPlayers.customData1` | Data areas that can be freely used in the game as member properties |
| `swapSupported` | Flag regarding whether or not the swap feature is supported. (The swap feature changes players to spectators and spectators to players without members who have already joined leaving the session) |
| `expirationTime` | Expiration time [sec] for a Player Session that non-PlayStation™Network users can join. It can be specified when creating a Player Session and cannot be changed later. If the expiration time is exceeded, the Player Session will be forcibly deleted, even if there are still participants in the session. There will be no push events for the Player Session in such cases. |
| `nonPsnSupported` | Flag indicating whether the Player Session can be joined by non-PlayStation™Network users. It can be specified when creating a Player Session and cannot be changed later. |
| `shareableTypes` | List of available methods of sharing   * `URL`: Sharing using an URL |

## Leaders

In a Player Session, there is one user who is the leader. The user who creates the Player Session becomes its first leader; the leader subsequently changes through the following operations:

* The leader leaves the Player Session (the remaining player who joined the earliest becomes the leader)
* The leader uses `changePlayerSessionLeader` to transfer leader privileges to one of the PlayStation™Network users
* The leader uses `putPlayerSessionsNonPsnLeader` to transfer leader privileges to one of the non-PlayStation™Network users

The leader can perform the following actions.

* Set which members can send invitations (`invitableUserType`)
* Force a member to leave
* Set the users who can join without invitations (`joinableUserType`)

These leader privileges can be disabled by using `exclusiveLeaderPrivileges` and `disableSystemUiMenu`. Operation from just the system software UI will be disabled for the items set in `disableSystemUiMenu`. Operation from both the system software UI and the game will be disabled for the items set in `exclusiveLeaderPrivileges`.

## Size (Number of Participants) of Player Sessions

In Player Sessions, slots for "players", who engage in ordinary gameplay, and for "spectators", who only watch in-game activities, can be set up separately. Set the required number of users for each type of member.

* `maxPlayers`: Number of player slots (total number of PlayStation™Network players and non-PlayStation™Network players)
* `maxSpectators`: The number of slots for spectators

## Sending Invitations

Users can invite their friends and other users to Player Sessions. Use `sendPlayerSessionInvitations` for sending in-game invitations. However, non-PlayStation™Network users cannot be invited.

Note:

In addition to this Web API, the sending of invitations can be performed with the PlayerInvitationDialog library. Furthermore, invitations can also be sent from the system software based on user actions. For details, refer to [Session Manager Service Overview](../../../SDK/latest/Session_Manager_Service-Overview/__document_toc.html) and [PlayerInvitationDialog Library Overview](../../../SDK/latest/PlayerInvitationDialog-Overview/__document_toc.html).

Because invitations are sent while linked to Player Sessions, it is necessary to create a Player Session before sending an invitation.

The conditions that determine which users can send invitations depend on `invitableUserType`.

* When it is `LEADER`, it should be the leader of the session
* When it is `MEMBER`, it should be a participating member of that session

## Sharing using an URL

Users can share the Player Session in which they are participating using a URL, prompting other users to join. Use `getPlayerSessionsShareableUrl` to obtain the URL for sharing in the game.

Sharing using URLs is possible when the Player Session is set so that anyone can join or when it is set so that users can invite other users. This can be determined based on whether `URL` is included in `shareableTypes`. Before calling `getPlayerSessionsShareableUrl`, use `getPlayerSessions` to confirm that sharing by URL is possible.

Note:

In addition to using the Session Manager Web API, the sending of invitations can be performed with the PlayerInvitationDialog library and by sharing by URL. In addition to in-game sharing, users can also use a system software feature to share by URL. For details, refer to [Session Manager Service Overview](../../../SDK/latest/Session_Manager_Service-Overview/__document_toc.html) and [PlayerInvitationDialog Library Overview](../../../SDK/latest/PlayerInvitationDialog-Overview/__document_toc.html).

When `getPlayerSessionsShareableUrl` is used, two URLs can be obtained.

* URL for a web page for joining the Player Session
  + This URL is for a web page from which a user can join the Player Session. If you have implemented your own UI in your game, share this URL with other users.
* Two-dimensional barcode image URL for sharing the Player Session
  + A web page for sharing by URL is displayed when a user reads this two-dimensional barcode with a smartphone or other device. This two-dimensional barcode can also be displayed in-game to provide sharing by URL.

## Joining a Player Session

To join a Player Session in a game, use `joinPlayerSessionAsPlayer`, `joinPlayerSessionAsSpectator`, or `postPlayerSessionsMemberNonPsnPlayers`.

Even without invitations, PlayStation™Network users can join a session if they know its ID, depending on the `joinableUserType` (refer to [Main Properties of Player Sessions](player-sessions.html#session-manager-web-api-overview_1_1__c32b6422-e267-11ee-bd3d-0242ac120002)) set for the session.

Even without invitations, non-PlayStation™Network users can join a session if they know its ID, regardless of the value of `joinableUserType` set for the session.

Note:

If a user performs an action in the system software to join a Player Session, a game intent, which includes the session ID, is passed to the application. Perform the processing to have the user join the Player Session in response.

For each platform (PlayStation®4 and PlayStation®5), a given PlayStation™Network user can participate in one Player Session at a time. If a user attempts to join a Player Session while already participating in another Player Session, they will join the new target Player Session after leaving the currently joined Player Session and all Game Sessions.

Non-PlayStation™Network users have a unique player ID within a single Player Session, but they do not have a unique ID across all Player Sessions. Therefore, when users try to join a Player Session, they will not automatically leave the Player Session that they are already in. For a user to participate in only one session at a time, appropriate action will need to be taken on the application side.

## Switching Between Player and Spectator (Swap Feature)

PlayStation™Network users who have joined a Player Session that uses the swap feature (`swapSupported` = `true`) can change their player/spectator role without having to leave the session. Use `joinPlayerSessionAsSpectator` to change from a player to spectator, and `joinPlayerSessionAsPlayer` to change from a spectator to a player. For detailed conditions for each, see the [Session Manager Web API Reference](../Session_Manager_WebAPI-Reference/__document_toc.html) document.

Non-PlayStation™Network users cannot join as a spectator, so they cannot use the swap feature either.

## Leaving the Player Session

PlayStation™Network users can explicitly leave the Player Session if `leavePlayerSession` is used within the game. When a user leaves the Player Session, they also leave any Game Sessions in which they are participating at the time. When the user terminates the game or goes offline, they automatically leave the session.

If `deletePlayerSessionsMemberNonPsnPlayer` is used within the game, non-PlayStation™Network users can explicitly leave the Player Session.

## Feature for Synchronizing the Information of Non-PlayStation™Network Users

If proprietary sessions are used, you can use `putPlayerSessionsMemberNonPsnPlayers` to perform the following three processes at once and synchronize user information between the proprietary session and Player session:

* If a non-PlayStation™Network user is joined into the proprietary session and also the Player Session, update the user's `customData1` and `playerName`
* If a non-PlayStation™Network user is joined into the proprietary session but not the Player Session, make the user join the Player Session
* If a non-PlayStation™Network user is joined into the Player Session but not the proprietary session, make the user leave the Player Session

Note:

The updating of `playerName` is not recommended. This is because changing `playerName` does not change the name under which that player sent invitations.

## List of Player Sessions in which Friends Are Participating

If `getFriendsPlayerSessions` is used within the game, the user can obtain a list of the Player Sessions in which their friends are participating. However, if a friend has enabled the Appear Offline feature or has configured title privacy settings to restrict their visibility, information concerning that friend cannot be obtained.

## Lifespan of a Player Session

Player Sessions are deleted at the following time:

* When the last player (PlayStation™Network player or non-PlayStation™Network player) leaves (spectators are deleted if present)
* When a Player Session that is joinable by non-PlayStation™Network users exceeds the `expirationTime` specified when it was created (Participants are forcibly deleted if present. Additionally, there will be no push events for the Player Session in this case.)

An API feature for explicitly deleting Player Sessions is not provided.

## Operations Using the System Software

PlayStation™Network users can perform the following actions affecting Player Sessions using the system software:

* Invite other users to the Player Session in which they are participating (only if they are members allowed to send invitations based on `invitableUserType`)
* Share the Player Session that the user has joined using a URL (For the conditions under which this operation can be performed, refer to [Sharing using an URL](player-sessions.html#session-manager-web-api-overview_1_1__section_z1x_g4t_tbc))
* Modify `invitableUserType` (only if the leader of the session and if `UPDATE_INVITABLE_USER_TYPE` is not specified for `exclusiveLeaderPrivileges` or `disableSystemUiMenu`)
* Modify `joinableUserType` (only if the leader of the session and if `UPDATE_JOINABLE_USER_TYPE` is not specified for `exclusiveLeaderPrivileges` or `disableSystemUiMenu`)
* View invitations to Player Sessions that they have received
* Join Player Sessions (either joining via invitations or jump-in joining without invitations)
* Change from a PlayStation™Network player to a spectator, or from a spectator to a PlayStation™Network player, without leaving the Player Session they are in (only when `swapSupported` is set to `true`)
* Kick out (force to leave) other members (only if the leader of the session and if `KICK` is not specified for `exclusiveLeaderPrivileges` or `disableSystemUiMenu`)
* Transfer the position of leader to another member (only if the leader of the session and if `PROMOTE_TO_LEADER` is not specified for `exclusiveLeaderPrivileges` or `disableSystemUiMenu`)

## Displaying Player Sessions in the Game

When a Player Session is displayed in the game, the user may make changes to the Player session directly through the system software (and not through the application). Even in such cases, it is recommended that you ensure the leader and members list of the Player Session matches the leader and members list of the in-game session linked to the Player Session. Below are some common cases where mismatches can occur and how to deal with them:

* When the leader changes
  + When the leader of the Player Session changes the leader to another user via the system software, reflect that change in the in-game session.
  + When the leader of the in-game session is changed, reflect that change in the Player Session.
* When a player leaves or is kicked out
  + When the leader of the Player Session kicks out another player from the Player Session via the system software, kick that player out from the in-game session.
  + When a player leaves or is kicked out from the in-game session, reflect that change in the Player Session.
* When a player joins
  + When a player joins the in-game session, reflect that change in the Player Session.

It is also not a problem to use the `exclusiveLeaderPrivileges` property or `disableSystemUiMenu` property of the Player Session to prevent users from making these changes via the system software.

Note:

From SDK 7.00 onwards, non-PlayStation™Network players can also join Player Sessions. It is recommended that non-PlayStation™Network players be included in Player Sessions if the application supports cross-platform gameplay.

**Check Method:**

The leader and members list of a Player Session can be checked/changed from the Player Session's card on the system software screen. To change the leader to another player, select the player's name on the card and select "Promote to Leader". To kick out another player from a Player Session, select the player's name on the card and select "Kick Out".

## Summary: Configurable/Modifiable Properties

Those Player Session properties that are configurable/modifiable are summarized below.

Configurable/Modifiable Properties in Player Sessions

| **Property** | **Configuration at Time of Creation** | **Modifiable** | **Modifiable via the System Software** |
| --- | --- | --- | --- |
| `maxPlayers` | Required | Yes | No |
| `maxSpectators` | Optional (The default value will be set if nothing is specified) | Yes | No |
| `joinDisabled` | Optional | Yes | No |
| `supportedPlatforms` | Required | No | No |
| `localizedSessionName` | Required | Yes | No |
| `joinableUserType` | Optional (The default value will be set if nothing is specified) | Yes (only if the leader and if `UPDATE_JOINABLE_USER_TYPE` is not specified for `exclusiveLeaderPrivileges`) | Yes (only if the leader and if `UPDATE_JOINABLE_USER_TYPE` is not specified for `exclusiveLeaderPrivileges` or `disableSystemUiMenu`) |
| `joinableSpecifiedUsers` | Optional | Yes | No |
| `invitableUserType` | Optional (The default value will be set if nothing is specified) | Yes (only if the leader and if `UPDATE_INVITABLE_USER_TYPE` is not specified for `exclusiveLeaderPrivileges`) | Yes (only if the leader and if `UPDATE_INVITABLE_USER_TYPE` is not specified for `exclusiveLeaderPrivileges` or `disableSystemUiMenu`) |
| `exclusiveLeaderPrivileges` | Optional | Yes | No |
| `disableSystemUiMenu` | Optional | Yes | No |
| `customData1,`  `customData2` | Optional | Yes | No |
| `member.players.customData1,`  `member.spectators.customData1,`  `member.nonPsnPlayer.customData1` | Optional | Yes | No |
| `swapSupported` | Optional | Yes | No |
| `expirationTime` | Optional (Required when creating a Player Session that non-PlayStation™Network users can join. This cannot be specified in Player Sessions that only PlayStation™Network users can join.) | No | No |
| `nonPsnSupported` | Optional (If the request is called by a PlayStation™Network user, either true or false can be specified. If nothing is specified, it will be false. If the request is called by a non-PlayStation™Network user, only true can be specified. If nothing is specified, it will be true.) | No | No |
| `shareableTypes` | Optional (Set based on the values of `joinableUserType` and `invitableUserType`) | Yes (When `joinableUserType` and `invitableUserType` can be modified) | Yes (When `joinableUserType` and `invitableUserType` can be modified) |

# Game Sessions

A Game Session is a session that a game can use however the developer chooses for online multiplayer gameplay. In cases such as when there is a proprietary game server that has the relevant features, there is no need to use Game Sessions if they are not required.

## Main Properties of Game Sessions

Main Properties of Game Sessions

| **Property** | **Description** |
| --- | --- |
| `maxPlayers` | Maximum number of players who can participate in the session |
| `maxSpectators` | Maximum number of spectators who can participate in the session |
| `joinDisabled` | Flag to temporarily disallow joining of the session |
| `supportedPlatforms` | PlayStation® platforms that can join the session |
| `customData1,`  `customData2` | Data areas that the game can use as the developer sees fit as session properties |
| `member.players.customData1,`  `member.spectators.customData1` | Data areas that can be freely used in the game as member properties |
| `usePlayerSession` | Flag indicating whether the Game Session is dependent on a Player Session |
| `reservationTimeoutSeconds` | Period for which a reservation by a member to join a Game Session remains valid |
| `matchmaking` | Information applied by the Matchmaking Service to Game Sessions created using Matchmaking |
| `searchIndex` | Index name for Game Session Search |
| `searchAttributes` | Attribute value group to be the search conditions for Game Session Search |
| `searchable` | Flag indicating whether a session is searchable with Game Session Search |
| `member.players.natType,`  `member.spectators.natType` | The NAT type of each member that is referenced when performing a Game Session Search that considers whether P2P communications are allowed |

## Game Session Representatives

The concept of leaders does not exist for Game Sessions. Instead, there is the concept of representatives. Representatives do not have special privileges; however, there is always exactly one among the members. If the representative leaves a session, the member who has been participating the longest automatically becomes the new representative.

The representative can be used, for example, as the user who performs processing relating to the `reportResults`.

## Size (Number of Participants) of Game Sessions

In Game Sessions, slots for "players", who engage in ordinary gameplay, and for "spectators", who only watch in-game activities, can be set up separately. Set the required number of users for each type of member.

* `maxPlayers`: The number of slots for players
* `maxSpectators`: The number of slots for spectators

## Requesting to Join a Game Session

Within games, users can request that other users join Game Sessions.

* When creating a Game Session, specify other users, in addition to the user who is creating the session, with `createGameSessions`
* If a Game Session already exists, specify other users with `joinGameSessionAsPlayer`

Push events are sent to the specified users, and they can use those as triggers to join the session. The users who were issued the join request gain reserved status as players in the Game Session. Reserved status is removed after a certain amount of time has passed.

Note:

There is no feature provided in the system software for users to send invitation requests for other users to join Game Sessions. Refer to [Session Manager Service Overview - Major Components of the Session Manager Service - Game Sessions](../../../SDK/latest/Session_Manager_Service-Overview/game-sessions.html) for details.

## Joining Game Sessions

A given user can participate in multiple Game Sessions at once.

To join a Game Session that is dependent on a Player Session as a player, a user must meet the following join condition:

* The user is participating in a Player Session as a player

To join as a spectator, a user must also meet the following join condition:

* The user is participating in a Player Session a player or spectator

However, the user is not required to meet the above conditions to join a Game Session that is not dependent on a Player Session, either as a player or as a spectator.

## Switching Between Player and Spectator (Swap Feature)

Players and spectators can change roles without having to leave the Game Session. Use `joinGameSessionAsSpectator` to change from a player to spectator, and `joinGameSessionAsPlayer` to change from a spectator to a player. For detailed conditions for each, see the [Session Manager Web API Reference](../Session_Manager_WebAPI-Reference/__document_toc.html) document.

## Leaving a Game Session

If `leaveGameSession` is used within the game, the user can explicitly leave the Game Session.

Additionally, when a user leaves a Player Session, they leave all the Game Sessions they are participating in at the time that are dependent on the Player Session.

Also, if the user terminates the game or goes offline, they will automatically leave any sessions.

## Lifespan of a Game Session

Game Sessions are deleted at the following times:

* When the last player leaves (The session will be deleted even if there are spectators)
* The session has been explicitly deleted using `deleteGameSession` within the game (The session will be deleted even if there are players)

## Flag Indicating Player Session Dependency

If Player Sessions aren't used in a game, set this flag to "false", and it will be possible to create Game Sessions that are not dependent on Player Sessions.

Note:

If Player Sessions aren't used in a game, it is not possible to invite other users to join the gameplay. There is no feature provided in the system software for users to send invitation requests for other users to join Game Sessions.

## Operations Using the System Software

Users cannot manipulate Game Sessions using the system software.

## Summary: Configurable/Modifiable Properties

Those Game Session properties that are configurable/modifiable are summarized below.

Configurable/Modifiable Properties in Game Sessions

| **Property** | **Configurable at the Time of Creation** | **Modifiable** |
| --- | --- | --- |
| `maxPlayers` | Required | Yes |
| `maxSpectators` | Optional (The default value will be set if nothing is specified) | Yes |
| `joinDisabled` | Optional | Yes |
| `supportedPlatforms` | Required | No |
| `customData1,`  `customData2` | Optional | Yes |
| `member.players.customData1,`  `member.spectators.customData1` | Optional | No |
| `usePlayerSession` | Optional | No |
| `matchmaking` | (It is not possible for the application to specify this property; through Matchmaking, it is automatically applied to the Game Session that was created) | No |
| `searchIndex` | Optional (required when using Game Session Search) | No |
| `searchAttributes` | Optional | Yes |
| `searchable` | Optional | Yes |
| `member.players.natType,`  `member.spectators.natType` | Optional | Yes |