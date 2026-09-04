# PlayStation®5 Tournaments Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PS5_Tournaments-Guide/defining-the-tournament-object.html

# Creating and Designing Tournaments

This chapter provides information on creating and designing tournaments.

To create and design tournaments:

1. Create a new competitive activity or use an existing one.
2. Define the tournament object to add a schedule and model to your tournament.
3. Define the rules of the tournament.

## Partnering with SIE for Tournament Design and Operation

SIE's Esports and Competitive Gaming Team maintains partnerships for support of tournaments.
As the operational leads on many partnered titles, they have a wealth of experience on tournament design.
It is recommended prior to designing your tournament experience to consult or seek a partnership.
If you are interested, please request support from the Esports and Competitive Gaming Team.

## Rewards

If you are interested in offering rewards for tournaments, raise a ticket on DevNet.
You can list rewards, similar to activities.
Titles can only base rewards on player participation in tournament matches.
You can only provide final placement or similar rewards in partnership with the SIE competitive gaming team.

# Creating Competitive Activities

This topic provides information on creating competitive activities.

Tournaments require a linked competitive activity to mark specific game modes supported by the title for the tournament experience. The linked competitive activity allows you to define the rules of your tournament, for example, how scoring works and how a winner is decided.

Competitive activities cannot be a team activity. Tournaments only support one-versus-one competition.

## Creating a New Activity

SIE recommends that you create a new competitive activity when implementing tournaments. Set **Available by default** to **False** and never set the activity to available in any `activityAvailabilityChange` events that the game posts to keep the activity hidden from players. The table shows the configuration for a hidden competitive activity:

Example Competitive Activity

| **Sample Tournament Activity** | |
| --- | --- |
| **Field** | **Sample Data** |
| `Category` | Competitive |
| `Name` | Tournament Game Mode |
| `Description` | N/A |
| `Hidden` | True |
| `Available by default` | False |
| `isOnlineMultiplay` | True |
| `Repeatable` | True |
| `isTeamActivity` | False |
| `Number of Players` | 1 |
| `Number of Total Players` | 2 |
| `Rewards` | N/A |
| `Score Statistic` | Scores |
| `Additional Statistics` | N/A |

## Using an Existing Activity

If an existing competitive activity matches the game mode you want to make a tournament for, you can use that activity when configuring the tournament. When receiving Game Intent for the activity, use `matchId` to differentiate the experience for players.

# Defining the Tournament Object

This topic provides information on defining tournament objects.

The tournament object allows you to define tournament details such as match length, number of rounds, player eligibility, and scheduling details.

To configure the tournament object:

1. Set a maximum match length value.
2. Define how long players have to join a match.
3. Define a minimum and maximum number of rounds.
4. Configure eligibility requirements, such as age and location restrictions.
5. Configure scheduling details, whether you need one tournament occurrence or multiple.
6. Configure metadata, such as activity card images and tournament logos.
7. Define the Zone ID, to restrict what map or area the tournament takes place.

For a complete list of all tournament object fields, see [PlayStation™Network Tournaments System Overview](../PSN_Tournaments_System-Overview/__document_toc.html).

## Maximum Match Length

Since tournaments progress automatically, you must set a maximum match length for tournament matches. The tournament service creates matches in the Matches Web API with an expiration time equivalent to this value. The game mode associated with a match should have a definite maximum length from the moment it is transitioned into playing state, until the match has a result. Consider the following into account when defining maximum match length:

* Time necessary for picking teams, characters, or other match settings prior to gameplay
* Pause rules, including disabling pause
* Overtime/tie match rules if the match ends in a draw
* Other elements that may extend this time for your title

## Waiting Expiration Time

**Waiting Expiration Time** defines how long players have to join the match. When a match in a bracket is created by the Tournament service, players receive a notification with a countdown. The recommended value for this field is five minutes but you can set this to any value based on your knowledge of player behavior.

## Minimum and Maximum Number of Rounds

The minimum number of rounds determines how many players must be present for the system to generate a bracket when the tournament starts. For example, a two round tournament requires four players, while a three round tournament requires eight players.

