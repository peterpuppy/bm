# Matches Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matches_WebAPI-Overview/using-the-web-api.html

# Using the Web API

# Basic Procedure

This chapter describes typical usage of the Matches Web API.

## (1) Create a match

Before gameplay begins, appoint one of the players participating in the match as a representative player and use that player's user context to create a (`createMatch`). It's possible to arbitrarily select the representative player on the application side; if a Game Session is being used, it's also possible to make the Game Session's representative user the representative player.

The status of a created match will be WAITING.

## (2) Change the match status

Because the status of the created match will be WAITING, be sure to update the status (`updateMatchStatus`) to PLAYING when the user begins gameplay. Also, update the status of the match as required, based on the conditions of how the game is proceeding. For details about the statuses that matches can be in, refer to the "[Match Status (status)](match-status-status.html)" section of the "[Overview and the Main Properties of Matches](overview-and-the-main-properties-of-matches.html)" chapter. Any player's user context can be used to update the status of the match.

## (3) Update match information

If players leave or join partway through, or there is some other change regarding the players in the middle of the competition, update the in-game roster (`leaveMatch`/`joinMatch`). Note that it is possible to update the information regarding new team additions and the participants at the same time (`updateMatchDetail`). When you update the in-game roster using `updateMatchDetail`, set the in-game roster with the latest statuses reflecting changes to the players and teams. If you do not set the players who had previously been included in the in-game roster in the roster at the time that `updateMatchDetail` is used, those players will leave the match at that point.

In accordance with the game's progress, report interim progress results (`updateMatchDetail`) when there's an update in the results (`matchResults`) or stats (`matchStatistics`). Interim progress results (`matchResults`) can only be reported for competitive play (when `competitionType` is `COMPETITIVE`).

Update the status and availability of tasks/sub tasks in accordance with the game's progress for cooperative play (when `competitionType` is `COOPERATIVE` if child activities (tasks/sub tasks) are set to the activity linked to the match.

Any player's user context can be used to update match information.

## (4) Report the results of the match

After the game has finished, report required data, such as ranks, scores, stats, etc., along with the final results (`reportResults`). Any player's user context can be used to report results.

Be aware that the format of the data sent differs depending on the type of activity selected. For details about results, refer to the "[Result (competitiveResult/cooperativeResult)](result-competitive-result-cooperative-result.html)" section of the "[Overview and the Main Properties of Matches](overview-and-the-main-properties-of-matches.html)" chapter.

Only the first-reported results will be used; results cannot be subsequently added or overwritten.

## Obtaining Detailed Information About Matches

You can obtain the current status of a match by specifying the match ID issued at the time the match was created (`getMatchDetail`). This feature is expected to be used in cases such as when current match conditions need to be confirmed when the representative user is changed. Any player's user context can be used to obtain detailed information about a match.