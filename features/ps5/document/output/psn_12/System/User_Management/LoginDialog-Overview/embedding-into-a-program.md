# LoginDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginDialog-Overview/embedding-into-a-program.html

# Library Overview

# Purpose and Characteristics

The LoginDialog library is a library that performs login of users selected from a list of users registered on a PlayStation®5 displayed onscreen.

On PlayStation®5, applications first obtain a list of already logged in users from the UserService library, then the controller input monitoring for each user and save data saving/loading is performed. Therefore, users must be logged in to the PlayStation®5 in order for the users to use applications.

On the other hand, on PlayStation®5 user login generally occurs when a controller is connected, therefore it was somewhat difficult for situations to naturally arise where there are more users logged in than there are controllers connected.

However, if applications could easily create such situations and also appropriately change the controller user, it would be possible to provide quality application experiences where multiple users take turns using the same controller in turn-based games, etc.

In order for the LoginDialog library to support the development of such applications, a feature is provided where new users can be logged in to a PlayStation®5 without additional controllers being connected.

The LoginDialog library hides GUI display and the handling of user operations. The basic usage flow is to first initialize dialog, then set the required parameters, display the dialog, monitor for the closing of the dialog through polling, and finally perform termination processing for the dialog once it is closed.

# Main Features

The main features provided by the LoginDialog library are as follows.

* Feature for displaying a list of users registered on a PlayStation®5 and logging in the selected user
* Feature for displaying a list of logged in users then logging out the selected user when a new user attempts to log with the LoginDialog library in a state where the maximum number of logged in users has been reached

# Embedding into a Program

Include login\_dialog.h in the source program. In addition, before calling any LoginDialog library function in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_LOGIN_DIALOG) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceLoginDialog\_stub\_weak.a.

# Sample Programs

Sample programs using the LoginDialog library are as follows.

## sample\_code/system/demo\_device\_switch\_game/

This sample is for a turn-based game played by two users taking turns. By using the LoginDialog library and LoginService library to appropriately switch the user holding the controller, it will be possible to allow gameplay where two users can take turns in an environment with just one controller.

# Reference Materials

For the concept of users regarding the PlayStation®5 system, refer to the following documents:

* [User Management Overview](../User_Management-Overview/__document_toc.html)
* [UserService Library Overview](../UserService-Overview/__document_toc.html)
* [UserService Library Reference](../UserService-Reference/__document_toc.html)

For details on the procedures for using the login dialog to share devices such as controllers between users, refer to the following documents:

* [LoginService Library Overview](../LoginService-Overview/__document_toc.html)
* [LoginService Library Reference](../LoginService-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - LoginDialog Library](../ReleaseNotes/System-LoginDialog-ReleaseNotes.html)