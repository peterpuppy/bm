# PlayStation™Network Multiplayer Best Practices – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Best_Practices/using-player-sessions.html

# Best Practices for Using the Session Manager

The Session Manager is designed to more easily facilitate multiplayer gameplay. Appropriate use of the Session Manager should lead to more players playing your game and enjoying their online multiplayer experience. This topic introduces the topics to refer to regarding the best practices for using the Session Manager.

Refer to [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html) for details about the Session Manager.

The Session Manager includes two different types of sessions (real-time groupings of players). Refer to the following topic for information about how to incorporate these types of sessions into your game design.

* [Using Player Sessions and Game Sessions](using-player-sessions.html "This topic describes how to optimize usage of the Player Sessions and Game Sessions of the Session Manager service, as well as the points to consider when using them.")

Refer to the following topics for best practices related to Player Sessions.

* [Obtaining a List of Friends' Player Sessions Using an API Request](api-access-to-player-sessions.html "This topic shows you how to obtain a list of the Player Sessions that are joined by friends from inside the game and how to enable the joining of sessions from the in-game friends list.")
* [Sending Invitations Appropriately](sending-invitations.html "This topic briefly introduces all the methods and precautions for sending invitations to Player Sessions.")
* [Appropriately Handling Push Notifications from the Platform](handling-push-changes-from-the-platform.html "This topic covers the processing that should be performed by the game when it receives push notifications from the platform regarding changes made to a session.")
* [Using Game Intent Events](handling-game-intents.html "This topic covers the purpose of using game intent events and provides references for understanding the game intent system.")
* [Mapping Player Sessions and In-Game Systems](mapping-to-in-game-systems.html "Mapping Player Sessions and in-game systems together, as well as performing appropriate control, is important to making it so that players can safely interact with other players in the game while participating in sessions within the system. This topic describes the key points that should be noted when mapping a Player Session and an in-game system to each other.")
* [Key Values and Points to Consider for Operating Player Sessions](key-player-session-values.html "When creating and managing Player Sessions, there are some key values ​​and points to consider for operating the sessions. This topic provides a summary of those values and points.")

Refer to the following topic for best practices and limitations regarding the method and timing to enable voice chat.

* [Best Practices Related to Voice Chat](setting-up-voice-chat.html "This topic describes the best practices and limitations of the Session Manager service when adding or changing voice chat.")

## Limitations on PlayStation®4

The limitations when using the Session Manager service on PlayStation®4 are as follows.

* When the Session Manager is used in a game on PlayStation®4, "Joinable" will not be displayed for players in What's New, communities, or friends lists. ("Now Playing" will be displayed.) "Joinable" will be displayed on the player's profile if the player is joined in to a Player Session.
* The voice chat feature provided in the PlayStation®5 SDK is not supported on PlayStation®4. This is because there is not enough system resources available. If you are building your game to support cross-gen gameplay, use proprietary voice chat.

# Using Player Sessions and Game Sessions

This topic describes how to optimize usage of the Player Sessions and Game Sessions of the Session Manager service, as well as the points to consider when using them.

## Optimal Usage of Player Sessions

Player Sessions are designed to facilitate players to create their own groups and enjoy gameplay for an extended period of time. These groups can be multiple dungeons, matches, levels, etc. A player can only be in one Player Session at any given time. In many games, these groups are generally called squads, fireteams, etc. In addition, Player Sessions are the primary way to have players invite their friends or group to your game.

Generally, it is good practice to create Player Sessions for all players who are currently available to play an online multiplayer game. This includes players sitting in a lobby, players waiting for game matchmaking, and players playing a round. These Player Sessions are expected to last a long time; a Player Session should be continued as long as a player is available to play an online multiplayer game. Terminating a Player Session disables and removes all invitations and corresponding system UI so players can no longer participate in that session, and an error will be returned when they attempt to do so. It is good practice to not terminate sessions unless absolutely necessary.

When a player joins a Player Session, several factors are checked to determine whether the session can be joined by others. If it can be joined by others, the session is promoted to other players throughout the system's user experience. For this promotion to happen, the target player must have the game installed, the session-side must be allowing players to join it, the player must be included in the settings for who can join the session or be invited to the session, and there must be an empty slot in the session. Most notably, this promotion happens in the game's hub and the Control Center.

Player Sessions Promoted in the Control Center
Player Sessions Shown in the Game's Hub

In addition to joinable Player Sessions being promoted in the Control Center and the game's hub, Player Sessions also appear on the profiles of joined in members regardless of whether they can be joined by others.

Player Session Shown on the Player's Profile

## Optimal Usage of Game Sessions

Game Sessions are a utility for facilitating your online multiplayer game. Any player can be joined in to multiple Game Sessions at once; players have no control over these Game Sessions.

In addition, Game Sessions aren't displayed to players in the system UI. The main use cases for Game Sessions are setting up P2P signaling, performing matchmaking, and enabling voice chat.

# Obtaining a List of Friends' Player Sessions Using an API Request

This topic shows you how to obtain a list of the Player Sessions that are joined by friends from inside the game and how to enable the joining of sessions from the in-game friends list.

In addition to using the system menu for joining friends' Player Sessions, an API request can be used to directly access friends' Player Sessions from inside the game. If you are providing an in-game friends list and want to enable a feature for joining sessions from that UI, you can do so using the `getFriendsPlayerSessions` API request that obtains a list of the Player Sessions that are joined by friends. This API request enables you to obtain all the Player Sessions that are joined by friends on the friends list at once, as well as information about whether those Player Sessions can be joined.

It is recommended that you make session joining possible from the in-game friends list as it will enable players to join sessions directly from the UI without having to navigate the system menu.

# Sending Invitations Appropriately

This topic briefly introduces all the methods and precautions for sending invitations to Player Sessions.

When sending invitations from inside the game, you have two options. One is to build the entire user experience in your game using a Web API to send invitations, and the other is to use an API request that calls the invitation flow from a system overlay. In general, if you're designing your game to allow players to see their social graph (friends list, clan list, etc.) in-game, it's best to directly use the API. If you are using a generic invite button, you must enable the sending of invitations using the platform.

Note that a player can invite everyone in a group with a single invite when the platform feature is used, but this is not currently possible when the Web API is used. However, this shouldn't be a major issue since players will still be able to invite everyone in a group with a single invite using the system UI even when you choose to use the Web API.

# Appropriately Handling Push Notifications from the Platform

This topic covers the processing that should be performed by the game when it receives push notifications from the platform regarding changes made to a session.

Once a session is created, the platform can send push notifications using the specified push context. Because you'll be notified of the changes made to a session, you'll be able to display the session properly in your game UI and service.

Players can make changes to their session at the platform level. This includes changing the privacy level, changing the leader, switching between player and spectator, and kicking out another player. When these changes are made and the session is displayed in-game, the changes must also be handled on the game side. When any one of these changes are made, updates will be sent via push notifications to the push context set up when creating the Player Session. These updates should be handled ASAP so that the display of the session in the game matches the display of the session on the platform. The platform side also performs the same processing for change notifications that are sent from a game-side session using an API request to ensure that the display of the session is always the same in the game as on the platform.

Refer to "[Mapping Player Sessions and In-Game Systems](mapping-to-in-game-systems.html "Mapping Player Sessions and in-game systems together, as well as performing appropriate control, is important to making it so that players can safely interact with other players in the game while participating in sessions within the system. This topic describes the key points that should be noted when mapping a Player Session and an in-game system to each other.")" for the points to consider for appropriately controlling the changes made to a session at the platform level in the game.

# Using Game Intent Events

This topic covers the purpose of using game intent events and provides references for understanding the game intent system.

Game intent events allow a platform to launch a game (or send a message if it's already running) with a well-formatted deep link payload. This feature is used when a player launches a game from a challenge activity or joins a session from a platform. Game intent events are categorized into 3 types:

* **launchActivity** - used when the player directly plays their own challenge activity
* **joinSession** - used when the player directly joins another player's session
* **LaunchTournamentMatch** - used when the player starts a tournament match

The types of game intent events that can be used are described in detail in [Game Intent System Overview - Game Intent Event Types and Properties](../Game_Intent_System-Overview/game-intent-event-types-and-properties.html). The [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html) also provides explanations about joining sessions that are displayed by the UI and sending invitations to players or groups.

# Mapping Player Sessions and In-Game Systems

Mapping Player Sessions and in-game systems together, as well as performing appropriate control, is important to making it so that players can safely interact with other players in the game while participating in sessions within the system. This topic describes the key points that should be noted when mapping a Player Session and an in-game system to each other.

Many games have their own internal session systems in order to support their own needs. While this is fine (even great in many cases), it is important to map such systems to Player Sessions. This serves as the key entity in the system and is used for players to interact with each other in a multiplayer game.

There are a few key points to note when mapping these systems together.

* **Creation and Lifetime**

  Generally, a Player Session must be created when a player enters a multiplayer context that they've been allowed to join by another player. This includes the scenario where a player sits in a lobby and waits for game matchmaking. Creating a Player Session as soon as a player enters a multiplayer context ensures that the session is visible to the player's friends throughout the system UI. Player Sessions are designed to last a long time, and it is good practice not to end sessions while the player is still in a multiplayer context. Even if a match is already going on and the player can't actively play until it ends, enable the player to still join the session and let them wait or participate as a spectator until the next round can begin.
* **Name**

  When in-game group names are set in the game, make sure the names match the names of the Player Sessions. This allows players to immediately recognize groups and take key actions quickly within the system.
* **Membership**

  Make sure the members of the in-game session match those in the Player Session. This allows the players to easily find each other and take key actions such as kicking out players from the session or transferring leadership between players. In addition, because this prevents sessions that are at full capacity from being displayed as joinable, other players won't have the unpleasant experience of trying to join a friend's session and being rejected.
* **Leadership**

  Player Sessions have leaders. This leader defaults to the person who joins the session first. If that person leaves the session, leadership is passed on to other players based on the order by which players joined the session, unless leadership is transferred explicitly to a specific player by the previous leader or the game. Make sure platform leadership aligns to the game's leader. If you use a different method for passing leadership instead of the joining order, make sure that leadership is passed to the appropriate player in the Player Session when the leader leaves the session. This makes sure the right player has the right level of control at all times.
* **Privacy/Permissions**

  This may be one of the trickiest points as in-game systems may handle joinability, privacy, and permissions differently than the platform. If the joinability of in-game sessions doesn't align to the platform values of "anyone", "friends of friends", "friends", and "no one", you need to set up your session to not allow the player to change the setting from the platform level. You can do this by not granting that privilege to the leader of the group through leader privileges. In addition, you should still keep the Player Session's privacy setting as up to date as possible so that even when the player changes it in-game, the right sessions to join can be suggested to the right players. In addition, if the kicking out of players is supported in the game, the privilege to do so should only be granted to the leader. If this feature is not supported, do not grant the privilege.

# Key Values and Points to Consider for Operating Player Sessions

When creating and managing Player Sessions, there are some key values ​​and points to consider for operating the sessions. This topic provides a summary of those values and points.

A list of properties for operating Player Sessions is provided in [Session Manager Web API Overview - Types of Sessions and Their Main Properties - Player Sessions](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/player-sessions.html). Refer to [Session Manager Service Overview - Usage Guides - Usage When You Have a Proprietary Game Server](../Session_Manager_Service-Overview/usage-when-you-have-a-proprietary-game-server.html) for the timings at which to update these values and how to perform the update.

* `maxPlayers` - Set the maximum number of players that can join the session as players. This value tells the platform how many people can be in the session at any given time. If the maximum number of players is reached, players will not be able to join the session from the system UI. The maximum number of players for a Player Session is 100. Note this number is not the same as the total number of players that can be in a match at the same time. (For example, let's assume players are playing trios in a 100-player battle royal. In this case the match supports up to 100 players, but the session should only support up to 3 players since players can only join this mode in groups of 3 or less.) In a Player Session that supports cross-platform gameplay, there will be both players of PlayStation™Network and other players.
* `maxSpectators` - Set the maximum number of players that can join the session as spectators. This is designed to support in-engine spectators. If this number is greater than zero, a "Watch" button will be displayed in addition to the "Join" button, and players will be able to join the session as spectators from the platform. If the maximum number of spectators is reached, players will not be able to join the session as spectators from the system UI.
* `swapSupported` - When true is set, this means the player can switch seamlessly between being a player of PlayStation™Network and being a spectator without having to first leave the session. When true is set, the player will be able to switch between being a spectator and a player using the system UX while they are joined in to the session. Set false when not supporting this feature.
* `joinDisabled` - This flag allows you to temporarily prevent players from joining the session. While true is set, any player attempting to join the session is denied to do so no matter what. This should only ever be used for major use cases and for short periods of time when the joining of players may disrupt the system.
* `supportedPlatforms` - Set from which PlayStation® platforms users can join the session. PlayStation®4, PlayStation®5, or both can be set. This setting will enable sessions and invitations to be shared between PlayStation®4 and PlayStation®5 systems. If you want to provide cross-gen support, you need to migrate to the Cross-Gen build of the PlayStation®4 SDK. Refer to the "[Limitations on PlayStation®4](best-practices-for-using-session-manager.html#best-practices-for-using-session-manager__section_ps4-limitations)" section of "[Best Practices for Using the Session Manager](best-practices-for-using-session-manager.html "The Session Manager is designed to more easily facilitate multiplayer gameplay. Appropriate use of the Session Manager should lead to more players playing your game and enjoying their online multiplayer experience. This topic introduces the topics to refer to regarding the best practices for using the Session Manager.")" for the limitations that apply when doing so.
* `nonPsnSupported` - Set whether players that aren't players of PlayStation™Network can join the Player Session. This setting will enable you to support cross-platform gameplay among PlayStation® platforms and other game platforms. This value is specified upon creating a Player Session and cannot be changed later. Refer to the "[Limitations](best-practices-for-cross-platform-play-exp.html#best-practices-for-cross-platform-play-exp__section_cross-platform-limitations)" section of "[Best Practices for Supporting Cross-Platform Gameplay](best-practices-for-cross-platform-play-exp.html "This topic describes the best practices and limitations when supporting cross-platform gameplay in Player Sessions of the Session Manager service.")" for the limitations that apply when supporting cross-platform gameplay.
* `expirationTime` - Specify the validity period of a Player Session that supports players that aren't players of PlayStation™Network. This value is specified upon creating a Player Session and cannot be changed later.
* `localizedSessionName` - This is the main name that is shown within the system UI when referring to the Player Session. This name should match whatever terminology is used for in-game groups such as "squads", "fireteam", or "group". We strongly advise against using the terminology of "party" anywhere in this string as it clashes with the system concept/feature called parties and causes significant confusion for players. If you do need to use party because it aligns with the name of your in-game groups we suggest adding a prefix such as "(Game Name) Party". In addition, "Game Group" will be used if you do not set a name here. Since this name is shown in the UI and is visible to players please DO NOT name this "Player Session" or "localizedSessionName".
  Session Name Appearing in the Profile UX

* `joinableUserType` - Set which players of PlayStation™Network can join the session without invitations. Participation is controlled based on the group leader's friendships. Anyone, Friends of Friends, Friends, No One, or Specified Users can be set. Players can change this setting from the system menu as well as in the game if the game provides the UI to do so. It is good practice to give the players this level of control as different players have different privacy needs. A player viewing a Player Session that they haven't been allowed to join yet can ask the session leader for an invite using the Request to Join feature. Request to Join is available to a Player Session viewer when the session leader allows messages from the viewer via their privacy settings and the viewer's relationship to the session leader is not covered in the currently selected "Who Can Join" Player Session settings. The Specified Users setting also allows specific users to join a session without invitations. This is generally used when there is an in-game "clan" system or something similar that allows a graph of players not represented at the platform level to join a session. If you this setting, you need a list of players in the `joinableSpecifiedUsers` field of the session as well. If you use the Specified Users option, "Other" will be displayed in the system UX, and the leader will be unable to change this setting from the system UX.
* `joinableSpecifiedUsers` - This represents a list of arbitrary players of PlayStation™Network that can join the Player Session. The maximum number of players is currently set to 32.
* `invitableUserType` - Specifies which members of the Player Session can create and send an invite. It can be set to leader only, all members, or no one. Based on what is set here, the platform will indicate to the appropriate players that it is possible to send an invite. In general, give all players the ability to invite others unless there is some game design reason for limiting the functionality.
* `leaderPrivileges` - You can give the leader of the group privileges that allow them to take certain actions in relation to the session. This includes whether they can kick out other members in the group or whether they can change the `joinableUserType` setting. It is generally good to give the leader these privileges as it allows them more control of the session to make sure they get the right players in with them and can play safely.
* `disableSystemUiMenu` - You can remove certain actions of the group leader in relation to the session from the system software. The specified action item will become inoperable from the system software but will be usable from within the game. Only use this when there is risk that operation from the system software will cause a problem in the management of the game's session.
* `customData` - There are multiple custom data fields that you can add in order to transfer data within the session. There are two `customData` fields that are global to the session and two for each individual player that can be used to pass data about individual players. These are extremely useful for mapping Player Sessions to in-game systems but can also be used for a myriad of things that you need.

# Best Practices Related to Voice Chat

This topic describes the best practices and limitations of the Session Manager service when adding or changing voice chat.

The best practices for supporting voice chat are as follows.

* [Points to Consider When Setting up Voice Chat](setting-up-voice-chat.html#topic21770_2_3__section_setting-voice-chat)
* [Only Enabling Voice Chat in One's Own Player Session (or In-Game Equivalent)](setting-up-voice-chat.html#topic21770_2_3__section_adding-voice-chat-player-session)
* [Controlling Chat Groups with Game Sessions](setting-up-voice-chat.html#topic21770_2_3__section_controlling-voice-chat-game-session)
* [Appropriately Handling Push Notifications from the Platform](setting-up-voice-chat.html#topic21770_2_3__section_handling-push-changes)

Refer to the following section for the limitations regarding voice chat.

* [PlayStation®4 Limitations](setting-up-voice-chat.html#topic21770_2_3__section_ps4-limitations)

## Points to Consider When Setting up Voice Chat

When adding voice chat to your game, there are two options for how you can support it. You can use the VoiceChat library or your own proprietary voice chat system. Platform voice chat on PlayStation®5 is greatly improved over previous generations. It uses a high-quality voice codec, runs entirely within system resources, and automatically provides accessibility capabilities like text-to-speech and speech-to-text. In addition, it also provides the player more control at the system level. The PlayStation®5 SDK also provides support for games that use off-platform voice chat solutions or middleware. However, controls for such voice chat channels must be handled entirely in-game.

When setting up a voice chat channel using the PlayStation®5 SDK you have the ability to name that channel. This name appears in the channel switching UX so players can identify them. It is generally good practice to align these names with game concepts such as "squad chat" or "team chat" so players can easily recognize their purpose and who they can expect to talk to. This can be changed in real time so that if the functionality of the channel changes, you can update it as necessary.

## Only Enabling Voice Chat in One's Own Player Session (or In-Game Equivalent)

Regardless of whether a proprietary voice chat or the platform solution is used, the player should only enable voice chat in their Player Session. This allows the player the ability to only communicate with trusted players so that they don't have to talk with players who may make them uncomfortable or is abusive. By tying a voice chat channel to a Player Session, you are keeping the player safe while still allowing them to communicate.

To enable voice chat for the current Player Session, the game needs to use the VoiceChat library to create a new voice chat channel. When creating the channel, the game provides the name to use and the session ID to associate it with. Once the channel is created, the player can discover and chat within the channel if they are in the Player Session.

When adding voice chat to a Player Session, it is generally good practice to only do this if the number of players in the session is greater than one as once the channel is created it begins to appear in the UI for the player. The player may also be auto-switched to the created channel if they are only in a chat channel that is associated with a Game Session. It is also good practice to remove the channel if the number of players drops to one. It is a very lonely online experience if voice chat is added and kept around when only one player is in the Player Session.

## Controlling Chat Groups with Game Sessions

One of the main use cases for making Game Sessions is to easily attach chat channels to them. This allows you to set up voice chat between any arbitrary grouping of players based on game design (teams, guild chat, and more). When using a voice chat channel that has been added to a Game Session, you can use more features. For example, you can set up virtual groups (called chat groups) within a single channel. With the chat group feature, you can group players in the same channel into smaller groups and control who can talk to whom in real time. A great example of this is enabling voice chat for a whole lobby (a single chat group), then splitting the group into two teams (two separate chat groups) once their match starts. This chat group feature allows you to change who can talk to whom in real time.

## Appropriately Handling Push Notifications from the Platform

Similar to sessions, you can get push updates from the platform when changes occur in voice chat. It is generally good to handle these ASAP to make sure that actions by the player (such as joining a channel or muting audio) are correctly reflected in the game.

## PlayStation®4 Limitations

The voice chat feature provided in the PlayStation®5 SDK is not supported on PlayStation®4. This is because there is not enough system resources available. If you are building your game to support cross-gen gameplay, use proprietary voice chat.