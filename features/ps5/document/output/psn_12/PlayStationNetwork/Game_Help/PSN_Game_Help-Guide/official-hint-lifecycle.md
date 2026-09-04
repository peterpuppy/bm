# PlayStation™Network Game Help Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Help-Guide/official-hint-lifecycle.html

# Configuring Official Hints

This chapter provides information on what official hints are and how to configure them.

Official hints are created by you and allow you to curate the game help experience directly. You can create official hints for activities and for trophies.

Official hints allow you to customize all the content that the player sees when requesting help. This includes adding helpful text for the player and displaying a video or image of your choosing.

You can use the Game Help Tool to create official hints, make official hints available for previewing on DevKits, and publish official hints to the production environment.

You can enable Game Help Tool access for users who do not have access to DevNet. To do this, add the user as a Content Creator, as described in [PlayStation™Network Service Setup Guide - Registering Titles - Adding Content Creator Collaborator](../PSN_Service_Setup-Guide/adding-content-creator-collaborator.html).

# Configuring Custom Game Help

This chapter provides information on how to design and optimize custom Game help content.

For games that want to control the entire Game Help content experience, we offer the ability to publish custom Game Help.

Custom hints are configured in the Game Help tool (see The Game Help Tool). To learn more about configuring official hints, see the High-Level Workflow for Creating Official Hints section.

Please note the following for Official Game Help

