# Session Manager Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Session_Manager_WebAPI-Overview/push-events-relating-to-game-sessions.html

# Push Events

This chapter explains push events that occur in the Session Manager Web API.

# How to Receive Push Events

Refer to [PlayStation™Network Web APIs Overview - Feature Overview - Push Events](../../../SDK/latest/PSN_WebAPI-Overview/push-events.html) for information about how applications can receive push events.

# Notes

Push events are not guaranteed to reach their recipient. The following push events are also not guaranteed to adhere to any order. Assume that the order in which push events are received will be different from the order in which they occurred, and handle them on the application side accordingly.

## Push Events (Order Not Guaranteed)

* Player Sessions
  + `psn:sessionManager:ps:sessionMessage:created`
  + `psn:sessionManager:ps:customData1:updated`
  + `psn:sessionManager:ps:customData2:updated`
  + `psn:sessionManager:ps:m:p:customData1:updated`
  + `psn:sessionManager:ps:m:s:customData1:updated`
  + `psn:sessionManager:ps:m:npp:customData1:updated`
  + `psn:sessionManager:ps:invitations:created`
* Game Sessions
  + `psn:sessionManager:gs:sessionMessage:created`
  + `psn:sessionManager:gs:customData1:updated`
  + `psn:sessionManager:gs:customData2:updated`
  + `psn:sessionManager:gs:m:p:customData1:updated`
  + `psn:sessionManager:gs:m:s:customData1:updated`
  + `psn:sessionManager:gs:invitations:created`

# Push Events Relating to Player Sessions

| **Data Type** | | **Request That Can Cause or Trigger the Push Event** | **Destination** |
| --- | --- | --- | --- |
| `psn:sessionManager:playerSession:created` | | Player Session created   * `createPlayerSessions` | Members who have joined or who have reserved a spot to join the created session |
| `psn:sessionManager:playerSession:deleted` | | Player Session deleted   * `leavePlayerSession` * `createPlayerSessions` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members of the session before it is deleted |
| `psn:sessionManager:ps:maxPlayers:updated` | | `maxPlayers` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:maxSpectators:updated` | | `maxSpectators` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:joinDisabled:updated` | | `joinDisabled` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:localizedSessionNames:updated` | | `localizedSessionNames` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps::joinableUserType:updated` | | `joinableUserType` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:invitableUserType:updated` | | `invitableUserType` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:exclusiveLeaderPrivileges:updated` | | `exclusiveLeaderPrivileges` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:disableSystemUiMenu:updated` | | `disableSystemUiMenu` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:customData1:updated` | | `customData1` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:customData2:updated` | | `customData2` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:leader:updated` | | The leader has changed to a PlayStation™Network user   * `changePlayerSessionLeader` * `leavePlayerSession` * `createPlayerSessions` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members participating in the session |
| `psn:sessionManager:ps:nonPsnLeader:updated` | | The leader has changed to a non-PlayStation™Network user   * `putPlayerSessionsNonPsnLeader` | Members participating in the session |
| `psn:sessionManager:ps:joinableSpecifiedUsers:created` | | User was saved in the `joinableSpecifiedUsers` list   * `addPlayerSessionJoinableSpecifiedUsers` | Members participating in the session |
| `psn:sessionManager:ps:joinableSpecifiedUsers:deleted` | | User was deleted from the `joinableSpecifiedUsers` list   * `deletePlayerSessionJoinableSpecifiedUsers` | Members participating in the session |
| `psn:sessionManager:ps:swapSupported:updated` | | `swapSupported` updated   * `setPlayerSessionProperties` | Members participating in the session |
| `psn:sessionManager:ps:m:players:created` | | A PlayStation™Network player has joined   * `createPlayerSessions` * `joinPlayerSessionAsPlayer` | Members participating in the session |
| `psn:sessionManager:ps:m:spectators:swapped` | | A member swapped from a PlayStation™Network player to spectator   * `joinPlayerSessionAsSpectator` | Members participating in the session |
| `psn:sessionManager:ps:m:players:deleted` | | A PlayStation™Network player has left   * `leavePlayerSession` * `createPlayerSessions` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members participating in the session before the user left |
| `psn:sessionManager:ps:m:p:customData1:updated` | | A PlayStation™Network player's `customData1` has been updated   * `setPlayerSessionMemberSystemProperties` | Members participating in the session |
| `psn:sessionManager:ps:m:spectators:created` | | A spectator has joined   * `joinPlayerSessionAsSpectator` | Members participating in the session |
| `psn:sessionManager:ps:m:players:swapped` | | A member swapped from a spectator to a PlayStation™Network player   * `joinPlayerSessionAsPlayer` | Members participating in the session |
| `psn:sessionManager:ps:m:spectators:deleted` | | Spectator has left   * `leavePlayerSession` * `createPlayerSessions` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members participating in the session before the user left |
| `psn:sessionManager:ps:m:s:customData1:updated` | | Spectator's `customData1` updated   * `setPlayerSessionMemberSystemProperties` | Members participating in the session |
| `psn:sessionManager:ps:m:nonPsnPlayers:created` | | A non-PlayStation™Network player has joined   * `createPlayerSessions` * `postPlayerSessionsMemberNonPsnPlayers` | Members participating in the session |
| `psn:sessionManager:ps:m:nonPsnPlayers:deleted` | | A non-PlayStation™Network player has left   * `deletePlayerSessionsMemberNonPsnPlayer` | Members participating in the session |
| `psn:sessionManager:ps:m:npp:customData1:updated` | | A non-PlayStation™Network player's customData1 has been updated   * `patchPlayerSessionsMemberNonPsnPlayer` | Members participating in the session |
| `psn:sessionManager:ps:sessionMessage:created` | | A session message was sent   * `sendPlayerSessionMessage` | Recipient user |
| `psn:sessionManager:ps:invitations:created` | | Invitation has been sent   * `sendPlayerSessionInvitations` | Recipient user |
| `psn:sessionManager:ps:m:nonPsnPlayers:updated` | | Information of non-PlayStation™Network players has been synchronized   * `putPlayerSessionsMemberNonPsnPlayers` | Members participating in the session |

