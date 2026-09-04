# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/displaying-activities.html

# Managing the Visibility of Activities, Tasks, and Sub-tasks

This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.

# Activity Visibility on Control Center

This topic provides information on how activities are displayed on Control Center.

## Full Size Activity Cards in the Control Center Action Card Strand

Full size action cards appear in the Control Center action card strand and display the activity's image, activity completion percentage, playtime estimates, and session members. Players can open these activity cards to view the *Activities Details* screen that displays additional information such as tasks, sub-tasks, Game Help content, descriptions, and rewards.

Activities appear as full size action cards in the following scenarios:

* The most recently updated progress activities that are in the *In Progress* state.
* The most recently updated open-ended activities that are in the *In Progress* state and that also contain Game Help.
* A player registers for a tournament and the start time is within ten minutes. Players can use this action card as a reminder for the tournament and as a way to join the tournament when it begins.
* A player is actively playing in a tournament. Players can use this action card to check the current tournament status or to re-join the tournament.
* A player is playing in a multiplayer session and there is an associated multiplayer activity. Players can use this action card to invite friends, send friend requests to other players in the match, or report players.

Activities are removed from this location if the most recent UDS event sent for the activity was any of the following: `activityTerminate`, `activityEnd(outcome: completed)`, `activityEnd(outcome: failed)`, `activityEnd(outcome: abandoned)`, `activityEnd(outcome: not defined)`.

Control Center

## Grouped Activity Cards in the Control Center Action Card Strand

Grouped activity cards appear in the Control Center action card strand and display a list of up to ten miniature activity cards, grouped by activity type.

Players can view details for these activities by highlighting each activity. As only up to ten activities appear within these cards, make sure to manage activity state so players can focus on the activities that are most relevant to what they’re currently doing.

Activities are grouped into the following categories:

* *Activities* and *Game Help Cards* - These cards include progress activities and open-ended activities that have Game Help. If an activity within the card features Game Help, the face of the card displays it. Otherwise, the card face is labeled as *Activities*. Activities within this card appear grouped by status, in the following order:
  + *In Progress* - Activities that players are currently playing. Activities appear in this state when an `activityStart` event is sent for it or any of its linked tasks or sub-tasks, and when an `activityEnd` event is sent for any of its linked tasks or sub-tasks. Activities in this section are sorted by most recently updated.
  + *Not Started* - Activities that players have not yet accessed. Activities appear in this state if they have never been started or completed from an `activityStart` or `activityEnd (outcome: completed)` event. Activities in this state are hidden via a spoiler block treatment unless you set them to **Available by Default** or make them available using `activityAvailabilityChange` calls. Players can reveal hidden activities with a button press. Hidden Activities appear if they contain Game Help. If game help does not exist for the activity, it doesn't appear in the *Not Started* section. Activities in this section are displayed in the order that you've configured your activities in UDS.
  + *Completed* - Activities that players have already completed. Activities appear in this state after you send the `activityEnd (outcome: completed)` event for it. Activities in this section are sorted by most recently updated.

    Activities and Game Help Card
* **Tournaments** - This card includes tournament type activities grouped by status in the following order:
  + *Registered* - Tournaments that players are currently registered for, including ongoing tournaments. Ordered by start time, with tournaments starting soonest at the top.
  + *Upcoming* - Tournaments that players have not registered for. Ordered by start time with the tournament starting soonest at the top.

    Tournaments
* **Challenges** - This card includes challenge activities grouped by status in the following order:
  + *Attempted* - Challenges the player has ever started or completed, ordered by most recently started or completed.
  + *Not Attempted* - Challenges the player has never started or completed, displayed in the order that you've configured your activities in UDS.

    Challenges

# Activity Visibility on Game Hub

This topic provides information on how activities are displayed on the Game Hub.

Activities can appear as a full page takeover in the Game Hub to encourage re-engagement with as game and remind players where they last left off.

When you display activities this way, the default Game Hub image is replaced with the large version of the activity's image if configured. The activity description is also visible. A label indicates if Game Help is available for the activity.

