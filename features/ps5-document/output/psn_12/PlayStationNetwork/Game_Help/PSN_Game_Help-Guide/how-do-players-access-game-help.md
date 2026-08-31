# PlayStation™Network Game Help Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Help-Guide/how-do-players-access-game-help.html

# PlayStation™Network Game Help Overview

This chapter provides an overview of PlayStation™Network Game Help and its systems.

PlayStation™Network Game Help uses Universal Data System (UDS) data sent by games to provide on-demand, spoiler-free help based on players' current game progress. Players can view hints, tips, and video walk-throughs for specific activities and trophies directly in the console UI and on the PlayStation™App.

Game Help is the most used feature inside of activities with high satisfaction among players. On average, those that view Game Help content are more likely to complete the game and play more hours than players who played the same games but did not view Game Help content.

Game Help content falls under two categories:

* Community Game Help - Content that is automatically generated for progress activities through player activity
* Custom Game Help - Custom content that you create

Community Game Help Details

# Game Help Features and Functionality

This topic provides an overview of the features you'll use when developing Game Help content.

* Game Help allows players to find hints to help them make progress in your game. For more information on the player UX, see [Accessing Game Help as a Player](how-do-players-access-game-help.html "This topic provides information on how players access Game Help content.").
* Game developers can configure official hints for leaf activities and trophies. For more information on the relationship between official hints and activities, see [How Game Help is Associated with Activities](how-game-help-is-associated-with-activitie.html).
* The Game Help tool is a GUI-based tool that allows you to configure and manage official hints. For more information, see [About the Game Help Tool](the-game-help-tool.html "This chapter provides details on the Game Help tool.").

# Game Help Concepts

This topic provides an overview of key concepts you must know when developing Game Help content, such as hints, activities, and the Universal Data System (UDS).

The following concepts are important for understanding how Game Help works:

* Hints - Single pieces of help content that players can view. Game Help can display hints for activities, tasks, sub-tasks, and trophies. At a minimum, hints must contain a video walk-through, but they can optionally include a hint name and description.
* Community Hints - Most new hints are generated from players in the Community Game Help program. These hints are raw gameplay videos that match activity data sent by games.
* Official Hints - Hints that are created by game developers. Official hints include a video walk-through and can optionally include a hint name and description. For more information, see [Configuring Official Hints](official-hint-lifecycle.html "This chapter provides information on what official hints are and how to configure them.").
* Activities - Sections of gameplay that are part of the game's defined structure. For more information, see [Creating Activity Hints](creating-activity-hints.html "This topic covers the process for creating official hints.").
* Leaf Activities - Activities can contain tasks and tasks can contain sub-tasks. An activity that does not contain any tasks or a task that does not contain any sub-tasks is called a leaf activity. All sub-tasks are leaf activities.
* Trophies - Players can earn trophies by completing specified objectives in a game. For more information, see [Creating Trophy Hints](creating-trophy-hints.html "This topic provides details on creating trophy hints.").
* The Universal Data System (UDS) - Game Help depends on UDS metadata to describe objects and events, particularly activities and trophies. UDS uploads in-game data from the console to PlayStation™Network servers and uses it to power player-facing and developer-facing experiences in real time. See [Configuring Custom Game Help](official-hints-developer-provided-help.html "This chapter provides information on how to design and optimize custom Game help content.") and [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) for more information.

# Accessing Game Help as a Player

This topic provides information on how players access Game Help content.

Players can access Game Help for activities and unearned trophies from the Control Center, Game Hub, PlayStation™App, and trophy details screen. Titles that integrate `sceSystemServiceLaunchSystemDeeplink()` can also allow players to access Game Help directly from a game application. See [Opening a Consolidated activity Card using the SDK](opening-a-consolidated-activity-card-using-the-sdk.html "This topic provides information on how to open a consolidated activity card using the SystemService SDK.") for more information.

The figure below shows activity cards and trophy cards in the Control Center. Activity cards and trophy cards display an icon when Game Help content is available. See [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html) for more information on accessing activities in the system.

Activities and Unearned Trophies in the Control Center

**Player UX for Accessing Activity Hints**

The figure below shows the player UX for accessing official hints for activities:

Accessing Activity Hints
Game Help in the PlayStation™App

* When a player opens an activity card, the card displays the activity’s tasks and sub-tasks.
* When a player selects an objective that has Game Help content provided by the game developer, the first official hint is shown.
* When a player interacts with the thumbnail, they are taken to the hint detail screen where they can watch the walk-through video and read any hint text.
* Players can rate the helpfulness of the hint.

**Player UX for Accessing Trophy Hints**

The figure below shows the player UX for accessing official hints for trophies:

Accessing Trophy Hints

* When a player selects a trophy that has Game Help content, they see a thumbnail of the trophy's Game Help video.
* When a player interacts with the thumbnail, they are taken to the hint detail screen where they can watch the walk-through video or read through the hint text.
* Players can rate the helpfulness of the hint.

# Opening a Consolidated Activity Card Using the SDK

This topic provides information on how to open a consolidated activity card using the SystemService SDK.

While players primarily access Game Help by opening the Consolidated Activity Card from the system UI (Control Center), you can use the SystemService Library to allow players to open the Consolidated Activity Card directly from the game.

When calling `sceSystemServiceLaunchSystemDeeplink()`, you must provide `userId` and `param` arguments:

| Field | Description |
| --- | --- |
| `userId` | User ID of the user operating the application. |
| `param` | Parameters required to specify the deep link destination. For example, to open a Game Help list, pass the following:  {  "functionName": "gameHelp",  "screen": "consolidatedActivity"  } |

See [SystemService Library Reference - Launching Specific System Features - sceSystemServiceLaunchSystemDeeplink](../SystemService-Reference/ps5-sce-system-service-launch-system-deeplink.html) for more information.

## Sample Programs

The following sample programs implement `sceSystemServiceLaunchSystemDeeplink()`:

* `sample_code/playstation_network/api_np_universal_data_system_activity` - Open a Game Help list when you select **Deeplink to Game Help** from the menu.