# User Management Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/User_Management-Overview/user-identifiers-shown-to-users.html

# User Management on the PlayStation®5

# Multi-user Simultaneous Login System

The PlayStation®5 system software permits multiple users to log in to the system simultaneously. By linking the management of input/output devices and save data to logged in users, a single console provides an environment that allows for the easy creation of multi-player games, whether player-vs.-player or cooperative play.

On the PlayStation®3 and earlier game consoles, applications were responsible for linking and managing multiple controllers and headsets for individual users. In addition, it was only possible to use one person's save data linked to a local account and one person's trophies/services linked to an account for PlayStation™Network.

With PlayStation®5 (and PlayStation®4), input/output devices such as controllers and headsets are linked to the local accounts of logged in users and managed by the system. In addition, each logged in user can access user-specific information such as save data and PlayStation™Network rights.

Figure 1. PlayStation®5 Multi-user Simultaneous Login System

Through this method of multi-user simultaneous logins, the responsibilities of applications will be reduced in the creation of multi-player games, and gameplay such as the following will become possible:

* When a monster is defeated in cooperative play, all players who contributed to the defeat will receive a trophy.

# User States

Only users logged in to the console can be recognized by applications.

When a device such as a controller or headphones are connected, dialog asking which user will use the device will be displayed, so user login will be performed for this by selecting an already registered local account or by creating a new local account and then logging in.

Note:

The dialog asking which user will use the device may be omitted depending on the number of logged in users.

When a user logs in, if the user has already signed in to the PlayStation™Network, the user will be in the "logged in + signed in" state. Users who have not signed up for the PlayStation™Network and users who have signed up but explicitly signed out or but were forcefully signed out by the system will be in a state called "logged in + signed out".

Applications can obtain notifications using a function provided by the UserService library when a user has logged in and when a user has logged out. In addition, whether a user is signed in or not and sign-in state changes can be obtained using functions provided by the Np library.

Up to 16 local accounts can be simultaneously registered on one console, and up to four users can be simultaneously logged in.

Note:

In addition to the local accounts registered on the console, there is a guest account for a temporary user. When a user logs out from a guest account, data of the account and save data linked to it will be deleted from the system. Note that there is no difference between local accounts and a guest account when seen from an application program and there is no method provided to distinguish them.

## Users Joined in a Game

Applications are not required to recognize all users logged in to a console. For example, in a single-player game, it is not a problem to only recognize the user who started the application and have that user join the game while ignoring other users (moreover, it is not a problem even if specifications are such that another user can start gameplay after the initial user logs out, or that other users are not recognized until reboot).

There are several requirements regarding user handling that applications must follow. Note that these requirements need only be applied to users who are recognized - and whose participation has been permitted - by the application. Permitting a user to join/participate in an application means displaying a text or image onscreen to indicate that user - for example, the player name or icon, character or "own device", a score or power bar; or accepting that user's controller operations or operations of another device. For such a user, parental control checking (for example) must be performed pursuant to the requirements; however, there is no need to take such action for other users.

# User Identifiers Used in a Program

## User ID

User IDs are provided as information for identifying logged in users. Applications can obtain a user ID list for the currently logged in users using a function provided by the UserService library.

A user ID is a positive number represented as a 32-bit signed integer. Note that in some cases the value may be larger than 16, which is the maximum number of local accounts.

Note:

The user ID is determined upon local account creation and is designed to not change until the local account is deleted.

`SCE_USER_SERVICE_USER_ID_SYSTEM` is defined as a special user ID that represents the system. This user ID is used when accessing shared input/output devices.

## Account ID

Account IDs used as user identifiers when using PlayStation™Network services can be obtained for user IDs using a function provided by the Np library.

# User Identifiers Shown to Users

## User Name

To correctly handle information linked to a user, it is extremely effective to display the user name obtained using a function provided by the UserService library onscreen in place of a display such as "player 1" or "player 2". It is strongly recommended that user names be used in screen designs for a multi-player game for PlayStation®5.

## User Number

When a user logs in to the system, the system assigns a "user number" from 1 to 4 to the user. User numbers are typically assigned in the order in which users log in and are valid only while they are logged in. User numbers are represented by the indicators that are part of each controller. Additionally, there are plans to add a feature that will display the correspondence between user numbers and user names in the UI of the system software. Applications can obtain user numbers using a function provided by the UserService library.

Applications can use user numbers as supplementary information for users. However, when a user logs out then logs in again during application suspension, the user will appear to be continually logged in from the viewpoint of the application, but there is a possibility that the user number for that user will have changed.

# Management of Devices Linked to Users

Input/output devices such as controllers that are used by each user are linked to logged in users and managed. The following are examples of applicable devices:

* Controllers
* Headsets
* Keyboards
* Mice

When these devices are connected to the console, dialog asking which user will use the device will be displayed, and the devices will be linked to users based on the user responses.

