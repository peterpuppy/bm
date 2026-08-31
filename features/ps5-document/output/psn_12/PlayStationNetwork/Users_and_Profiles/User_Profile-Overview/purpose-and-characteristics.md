# User Profile Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/User_Profile-Overview/purpose-and-characteristics.html

# Feature Overview

# Purpose and Characteristics

The PlayStation™Network User Profile feature provides various functionalities regarding relationships between users on PlayStation™Network, including the handling of user profile information, presence information, and friend lists.

Note:

Whether the User Profile Web API can be used or not is determined by the combination of platform and product type. For details, refer to the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html) document.

# Main Features

Applications can use the User Profile Web API to perform the following.

* Obtaining user profile information (real name, "About Me", etc.): Refer to the "[Profile Information](profile-information.html)" chapter for details.
* Obtaining presence information (whether online or not, etc.) regarding the user: Refer to the "[Presence Information](presence-information.html)" chapter for details.
* Obtaining a user's friend list/block list: Refer to the "[Friends](friends.html)" chapter for details.

# Handling Data of the User Profile Feature

In the Sandbox network architecture, data of the User Profile feature is handled as global data or sandboxed data, and the scope of data that can be obtained differs for each. Refer to [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html) for details about Sandbox and for details about global data and sandboxed data.

Data handling is explained below for each type of information.

## Profile Information

* Profile information is handled as global data. During development, the current user can obtain profile information of all the users in the development environment (DEV) and certification environment (CERT) of Sandbox.
* Privacy settings relating to profile information is also handled as global data. The same settings apply to all the environments of Sandbox.

Refer to [Profile Information](profile-information.html) for details about profile information.

## Presence Information

* The following presence information is handled as sandboxed data. During development, the current user can only obtain information pertaining to the environment of Sandbox (development environment (DEV) or certification environment (CERT)) that they are currently using.
  + `inContext` information (whether the current user and the target user are playing a game with the same NP communication ID)
  + Game title name and title icon displayed by the presence feature of the system software
* Presence information other than the above, such as a user's online state, is handled as global data. During development, the current user can obtain information of all the users in the development environment (DEV) and certification environment (CERT) of Sandbox.
* The Appear Offline setting is handled as global data. Common settings are applied to all environments of Sandbox.
* Privacy settings relating to presence information is also handled as global data. The same settings apply to all the environments of Sandbox.

Refer to "[Presence Information](presence-information.html)" for details about presence information.

## Friend List Information and Block List Information

* Friend list information and block list information are handled as global data. During development, the current user can obtain friend list information and block list information of all the users in the development environment (DEV) and certification environment (CERT) of Sandbox, and can establish friend and block relationships among all users.
* Privacy settings relating to friend list information is also handled as global data. The same settings apply to all the environments of Sandbox.

Refer to "[Friends](friends.html)" for details about friend list information and block list information.

## Push Notification

* The following Push event is handled as sandboxed data. During development, this Push event is only sent to the environment of Sandbox (development environment (DEV) or certification environment (CERT)) that the current user is currently using.
  + Presence inContext information update event
* Push events other than the above are handled as global data. During development, Push events other than the above are sent to both the development environment (DEV) and certification environment (CERT) of Sandbox.

For details, refer to the "Push Notification" chapter in [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html).

# Reference Materials

The User Profile Web API is part of the PlayStation™Network Web APIs. Refer to the following document for general topics, such as call procedures for requests, error handling, and call rate limits.

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - User Profile Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-User_Profile_WebAPI-ReleaseNotes.html)