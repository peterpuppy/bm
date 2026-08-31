# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/trc-requirements-r5301.html

# Configuring Activities for Campaign and Story Modes

This chapter provides details on how to configure activities for games that feature campaign and story modes.

Campaign and story modes typically consist of a series of missions, chapters, or levels that players must complete to finish the campaign or story. Games with campaigns [must have at least one required progress activity that represents starting and finishing the campaign](trc-requirements-r5301.html "This topic provides information on the TRC requirements you must follow if your game has a campaign or story mode.").

Activities that you create for campaign and story modes [follow a general guidance that includes creating the activity, creating associated tasks, and managing the activity's state using UDS events](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters."). Depending on how you've designed your campaign, your activities may have configurations that extend beyond this general guidance. For example, activity configuration is different for linear and non-linear campaigns.

After you've followed the general guidance for creating campaign and story mode activities, follow the extended guidance based on your game's design:

* [Campaigns with collectible objectives (linear games)](collectibles-linear.html "This topic provides guidance for configuring activities that handle collectibles in linear games.")
* [Campaigns with collectible objectives (open world games)](collectibles-open-world.html "This topic provides guidance for configuring activities that handle collectibles in open world games.")
* [Campaigns with cooperative multiplayer](cooperative-campaigns.html "This topic provides guidance on configuring activities for games with cooperative multiplayer campaigns.")
* [Campaigns with Open world objectives](open-world.html "This topic provides guidance on configuring activities for games with open world objectives.")

# Configuring Activities for Required and Optional Missions, Chapters, and Levels

This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.

When designing activities for campaign and story modes, represent each mission as an activity and each mission objective as a task. This helps players understand what mission they are on, what they have left to do to complete the mission, and how long it may take. It also helps them find Game Help content as long as the activity or task does not exceed an hour of gameplay.

These activities can apply to first playthroughs, repeat playthroughs, and new game plus modes, as well as for linear and non-linear games.

Follow the best practices below when designing activities for games with campaign and story modes.

## Creating Activities

In this configuration, activities represent entire missions, chapters, or levels in your game.

1. Create a progress activity for each main or side mission, chapter, or level in your game. Progress activities represent parts of a game that have clearly defined start and end points. For more information on progress activities, see [Progress Activities](activity-types.html#psn-activities-guide_9_1__psn-activities-guide_9_1_1).
2. Give each activity a unique name that represents the mission. Ideally, this name matches how it’s displayed in the game.
3. Enable **Is Required for Completion** if the activity represents a mission that players must complete to finish the campaign. Do not enable this for activities that represent optional or side missions. Activities that are required for completion contribute to the game progress percentage that’s shown on the Game Hub. For more information, see [Activity Visibility on Game Hub](displaying-activities-game-hub.html "This topic provides information on how activities are displayed on the Game Hub.").

After you create an activity, create tasks to represent the mission's objectives. If you don't create tasks, PlayStation™Network generates Community Game Help for the entire activity as long as the activity is under one hour of gameplay.

## Creating Tasks

In this configuration, tasks represent the objectives that players must complete to finish a mission, chapter, or level.

1. Create a task for each mission objective and link it to the parent activity.
2. Link tasks in the order the player is likely to encounter them within the mission and name them in a way that conveys the intended path of completing the objective. For example:
   * “Drive to the meeting point”
   * “Defeat the enemies”
   * “Find a way to open the door”
3. If your mission can’t be broken down into objectives, create tasks based on your mission's checkpoints or auto-save points.
4. Enable **Is Required for Completion** if the task represents an objective that players must complete to finish the mission. Do not enable this if the objective is not required.

Game Help video walkthroughs appear on tasks and activities from Community Game Help if you don't upload custom Game Help videos.

Community Game Help videos are not generated for tasks or activities that exceed one hour in length. SIE recommends that tasks represent around 15 minutes or less of gameplay to generate effective Game Help videos. For more information, see [Game Help](feature-overview.html#psn-activities-guide_0_1__psn-activities-guide_0_1_1).

## Uploading Images

Upload an image for the activity card that represents the mission. Use a unique image for each mission so players can differentiate between activity cards.

Images must be 24-bit non-interlaced PNG files, 864 x 1040 pixels.

If you do not upload a Mini Activity Card Image, the activity card image is cropped to fit the activities shown in grouped activity cards in the Control Center.

For more information on how images are used in the UI, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.") and [Images](activity-attributes.html#psn-activities-guide_8_1__psn-activities-guide_8_1_6).

## Managing Activity State

Ensure your activities accurately represent the intended game state by sending the following events at the right time:

* `activityStart` - Send this event immediately when a player starts a mission, including on repeat playthroughs. If the activity includes tasks, send this event immediately when the player starts a task. This event moves activities and tasks into the *In Progress* state, allowing players to view them in the Game Hub. It also serves as the starting point for Community Game Help videos. Do not send this event when a player:
  + Makes progress in an activity or task that was previously started.
  + Loads a save where the activity or task is already in progress and was previously started. You can send this event again if the player is sent back to the starting point of the activity or task.
  + Reaches a fail state and is able to continue the activity or task from a checkpoint. You can send this event again if the player is sent back to the starting point of the activity or task.
* `activityEnd (outcome: completed)` - Send this event immediately when the player successfully completes a task. Additionally, send this event for the parent activity representing the mission once the player successfully completes it, even if it was already sent for all linked tasks. This event moves activities and tasks into the *Completed* state so other *In Progress* activities and tasks are shown more prominently in the Game Hub. It also serves as the ending point for Community Game Help videos. Do not send this event when a player:
  + Reaches a fail state and must restart the activity or task from any point.
  + Abandons the activity or task by leaving the mission area or beginning a new mission in an open world game.
  + Exits the campaign by returning to the main menu or switching to a different game mode.

For information on managing activities in games that support cross-platform save data, see [Completed](managing-single-player-activity-states.html#psn-activities-guide_7_1__psn-activities-guide_7_1_3).

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").

## Guidance for Other Game Designs

The best practices in this topic are universal when configuring activities for games with campaign and story modes, but do not cover alternate game designs such as multiple endings. Refer to the relevant topic that matches your game design for further guidance:

* [Configuring Activities for Missions, Chapters, and Levels with Multiple Completion Methods](multiple-completion-methods.html "This topic provides guidance on configuring activities for campaign modes with missions that have multiple completion methods.")
* [Configuring Activities for Campaigns or Missions with Branching Paths or Multiple Endings](multiple-endings.html "This topic provides guidance on creating activities for games that feature campaigns and missions with branching paths and multiple endings.")
* [Configuring Activities for Campaigns with Procedurally Generated Content](procedurally-generated-content.html "This topic provides guidance on configuring activities for games that feature campaigns with procedurally generated content.")

# Configuring Activities for Missions, Chapters, and Levels with Multiple Completion Methods

This topic provides guidance on configuring activities for campaign modes with missions that have multiple completion methods.

Note: Ensure that you [follow the general guidance for configuring activities for missions, chapters, and levels](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.") before implementing the guidance in this topic.

Some games feature missions or objectives that players can complete in multiple ways. For example, imagine a mission that begins by speaking with a wizard who tasks the player with retrieving a dragon’s egg.

The player can choose to steal one from a dragon’s nest, buy one from a shop, or pass a speech check to convince the wizard to use one of his own eggs. Once the player acquires the egg, regardless of the method, they speak with the wizard again to complete the mission.

To design activities for these types of missions:

1. Create an activity for the entire mission.
2. Create the tasks required to complete the activity. In the above scenario, the first required task would be to acquire a dragon’s egg. This task starts after the initial dialog with the wizard and ends once the egg has been acquired. The second required task would be returning the egg to the wizard. This task starts when the egg is acquired and ends once it’s given to the wizard.
3. Enable **Is Required for Completion**. This ensures that mandatory requirements for the quest are captured and updated with the player's progress through the mission.

PlayStation™Network generates Community Game Help videos that show a complete playthrough of the mission,using one of the possible completion methods chosen at random.

## Allowing all Possible Completion Methods in Game Help

There are scenarios when you may want to allow all possible completion methods in Community Game Help videos. For example, you may want to represent all solutions to show the breadth of possibilities allowed in the game, or to inform players that they can complete the task regardless of previous choices they may have made. In the scenario above, the option that involves passing the speech check can only be performed by players that built their character in a specific way.

In these cases, you might not want to risk showing a Community Game Help video that the player can’t replicate. Allowing all possible completion methods allows players to choose the best completion option based on their playstyle.

To allow all possible completion methods in Game Help:

1. Create tasks for each completion method. For example, create one task each for stealing the egg, buying an egg, and convincing the wizard to use his own egg.
2. Do not enable *Is Required for Completion*.

Send an `activityStart` event for these tasks after the initial conversation when the player starts the quest. Send an `activityEnd` event for these tasks only when the player completes them using the method above.

Incomplete tasks remain in the *In Progress* state; however, they are hidden in the UX as the parent activity moves into the *Completed* state when the `activityEnd (outcome: completed)` event is sent after the player completes the mission.

# Configuring Activities for Campaigns or Missions with Branching Paths or Multiple Endings

This topic provides guidance on creating activities for games that feature campaigns and missions with branching paths and multiple endings.

Note: Ensure that you [follow the general guidance for configuring activities for missions, chapters, and levels](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.") before implementing the guidance in this topic.

Some games feature stories with branching paths, where players may experience completely different content depending on the choices they make.

For games designed this way, ensure that you enable *Is Required for Completion* for all activities and tasks that every player will experience, regardless of player choice. This ensures that game progress and Community Game Help is available for the required parts of the game.

For activities and tasks that may not be experienced by all players, do not enable *Is Required for Completion*. This ensures that Community Game Help is available for all content, but completion of this content does not contribute towards the games completion progress shown on the Game Hub.

To create activities for games with multiple endings:

1. Create a generic activity that represents the entire campaign. The activity should start when the player begins the campaign and end once the campaign is completed, regardless of which ending was achieved. This ensures your game is adhering to the [TRC for campaigns (R5301)](trc-requirements-r5301.html "This topic provides information on the TRC requirements you must follow if your game has a campaign or story mode.") which requires a progress activity for campaigns.
2. Create separate activities to cover all variations of the final mission. Do not enable *Is Required for Completion* for these activities.

# Configuring Activities for Campaigns with Procedurally Generated Content

This topic provides guidance on configuring activities for games that feature campaigns with procedurally generated content.

Note: Ensure that you [follow the general guidance for configuring activities for missions, chapters, and levels](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.") before implementing the guidance in this topic.

Some games feature levels and dungeons with procedurally generated content, where players may explore different environmental layouts or enemy configurations.

For games designed this way, ensure that you enable **Is Required for Completion** for all activities and tasks that every player will experience. This ensures that game progress and Community Game Help is available for the required parts of the game.

For example, your game may feature procedurally generated dungeons where the layout and enemy configurations change after each player death, but the overall objectives remain the same. In this example, you would create an activity for each dungeon and create tasks that represent each objective. Then, enable **Is Required for Completion**, as all players must complete them in order to finish the game.

For activities and tasks that may not be experienced by all players, do not enable *Is Required for Completion*. This ensures that Community Game Help is available for all content, but completion of this content does not contribute towards the game's completion progress shown on the Game Hub.

For example, the boss that spawns might be one of five different options. In this case, you would create five tasks, each one representing one of the five possible bosses.

# Configuring Activities for Collectibles in Linear Games

This topic provides guidance for configuring activities that handle collectibles in linear games.

Collectibles represent single-time items or actions that players pick up or interact with in specific locations. This does not include things that players pick up repeatedly, such as currency, ammunition, or health.

Collectibles may not necessarily be items that are picked up. They may involve some other type of interaction. For example, the following things may be considered collectibles:

* Photo opportunities
* Stunt jumps
* Special NPC interactions
* Objects to break
* Legendary gear or weapons
* Legendary animal hunts
* Graffiti spots to clean or tag

Configuring activities for games that feature collectibles allows players to keep track of which collectibles they have and haven't picked up. Additionally, PlayStation™Network creates Community Game Help videos from those activities to show players where to find collectibles they can't find on their own.

Follow the best practices below when designing activities for collectibles in linear games:

## Creating Activities

In this configuration. activities represent the mission, level, or chapter where collectibles are present.

1. Create a progress activity for each mission, level, and chapter where collectibles are present. Don't create separate activities for individual collectible types. For example:
   * **Recommended** - an activity named “Collectibles - Chapter 1” that has tasks for all notes and audio logs that players can find in that chapter.
   * **Not recommended** - activities named "Audio Logs - Chapter 1” and “Survivor Notes - Chapter 1” where each type of collectible has its own activity and associated tasks per location.Progress activities are intended to represent parts of a game that have clearly defined start and end points. For more information on progress activities, see [Progress Activities](activity-types.html#psn-activities-guide_9_1__psn-activities-guide_9_1_1).
2. Give each activity a unique name that represents the collectibles for the mission, level, or chapter. If your game features multiple types of collectibles that can be found in a single chapter, use a generic name that players can understand. For example, “Collectibles - [chapter name]”. If your game only has one type of collectible, for example, audio logs, use a more specific name like “Audio Logs - [chapter name]”.

## Creating Tasks

In this configuration, tasks represent the individual collectibles that players interact with.

1. Create a task for each individual collectible and set the **Is Collectible for Game Help** field on each task.
2. Name each task. You can use generic names such as “Audio log 1” or “Audio log 2”, however; more specific names like “Audio log in the office desk” are recommended if applicable.
3. List the tasks in the order the player is likely to encounter them within the level.

If you don't upload custom Game Help videos, PlayStation™Network creates Community Game Help videos that start 30 seconds prior to the sending of the `activityEnd (outcome: completed)` event on tasks where you've set the **Is Collectible for Game Help** field. Game Help videos are most helpful to players if they show the player character traveling to the collectible and interacting with it.

If you need more than 30 seconds to show the location of the collectible, you may want to configure your activity as an open world objective. See [Configuring Activities for Open World Objectives](open-world.html "This topic provides guidance on configuring activities for games with open world objectives.") for more details.

For more information on tasks and Game Help, see [Tasks and Sub-tasks](tasks-and-subtasks.html "This topic provides information on task and sub-task object structure.") and [Game Help](feature-overview.html#psn-activities-guide_0_1__psn-activities-guide_0_1_1).

## Managing Activity State

Ensure your activities accurately represent the intended game state by sending the following events at the right time:

* `activityStart` - Send this event for the activities that represent missions where collectibles are present when the player starts one of those missions. This event moves the activity to the *In Progress* state, allowing players to find it as soon as they start a mission. Also send this event for each task within the activity so that spoiler treatment is removed from the task UI, allowing players to view Game Help videos. Based on your game design, you may have a large number of collectibles that become available to players at once.
* `activityEnd (outcome: completed)` - Send this event for the tasks representing individual collectibles immediately after the player interacts with them. Also send this event for the parent activity once the player finds the final collectible in that mission. For example, if the player found all audio logs in Chapter 1, send the event for the “Chapter 1 - Audio Logs” parent activity. This event moves the activity and tasks to the *Completed* state so other *In Progress* activities and tasks are shown more prominently in the Game Hub. It also creates Community Game Help videos starting 30 seconds before the event was sent, so send this event as soon as the player picks up the collectible to ensure the video shows the player character approaching the collectible.

For information on managing activities in games that support cross-platform save data, see [Completed](managing-single-player-activity-states.html#psn-activities-guide_7_1__psn-activities-guide_7_1_3).

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").

# Configuring Activities for Collectibles in Open World Games

This topic provides guidance for configuring activities that handle collectibles in open world games.

Collectibles represent single-time items or actions that players pick up or interact with in specific locations. This does not include things that players pick up repeatedly, such as currency, ammunition, or health.

Collectibles may not necessarily be items that players pick up, and may involve some other type of interaction. For example, the following things may be considered collectibles:

* Photo opportunities
* Stunt jumps
* Special NPC interactions
* Objects to break
* Legendary gear or weapons
* Legendary animal hunts
* Graffiti spots to clean or tag

Configuring activities for games that feature collectibles allows players to keep track of which collectibles they have and haven't picked up. Additionally, PlayStation™Network creates Community Game Help videos from those activities to show players where to find collectibles they can't find on their own.

Follow the best practices below when designing activities for collectibles in open world and non-linear games:

## Creating Activities

In this configuration, activities represent entire groups of collectibles.

1. Create one progress activity for each group of collectibles. For example, create one activity to “Find Treasure” and a separate activity to “Take Photos”. Progress activities are intended to represent parts of a game that have clearly defined start and end points. For more information on progress activities, see [Progress Activities](activity-types.html#psn-activities-guide_9_1__psn-activities-guide_9_1_1).
2. Give each activity a unique name that represents the objective of the collectible group. For example, “Find Treasure”. If you want to separate the collectible group to help prevent spoilers, consider including the location in the name, for example,“Find Treasure - Island 1”. Separating activities this way keeps later activities hidden until the player reaches those points in the game.

## Creating Tasks

In this configuration, tasks represent individual collectibles that players interact with.

1. Create one task for each individual collectible and set the **Is Collectible for Game Help** field on each task.
2. Name each task. You can use generic names such as “Treasure 1” or “Treasure 2”, however; more specific names such as “Treasure by the shipwreck” are recommended if applicable.
3. Link each task to its corresponding parent activity.

If you don't upload custom Game Help videos, PlayStation™Network creates Community Game Help videos that start 30 seconds prior to the sending of the `activityEnd (outcome: completed)` event on tasks where you've set the **Is Collectible for Game Help** field. Game Help videos are most helpful to players if they show the player character traveling to the collectible and interacting with it.

If you need more than 30 seconds to show the location of the collectible, you may want to configure your activity as an open world objective. See [Configuring Activities for Open World Objectives](open-world.html "This topic provides guidance on configuring activities for games with open world objectives.") for more details.

For more information on tasks and Game Help, see [Tasks and Sub-tasks](tasks-and-subtasks.html "This topic provides information on task and sub-task object structure.") and [Game Help](feature-overview.html#psn-activities-guide_0_1__psn-activities-guide_0_1_1).

## Managing Activity State

Ensure your activities accurately represent the intended game state by sending the following events at the right time:

* `activityStart` - Send this event for the tasks that represent each individual collectible when the player can start interacting with them. For example, if the player can start finding the collectible type as soon as the game begins, send this event at the start of the game. Alternatively, if the player must meet a condition before they can interact with the collectible type, don't send this event until they've met the condition. This event moves the activity to the *In Progress* state, allowing players to find it as soon as they can start interacting with it. Based on your game design, you may have a large number of collectibles that become available to players at once.
* `activityEnd (outcome: completed)` - Send this event for the tasks that represent individual collectibles immediately when the player interacts with them. For example, when the player picks up a piece of treasure. Also send this event for the parent activity that represents the collectible group once the player finds the final collectible in that group. For example, when the player finds all pieces of treasure. This event moves the activity and tasks to the *Completed* state so other *In Progress* activities and tasks are shown more prominently in the Game Hub. It also creates a Community Game Help video starting 30 seconds before the event was sent, so send this event as soon as the player picks up the collectible to ensure the video shows the player character approaching the collectible.

For information on managing activities in games that support cross-platform save data, see [Completed](managing-single-player-activity-states.html#psn-activities-guide_7_1__psn-activities-guide_7_1_3).

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").

# Configuring Activities for Cooperative Multiplayer Campaigns

This topic provides guidance on configuring activities for games with cooperative multiplayer campaigns.

When configuring activities for cooperative multiplayer campaigns, create single player activities rather than multiplayer activities.

Multiplayer activities are updated using the Matches Web API, which is primarily used for reporting match details in competitive modes. As cooperative multiplayer activities need to track campaign progress, the Matches Web API is not necessary. Additionally, multiplayer activities do not support Game Help, a main component of PlayStation™Network Activities.

To create activities for games with cooperative multiplayer:

1. [Configure activities as single player activities](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.").
2. Leave the *Number of Players* and *Total Number of Players* fields empty.
3. Set **Has Online Multiplayer** to **false**.

This ensures that PlayStation™Network does not treat your activity as a multiplayer activity.

# Configuring Activities for Open World Objectives

This topic provides guidance on configuring activities for games with open world objectives.

Non-linear and open world games frequently feature objectives that players can complete while exploring the world between missions. Players often complete these objectives multiple times at specific locations on the map. Unlike collectibles, these objectives typically have defined start and end points. For example:

Open World Objective Examples

| Objective Group | Start Point | End Point |
| --- | --- | --- |
| Clear enemy bases | Player character moves within close proximity of an enemy base | The player character defeats the last enemy in a base |
| Win races | A race begins | The player character wins a race |
| Climb lookout towers | Player character begins climbing a tower | Player character reaches the top of a tower |

When creating activities for open world objectives, represent each objective group as an activity and each individual objective as a task. For example, an activity could be "Win races" while its associated tasks would be "Win Race 1", "Win race 2", etc.

This allows players to understand what objectives they have and have not completed and find Game Help for content they can't complete on their own.

Follow the best practices below when designing activities for open world objectives.

## Creating Activities

In this configuration, activities represent a group of objectives.

1. Create one progress activity for each objective group. For example, create one activity to “Win races” and a separate activity to “Clear enemy bases”. Progress activities are intended to represent parts of a game that have clearly defined start and end points. For more information on progress activities, see [Progress Activities](activity-types.html#psn-activities-guide_9_1__psn-activities-guide_9_1_1).
2. Give each activity a unique name that represents the objective group. For example, "Win races". If you want to separate the objective group to help prevent spoilers, consider including the location in the name, for example, "Win races on island 1". Separating activities this way keeps later activities hidden until the player reaches those points in the game.

## Creating Tasks

1. Create a task for each individual objective the player must complete in the objective group. For example, if players must complete five races for the “Win races” activity, create five tasks, one for each race.
2. Name each task. You can give tasks generic names such as “Win race 1” or “Win race 2”, however; more specific names like “Win the race at the beach” or “Win the race downtown” are recommended if applicable.

For more information on tasks and Game Help, see [Tasks and Sub-tasks](tasks-and-subtasks.html "This topic provides information on task and sub-task object structure.") and [Game Help](feature-overview.html#psn-activities-guide_0_1__psn-activities-guide_0_1_1).

## Uploading Images

Upload an image for the activity card that represents the objective group. Use a unique image for each objective group so players can differentiate between activity cards.

Images must be 24-bit non-interlaced PNG files, 864 x 1040 pixels.

If you do not upload a Mini Activity Card Image, the activity card image is cropped to fit the activities shown in grouped activity cards in the Control Center.

For more information on how images are used in the UI, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.") and [Images](activity-attributes.html#psn-activities-guide_8_1__psn-activities-guide_8_1_6).

## Managing Activity State

Ensure your activities accurately represent the intended game state by sending the following events at the right time:

* `activityStart` - Send this event for the task immediately when a player starts it. This event moves the activity and task to the *In Progress* state, allowing players to find it. This event also serves as the starting point for Community Game Help videos.
* `activityEnd (outcome: completed)` - Send this event for the task immediately when the player successfully completes it. Also send this event for the parent activity representing the objective group once the player successfully completes the final objective. This event moves the activity and tasks to the *Completed* state so that other *In Progress* activities and tasks are shown more prominently in the Game Hub. This event also serves as the ending point for Community Game Help videos.

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").

# TRC R5301 Requirements for Games with Campaigns

This topic provides information on the TRC requirements you must follow if your game has a campaign or story mode.

If your game features a campaign or story mode, TRC [R5301](../../../TRC/latest/TRC/R5301.html) requires that you create at least one progress activity with *Is Required for Completion* enabled. If your game is a compilation or game bundle that includes more than one game in the package, you may be required to configure one progress activity for each campaign.

The following examples are game designs that must follow this TRC:

* Games with modes that feature a final mission, boss, or level that is part of game completion, or triggers an end cut-scene and credits
* Games with a campaign or story mode that allow players to save their progress and continue later
* Arcade style games with a definitive ending

The following examples are game designs that are not required to follow this TRC:

* Arcade style games without a definitive ending and that only include infinite play modes
* Games that are collections of free play modes such as local or online competitive modes
* Games that only feature free play or sandbox modes without clearly defined endings that are intended to be played indefinitely

While SIE enforces a minimum configuration for activities, SIE recommends that you follow the guidance in [Configuring Activities for Campaign and Story Modes](configuring-campaign-or-story-modes.html "This chapter provides details on how to configure activities for games that feature campaign and story modes.") to maximize the potential of activities.

Activities that are configured to the TRC minimum requirements lack most functionality that make them useful for players. Activities that exceed TRC minimum requirements see higher player engagement, leading to increased playtime and retention.

Follow the required minimum configuration below when designing activities for games with campaign and story modes.

## Creating Activities

In this configuration, activities represent an entire campaign or story, from start to finish.

1. Create a progress activity that represents your entire campaign.
2. Enable **Is Required for Completion**.
3. Give your activity a name that represents the campaign. It could be as simple as “Campaign” or “Complete the Story”.

## Managing Activity State

Ensure your activities accurately represent the intended game state by sending the following events at the right time:

* `activityStart` - Send this event for the activity immediately when the player starts the campaign.
* `activityEnd with (outcome: completed)` - Send this event for the activity when the player successfully completes the campaign.

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").