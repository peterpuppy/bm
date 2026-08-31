# Matches Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matches_WebAPI-Overview/stats-match-statistics.html

# Overview and the Main Properties of Matches

# Matches

A "match" represents a general container for recording the play status and results of multi-play. Matches can be individually created for each multi-play session; however, specifically which part of the game constitutes a match must be defined in each application in whatever way will be optimal to the users.

# Links with Activities

The definition of a match can be set arbitrarily for each application; however, a match must always be linked to a single "activity" so that it can be categorized and displayed by the system software. An activity is a data object defined using the UDS service and has various properties that indicate the characteristics of the gameplay. An error will occur when attempting to link a match with an activity that hasn't been configured using the UDS service; make sure to configure the activity in advance.

A match can only be linked to an activity that meets one of the following conditions. Attempting to link a match upon its creation with an activity that doesn't satisfy one of these conditions will result in an error.

* The value of `Category` is `Competitive`
* The value of `Category` is `Progress` or `OpenEnded` and the value of `isOnlineMultiplay` is true

## Properties Determined by the Activity

Upon creating a match, the three parameters of `groupingType`, `competitionType`, and `resultType` will be determined automatically according to the definition of the activity the match will be linked with.

groupingType (How Users Are Grouped in the Match)

| `isTeamActivity` **of the Activity** | `groupingType` **of the Match** | **Description** |
| --- | --- | --- |
| true | `TEAM_MATCH` | Match played among teams |
| Other than true | `NON_TEAM_MATCH` | Match played among individuals |

competitionType (How the Match Is Played)

| `category` **of the Activity** | `competitionType` **of the Match** | **Description** |
| --- | --- | --- |
| `Competitive` | `COMPETITIVE` | Competitive play |
| Other than `Competitive` | `COOPERATIVE` | Cooperative play |

resultType (How Results are Recorded in the Match)

| `scoreStatistics` **of the Activity** | `resultType` **of the Match** | **Description** |
| --- | --- | --- |
| Values exist | `SCORE` | Match results include scores |
| Values don't exist | `RESULT` | Only the ranking of each user |

# Match Status (status)

