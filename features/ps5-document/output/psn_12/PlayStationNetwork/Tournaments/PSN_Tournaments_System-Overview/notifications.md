# PlayStation™Network Tournaments System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Tournaments_System-Overview/notifications.html

# Managing Tournaments

This chapter includes information on previewing tournaments, opening tournament activity cards, and tournament-related console notifications.

# Tournament Preview

This topic provides information on how to preview tournaments and open tournament activity cards.

Check the appearance and behavior of activities from **Tournament Preview**.

To launch Tournament Preview from the Tournaments Debug UI:

1. Select **★Debug Settings > PlayStation Network > Tournaments** while the game is running.
2. Select **Card Preview**. This only displays tournament activity cards.

To launch Tournament Preview from Activity Preview:

1. Navigate to **Activity Preview** from either the experience switcher shortcut or from **Debug Settings**.
2. Select the **overflow (…)** menu.
3. Select **Open Tournament Preview**.

Each tournament activity is classified and displayed depending on its status:

* Available Tournaments - A list of tournament activities that are open for registration. To display an activity on this list, you must create tournament occurrences.
* Active Tournaments - A list of tournament activities that are active for the user. Active means the user is registered and the start point is 15 minutes before the occurrence starts and the end point is 30 minutes after the user's participation in the occurrence ended.
* History of Completed Tournaments - A list of activities that the occurrence has completed or canceled.

## Opening a Tournament Activity Card using the SDK

Using the System Services SDK, you can open and display the tournament activity card for the current user, from within the game application. See [SystemService Library Overview](../SystemService-Overview/__document_toc.html) for more information.

There are two key arguments to understand when calling `sceSystemServiceOpenTournamentOccurence()`:

Tournament Occurrence Parameters

| **Field** | **Description** |
| --- | --- |
| `tournamentId` | The system opens the tournament activity card for the next available tournament occurrence for the Tournament Object ID passed. If the user is currently active for that `tournamentId`, that card is displayed instead.  If you pass the following reserved tournament ID values for `tournamentId`, a different tournament activity card is opened:   * `_nextAvailableTournament` - Opens the tournament activity card for the next available tournament occurrence, across all tournament objects. * `_nextAvailableTournamentByActivity:<activityId>` - Opens the tournament activity card for the next available tournament for the given `<activityId>`, if one exists. * `_activeTournament` - Opens the tournament activity card for the currently active tournament occurrence. * `_listAvailableTournaments` - Opens the consolidated tournament activity card for the game and displays all active and upcoming tournaments, if any are available. |
| `userId` | The System ID for the user. |

## Opening a Tournament Activity Card from the UI

Users can open tournaments from the system UI. The tournament card shows tournament metadata.

Depending on the tournament state, the CTA button changes to allow the player to advance in the tournament. For example, if the tournament occurrence is `OPEN`, the CTA button shows **Register**.

In the figure below, the tournament occurrence has started, and the player was matched against their next opponent. The player can now join the match and start the next round.

Tournament Selected Mode

**View Tournament Bracket** allows the player to explore their current position in the tournament status results.

Tournament Bracket Viewer

# Tournament Notifications

This topic provides details on the tournament-related console notifications that players can receive.

Console notifications are integral for players to participate in tournaments. Notifications generated for tournaments consist of both a toast and an expanded version of the notification that can be accessed when the player presses the PS button.

In the expanded mode of the notification, the top call to action is context specific and invokes the game intent and brings the player in the game (as configured by your title). The **View Details** call to action takes the player back to the tournament activity card.

## Tournament Starting

This notification is sent to all players who are registered in a tournament occurrence, 15 minutes before the scheduler moves the tournament occurrence from OPEN to STARTED, and only after the scheduler has already assigned brackets and assigned players to matches.

Tournament Starting Notification

## Tournament Started

This notification is sent to all players who are registered in a tournament occurrence, when the scheduler moves the tournament occurrence from OPEN to STARTED, and only after the scheduler has already assigned brackets and assigned players to matches. If a player does not join a match by the **Waiting Expiration Time**, they are forfeited from the match. A player may not join the match and advance to the next round if either of the following conditions occur:

1. The opponent never joins the match and the system randomly assigns a winner.
2. The opponent forfeits their match explicitly by choosing to do so using a CTA button.

Tournament Started Notification

## Join Match

This notification is sent to individual players who advance to a next round in a tournament occurrence. If a player does not join a match by the **Waiting Expiration Time**, they are forfeited from the match. A player may not join the match and advance if either of the following conditions occurs:

1. The opponent never joins the match, and the system randomly assigns a winner.
2. The opponent forfeits their match explicitly by choosing to do so using a CTA button.

Join Match Notification

## Round Win

This notification is sent to players who won their current match, before their next round is ready to join. A round is ready to join when the Tournament service assigns two opponents to a match.

Round Win Notification

## Next Round Ready

This notification is sent to players to notify both opponents that they need to join the next round within the allotted time, or they risk forfeiting the match.

Next Round Ready Notification

## Tournament End (Lost)

This notification is sent to players when they are eliminated from a tournament.

Tournament End (Lost) Notification

## Tournament End (Won)

This notification is sent to players when they win their bracket by eliminating their final opponent.

Tournament End (Won) Notification

## Tournament Canceled

This notification is sent to players when the system cancels a tournament. The notification includes a reason for the cancellation:

* **This event did not meet the minimum required number of players:** The system detected that the number of registered users is less than the minimum required number of players. When configuring tournament objects, you define the minimum and maximum number of rounds. If there are not enough registered players to satisfy the minimum number of rounds, the system cancels the tournament.
* **You can't participate in multiple tournaments at the same time:** The system detected that the player is attempting to register in a different tournament while actively participating in one.
* **This event was called off by the organizer:** In some instances, you may change the tournament scheduling parameters after users have registered. When this occurs, the system cancels the tournament.

Tournament Canceled Notification

## Tournament Bye Notification

This notification is sent when a player does not have an opponent in a round of a tournament. This acts as a win for the player, even though they did not play a match. A "Bye" scenario can occur when there is an odd number of players in a bracket or when a player forfeits their position in the tournament.

* Tournament Start Bye - Occurs when a player does not have an opponent in the first-round match.

Tournament First Round Bye Notification

* Mid Tournament Bye - Occurs when a player forfeits their position in the middle-round matches.