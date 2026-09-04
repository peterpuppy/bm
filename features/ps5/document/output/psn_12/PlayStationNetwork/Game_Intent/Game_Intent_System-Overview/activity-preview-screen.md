# Game Intent System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Game_Intent_System-Overview/activity-preview-screen.html

# Debugging Support for Developing Game Intent-Compatible Applications

This topic describes the debugging feature provided by the system software for supporting the development of game intent-compatible applications.

## Activity Debugging Feature

An activity created using the Universal Data System Management Tool can be checked using the activity debugging feature. The activity debugging feature is embedded in the system software of development machines and consists of the following 2 screens.

* [Activity Configuration Screen for Checking Activity Configurations and for Performing Various Operations](activity-configuration-screen.html "This topic provides an explanation of the Activity Configuration screen. For example, you can check the information set to activities and launch activities from this screen.")
* [Activity Preview Screen](activity-preview-screen.html "This topic provides an explanation of the Activity Preview screen, which enables you to check the appearance of activities displayed on the system software and their behavior.")

For details about "★Debug Settings", refer to the [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html) document.

Note:

The "WS-119115-8" error code will be displayed when the user attempts to open the activity debugging screen and both of the following conditions are met.

* The user doesn't have the Title Dev or Title Admin privilege.
* The application isn't running.

Refer to [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html) for details.

The activity debugging feature can also be used on a Development Kit/Testing Kit that has been set to Local Mode.

For details about Local Mode, refer to [Universal Data System Guide - Local Development Workflow - UDS Local Mode](../Universal_Data_System-Guide/about-the-uds-local-mode.html).

For sample programs for Local Mode, refer to [NpUniversalDataSystem Library Overview - Library Overview - Sample Programs](../NpUniversalDataSystem-Overview/sample-programs.html).

Note:

The activity debugging feature in Local Mode has the following limitations:

* The Game Help feature is not yet supported. (However, Game Help is enabled by default for all activities/tasks/sub tasks so that the activity card UX can be checked.)

# Activity Configuration Screen for Checking Activity Configurations and for Performing Various Operations

This topic provides an explanation of the Activity Configuration screen. For example, you can check the information set to activities and launch activities from this screen.

View of the Activity Configuration Screen

There are two ways to open this screen.

* Launching from Debug Settings

  Select "★Debug Settings" > "PlayStation Network" > "Show Activity Configuration" from "Settings" of the system software.

  If the application is running, a list of activities for the running application will be displayed.

* Launching from the experience switcher

  Place the focus on the target application in the experience switcher, press the options button to display the menu, and select "★Show Activity Configuration".

  A list of activities for the selected application will be displayed. The application doesn't have to be running.

When launching the Activity Preview screen from Debug Settings, you can perform tests for the game intent system without creating a package. When launching the Activity Preview screen from the experience switcher, you can test game startup entailing the game intent system for a game that isn't currently running. Use them separately according to your development phase and purpose.