You can only display progress activities and joinable sessions as takeovers on Game Hub. Joinable sessions appear automatically if players can join them. If the first activity in the Game Hub activities strand is one of these types, it is displayed as a takeover instead of appearing in the strand.

Game Hub

## Activities Strand

Activities can appear as individual, full size action cards in an activity' action card strand on Game Hub. This strand displays up to 16 activities.

The strand displays:

* Available joinable sessions
* *In Progress* or *Completed* progress activities, listed in order of how recently the activity was updated. Updates are based on start/end events of the parent activity or any of its associated tasks or sub-tasks.
* Unearned trophies

Activities Strand

## Tournaments Strand

If you have configured tournaments, they appear as individual full size action cards in an action card strand on Game Hub. This strand displays up to ten tournaments, including those in registered and unregistered states.

Tournaments Strand

# Activity Visibility on the PlayStation™App

This topic provides information on how activities are displayed on the PlayStation™App.

Activities and tasks that have Game Help are visible on the *Play* screen of the PlayStation™App.

This allows players to view information and get help on their current objectives without having to pause the game.

Mobile Game Help

# Activity Visibility on Profile and Mini Profile

This topic provides information on how activities are displayed on Profile and Mini Profile.

Players' most recently updated activity displays on their Profile and Mini Profile. This allows other players to get more information about what they are currently doing.

The following types of activities are visible on a user’s Profile and Mini Profile:

* Sessions
* Progress activities
* Competitive activities
* Open-ended activities

Activities are removed from this location if the most recent UDS event sent for the activity was any of the following: `activityTerminate`, `activityEnd(outcome: completed)`, `activityEnd(outcome: failed)`, `activityEnd(outcome: abandoned)`, `activityEnd(outcome: not defined)`.

Example Activity on Profile
Example Activity on Mini Profile

# Task and Sub-task Visibility

This topic provides information on how tasks and sub-tasks are made visible to players.

Tasks and sub-tasks appear on the details screen of the activity they are linked to. Tasks appear on the activity details screen if there are no linked sub-tasks. If the tasks have linked sub-tasks, they are shown instead of the task.

The details screen of the parent activity displays the names of the tasks and sub-tasks and playtime estimates, if applicable. It also displays either a thumbnail image from a related Game Help video, or the related Game Help image, whichever is configured for the activity.

Up to three tasks or sub-tasks are shown directly on the details screen, with the remainder viewable under *View All Objectives*. As only three tasks or sub-tasks can appear at the top level, make sure to manage task and sub-task state so players can focus on the content most relevant to what they’re currently doing.

Tasks and sub-tasks are grouped by state into the following sections:

## Not Started

*Not Started* indicates tasks and sub-tasks the player has never played.

Tasks and sub-tasks appear in this section if they have never been started from an `activityStart` event or ended from an `activityEnd` event.

* Tasks and sub-tasks with Game Help always appear in this section with a spoiler block treatment unless they were configured as *Available by Default*, an `activityAvailabilityChange` event was sent, or if players manually reveal them.
* Tasks and sub-tasks without Game Help only appear in this section if they have been configured as *Available by Default* or an `activityAvailabilityChange` event was sent. They do not appear with a spoiler block treatment.

## In Progress

*In Progress* indicates tasks and sub-tasks that players are currently playing, sorted by most recently started.

Tasks and sub-tasks appear in this section if an `activityStart` event is sent but an `activityEnd(outcome: completed)` event has never been sent for the task or sub-task.

Tasks and sub-tasks in this section never have spoiler block treatment.

## Completed

*Completed* indicates tasks and sub-tasks the player has already completed.

Tasks and sub-tasks appear in this section after you send the `activityEnd (outcome: completed)` event.

Tasks and sub-tasks in this section never have spoiler block treatment.

# Avoiding Spoilers with Progress Activities

This topic provides guidance on how to configure and manage the state of progress activities with the intention of preventing spoilers.

