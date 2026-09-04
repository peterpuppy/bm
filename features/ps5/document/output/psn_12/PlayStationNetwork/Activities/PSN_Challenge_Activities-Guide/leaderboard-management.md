# PlayStation™Network Challenge Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Challenge_Activities-Guide/leaderboard-management.html

# Managing Leaderboards

This chapter provides information on managing leaderboards for challenge activities.

Challenges use the platform Leaderboards Service. Refer to [Leaderboards Overview](../../../WebAPI/latest/Leaderboards-Overview/__document_toc.html) for more details. For leaderboards created for challenge objects (ones under "AutoGen"), the following limitations apply:

* The Leaderboards Management Web API cannot be used to record or delete scores. It can be used to retrieve scores and ranks to show in your game.
* The Leaderboards Tool cannot be used to record scores. You can however use it to retrieve scores and ranks.
* Each challenge leaderboard is limited to five million score entries. This number is subject to change in the future. Once the leaderboard is full, new entries override lower ranked entries and entries that do not qualify for placement are dropped.

## Resetting Leaderboards

Leaderboards can be reset using the reset button of the Leaderboards Tool to completely wipe out associated data. This operation should be coordinated by an administrator. Be aware that this has the effect of also removing all challenge play history and should only be used when absolutely necessary (for example, an exploit is discovered that allows players to get scores or times that should not have been achievable).

Due to the dynamic nature of running challenges, administrators must ensure that players actively playing the challenge to be reset are properly notified:

* SIE recommends that you make the challenge invalid for a period of time before resetting the score to prevent the challenge from being recommended by the system to users during the reset operation. This also prevents any unexpected behavior such as recording scores of in-progress challenge runs.
* Resetting a challenge may take time to propagate through the system. Sometimes activity cards may be stale or fail to load for a period of time.

Note: Deleting challenge activities using the UDS management tool does not delete the
associated leaderboard. The leaderboard linked to the deleted challenge activity does
not disrupt or impact user experience or the function of other challenge activities.