# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/activity-attributes.html

# Activity Metadata

This chapter provides information on the metadata of activities, such as attributes and rewards.

# Activity Attributes

This topic provides information on activity attributes, such as object ID, display name, and image.

## Object ID

*Object ID* is an identifier that you use to update activities, tasks, and sub-tasks when sending events. Players cannot see this value.

You can use the same name as the user-facing field *Display Name*. For example, if you created an activity for the first chapter of your game, you may give it a user facing *Display Name* of “Chapter 1”. You can also use "Chapter 1" for the *Object ID*. When sending UDS events, specify the *Object ID* rather than the *Display Name*.

## Subcategory

*Subcategory* informs players of the type of content the activity represents. If included, the subcategory appears as a prefix before the activity name. For example, “Subcategory” | “Activity Name”. This can help players find activities for content they are interested in viewing.

If possible, use generic terms to categorize the types of content in your game. The following are examples of generic terms you might use for common content types:

* **Campaign**, **Story**, or **Main Quest** - Use for any mission, chapter, or level that’s required to complete the game.
* **Side Mission** or **Side Quest** - Use for any mission, chapter, or level that is optional and not required to complete the game.
* **Collectible** - Use for any activity that represents hidden collectibles in your game. The activity name should convey the type of collectible or region/level players can find them in.
* **Multiplayer** - Use for any online multiplayer activity.

Subcategories on an Activity Card

## Display Name

*Display Name* is the name players see throughout the UI for activities, tasks, and sub-tasks.

This field supports up to 128 characters; however, SIE recommends keeping the names as short as possible so players can quickly understand what the activity represents.

If your game supports multiple languages, upload localized text for each supported language. If you don't upload localized languages, the default language is displayed. You don't need to include this name in the game package, and you can update it after publishing without a game patch.

Display Name on an Activity Card

## Description

A description of the activity that players can view within an activity card.

When playing a game, players may want to read descriptions to get a better understanding of what they need to do in order to complete the Activity. When players are returning to a game after a break, they may also refer to the description to get a reminder of what they were last doing.

When writing descriptions, give an outline of what the player will be doing while playing the activity. For example, if the activity represents a story mission, the description may detail the purpose, goal, or objectives. If the activity represents a competitive multiplayer mode, the description may outline the win conditions for the mode.

Localize the description for all supported languages. If you don't upload localized languages, the default language is displayed.

Activity Description on an Activity Card

## Default Playtime Estimate

*Default Playtime Estimate* shows players the expected minutes it may take to complete the activity.

Enter values in multiples of 5. For example, 5, 10, 15, etc. Values over 120 display as “more than 2 hours”.

A default value appears on the activity, but you can update it with a more accurate value based on actual player data from the `activityStart` and `activityEnd` events you send once enough players have completed the activity.

Playtime Estimation

## Images

An activity's image gives players a fast way to get more information about the current status of the game. SIE recommends using unique images that represent the game mode for each activity so players can quickly differentiate between activity types.

For example, an activity representing a mission may include imagery related to a character or the environment featured in that mission. An activity representing a collectible may display a picture of the collectible type.

Wherever possible, SIE recommends using images without text to avoid localization concerns.

Images can be custom or in-game screenshots.

You do not need to include images in the game package and you can update them after publishing without a patch.

Upload the following image types for each activity:

* **Activity Card Image** - 24-bit non-interlaced PNG only, 864 x 1040 pixels. Appears on the face of the activity card anywhere the activity is shown. This includes within the Control Center action card strand, on the Game Hub Activity Card strand, and on the player’s profile while the activity is in progress. If you don't include an image, the activity card appears with a gray background. For more information about how and where these appear, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.").
  Activity Card Image
* **Mini Activity Card Image** - 24-bit non-interlaced PNG only, 944 x 332 pixel. Appears when the activity is shown in its smallest form within the Grouped Activity Cards found in the Control Center or on a players mini profile when the activity is in progress. If you don't include an image, a cropped version of the *Activity Card Image* displays. For more information about how and where these appear, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.").
  Mini Activity Card Image
* **Activity Large Image (Game Hub Cover Asset)** - 24-bit non-interlaced PNG only, 3840 x 2160 pixels (4K image). Appears as a player’s most recent *In Progress* activity on the Game Hub. This image replaces the default game image shown on the Game Hub. If you don't include an image, the default game image displays. For more information about how and where these appear, see [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.").
  Activity Large Image

## Available by Default

You can use *Available By Default* to display your activities without spoiler block treatment. Only use this on activities that the player has access to immediately when starting the game.

