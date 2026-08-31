# Leaderboards Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards-Overview/user.html

# Components of the Leaderboards

This topic describes the user identifiers used in the Leaderboards service and the main specifications of the leaderboards you can create.

# User

With PlayStation™Network, account IDs are used as user identifiers, and Online IDs are used as display names. The Leaderboards service also accordingly uses combinations of an account ID and Online ID.

For details about account IDs and Online IDs, refer to the [Np Library Overview](../../../SDK/latest/Np-Overview/__document_toc.html) and [Np Library Reference](../../../SDK/latest/Np-Reference/__document_toc.html) documents.

# Player Character ID

The player character ID is a unique ID used by the Leaderboards service. For example, assume a scenario where one user selects several characters to play the game as and each character's score needs to be separately recorded. Using player character IDs will, in such cases, enable a user named foo (for example) to record scores separately under different names like "foo:0", "foo:1", and "foo:2". If the player character ID is not used or if specification for it is omitted, it will be handled as if the player character ID is 0.

Because the player character ID is only valid in the Leaderboards service, care is required when coordinating with the other PlayStation™Network features, if it is used. For example, only the account ID is used to register a player as a friend. It will be possible to register a user named foo as a friend, but it will not be possible to distinguish between "foo:0" and "foo:2" when sending/receiving messages. Because an invitation message gets sent to a player by specifying their account ID with the Matchmaking service or another such service, "foo:1" cannot be specified as the destination of an invitation message. In addition, information that can be added to the account ID, such as the avatar and profile, is limited to one per account ID; such information cannot be set per player character ID. Also, it is not possible to create a ranking by extracting only the same player character ID from an existing board. If you want to create a ranking for that same player character ID only, create another board with that same player character ID only.

Consider the use of player character IDs in your title with the understanding that their specifications are unique to the Leaderboards service.

# Server

Use of the Leaderboards service is by application only. A server will only be provided for titles that use the service.

# Leaderboards

Multiple leaderboards are provided per server. Basically, only one score per user can be recorded on a leaderboard. However, multiple scores per user can be entered by using player character IDs.

## Leaderboard Customization

The following elements can be customized in a leaderboard.

* Number of leaderboards and the maximum number of user entries per board
* Score display in ascending order/descending order
* Score update mode (overwrite without exception or overwrite only when breaking record)
* Maximum size of large-volume attachment data
* Minimum rank for which large-volume attachment data can be recorded and attached to a score
* Sharing of scores with other leaderboards
* Scheduling of ranking snapshot output (in JSON or CSV format)
* Configuring score reset schedules

Leaderboard customization is subject to the following limitations.

* The maximum number for leaderboards is 10000 (board ID from 0 to 9999)
* The maximum number of score registrations on all the leaderboards is 3,200,000
* The maximum number of scores on one leaderboard is approximately 1,000,000
* The maximum total size of large-volume attached data on all the leaderboards must not exceed 1 GiB
* The maximum size of one instance of large-volume attachment data must not exceed 1 MiB
* The ranking snapshot output and score reset time must not be 00:00 (Even if the time is not 00:00, a time change may be requested if numerous titles have concentrated their output/reset times around a single time)

## Leaderboard Response

A score recorded on a leaderboard is first sent to the server for ranking creation processing and then reflected onto the leaderboard. In other words, when a score is first recorded, a temporary rank is returned to the user. There is a slight time lag until that score will be visible on the leaderboard from other users.

Usually, this time lag is at most a few dozen seconds, and the smaller the number of scores recorded per unit of time, the shorter the lag. Note, however, that the time lag may require a lengthy period to resolve when manual operations, such as deleting an invalid score, are performed or when a system failure occurs. Make sure to program your application so that it does not malfunction even if there is a lengthy time lag.