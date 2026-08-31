# PlayStation™Network Challenge Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Challenge_Activities-Guide/challenges-best-practices.html

# Challenge Activity Best Practices

This chapter describes best practices to follow when configuring challenge activities.

There are some major differences between challenges and all other activity types that you should be aware of when determining which of your in-game modes you are considering supporting as a challenge.

## Real-Time Notifications

Although challenges are designed for asynchronous competition, system notifications are used to provide real-time updates to users related to completion of a challenge, the player's time or score being surpassed by a friend in the Leaderboard, player-to-player invitations from friends, etc. Due to these notifications, please be aware that players may be surprised to see a system notification triggered if it was not clear to the player through the in-game UX that they were about to participate in a challenge that results in placement in a leaderboard that is visible by their friends and other participants. The figure below has examples of real-time challenge notifications.

Examples of Challenge Notifications

## Friends-Only Challenges

If your game supports activities that result in a score or time that can promote friendly competition amongst smaller groups of players, but may not scale globally due to a high likelihood of ties for top placed players, you can elect to disable the Global Leaderboard. Players are still notified when they've been challenged or beaten by a friend. You can always decide to enable the Global Leaderboard at a later date as all results are maintained in the leaderboards service.

## Image Usage

Other than providing a background image for your challenge cards, the small image (864w x 1040h) is also shown in the expanded state of challenge notifications. In addition to the guidelines listed in the Configuring Your Activities section, please also ensure that small images provided for challenges still are clear to users when shown as standalone imagery in notifications when there is less metadata surrounding it. The figure below shows a vague image, while following figure below shows an image that is clearer.

Potentially Vague Image
Better, Clearer Imagery

## Handling Ties

Challenges work best when the scores or times posted are unlikely to result in a significant number of ties. Please use smaller units where possible to help reduce ties, e.g. using milliseconds for time trials and large point variations for score-based challenges. If you have a game mode where ties are commonplace, it probably does not work well as a challenge.

## In-Game Leaderboards

If you want to show challenge leaderboards in-game, you must integrate with the Leaderboards service. The Leaderboards service provides you with the raw ranking information required to display rankings in-game; however, there may not be 100% consistency with what is shown in the challenges leaderboards due to platform-level anonymization of results based on privacy settings. It is good practice to design your in-game leaderboards to match with your own design goals and not to try and align directly with what is shown in the platform UX.

## Score Statistic Name

Please be aware that the Score Statistic Name provided when creating your challenge also appears directly in the platform side leaderboards. As there is a limited amount of screen real estate for this string, please be sure to verify how the score statistic looks when displayed in the challenge leaderboard.

## Rewards Distribution

If your challenges have rewards associated with them, rewards information (image + text) can be shown directly in the challenge card as shown above in Rewards for Activity Completion. For challenges, it is important that players have an easy way to confirm rewards acquisition directly in-game as the Challenges UI is not able to confirm or update on rewards fulfillment status.

## Ensuring Proper Player Stats and Future Extensibility

In order to ensure that players are seeing the correct run counter for their number of attempts for each of your challenges, and to ensure that future functionality added on the platform works correctly for your title, please be sure to always send a corresponding `activityStart` and `activityEnd` for each challenge run. This applies regardless of whether the player successfully completes the run or restarts in the middle of an attempt due to an in-game death or manual restart.

## Challenges and Game Intents

In addition to the guidelines provided in the Handling Game Intents section, keep in mind that placement of the player is particularly important when linking into challenges. If the game intent associated with a challenge drops a player into a different area of the current level or map, it may be difficult for players to understand why the challenge has not started or where to go in order to start the challenge. If the game intent cannot take the player to exactly where they must be to start a challenge, please ensure that there is appropriate in-game messaging to direct them accordingly.

## Handling Changes to Challenges When Challenge is Live

Please be aware that we do not automatically notify players of any changes to a challenge that have been made after it has been released (e.g. in-game updates, rewards or description modifications, etc.).

## Co-op

Challenges are a single player focused experience. To have players play a challenge cooperatively, each signed-in player's score must be posted as individual, distinguishable entries.

## Handling Fail Conditions

If a challenge can be failed (for example, when not finished within a specified time limit or due to an in-game death, etc.), please indicate that the challenge failed by using outcome = FAILED in the `activityEnd` so that errant scores are not posted.

## Offline Scenarios

In general, challenges should not be available when the user is offline. However, in the case of temporary outages, challenge results are still posted once the user comes back online. However, if a challenge has already ended when the score comes in, it is not posted to the leaderboard.