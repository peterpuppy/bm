# System Software User's Guide (Main Screens) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Main_Screens/game-library.html

# Main Screens of the System Software

This document explains the main screens of the system software (their purpose, role, and design background) that should be understood by application developers.

The following screens of the system software operate in coordination with applications:

* **Home screen**.

  A user can select an application to start up on this screen. There are two homes: a game home for game experiences and a media home for media experiences. The user can also obtain various information concerning the application in a personalized form through the hub. For more information, see [Home Screens](home-screen.html "This topic describes the main features that are available on the game home screen and media home screen on a development machine. For information on the layout shared by all home screens, see Basic Configuration of the Home Screen.").
* **Control Center**.

  A user can execute simple tasks and features for enhancing the game experience on this screen. The Control Center will be displayed over a section of the game screen by pressing the PS button while the application is running. Because the application will keep running even while this screen is being displayed, it can be used without disrupting the user's game experience or feeling of being immersed in the game. For more information, see [Control Center](control-center.html "A user performs various operations during gameplay to optimize the game experience such as checking a friend's online status, adjusting voice chat, and checking session invitations or messages. The Control Center is provided so that the user can complete these simple tasks without having to completely leave the game and still be able to maintain the feeling of being immersed in the game.").

Main Screens of the System Software (Transitions from the Home Screen to the Control Center)

# Home Screens

This topic describes the main features that are available on the game home screen and media home screen on a development machine. For information on the layout shared by all home screens, see [Basic Configuration of the Home Screen](basic_configuration_of_the_home_screen.html "The home screen is composed of three areas: the system view, experience switcher, and the hub. Each of these areas is described here.").