Devices such as TVs that are expected to be shared among multiple users will be automatically linked to the system (`SCE_USER_SERVICE_USER_ID_SYSTEM`). The following are examples of applicable devices:

* TVs or AV receivers/amplifiers
* Cameras

The libraries that access input/output devices are designed based on shared virtual device models and will specify input/output destinations using user IDs. For details, refer to "[Device Management](device-management.html)".

## "Switch User" Feature

The user using devices can be switched by pressing the PS button and selecting "Switch User" from the displayed menu.

Note that as seen from the application, there is no special change in users because of this feature. For example, the application views operation as follows when a switch is made from user A to user B.

1. User A logs out. (Note: On the PlayStation®4, user A does not log out.)
2. A login event will be issued for user B if user B was not logged in before. Nothing will happen if user B was already logged in.
3. All devices that were linked to user A will be linked to user B. For instance, if user A was in possession of a controller and user B was not, the switch will give possession of the controller to user B.

Information that would distinguish between logouts, logins, and changes to device linkages caused by the "Switch User" feature and those caused by other operations is not provided to the application. User B logging in should be treated the same as an ordinary login, and all that needs to be done to determine whether the user should be allowed to participate in game is the ordinary handling that the application would perform in any case, based on its specifications. If logging out means not being able to continue playing, then handle the logout by returning to the title screen or by doing whatever else would be suitable in that case. Any other handling, such as switching the user who controls "player 1" from user A to user B, is unnecessary.

## Feature to Change User-Device Linking

Applications can change devices linked to users using `sceLoginServiceRequestDevices()` of the LoginService library. This feature is useful for game applications played in turns, such as board game applications. For details, refer to the [LoginService Library Overview](../LoginService-Overview/__document_toc.html) document.

# Handling of Information Linked to a User

Information linked to individual users includes save data, trophies, and various information in the PlayStation™Network such as purchased entitlements.

Likewise, because a device is linked to a specific user on PlayStation®5, input from a device is linked to a single user. Take care to correctly link input data and in-game information using the user as key.

# Handling User Login/Logout

## For a Single-player Game

The handling of user login/logout can be omitted in an application that is played alone, as in a first-person-shooting game, by using the InitialUserAlwaysLoggedIn mode as long as specifications are such that only the user who started the application is allowed to join the game.

The enabling/disabling of the InitialUserAlwaysLoggedIn mode can be set using param.json. (For details, refer to [Param.json File Specification - Param File (param.json) Specifications - Parameter Definitions for Applications](../Param_Json-Specification/parameter-definitions-for-applications.html).) When enabled, it is guaranteed that the user who started the application will not log out. More specifically, when the user who started the application attempts to log out, the application will be suspended before logout processing is carried out. When the same user subsequently logs in again and attempts to use the suspended application, the application will be resumed; when a different user attempts to use the application, it will be restarted. In this manner, it will be guaranteed - as seen from the application - that the user who started the application is logged in. It is possible that other users will log in/log out; however, they can be ignored, as they are not allowed to join the game. In this way, there will be no need to handle login/logout.

The user who started the application can be obtained by using `sceUserServiceGetInitialUser()` of the UserService library.

It is often misunderstood that the InitialUserAlwaysLoggedIn mode forces/guarantees single-player gameplay. Even when this mode is enabled, other users can log in/log out; however, it is sufficient to ignore them in a single-player game as explained above.

## For a Multi-player Game

An application can receive notifications regarding user login/logout from the UserService library. In an application played by multiple players such as, fighting games and party games, handle the above notifications and open the device to respond to user operation.

When supporting the login of other users in addition to the user who started the application with the InitialUserAlwaysLoggedIn mode enabled, it is possible to realize a multi-player game with special handling of the user who starts the application. This can be used, for example, in a design where the user who starts the application plays a game to advance a story as the main character of a scenario and other users play the game in supporting roles to help the main character.

## For a Game Played in Turns

In a game played in turns such as, a board game, more users than the number of controllers can use the application. For example, the "Switch User" feature can be used for more users to log in than the number of controllers. With this feature, however, it is difficult to have many users log in in exactly the manner desired by the application.

To enable use in such a case, the LoginDialog library is provided. The application can prompt user login using a LoginDialog library API feature and provide navigation for multiple users to log in smoothly. For details, refer to the [LoginDialog Library Overview](../LoginDialog-Overview/__document_toc.html) document.

# Summary: Recommended User-oriented Game Design

The characteristic of a multi-user simultaneous login system is a "user-oriented system" in terms of game design. In other words, it may be easier understood as a "system that is not controller-oriented" when compared to previous game designs.

The traditional concept of "controller 1" or "controller 2" is not recommended on PlayStation®5, because changes to the links between users and controllers, users logging in or out, and other events can easily change the relationships between such numbers and users.

In designing/developing a game for PlayStation®5, it is strongly recommended that each user playing the game be focused on, instead of focusing on each controller, and that game design be centered on communication with users based on user information that can be obtained using the UserService library.