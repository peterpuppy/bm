# Session Manager Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Session_Manager_WebAPI-Overview/using-the-web-api.html

# Using the Web API

# Basic Usage of Player Sessions (for PlayStation™Network Users)

The basic procedure for PlayStation™Network users to call requests and for a PlayStation®5 application to use the Session Manager Web API to handle Player Sessions is provided below.

1. **Creation of a Push Context**

   Create a Push context for saving Push events that arise within the Player Session. Be sure to create and use a separate Push context whenever a Player Session is created or joined. For example, make sure to create a new Push context even when the user rejoins a Player Session that they left.

   In addition, even when a Session Manager Web API feature is called from the game server, a Push context must be created on the console side.

   For information about Push contexts, refer to [NpWebApi2 Library Overview - Feature Description - Feature for Receiving Push Events](../../../SDK/latest/NpWebApi2-Overview/feature-for-receiving-push-events.html).
2. **Creation of a Player Session**

   Call `createPlayerSessions` to create a Player Session when required, such as when multiplayer game mode has been entered. Specify the Push context as a parameter.

   The user who created the Player Session always joins as a player and automatically becomes the leader.
3. **Sending and Receiving of Invitations to the Player Session**

   Within the game, call `sendPlayerSessionInvitations` to send invitations to the Player Session. Any user who can send invitations is a `MEMBER` or the `LEADER` specified with `invitableUserType` at the time the Player Session was created.

   The Push event `psn:sessionManager:ps:invitations:created` is sent to the invited users.

   Additionally, `getPlayerSessionInvitations` is used to display a list of received invitations within the game.
4. **Joining the Player Session**

   When a user joins a Player Session, it must be explicitly specified whether they are joining as a "PlayStation™Network player" or as a "spectator".

   Use `joinPlayerSessionAsPlayer` if the user is joining as a player. Use `joinPlayerSessionAsSpectator` if the user is joining as a spectator.

   The conditions for joining are determined with the following order of priority:

   * `joinDisabled` is false
   * `supportedPlatforms` is supported
   * The number of players or spectators currently joined is fewer than the maximum number who can join
   * `joinableUserType` (`FRIENDS`, `FRIENDS_OF_FRIENDS`, or `ANYONE`) is met