When properly configured, activities can help players avoid spoilers when they search for help content. Unlike external sources on the internet, activities are built with spoiler protection in mind, showing players game-related details based on their current progress in the game.

## Configuring Activities and Tasks to Match Your Game’s Content

Although most activity usage occurs for activities in the *In Progress* state, it is possible for players to look at the details of activities they haven’t started playing yet.

You can reduce the risk of spoilers that players may come across when interacting with activities by matching activity content and state management to game progress, sending `activityStart` and `activityEnd` events at the right time, and naming activities and tasks appropriately.

**Matching Activity Content and State Management to Game Progress**

As it can be difficult to know where in your game players will need help, configure progress activities with Game Help that covers all of your game’s content. Full coverage of your game's content and appropriate state management allows players to find help content without having to use external sources.

For example, if an activity is not configured for collectibles, a player may encounter story related spoilers while looking up a collectible guide from an external source or checking the activity list to see if an activity exists for the collectible. If an activity for the collectible does exist, the player may come across spoilers if an `activityStart` event is not sent to reveal the details of the activity to the player at the appropriate time.

See [Configuring Activities Based on Your Game’s Design](configuring-activities-based-on-game-structure.html "This chapter provides on overview on how to maximize the potential of PlayStation™Network Activities by creating them based on how you've designed your game.") for guidance on configuring and managing activities that cover common game designs and content types. Following this guidance ensures that high quality Game Help content is available for players when they need it.

**Sending Activity Start and Activity End Events at the Right Time**

Community Game Help videos are automatically generated for your progress activities based on the `activtyStart` and `activityEnd` events that your game sends. The `activityStart` event acts as the timestamp for the start of the video and the `activityEnd` event acts as the timestamp for the end of the video. You can choose when to send these events to ensure that the generated video does not capture a moment you don’t want the player to see.

For example, if your game features cut-scenes at the start and end of each mission, you could send the `activityStart` event when gameplay begins after the beginning cut-scene and the `activityEnd` event at the end of the gameplay segment before the ending cut-scene. This ensures that the cut-scenes are not viewable in the video.

**Naming Activities and Tasks Appropriately**

While you generally should name activities and tasks in ways that are most helpful to players, there may be scenarios where using more generic terms can help prevent spoilers.

For example, if a mission objective involves winning a fight against a former ally, you could name the task “Defeat the enemy” rather than “Defeat (character name)”. Likewise, if a mission objective is to find a legendary artifact, you could name the task “Find the artifact” instead of “Find (artifact name)”.

## Example Activity Design

This example activity design explains what details players can see and what details are spoiler blocked on activities when players:

* First launch the game
* Start the campaign or story
* Progress through the first activity
* Complete the first activity and begin the second activity

**Activity State on a Player's First Game Launch**

When a player first launches the game, prior to them starting the campaign, the game does not send any events.

The first ten progress activities appear on the left panel of the grouped activity card in the *Not Started* state. By default, activities in this state have a spoiler block treatment that hides the activity name and image. The right panel, which displays additional information such as task names and Game Help content, also has a spoiler block treatment.

Spoiler Block Treatment Default State

You can remove spoiler block treatment for any activity by enabling *Available by Default* when configuring the activity, or by sending an `activityAvailabilityChange` event. This reveals the activity name and image, but not any task names or Game Help content. The most common use of this option is to ensure that activities that represent [repeatable game modes](configuring-repeatable-or-endless-modes.html "This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.") appear by default. You can also enable this option on the first activity so that players can see it immediately before starting a new campaign or story.

Activity Available from Configuration or UDS Event

Players can manually reveal details of activities in the *Not Started* state. This removes the spoiler block treatment revealing the activity name and image, as well as the task name and Game Help content of the first task.

Revealing Activity and Task Details

If the activity includes more than one task, players can display the task names and Game Help content for those tasks by selecting *Reveal All Objectives*.

Revealing All Objectives

**Activity State When the Player Starts the Campaign or Story**

