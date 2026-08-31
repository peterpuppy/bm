# PlayStation™Network Challenge Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Challenge_Activities-Guide/notifications.html

# About Notifications

This chapter provides information on console notifications related to challenge activities.

Console notifications are integral for players to participate in challenges. Notifications generated for challenges consist of both a toast and an expanded version of the notification that can be accessed when the player presses the PS button.

In the expanded mode of the notification, *Play* invokes the Game Intent and brings the player back to the challenge (as configured by your title). *View Details* takes the player back to the challenge card.

## Personal Best Notification

A personal best notification is sent every time the `activityEnd` event is received by the server with a score and a completed outcome, and when the player has beaten their previous best score recorded by the server. The score sent is reported in the notification directly, as well as the change in rank.

Personal Best Notification

## Challenge Completion Notification

A challenge completed notification is sent every time the `activityEnd` event is received by the server with a score and a completed outcome, and when the player did not beat their previous best score recorded by the server. The score sent is reported in the notification directly.

Challenge Complete Notification

**Limiting This Notification to Player Personal Bests**

To limit notifications to only when a player has beaten their previous score, you can configure the challenge activity object using the tools with `Personal Best Notification = True`. This way players get notified only when they beat their best score and receive the personal best notification and never receive the challenge completed notification.

## Score Beaten By Friend Notification

When a friend of the current player participates in the same challenge and beats the player's score on the leaderboard, this notification is sent as a way to re-engage players with the challenge.

Beaten By Friend Notification

## Invite Notification

When a player explicitly invites another player using the invite button on the challenge card, this notification is sent to the recipient.

Invite Notification

## Global 100 Knockout Notification

When a player who originally ranked in the top 100 players on the global leaderboard for a challenge, got overtaken by other players and fell out of the top 100, this notification is sent as a way to re-engage the player with the challenge.

Global 100 Knockout Notification