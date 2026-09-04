# PlayStation™Network Multiplayer Best Practices – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Best_Practices/best-practices-for-cross-platform-play-exp.html

# Best Practices for Supporting Cross-Platform Gameplay

This topic describes the best practices and limitations when supporting cross-platform gameplay in Player Sessions of the Session Manager service.

Refer to "Player Session" of [PlayStation™Network Multiplayer Platform Concept Overview](../PSN_Multiplayer_Platform_Concept-Overview/__document_toc.html) for information about cross-platform gameplay in Player Sessions.

The best practices for supporting cross-platform gameplay are as follows.

* [Sending Invitations to PlayStation® Platforms](best-practices-for-cross-platform-play-exp.html#best-practices-for-cross-platform-play-exp__section_send-invitation-to-platform)
* [Synchronizing Session Information](best-practices-for-cross-platform-play-exp.html#best-practices-for-cross-platform-play-exp__section_synchronization-of-session-information)
* [Communicating That a Session Can Be Joined without an Invitation](best-practices-for-cross-platform-play-exp.html#best-practices-for-cross-platform-play-exp__join-session-without-invitation)

Refer to the following section for the limitations that apply when supporting cross-platform gameplay.

* [Limitations](best-practices-for-cross-platform-play-exp.html#best-practices-for-cross-platform-play-exp__section_cross-platform-limitations)

## Sending Invitations to PlayStation® Platforms

When a player that isn't a player of PlayStation™Network invites a player of PlayStation™Network to a session from within the game, the invitation can be sent to a PlayStation® platform. It is recommended that the invitation be sent to a PlayStation® platform to make it easier for the player of PlayStation™Network to realize that they've been invited to a session. For usage, refer to [Session Manager Web API Overview - Using the Web API - Basic Usage of Player Sessions (for non-PlayStation™Network Users)](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/basic-usage-of-player-sessions-for-non-psn-users.html).

## Synchronizing Session Information

When supporting cross-platform gameplay, you need to synchronize information of the sessions managed by the game server with Player Session information. When a player that isn't a player of PlayStation™Network starts a session, the creation of the Player Session can be at the start of the session.

A Player Session must be created before a player of PlayStation™Network joins a session for the first time or before a player that isn't a player of PlayStation™Network sends a platform invitation to a player of PlayStation™Network. If a Player Session is not created at the start of a session and players that aren't players of PlayStation™Network are already in the session, make sure to add a new Player Session before these times.

A Player Session is deleted when there are no more members. If the session managed by the game server continues to exist even if there are no members, recreate the Player Session as necessary.

## Communicating That a Session Can Be Joined without an Invitation

The `joinableUserType` value is not set for players that aren't players of PlayStation™Network. If you are allowing players that aren't players of PlayStation™Network to join a Player Session beyond the `joinableUserType` scope specified for it, we recommend that you communicate this to the players in the game.

## Limitations

Note the following limitations when supporting cross-platform gameplay.

* **Voice Chat**

  The voice chat feature provided in the PlayStation®5 SDK is not supported by Player Sessions that support cross-platform gameplay. This is because players that aren't players of PlayStation™Network cannot be covered. If you are building your game to support cross-platform gameplay, please use proprietary voice chat.
* **Signaling**

  The signaling API features of PlayStation®5 cannot be used by Player Sessions that support cross-platform gameplay. This is because players that aren't players of PlayStation™Network cannot be covered.
* **Reporting and Moderation**

  Players that aren't players of PlayStation™Network are outside the scope of reporting and moderation of PlayStation® platforms. Please take appropriate action on the game side.
* **Request to Join**

  The Request to Join feature, by which you can send a request for joining a Player Session that you're not yet allowed to join to the session leader, cannot be used if the session leader is not a player of PlayStation™Network.
* **joinableUserType and joinableSpecifiedUsers**

  The limitations regarding the range of players that can join a session set by `joinableUserType` apply to players of PlayStation™Network but not to other players. In addition, it is not possible to specify players that aren't players of PlayStation™Network for `joinableSpecifiedUsers`.