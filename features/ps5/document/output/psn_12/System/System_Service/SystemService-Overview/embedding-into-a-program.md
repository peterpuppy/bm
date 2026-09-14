# SystemService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Overview/embedding-into-a-program.html

# Library Overview

# Purpose and Characteristics

The SystemService library allows you to use various system software features listed below.

* [Obtaining System Parameters](obtaining-system-parameters.html):

  The language used, date format, etc., set by the user in the system software menu can be obtained.
* [Obtaining the Notification of Events Occurring Outside the Application](obtaining-the-notification-of-events-occurring-outside-the-a.html):

  Events related to an application may occur outside the application. The system software notifies the application of such occurrences through this feature.
* [Obtaining the UI Status of the System Software](obtaining-the-ui-status-of-the-system-software.html):

  Screen and input device usage rights may be temporarily intercepted from an application by the system software. The application can check for such occurrences with this feature.
* [Obtaining the Execution Status of an Application](obtaining-the-execution-status-of-an-application.html):

  A user can switch to another application without terminating the application in use. In this case, the first application will continue running in the background. An application can check to see if it is running in the background with this feature.
* [Switching Executable Files](switching-executable-files.html):

  A program being executed by the application can be switched to another program file.
* [Controlling Media Playback](ps5-controlling-media-playback.html):

  The system software is equipped a media playback feature for music and videos, and users can play back media while simultaneously using an application. The application can request the system software to stop playback of this media when there is a situation in the game when it is desirable to do so.
* [Controlling the GPU Load of the System Software](ps5-controlling-the-gpu-load-of-the-system-software.html):

  The system software continues to use the GPU while the application is running in the foreground. When it is required upon debugging or analyzing performance, the GPU load of the system software can be changed (limited to the development stage).
* [Obtaining the Display's Safe Area](obtaining-the-displays-safe-area.html):

  Depending on the type of display or individual differences of the displays, margins of the frame buffer may not be displayed. The application can make an inquiry to the system software regarding the area that can be displayed on the connected display.
* [Reporting a Fatal Abnormal State and Terminating the Application](reporting-a-fatal-abnormal-state-and-terminating-the-applica.html):

  When entering a fatal abnormal state in which proper program operation cannot be continued, a report can be made to the system software, the user can be notified of an error occurrence, and the execution of the application can be terminated.
* [Launching the Controller Settings Screen](ps5-launching-the-controller-settings-screen.html):

  Applications can launch the "Controllers" settings screen in the system software as needed.
* [Obtaining HDR Display Parameters](ps5-obtaining-hdr-display-parameters.html):

  Parameters that represent the luminance characteristics of the connected TV/display can be obtained. Using these parameters, applications can provide appropriate HDR representations that match the performance that a TV/display is capable of.
* [Launching Player Dialogs](ps5-launching-player-dialogs.html):

  Applications can launch player dialogs as required, initiating actions concerning players on the PlayStation™Network.
* [Clearing the Splash Screen](clearing-the-splash-screen.html):

  The system software displays the application's startup image to prevent a screen blackout upon application startup. The application must instruct the system software to stop this display when it is ready to perform screen outputs.
* [Controlling the Notice Screen Skip Flag](ps5-controlling-the-notice-screen-skip-flag.html):

  The Notice Screen Skip flag is a mechanism for allowing the skipping of logos, warnings, and other matter displayed immediately after an application is launched so that they are not redundantly and repetitively displayed every time the application is run. The application can obtain the Notice Screen Skip flag and can also, if necessary, be put in manually set mode to enable the Notice Screen Skip feature at any time.
* [Displaying Challenge Activity Cards](ps5-displaying-challenge-activity-cards.html):

  The application can open challenge activity cards (action cards for challenge activities) on the screen and display interactions undertaken via challenges between users on PlayStation™Network.
* [Displaying Tournament Activity Cards](ps5-displaying-tournament-activity-cards.html):

  The application can open tournament activity cards (action cards for tournament-linked competitive activities) on the screen and show the user tournaments that can be joined on PlayStation™Network.
* [Launching Specific System Features](ps5-launching-specific-system-features.html):

  The application can launch specific features that come standard as part of the system to allow users to use them.

# Embedding into a Program

Include system\_service.h in the source program.

Upon building the program, link libSceSystemService\_stub\_weak.a. (The application does not have to load the PRX module for the SystemService library, as this process will be carried out automatically.)

# Reference Materials

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - SystemService Library](../ReleaseNotes/System-SystemService-ReleaseNotes.html)

For details about challenge activities on PlayStation™Network that use challenge activity cards, refer to the following document:

* [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html)

Refer to the following document for information about tournaments:

* [PlayStation™Network Tournaments System Overview](../PSN_Tournaments_System-Overview/__document_toc.html)