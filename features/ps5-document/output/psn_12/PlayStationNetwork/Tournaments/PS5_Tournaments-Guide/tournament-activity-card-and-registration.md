# PlayStation®5 Tournaments Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PS5_Tournaments-Guide/tournament-activity-card-and-registration.html

# User Experience

This chapter provides information on how users interact with tournaments on PlayStation®5.

Tournaments are designed to guide a player through the steps needed to participate in a competition. Players must find tournament occurrences they are interested in and register for them if they wish to participate. Players receive notifications when a match is available and they can join the game. Players are given a final placement for their tournament bracket performance once they have played all their matches and the tournament occurrence is over.

# Tournament Discovery

This topic outlines the different ways that users can discover tournaments.

Players have four distinct methods of discovering Tournaments on their console:

* **SDK Deep link to Tournaments (requires integration)** - You can promote tournaments in your title by implementing a shortcut to trigger an SDK deep link to recommend players to join a tournament. For more information, see [PlayStation™Network Tournaments System Overview](../PSN_Tournaments_System-Overview/__document_toc.html) and [SystemService Library Overview](../SystemService-Overview/__document_toc.html).
* **Control Center** - If a player has available tournaments, a "Tournaments" card appears in Control Center. Selecting the card opens a list of all available competitions. You can restrict what tournaments appear for players by using the eligibility fields on the tournament object. Tournaments are prioritized as the active activity in Control Center for players competing in a bracket. For more information, see "PlayStation™Network Activities Guide - User Experience - Active Activities".
* **Game Hub Upcoming Tournaments Strand** - If you have enabled tournaments for your title and have published at least one tournament, a strand appears in the title's Game Hub with a list of tournament occurrences available to users. If the player is not eligible for a tournament, or no tournaments are available, the strand is hidden.
* **Invite from other players** - Players can invite each other to participate in tournaments. Users receive a notification with a CTA to view the activity card for the tournament occurrence.

# Tournament Activity Card and Registration

This topic provides information on the tournament activity card, and how users can register for tournaments.

Players can access information about the tournament and register to compete from the tournament's activity card.

The tournament activity card presents the player with critical information about the tournament, including the start time, name of the tournament, the player's registration status, and the topmost item from **View All Details**.

Players can reach additional information about the tournament from the overflow menu (**…**), and **View All Details**.

The overflow menu has the following options:

* Tournament Rules - View the tournament rules without entering the registration flow.
* Invite - Invite another player to a tournament.
* Unregister/Forfeit - If registered for a tournament, leave, or forfeit the tournament.

**View All Details** shows:

* Start Time
* Rewards
* Playtime estimate
* Number of players
* Tournament format
* Game mode

Tournament Activity Card

Before registering for a tournament, players must accept the rules of the tournament. Players are prompted to accept the rules after selecting **Register**.

# Competing in a Tournament

This topic outlines how users participate and compete in tournaments.

If players are registered at the start time of a tournament, they are placed in a bracket and their first match is generated for them. Players receive a notification informing them how long they have until the match starts and prompting them to join their match. If players do not join by the end of the countdown, they are forfeited from their match.

Player Notification to Join a Match

After their match has concluded, players receive a notification confirming their win or loss.

Player Match Result Notification

Players can view the complete bracket for their tournament, including all players they may compete against.

## Competing in Multiple Tournaments

Players who attempt to compete in multiple tournament occurrences at once are only bracketed in the first occurrence they registered for. All other registrations are canceled.

If a player is competing in a tournament and a separate tournament occurrence they registered for begins, the player remains in their active bracket and the registration for the new occurrence is canceled.

An Active Tournament Bracket