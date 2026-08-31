# Leaderboards Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards-Overview/faq.html

# Notes

This topic describes the points to note when using the Leaderboards service as well as FAQs.

# Notes Regarding Server Load and Request Frequency

Server overloads are possible for an application with high request call rates when the number of users increases. Note the following regarding specification design and implementation of your application. (When in doubt regarding a specification or implementation, contact SIE.)

If excessive access is performed, SIE may stop services for the corresponding application without notice. The points below should be carefully considered in particular for large-scale applications.

## Frequency of Recording Scores

On average, relative to the overall playing time of the game, the frequency of recording scores should be kept to under once every 5 minutes.

For example, avoid recording a score per game if the game ends every 30 seconds on average. However, make your decision based on the average of the overall game. For a game with mini-games inserted within, it will most probably not be a problem to allow the recording of scores for mini-games that end in 30 seconds. When accessing multiple leaderboards at the same time, the recording of a score to four leaderboards can be counted as one recording. In other words, when recording one score to four leaderboards: normal ranking, today's ranking, this week's ranking, and this month's ranking at the same time, this can be counted as one recording.

Using large-volume attachment data frequently can result in high server loads. If the data size is only up to 189 bytes, recording of small-volume attachment data can be done without any restrictions on the number of users; therefore, if the size is sufficiently small, use that type of attachment data.

## Frequency of Score Access

If the following points are noted, there will be no limit placed on the frequency of access to the server for obtaining scores.

* All obtained score information is displayed onscreen
* Score information is not discarded
* Score information is not obtained unless it is known that it is necessary
* Large amounts of data are not summarized and displayed (calculating the average of all the users' scores recorded on the leaderboard, for example)

Even if these points are not honored, it is still acceptable to access the server for scores approximately once every 5 minutes. However, server performance is finite, so avoid unnecessary access as much as possible, by, for example, taking measures to cache the data of attachments that are known to be used more than once wherever possible.

## Number of Simultaneous Communication Processes

When executing multiple communication processes (recording scores and accessing ranking data), keep the number of simultaneous communication processes to 6 processes or fewer.

The simultaneous execution of numerous communication processes causes not only the problem of increasing server load but extremely long wait times depending on the user's network environment. For example, a network delay will occur if a communication process is executed per friend when obtaining ranking data of a user's friends. The group parameter and the offset/limit parameter can be used to obtain multiple rankings of a specified number of friends at once. The `users` parameter can be used to obtain the rankings of multiple users at once even if they are not friends of the user; obtain rankings in a batch wherever possible.

As another example, if information of all leaderboards is obtained simultaneously when accessing ranking data, it is possible for a network delay to occur depending on the number of leaderboards. Take measures, for example, to only obtain the leaderboard information needed at the time according to the user's scrolling operation.

## Reloads

If you are implementing a reload feature to update information to the latest version whenever ranking data is viewed, design it so that the user cannot unnecessarily reload the data too frequently. For example, avoid a design where multiple reloads occur consecutively while the reload button is held down.

## Automatic Communication Processes

Processing that repeatedly obtains ranking data automatically without user operation as a trigger will lead to an increase in the server load. Avoid such processing regardless of its usage frequency.

It is not a problem to adopt automatic data obtainment if positive effects can be expected from it; however, even in such cases, try to reduce the data volume as much as possible (for example, by only receiving large-volume attachment data when the user instructs it). Contact SIE when in doubt about adopting automatic communication processes.

## Handling "Currently Undergoing Maintenance"

When an application performs excessive access to ranking servers, SIE may stop service provision for that application without notice. In such cases, an error will be returned to the application, indicating that ranking servers cannot be used temporarily. Implement appropriate handling for this error.

Note that Private Support will contact the publisher after services have been stopped. SIE may request you to revise the frequency and procedure by which the application accesses servers.

# Limitations of the Leaderboards Tool

The following features cannot currently be used by titles that have been migrated to the PlayStation® environments of the Sandbox network architecture:

* [Configuring ranking snapshot output schedules](using-the-leaderboards-tool.html#leaderboards-overview_2_2__leaderboards-overview_2_2_3)
* [Configuring score reset schedules](using-the-leaderboards-tool.html#leaderboards-overview_2_2__leaderboards-overview_2_2_4)
* [Operational history](using-the-leaderboards-tool.html#leaderboards-overview_2_2__leaderboards-overview_2_2_6)

# FAQ

## Q: Can a player enter multiple scores on one leaderboard?

A: As a general rule, a single user is allowed to record one score per leaderboard; however, a user can record multiple scores to a leaderboard by using player character IDs. However, note that this makes it difficult to realize friend rankings, etc. Consider the usage of player character IDs with this point in mind. It will not be possible to specify multiple player character IDs when obtaining friends' rankings.

## Q: Is there a filter against inappropriate text?

A: The Profanity Filter Web API is provided.

Refer to [Profanity Filter Web API Overview](../Profanity_Filter_WebAPI-Overview/__document_toc.html) for details.

## Q: Can small-volume attachment data be modified after recording a score?

A: If the leaderboard has the setting to always overwrite with the new score without exception, small-volume attachment data can be modified at arbitrary times.

Note, however, that the processing to record scores entails a heavy server load; avoid frequent usage.

## Q: If two users have the same score, how will the ranking of their scores be handled?

A: Two ranking systems are provided in every leaderboard - one that deems same scores to be of equal ranking (`rank`) and one that favors a score according to a first-come-first-serve basis (`serialRank`).

## Q: Can size of replay data that can be attached be changed?

A: Although there is a limit placed on the total size of game data to be attached, it is possible to customize the number of people who can record replay data and the size of data to be attached by each player.

The total size of data for all leaderboards should be kept under 1 GiB. Upper limits on the size of data to be attached per player and the number of players to be recorded can be changed per leaderboard. Therefore, customization of a leaderboard as in the following examples is permitted.

* Having 160 leaderboards where players with the top 50 ranked scores can record 128 KiB of data each (= 1000 MiB)
* Having 320 leaderboards where players with the top 25 ranked scores can record 128 KiB of data each (= 1000 MiB)
* Having 8 leaderboards where players with the top 1000 ranked scores can record 64 KiB of data each and having 64 leaderboards without any game data attached (= 500 MiB + 0 MB)

## Q: Do scores need to be reset when the Entry Limit on the leaderboard has been changed?

A: No score reset is required. The existing scores can be used as-is.

## Q: What is the behavior after the Entry Limit of the leaderboard has been changed?

A: If the Entry Limit has been reduced, data outside the range of the new Entry Limit may be returned when obtaining rankings. However, if at least one score is recorded immediately after the change to a reduced Entry Limit, the new Entry Limit will be applied and data within the range of the new Entry Limit will be returned when obtaining rankings. If the Entry Limit has been increased, there are no special considerations.

## Q: Are Score Ranking and Leaderboards compatible with each other?

A: Score Ranking and Leaderboards are not compatible with each other and have no history of supporting data transfers. Also, there are no plans to support their compatibility in the future.

## Q: Can score resets be scheduled for Activity Challenge boards?

A: No.