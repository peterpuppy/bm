# PlayStation™Network Challenge Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Challenge_Activities-Guide/a-challenge-example.html

# Challenge Activity Use Case

This chapter shows an example of setting up and testing a challenge activity, including the lifecycle of the activity challenge instance, how these are represented in the UI, some of the different choices you have, and how these choices affect the overall user experience.

## Challenge Activity Object Configuration

This configuration focuses on the challenge-specific attributes used within the activity and assumes you have already created the required services for UDS and leaderboard for your title.

Using Horizon® as a game example, and the developer is setting up an activity object of type challenge called "Nora Hunting Grounds". The goal of this challenge is to get through this level as fast as possible. The top winner of the challenge is placed in the 1st place on the leaderboard and has the smallest time amongst other participants.

Example Properties Tab Values

| **Field** | **Description** |
| --- | --- |
| Object Id | HuntingGrounds |
| Subcategory (optional) | Hunting Grounds  This must be localized. This shows on the challenge activity card, above the challenge name. If not set, the title display name appears instead. |
| Display Order | Three  Auto-assigned by the system, as this is the third activity object defined for the game. |
| Display Name | Nora Hunting Grounds  This must be localized. |
| Description (optional) | Get through this level as fast as possible.  This must be localized. |
| Activity Large Image | A full screen image is used, which appears under the game's hub. |
| Activity Card Image | An activity card image is used. See below. |
| Available By Default | True  This challenge is available on start-up of the game. Users do not have to complete other activities to unlock this challenge. |
| Available From/To (optional) | Empty  This challenge is available all the time for users to participate in. |
| Personal Best Notification Only (optional) | False (by default)  Players receive two types of notifications: a personal best notification when they beat their best score, and a challenge completed notification, when they don't. |
| Global Leaderboard Cohort (optional) | True (by default)  Global cohorts are enabled. |
| Leaderboard Board ID | 1073741823  This title unique leaderboard ID is auto assigned by the system. The Leaderboards Tool can be used to manage this auto-generated leaderboard, with certain restrictions. |

In the **Statistics** tab, the fields are set as shown in the following table:

Example Statistics Tab Fields

| **Field** | **Description** |
| --- | --- |
| Score Name | Time. If the score name is for numeric scores, this also appears in notifications, and must be localized in that case. |
| Display Format | Time. Defines the value sent in milliseconds and interpreted as a time-based score. |
| Sort | Ascending. Lower values, which indicates fastest time, appear first in the leaderboard. |
| decimalPlaces (optional) | Zero. Indicating that the score is an integer. |

## Challenge Activity Life Cycle

A challenge activity is represented by the UI in the form of activity cards. The platform tracks the lifecycle of the challenge, from the instance the user engages with the challenge until it is completed or terminated. The information shown on the card depends on a number of factors, most importantly on the state of the challenge instance tracked by the platform. The following table shows some different representations of a challenge on the PlayStation®5 UI.

Challenge Instance UI Representation

|  |  |
| --- | --- |
| Unplayed Challenge | In-Progress Challenge |
| Completed Outcome | Failed/Abandoned Challenge |

A challenge is first presented to a player when it is suggested by the platform in a destination such as Control Center or game base. This may be due to a player reaching a specific location in the game, or due to a challenge being made available at a specific date and time. A challenge can also be introduced to players when they receive invites from a friend.

Once a player engages with the challenge by clicking on the start button (or by starting the challenge through any other means), the game should send an `activityStart` event to indicate to the platform that the challenge is now in progress and to increment the player's run counter to show how many attempts they've made directly in the card.

From the moment an `activityStart` event is received by the service, a challenge activity instance is created and tracked by the platform until the activity has ended (indicated by the game sending an `activityEnd` event).

During the time that a player is actively playing in a challenge, any representation of this challenge activity instance is shown with an "In Progress" label on the activity card.

When the player completes, fails, or restarts in the middle of a challenge, the outcome of the challenge instance is stored by the platform and the representation of the challenge activity card instance is changed according to `outcome` field value sent by the game in the `activityEnd` event:

If `outcome=completed`: This indicates to the platform that the player successfully completed the challenge and that the score should be stored, and stored in the challenge leaderboard if it is the player's best score or time. An empty `score` field results in the `outcome` being treated as `failed` instead.

If `outcome=failed`: This indicates to the platform that the player failed to complete the challenge (perhaps by not meeting the minimum time required, due to the player's character dying, or any other condition that invalidates the run).

If `outcome=abandoned`: This indicates to the platform that the player quit, restarted, or the player's character left the playable area in the middle of the challenge instance.

For either a `failed` or `abandoned` outcome, the representation of the challenge activity card instance is changed to show "Try Again".

The figure below summarizes how the `activityStart` and `activityEnd` parameters sent by the game affect the lifecycle of the challenge instance tracked by the platform, which in turn affect its UI representation on the console.

Challenge Lifecycle Example