If the minimum number of players is not met, the tournament is canceled and players are informed there were insufficient players to start the tournament.

The maximum number of rounds determines how many players can be placed in a single bracket before a new bracket is generated. To prevent accidental cancelation, this value must be greater than the minimum number of rounds.

When setting your minimum and maximum number of rounds, keep in mind the average match length for your title. In a title where matches on average take five minutes, a seven round, 128 player bracket will take approximately 35-70 minutes. If your matches instead average 20 minutes, that same bracket could take 180 minutes or longer. Aim to set your minimum number of rounds so that winning the tournament feels like an achievement, and set the maximum number of rounds to ensure that no bracket takes excessively long to complete.

## Eligibility

Setting eligibility ensures that tournaments are offered to the correct players. Use the age requirement to set parameters for how old a player must be to compete, and country/region restrictions to limit a tournament to a specific region of the world.

## Statistics Eligibility

Statistics eligibility allows you to restrict what players can participate in a tournament and enables more complex tournament designs. You can connect a tournament object to the UDS stats configured for your title and reference those stats to limit the pool of players eligible to register.

For example, you could restrict tournaments to only those players who are Level 10 in your ranked mode by connecting the tournament object to a "Level" UDS stat and setting the required value to 10. Alternatively, you could create a tournament object that only allows registrations for players Level 1-10, and another tournament object for players Level 10 and up.

## Scheduling

Schedule a single tournament occurrence by setting an **Available From** date and time and setting **Repeatable** to false.

Using the Repeatable function for scheduling, Tournaments can be set on a weekly or daily recurring basis. We recommend offering Tournaments when player concurrency is the highest.

For a complete introduction to the Tournament Object tooling in UDS, please read [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html). For a complete list of all Tournament Object fields and their purpose, see [PlayStation™Network Tournaments System Overview](../PSN_Tournaments_System-Overview/__document_toc.html).

The following is an example of a basic tournament configuration:

Sample Tournament Structure

| **Field** | **Sample Data** | **Recommendations** |
| --- | --- | --- |
| `Object Id` | Test\_4p\_onevsone | Include "test" and "2 rounds" or "4 player" |
| `Display Name` | Test Tournament 1v1 | Include "test" and "2 rounds" or "4 player" |
| `Tournament Format` | `symmetricSingleElimination` | Required field with only this option until Tournaments functionality is expanded to other formats |
| `Activity` | `activityid_onevone` | The Activity you are using for the Tournament. |
| `Minimum Number of Rounds` | 2 | Requires 4 players registered to generate a bracket. |
| `Maximum Number of Rounds` | 7 | Will generate a new bracket after player count exceeds 128. |
| `Maximum Match Length` | 20 minutes | Based on title game mode. |
| `Waiting Expiration Time` | 5 minutes | Based on title game mode. |
| `Country Age Rules` | 16, SIEA | Set based on competition requirements for your title or age rating. |
| `Available From` | 9:00 AM UTC, March 1, 2023 | Set based on your desired occurrence start time. |
| `Repeatable` | FALSE | Not needed, complicates testing. |

Use the tournament debug UI tooling to assist when creating tournaments. For more information, see [PlayStation™Network Tournaments System Overview](../PSN_Tournaments_System-Overview/__document_toc.html).

## Metadata and Images

The tournament object includes a number of optional metadata fields to provide additional information to your players before registering for the tournament. This information can encourage players to register and clarify the nature of the tournament. You can make the tournament activity card visually distinct by adding images and a tournament logo.

Define SubCategory, Game Mode, and Display Name to communicate the mode of play, scheduling, and other design elements with players.

## Zone ID

The tournament object can include a zoneId in addition to an acitivtyId to specify what map players use during tournament matches or to specify other in-game mechanics.

# Defining Tournament Rules

This topic provides information on defining rules for tournaments.

A rules file is required to publish a tournament. Players are also required to accept the rules to compete in the tournament with default settings. If you unselect "Rules Acceptance Required" then users will be prompted to view the rules but do not need to accept them to participate. You must include a rules file that details the nature of the competition to players before they choose to compete.