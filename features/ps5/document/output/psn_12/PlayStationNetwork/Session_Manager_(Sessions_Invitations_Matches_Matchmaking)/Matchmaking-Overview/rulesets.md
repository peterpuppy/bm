# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/rulesets.html

# Major Components of the Matchmaking Service

# Matchmaking Server

A matchmaking server (sometimes referred to simply as a "server") is a server that provides asynchronous server-side matchmaking features.

# Rulesets

A ruleset consists of a set of condition definitions for matchmaking. You can define just as many rulesets as you need, based on the multi-play game modes in the application - such as "team death match" - as well as based on the type of matchmaking to be conducted within a given game mode - such as "quick match" or "rank match". In a ruleset, you can include definitions of the teams that will engage in multi-play, declarations of player attributes and of ticket attributes, and definitions of rules that use those declarations. The players who have requested matchmaking are each evaluated according to the ruleset and combined into teams.

# Matchmaking Tool

The Matchmaking Tool is a web tool that a developer can use to manage the Matchmaking service.

Using this tool, a developer can set up and edit rulesets.

# Matchmaking Tickets

A matchmaking ticket is an object that an application issues when requesting matchmaking from a server.

A matchmaking ticket includes a specification of the ruleset to apply, player attributes (in-game skill levels, etc.), and ticket attributes (the stage where the competitive play is to take place, etc.). If, for instance, there are players who have already joined a Player Session and have already decided that they would like to play together, it is also possible to include specifications of those players or of teams.

The server performs matchmaking by comparing the matchmaking tickets issued by multiple players based on the conditions set forth in the ruleset.

# Matchmaking Offers

A matchmaking offer is an object that a server issues to an application when matchmaking has been achieved. If you refer to a matchmaking offer, you can obtain the name of the ruleset that has been applied, information concerning the other players with whom the local player will be playing, information concerning the teams to which the players belong, and the ID of the Game Session that was created.

# Game Sessions

A Game Session is one type of session provided by the Session Manager service. An application can use one for an arbitrary purpose during online multiplayer gameplay. The players put together through matchmaking join one Game Session and engage in gameplay and communication within it. Refer to [Session Manager Service Overview](../../../SDK/latest/Session_Manager_Service-Overview/__document_toc.html) and [Session Manager Web API Overview](../Session_Manager_WebAPI-Overview/__document_toc.html) for details.

# Teams

Teams represent groupings of players who have undergone matchmaking. A player who has undergone matchmaking always belongs to one team; at least one team must be set to a ruleset. Note that a "team" in the Matchmaking service does not always mean the same thing as a team in the ordinary sense of the term. For example, if you are one of two players who are to engage in one-on-one competitive play, you and your competitor will constitute one team. It is also possible to set up a team in a ruleset that closely resembles a team in the ordinary sense of the word. For example, a more typical setup might consist of one in which a total of four players, split into teams of two, play against one another, as in tennis doubles. With settings like these, the players who undergo matchmaking are automatically allocated to teams as appropriate by the server. It is not necessary to have a fixed number of players on a team; it is also possible to set minimum and maximum numbers of players. It is also possible to have settings where the number of players on each team is not the same - for example, settings with a monster team consisting of one player and hunter team consisting of four players.

# Backfilling

Backfilling is a feature by which matchmaking fills up any empty slots in a Game Session with supplemental players. For example, suppose that you want to have a new player join whenever a player suspends gameplay and leaves the Game Session so that playing can continue. In that case, you could recruit new players by issuing a matchmaking ticket with the target Game Session ID and the conditions for the supplemental players specified.