# Push Events Relating to Game Sessions

| **Data Type** | **Request That Can Cause or Trigger the Push Event** | **Destination** |
| --- | --- | --- |
| `psn:sessionManager:gameSession:created` | Game Session created   * `createGameSessions` | Members of the created session |
| `psn:sessionManager:gameSession:deleted` | Game Session deleted   * `deleteGameSession` * `leaveGameSession` * `createPlayerSessions` * `leavePlayerSession` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members of the session before it is deleted |
| `psn:sessionManager:gs:maxPlayers:updated` | `maxPlayers` updated   * `setGameSessionProperties` | Members of the session |
| `psn:sessionManager:gs:maxSpectators:updated` | `maxSpectators` updated   * `setGameSessionProperties` | Members of the session |
| `psn:sessionManager:gs:joinDisabled:updated` | `joinDisabled` updated   * `setGameSessionProperties` | Members of the session |
| `psn:sessionManager:gs:customData1:updated` | `customData1` updated   * `setGameSessionProperties` | Members of the session |
| `psn:sessionManager:gs:customData2:updated` | `customData2` updated   * `setGameSessionProperties` | Members of the session |
| `psn:sessionManager:gs:representative:updated` | Representative has changed   * `leaveGameSession` * `createPlayerSessions` * `leavePlayerSession` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members of the session |
| `psn:sessionManager:gs:m:players:created` | A player has joined   * `createGameSessions` * `joinGameSessionAsPlayer` | Members of the session |
| `psn:sessionManager:gs:m:spectators:swapped` | A member changed from player to spectator   * `joinGameSessionAsSpectator` | Members of the session |
| `psn:sessionManager:gs:m:players:deleted` | Player has left   * `leaveGameSession` * `createPlayerSessions` * `leavePlayerSession` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members of the session before the user left |
| `psn:sessionManager:gs:m:p:customData1:updated` | Player's `customData1` updated   * `setGameSessionMemberSystemProperties` | Members of the session |
| `psn:sessionManager:gs:m:spectators:created` | New spectator has joined   * `joinGameSessionAsSpectator` | Members of the session |
| `psn:sessionManager:gs:m:players:swapped` | A member changed from spectator to player   * `joinGameSessionAsPlayer` | Members of the session |
| `psn:sessionManager:gs:m:spectators:deleted` | Spectator has left   * `leaveGameSession` * `createPlayerSessions` * `leavePlayerSession` * `joinPlayerSessionAsPlayer` * `joinPlayerSessionAsSpectator` | Members of the session before the user left |
| `psn:sessionManager:gs:m:s:customData1:updated` | Spectator's `customData1` updated   * `setGameSessionMemberSystemProperties` | Members of the session |
| `psn:sessionManager:gs:sessionMessage:created` | A session message was sent   * `sendGameSessionMessage` | Recipient user |
| `psn:sessionManager:gs:invitations:created` | Join slot reserved   * `createGameSessions` * `joinGameSessionAsPlayer` | User for whom a join slot has been reserved |
| `psn:sessionManager:gs:matchmaking:updated` | `matchmaking` updated   * If backfilling by the Matchmaking service succeeds | Members of the session |
| `psn:sessionManager:gs:searchable:updated` | `searchable` updated   * `setGameSessionProperties` | Members of the session |
| `psn:sessionManager:gs:m:p:natType:updated` | Player's `natType` updated   * `setGameSessionMemberSystemProperties` | Members of the session |
| `psn:sessionManager:gs:m:s:natType:updated` | Spectator's `natType` updated   * `setGameSessionMemberSystemProperties` | Members of the session |