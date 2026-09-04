# PlayStation™Network Multiplayer Platform Concept Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Platform_Concept-Overview/multiplayer-platform-main-features.html

# Main Features of the Multiplayer Platform

The Multiplayer Platform consists mainly of Session Manager, matches, and game intents. This topic describes these features in a simple terms.

* **Session Manager** helps game developers to find and facilitate real-time groupings of players within their games and to enable the core communication paths between them. When used, multiplayer groupings appear throughout the console experience bringing players together and allowing players to manage their play experience with others. Session Manager enables you to send data between players and set up system-resource-backed voice-chat channels. Session Manager also has brand new matchmaking functionality to help you find proper groupings of players to play. For details about Session Manager, refer to [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html).
* **Matches** allow you to provide rich progress, scores, and results for multiplayer activities. Matches are used to bring together the experiences of participating players as one cohesive experience for all matched players. Matches work in conjunction with the Activities framework. See the [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html) for more information on how these two systems work together.
* **Game Intent** enables players to transition from system context to the game's context in the fastest way possible, leveraging the information known about the game as provided by Session Manager, matches, and activities. These may be sent for single player or multiplayer experiences. For details about game intents, refer to [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html).