5. **Processing After Joining a Player Session**

   Make it so that users who have joined a Player Session can play the game together with the members of the same session. Handle the situation appropriately to allow users who join after gameplay has already begun to play, for example, by allowing them to join in the middle of gameplay or by having them simply view the action until a well-defined break in the gameplay occurs.

   If you want to make a user who has joined a Player Session join a specific Game Session (for example, when you are using a Player Session in conjunction with a Game Session, see the text under the [Requesting to Join a Game Session](game-sessions.html#session-manager-web-api-overview_1_2__session-manager-web-api-overview_1_2_4) heading.
6. **Sending and Receiving Messages Among Members**

   You can use `sendPlayerSessionMessage` for low-frequency exchanges of messages, such as passing over information to guide users to a feature on a proprietary game server that is equivalent to a session. The Push event `psn:sessionManager:ps:sessionMessage:created` is sent to the user specified as the recipient.
7. **Leaving Player Sessions**

   If `leavePlayerSession` is called within the game, the user will leave the Player Session. When a user leaves a Player Session, they also automatically leave any Game Sessions in which they are participating. If the leader leaves, the privileges of the leader are transferred to the first member who joined among the remaining members.

# Basic Usage of Player Sessions (for non-PlayStation™Network Users)

The basic procedure for non-PlayStation™Network users to call requests and use the Session Manager Web API to handle Player Sessions is provided below. The product type must be App Server (Client Credential) to use the API. Non-PlayStation™Network users are not sent Push events generated in the Player Session, so there is no need to create a Push context.

1. **Creation of a Player Session**

   Call `createPlayerSessions` to create a Player Session when required, such as when multiplayer game mode has been entered.

   The user who created the Player Session always joins as a player and automatically becomes the leader.
2. **Sending an Invitation to the Player Session**

   Within the game, call `sendPlayerSessionInvitations` to send invitations to the Player Session to PlayStation™Network users. It is not possible to send invitations to non-PlayStation™Network users. Any user specified as a `MEMBER` or `LEADER` in `invitableUserType` when the Player Session was created can send invitations.

   The users of PlayStation™Network on the receiving end must have "Get crossplay game invitations" enabled in their privacy settings to receive the invitations.

   The Push event `psn:sessionManager:ps:invitations:created` is sent to the invited PlayStation™Network users.
3. **Joining the Player Session**

   Non-PlayStation™Network users can join as "non-PlayStation™Network players". They cannot join as spectators. Use `postPlayerSessionsMemberNonPsnPlayers` in order to join as a "non-PlayStation™Network player".

   The conditions for joining are determined with the following order of priority:

   * `joinDisabled` is false
   * `nonPsnSupported` is true
   * The number of players currently participating (total number of PlayStation™Network players and non-PlayStation™Network players) is less than the maximum number of participants
4. **Processing After Joining a Player Session**

   Make it so that users who have joined a Player Session can play the game together with the members of the same session.
5. **Leaving Player Sessions**

   If `deletePlayerSessionsMemberNonPsnPlayer` is called within the game, the user can leave the Player Session. If the leader leaves, leader privileges are transferred to the first member who joined among the remaining members.

**Notes for When the Leader Is a non-PlayStation™Network User**

* For a Player Session in which a user who is not on PlayStation™Network is the leader, `FRIENDS` or `FRIENDS_OF_FRIENDS` is ignored if either of these values has been set for `joinableUserType`, and users cannot join without invitations.
* If you would like to allow users of PlayStation™Network to join a Player Session whose leader is not on PlayStation™Network, set `SPECIFIED_USERS` to `joinableUserType`, and register the users whom you would like to allow to join to the `joinableSpecifiedUsers` list. Alternatively, have the non-PlayStation™Network user who has joined that Player Session invite the users whom they would like to allow to join.

# Basic Usage of Game Sessions

1. **Creation of a Push Context**

   Create a Push context for saving Push events that arise within the Game Session. Be sure to create and use a separate Push context whenever a Game Session is created or joined. For example, make sure to create a new Push context even when the user rejoins a Game Session that they left.

   In addition, even when a Session Manager Web API feature is called from the game server, a Push context must be created on the console side.
2. **Creation of a Game Session**

   Because Game Sessions can be used by the game however the developer chooses, when they are created is up to the game's developer, and multiple sessions can be created at once. A typical anticipated use is working in tandem with the match-making feature.

   Use `createGameSessions` to create a Game Session and specify a Push context. Here, you can specify the current and other users. The current user can immediately join a Game Session they have created, but the other users' status will be reserved to join as players. (There are plans for future support for a feature for reserving spaces in sessions as spectators.) The reserved users receive the Push event `psn:sessionManager:gs:invitations:created`.
3. **Joining the Game Session**

   When a user joins a Game Session, it must be explicitly specified whether they are joining as a "player" or as a "spectator". Use `joinGameSessionAsPlayer` if the user is joining as a player. Use `joinGameSessionAsSpectator` if the user is joining as a spectator.

   If a user is joining via the Push event `psn:sessionManager:gs:invitations:created`, the Game Session ID is included in the Push event; therefore, specify the session ID in `joinGameSessionAsPlayer`.

   The conditions for joining as a player are determined with the following order of priority:

   * The user is participating in a Player Session as a player
   * `joinDisabled` is false
   * The number of players currently joined is fewer than the maximum number who can join

   The conditions for joining as a spectator are determined with the following order of priority:

   * The user is participating in a Player Session as a player or spectator
   * `joinDisabled` is false
   * The number of spectators currently joined is fewer than the maximum number who can join
4. **Requesting to Join a Game Session**

   If a user would like to allow another user to join an existing Game Session, they can, via specification of that user in `joinGameSessionAsPlayer`, send a join request Push event `psn:sessionManager:gs:invitations:created`. A reservation will be made for the user receiving the request to join as a player, and they will be able to join the Game Session as a player if they call `joinGameSessionAsPlayer` within the allotted amount of time.

   If a user would like to make another user join as a spectator, they can, for example, use `sendPlayerSessionMessage` to pass over the Game Session ID to another member in the Player Session, and that member receiving the request can call `joinGameSessionAsSpectator`. (A feature for making a reservation to join as a spectator will be provided in the future.)
5. **Sending and Receiving Messages Among Members**

   You can use `sendGameSessionMessage` for conversations involving low-frequency messages. The Push event `psn:sessionManager:gs:sessionMessage:created` is sent to the user specified as the recipient.
6. **Leaving a Game Session**

   If `leaveGameSession` is called within the game, the user will leave the Game Session. If the representative of a Game Session leaves, the member among those who remain who joined the earliest will become the new representative of the Game Session.

# Basic Usage of Game Session Search

1. **Creation of a Game Session**

   Specify `searchIndex` when creating a Game Session to make it searchable with Game Session Search. `searchIndex` cannot be modified after a Game Session has been created.

   An array of up to 64 arbitrary alphanumeric characters can be specified for `searchIndex`; no prior configuration, requests, or other actions are required. One title can use a maximum of 100 different `searchIndex` values. Once a `searchIndex` has been specified for a Game Session, a record of what was specified will remain. Be careful not to make specifications without reason.

   When the number of Game Sessions with the same `searchIndex` exceeds a certain number, the processing of search requests targeting that `searchIndex` will slow down, and the possibility of errors such as a timeout occurring will increase. As reference, the threshold at which processing speed largely deteriorates is approximately 100,000. Therefore, in order to prevent the number of Game Sessions with the same `searchIndex` from exceeding this threshold, prepare multiple `searchIndex` for one purpose and determine the `searchIndex` to use, for example, according to the player's attribute. A problem won't immediately occur when the threshold is exceeded; however, if it's expected to be exceeded, contact us in advance via "Post new issue" of Private Support (<https://p.siedev.net/support/newissue>).
2. **Configuration of Attributes for Searching**

   Set attribute values for narrowing down search conditions to `searchAttributes`. `searchAttributes` can also be specified when creating a Game Session; depending on the situation, this specification can be modified as many times as you would like. There are three types of attribute values for `searchAttributes`: Boolean values, integer values, and strings. A maximum of 10 values of each type can be set.

   Extensive use of search attributes will affect the processing speed of search requests. To improve the processing speed of search requests, minimize the number of search attributes to set to one Game Session, reduce the data size by using integers and Boolean values instead of strings, etc.
3. **Searches**

   Game Sessions are searched for by specifying a `searchIndex` and arbitrary search conditions. The server returns the Game Sessions that match the search conditions out of those with the specified `searchIndex`. When multiple search conditions are specified, Game Sessions that match all the search conditions will be returned.

   **Attributes That Can Be Specified for Search Conditions**

   Attributes that can be specified for search conditions are shown in a table. In addition to the attributes for searching, there are also attributes that are generated automatically based on the state of the Game Session.

   Attributes That Can Be Specified for Search Conditions

   | **Attribute** | **Data Type** | **Description** |
   | --- | --- | --- |
   | `maxPlayers` | Integer value | Game Session `maxPlayers` property |
   | `maxSpectators` | Integer value | Game Session `maxSpectators` property |
   | `numPlayerSlots` | Integer value | Number of empty slots for players  `maxPlayers - member.players` |
   | `numSpectatorSlots` | Integer value | Number of empty slots for spectators  `maxSpectators - member.spectators` |
   | `joinDisabled` | Boolean value | Game Session `joinDisabled` property |
   | `natType` | Integer value (1, 2, or 3 only) | Used for searching that considers P2P communications (described later) Specify the NAT type of the user who is performing the search. The only conditional operator that can be specified together is EQUAL. |
   | `searchAttributes.boolean1,….boolean10` | Boolean value | Attribute for searching (Boolean value) |
   | `searchAttributes.integer1,….integer10` | Integer value | Attribute for searching (integer value) |
   | `searchAttributes.string1,….string10` | String | Attribute for searching (string) |

   **Conditional Operators and Data Types**

   The correspondences between the conditional operators that can be specified as search conditions and the data types of attributes is as follows:

   Conditional Operators and Data Types

   | **Conditional Operator** | **Description** | **Boolean value** | **Integer value** | **String** |
   | --- | --- | --- | --- | --- |
   | `EQUAL` | Matches the specified value | Yes | Yes | Yes |
   | `NOT_EQUAL` | Does not match the specified value | Yes | Yes | Yes |
   | `GREATER_THAN` | Is greater than the specified value |  | Yes |  |
   | `LESS_THAN` | Is less than the specified value |  | Yes |  |
   | `GREATER_THAN_OR_EQUAL` | Is greater than or equal to the specified value |  | Yes |  |
   | `LESS_THAN_OR_EQUAL` | Is less than or equal to the specified value |  | Yes |  |
   | `IN` | Matches one of multiple specified values |  | Yes | Yes |

## Automatic Exclusion from Searching Due to the Passage of Time

To avoid having Game Sessions that are no longer being used end up being included in search results, Game Session Search automatically excludes from searching any Game Sessions for which there have been no changes in the number of members or updates to properties in the last 15 minutes.

If you would like a Game Session with a long lifespan to remain continuously searchable regardless of changes to the number of members or modifications of properties, periodically call `postGameSessionsTouch`. A Game Session for which `postGameSessionsTouch` has been called will not be automatically excluded from searching for the next 15 minutes.

It is sufficient for any one member of the Game Session to call `postGameSessionsTouch`; it is recommended that the representative of the Game Session be the one to call `postGameSessionsTouch`.

## Explicit Exclusion from Searching

By changing the `searchable` flag to false, you can temporarily exclude a Game Session from searching. (It will become searchable when the value is switched back to true.) It is recommended that you change the `searchable` flag to false on the fly for any Game Session for which it is no longer necessary that it be searched for to avoid adversely affecting the user experience or the search feature.

## Searching That Considers P2P Communications

Applications that use the NpSessionSignaling library to perform P2P communications can search for Game Sessions while considering P2P communications.

* Preparations on the side of the Game Session that will be searched for
  + Specify a session ID and activate a signaling group
  + Set the members' NAT type for the Game Session
* Specify the user's own NAT type in the search conditions and perform a search

Based on the P2P connection topology, the server will return only Game Sessions that match the conditions provided below as search results. (If the P2P connection topology is unclear, it will be handled as full mesh.)

* Full mesh: (Once the user who performed the search has joined) there is at most 1 member with NAT type 3
* Star: (Once the user who performed the search has joined) there is at least 1 member with NAT type 1 or 2

Obtaining NAT types and activating signaling groups is performed using the NpSessionSignaling library. For details, refer to the following documents:

* [NpSessionSignaling Library Overview](../../../SDK/latest/NpSessionSignaling-Overview/__document_toc.html)
* [NpSessionSignaling Library Reference](../../../SDK/latest/NpSessionSignaling-Reference/__document_toc.html)

## Time Lag Until Changes in Search Attributes Are Reflected

When Game Session attributes change (the number of empty slots changed due to members joining or leaving, search attribute values were changed, etc.), there's a time lag until that change is reflected to the search request results. The time lag is approximately 2 to 3 seconds regardless of the number of Game Sessions. This time lag can't be avoided. Consider the UX with the assumption that time lags will occur.