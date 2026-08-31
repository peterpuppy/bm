# Session Manager Service Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Session_Manager_Service-Overview/the-lifecycle-of-player-sessions-game-sessions-and-matches.html

# Major Components of the Session Manager Service

# Player Sessions

A Player Session is a session created for the purpose of users playing together, for example, by forming in-game parties. Usage of this feature could take the following form: The members who have joined a session together play competitively against other users, and once that fight is over, they then fight a different set of users while maintaining the same Player Session. There are two types of Player Sessions available: a Player Session that only users of the PlayStation™Network can participate in, and a Player Session that both users of the PlayStation™Network and non-users can participate in. A user of the PlayStation™Network can only participate in one Player Session at once. A Player Session always has one leader. The leader has special privileges, such as being able to set the conditions for joining the Player Session.

Use the Player Session feature in applications in which you intend to use the invitation feature. Note that users who have not received explicit invitations, if conditions pertaining to the Player Session allow it, can use features of the system software to search for Player Sessions and jump in to participate.

# Game Sessions

A Game Session is a session that can be used for arbitrary purposes within applications during online multiplayer gameplay, such as for providing sessions for competitive gameplay or lobby-like sessions for communicating. The Session Manager service has no restrictions on users simultaneously participating in multiple Game Sessions. When sessions are being managed by a game server or there is otherwise no need for the feature, it is not mandatory to use Game Sessions.

Note that users cannot invite other users to Game Sessions. Invitations are only used with Player Sessions; follow the procedure of making users join the appropriate Game Sessions after they have joined a Player Session. Applications that do not require invitations can use Game Sessions only, without using Player Sessions.

# Players and Spectators

To support in-game modes where participants view other users' gameplay, you can provide both "player" slots for users to play the game and "spectator" slots for users to view gameplay in both Player Sessions and Game Sessions. When a user joins a session, it must be explicitly specified whether they are joining as a player or as a spectator. Because players who have joined as spectators have done so for the purpose of watching others play, rather than of playing, themselves, program the application to treat such players in that way (there is no problem if users who have joined as players watch without playing).

# Matches

A "match" represents a "container" for recording gameplay statuses and results.

The gameplay modes (e.g., "team death match" or "capture the flag") provided by an application are defined ahead of time as "activities", and the application reports matches linked to those activities to PlayStation™Network. This allows users to flaunt their gameplay statuses, results, and histories outside games, such as by displaying this information on the users' profile screens, and can make gameplay a livelier experience.

What constitutes a match can be defined arbitrarily based on gameplay. Both online multiplayer and single player gameplay can be supported.

# Matchmaking

Matchmaking is a feature for finding other players online for competitive or cooperative play. When an application issues a matchmaking request to a server, the server creates a Game Session as soon as other players are found and then returns the session to the application; matchmaking is thus an asynchronous-type system. Conditions, such as the number of players participating, are set beforehand on the server. The configuration of these settings is performed using the matchmaking tool.

# Game Session Search

A Game Session search is a feature for finding Game Sessions to perform competitive or cooperative play. When the application makes a query to the server with specified attributes, the server searches for hits using search attributes that have been set to Game Sessions in advance and lists the hits.

# The Lifecycle of Player Sessions, Game Sessions, and Matches

An example of a scenario demonstrating how the lifecycle of Player Sessions, Game Sessions, and matches works when users play a multiplayer game using the Session Manager service is provided in the figure below.

Example Lifecycle of a Player Session, Game Sessions, and Matches

1. User A launches the game. At this point, no Player Session has been joined yet.
2. User A transitions to multiplayer mode. The application creates a Player Session, and User A enters a joined state as the leader.
3. User A invites User B, with whom they want to play, to their own Player Session, and User B accepts the invitation and joins the Player Session.
4. Both User A and User B request matchmaking. User A, User B, and another player found by the server all join a Game Session that is created as the result of the requests.
5. They play the game. The application now creates a match and reports the results.
6. Continuing to use the same Game Session, the same members play again. The application now creates a different match and reports the results.
7. To play against another player, both User A and User B request matchmaking. Another player found by the server joins a Game Session that is created as the result of the requests.
8. They play the game with a new member. The application now creates a match and reports the results.

## Network Disconnection and Leaving Sessions

The Session Manager service supports a feature that allows a user to leave the Player Session/Game Session that they are in when it's detected that their network connection has become disconnected. However, there are instances where the user may not leave the Player Session/Game Session, even if a network disconnection has been detected by another library. If a network disconnection is detected by another library while the user is participating in a Player Session/Game Session, use `getJoinedPlayerSessionsByUser`/`getJoinedGameSessionsByUser` to check which Player Session/Game Session the user is participating in. If even one Player Session/Game Session that the user is supposed to be participating in does not exist, it means that the Session Manager service detected a network disconnection and performed processing for the user to leave the session(s). Proceed with the in-game process to ensure that information held in the game correctly reflects the user leaving the session(s).

# Signaling and P2P Communications

Features are provided for signaling among the members of Player Sessions and Game Sessions and establishing P2P connections. For details, refer to the [NpSessionSignaling Library Overview](../NpSessionSignaling-Overview/__document_toc.html) and [NpSessionSignaling Library Reference](../NpSessionSignaling-Reference/__document_toc.html) documents.

# Voice Chats

Features are provided that allow members of Player Sessions and Game Sessions to conduct voice chats among themselves. Applications can use voice chats in both Player Sessions and Game Sessions that have been created; however, a user can only actually participate in one voice chat at a time. For details, refer to the [VoiceChat Library Overview](../VoiceChat-Overview/__document_toc.html) and [VoiceChat Library Reference](../VoiceChat-Reference/__document_toc.html) documents.

# Game Intent

A game intent is a general-purpose message object that is passed to an application to instruct the game how it should behave when it is launched. For example, when a user accepts an invitation and joins a Player Session, the information that provides instructions about the Player Session that the user will join is passed to the application as a game intent simultaneously with the launching of the application. Because the application follows those instructions and performs the processing to allow the user to join the Player Session, the user can immediately play the game while joining in the Player Session. For details, refer to the [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html), [NpGameIntent Library Overview](../NpGameIntent-Overview/__document_toc.html), and [NpGameIntent Library Reference](../NpGameIntent-Reference/__document_toc.html) documents.