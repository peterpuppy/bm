# User Profile Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/User_Profile-Overview/profile-information.html

# Profile Information

# Account Profile Information

Profile information that is linked to an account for PlayStation™Network includes the following.

* Real name (master account only)
* Avatar or profile picture (avatar only for sub accounts)
* About Me
* My Languages

## Privacy Settings

The user can separately set the scope of people who can view their real name and profile picture. Refer to the "[Privacy Settings](privacy-settings.html)" section of the "[Friends](friends.html)" chapter.

# Obtaining Profile Information

The following requests are provided for obtaining profile information.

* `GetPublicProfile`:

  This request obtains profile information of the user with the specified account ID. If conditions are satisfied, their real name and profile picture can also be obtained.
* `GetPublicProfiles`:

  Up to 100 account IDs can be specified and the profile information of these users can be obtained with this request. If conditions are satisfied, the users' real names and profile pictures can also be obtained.