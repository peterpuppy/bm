# UserService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/UserService-Overview/using-the-settings-related-to-accessibility.html

# Using the Library

This topic describes the basic procedure for user management using the UserService library, how to obtain user IDs in a single player game, game preset configuration, and how to use settings values related to accessibility.

# Basic Procedure

This chapter explains the processing procedure in a game played by multiple users as the basic procedure for UserService processing. Note that dynamic management in consideration of user logins/logouts when an application is running is required.

1. **Initialize the library**

   Call `sceUserServiceInitialize()` to initialize the library. NULL may normally be used for the argument, but if you want to change the priority of the thread internally created in the UserService library for event transmission, prepare an `SceUserServiceInitializeParams` type variable, set the `priority` member appropriately, and specify the variable as an argument.

   Note:

   To explicitly specify a CPU affinity mask, use `sceUserServiceInitialize2()` instead of `sceUserServiceInitialize()`.
2. **Obtain logged in users**

   To look up the users logged in to the system, call `sceUserServiceGetEvent()` and obtain UserService events. UserService events can be obtained as `SceUserServiceEvent` structures and contain the event type (login/logout) and the user ID of the user that caused the event. Notifications of login events for users logged in at application start will also be issued immediately after UserService library initialization.

   Note:

   Another way of doing this is to use `sceUserServiceGetLoginUserIdList()` to obtain a list of the user IDs of logged in users, but using `sceUserServiceGetEvent()`, as described above, is recommended.
3. **Processing for each user**

   Once the user IDs of the logged in users are known, ports can be opened with the Pad library, AudioIn library, AudioOut library, etc., based on this information.

   If you want to display the user names on the screen, `sceUserServiceGetUserName()` can be used to obtain the user names.

   If you want to use user numbers (numbers allocated to users by the system), they can be obtained with `sceUserServiceGetUserNumber()`. Regarding user numbers, see the [User Management Overview](../User_Management-Overview/__document_toc.html) document.

   If you want to obtain the value of "Age Level for PS5 Games" set for a user, obtain it using `sceUserServiceGetAgeLevel()`. Refer to the [UserService Library Reference](../UserService-Reference/__document_toc.html) document regarding the setting of "Age Level for PS5 Games".
4. **Terminate the library**

   When the UserService library is no longer required, call `sceUserServiceTerminate()` to perform termination processing. By doing this, resources allocated in the library will be released.

## API Summary

The API features used in basic processing for the UserService library are shown below.

API Features Used in Basic Processing

| **API feature** | **Description** |
| --- | --- |
| `sceUserServiceInitialize()` | Function that initializes the library |
| `SceUserServiceInitializeParams` | Initialization parameter structure |
| `sceUserServiceGetEvent()` | Structure that obtains a UserService event |
| `SceUserServiceEvent` | Structure that holds a UserService event |
| `SceUserServiceLoginUserIdList` | Structure that holds the user ID list of the logged in users |
| `sceUserServiceGetLoginUserIdList()` | Function that obtains the user ID list of the logged in users |
| `sceUserServiceGetUserName()` | Function that obtains the user name |
| `sceUserServiceGetUserNumber()` | Function that obtains the user number |
| `sceUserServiceGetAgeLevel()` | Function that obtains the value set for a game's age level restriction |
| `sceUserServiceTerminate()` | Function that terminates the library |

# Processing Procedure for Single-Player Games

Obtaining the user ID of the user is required for input/output device and save data access, even for applications meant for one player. However, there are mechanisms designed to reduce the user management processing required for applications limited to one player.

Enable the InitialUserAlwaysLoggedIn flag during package creation if the application is meant for one player. By doing this, the user that started the application will be guaranteed to always be logged in, and there will be no need to deal with user logout so long as the user ID of the user that started the application has been obtained. (The mechanisms that guarantee this fact are explained in the [User Management Overview](../User_Management-Overview/__document_toc.html) document.)

The user ID of the user that started the application can be obtained using `sceUserServiceGetInitialUser()` after the library has been initialized. In addition, the user name can be obtained using `sceUserServiceGetUserName()`. Once this information has been obtained, the library can be terminated.

Note:

The InitialUserAlwaysLoggedIn flag is not a feature that forces one player play. Even if this flag is enabled, it is possible for other users to log in/log out, and the application can obtain the user list and login/logout events to handle multiple players.

## API Summary

The API features used in processing for single player games are shown below.

API Features Used in Processing for Single Player Games

| **API feature** | **Description** |
| --- | --- |
| `SceUserServiceInitializeParams` | Initialization parameter structure |
| `sceUserServiceInitialize()` | Function that initializes the library |
| `sceUserServiceGetInitialUser()` | Function that obtains the user ID of the user that started the application |
| `sceUserServiceGetUserName()` | Function that obtains the user name |
| `sceUserServiceTerminate()` | Function that terminates the library |

# Using Game Presets

Game presets are common configuration items for games; they are provided for the purpose of eliminating the user's burden of having to make settings for each game.

