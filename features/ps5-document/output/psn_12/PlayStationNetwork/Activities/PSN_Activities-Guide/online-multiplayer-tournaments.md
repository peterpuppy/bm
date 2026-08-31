# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/online-multiplayer-tournaments.html

# Configuring Activities for PVP Online Multiplayer Modes

This chapter provides guidance on creating activities for games with online multiplayer modes.

Typical online multiplayer modes feature repeatable, match-based designs where each match is a discrete competition between a set of players, with an outcome that includes standings of all players. These modes can include a ranking system or not, and typically include some form of automated matchmaking for players.

When creating activities for these types of game modes, create competitive activities that track information about matches in the mode for each player. PlayStation™Network uses match data to power enhanced session information and social recommendations, provide in-depth stats to the player, and power tournaments.

Note: You can only set multiplayer activities to active using the Matches Web API. Do not create multiplayer activities without corresponding Matches Web API updates.

Follow the guidance below when designing activities for online multiplayer modes:

## Creating Activities

In this configuration, activities represent competitive game modes.

1. Create a competitive activity for each competitive mode in your title. Competitive activities represent player-vs-player modes in games that have defined match structures, including a winner for the match.
2. Give each competitive activity a unique name for the mode it represents. If you intend to create activities for multiple variants of a game mode, reflect that in the title as well.
3. Set **Available by Default** to **true** unless there are requirements that players must meet to unlock the mode. In that case, use `activityAvailabilityChange` to make the activity available after they have completed those requirements.
4. Do not enable *Is Required for Completion* for competitive activities. If the player must play an online match to complete the main campaign, [configure that requirement as a progress activity](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.").
5. Set **Has Online Multiplayer** to **true**.
6. Set **Support Non-PSN Players** to **true** if your game supports cross-platform play for this mode.
7. Select the platforms your title is available for. The activity displays *Platforms Available* along with the choices you select for this setting.
8. Provide a statistic that is relevant to the win conditions of the game mode, such as kills, goals, score, or time. The score statistic gives players additional context on the result of the match. Players can view this statistic on the cover of the activity card throughout the match, as well as updates you make to it with the Matches API. Provide the following additional details for the statistic:
   * *Score Name* - The name of the primary metric that leads to wins or losses in the mode. For example, kills, goals, points, or time.
   * *Display Format* - The format of the statistic. Set as **Numeric** unless your game utilizes **Time** as the primary score statistic.
   * *Sort* - The sorting logic for the statistic on the activity card. Select **Ascending** when smaller values mean better performance and **Descending** when larger values mean better performance.
   * *Decimal Places* - The number of decimal places displayed for the statistic on the activity card.

Online Multiplayer Activity Settings

## Managing Activity State

Ensure your activities accurately represent the intended game state by using the following endpoints of the Matches Web API:

* `createMatch` - Generates a `matchId` when your game creates a match. This action makes the activity card visible to the player.
* `joinMatch` - Adds players to the match roster.
* `updateMatchStatus` - Sets the status for the match. Set the match to `PLAYING` when gameplay begins and all players have been added to the roster. You can use this call again to set the match to `COMPLETED` or `CANCELED` when the match is over.
* `reportResults` and `competitiveResults` - Provides the final results of the match with player rankings and score statistics, and moves the match to `COMPLETED`.

## Guidance for Other Game Designs

The best practices in this topic are general guidelines to follow when creating activities for online multiplayer modes. For extended guidance on specific game modes, refer to the following topics

* [Solo player vs player (PvP) online multiplayer modes](online-multiplayer-pvp.html "This topic provides guidance on creating activities for online multiplayer player vs player modes.")
* [Team based competitive online multiplayer modes](online-multiplayer-team-based.html "This topic provides guidance on creating activities for online multiplayer team-based competitive modes.")
* [Online multiplayer tournaments](online-multiplayer-tournaments.html "This topic provides guidance on creating activities for online multiplayer tournament modes.")

  Note: If you have a non-competitve PVE mode, please refer to the section for Configuring Activities for Repeatable and Endless Modes

# Configuring Activities for Solo Online Player vs. Player (PVP) Modes

This topic provides guidance on creating activities for online multiplayer player vs player modes.

Note: Ensure that you [follow the general guidance for configuring online, player vs. player multiplayer activities](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.") before implementing the guidance in this topic.

Follow the guidance below for solo PVP modes where repeatable matches occur and players have unique final results or scores:

## Creating Activities

Activities in this configuration represent online competitive modes.

1. [Create activities according to the general guidance for multiplayer modes](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.").
2. Leave **Is Team Activity** unchecked. *Is Team Activity*  determines whether or not players are placed as members of a team when creating matches in the Matches Web API.
3. Set **Number of Players** to **1**. The activity displays a *Game Group Limit* to players in the details section of the activity card.
4. Under **Number of Total Players**, set the total number of players who can participate in a match together. The activity displays *Total Player Limit* on the activity card to indicate the maximum number of players allowed in a match. For example, in 1v1 matches, the value is 2. In 1v1v1v1 free-for-all matches, the value is 4.

# Configuring Activities for Online Team Based Competitive Modes

This topic provides guidance on creating activities for online multiplayer team-based competitive modes.

Note: Ensure that you [follow the general guidance for configuring online, player vs. player multiplayer activities](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.") before implementing the guidance in this topic.

This guidance is intended for team-vs-team or team-vs-computer modes where repeatable matches occur and a team has a unique final result or score.

Follow the guidance below on designing activities for team-based competitive modes:

## Creating Activities

Activities in this configuration represent online competitive modes.

1. [Create activities according to the general guidance for multiplayer modes](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.").
2. Set **Is Team Activity** to **true**. *Is Team Activity* determines whether or not players are placed as members of a team when creating matches in the Matches Web API.
3. Set **Number of Players** to a value greater than **1**. This represents the maximum number of players that can join a match as a single team. The activity displays a *Game Group Limit* to players in the details section of the activity card.
4. Under **Number of Total Players**, set the total number of players who can play in a match together across all teams participating. The activity displays *Total Player Limit* on the activity card to indicate the maximum number of players allowed in a match.

## Managing Activity State

Ensure your activities accurately represent the intended game state by using the following endpoints of the Matches Web API:

* `joinMatch` or `updateMatchDetails`: Adds players to the match and defines teams and teams' rosters.

# Configuring Activities for Online Tournaments

This topic provides guidance on creating activities for online multiplayer tournament modes.

Tournaments are single-elimination, one-versus-one bracket competitions that you can add to PlayStation®5 applications. For each tournament bracket, you can schedule and monitor a series of online multiplayer matches to determine the winner of the bracket, without the need to implement standalone matchmaking and bracketing logic.

Your game must have a one-versus-one competitive game mode to enable tournaments.

## Creating Activities

To create activities for tournaments:

1. [Create activities according to the guidance for Solo Online Player vs. Player (PVP) activities](online-multiplayer-pvp.html "This topic provides guidance on creating activities for online multiplayer player vs player modes."). Tournaments are only supported for one-versus-one multiplayer modes.
2. Set **Available by Default** to **false** if this activity is only intended for use by the Tournaments feature to prevent it from appearing to general players.

## Managing State

Ensure you are reporting the score statistic configured for your activity to improve the tournament experience for players. Score data is viewable in the tournament's bracket and useful to players competing in the tournament, allowing them to track the progress of their opponents.

The Tournaments system has additional requirements to function that rely on the *Join Status* of individual players and the overall *Match Status*. Review the [PlayStation®5 Tournaments Guide](../PS5_Tournaments-Guide/__document_toc.html) for additional information.

# TRC R5302 Requirements for Competitive Multiplayer Games

This topic provides information on the TRC requirements you must follow if your game has competitive multiplayer modes.

If your game features a real-time multiplayer mode where players compete against each other, you must create at least one competitive activity to represent the mode. Multiplayer modes with any of the following conditions must adhere to this requirement:

* Winners and losers are determined based on the results of a match
* Players are ranked on a leaderboard
* Placement is determined at the end of the match

Create a competitive activity for every mode that meets one of these conditions.

While there is a required minimum configuration for activities explained in this TRC, SIE recommends that you [follow the extended guidance for configuring activities for online multiplayer modes](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.") to access the full functionality of activities.

Activities that are configured to the TRC minimum requirements lack most functionality that make them useful for players. Activities that exceed TRC minimum requirements see higher player engagement, including increased playtime and retention.

Follow the required minimum configuration below to create activities for online multiplayer modes.

## Creating Activities

In this configuration, activities represent online, competitive multiplayer modes.

1. Create a competitive activity for every competitive mode in your title. For more information on competitive activities, see [Configuring Activities for PVP Online Multiplayer Modes](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.").
2. Give your activity or activities a name that represents the mode. For example, “Online Match”.
3. Set **Available by Default** to **true** unless there are requirements that players must meet to unlock the mode. In that case, use `activityAvailabilityChange` to make the activity available after they have completed those requirements.
4. Do not enable *Is Required for Completion* for competitive activities. If the player must play an online match to complete the main campaign, [configure that requirement as a progress activity](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.").
5. Set **Has Online Multiplayer** to **true**.
6. Set **Support Non-PSN Players** to **true** if your game supports cross-platform play for this mode.
7. Set **Is Team Activity** to **true** for team based competitive modes. If you only create one activity for solo and team modes combined, you must set this value to **true** and add the player to a team with only one player on it when starting matches.
8. Select the platforms your title is available for. The activity displays *Platforms Available* along with the choices you select for this setting.
9. Set **Number of Players** to the maximum number of players that are allowed to group up and play together in a party. If you have configured a single competitive activity to represent all online modes, set this value as high as possible. The activity displays a *Game Group Limit* to players in the details section of the activity card.
10. Set the **Number of Total Players** who can participate in a match together. If you have configured a single competitive activity to represent all online modes, set this value as high as possible. The activity displays *Total Player Limit* on the activity card to indicate the maximum number of players allowed in a Match. For 1v1 matches, the value is 2. For 1v1v1v1 free-for-all modes, the value is 4.

## Managing Activity State

Ensure your activities accurately represent the intended game state by using the following endpoints of the Matches Web API:

* `createMatch` - Generates a `matchId` when your game creates a match. This action makes the activity card visible to the player.
* `joinMatch` - Adds players to the match roster.
* `updateMatchStatus` - Sets the status for the match. Set the match to `PLAYING` when gameplay begins and all players have been added to the roster. You can use this call again to set the match to `COMPLETED` or `CANCELED` when the match is over.
* `reportResults` and `competitiveResults` - Provides the final results of the match with player rankings and score statistics, and moves the match to `COMPLETED`.

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").