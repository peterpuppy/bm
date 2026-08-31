# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/managing-multiplayer-activity-states.html

# Managing the State of Activities, Tasks, and Sub-tasks

This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.

Activity state informs players when activities start, are in-progress, and end. Properly managing the state of activities keeps players aware of game completion progress as they play your game.

Manage the state and visibility of activities, tasks, and sub-tasks for single player activities by sending UDS events. You cannot send UDS events from your server. You must send UDS events from the console.

Manage the state of multiplayer activities, tasks, and sub-tasks using the Matches Web API. You can send Matches Web API calls from your server. For multiplayer activities, `activityAvaialbilityChange` events are sent as UDS events without the need to use the Matches Web API.

If your integration uses a server, you must first pass the known game state from your game server to your game client, then pass it on to UDS through the console.

For multiplayer games, you can create and handle your active activities by using the Matches Web API directly from your game server. SIE recommends that you do this using your game server to prevent players from finding a way to report erroneous results.

# Managing the State of Single Player Activities

This topic provides information on how to manage the state of single player activities.

Manage the state and visibility of activities, tasks, and sub-tasks for single player activities by sending UDS events.

Single player activities typically have three states:

* *Not Started*
* *In Progress*
* *Completed*

Properly managing the state of activities keeps players aware of game completion progress as they play your game.

## Not Started

Activities in the *Not Started* state represent activities that players have not yet accessed. By default, all progress, challenge, and open-ended activities and their associated tasks appear in this state. *Not Started* activities do not appear in the UI unless they contain Game Help.

While in this state, activities are visible in the UI with a spoiler block treatment. Players can manually reveal the details of any activity and task in this state. Sending an `activityStart` or `activityEnd (outcome: completed)` event reveals the details for activities and tasks and updates the activity's state to *In Progress* and *Completed*, respectively.

If you want your activities in the *Not Started* state to appear without a spoiler block treatment, send an `activityAvailabilityChange` event. For example, send this event in the following or similar situations:

* The player may have a new mission available in an open world game but they have not yet traveled to the mission start point.
* The player completed the game and a new mode was unlocked but the player has not started playing it yet.

You can also have *Not Started* activities appear without spoiler treatment by setting **Available by Default** to true. For example, set activities to *Available by Default* in the following or similar situations:

* The activity represents the first chapter or mission of the campaign.
* The activity represents a game mode that is always available to the player immediately upon starting the game.

You can only set *Available by Default* on activities. If you configured tasks or sub-tasks for an activity that is *Available by Default*, also send an `activityAvailabilityChange` event to display tasks and sub-tasks without a spoiler block treatment.

Players can view activities in the *Not started* state on grouped activity cards in the Control Center and on the activity card strand in Game Hub.

## In Progress

Activities in the *In Progress* state represent activities that players are currently playing. Sending an `activityStart` UDS event for an activity, task, or sub-task moves it to the *In Progress* state. Sending an `activtyStart` or `activityEnd` event for a task or sub-task moves the parent activity to the `In Progress`state as well.

You can reduce the overall events you send by only sending an `activityStart` or `activityEnd` event for the task representing the first objective of an activity rather than sending an `activityStart` event for the activity itself.

Activities in the *In Progress* state remain in that state until your game sends an `activityEnd (outcome: completed)` event for the activity.

Players can view *In Progress* activities on grouped activity cards in the Control Center and on the activity card strand in Game Hub. The most recently updated *In Progress* activity displays as a full sized activity card at the front of the action card strand in the Control Center.

## Completed

Activities in the *Completed* state represent activities that players have completed all objectives for. Sending an `activityEnd (outcome: completed)` event for an activity, task, or sub-task moves it to the *Completed* state.

Players can view activities in the *Completed* state on grouped activity cards in the Control Center and on the activity card strand in Game Hub.

**Cross-platform Save Data**

If your game allows players to use save data where progression can be made on other platforms without activities, including PlayStation®4, you can send an `activityEnd (outcome: completed)` event for all activities and tasks that have already been completed each time the save data created on another platform is loaded. This ensures all gameplay segments represented by activities appear as completed even if they were completed on another platform.

# Managing the State of Multiplayer Activities

This topic provides information on managing the state of multiplayer activities using the Matches Web API.

Matches allow you to manage activities where multiple players are playing together. You can use matches for progress, open-ended, and competitive activities.

Matches have a set of states that allow you to control the status of each match. Depending on the status, the player sees the activity in different places or not at all. The table below shows the available match states:

Match States

| State | Description |
| --- | --- |
| `WAITING` | The match is waiting for participants to register. Shown as *Active* in the UI. |
| `PLAYING` | The match has started. The activity is treated as active, appears on the player's control center, and is shown as their presence. |
| `ONHOLD` | The match has been temporarily suspended. Shown as *Active* in the UI. |
| `CANCELED` | The match was forced to terminate partway through. The match appears as history to the player but does not count towards any completed matches. |
| `COMPLETED` | The results of the match have been reported. The match shows the final result to the player and appears as part of their history. |

The `createMatch` request allows you to create a match and link it to the activity the match represents. This tells the platform what to expect from this match and to represent it properly.

When creating a match, set a reasonable expiration time. This allows for the system to clean up any matches that are not closed properly. If you do not set this value, the default expiration time is 24 hours. This ensures that matches do not remain in the system forever.

After you create a match, its state is set to `WAITING`. Keep the activity in this state until players begin playing. Once the match begins, use the `updateMatchStatus` request to update it to the correct status.

Score and additional statistics have no default values when you create a match. When you create a match, set stats to **0** or the appropriate starting number for each player as they are added. You can update these stats in real-time during the match using the `updateMatchDetail` request.

Matches are completed when you send the `reportResults` request or they hit the expiration time and are canceled.

When reporting results, you must report results for players who left during a match or changed teams, as their results in these cases are still are valid.

To cancel a match with a request, specify `CANCELLED` in `updateMatchStatus`.