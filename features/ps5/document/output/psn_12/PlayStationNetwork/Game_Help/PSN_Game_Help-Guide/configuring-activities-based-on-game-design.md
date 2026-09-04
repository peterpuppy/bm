# PlayStation™Network Game Help Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Help-Guide/configuring-activities-based-on-game-design.html

# Configuring Community Game Help

This chapter provides details on Community Game Help and how it's generated.

Community Game Help automatically generates video walk-throughs for progress activities and their tasks, based on the UDS events sent by your game. Community Game Help videos do not incur additional cost and do not require new development beyond using UDS events in your game.

Community Game Help videos are available inside the current Game Help UX on both console and the PlayStation™App. Videos are labeled as being from the community to inform players of the video's source.

## Community Game Help Design Overview

The following is an overview of the general lifecycle of Community Game Help content, from its development to its eventual availability for players to view.

**Developers Configure Their Activities in UDS**

Community Game Help generates its videos by listening to the UDS events sent by your game.

For each leaf node in the activity tree, PlayStation™Network listens to the `activityStart` and `activityEnd (outcome: completed)` events sent by your game and combine them into a single play-through, meaning that the way you design your activities directly impacts the final output of Community Game Help videos.

**Players Opt In to Community Game Help**

To have their game footage captured in Community Game Help, players must opt-in to the program.

Players can access their settings by navigating to **Settings** > **Captures and Broadcasts** > **Captures** > **Auto Captures** > **Community Game Help** on the PlayStation®5 console.

This is a one time opt-in and does not need to be configured on a per-game basis. Players from all SIE regions can opt-in to Community Game Help; however, child accounts are not allowed to opt-in.

**Opted-in Players Play Supported Games**

As players play through your game, you send `activityStart` and `activityEnd (outcome: completed)` events to update the state of your activities, tasks, and sub-tasks.

**Game Help Server Performs Logic**

PlayStation™Network uses the `activityStart` and `activityEnd (outcome: completed)` events sent by your game to construct potential play-throughs that may qualify for Game Help content.