The following are examples of common activities that you might use *Available by Default* for:

* The activity representing the first mission or chapter of a campaign or story mode.
* Any game modes that are always available to players, including local or online multiplayer modes.

## Is Collectible for Game Help

Enable *Is Collectible for Game Help* to have PlayStation™Network generate Community Game Help videos for activities, tasks, and sub-tasks that represent collectibles.

Community Game Help videos start 30 seconds before your game sends the `activityEnd (outcome: completed)` event for the activity, task, or sub-task.

Do not enable this for activities, tasks, or sub-tasks that do not represent collectibles.

## Is Required for Completion

Enable *Is Required for Completion* on activities and tasks that players must complete to complete the main story or campaign.

PlayStation™Network displays and updates game progress percentages on the Game Hub as players complete these activities and tasks. Do not enable this option for side or optional content.

You can't enable this option for sub-tasks.

Additionally, refer to the following best practices when enabling this option on activities or tasks:

* Send `activityEnd (outcome: completed)` events for activities as the player completes them, otherwise, game completion percentages don't update
* Do not enable this option for activities that are not in use.
* You can enable this option for activities related to down-loadable content (DLC); however, players without the DLC can't achieve 100% game completion.
* Game progress represents how far players have ever reached in a game and is not affected by starting a new playthrough.
* If your main campaign or story contains branching paths, ensure that players can complete all required activities and tasks in a single playthrough, unless game completion requires multiple playthroughs.

## Has Online Multiplayer

Enable *Has Online Multiplayer* for any online competitive multiplayer activity where a match contains another non-local player.

Don't enable this option for games that allow players to complete the campaign cooperatively with others online. Instead, follow the guidance in [Configuring Activities for Cooperative Multiplayer Campaigns](cooperative-campaigns.html "This topic provides guidance on configuring activities for games with cooperative multiplayer campaigns.").

## Support Non-PSN Players

Enable *Support Non-PSN Players* to create cross-platform sessions when players start the activity. Always enable this option if your game supports cross-platform play.

## Supported Platforms

This option informs players what platforms the activity is available for.

Select `PS5` if your game doesn’t support cross-gen play between `PS5` and `PS4`. Select `PS5 and PS4` if your game supports cross-gen play.

This value displays on the Activity Card.

## Number of Players

*Number of Players*represents the number of players that can play the activity together in a game group for modes that support game invites.

For example, your game might include a competitive mode where 16 total players are split into four teams of four players. In this case, set *Number of Players* to **4**.

## Number of Total Players

*Number of Total Players* represents the total number of players that play in a match.

For example, an activity that represents a mode that supports 6v6, this value is 12.

This value displays on the Activity Card.

## Available From/Until

Set a date range for *Available From/Until* to control which activities players can see. Activities that fall within the date range that you specify are visible to players.

See [Managing the Visibility of Activities, Tasks, and Sub-tasks](displaying-activities.html "This chapter provides information on how to manage the visibility of activities, tasks, and sub-tasks in the PlayStation®5 UI.") for examples of when to use this field.

# Activity Statistics

This topic provides information on activity statistics and how they are displayed.

Statistics only apply to competitive activities.

Use the available statistics fields to display scores for competitive activities, informing players of the current status of the match and final results.

Competitive Activity Card

## Score Name

The *Score Name* is the in-game name of the numerical value that determines who wins or loses a competitive match. For example, points, kills, time, or a value unique to your game.

## Display Format

Use *Display Format* to determine how your scores are displayed.

You can display your score in *Time* or *Numeric* format. Time formats display in a HH:MM:SS format, while numeric scores display as numbers.

## Sort

Use *Sort* to sort scores in an ascending or descending pattern.

Use ascending when smaller values indicate better performances, and descending when larger values indicate better performances.

## Decimal Places

*Decimal Places* allows you to determine how many decimal places are displayed to the user for numerical scores. This option is not available for time based scores.

## Additional Statistics

*Additional Statistics* allows you to improve match card navigation by displaying per-player or per-team statistics for the match.

*Stats Name* is the display name shown to players. *Stats Key* updates those statistics using the Matches Web API.

You can also use *Additional Statistics* to control eligibility for tournaments.

Additional Player Statistics

# Activity Rewards

This topic provides information on activity rewards.

## Reward Name

The name of in-game rewards available to players for completing activities.

If your game features rewards that scale depending on the player's status, consider using a more general name such as "Gold" rather than "100 Gold".

## Reward Image

You can provide an icon sized image asset to appear with the reward. Images must be 512 x 512 pixels.

Activity Reward