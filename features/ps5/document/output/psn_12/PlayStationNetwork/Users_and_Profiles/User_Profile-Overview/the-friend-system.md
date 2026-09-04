# User Profile Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/User_Profile-Overview/the-friend-system.html

# Friends

# The Friend System

PlayStation™Network users can become friends with each other. When a user is a friend with another user, the friend's online status and games being played will be displayed to the user in the "Friends" menu of the system software.

Mutual approval is required to become friends. The current user can send a friend request to another user and if the request is approved, the two will become friends. Similarly, when a friend request is received from another user and the current user approves the request, they will become friends.

A single user can have up to 2000 friends (including users to whom a friend request has been sent and users from whom a friend request has been received, but with approval pending).

It is possible to send a request to a friend for disclosing real names and profile pictures to each other. When the current user sends a real name request to a friend and the request is approved, or when a real name request is received from a friend and the current user approves the request, the two will become close friends (real names will be displayed to each other). In place of the Online ID and avatar that are displayed for friends, real names and profile pictures will be displayed for close friends.

It is also possible to send a request to a user who is not a friend for disclosing real names and profile pictures to each other. Such users will become close friends when a close friend request is sent/received and accepted.

Users can also stop being friends. When one user deletes the other user from their friend list, the two will no longer be friends.

State Transitions Leading to the Friends Status
State Transitions Leading to Real Name Display Status

# Block List

When friend requests and other messages from specific users are not wanted, it is possible to register these users on a block list. When registered on the current user's block list, friend requests and other messages sent from these users will not be received by the current user.

The maximum number of users that can be registered on a block list is 2000.

It is also possible to register friends on the block list. In such cases, since it is not possible for blocked users to be friends, the friend relationship will be canceled at the same time, and the users will no longer be friends.

# Privacy Settings

## Friend List Display Scope

Each user can set the scope of people who can view their friend list from the following four setting options.

* Anyone
* Friends of Friends
* Friends Only
* No One

## Real Name/Profile Picture Display Scope

Each user can set an additional privacy setting for the real name and profile picture that is displayed to friends after a real name request is approved.

* Close friends in a multiplayer game

  This is a setting to allow/prohibit disclosure of the current user's real name and profile picture in the game. When disclosure is allowed, the current user's real name and profile picture will be displayed on game screens of friends who are also playing the game online (if the application supports it).

# Usage of Friends in Applications

Applications can obtain the following data related to friends using the User Profile Web API.

* Friend list of a certain user
* Profile information of a certain user including their real name and profile picture

For details, refer to the [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html) document.

In addition the application can obtain friend list/block list changes via Push events. Refer to the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html) document for information on how to use Push events and refer to the [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html) document for details on Push events that can be used.

## Effects of Privacy Settings

The data related to friends (friend list, real name, and profile picture) that can be obtained using the User Profile Web API is limited to data that is authorized according to the target user's privacy settings.

* When a user who is not in the target user's display scope attempts to obtain the target user's friend list, an error will return.
* When a user, who is not a friend with whom a real name request has been approved, attempts to obtain the target user's profile information, profile information excluding their real name and profile picture will return.
* When the target user is not displaying their real name or profile picture in games, it will not be possible to obtain their real name or profile picture, even for a user who is a friend and with whom a real name request has been approved.

Because information corresponding in this way to each user's privacy settings and the relationship between users can be obtained, it is not necessary for the application to reference actual privacy settings of users.

Note that privacy settings are also effective during development. When implementing/testing features that obtain friend lists, real names/profile pictures, etc., note that the results will vary depending on the target user's privacy settings and on the relationship between the target user and current user.

## Changing Privacy Settings

The application can use the User Profile Web API to obtain the display scope set by the user for their real name and profile picture. For details, refer to the [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html) document.

If the display scope is set so that disclosure is prohibited, the MsgDialog library can be used to display a message to indicate this; it is also possible to display a message prompting the user to open and change their privacy settings. For details, refer to [MsgDialog Library Reference](../../../SDK/latest/MsgDialog-Reference/__document_toc.html).

Refer to the following sample program for the implementation an application to obtain a user's display scope for their real name and profile picture and to display the message dialog for changing the scope if required.

* sample\_code/system/api\_common\_dialog/showcase/message\_dialog