# PlayStation®5 Tournaments Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PS5_Tournaments-Guide/tournaments-integration-overview.html

# Tournaments Integration Overview

This chapter provides information on integrating tournaments with your applications using the Matches Web API and Game Intent.

After you have configured a competitive activity and the tournament object, use the Matches Web API to reference specific matches and support results reporting to enable the tournament for players to join.

# Tournament Match Cycle

This topic provides information on the lifecycle of a match within a tournament.

The Tournament match cycle begins by pairing together players and generating matches using the Matches Web API. Players are then informed they must join their match before the waiting expiration time. If both players join the match, the title initiates the match.

Tournament Match Cycle

At the conclusion of the match, the title reports results using the Matches Web API. The tournament service generates new matches for the next round of competition as the bracket progresses.

Bracket Match Status

Tournament matches are created in the WAITING state with the Waiting Expiration Time set. The title moves the match to PLAYING as soon as both players have joined the match. COMPLETED or CANCELLED statues update player progression through the bracket.

# Game Intent, the Lobby, and Match Start

This topic provides information on how tournaments are implemented in Game Intent.

Every tournament game intent includes an activityId and matchId. Use these fields to load the player into the match lobby with the correct opponent.

When a player successfully joins the lobby, the title must trigger joinMatch to indicate that a player has joined. This information is used to resolve cases in which only one player, or neither player joins.

Place players in a lobby while they wait for their opponent to join. Ensure that players in the lobby do not have the ability to invite additional player or change the game settings. SIE recommends indicating that players in the lobby have joined a tournament match and are waiting for their opponent to join.

Initiating a Match

For more information on the Tournament implementation of game intent, see [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html).

# Using the Matches Web API with Tournaments

This topic provides information on how to use the Matches Web API to manage your tournament's matches.

Tournaments use the Matches Web API to receive information from the title about the progression of the match. This includes players joining the match, that the match has begun, that the match has been completed, or the match has been disrupted in some way.

If a match is moved to CANCELLED, the tournament uses information about the disconnect status and the score reported from the Matches Web API to determine the winner.

Executing a Match

# Managing Exception Scenarios

This topic provides information on how the Matches Web API handles specific scenarios that can arise when implementing your tournaments. For example, what would happen if not enough players show up for a scheduled tournament.

Below you can find a list of common exception scenarios and how they are managed based on the tournament service logic, inputs from players, or the Matches Web API.

Common Exception Scenarios

| **Tournament Scenario** | **Result** |
| --- | --- |
| Player A does not join the match within the *Waiting Expiration Time*, while Player B does join. | Player B is given the victory and advances. |
| Both players do not join the match within the *Waiting Expiration Time*. | Players advance by coin-toss. Exception: If it is the Finals of the Tournament, both players are listed as tied for second place. |
| Player A joins the match, then quits. Player B joins the match before the end of *Waiting Expiration Time*. | The title updates the match through REMOVE based on the DISCONNECTED or QUIT reason for Player A. In this case, Player B is given the victory and advances. |
| Player A disconnects or quits the game after the match has started against Player B (entered PLAYING state). | The title must handle this use case as part of their integration work. If the player does not immediately return, give Player B the victory. |
| Player A uses the forfeit option from the tournament action card after the tournament has begun. | Their current opponent will receive an automatic victory, even if the match is already in progress. The title is not aware Player A has forfeited and should continue the match. |
| Match is set to CANCELLED, based on *Maximum Match Length*. | Winner is decided by current score, or advanced by coin-toss if tied. |
| The tournament gameplay mode is not available to players because of technical difficulties or service disruption. | The tournament service will use waiting and cancellation expiration times to determine bracket advancement if no input is received. |
| The minimum player number is not reached. | Players receive a notification at the tournament's start time that the tournament was cancelled due to insufficient participation. |
| The tournament is cancelled through the tournament tool. | Notification is triggered by the system that informs users that that tournament was cancelled. |
| The tournament schedule or other major details are changed though the tournament tool. | Changes to critical tournament details cancel future tournaments. Players receive notifications that those specific tournament occurrences have been cancelled. |