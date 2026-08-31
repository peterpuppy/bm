# PlayStation™Network Game Help Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Help-Guide/the-trophy-hints-view.html

# About the Game Help Tool

This chapter provides details on the Game Help tool.

The Game Help Tool allows you to create official hints by customizing the help text, video or image that a player sees when they request help for an activity or trophy.

For guidance on how to design and structure official activity hints for Game Help, see [Configuring Official Hints](official-hint-lifecycle.html "This chapter provides information on what official hints are and how to configure them.").

## Supported Browsers

The Game Help Tool is supported on Chrome and Firefox.

## Accessing the Game Help Tool

The Game Help Tool is accessed from the UDS Management Tool. The UDS Management Tool is accessed from a link on the product detail page for the title in DevNet. The following conditions are required to launch the UDS Management Tool from DevNet:

* The UDS service is successfully provisioned with NP Communication ID for the DevNet product.
* You are a title collaborator in DevNet for that DevNet product OR you are a designated Content Creator for that NP Communication ID.

  Note:

  You can enable Game Help Tool access on a per-NP Communication ID basis for users who do not have access to DevNet. To do this, add the user as a Content Creator, as described in [PlayStation™Network Service Setup Guide - Registering Titles - Adding Content Creator Collaborator](../PSN_Service_Setup-Guide/adding-content-creator-collaborator.html).

  Content Creators can use the Game Help Tool to create, edit, view, and publish hints for provisioned NP Communication IDs. However, Content Creators cannot view or edit anything else in the UDS Management Tool.

Please see the [PlayStation™Network Service Setup Guide - Registering Titles - Product Access Privileges](../PSN_Service_Setup-Guide/product-access-privileges.html) for details on how to configure permissions and provision services.

You can launch the Game Help Tool from the UDS Management Tool as shown in the figure below. You can select either **Activity Hints, Trophy Hints** or **Media Asset Library** from the **Game Help** section on the **Features** menu:

UDS Management Tool Features Menu

* The **Activity Hints** view is used to manage and publish official hints for activities. See [Viewing Activity Hints](the-activity-hints-view.html "This topic provides information on how to view activity hints that you've designed for your game.") for more information.
* The **Trophy Hints** view is used to manage and publish official hints for trophies. See [Viewing Trophy Hints](the-trophy-hints-view.html "This topic provides information on how to view trophy hints that you've designed for your game.") for more information.
* The **Media Asset Library** is used to manage and preview media files for Game Help. See [Viewing Media Assets](the-media-asset-library.html "This topic provides information on how to view media assets you can use with Game Help content.") for more information.

# Viewing Activity Hints

This topic provides information on how to view activity hints that you've designed for your game.

Select **Game Help** > **Activity Hints** to view a list of the in-game activities that you've defined.

The Activity Hints View

Each row in the activity tree represents a parent activity or a leaf activity. Game Help is only available for leaf activities. See [How Game Help is Associated with Activities](how-game-help-is-associated-with-activitie.html) for more information.

Clicking a parent activity row toggles the display of its child activity tree.

For each activity in the list, the page displays:

* Object Display Name: The name of the activity, task or sub-task.
* Official Hint Quantity: The total number of official hints created for this activity and all of its children.

Each leaf activity row also has a Create New Hint link.

Clicking a leaf activity row opens the [Viewing Hint and Media Details](the-hint-media-detail-panel.html "This topic provides information on how to view the details of hints that you've designed."). This panel contains an overview of all the Game Help hints available for this activity.

Note:

If a leaf activity becomes a parent activity, for example if sub-tasks are added to a task, then any hints associated with the original leaf activity become inaccessible on the console and in the tool. If the new leaf activities are deleted, and the parent activity becomes a leaf activity again, then the hints that were associated with it become available again.

# Viewing Trophy Hints

This topic provides information on how to view trophy hints that you've designed for your game.

Select **Game Help** > **Trophy Hints** to view a list of the trophies that you've configured.

Accessing the Game Help Tool Trophy Hints View

## The Trophy List

The trophy list displays the following information for each trophy:

* The name of the trophy.
* The total number of official hints created for the trophy in the development environment, both active and inactive.
* The number of active official hints for the trophy in the development environment.
* The number of active official hints that have been published to production for the trophy.

  Trophy Hints View

Click on a row in the trophy list to display more detailed information about the official hints that have been created for that trophy. The details are displayed in the Hint Detail Panel. See [Viewing Hint and Media Details](the-hint-media-detail-panel.html "This topic provides information on how to view the details of hints that you've designed.") for more information.

# Viewing Hint and Media Details

This topic provides information on how to view the details of hints that you've designed.

When you select an activity in the Activity Hints view or a trophy in the Trophy Hints view, the Hint and Media Detail panel opens on the right of the screen. It provides details of the official hints that have been created for the selected activity or trophy.

Note:

For trophy hints, this panel is referred to as the 'Hint Detail Panel' as the 'Media Associated with this Activity' table is only relevant for activity hints.

The Hint & Media Detail Panel contains a tab for each environment and allows you to create, edit, and publish official hints across both environments in their respective tabs.

* **Development**

  Official hints created in the development environment can be viewed on your DevKit for validation before you publish hints to Production.