Users can enter in advance their preferred value for each of the configuration items provided by the system from "Settings" > "Save Data and Game/App Settings" > "Game Presets". Items that can be configured are as follows:

Game Preset Configuration Items

| **Item** | **Value** |
| --- | --- |
| Difficulty | Game Default/Easiest/Easy/Normal/Hard/Hardest |
| Performance Mode or Resolution Mode | Game Default/Performance Mode/Resolution Mode |
| First-Person View > Vertical Camera Movement | Game Default/Normal/Invert (Refer to [First-Person View Camera Operations](using-game-presets.html#user-service-library-overview_1_3__12a109b9-947c-1124-8f3b-87eb58680003)) |
| First-Person View > Horizontal Camera Movement | Game Default/Normal/Invert (Refer to [First-Person View Camera Operations](using-game-presets.html#user-service-library-overview_1_3__12a109b9-947c-1124-8f3b-87eb58680003)) |
| Third-Person View > Vertical Camera Movement | Game Default/Normal/Invert (Refer to [Third-Person View Camera Operations](using-game-presets.html#user-service-library-overview_1_3__12a109b9-947c-1124-8f3b-87eb58680004)) |
| Third-Person View > Horizontal Camera Movement | Game Default/Normal/Invert (Refer to [Third-Person View Camera Operations](using-game-presets.html#user-service-library-overview_1_3__12a109b9-947c-1124-8f3b-87eb58680004)) |
| Subtitles and Audio > Display Subtitles | Game Default/Off/On |
| Subtitles and Audio > Audio Language | Same as Console/Original Audio |
| Online Multiplayer Sessions > Who Can Join | Game Default/Invited Players/Friends/Friends of Friends/Anyone |
| Online Multiplayer Sessions > Who Can Invite | Game Default/Leader Only/All Members |

It is recommended that these configuration values be obtained from the system using `sceUserServiceGetGamePresets()` when the user first begins a game and that they be used as default values for configuring the play environment. The handling of each item can be freely determined by the application; some examples are given below:

* Automatically apply the configuration values of items as the application's default settings
* Read the configuration values of items, display them as default values on the application's configuration screen, and let them be applied by user operation
* If the application does not have settings that correspond to the configuration items, do not use the configuration values; use the application's unique settings instead

A user can change these configuration values at any time regardless of the game progress. It is sufficient for an application to reflect these values upon initial configuration of the play environment; once gameplay is started, it is not necessary to keep track of the latest configuration content.

"Game Default" means the user has not made a setting for the item yet or that the user has no preference regarding the item. An application can apply its own default values for such items.

## Camera Operations

Do not treat the settings for first/third-person camera operations as simply configuration values for either inverting or not inverting the default camera operation behavior set by the application. Interpret them so that when either the normal or invert configuration value is obtained, behavior will be as follows.

First-Person View Camera Operations
Third-Person View Camera Operations

## Online Multiplayer Sessions

The user's preference regarding users who can join and users who can invite others to online multiplayer gameplay will be set. These values correspond to the `joinableUserType` (users who can join without invitations) and `invitableUserType` (members who can send invitations) properties described in [Session Manager Web API Overview - Types of Sessions and Their Main Properties - Player Sessions](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/player-sessions.html). Because it is difficult or inappropriate to set `joinableUserType` : `SPECIFIED_USERS` and `invitableUserType` : `NO_ONE` as user preferences, there are no values corresponding to these settings.

## API Summary

The API features used in the processing of using game presets are shown below.

API Features Used in Processing for Game Presets Usage

| **API feature** | **Description** |
| --- | --- |
| `SceUserServiceInitializeParams` | Initialization parameter structure |
| `sceUserServiceInitialize()` | Function that initializes the library |
| `SceUserServiceGamePresets` | Game presets structure |
| `sceUserServiceGamePresetsInitialize()` | Function that initializes the game presets structure |
| `sceUserServiceGetGamePresets()` | Function that obtains game presets |
| `sceUserServiceTerminate()` | Function that terminates the library |

# Using the Settings Related to Accessibility

This library can be used to obtain the configuration values for accessibility-related system software settings that can be set individually per user. Obtain and use these configuration values if referencing them in the application would improve the user experience.

## API Summary

The API features used to obtain accessibility configuration values are shown below.

API Features Used for Obtaining Accessibility Configuration Values

| **API feature** | **Description** |
| --- | --- |
| `sceUserServiceGetAccessibilityChatTranscription()` | Obtains the setting for "Enable Chat Transcription" |
| `sceUserServiceGetAccessibilityPressAndHoldDelay()` | Obtains the setting for "Press and Hold Delay" |
| `sceUserServiceGetAccessibilityTriggerEffect()` | Obtains the setting for "Trigger Effect Intensity" |
| `sceUserServiceGetAccessibilityVibration()` | Obtains the setting for "Vibration Intensity" |
| `sceUserServiceGetAccessibilityZoomEnabled()` | Obtains the setting for "Zoom" |
| `sceUserServiceGetAccessibilityZoomFollowFocus()` | Obtains the setting for "Adjust Display Area to Movement" for zoom |