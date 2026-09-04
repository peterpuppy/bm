# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/local-multiplayer.html

# Configuring Activities for Repeatable and Endless Modes

This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.

Some games feature modes outside of the main campaign that players can play repeatedly that do not have fixed end points.

When creating activities for these types of game modes, ensure that you are accurately representing the player's state on their profile or the friends list so that other players can see what they’re doing in the game at the moment.

Follow the guidance below when designing activities for endless game modes:

## Creating Activities

1. Create an open ended activity for each applicable mode in your game. Open ended activities represent parts of a game that players can play repeatedly. They do not have defined endings, and do not represent a player's progression toward completing the game. For more information on open ended activities, see [Open Ended Activities](activity-types.html#psn-activities-guide_9_1__psn-activities-guide_9_1_2).
2. Give each activity a unique name that represents the mode.
3. Do not enable *Is Required for Completion* unless the activity is required for the player to progress through the main campaign. If the mode represents part of the campaign or is considered a completion requirement, you may want to [create a required progress activity instead](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.").
4. If you have configured an open ended activity that is always accessible by the player, set **Available by Default** to **true**. *Available by Default* makes the activity visible in the UI without a spoiler block treatment. For more information, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.").

## Uploading Images

Upload an image for the activity card that represents the mode. Use a unique image for each mode so players can differentiate between activity cards.

Images must be 24-bit non-interlaced PNG files, 864 x 1040 pixels.

If you do not upload a Mini Activity Card Image, the activity card image is cropped to fit the activities shown in grouped activity cards in the Control Center.

For more information on how images are used in the UI, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.") and [Images](activity-attributes.html#psn-activities-guide_8_1__psn-activities-guide_8_1_6).

## Managing Activity State

Ensure your activities accurately represent the intended game state by sending the following events at the right time:

* `activityStart` - Send this event for the activity immediately when a player starts playing the mode. This event moves the activity to the *In Progress* state so other players can view it on the player’s profile. It also removes the spoiler block treatment if the activity does not have *Available by Default* set to true.
* `activityEnd (outcome: completed)` - Send this event for the activity when the player is no longer playing the mode. This event moves the activity to the *Completed* section so other players can no longer view it on the player’s profile.
* `activityAvailabilityChange` - If you did not set *Available by Default* to true for the activity, send this event immediately when the mode becomes playable. This removes the spoiler block treatment from the activity UI. This event is optional, as the spoiler block treatment is automatically removed when the first `activityStart` event is sent.

For more information on all UDS state management calls and when to use them, see [Managing the State of Activities, Tasks, and Sub-tasks](managing-state-of-activities.html "This chapter provides information on how to manage the state of activities, tasks, and sub-tasks.").

# Configuring Activities for Franchise Modes or Seasons for Sports and Racing Games

This topic provides guidance on creating activities for sports and racing games with franchise and season modes.

Sports and racing games sometimes feature modes that allows players to compete in a season of events to win a championship. Players can replay these modes repeatedly as the game continues on to the next season upon completion.

For game modes designed this way, [follow the general guidance for creating activities for endless or repeatable modes](configuring-repeatable-or-endless-modes.html "This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.").

If your season mode qualifies as a campaign or story, consider using a progress activity. For example, you can design a progress activity that represents one entire season, then create tasks for the activity that represent each event (race, game, or match) that players must complete. For more information, see [Configuring Activities for Required and Optional Missions, Chapters, and Levels](required-and-optional.html "This topic provides guidance on creating activities for games that feature required and/or optional missions, levels, and chapters.").

# Configuring Activities for Local Multiplayer

This topic provides guidance for games that feature modes with local multiplayer.

Some games feature competitive multiplayer that players can play locally vs another player or the computer.

To create activities for games with these types of modes:

1. [Follow the general guidance for creating activities for endless or repeatable modes](configuring-repeatable-or-endless-modes.html "This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.").
2. Configure the activities as single player activities by leaving the *Number of Players* and *Total Number of Players* fields empty.

Multiplayer activities are updated using the Matches Web API, which is primarily used for reporting match details in competitive modes. As local multiplayer activities don't need to capture match results, the Matches Web API is not necessary.

If you need to configure activities for online multiplayer modes, see [Configuring Activities for PVP Online Multiplayer Modes](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.").

If your mode is available both online and locally, configure two activities. One to cover local multiplayer as an open ended activity, and one to cover online multiplayer. While the guidance for the local multiplayer mode is optional, [guidance for the online mode may be required](trc-requirements-r5302.html "This topic provides information on the TRC requirements you must follow if your game has competitive multiplayer modes.").

# Configuring Activities for Solo Modes or Missions Where Players are Ranked by Time or Score

This topic provides guidance on creating activities for games that feature solo player modes that are ranked by a time or score.

Some games feature modes that players can play repeatedly where they are ranked by a time or score. For example:

* A mode in a puzzle game where the player must clear the board as fast as possible or achieve the highest score possible within a set time or before reaching a fail state
* Challenge missions with a scoring system
* Mission replays or speedrun modes with a scoring system
* Boss rush modes

Configure challenge activities for these types of game modes. Challenge activities create asynchronous multiplayer experiences, encouraging competition and re-engagement with functionality such as:

* Leaderboards viewable within the PlayStation®5 system software
* Notifications that are sent when a friend gets a better score
* Invite flows to attract new players or re-engage lapsed players

For more information on challenge activities, see "PlayStation™Network Challenge Activity Guide".

If you do not need the functionality of challenge activities, [follow the general guidance for creating activities for endless or repeatable modes](configuring-repeatable-or-endless-modes.html "This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.").

# Configuring Activities for Training, Simulation, Sandbox, Build/Creator, Arcade, Co-op PVE, and other Endless Modes

This topic provides guidance on creating activities for training, sandbox, creation, and other endless game modes.

Some games feature modes that players can play endlessly without a predefined ending. For example:

* Simulation and sandbox style games without a defined goal or mission structure. If your game features a goal or ending that qualifies as a campaign or story, [consider using a progress activity](configuring-campaign-or-story-modes.html "This chapter provides details on how to configure activities for games that feature campaign and story modes.").
* Creation and build modes where players can spend as much time as they want
* PVE modes where players cooperate to accomplish goals in a multiplayer setting against non-player character opponents
* Training modes where players can practice mechanics as long as they want

For game modes designed this way, [follow the general guidance for creating activities for endless or repeatable modes](configuring-repeatable-or-endless-modes.html "This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.").