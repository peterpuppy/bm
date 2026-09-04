# PlayStation™Network Multiplayer Best Practices – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Best_Practices/best-practices-for-other-multiplayer-exper.html

# Multiplayer Experience Best Practices Not Related to the Session Manager

This topic describes the best practices for enhancing multiplayer experiences through elements that are not directly related to the Session Manager service.

The best practices for enhancing multiplayer experiences that aren't directly related to the Session Manager service are as follows.

* [Using Multiplayer Activities and Game Intent Events](best-practices-for-other-multiplayer-exper.html#topic21770_3__section_activities-and-game-intent)
* [Using Advanced Player Profile Data in Matchmaking](best-practices-for-other-multiplayer-exper.html#topic21770_3__section_advanced-player-profile)

## Using Multiplayer Activities and Game Intent Events

For how to leverage activities and game intent events for multiplayer experiences, refer to [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html).

However, to take full advantage of these features, you must utilize activities set by the UDS tool and matches of the Session Manager.

## Using Advanced Player Profile Data in Matchmaking

The Advanced Player Profile is an API that provides aggregated data across the PlayStation®5 platform to game titles for enhancing the player experience. Data that is provided includes detailed stats about a player's network environment, social tendencies across various games, as well as their personal preferences. It is important to note that these pieces of data are intended to be indicators and used as inputs into your own systems in addition to any other data that you may be gathering that is game specific. We suggest using this feature as a starting point when you have little data about a player, or as additional information to build a stronger profile about a particular player in your game.

As a part of multiplayer matchmaking, games can use the data from Advanced Player Profile to create more engaging matches, select players with stronger network environments to host P2P matches, and suggest starting points or pre-populate certain in-game settings based on their previous experiences.

When performing matchmaking for a multiplayer game, there are some key pieces of data that can be looked at as indicators for matching players. These can be inputs into the PlayStation® matchmaking system or a custom solution.

For P2P games, there is the additional consideration of who should be selected as the host. This player does not necessarily have to be the "leader" of the room if the game supports that, but is simply the player selected in the background to marshal around traffic between participants. Selecting a strong host is key to reducing laggy gameplay experiences and hiccups when people quit out early.

After matchmaking is complete, additional pieces of data can be used as inputs to determine the person who is most suitable to host the game. Below are some examples of how Advanced Player Profile data can be used in your games:

* Bandwidth - Make sure that the host has sufficient bandwidth to host a room of the required size.
* NAT Connectivity - Select a host that has the best chance of establishing P2P connections with different NAT Types.
* Match Completion Rate - Understand if a player is likely to leave early from a match (resulting in mid-game host migration). Developers can also get results that are aggregated by every game's title.
* Play Style - Based on activities completed on the platform, determine the most frequent type of activity completed (competitive, progress, open ended, challenges).

For additional examples, refer to [Advanced Player Profile Overview](../../../WebAPI/latest/Advanced_Player_Profile-Overview/__document_toc.html).