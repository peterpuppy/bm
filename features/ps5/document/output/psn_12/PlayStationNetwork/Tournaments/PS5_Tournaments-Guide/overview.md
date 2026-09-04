# PlayStation®5 Tournaments Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PS5_Tournaments-Guide/overview.html

# Overview

This chapter provides an overview of tournaments in PlayStation®5 applications.

Tournaments are single-elimination, one-versus-one bracket competitions that you can add to PlayStation®5 applications. For each tournament bracket, you can schedule and monitor a series of online multiplayer matches to determine the winner of the bracket, without the need to implement standalone matchmaking and bracketing logic.

Your game must have a one-versus-one competitive game mode to enable tournaments.

Tournament objects have two main fields you must configure:

* Scheduling - Allows you to create one or more tournaments. Scheduled tournament play periods are referred to as occurrences.
* Model - Defines a set of parameters for tournaments to determine the mode of competition, number of rounds, and other key variables of the player experience.

When the number of registered players for a scheduled occurrence exceeds the maximum allowed by the model, the tournament generates additional brackets.

Tournament Object

User experience and key responsibilities for each tournament occurrence and bracket are split in the following way:

* Registration - Allow users to register for a future tournament occurrence. Fields on the tournament object validate each member's registration eligibility.
* Bracketing - Generate the appropriate bracket and create a match schedule for each match. Subsequent matches are generated between rounds.
* Playing and reporting - Facilitate a path for users to join the scheduled match, monitor a match for any disruptions and forfeits, and collect in-game results to finalize match results.

User Experience and Responsibilities

Registration and bracketing are handled by the PlayStation®5 system software. You must configure the details for how users join a tournament, and how to report tournament results.

Tournament specific integration is not required. Tournaments are built on top of the following components:

* **Competitive activity** - Activities allow you to expose in-game experiences and contexts at the platform-level. A competitive activity is a type of activity that targets synchronous play experiences. It is required to create a tournament object and is used to define game settings for each tournament match. For more details, see "PlayStation™Network Activities Guide - Creating and Designing Activities".
* **Matches Web API** - The Matches Web API captures detailed information about multiplayer sessions such as game modes, participants, conditions during play, and results. You can use the Matches Web API to record tournament matches and expose them at the platform level. Tournaments leverage the Matches Web API to schedule, monitor, and collect results for tournament matches. For more details, see [Matches Web API Overview](../../../WebAPI/latest/Matches_WebAPI-Overview/__document_toc.html).
* **Game Intent** - Game intent notifies the game about specific activities and matches occurring in the game, allowing players to join a tournament match directly from various system software features. For more details, see [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html).

## Options for Improving User Experience

Promoting tournaments within a game allows players to discover the feature.
To facilitate discovery, the Launch Tournament Dialog SDK API allows you to link directly to the tournament experience in the PlayStation®5 system UX.
For more information on promoting tournaments in your game, see [PlayStation™Network Tournaments System Overview](../PSN_Tournaments_System-Overview/__document_toc.html).