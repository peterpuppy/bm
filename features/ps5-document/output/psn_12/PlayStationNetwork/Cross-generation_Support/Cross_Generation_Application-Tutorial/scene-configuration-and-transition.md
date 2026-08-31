# Cross-generation Application Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Cross_Generation_Application-Tutorial/scene-configuration-and-transition.html

# Configuration of the Tutorial Sample

This topic describes the directories and file structure in the tutorial sample supporting cross-generation gameplay between PlayStation®5 and PlayStation®4, and the transitions of scenes and views within the application.

# Directories and File Structure in This Sample

The table below shows the main directories and files in the sample.

Main Directories and Files

| **Directory or File** | **Description** |
| --- | --- |
| ps4/ | This folder contains files and assets required to create PlayStation®4 packages. |
| ps5/ | This folder contains files and assets required to create PlayStation®5 packages. |
| psn/ | This folder contains processes to call PlayStation™Network-related features. The majority of these processes have been created using the samples in sample\_code/playstation\_network of the PlayStation®5 SDK. |
| duck\_shooting\_game.cpp | This is the base class for the application. The majority of the processes described in this tutorial document are contained in this file. |
| scene.cpp | This class manages the view classes. |
| view.cpp | This includes the processing performed on each screen. For the specific processing performed on each of these screens, refer to the derived classes. |
| tutorial\_cross\_gen.sln | This solution file contains projects for both PlayStation®5 and PlayStation®4. |

# Scenes and Views in This Tutorial and Transitions Among Them

This application consists of the following two scenes:

* Title Scene
* Game Scene

Each scene includes View classes, and the processing on each screen is controlled by the View class.

The Title Scene is for displaying various menus. The Title Scene includes the following views:

* Title Menu
* Single Player Menu
* Nat Type Check
* Premium Check
* Sign in Dialog (used only on PS4)
* Multiplayer Menu

Game Scene is a scene for engaging in single player or multiplayer gameplay. Game Scene includes the following views:

* Single Player Game
* Count Down
* Multiplayer Host Game
* Multiplayer Client Game

The general flow for scenes and views is provided below.

Transitions Among Scenes and Views

"Multiplayer" or "Single Player" can be selected in the Title Menu view.

* Select "Start Game" to transition to the Multiplayer Menu view for multiplayer mode (after a NAT type and premium check are performed) or to the Single Player Menu view for single player mode.
* The Lobby menu is displayed in the Multiplayer Menu view. A player session is automatically created in the Lobby menu. You can invite friends to the player session by selecting "Invite Friends". You can also check the Online IDs of friends who have been invited in the Lobby menu. After you select "Get Ready?" and all the members in the player session are ready, the scene transitions to the Multiplayer Host or Client Game view via the Count Down view.

Lobby Menu

* The Single Player Menu view displays "New Game" or "Continue". Select "New Game" to transition to the Single Player Game view with Level 1 selected. Select "Continue" to transition to the Single Player Game view with the level that is recorded in save data selected.

Single Player Menu

* In both multiplayer mode and single player mode, the results of the game are displayed when the game ends.

Refer to the "[Multiplayer Mode](multiplayer-mode.html "This topic describes the techniques for implementing real-time multiplayer gameplay (such as competitive activities and premium features, the invitation feature, and network communication) using the \"multiplayer mode\" of the tutorial sample supporting cross-generation gameplay between PlayStation®5 and PlayStation®4.")" chapter and the "[Single Player Mode](single-player-mode.html "This topic describes the techniques exclusively for implementing single-player gameplay (such as progress activities) using the \"single player mode\" of the tutorial sample supporting cross-generation gameplay between PlayStation®5 and PlayStation®4.")" chapter regarding the implementation points for multiplayer mode and single player mode, respectively.