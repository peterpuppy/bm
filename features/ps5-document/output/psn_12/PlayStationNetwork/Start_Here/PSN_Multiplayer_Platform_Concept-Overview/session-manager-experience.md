# PlayStation™Network Multiplayer Platform Concept Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Platform_Concept-Overview/session-manager-experience.html

# Experiences That Use the Multiplayer Platform

The Session Manager and game intents that constitute the Multiplayer Platform make it easier for players to find and join multiplayer gameplay that is in progress. Developers can provide a consistent, easy-to-use experience for players who want to play multiplayer games on PlayStation® platforms.

Session Manager and game intents make it easier for gamers to find and join multiplayer gameplay. Session Manager is a brand-new platform built from the ground up for PlayStation®5 in order to improve the overall multiplayer experience for games on PlayStation®5.

When used together or piecemeal, these features (sessions, invitations, signaling, voice chat, matchmaking, game intents, and matches) create a consistent, easy-to-use experience for players who want to play multiplayer games on PlayStation® platforms. These features make it easier than ever for players to form groups with other users, chat, and play games.

The following topic explains how Session Manager, matches, and the game intent feature help players and your company's games while providing examples of the user experience.

* [Session Manager Experience](session-manager-experience.html "This topic explains how Session Manager helps players and your company's games while providing examples of the user experience.")
* [Matches Experience](matches-experience.html "This topic explains how the matches features benefit players and your game while providing examples of the user experience.")
* [Game Intent Experience](game-intent-experience.html "This topic explains how the game intent feature helps players and your company's games while providing examples of the user experience.")

# Session Manager Experience

This topic explains how Session Manager helps players and your company's games while providing examples of the user experience.

Session Manager helps game developers to create, find, and facilitate real-time groupings of players within their games; it functions as the central pillar for communications among players. This is the core of the Multiplayer Platform, enabling the major use cases of players joining games with other players and of users playing together while communicating.

These real-time groupings are known as sessions. As a developer, you can create and manage sessions throughout your game experience to enable players to play together. Sessions can be used to ensure that players transition smoothly from system context to in-game context. Once a session is established, you can enable signaling between its members quickly, thereby enabling them to exchange packets of gameplay data in real time. When you use the platform's signaling APIs it handles NAT traversal, managing firewall rules, and other challenging tasks related to passing data between players in a session.

Developers can use the following types of sessions within a game:

1. *Player sessions* support groups of players who play with each other for extended periods of time; for example, multiple dungeons, matches, levels, and so on.
2. *Game sessions* support arbitrary groupings of players as necessary by the game; for example, random matchmaking, open world, and so on.

A player session enables in-session players to send invitations to players outside the session in order to get together within the game. Additionally, player sessions appear throughout the console to make it easy for players to join and manage them. Players who are viewing a player session that they aren't currently in can ask the session leader for an invite using the Request to Join feature. Request to Join is available to a player session viewer when the session leader allows messages from the viewer via their privacy settings and viewers relationship to the session leader is not covered in the currently selected "Who Can Join" player session settings. See [Session Appearing in the UX](session-manager-experience.html#session-manager-experience__uuid-cd9cfa25-ea03-f832-09a0-df159d33b851_figure-idm232224994080738) for an example session in the UX. In this image, the first card shows session and match together. The fourth card shows joinable player sessions from friends.

Session Appearing in the UX

Game sessions are a utility for you as a game developer and do not appear in the system UX. They are extremely useful for when your experience requires players to be matchmade together with players not in their player session using our matchmaking system or your own.

When a player decides to participate in an in-game activity that requires finding additional players, your application can use a queue-based matchmaking solution that Session Manager provides to find groups of players based on your pre-defined ruleset. When the matchmaker finds a potential grouping, the matchmaking system automatically creates a game session to house the gameplay experience and it returns that session to the game. This is a brand-new matchmaking system for the PlayStation®5 generation but can also be utilized by cross-generation titles on PlayStation®4.

When creating either type of session, you have the option to attach voice-chat channels to the session. Any voice channel made through this method runs in system resources and your code does not need to manage these chat channels. Additionally, these chat channels will support both text to speech and speech to text without any changes from you as a developer. When using system voice chat, the player can switch between available voice chat channels manually and can mute other players through the system software. (See [Chat Channel Switching](session-manager-experience.html#session-manager-experience__uuid-cd9cfa25-ea03-f832-09a0-df159d33b851_figure-idm232224999384009).)

Chat Channel Switching

Alternatively, your code can implement its own voice-chat channel. If you go this route, the system software will only allow for the player to swap their microphone between party voice chat and the game's chat.

# Matches Experience

This topic explains how the matches features benefit players and your game while providing examples of the user experience.

When players are playing in multiplayer or competitive activities in your game (see the [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html)), your code can expose this information to the platform. To do so, you can use matches to create the context necessary to inform the platform of the basics of the experience. For example, you might provide information such as the activity being played, the members of each team, the map being used, scores, and results. As matches are created, they appear in conjunction with sessions to incentivize players to join the session and play together with their friends in real time. (See [Player Session Appearing in the Control Center UX](matches-experience.html#matches-experience__uuid-cd9cfa25-ea03-f832-09a0-df159d33b851_figure-idm232225009725489).)

Player Session Appearing in the Control Center UX

When match results are reported, the matches become part of each player's history, enabling them to play the same activity again with the same friends later. Currently, this only appears to players to play again in the suggested activity user experience, but we are retaining this information for future features.

Matches will also be leveraged in tournament features. If your game is competitive in nature, these features are extremely valuable.

# Game Intent Experience

This topic explains how the game intent feature helps players and your company's games while providing examples of the user experience.

Game intent enables players to transition from system context to the game's context in the fastest way possible, leveraging information about the game that Session Manager and challenge activities provide.

When players interact with sessions, tournaments, and challenge activities throughout the platform UX, they can initiate game intents that inform the game executable about what the player wants to play, thus lowering the time from play trigger to gameplay. Game intents are strongly typed deep links that inform the game of what the player is trying to do within the game. Game intents can include a session, a tournament, and a challenge activity, allowing the system to initiate complex gameplay experiences in your title and to smooth out the player's experience in launching the game.

When receiving a Game intent, it is best practice to move the player in the game to the experience described in the intent within the limits of your game's design. When receiving a new session via a game intent, you may want to wait until all players arrive and connect before initiating the experience, although this is game design dependent. An example of this kind of processing is moving the player to the lobby while pre-selecting a challenge activity, among other methods. In general, it is best practice to also use the most recently saved file, unless your game requires the user to choose one. For more on best practices, see [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html).