Matches can be in the statuses shown in [Match Statuses](match-status-status.html#matches-web-api-overview_1_3__035f77d6-fae7-11ed-be56-0242ac120002) and [Match Status Transition Diagram](match-status-status.html#matches-web-api-overview_1_3__035f808c-fae7-11ed-be56-0242ac120002), and this status is stored as a match's property. The status of a match is explicitly updated when the application calls `updateMatchStatus`; additionally, status transitions will occur automatically based on the conditions described later.

Upon creation, a match's status is WAITING. Do not forget to update the match status to PLAYING from the application side when the user starts gameplay. A match's status must be PLAYING in order to report results with `reportResults` and to terminate the match. If the match's status is other than PLAYING (specifically either WAITING or ONHOLD) when reporting results, change the status to PLAYING using `updateMatchStatus` and then report the results.

Match Statuses

| **Status** | **Description** |
| --- | --- |
| SCHEDULED | Status in which the match is waiting until its start time  \*\*Not currently used. Future usage is expected. |
| WAITING | Status where the participation of players is being waited for |
| PLAYING | Status where the match has begun and is currently underway |
| ONHOLD | Status where the match has been temporarily suspended |
| CANCELLED | Status where the match was forced to terminate partway through |
| COMPLETED | Status where the results of the match have been reported and the match terminated |

Match Status Transition Diagram

## Automatic Changes of Status

Match status changes automatically based on the following conditions:

**Reporting of Match Results**

When the application calls `reportResults` for a match with PLAYING as its status, that match will be terminated automatically, and its status will transition to COMPLETED. If `reportResults` isn't called or when its call fails, the match won't be terminated and will remain displayed in the system software as being played; make sure to call `reportResults` from the application side once a match concludes and terminate it.

**Expiration of a Match**

If a match is left alone in the WAITING or ONHOLD status, its status will automatically be transitioned to CANCELLED. The time until the changeover is set using the `expirationTime` parameter when the match is created or updated. The elapsed time is counted from when the match status is updated or from when `expirationTime` is updated and will be reset if either is updated while a count is ongoing.

The match's status will also automatically transition to CANCELLED if the match is left alone while in the PLAYING status. The time until the changeover is set using the `cancellationTime` parameter when the match is created or updated. The amount of time elapsed is counted from the transition to PLAYING status; the count is reset if the match transitions to ONHOLD status during the count. Unlike `expirationTime`, `cancellationTime` can't be updated.

# In-Game Roster (inGameRoster)

This property manages the players (`players`) or teams (`teams`) who have joined a match. Players can leave a match in the middle of play; however, records that they participated in the match will remain permanently.

At least one player or more must be registered before the match is started. In addition, if `groupingType` is `TEAM_MATCH`, at least one team or more must be specified before the match is started.

## Player (`players`)

A player is an object representing a participant in a match. Each player has a `playerId` as an identifier. This value can be specified arbitrarily but must be unique within each match.

In addition to the users with accounts for PlayStation™Network, users on other platforms and NPCs can be registered as players. If a player is a user of PlayStation™Network, specify the user's account ID as the `accountId` to link their actual account information and match information.

Optionally, a `playerName` can be specified for each player as their display name. If a `playerName` is not specified, the PlayStation™Network user's `onlineId` or default name will be displayed by the system software.

Note:

Avoid using the account ID or online ID of a player who has joined the match for `playerName`.

In addition, because `playerName` is a string that is displayed onscreen, always make sure that no inappropriate language is included using the Profanity Filter Web API (for example).

## Team (`teams`)

A team is an object representing a participating team in a match. Each team has a `teamId` as an identifier. This value can be specified arbitrarily but must be unique within each match.

Optionally, a `teamName` can be specified for each team as its display name. If a `teamName` is not specified, the default name will be displayed by the system software.

Note:

Avoid using the account ID or online ID of a player who has joined the match for `teamId` or `teamName`.

In addition, because `teamName` is a string that is displayed onscreen, always make sure that no inappropriate language is included using the Profanity Filter Web API (for example).

## Players and Teams

A player can belong to one team at a time. Players need not necessarily belong to teams. Additionally, players can transfer to other teams whenever they choose.

# Result (competitiveResult/cooperativeResult)

A result is a property that retains the interim or final results of a match along with data such as scores and rankings. You can report interim results by specifying `matchResults` for an in-progress match and calling `updateMatchDetail`. Every time interim results are reported, previously reported results are all overwritten. If `reportResults` is called with `matchResults` specified, the results will be finalized, and the match will end.

If the `competitionType` is `COMPETITIVE`, specify `competitiveResult` for the result; if it is `COOPERATIVE`, specify `cooperativeResult`. With `updateMatchDetail`, only `competitiveResult` can be specified. Each property is explained below.

## `competitiveResult`

This is a property for retaining the result of competitive play. If `groupingType` is `NON_TEAM_MATCH`, specify the `playerResults` property; if it is `TEAM_MATCH`, specify the `teamResults` property.

These property values are objects that contain multiple pairs, each consisting of a player/team identifier (`playerId`/`teamId`) and the ranking (`rank`) of that player/team. If the `resultType` is `SCORE`, be sure to specify a value as follows for score (`score`) that corresponds to the `scoreStatistics` defined in the activity, in addition to the above two properties.

* When `displayFormat` of `scoreStatistics` is `time`:

  Specify a positive integer value in milliseconds.
* When `displayFormat` of `scoreStatistics` is `numeric`:

  Specify an integer value. Note that by specifying the number of digits after the decimal point in `decimalPlaces` of `scoreStatistics`, it is possible to display decimal scores on the system software.

If you specify a score that does not correspond to the defined `scoreStatistics`, the score may not be displayed correctly on the system software.

You do not necessarily need to include results for all players/teams. However, all interim progress results of players/teams registered in the past will be deleted if those players/teams aren't included. However, if a player participated in a match, even if for one time only, you may still include their results even if they left during the middle of gameplay. Meanwhile, the players/teams included in the results must always be included in the in-game roster.

Specify the rankings as described below, based on the type of match.

* Many vs many competitive play: Specify each player or team's ranking as-is, as in 1, 2, 3....
* Player vs player/team vs team competitive match: Specify first place for the winning player/team and second place for the losing player/team in the rankings.

It is also possible to specify the same ranking to multiple players/teams. In the case of a tie for a player-vs-player or team-vs-team match, give first place to both players/teams.

For the scores, specify values that correspond to the activity's `scoreStatistics`.

* When the match's `groupingType` is `NON_TEAM_MATCH`:

  Specify each player's score as-is.
* When the match's `groupingType` is `TEAM_MATCH`:

  Specify each team's score as-is. If calculations are required to yield teams' scores, specify the results calculated within the game. Although it will have no bearing on determining which team won, it is also possible to send scores of each player belonging to the team along with team scores.

## `cooperativeResult`

This is a property for retaining the result of cooperative play. Specify only the final status of cooperative play (`SUCCESS`, `FAILED`, or `UNFINISHED`) for the `cooperativeResult` property.

# Stats (matchStatistics)

This property retains scores and rankings that aren't directly related to the match results. To display stats in the system software, they must be defined, each in a uniquely identifiable format using a `statsKey` in the `additionalStatistics` of an activity. If undefined stats are reported, they will not be displayed.

Stats can be reported an indefinite number of times up to when a match ends. However, every time there is a report, previously reported stats will all be overwritten. Using this behavior, it is possible to delete additional stats by removing specific stats from the `matchStatistics`.

The property of additional stats that can be reported differs depending on the match's `competitionType` and `groupingType`.

* The `playerStatistics` property must be specified if the match's `competitionType` is `COOPERATIVE` or if the match's `competitionType` is `COMPETITIVE` and `groupingType` is `NON_TEAM_MATCH`.
* The `teamStatistics` property must be specified if the match's `competitionType` is `COMPETITIVE` and `groupingType` is `TEAM_MATCH`.

## `playerStatistics` and `teamStatistics`

`playerStatistics` is a property that retains player stats, and `teamStatistics` is a property that retains team stats. These property values are objects that contain multiple pairs, each consisting of a player/team identifier (`playerId/teamId`) and the stats (`stats`) of that player/team. Each stats object contains a stats identifier (`statsKey`) and a stats value (`statsValue`).

For `teamStatistics`, stats pertaining to each team member can be retained, in addition to team stats.

You do not necessarily need to include the stats of all players/teams. However, if a player participated in a match, even if for one time only, you may still include their stats even if they left during the middle of gameplay. Meanwhile, the players/teams with stats must always be included in the in-game roster.

# Child Activities (childActivities)

This property stores information of child activities (tasks/sub tasks) of the activity linked to the match. This property is only valid when the match's `competitionType` is `COOPERATIVE`.

The status and availability of child activities (tasks/sub tasks) can be updated by calling `updateMatchDetail` with `childActivities` specified for the match in progress. Each property is explained below.

## Child Activity Status (`status`)

The `status` property stores the status of a child activity. The match's progress can be updated by updating the child activity status. The progress status of a match entailing cooperative play is calculated based on the child activity status.

Upon creation of the match, `status` of all child activities will be set to WAITING. The status of child activities has three types: WAITING, PLAYING, and COMPLETED. Updates can only be made to transition from left to right in this order. An update that makes a status go back (right to left) from the current status can't be performed.

A sub task can only be updated if the parent task's status is already PLAYING or when the parent's task is being updated from WAITING to PLAYING or COMPLETED. The status of sub tasks can be updated at the same time the status of a parent task is updated.

## Child Activity Availability (`availability`)

The `availability` stores the availability of a child activity. The display or lack of display of the player's child activities can be controlled by updating the child activity availability.

Upon creation of the match, `availability` of all child activities will be set to UNAVAILABLE. A child activity will be displayed in the system software if its `availability` is set to AVAILABLE and won't be displayed if UNAVAILABLE is set.