When a player starts the campaign or story mode, the game sends an `activityStart` event for the activity that represents the first mission and for the task that represents the first objective. This moves the activity and the task into the *In Progress* state.

The activity appears at the front of the Control Center action card strand as a full-sized activity card displaying the activity name and image. This is the most common way players access activities and the Game Help Content within them. When a player selects the activity, the details screen displays the task name and help content of the first task. As the remaining tasks have not received an `activityStart` event, they remain in the *Not Started* state, hidden behind *Reveal all Objectives*.

Note: Only the player’s most recent in-progress activity appears in this position.

Most Recent In-Progress Activity in Control Center
Activity Details Screen

Within the grouped activity card, the activity representing the first mission moves to the *In Progress* section with its name and image displayed.

The activities representing the second mission and its collectibles remain in the *Not Started* state with a spoiler block treatment, as shown in the figure below:
Most Recent In-Progress Activity in Grouped Activity Card

Additionally, the player's profile displays the activity for other players to see.

Note: Only the player’s most recent in-progress activity appears in this position. If the viewer has never played the activity, (no `activityStart` or `activityEnd` has been received for the viewer), it has a spoiler block treatment. The viewer can reveal the hidden details if they choose.

Spoiler Blocked Activity On Player Profile

If the viewer has previously played that activity, it appears without a spoiler block treatment. Task names and Game Help content are never shown to the viewer regardless if they have played the activity or not.
Activity on Player Profile Without Spoiler Block

**Activity State as a Player Progresses Through the First Mission**

When a player completes the first objective and begins the second objective, the game sends an `activityEnd(outcome: completed)` event for the task representing the first objective and an `activtyStart` event for the task representing the second objective. This moves the first task to the *Completed* state and the second task to the *In Progress* state.

On the activity details screen, the task representing the first objective moves to the *Completed* section, behind *Reveal all Objectives*. The task representing the second objective moves to the top of the *In Progress* section.
Task Progression

**Activity State as the Player completes the First Activity and Begins the Second Activity**

When the player completes the first mission, the game sends an `activityEnd` event for the task representing the second objective and the activity representing the first mission. Then, the game sends an `activityStart` event for the activity representing the second mission and for the activity representing the second mission's collectibles, as well as for each task representing each individual collectible that can be found during the mission.

This ensures that the spoiler block treatment is removed from these tasks when the player begins playing the section of the game where they can find the collectibles.

The activity representing the first mission leaves the Control Center action card strand and is replaced by the activity representing the second mission.
Most Recent In Progress Activity

Within the grouped activity card, the activity representing the first mission moves to the *Completed* section.

Note: Only ten activities can appear in the grouped activity card. If ten activities already appear between the *In Progress* and *Not Started* sections, the *Completed* section does not appear.

The activities representing the second mission and its collectibles move to the *In Progress* section with spoiler block treatment removed. The details screen of the activity representing the collectibles in the second mission displays the task names and Game Help content of those tasks without spoiler block treatment.

In-Progress and Completed Activities in Grouped Activity Card

# Hiding Activities

This topic provides information on hiding activities in the PlayStation®5 UI.

Players can view activities, tasks, and sub-tasks that you publish to production, however; there may be cases where you don’t want them to be seen at all.

You can accomplish this by using the *Available From* and *Available To* fields. If configured, activities are only visible to players if the date falls within the date range that you specify. You can edit this range after publishing without the need for a game patch. Some instances where you might want to consider using this field are:

* You are publishing activities for upcoming post-release content and do not want players to see the activities prior to the release date. In this case, set *Available From* to the release date of the content.
* You are publishing activities for a limited time game mode. In this case, set *Available From* to the date the mode begins, and *Available Until* to the expected end date.
* You have published placeholder data, test data, or data related to content that was cut from your game. In this case, set *Available From* and *Available Until* to be any point in the past.

You can only configure *Available From* and *Available Until* for activities. If you have published tasks or sub-tasks that you don’t want players to see, hide the parent activity. If needed, publish a new activity with new tasks and sub-tasks to replace those that were removed.