As server logic looks at both `activityStart` and `activityEnd (outcome: completed)` events to construct a play-through, only successfully completed gameplay is included. The only exception to this logic is game content that involves collectables. For more information, see [Configuring Activities Based on Your Game's Design](configuring-activities-based-on-game-design.html "This topic provides links to other topics that explain how to optimize activities for Game Help content by configuring them based on the design of your game.").

For activity playtime calculations, PlayStation™Network checks to see if the player has opted-in to the Community Game Help program. If they have, their completion time for the target activity is compared to the rest of the community to see if it is representative of expected playtime.

PlayStation™Network excludes slower than average times and unusually fast times. This creates a successful playthrough that is representative of the average player experience. PlayStation™Network supports a maximum of three videos per leaf node at any one time.

**New Video Request is Sent to Player’s Console**

When a successful play-through is identified, PlayStation™Network sends a packet of information to that player's console to request creation of a video of that play-through.

The timestamps associated with the UDS data sent by the game are used to define the start and end of the video. The `activityStart` timestamp is the start of video, while the `activityEnd (outcome: completed)`timestamp is the end of video. PlayStation™Network generates a video file using these timestamps, uploads the video to Game Help services, and removes it from the player’s console storage.

**New Community Game Help Video is Shown to Other Players**

After receiving the video from a player’s console, other players can view it from inside the Game Help UX on console and mobile.

All Community Game Help videos are reviewed internally before being shown to other players. This provides stability to the system, but SIE has plans to eventually remove this step.

Community Game Help videos appear inside of activity cards on console and within the Game Help area in the PlayStation™App.

All Community Game Help videos are labeled on console and in the PlayStation™App to distinguish them from custom Game Help that you've created.

# Configuring Activities Based on Your Game's Design

This topic provides links to other topics that explain how to optimize activities for Game Help content by configuring them based on the design of your game.

PlayStation™Network uses the UDS events sent by your game to create Community Game Help content.

Specifically, the system looks for `activityStart` and `activityEnd (outcome: completed)` to determine what might qualify as Game Help content. For this to work, you must use the UDS management tool to properly configure your game's activities.

The way that you configure your game's activities determines the type and length of content that is generated for Community Game Help. Activities should represent meaningful chunks of gameplay that players may encounter. For example, if you anticipate that a particular section of your game will take 30 minutes for an average player to complete, and configure a related activity that reflects this, PlayStation™Network will create a 30 min Community Game Help video.

Note: Community Game Help videos are limited to a length of 60 minutes. SIE recommends that the expected length of time for any leaf node in the activity tree is at most 15-30 minutes.

For in-depth guidance on how to configure activities based on your game's design, see [PlayStation™Network Activities Guide - Configuring Activities Based on Your Game’s Design](../PSN_Activities-Guide/configuring-activities-based-on-game-structure.html).

# How Game Help is Associated with Activities

Hints are presented to players using help cards, which are associated with leaf activities in the game. Leaf activities can be any of the following:

* Activities that do not contain tasks.
* Tasks that do not contain sub-tasks.
* Sub-tasks

Help cards are only linked to leaf activities, which are indicated by the dark gray boxes in the figure below.

How Help Cards are Attached to Leaf Activities

## Progress Activities

Community Game Help is only created for progress activities in UDS. Open-ended, competitive, and challenge activities are not supported.

Community Game Help only looks at the leaf nodes in the activity tree when creating content. For example, if you configure an activity with tasks, Community Game Help only generates videos for the tasks and not the parent activity. Likewise, if any of the tasks have sub-tasks, only the sub-tasks receive Community Game Help content.

## activityStart and activityEnd (outcome: completed) Events

Community Game Help only looks at two UDS events sent by your game: `activityStart` and `activityEnd (outcome: completed)`.

PlayStation™Network combines the timestamp associated with the `activityStart` event with the timestamp for the `activityEnd (outcome: completed)` event into a single play-through of the activity.

PlayStation™Network also uses these events to perform the following actions:

* Track expected completion times from the entire community. Completion times from all players, including players that have not opted-in to the Community Game Help program, are compiled into percentiles so the system can understand what represents average gameplay for a particular activity. For more information on how this works, see [How Game Help Calculates Play Times](game-help-time-calculation.html "This topic provides information on how Game Help calculates play times for activities when determining if play-throughs are eligible for Community Game Help videos.").
* Compare eligible play-throughs against the wider community. To select a play-through that is representative of the average player's experience, PlayStation™Network looks at play-throughs from opted-in players to determine if their times fit within certain percentiles. Completion times that are too slow are excluded, with the default cutoff being 50th percentile and below. Completion times that are too fast are also excluded. with a default cutoff of 95th percentile and above.
* Exclude all play-throughs that do not have a successful `activityEnd (outcome: completed)` event.

## Collectables

Activities that involve collectables do not use both `activityStart` and `activityEnd (outcome: completed)` events to construct Community Game Help videos. Collectables are defined as leaf nodes in the UDS tool that have the *Is Collectable* flag set to `true`.

Is Collectable Field in the UDS Tool

When PlayStation™Network receives an `activityEnd (outcome: completed)` event for an activity and determines that the `Is Collectable` flag set to `true`, it ignores the timestamp of the `activityStart` event and sets the video start time to be 30 seconds prior to the `activityEnd (outcome: completed)` event.

Community Game Help treats the `activityEnd (outcome: completed)` timestamp literally when it comes to generating collectable videos. If you send the event after an extended animation or after a player is done inspecting the item, it may exclude the actual path showing how and where the player was able to find the collectable.

SIE recommends that you send the `activityEnd (outcome: completed)` event for collectables at the moment that a player has found the item and it is permanently considered found within your game’s logic.

# How Game Help Calculates Play Times

This topic provides information on how Game Help calculates play times for activities when determining if play-throughs are eligible for Community Game Help videos.

To determine if play-throughs are eligible for Community Game Help videos, PlayStation™Network gathers play times from the entire community of players for a particular activity, places those times into percentiles, and compares eligible play-throughs against those percentiles to determine if it fits within certain limits.

PlayStation™Network typically chooses play-throughs that fall between the 50th and 95th percentiles for that particular `activityId`, though the system may tighten or loosen the selected percentile range depending on the volume of completions and the distribution of play times.

## Calculating Uninterrupted Gameplay

To get the cleanest gameplay videos possible for Game Help, PlayStation™Network defaults to look for completion times and videos of uninterrupted gameplay. PlayStation™Network considers the order in which the game sends its UDS events for a specific `activityId`, and excludes play-throughs if those events are not sent in an expected order.

Game Help Content Eligibility

| First Event | Second Event | Eligible For Help? |
| --- | --- | --- |
| `activityStart` | `activityEnd (outcome: completed)` | Yes |
| `activityStart` | `activityStart` | No |
| `activityStart` | `activityEnd (outcome: completed) (abandoned)`  `activityEnd (outcome: completed) (failed)`  `activityEnd (outcome: completed) (empty)`  `activityTerminate`  `actvityResume` | No |
| `activityStart` | Game Close | No |
| `activityStart` | Console Rest Mode / Shut Off | No |

# Community Game Help Moderation Tool

This topic provides details about the Community Game Help Moderation
Tool.

Community Game Help is designed to be fully automated. Videos are initially selected based on how representative they are of overall gameplay. Players can rate the helpfulness of each video, with low-rated videos automatically removed by the system.

The Community Game Help Moderation Tool allows you to review game help videos that are automatically generated by the system and remove any videos that may be inappropriate for players. In the event a specific video contains potentially offensive content or could harm your game if left available, you can use the tool to review and remove the video directly without opening a DevNet ticket.

PlayStation™Network aims to keep up to three videos for each leaf node in the activity tree. If a video is removed for any reason, the system attempts to replace it with another video. Therefore, deleting videos using this tool does not remove Game Help entirely.

Note: Community Game Help only captures raw gameplay footage. If PlayStation™Network detects that player media, such as voice audio or webcam footage, was enabled during the requested timestamps, the console rejects the request to create the Game Help video.

**Supported Browsers**

The Community Game Help Moderation Tool is supported on Chrome and Firefox.

## Prerequisites

To use the Community Game Help Moderation Tool, you'll need:

* Access to the Universal Data System (UDS) Management Tool
* A successfully provisioned UDS service with an NP Communication ID for the DevNet product
* Title collaborator status in DevNet for the DevNet product or designated content creator status for the NP Communication ID

See [PlayStation™Network Service Setup Guide - Registering Titles - Product Access Privileges](../PSN_Service_Setup-Guide/product-access-privileges.html) for details on configuring permissions and provisioning services.

## Using the Community Game Help Moderation Tool

To use the tool, do the following:

1. From the UDS Management Tool, go to **UDS Management** > **Features** > **Game Help** > **Automated Activity Hints**.
2. Select an activity from the left navigation panel. The interface displays how many videos are live for that specific activity. If the activity has leaf nodes, it expands to show additional options.
3. Select a leaf node to view the available live content. The leaf node detail screen displays the selected video and its metadata, as well as any other live videos. You can use the video player to watch the currently selected video or choose a different video from the list.
4. To delete a video, select **Delete** and confirm your choice.

Note: Deleting Community Game Help videos is a permanent action and cannot be undone.

# Community Game Help Examples

This topic provides examples of Game Help implementation for different game designs.

The following examples showcase how PlayStation™Network uses the UDS activity events that you configure to create Community Game Help videos.

## Game Designs That Feature Missions, Chapters, or Levels

The following is an example of a mission called "The Quarantine Zone" from *The Last of Us Part I Remake*. The mission includes three main tasks that players must complete in sequence called “Get your guns from Robert”, “Follow Marlene”, and “Take Ellie out of town”:

* When the “The Quarantine Zone” activity begins, the game sends an `activityStart` event for the first task “Get your guns from Robert”. This starts the playtime calculation for the first task.
* When a player completes the first task and finishes the cut scene, the game sends an `activityEnd (outcome: completed)` event for the task “Get your guns from Robert”.
* PlayStation™Network determines that the 24 minute play-through meets the requirements of a Game Help video and requests a new video from the player's console.
* Other players looking for Game Help would see a video that was roughly 24 minutes long and covers the entire play-through from the introductory cut scene to the concluding cut scene of the "Get your guns from Robert" task.
* Alternatively, if your game had an introductory cut scene and/or an ending cut scene for each task, you could structure your events to send `activityStart` for the parent `activityId` but withhold the `activityStart` event for the first task until the introductory cut scene is over. Then, send the `activityEnd (outcome: completed)` event once the player performs the necessary in-game actions, but before the cut scene plays. The end result would be a video that includes only actual gameplay and would be roughly 19 minutes long as compared to 24 minutes.

Game Help for "Get your guns from Robert"

* After players complete the “Get your guns from Robert” task, the game moves immediately into the next task, “Follow Marlene”.
* The game sends an `activityStart` event for the next task.
* The player makes it through the next task and once complete, the game sends an `activityEnd (outcome: completed)` event for the task “Follow Marlene”. This results in a roughly five minute long video.

Game Help for "Follow Marlene"

Note: Community Game Help videos are selected from the entire community of eligible players for each game. In almost all cases, subsequent game help videos as in the example above would come from different players.

After the games sends an `activityEnd (outcome: completed)` event for the task “Follow Marlene”, an `activityStart` it sends an event for the task “Take Ellie out of town”. As above, when players complete this section, PlayStation™Network generates a roughly five minute long video.

Game Help for "Take Ellie out of town"

## Open World Objectives

Open world and optional objectives behave similarly to main missions; however, players can start side missions and leave them in an open state as they move on to other areas of the game. For these types of activities, PlayStation™Network utilizes percentile calculations for activity play times when creating Game Help content.

For players that start side missions and move on to other parts of the game before completing them, their overall playtimes are much longer than players that play these side missions from start to finish without deviating. Community Game Help only requires a small portion of the player base to start and complete a side mission without deviating to generate a high quality play-through video.

The following is an example of an optional side mission called “Cauldron: IOTA” in *Horizon Forbidden West*.

* When players enter the cauldron, the game sends an `activityStart` event.
* There are no tasks for this area of the game, so players go through the entire area before defeating the end boss.
* The game sends an `activityEnd (outcome: completed)` after players defeat the boss.

## Collectables

When you set the *Is Collectable* field to `true` for an `activityId`, PlayStation™Network ignores the `activityStart` time and generates a 30 second video that uses the `activityEnd (outcome: completed) (Completed time)` as the end time.

The following is an example of an activity in *The Last of Us Part I Remake* called “Quarantine Zone collectables”. This activity covers all of the different types of collectables for the mission called “The Quarantine Zone”:

* When players pick up one of the collectables, the game sends an `activityEnd (outcome: completed)` event for that specific `activityId` associated with the collectable.
* PlayStation™Network sends a request to that player’s console for a 30 second video that uses the `activityEnd (Completed)` timestamp as the end of the video, showing players approaching and finding the collectable.
* Other players looking to find all of the collectables are able to see a video on the task called “Find the drafting call”.

Game Help for "Quarantine Zone collectibles"

# Community Game Help Spoiler Block

This topic provides information on how spoiler block works for Community Game Help content and Official Hints.

When players interact with Game Help, it's possible for them to encounter content for parts of the game they haven’t reached yet, spoiling those parts of the game.

To avoid spoilers, the system applies a spoiler block based on UDS events sent by the game. If an activity is not available by default and has never been changed to available, or a player has not received an `activityStart` or `activityEnd` event for a specific activity object, that item is spoiler-blocked.

Spoiler block applies to Game Help content and activity-level metadata, such as the activity name or playtime estimate.

Spoiler Block Example

You can also address potential spoilers by ensuring that the names of activities, tasks, or sub-tasks do not contain anything that could be considered a spoiler. For more information, see [PlayStation™Network Activities Guide - Managing the Visibility of Activities, Tasks, and Sub-tasks - Avoiding Spoilers with Progress Activities](../PSN_Activities-Guide/avoiding-spoilers-with-progress-activities.html).

For information on the structure of activities and guidance on how to design them, see [PlayStation™Network Activities Guide - Configuring Activities Based on Your Game’s Design](../PSN_Activities-Guide/configuring-activities-based-on-game-structure.html).

## Example Use Cases

The following examples describe scenarios where the system applies spoiler block.

**Example 1: Start of the game**

The player has just started playing "The Last of Us Part I" for the first time. Only the first activity, “Hometown” was made available by default, so the stand alone activity card is visible to the player. However, none of the tasks for the activity have received an `activityStart` event, so all Game Help videos for the activity have spoiler block applied.
Activity Spoiler Block Example

Once the opening cut-scene ends, the game sends an `activityStart` event for its first task: “Find your dad”. That Game Help video is now visible in the activity card, but future tasks still have spoiler block applied and are listed behind the *Reveal All Objectives* button.
Reveal All Objectives

As the player progresses through the level, `activityStart` events are sent for each subsequent task until everything is either completed or encountered by the player.

**Example 2: Multiple activities**

In this example, the player has just completed the "Hometown" activity, which moves into the *Completed* state. The player starts the activity: "The Quarantine Zone" and an `activityStart` event is sent for the parent activity. After the cut-scene ends, an `activityStart` event is sent for the first task: “Get your guns from Robert”. No `activityStart` events have been sent for any subsequent tasks, so those elements have spoiler block applied and are listed as *Not Started*.
"Get your guns from Robert" Activity

The game also sends an `activityStart` event for the activity: "The Quarantine Zone Collectibles". This card displays in the aggregate Game Help card along with the activity: "The Quarantine Zone".

Aggregate Game Help Card

**Example 3: Collectibles**

Collectibles are treated differently from main missions and tasks because players can find them at any time. SIE recommends that you remove spoiler block from these tasks once a player is capable of finding them in the game. To ensure that spoiler block is not applied to activities that involve collectibles, send an `activityStart` event for each collectible as soon as it becomes available to the player.

In this example, the player is playing through the activity: "The Quarantine Zone", which also unlocks the corresponding "The Quarantine Zone Collectibles" activity. The game sends an `activityStart` event for all tasks inside of the activity: "The Quarantine Zone Collectibles", making all of the Game Help videos visible to the player.
Collectible Type Activity without Spoiler Block

Note: The timestamp associated with `activityStart` is ignored and only `activityEnd (outcome: completed)` is used. For more information, see [Community Game Help Examples](community-game-help-examples.html "This topic provides examples of Game Help implementation for different game designs.").

**Example 4: Revealing upcoming content**

The system does not automatically display activity and Game Help details that players have not yet encountered; however, players can choose to manually reveal those details.

In this example, the player has just started the activity: "The Quarantine Zone", and the game sent an `activityStart` event for the parent activity but not for the first task. If the player opens the Game Help card at this point, they would see a single thumbnail listed under *Upcoming (might contain spoilers)* with the option to select *Reveal All Objectives*.
Reveal All Objectives on the Aggregate Activity Card

Note: Spoiler blocked thumbnails are only shown when a player has no tasks or sub-tasks that have received an `activityStart` event.

If the player interacts with the Game Help thumbnail, they see the first instance of Game Help for the task: “Get your guns from Robert”. Players can view all of the upcoming tasks, including areas of the game they have not seen yet, by selecting *Reveal All Objectives*.
Game Help for a Revealed Task

Selecting *Reveal All Objectives* displays a second screen that shows players the entire activity.
Fully Revealed Activity

**Example 5: Revealing all content for an activity**

In this example, the player only has an `activityStart` event for the first activity. All other activities in the Game Help card are listed under *Not Started*. All details are hidden from the player, including the activity metadata. If the player selects *Show Details*, they see all activity information and Game Help content for that activity.

Show Details View

# Video Generation Errors

This topic provides details on unique error cases you may encounter when PlayStation™Network generates Community Game Help content.

When the Community Game Help system requests a new video from a player, the console may reject the request based on a number of cases.

While many of these cases deal with background information, for example, whether or not the player has enough temporary space on their hard drive or whether or not the player’s network connection may be affected, there are some unique cases you should be aware of.

## Video not found on ring buffer

The PlayStation®5 overwrites its media capture ring buffer every 60 minutes. If the timestamps for a completed activity exceed this time, the console cannot generate a Game Help video.

While all requests over 60 minutes are guaranteed to fail, the closer a completed activity gets to 60 minutes, the more likely it is that the request will fail due to the time it takes for information to move through PlayStation™Network.

To avoid this error, ensure that activities you configure have leaf nodes that players can complete in roughly 15 minutes.

## Player Audio, Party Voice Audio, or Webcam detected

Community Game Help only captures raw gameplay footage.

If PlayStation™Network detects that player media such as voice audio or web cam footage was enabled during the requested timestamps, the console rejects the request to create the Game Help video.