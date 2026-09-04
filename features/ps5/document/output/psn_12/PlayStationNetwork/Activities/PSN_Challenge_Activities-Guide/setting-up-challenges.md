# PlayStation™Network Challenge Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Challenge_Activities-Guide/setting-up-challenges.html

# Configuring Challenge Activities

This chapter provides information on how to configure challenge activities.

The figure below illustrates the process game developers must take in order to integrate their game with activity challenges. For the general development process of UDS, see [Universal Data System Guide - Development Process Overview](../Universal_Data_System-Guide/development-process-overview.html).

The Application Development Process for Challenges

## Request Services

Because challenges internally use the platform Leaderboards Service, developers must make sure to request the Leaderboards Service along with the UDS Service for their title ID.

## Define PlayStation™Network Object for Challenges

Challenges are a category of the activity object. They do not support tasks.

Using the UDS Management Tool, follow the standard way of creating a new activity object, and choose challenge as your category.

Under **Create New Challenge Activity**, the properties listed in the table below should be set in the **Properties** tab.

Properties Tab Values

| Field | Description |
| --- | --- |
| Object Id | Object ID of the challenge. The partner can self-define object ID. The object ID is a string of 1 to 32 characters comprising alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| Subcategory (optional) | An additional description line to the challenge that appears on activity cards, under the display name. Although this property is optional, it's advised to include it for user clarity. |
| Display Order | This number is auto-assigned. |
| Display Name | The name of the challenge. This field can be localized. |
| Description (optional) | The description of the challenge. This field can be localized. |
| Activity Large Image | Full screen image used. The image has the following properties:   * Dimension: 3840x2160 px * Image Format: PNG * 24-bit non-Interlaced |
| Activity Card Image | Image used on action cards representing the game or challenge and in notifications triggered for a challenge. The image has the following properties:   * Dimension: 864x1040 px * Image Format: PNG * 24 bit non-Interlaced |
| Available By Default | You can use *Available By Default* to display your activities without spoiler block treatment. Only use this on activities that the player has access to immediately when starting the game. Scores can be recorded regardless of the state of spoiler block treatment. |
| Available From/To (optional) | Set a date range for *Available From/Until* to control which Challenges players can see. Challenges that fall within the date range that you specify are visible to players. Challenges that fall outside of the date range that you specify will not accept scores from players. |
| Personal Best Notification Only (optional) | Defaults to false. When set to true, only personal best notifications are sent to the player. This reports their challenge completion only when the player beats their best score recorded by the server. If false, players receive two types of notifications: personal best notifications when they beat their best score, and challenge completed notifications, when they don't. |
| Global Leaderboard Cohort (optional) | Defaults to true. Global cohorts are enabled by default. In some situations, The game developer might want to show global leaderboards only within their game. By setting this flag to false, only friend's cohorts are enabled in challenge action cards and global leaderboards are selectable. Also, all global rank reporting is suppressed from the UI. |
| Leaderboard Board ID | The leaderboard ID is auto-assigned by the system. Each challenge has a unique leaderboard ID which you can use to access the Leaderboards Tool, leaderboard APIs, and manage the leaderboard associated with the challenge. |

In the **Statistics** tab, you must provide the fields listed in the following table:

Statistics Tab Fields

| Field | Description |
| --- | --- |
| Score Name | This is a localized string used to describe the challenge score, for example, kills, laps, or miles, which is shown on leaderboards. If the score name is for numeric scores, this also appears in notifications. |
| Display Format | The format of the score. Select from the following:   * **Time**: defines the value sent in milliseconds and interpreted as a time-based score. * **Numeric**: defines the value sent as a discrete integer which is interpreted as a generic score. |
| Sort | Defines the sort order on the leaderboard.   * **Descending**: higher values appear first in the leaderboard. * **Ascending**: lower values appear first in the leaderboard. |
| Decimal Places | This is only valid when the display format is set to numeric. Possible values are 0-3. Denoting the number of digits in the score sent after which a decimal point is placed. Zero means the score is interpreted as an integer. |

The **Rewards** and **Localization** tabs are set up consistently with other activities.

Note: Current requirements dictate that for all the languages supported by a title, the non-optional property strings must have all the localizations supplied prior to deployment. For example, when creating a challenge, the display name must be supplied in all of the languages that your title supports. Although the tool allows you to test without providing all of the localized strings in the staging environment, if these strings are not supplied prior to deployment to production, some undesired behavior occurs and a placeholder string appears (for example, `%challengeName%`) in notifications and elsewhere until the corresponding string is provided via the tool. This same behavior happens when testing your title on the staging environment.

## Defining UDS Events for Challenge Activities

You can create many event types for your challenge activity object. The following event types have particular relevance to challenges and may impact the user experience in a unique way:

