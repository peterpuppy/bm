# LoginService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginService-Overview/library-overview.html

# Library Overview

# Purpose and Characteristics

The LoginService library is a library that provides features related to the devices managed by the system software and the holders of these devices.

By using the device reassignment feature in the LoginService library, it will be possible to transfer devices being used from their current users to other users at arbitrary times determined by the application. This feature is useful for turn-based games such as board games.

# Main Features

The main feature provided by the LoginService library is as follows.

* Feature that assigns an arbitrary device to each user

# Embedding into a Program

Include login\_service.h in the source program. In addition, before calling any LoginService library function in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_LOGIN_SERVICE) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceLoginService\_stub\_weak.a.

# Sample Programs

A sample program that uses the LoginService library is as follows.

## sample\_code/system/demo\_device\_switch\_game/

This is a turn-based game sample where two users take turns. It is programmed so that it is possible for two players in an environment with only one controller to play the game by switching the controller through appropriate use of the LoginDialog library and LoginService library to switch the user who holds the controller.

# Reference Materials

For details about users are conceptualized in the PlayStation®5 system, refer to the following documents.

* [User Management Overview](../User_Management-Overview/__document_toc.html)
* [UserService Library Overview](../UserService-Overview/__document_toc.html)
* [UserService Library Reference](../UserService-Reference/__document_toc.html)

The LoginDialog library provides a GUI for determining the target users when using the LoginService library to transfer devices between users. For details on the LoginDialog library, refer to the following documents.

* [LoginDialog Library Overview](../LoginDialog-Overview/__document_toc.html)
* [LoginDialog Library Reference](../LoginDialog-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - LoginService Library](../ReleaseNotes/System-LoginService-ReleaseNotes.html)