* **Production**

  Official hints that have been published to production are visible to players when the associated UDS Activities or Trophies are available.

  Note:

  System-generated hints are unavailable for configuration as of October 2021. The previously existing tabs for 'Location Hints' and 'Mechanic Hints' have been removed from the Hint & Media Detail Panel accordingly.

  Hint & Media Detail Panel

## Active Hints Table

The active hints table contains the active official hints that are associated with the selected activity or trophy in the selected environment. You can have a maximum of three active official hints for each trophy or leaf activity in each environment. During gameplay, active hints are displayed in the order specified in the active hints table.

Active hints in the development environment are available for preview and testing on your DevKit (see [Previewing Official Hints on DevKits](previewing-official-hints-on-dev-kits.html "This topic provides details on how to preview official hints on DevKits during development.")). Active hints in the production environment are available to players who can access the associated activity or trophy.

You can use this table to change the display order of active hints, or to make active hints inactive. In the development environment, you can also use this table to publish active hints to the production environment (see [Publishing Official Hints to Production](publishing-official-hints-to-production.html "This topic provides details on publishing official hints to production environments, including how to edit and delete them after they've been published.")).

Active hints cannot be edited in the Game Help tool. To make changes to an active hint, you must first move the hint to the Inactive Hints table by selecting 'Move to Inactive'.

## Inactive Hints Table

The inactive hints table contains the inactive official hints associated with the selected activity or trophy in the selected environment. There is no limit to the number of inactive hints you can create, and inactive hints have no display order.

Inactive hints in the development environment are available for editing, but they cannot be previewed or tested on console. Inactive hints in the production environment are not available to players.

You can use this table to make inactive hints active. In the development environment, you can also use this table to publish hints to the production environment.

## Media Associated with this Activity

Note:

This table is only available for activity hints and does not appear in the Hint Details Panel for trophy hints.

The Hint & Media Detail Panel contains a list of video clips that have been uploaded into the tool and associated with the selected activity. These are generated from videos uploaded via the media gallery on DevKits. You can click on a video clip to preview it. You can use a video clip to create a new official hint by clicking Create New Hint in the row that contains the video clip. This launches the Create New Hint page with the relevant information pre-filled.

See [Creating Activity Hints](creating-activity-hints.html "This topic covers the process for creating official hints.") for more ways to create official hints.

# Viewing Media Assets

This topic provides information on how to view media assets you can use with Game Help content.

Select **Game Help** > **Media Asset Library** to view all the media files you can use with Game Help. This includes images and videos uploaded from your PC, and videos uploaded from the console's Media Gallery. See [Uploading Media Assets](uploading-media.html "This topic provides information on the types of media assets you can upload to use for custom Game Help content.") for more information.

Media Asset Library

In the Media Asset Library, each row corresponds to a media file. Each row contains the following information:

* File Name

  The filename identifying this file. If the file was uploaded from the Game Help Tool, this is the original filename. If the file was provided from a media gallery video, the filename is automatically generated from relevant video clip information.
* Segment Timecode

  If the video was uploaded from the console's Media Gallery and contains activities, Game Help generates a relevant video clip of the activity. The start and end timestamps of the generated clip are when the `activityStart` and `activityEnd` occur within the original video capture.
* Source

  Whether the file was uploaded from a PC via the Game Help Tool, or from a console, using the Media Gallery.
* Upload Status

  The date and time that the file was provided to the Game Help system. If the file is not yet fully transcoded by the system, the current transcoding status is shown instead. If the file cannot be processed correctly, a failure message is shown.

Each row also contains links that enable you to perform the following actions:

* Delete

  This link allows you to delete the image or video clip from your media asset library. This link is disabled if the image or video clip is associated with any official hint, whether or not the hint is active or published to production. To delete a media file, make sure there are no official hints that are using the media.
* Create New Hint

  You can select Create New Hint to create a new activity hint using this file. This opens the Create New Hint page with relevant information prefilled (see [Creating Activity Hints](creating-activity-hints.html "This topic covers the process for creating official hints.")).

Click on a media row to expand it. Expanding a media row allows you to perform the following actions:

* View the media file. If the media file is a video, you can play the video in a browser video player.
* See the automatically-associated activity this video contains, where applicable. This is only available for videos that contain activities and that were uploaded from DevKits.
* See a list of official hints that use this media file.

  Expanded Media File Row in Media Asset Library

## Searching and Filtering for Media

Game Help currently allows you to upload an unlimited number of media files for your game. This design means that your browser's built-in search functionality might not always work as expected for searching or filtering your files. For the best results, use the Game Help tool's search box at the top of the media asset library table, as shown in the figure below.

Searching for Media in the Media Asset Library

# Selecting Languages

This topic provides information on selecting the language used for your activity and trophy names.

The Game Help Tool allows you to choose which language to use for viewing your activity and trophy names. When you launch the Game Help Tool, names are initially displayed in your default supported language.

You can use the the System Language drop down to select any of the languages supported by your game.

Language Selector Dropdown on Activity Tree

When you select a different language, the Game Help Tool updates to show the localized property names that have been configured for trophies, activities, and hints.

Localized Activity Tree