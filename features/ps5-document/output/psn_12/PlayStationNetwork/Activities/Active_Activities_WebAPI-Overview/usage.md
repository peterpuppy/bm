# Active Activities Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Active_Activities_WebAPI-Overview/usage.html

# Usage

Typical usage of the Active Activities Web API is described below.

# Retrieving Activity Information

Use `GetUserActivities` to obtain the activities that are being played by target users by specifying their account IDs.

Activities can be obtained when each target user satisfies the following conditions.

* The target user is playing the same game
* The target user has the Appear Offline setting disabled
* Presence information of the target user is available to the current user (the user who called `GetUserActivities`)
* The target user's privacy setting ("Hide your games from other players") is disabled for the specified game

When obtaining the activities of friends who are playing the same game, first obtain their account IDs through the process described below:

* Obtain the current user's friend list using `GetFriends` from the User Profile Web API
* Obtain presence information for each user included in the obtained friend list using `GetBasicPresences` from the User Profile Web API
* Identify the accounts of users who are playing the same game as the current user from the obtained presence information

For details about the User Profile Web API, refer to the [User Profile Overview](../User_Profile-Overview/__document_toc.html) and [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html) documents.

## Activity Information Retrieved from GetUserActivities

The activity information that can be obtained with `GetUserActivities` consists of the following items:

* Activity ID: This is a unique ID set by the developer that is used to identify activities.
* Activity name: This is the name of the activity set by the developer. One activity name corresponding to the language specified with an Accept-Language request header will be obtained.
* hidden flag: This is the hidden flag set for the activity. Whether to apply the Spoiler flag must be considered if this flag is true.
* Match ID: This is returned only if the activity is linked to a match. Detailed information about the match can be obtained using this ID.

For details about activities, refer to the [PlayStation™Network Activities Guide](../../../SDK/latest/PSN_Activities-Guide/__document_toc.html) document; for details about matches, refer to the [Matches Web API Overview](../Matches_WebAPI-Overview/__document_toc.html) document.

## Activities Returned from GetUserActivities

`GetUserActivities` only returns activities if they are in the *Started* (for single player activities) or *Active* (for multiplayer activities) states.

Single player activities are in the *Started* state when:

* `activityStart` or `activityResume` was the most recent UDS event for the activity.
* `activityStart` or `activityEnd` was the most recent UDS event sent for any child task or sub-task, but not the parent activity.

Note: Activities are not returned if the most recent UDS event received is `activityTerminate`, `activityEnd(outcome: completed)`, `activityEnd(outcome: failed)`, `activityEnd(outcome: abandoned)`, or `activityEnd(no outcome defined)`.

Multiplayer activities are in the *Active* state when a match has been created using the Matches Web API and the match is in the WAITING, PLAYING or ON HOLD status. For more information on match statuses, see [Matches Web API Overview - Overview and the Main Properties of Matches - Match Status (status)](../Matches_WebAPI-Overview/match-status-status.html).

Note: Matches in the *CANCELLED* and *COMPLETED* statuses are not returned.