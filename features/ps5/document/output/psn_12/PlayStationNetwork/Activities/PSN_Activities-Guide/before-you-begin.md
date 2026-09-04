# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/before-you-begin.html

# PlayStation™Network Activities Overview

This chapter provides an overview of PlayStation™Network Activities and its features.

PlayStation™Network Activities integrate with UDS data to represent different gameplay elements and such as levels, chapters, missions, quests, and game modes. PlayStation™Network displays activities you've configured throughout the PlayStation®5 UI to inform players about what they're currently doing, what they could be doing, and what other players are doing in a specific game.

Activities encourage continued interaction and engagement with your game by enabling the following features and functionality:

* Game Help
* Playtime estimates
* Activity progress
* Game progress
* Challenge leaderboards and invites
* Tournaments

To learn more about these features and how they help players and impact your game, see [Feature Overview](feature-overview.html "This topic provides information on the features you can configure with PlayStation™Network Activities.").

When you are ready to begin creating activities, see [Configuring Activities Based on Your Game’s Design](configuring-activities-based-on-game-structure.html "This chapter provides on overview on how to maximize the potential of PlayStation™Network Activities by creating them based on how you've designed your game.").

# Before you begin

## Intended Audience and Usage

This document is intended for developers who are adding activities to their game.

Begin by reading the [Feature Overview](feature-overview.html "This topic provides information on the features you can configure with PlayStation™Network Activities.") section to get an understanding of what functionality is available, how it helps players, and how it impacts your game.

After you've read the feature overview, read the sections in [Configuring Activities Based on Your Game’s Design](configuring-activities-based-on-game-structure.html "This chapter provides on overview on how to maximize the potential of PlayStation™Network Activities by creating them based on how you've designed your game.") that match your game's content. These sections provide guidance on how to configure and manage activities that lead to the highest player usage. These sections also refer you to supplemental parts of the document that provide more thorough explanations of the functionality and configuration options available to you. These links are optional but provide more information on specific topics if necessary.

# Feature Overview

This topic provides information on the features you can configure with PlayStation™Network Activities.

## Game Help

PlayStation™Network’s Game Help feature uses the UDS data sent by games to provide on-demand, spoiler-free help based on a player's current game progress. Players can view hints, tips, and video walkthroughs for specific activities and trophies on the console and the PlayStation™App.

On average, players that view Game Help content are more likely to complete the game and play more hours than players who played the same games but did not view Game Help content.

Game Help content falls under two categories:

* Community Game Help - Content that is automatically generated for progress activities through player activity
* Custom Game Help - Custom content that you create

Custom Game Help and Community Game Help content cannot both exist on a single title.

**Community Game Help**

Community Game Help automatically generates video walkthroughs that show successful completions of activities, tasks, or sub-tasks. Once generated, players can view these videos from a game's activity card.

Successful and complete playthroughs are determined by the `activityStart` and `activityEnd``outcome: completed` events your game sends to PlayStation™Network. These events also serve as the start and end points of the video. This allows you to control the video's content, length, and when a video is sent based on your game's activity structure. Community Game Help videos are only generated for progress activities and only for the smallest level object in the structure. For example, videos are generated for progress activities without tasks, tasks without sub-tasks, or sub-tasks.

The duration of Community Game Help videos is limited to one hour, meaning SIE can't generate videos for activities, tasks, or sub-tasks that can’t be completed within one hour. See [Configuring Activities for Campaign and Story Modes](configuring-campaign-or-story-modes.html "This chapter provides details on how to configure activities for games that feature campaign and story modes.") for guidance on how to configure and manage progress activities that produce high quality Community Game Help videos.

For more information on Community Game Help, see [PlayStation™Network Game Help Guide - Configuring Community Game Help](../PSN_Game_Help-Guide/community-game-help.html).

**Custom Game Help**

Using the Game Help Tool, you can publish custom videos and hint text for activities, tasks, and sub-tasks. Custom Game Help content must adhere to SIE's policy and guidelines. SIE may request modifications or remove content from production that does not adhere to these standards.

Custom Game Help

## Playtime Estimates

Playtime estimates appear on individual activities and tasks and inform players of how much time it takes to complete the activity or task.

These estimates are based on the `activityStart` and `activityEnd outcome: completed` events that PlayStation™Network receives as players start and complete activities. Using this data, SIE generates estimates of how long it will take a player to complete activities and tasks in a game. These estimates are personalized based on the user’s historical completion time for other activities in comparison to other players. They are prorated based on task and sub-task completion where possible.

Playtime estimates are displayed on activity card faces, in activity details, and in task lists. The maximum amount of time that can be displayed for a playtime estimation is two hours. You can display times in minutes depending on your activity structure.

As estimates are based on completion times from players, it is sometimes difficult or impossible to estimate an accurate completion time for an activity. In cases where playtime estimates are not considered to be accurate, no estimate is displayed.

You can provide playtime estimation data in your game's UDS configuration using the *Default Playtime Estimate* field. These default estimates are used until it’s possible to generate an accurate estimate based on player data.

Playtime Estimation

## Activity Progress

Activity progress is displayed on the face of the activity card as a percentage based on the number of required tasks and sub-tasks the player has completed and the remaining number of tasks and sub-tasks to complete. For example, if an activity includes five tasks and the player has completed two of those tasks, 40% is shown.

Activity Progress
>

Tasks and sub-tasks are considered completed when PlayStation™Network receives an `activityEnd outcome: completed` event for it.

For more information, see [Activity Visibility on Control Center](displaying-activities-control-center.html "This topic provides information on how activities are displayed on Control Center.").

## Game Progress

Game Progress is represented as a completion percentage and informs players of how much of the main campaign or story they've completed.

The player’s completion percentage is shown on the Game Hub if you’ve configured more than one progress type activity or task with *Is Required for Completion* enabled. For example, if your game has ten activities that are marked *Required for Completion* and the player has completed five of them, 50% is shown.

Since this number is intended to progress toward completing the main campaign, SIE recommends that you do not mark optional or side content as required. This includes post release content.

For more information, see [Activity Visibility on Game Hub](displaying-activities-game-hub.html "This topic provides information on how activities are displayed on the Game Hub.").

Game Progress 
>

## Challenge Leaderboards and Invites

Some games feature modes that a solo player can play repeatedly where they are ranked by time or score. For example:

* A mode in a puzzle game where the player must clear the board as fast as possible or achieve the highest score possible within a set time or before reaching a fail state
* Challenge missions with a scoring system
* Mission replays or speedrun modes with a scoring system
* Boss rush modes

You can configure challenge activities to create asynchronous multiplayer for these single player games and modes. For example:

* Leaderboards viewable within the PlayStation®5 system software
* Notifications that are sent when a friend gets a better score
* Invite flows to attract new players or re-engage lapsed players

For more information on configuring challenge activities, see “PlayStation™Network Challenge Activities Guide''.

Example Leaderboard

## Tournaments

Tournaments are single-elimination, one-versus-one bracket competitions that you can add to PlayStation®5 applications. For each tournament bracket, you can schedule and monitor a series of online multiplayer matches to determine the winner of the bracket, without the need to implement standalone matchmaking and bracketing logic. You can also configure prizes for tournaments to encourage re-engagement.

For more information, see [PlayStation®5 Tournaments Guide](../PS5_Tournaments-Guide/__document_toc.html).

Example Tournament