* Publishing custom Game Help will completely override Community Game Help. There cannot be custom Game Help for some Activities and Community Help for others.
* As such, there is a new Game Help policy in effect that requires a level of coverage equal to what Community Game Help would provide. For information on the new Game Help policy, see [Policies and Business Model Guidelines](https://learn.playstation.net/bundle/policies-and-business-model-guidelines/page/Game_Help.html).

Official Hint Template

## Configuring UDS Metadata for Game Help

Game Help depends on UDS metadata to describe objects and events. UDS metadata includes PlayStation™Network objects, such as activities and trophies, and UDS events, such as `activityStart` and `activityEnd` events. For more information on configuring UDS metadata, refer to the following:

* [Universal Data System Guide - Using the UDS Management Tool - Configuring the UDS Data Model](../Universal_Data_System-Guide/configuring-the-uds-data-model.html)
* [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html)
* [Universal Data System Guide - Using the UDS Management Tool - Bulk Configuring UDS Entities](../Universal_Data_System-Guide/bulk-configuring-uds-entities.html)

**PlayStation™Network Objects**

Game Help requires UDS metadata for activity and trophy objects to be configured using the UDS Management Tool. See [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) for information on configuring this metadata.

**Activity**

Note:

Activities are required for activity hints.

An activity is a unit of gameplay that is part of the game's defined structure. An activity can contain tasks, and tasks can contain sub-tasks. The beginning and end of an activity are defined by events. See [Configuring Custom Game Help](official-hints-developer-provided-help.html "This chapter provides information on how to design and optimize custom Game help content.")) for more information. To support activity hints, Game Help needs all in-game objectives and tasks to be configured as activities. Game Help provides help for the following types of activity:

* **Progress-based.** This kind of activity requires the completion of one or multiple tasks to advance a game.

  + In open world games, examples of progress-based activities are quests, missions, and raids.
  + In linear games, examples of progress-based activities are chapters and levels
* **Open-ended.** This kind of activity describes in-game spaces where players can build and explore.

  + In open world games, examples of open-ended activities are cities, planets, realms, neighborhoods.
  + Linear games cannot contain open-ended activities.
  + In sandbox games, the entire game mode is an open-ended activity.
  + In sports games: free-play style modes are open-ended activities.

See [Configuring Activities Based on Your Game's Design](configuring-activities-based-on-game-design.html "This topic provides links to other topics that explain how to optimize activities for Game Help content by configuring them based on the design of your game.") for more information on how to design activities to provide the best help experience for players.

**Trophy**

Note:

Trophies are required for trophy hints

A player can unlock trophies by completing specified objectives in a game, such as defeating a certain monster, winning a particular race, or meeting a character in a specific situation. Each trophy is linked with one or more UDS Stats. When a linked UDS Stat is updated, the trophy system evaluates the new value against the trophy unlocking condition to determine whether or not the player has unlocked the trophy.

Each trophy can have up to three official hints. Players can see hints in Game Help for trophies that they have not yet unlocked.

You can configure trophies in the UDS Management Tool. Trophy configuration is available on the UDS Management Tool Features Menu.

Accessing the Trophy Tool

See the [Trophy System Overview](../Trophy_System-Overview/__document_toc.html) for more information on the trophy system and how to configure trophies and their unlocking conditions.

**UDS Events**

Game Help requires some UDS events to be configured and instrumented in the game. The types of events required depend on the types of hints you want to support, as follows:

* ****Activity hints**** require `activityStart` events in most cases. Optionally, they may also use `activityEnd` events.
* ****Trophy hints**** do not directly require any specific types of UDS events. However, trophies rely on UDS event processing to determine whether the trophy is locked or unlocked. Players can only access trophy hints for trophies that are locked.

See [Universal Data System Guide - UDS Data Model - UDS Events](../Universal_Data_System-Guide/uds-events.html) for more information on events and event types.

See [Universal Data System Guide - Using the UDS Management Tool - Configuring the UDS Data Model](../Universal_Data_System-Guide/configuring-the-uds-data-model.html) for information on configuring events.

**activityStart Events**

Instrument the game so that when a player starts an activity, the game sends an `activityStart` event. Game Help uses `activityStart` events to provide help videos that help a player to progress through an activity.

Some activities do not need an `activityStart` event. For example, if you are creating an open world game that contains a 'collect an item' activity, you do not need an `activityStart` event for that activity.

**activityEnd Events**

Instrument the game so that when a player leaves an activity, the game sends an `activityEnd` event. If you wish to use the Capture Gallery video capture method, `activityEnd` events can help automatically tag captured videos so that the relevant video segment can be associated with a hint for that activity.

# High-Level Workflow for Creating Official Hints

This topic describes the high-level process and requirements for creating official hints.

1. **Request PlayStation™Network Services**

   Request the UDS service in PlayStation®5 DevNet.
2. **Define PlayStation™Network Objects, UDS Events, and UDS Stats**

   Game help can be configured for Activity and Trophy PlayStation™Network Objects. Define the relevant objects, configure their properties, and set up UDS Events and Stats in the UDS Management Tool. (See [Configuring Custom Game Help](official-hints-developer-provided-help.html "This chapter provides information on how to design and optimize custom Game help content.")).
3. **Instrumentation**

   Add instrumentation in your game to send in-game UDS events for activities and trophies.

   To support activity hints, your instrumentation must include events that define the start of activities. To support trophy hints, your instrumentation must define the unlock requirements for your trophies.
4. **Upload hint media to the Media Asset Library**

   Media (videos or images) can be associated with hints either during hint creation or by configuring hints that have already been created. To associate media with hints, you must upload the media to the Media Asset Library in the Game Help Tool. Game help supports two upload methods for media.

   * **Uploading media from PC**

     You can use either the Game Help Tool or User Bucket for Partners to upload videos and images to the Media Asset Library from a PC.
   * **Uploading videos from console (activity hints only)**

     Video for activity hints can be captured and uploaded from a DevKit using the Capture Gallery. Videos are automatically tagged with the relevant UDS activity and event metadata for easier association with relevant hints.
5. **Configure Official Hints**

   Configure official hints using either the Game Help Tool or User Bucket for Partners (UBP; see [Universal Data System Guide - Using the UDS Management Tool - Bulk Configuring UDS Entities](../Universal_Data_System-Guide/bulk-configuring-uds-entities.html) for details). The Game Help Tool supports the creation, configuration, and management of hints, both individually and in bulk (see [About the Game Help Tool](the-game-help-tool.html "This chapter provides details on the Game Help tool.")). UBP supports bulk configuration only. For information on bulk configuration of hints, either using the Game Help tool or UBP, see [Configuring Bulk Hints](bulk-configuration-of-hints.html "This chapter provides information on configuring hints in bulk.")).

   Whichever tool is used, official hints have the following attributes:

   * The PlayStation™Network Object (activity or trophy) associated with the hint.
   * A hint name.
   * (Optional) A hint description.
   * (Optional) Image or video media from the **Media Asset Library** (uploaded as described in [Viewing Media Assets](the-media-asset-library.html "This topic provides information on how to view media assets you can use with Game Help content.")). There are two ways to add media to a hint:

     + **Adding media to a hint using the Game Help Tool (activity hints only)**

       In the Game Help Tool, click the Add Media File button on the **Properties & Media** tab of the Create New Hint form. Select media from the available assets in the **Add Media Asset Dialog**.

       For more information on creating a new hint and the **Properties & Media** tab, see [Creating Activity Hints](creating-activity-hints.html "This topic covers the process for creating official hints.").

       Add Media Asset Dialog
     + **Adding media to a hint using bulk configuration**

       Specify the associated media details in the bulk configuration metadata JSON. (See [Configuring Bulk Hints](bulk-configuration-of-hints.html "This chapter provides information on configuring hints in bulk.").)
6. **(Optional) Localize Official Hints**

   Localized hint names, descriptions, and media can be defined for official hints either in the Game Help Tool or through bulk configuration. The title configuration defines the supported languages. You are encouraged to provide localization for hints, but it is not required.
7. **Validate Hints and Media**

   You can use the the Game Help Tool to validate configured hints and uploaded media. To preview the metadata and associated media for an activity hint in the Game Help Tool, select the "Preview Hints" option from the hint's submenu.

   You can also separately validate your uploaded media in the Media Asset Library. For activity-related videos, the Media Asset Library allows you to view debug information to validate console-uploaded videos against in-game events. See [Viewing Media Assets](the-media-asset-library.html "This topic provides information on how to view media assets you can use with Game Help content.") for more information.

   You can use DevKits to validate the on-console behavior of both activity and trophy hints in the development environment before publishing them to the production environment. Note that the DevKit must be running System Software version 4.00 or later to validate trophy hints, and at this time, trophy hints cannot be accessed via the Control Center. See [Previewing Official Hints on DevKits](previewing-official-hints-on-dev-kits.html "This topic provides details on how to preview official hints on DevKits during development.") for more information.
8. **Publish Hints to Production**

   When you are satisfied with the configuration of your help content, use the Game Help Tool to publish your hints to the production environment (see [Publishing Official Hints to Production](publishing-official-hints-to-production.html "This topic provides details on publishing official hints to production environments, including how to edit and delete them after they've been published.")).

## Types of Hint Content

All official hints have a **Hint Name**, which the player sees as a title or headline for the hint. You must configure a hint name for each hint.

As well as the hint name, hints can optionally contain additional text content and a single video or image:

* **Hint Text** is displayed under the Hint Name. Hint text is optional.
* The **Media Asset** may be either a still image or a video. Each hint can display one media asset. The media asset is optional, but strongly recommended.

## Official Hints on Activities

* When creating official hints for activities, you can only add hints to leaf activities (see [How Game Help is Associated with Activities](how-game-help-is-associated-with-activitie.html)).
* A maximum of three hints can be added to each leaf activity.
* Hints can be added to activities before or after a game has been published, without needing to update the game package or activity configuration.

## Official Hints on Trophies

* When adding official hints to trophies, hints can be only added to PlayStation®5 trophies (PlayStation®4 Trophies are not supported at this time).
* A maximum of three hints can be added to each trophy.
* Hints can be added to hidden trophies. The hints are only visible after the player has revealed the trophy.
* Hints can be added to trophies before or after a game has been published, without needing to update the game package or trophy configuration.

# Creating Activity Hints

This topic covers the process for creating official hints.

The Game Help Tool allows you to create official hints for any leaf activity. This section describes how to use the Game Help Tool to create activity hints one at a time. If you want to create activity hints in bulk, see [Configuring Bulk Hints](bulk-configuration-of-hints.html "This chapter provides information on configuring hints in bulk.").

Note:

Official hints must comply with the PlayStation®5 Business Policies. You can download the policies from <https://learn.playstation.net/bundle/policies-and-business-model-guidelines/page/Game_Help.html>

To create a new hint, Select **Actions** > **Create New Hint** from any page within the Activity Hints view.

Create Hints from the Activity Hints View

You can also create hints by selecting **Hint & Media Detail** > **Create New Hint** from a leaf activity.

Create Hints from a Leaf Activity

## The Properties and Media Tab

The Properties and Media tab is used to configure the default metadata for an official activity hint. If your game supports multiple languages, the values supplied for the text and media properties in this tab are used for the default supported language. They are also used as default values for other supported languages if a localized value is not specified.

* Associated Activity (Required)

  This field allows you to search for and select the activity that this hint will be associated with. Official hints must be associated with leaf activities, so if the selected activity has any tasks, you must select a task, and if the task has sub-tasks, you must also select a sub-task.
* Hint Name (Required)

  The hint name identifies the hint in the Game Help Tool. The hint name is also shown to players who are viewing official hints on the console.
* Hint Text (Optional)

  The hint text is an optional, freeform text field that allows you to supply more details, instructions, and guidance for players who are viewing your hint on the console.
* Media Asset (Optional)

  An official hint can display one media asset from the Media Asset Library. You cannot use the Properties & Media tab to upload a new image or video, but you can select any previously uploaded and fully-transcoded image or video at this point.

  To add a media asset to the hint, click Add Media File > **Create New Hint**. The Add Media Asset dialog displays two tables containing available media assets:

  + Media Associated With Activity

    This table contains the same media as the "Media Associated with this Activity" section of the official hints tab. All videos here are automatically associated with the selected activity based on gameplay data obtained when uploading the video from a DevKit.
  + All Other Media

    This table contains the rest of the media in the Media Asset Library, including images and videos that have been uploaded directly to the Game Help Tool via the browser.Add Media Asset Dialog

## The Localization Tab

The Localization tab allows you to provide localized hint property values for each language supported by your NP Communication ID. You can supply localized values for the following hint properties:

* Hint Name (Optional)
* Hint Text (Optional)
* Media Asset (Optional)

  Localization Tab

Game Help displays the localized versions of hint properties to the player when they set their console language to a language supported by your NP Communication ID. If a localized property value is not provided for the selected language, the value for the default language, set in the Properties & Media tab, is displayed. For example, if your game's default language is English, you might set a hint name and video in the Properties & Media tab, and a French hint name, but no French video, in the Localization tab. A player who sets their console language to French sees the French hint name, but the default (English) video.

You do not need to fully localize official hints to preview them on a DevKit or publish hints to production, but you are encouraged to do so for a consistent player experience. Any language that does not have localized official hint content is marked by an alert symbol, as shown in the figure above.

# Creating Trophy Hints

This topic provides details on creating trophy hints.

Official hints for trophies can be created, edited, and associated with trophies via the Game Help tool bulk configuration feature. See [Configuring Bulk Hints](bulk-configuration-of-hints.html "This chapter provides information on configuring hints in bulk.") for more information. All official hints can be published to production through the bulk publish functionality in the Game Help tool.

Trophy hints in both the development and production environments can be activated or deactivated in the Hint Detail Panel. Hints in the Active Hints table can be reordered. In the development environment, individual hints in the Inactive Hints table can also be deleted.

Note:

You can currently create, edit, and publish hints for trophies in bulk. GUI support for creating, editing, and publishing hints for trophies individually will be added to the Game Help tool in a future update.

# Uploading Media Assets

This topic provides information on the types of media assets you can upload to use for custom Game Help content.

The Game Help tool allows you to upload and store media assets that can then be used in the Game Help for your game.

You can you can [upload assets from a PC](uploading-media.html#psn-game-help-guide_4_5__psn-game-help-guide_4_5_1) or [upload captured video directly from DevKits](uploading-media.html#psn-game-help-guide_4_5__psn-game-help-guide_4_5_2).

After assets have been uploaded, they are stored in the [Game Help Media Asset Library](the-media-asset-library.html "This topic provides information on how to view media assets you can use with Game Help content.").

## Uploading Files from PC

Game Help allows you to upload media assets from your PC using the Media Asset Library. You can select multiple files to upload at a time. Each file uploads asynchronously and each file is added individually to the media asset library table. If you navigate away from the Media Asset Library page while an upload is in progress, the processing of any file that has not been fully uploaded is aborted. The Upload Status column shows the accurate status for your uploads.

When a file has been uploaded, the tool processes and transcodes it. You can navigate to other pages while processing and transcoding are still in progress. The Upload Status column indicates the transcoding status for files that are still transcoding and allows you to verify when transcoding is complete. Only files that have been successfully transcoded can be used in official hints.

When fully transcoded the video output has the following characteristics:

* Video codec: AVC
* HDR/SDR: SDR
* Audio codec: AAC
* Frame rate: 30 or 60 fps (depending on video uploaded)
* Max resolution: 1080p @ 8 mbps
* Sample rate: Same as source

**Image File Specifications**

Images must conform to the following specifications:

* Format: .png
* Maximum resolution: 4K
* Aspect ratio 16:9
* Maximum size: 4 GB

**Video File Specifications**

Videos must conform to the following specifications:

* Supported video codecs:

  + Recommended: H.264, VP9
  + Other supported formats: H.265 HEVC
* Video resolution and frame rate, expressed as (height x width in pixels) : FPS (frames per second)

  + 2160p X 3840p: 60 FPS
  + 2160p X 3840p: 30 FPS
  + 1080p X 1920p: 60 FPS
  + 1080p X 1920p: 30 FPS
  + 720p X 1280p: 60 FPS
  + 720p X 1280p: 30 FPS
* Audio codecs

  + Recommended: AAC
  + Other supported formats: opus (VP9)
* Container formats

  + mp4
  + webm

## Uploading Videos from DevKits (Activity Hints Only)

The Media Gallery, which is available on DevKits and TestKits, supports the ability to upload videos to Game Help. Unlike media uploaded from a PC, these videos cannot be edited before they are uploaded, and are sourced directly from captured gameplay. However, capturing and uploading video content directly from the DevKit allows Game Help to automatically associate the video content with the related activities. Game Help can process an uploaded video and create segmented video clips for each activity contained within the gameplay.

To get started, instrument your game with appropriate activity events. When your game is sending UDS events, follow these steps to capture and upload gameplay video to Game Help:

1. Play the instrumented activity on a console and use the create button to capture gameplay footage. Click Record Video to start recording gameplay footage on the console.
2. Browse captured videos in the Media Gallery. Select the video you want to use for your official hint.
3. Play the selected video and use the ★View Events menu option to verify that activity details such as Activity Name, Start Time, End Time, and Outcome are correctly mapped to the footage.

   View Events in a Captured Video
   Verify Activity Details in the Captured Video
4. Use **★Add to Game Help** in the Media Gallery to push the selected video from the console to Game Help.

   Upload Video to Game Help

The Media Gallery shows the progress of your video upload and displays a confirmation when the video has uploaded successfully. After successful processing, the video file and its automatically segmented video clips appear in the Media Asset Library in the Game Help Tool.

# Previewing Official Hints on DevKits

This topic provides details on how to preview official hints on DevKits during development.

DevKits allow you to preview official hints that are in the active list in the development environment. You can create an unlimited number of official hints, but each trophy or leaf activity can have a maximum of three active official hints at any one time. The active list is shown in the **Active Hints (Displayed on DevKit)** table on the Development section of the hint details panel (see [Viewing Hint and Media Details](the-hint-media-detail-panel.html "This topic provides information on how to view the details of hints that you've designed.")).

DevKits provide two ways to preview active official hints:

* Preview hints in the player context. The DevKit displays active hints in the Control Center or in the trophies screen, but only for activities and trophies that are currently available to the user. This is similar to the way that hints are displayed to players in the production environment. See [Previewing Official Hints on DevKits](previewing-official-hints-on-dev-kits.html "This topic provides details on how to preview official hints on DevKits during development.").
* Use the activity debug feature to preview active activity hints for all configured activities. This feature allows you to preview all the configured activities, tasks, and sub-tasks for your game, and the associated active activity hints. You can access the activity debug feature in **★Debug Settings**. See [How to Use Activity Debug to View Activity Hints on a DevKit](previewing-official-hints-on-dev-kits.html#psn-game-help-guide_4_6__psn-game-help-guide_4_6_4).

## How to Make Hints Visible on DevKits

Before you can use your DevKit to view and test official hints for trophies and activities, the official hint must be in the active list for the development environment. To add a hint to the active list for the development environment, open the [Viewing Hint and Media Details](the-hint-media-detail-panel.html "This topic provides information on how to view the details of hints that you've designed.") for the trophy or activity and click **Move to Active** in the row of the official hint you want to activate.

If there are already three hints in the active list for your activity or trophy, you need to remove one of the currently active hints before you can add another hint to the active list. To remove an official hint from the active list, select **Move to Inactive** in the corresponding row of the active table.

You can also re-order the official hints in the active list to make sure the player sees the content in the order you prefer.

## How to View Hints on a DevKit in the Player Context

You can use a DevKit to preview hints in the player context by using one of the following methods. When you preview hints in the player context, the DevKit only displays hints that have are active in the development environment and that are associated with activities or trophies that are currently available to the user. For information on active hints, see [Previewing Official Hints on DevKits](previewing-official-hints-on-dev-kits.html "This topic provides details on how to preview official hints on DevKits during development.").

* **Trophy Hints**

  You can use either the Control Center or the trophies screen to view and validate trophy hints on a DevKit.

  + **From the trophies screen:** Open the trophies screen by opening **Trophies** in your profile, then choosing your title. Alternatively you can navigate to your title's Game Hub page and select **Trophies**. Select the relevant trophy from the list and choose **View Hints**.
  + **From the Control Center:** Press the PS button to open the Control Center while your title is running. Select the relevant Trophy Card and choose **View Hints**.
* **Activity Hints**

  To view and validate activity hints using a DevKit, launch your title, use the PS button on your controller to access the control center, then open the activity card.

  Depending on the structure of your leaf activities, you will see one of the following UX flows on DevKit:

  Previewing Hints

  | Number of Available Sub-tasks | UX on Console |
  | --- | --- |
  | 0 | Select **Objective** > **Hints** for the task |
  | 1 | Select **Objective** > **Hints** for the sub-task |
  | More than one | Select **Objective** > **List of available sub-tasks** |

  Task with No Sub-tasks
  Task with One Available Sub-task

## Troubleshooting: Previewing Activity Hints in the Player Context on a DevKit

If you are unable to view activity hints that you have configured for a leaf activity, task, or sub-task, check the following:

1. **Is the activity active?** You can only view hints for active activities. To check if the activity is active, open the Control Center by pressing the PS button. You should be able to find a card for the activity, and the card should display the text "In Progress".

   * If you do not see a card for the activity, you need to start progress for the activity to make hints available.
2. **Is the task that is associated with your hints available?** If the activity contains one or more tasks, you should see the task in the Objectives list when you open the card for the in-progress parent activity.

   * If you do not see the expected task in the Objectives list, you need to make the task available so you can access the associated hints. You may need to start the task or check your UDS events and stats.
3. **Are the sub-task(s) associated with your hints available?**  If the task only has one sub-task, you should see the hint for that sub-task when you select the task from the objectives list. If the task has more than one sub-task, you should see a list of available sub-tasks when the task is selected. Sub-tasks that have hints configured display a hint icon and can be selected to navigate to the associated hint.

   * If you do not see the expected sub-task in the sub-task list, you need to make the sub-task available so you can access associated hints. Ensure you have started the sub-task or check your UDS events and stats.

## How to Use Activity Debug to View Activity Hints on a DevKit

You can use the activity debug feature to view all active activity hints that are configured for your title. The activity debug feature, which is available in **★Debug Settings**, displays all the activities, tasks, and sub-tasks that are configured for your title. After you have opened the activity debug feature for your title, you can validate the metadata and on-console appearance of all the active activity hints that you have configured for your activities, tasks, and sub-tasks.

* For more information about how to access and use the activity debug feature, see [Game Intent System Overview - Debugging Support for Developing Game Intent-Compatible Applications](../Game_Intent_System-Overview/debugging-support-using-the-system-software.html).
* For more information about **★Debug Settings**, see the [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html).

# Publishing Official Hints to Production

This topic provides details on publishing official hints to production environments, including how to edit and delete them after they've been published.

Players can only view and experience your official hints after you have published both the hint and your PlayStation™Network Object configuration to the production environment. The Game Help Tool offers the ability to publish individual activity hints or to bulk publish all official hints to production for your game at once.

You can publish official hints to the production environment at any time. However, Game Help is not available to players on consumer consoles until your PlayStation™Network Object configuration has also been published to the production environment. If you publish hints to the production environment before your PlayStation™Network Object configuration is published, Game Help automatically makes the hints available to players as soon as the PlayStation™Network Object configuration becomes available.

If your PlayStation™Network Object configuration is already available when you publish an official hint to the production environment, the hint is immediately made available to players, as described in the publishing confirmation process shown in [Publishing Official Hints to Production](publishing-official-hints-to-production.html "This topic provides details on publishing official hints to production environments, including how to edit and delete them after they've been published.").

Note:

When publishing hints to production for the first time, there is a delay of approximately 1-2 minutes before hints appear on consoles in the production environment. This occurs after clicking **Publish** in the Game Help Tool when you are publishing hints individually, or after you receive the bulk publishing email report when you are publishing hints in bulk.

## Publishing Individual Hints from the Tool UI

Individual activity hints can be published to production from the Hint & Media Detail Panel of Activity Hints view in the Game Help Tool.

Note:

Publishing individual trophy hints from the Hint Detail Panel in the Game Help Tool will be enabled in a future update.

If you create a new hint or update an existing hint, the respective option to 'Publish to Production' or 'Sync Changes to Production' will be enabled in the hint row of the Active Hints or Inactive Hints table. Selecting this option will publish the individual hint to production, subject to the following limitations:

* Up to three active official hints can be published to production for a given activity or trophy. If there are already three active hints for the activity or trophy in production, the 'Publish to Production' or 'Sync Changes to Production' option will be disabled for any new or updated hints in development. You must move at least one active hint in production to the inactive table to enable publishing any additional hint to production.
* If you publish an **inactive** hint to the production environment, it is automatically made active when the publish succeeds. This does not happen if you choose to 'Sync Changes to Production' for an inactive hint.

  Publishing an Individual Official Hint to the Production Environment

## Bulk Publishing to Production

When you are ready to release your game, you may need to publish a large number of official hints to production. Publishing each hint individually across all your trophies and activities can be time consuming, so the Game Help Tool provides a way to publish all your official hints from development to production at the same time.

Note:

Bulk publishing replaces all of the hints currently in production with a snapshot of all the official hints in the development environment. This action copies the active or inactive state of each hint, so inactive hints that are published to production using this method are not automatically set to active.

Actions Menu - Publish Hints
Bulk Publishing Hints - Confirmation

When you select Publish Hints, Game Help begins a background process to publish every active official hint for all your game's trophies or activities. At the end of the process, Game Help sends an email to the user who initiated the publishing process. The email contains a report of the hints published, along with any errors or warnings that occurred. At this point, any official hint that could not be published must be corrected, and then publishing re-attempted.

## Editing Hints After Publishing to Production

You cannot make edits to official hints in the production environment. Instead, you must edit the hint in the development environment first, then click Sync Changes to Production to synchronize the changes to the production environment. This overwrites the previously published version.

If the hint is currently in the Active Hints table of the development environment, you must first move the hint to inactive to enable editing.

Sync Changes to Production

## Deleting Hints After Publishing to Production

You can take down an active official hint that has been published to production by moving it to the inactive table. This immediately removes it from the players' consumer console experience so that they can no longer view the official hint.

You can also permanently delete inactive official hints in the development environment. Bulk publishing then also deletes the hint from the production environment. Note that this cannot be undone. Because this is an irreversible action, it may be preferable to leave unused official hints in the inactive state instead of deleting them.