There are two home screens: a [game home](home-screen.html#system-software-users-guide-main-screens_0_3__system-software-users-guide-main-screens_0_3_2) for game experiences and a [media home](home-screen.html#system-software-users-guide-main-screens_0_3__system-software-users-guide-main-screens_0_3_3) for media experiences. The home screen allows users to select applications to start up. The home screen also includes the hub, where users can also get personalized, application-related information, and the game library, where users can access all their installed games and applications.

Game Home and Media Home

## Game Home Screen

The main features that can be used from the game home screen of a development machine are as follows:

* ★Store Preview
* ★workspace
* ★Game Hub Preview
* ★Cloud Streaming Preview
* ★Debug Settings
* Installed applications and game hubs (see [Game Hubs](game-hubs.html "Game hubs provide features for obtaining the latest information about installed games. The player can view all information concerning a specific game in a personalized form."))
* Game library (see [Game Library](game-library.html "Home displays a limited number of icons and Game Library is the main location where the user can access all the installed games and applications. Game Library is located on the furthest right position of Home for easy access. Games and applications that are no longer displayed on the Home Screen are captured in Game Library.")).

## Media Home Screen

The main features that can be used from the media home screen of a development machine are as follows:

* ★Debug Settings
* Application library

## Reference Information

The following features are also explained in the documents indicated below:

* ★workspace: [System Software User's Guide (Application Development Support)](../System_Software-Users_Guide_for_Development_Support/__document_toc.html)
* ★Debug Settings: [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html)
* Game Hub: [Game and App Hub Overview](https://learn.playstation.net/bundle/content-pipeline/page/GameHub_Overview.html)
* ★Game Hub Preview: [PlayStation™Network Game Hub Preview Application Overview](../PSN_Game_Hub_Preview_Application-Overview/__document_toc.html)

# Basic Configuration of the Home Screen

The home screen is composed of three areas: the system view, experience switcher, and the hub. Each of these areas is described here.

Basic Configuration of the Home Screen

## System View

The main features of the system view are as follows:

* Switching between game and media homes
* Settings
* Profile

The system view is displayed in both the game home and the media home.

## Experience Switcher

The experience switcher displays executable applications. Select an application using the directional keys and start it by pressing the Enter button. If multiple packages under a concept are installed, they are displayed separately.

## Hub

This area is for rapidly displaying various information relating to an application on the home screen, increasing user engagement with the application, and encouraging the user to launch the application. A hub for a game application is called a game hub. For details, refer to the [Game Hubs](game-hubs.html "Game hubs provide features for obtaining the latest information about installed games. The player can view all information concerning a specific game in a personalized form.") section and the [Game and App Hub Overview](https://learn.playstation.net/bundle/content-pipeline/page/GameHub_Overview.html) document.

# Game Hubs

Game hubs provide features for obtaining the latest information about installed games. The player can view all information concerning a specific game in a personalized form.

When a game is installed, its icon is displayed on the home screen. If the cursor is moved to the icon, the game hub is displayed below the icon, and the player can view information about the game.

What is currently supported is as follows:

* Displaying a background image included in the game package. (If a background image is not included in the package, the default background image is displayed)
* Pushing the "Play" button to launch the game

A Game Hub

# Game Library

Home displays a limited number of icons and Game Library is the main location where the user can access all the installed games and applications. Game Library is located on the furthest right position of Home for easy access. Games and applications that are no longer displayed on the Home Screen are captured in Game Library.

Game Library offers two main tabs:

* Installed tab: This is the default tab. It displays all the installed packages, whether they are stored in internal storage, or on external hard drives or m.2 solid state drives. Pre-installed system applications can also be accessed from this tab. Users can perform various storage-related operations through the options menu. These include deleting a package or transferring packages between storage locations. See also [Display Rules of the Installed Tab](display_rules_of_installed_tab.html "To ensure users can easily access each installed package, the Installed tab creates an icon for each package that is installed. This means that if the user has both PlayStation®4 and PlayStation®5 versions of the game installed, the Installed tab displays two icons. Users can open the options menu of each tile to access management options specific to that package.").

  + When the user is offline, only the Installed Tab is displayed.
* Your Collection tab: This tab displays every game the user has purchased or played. A user can select each game to access its Game Hub and take actions to play such as Download and Stream. See also [Display Rules of the Your Collection Tab](display_rules_of_your_collection_tab.html "To maintain a simple and organized view, the Your Collection tab groups multiple versions of the same game onto a single tile. This means that if the user purchases both the PlayStation®4 and PlayStation®5 versions of the game, only a single game tile is displayed.").

Game Library

# Display Rules of the Installed Tab

To ensure users can easily access each installed package, the Installed tab creates an icon for each package that is installed. This means that if the user has both PlayStation®4 and PlayStation®5 versions of the game installed, the Installed tab displays two icons. Users can open the options menu of each tile to access management options specific to that package.

Installed Tab Showing Multiple Installed Versions of a Game

If the user has games that are installed on the external hard drive, the Extended Storage section is displayed below the Console Storage section. This helps users to understand where each game is stored. The m.2 solid state drive is considered an extension of console storage, so games stored on m.2 solid state drives are displayed in the Console Storage section.

Installed Tab Showing Extended Storage Section

# Display Rules of the Your Collection Tab

To maintain a simple and organized view, the Your Collection tab groups multiple versions of the same game onto a single tile. This means that if the user purchases both the PlayStation®4 and PlayStation®5 versions of the game, only a single game tile is displayed.

Grouped tiles display an overlay that shows the number of items that are contained in the group. Grouped tiles also display platform tags, which show the platforms that are supported by the game versions in the user's collection. Note that this is not the same as a list of platforms that the game supports.

When the user selects a grouped tile, the user is navigated to a selection flow where they can select which Game Hub to view.

Interaction with a Grouped Tile

If the user has played or purchased only one version of the game, the displayed metadata directly reflects that specific version. When the user selects the tile, they are directly navigated to that Game Hub.

Interaction with a Non-Grouped Tile

# Control Center

A user performs various operations during gameplay to optimize the game experience such as checking a friend's online status, adjusting voice chat, and checking session invitations or messages. The Control Center is provided so that the user can complete these simple tasks without having to completely leave the game and still be able to maintain the feeling of being immersed in the game.

The Control Center is displayed when the user presses the PS button. The Control Center is displayed using a section of the screen, so the user can see game progress alongside the Control Center.

Note: To maintain the user's feeling of being immersed in the game, make sure the user feels as though the application is still running, by continuing the application's BGM for example, when the Control Center is displayed (when the application is in the foreground and when the controller's focus is off the application).

## Main Features of the Control Center

The following features can be operated from the Control Center of Development Kits:

Control: Features frequently accessed by the user in-game are placed at the bottom of the Control Center. When the options button is pressed with the focus on the control menu icon, the displayed menu can be customized. The available options are listed below:

* Home: return to the home screen.
* Switcher: switch between recently-used games and media apps.
* Notifications: view and manage recently-received notifications.
* Game Base: start a party or play games with your friends.
* Music: access your playlists and featured music.
* Broadcast: broadcast gameplay to your streaming channels
* Accessibility: manage common accessibility features, such as text size options.
* Downloads/Uploads: view and manage your current downloads and uploads.
* Network: check your network status.
* PlayStation®VR: adjust the settings of your PlayStation®VR.
* Sound: adjust audio output and voice chat balance.
* Mic: adjust your audio input devices.
* Accessories: manage connected devices.
* Voice and Agent (US and UK only): operate your PlayStation®5 with your voice.
* Profile: check your online status, profile and trophies.
* Power: access power options.

Cards: cards are displayed according to the game scene and system state.

* Activities of information regarding joined-in sessions, for example.
* On DevKits, an optional debug card that can be used for testing can be displayed.

Control Center