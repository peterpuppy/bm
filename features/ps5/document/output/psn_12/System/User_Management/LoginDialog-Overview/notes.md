# LoginDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginDialog-Overview/notes.html

# Notes

# User Logout Feature

On PlayStation®5, the maximum number of users that can be logged in at the same time is fixed at 4. When a new user attempts to log in during a state where the maximum number of logged in users has been reached, the LoginDialog library will show application users a list of the users who are already logged in and prompt selection of a user to log out. Afterward the user to log out is selected and logged out, the LoginDialog library will perform login of a new user.

By applications appropriately specifying parameters for the login dialog, it will be possible to exclude specific users from the selections of users to log out at this time. However, if there are 0 selection candidates for users to log out that are reflected in the specified parameters, the specified users to exclude in the dialog parameters will be ignored. Therefore, note that even if an application excludes a user from target users to log out, there is a possibility that the user will still be logged out.

# Relationship Between Devices and Users Selected in Login Dialog

Unlike the standard cases where user login occurs when a controller is connected to the PlayStation®5, controllers are not assigned to users logged in through the login dialog at the time of login. Therefore, when application operation requires a controller, the application must use the LoginService library at an appropriate timing to assign a controller to the user.

For details on the procedure for assigning a device to a user, refer to the [LoginService Library Overview](../LoginService-Overview/__document_toc.html) document and [LoginService Library Reference](../LoginService-Reference/__document_toc.html) document.