The list of all activities (including those that can't be played) set using the Universal Data System Management Tool is displayed in descending order of the activity ID. Some of the attributes set are displayed on each activity panel.

The categories of activities displayed are as follows:

* progress
* openEnded
* competitive
* challenge

The following lists are displayed on this screen.

* Defined Activities
* Defined Activities (User Experience)

## Defined Activities

Because this list can be used to send a game intent event (such as for starting an activity) to an activity that is hidden from the Activity Preview screen or the Control Center of the system software, it's possible to perform tests for the game intent system in situations that are otherwise difficult to do.

The following features can be executed by selecting the panel for each activity:

* "Launch Activity"
* "Check Activity Metadata"
* "Check Activity Images"

**Launch Activity**

This feature launches the activity in single-player mode. If this item is selected, a game intent event of the Launch Activity type will be sent to the application.

Use this feature for the purpose of checking an implementation that uses a game intent event of the Launch Activity type.

**Check Activity Metadata**

When this item is selected, all of the attribute values set for the activity will be displayed.

Use this feature for the purpose of checking activity attribute values set using the Universal Data System Management Tool.

**Check Activity Images**

When this item is selected, all of the images set for the activity will be displayed. The images displayed are as follows:

* Activity large image
* Activity card image
* Reward images

Use this feature for the purpose of checking activity images set using the Universal Data System Management Tool.

## Defined Activities (User Experience)

This list displays activities and the activity details screen in the same way as they actually appear. The activity details screen can be displayed by selecting an activity. Use it for checking the appearance of an activity.

However, the following limitations exist.

* Dummy data will be displayed for some data such as match information.
* CTA of an activity's details screen will always be disabled.

In addition, this screen features a text box and the "Close App" button. The features of each are as follows.

## Text Box

A list of activities for an arbitrary game can be displayed by entering an npTitleId in this text box. If an application is running, the npTitleId of the application will be set in the text box by default.

## "Close App" Button

The application that is currently running will be terminated when this button is pressed. Next, when the Launch Activity option is selected, the application will launch, and a game intent event specific to the relevant type will be sent. You can thereby check the behavior of the application upon receiving a game intent event immediately after being launched.

# Activity Preview Screen

This topic provides an explanation of the Activity Preview screen, which enables you to check the appearance of activities displayed on the system software and their behavior.

View of the Activity Preview Screen

There are two ways to open this screen.

* Launching from Debug Settings

  First embed a parameter file in the application, execute the application, and then select "★Debug Settings" > "PlayStation Network" > "Activity Preview" from "Settings" in the system software.

  A list of activities for the currently-running application will be displayed. Since this screen does not display activities for applications that are not running, ensure that you start the application before opening this screen.

* Launching from the experience switcher

  Place the focus on the target application in the experience switcher, press the options button to display the menu, and select "★Activity Preview".

  A list of activities for the selected application will be displayed. The application doesn't have to be running.

When launching the Activity Preview screen from Debug Settings, you can perform tests for the game intent system without creating a package. When launching the Activity Preview screen from the experience switcher, you can test game startup entailing the game intent system for a game that isn't currently running. Use them separately according to your development phase and purpose.

Each activity panel will be displayed in exactly the same way as by the system software Control Center (for example).

Click on "**Close App**" to close the Activity Preview screen.

## Displaying Activity Lists

Each activity is classified and displayed as follows depending on its category and status.

* "*Available Challenges*" is a list of challenge activities that can be played by the user. In order to display an activity on this list, the `availableByDefault` value in the activity settings must be set to true in advance, or the activity must be set to *Available* to play with a UDS `activityAvailabilityChange` event.
* "*Active Challenges*" is a list of challenge activities that is being played by the user. In order to display an activity on this list, the activity must be started with a UDS `activityStart` event.
* "*History of Completed Challenges*" is a list of challenge activities that the user has finished playing. In order to display an activity on this list, the activity must be ended with a UDS `activityEnd` event.
* "*Not Started Activities*" is a list of activities that has never been started or completed by the user. In order to display an activity on this list, the activity must not be started with a UDS `activityStart` event or ended with an `activityEnd` event.
* "*In Progress Activities*" is a list of activities that has been started but never completed by the user. In order to display an activity on this list, the activity must be started with a UDS `activityStart` event and not ended with an `activityEnd` event.
* "*Completed Activities*" is a list of activities that has been completed by the user at least once. In order to display an activity on this list, the activity must be ended with a UDS `activityEnd (outcome: completed)` event.

The following lists are only displayed in [Resettable Mode](activity-preview-screen.html#game-intent-system-overview_4_2__section_jlb_lqf_y2c).

* "*Available Activities*" is a list of activities that can be played by the user. In order to display an activity on this list, the `availableByDefault` value in the activity settings must be set to true in advance, or the activity must be set to available to play with a UDS `activityAvailabilityChange` event.
* "*Active Activities*" is a list of activities that are being played by the user. In order to display an activity on this list, the activity must be available to play and it must be started with a UDS `activityStart` event. If a Player Session is created using the Session Manager service, the corresponding activity card will be displayed on this list.
* "*History of Completed Activities*" is a list of activities that the user has finished playing. In order to display an activity on this list, the activity must be ended with a UDS `activityEnd` event (regardless of the outcome).

  Note: Note that in the system UI for end users, an activity will only be displayed as "*Completed*" to the user if an `activityEnd` event is sent with `(outcome: completed)`.

Refer to [Universal Data System Guide - Reference](../Universal_Data_System-Guide/reference.html) for details about activity attributes and UDS events.

To reset the status of activities of the user viewing the screen, select "**★Debug Settings**" > "**PlayStation™Network**" > "**Universal Data System data**" > "**Delete data of this user (console and server)**" from "**Settings**" of the system software. Refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html) for details.

Activity Preview does not support the Local Development Workflow. Refer to [Universal Data System Guide - Local Development Workflow](../Universal_Data_System-Guide/local-development-workflow.html) for information about the Local Development Workflow.

Tournament activities are displayed under "**Tournaments**".

## Displaying Activity Lists in Resettable Mode

A switch can be made to *Resettable Mode* when selecting "**Go to Resettable Mode**" while viewing a list of activities. Select "**Go to Standard Mode**" in *Resettable Mode* to return to the default display.

The differences between *Resettable Mode* and the default display are as follows.

* In the *Resettable Mode* list, the progress and activity status are based on the activities, tasks, and sub-tasks the user has completed in the most recent instance of the activity. The most recent instance of the activity can be reset by sending a new start event for the task, sub-tasks, or the parent activity. This was the default UX displayed for activity cards prior to the 10.2 firmware update.
* In the *Standard Mode* list, the progress and activity status are based on the activities, tasks, and sub-tasks the user has started and completed so far (at any point in time). This is the default UX displayed for the system software's activity cards since the 10.2 firmware update. This option is only displayed when in *Resettable Mode*.