# PlayStation™Network Multiplayer Platform Concept Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Platform_Concept-Overview/technical-concepts.html

# Technical Components That Constitute the Multiplayer Platform

The support for a cohesive experience using the Multiplayer Platform is provided by a combination of multiple technical components. This topic describes the signature technical components that constitute the Multiplayer Platform and the technical concepts behind them.

## Player Session

*Player sessions* support groups of players playing with each other for extended periods of time; for example, multiple dungeons, matches, levels, and so on. Players can be in only one player session at any time per PlayStation® platform.

These sessions enable invitations to be sent between players by means of the player invitation dialog or by means of your own code that calls the appropriate Web API. On the PlayStation®5 console, players in a player session can send invitations both to individual players and to message groups and initiate those invitations from outside the game via system UI.

Each player session contains many properties that your code can use to modify how they work for given players, including privacy settings, blocking joins, setting who can invite, and so forth. Some of the settings such as the privacy setting can be changed by the player through the platform UX.

When players enter a portion of the game in which they can be joined actively by others or they can invite others, you should create a player session for them in order to facilitate other players joining the group to play the game.

To support cross-generation play and invitations between PlayStation®4 and PlayStation®5, you must support player sessions in both versions of your game.

Player sessions support cross-platform play in which users can engage in play taking place between PlayStation® platforms and other platforms and in which players not in PlayStation™Network can send invitations to users of PlayStation™Network.

For details about player sessions, refer to the [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html).

## Game Session

*Game sessions* support arbitrary groupings of players as necessary by the game; for example, random matchmaking, open world, and so on. Game sessions are completely optional from the platform perspective, but they offer your code great flexibility to enable matchmaking, to set up chat channels, and to run synchronous gameplay experiences through signaling. The player can be in many game sessions at a given time, as many complex games need this feature in order to function.

Ideally, you create game sessions whenever you need them to facilitate matchmaking, signaling, or voice chat and destroy them whenever they are no longer needed.

Game sessions are also supported on PlayStation®4 to enable cross-generation play.

For details about game sessions, refer to [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html).

## Matchmaking

*Matchmaking* is the act of automating the discovery of groups of players for an in-game experience. Session Manager implements queue-based matchmaking, in which players searching for a match are added to a queue while waiting to find a match. When the matchmaker finds groups of players that satisfy a specific ruleset, it moves those players into a game session in order to facilitate the gameplay experience. Queue-based matchmaking allows for flexible growth of matchmaking pools and is the current industry standard.

Matchmaking sessions are also supported on PlayStation®4 to enable cross-generation play.

For details about matchmaking, refer to [Matchmaking Overview](../../../WebAPI/latest/Matchmaking-Overview/__document_toc.html).

## Voice-Chat Channel

A *voice-chat channel* is a specific group of players who can talk to one another through their microphones. Players may be in many chat channels at once in order to facilitate the complexities of gameplay, but they can listen and talk on only one channel at a time. You can create voice chat channels by means of the VoiceChat library in Session Manager or through proprietary means.

For details about the VoiceChat library, refer to [VoiceChat Library Overview](../VoiceChat-Overview/__document_toc.html). For details about cases in which you might create a propriety voice chat, refer to [ProprietaryVoiceChatHelper Library Overview](../ProprietaryVoiceChatHelper-Overview/__document_toc.html).

## Match

A *match* is a specific instance of a multiplayer or competitive activity. A match always contains the players who are participating in said instance or who have taken part in said instance, as well as the final result for those who have finished. Matches are a core part of the way that players find other players to play with, and they are the way that players can relive past experiences with friends.

For best practices when using matches, see [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html).

## Game Intent

A *game intent* is a strongly typed deep link that enables the player to transition from platform context to game context in order to bring the player to their desired gameplay experience quickly and easily. Game intents enable players to initiate complex in-game experiences from the platform to get the most out of their gameplay experiences.

For details about game intents, refer to [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html).