* An event of type `activityStart`: Send the challenge object ID in the `activityId` property for the event. Note that every time the Challenges Service receives an `activityStart` event, it increments the number of attempts the user has played the challenge activity (which is displayed in the challenge card).
* An event of type `activityEnd`: Send the challenge object ID in the `activityId` property for the event. In addition, the following properties are optional:

  + `score`: Used in the leaderboard to determine the rank. The score sent should be consistent with the score statistic defined for the challenge. If a score property is not sent, the challenge outcome is considered failed. If the score is sent with no outcome value specified, the challenge outcome is automatically considered "completed". Note that the challenge completion notification is only sent when the outcome is completed.
  + `outcome`: This property affects the result of an activity run. Values of `outcome` when specified can be completed, failed, or abandoned.

    An outcome of "completed" indicates that the score should be recorded on the leaderboard, as well as triggering notifications. Any other outcome results in the score being ignored for that run.

    An outcome of "failed" or "abandoned" indicates that the score should not be recorded on the leaderboard, but this status is shown in the UI on the activity card for that run instance (see example section for details).
  + All other `activityEnd` event properties (for example, `mapPosition` and `difficultySetting`) are ignored in the context of challenges.
* An event of type `activityAvailabilityChange`: Set up consistently with other activities at the system level. Used in challenges to control the unlocking of challenges by the game. Unavailable challenges are not recommended in the UI.
* An event of type `activityTerminate`: Games use `activityTerminate` in some circumstances to indicate to the server the Challenge is no longer in-progress.
* An event of type `activityResume`: Should be sent by the game when resuming a challenge run. If an in-progress challenge run exists, the attempt count is not incremented. Otherwise, this event is treated similarly to an `activityStart`, and a new run is started.

## Download and Place the Configuration File

Download the configuration file from GEMS and place the configuration file in the root directory. For details, see [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html).

## Implement

Challenges use the UDS SDK reference document & sample. Use the sample programs provided by the UDS SDK as well as relevant documentation to send `activityStart` and `activityEnd` events with the proper parameter to the UDS server.

For more information, see [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html).

## Debugging and Testing

For testing challenges, once an `activityEnd` event is received by the server, a challenge completed notification confirming the score should appear.

In addition, use the [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) as a reference for the web-based tool that enables the viewing of data sent from a game application during developing, debugging, and testing, as well as the viewing of data processed from the sent data.

# Challenge Activity Settings

This topic describes different system settings which affect challenges, and how they can impact the user experience.

## Challenges and User Privacy

Privacy settings affect notifications as well as the visibility of usernames in leaderboards. This is set by who can see your games and your gaming history under **Users and Accounts** > **Privacy** > **View and Customize Your Privacy Setting** > **Your Activity**.

If a player chooses to modify this setting, they are treated as anonymous to players outside of their chosen group (for example, friends or friends of friends) and therefore score beaten notifications are sent to only those who are included in the chosen group. In addition, the player appears as anonymous on the global leaderboard. In the friends leaderboard, the player does not appear if the user has chosen "no one" in the privacy setting.

Similarly, if the player chooses to appear offline, score beaten notifications are suppressed; however, the player's score is still registered to the leaderboard.

## Automatic Capture of Personal Best Challenge Videos

The automatic capture of challenges can be controlled using **Settings** > **Capture and Broadcasts** > **Auto Captures** > **Challenges**.

This setting is turned on by default.

# Opening Challenge Activity Cards

This topic provides information on how to open challenge activities from within a game.

Using System Services SDK functions, you can open challenge activity cards from within the game. The SDK function supports several parameters to enable opening the card in several modes, including showing the expanded friends or global leaderboard cohort.

See [SystemService Library Overview](../SystemService-Overview/__document_toc.html) for details on exact usage.

# Capturing and Sharing Personal Best Videos

This topic provides information on how PlayStation™Network captures and shares videos when users record new personal records in challenge activities.

When a player sets a new personal best in any challenge, a video of the run is automatically captured for players to review or share later. The video can be viewed directly in the challenge activity card or in the Media Gallery. Players can share the captured videos to parties or to social networks linked to the player's account. Personal best videos in the Media Gallery are adorned with a challenge crown icon. Players can edit the videos prior to sharing.

Challenge Activity Card
Media Gallery

By default, personal best captures have an additional buffer of 4 seconds added before `activityStart` and after `activityEnd` to ensure that the start and end of the challenge is shown. If the default value does not work for your title, file a support ticket, and the values for your title can be adjusted accordingly.

Videos are only captured if:

* The duration of the video is longer than 3 seconds
* The full video is still available in the Previous Gameplay Buffer (up to the last 60 minutes). This may occur when the challenge duration is longer than 60 minutes or if the player has paused the game for an extended period of time prior to finishing an ongoing challenge.

This functionality is enabled by default, but players can disable it using the auto-capture settings available in the **Captures and Broadcasts**.