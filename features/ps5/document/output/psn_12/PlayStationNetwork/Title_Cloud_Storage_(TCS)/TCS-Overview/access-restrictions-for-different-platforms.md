# Title Cloud Storage Service Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS-Overview/access-restrictions-for-different-platforms.html

# Using Title Cloud Storage

This topic provides the details of storage relating to the use of Title Cloud Storage, applied examples, and information about access restrictions for different platforms.

# Storage (TCS Variables/TCS Data)

The Title Cloud Storage service provides two types of storage - the "TCS variable" and the "TCS data". The TCS variable stores a signed 64-bit integer. The TCS data stores binary data.

For a single user, up to 64 TCS variables and 16 TCS data can be prepared. However, the size of a single piece of TCS data must be 4 MiB or less, and the total size of all the TCS data for a single user must be 8 MiB or less. It is necessary to have the number of TCS variables and the size and number of TCS data set in advance on the server.

The TCS variable and TCS data may be referred to as "slots". Each slot can be identified by a slot ID.

The TCS variable is accompanied by information regarding the status of the storage area. Status information includes information indicating who the owner of this storage is, the person who last updated this variable, the last update time, etc.

In addition to the above status information, the TCS data is also accompanied by "supplementary data" that can be used as index information.

Note:

If you require larger storage given the content of your title, please contact Private Support through the "Post new issue" page (<https://game.develop.playstation.net/support>).

## The "anyone" User

A special user identifier known as the "anyone" user is available to deliver common storage for all users of a given title. By using a TCS variable belonging to an "anyone" user, the total number of times that a certain game stage has been cleared by users all around the world can be counted, to give an example.

A slot for an "anyone" user must be set up in advance on the server, separate from the slots for ordinary users. For each title (more accurately, for each NP Communication ID), up to 2048 TCS variables and up to 512 pieces of TCS data can be prepared. Each piece of TCS data must be 4 MiB or less, and the total size of TCS data for the "anyone" user must be 64 MiB or less.

Note:

Updating the TCS variables and TCS data of the "anyone" user results in processing that imposes high server load. Refer to "[Limit the Frequency with Which TCS Data and Variables Concerning the "anyone" User Are Updated](notes-on-server-load-and-request-execution-rates.html#title-cloud-storage-service-overview_4_1__title-cloud-storage-service-overview_4_1_2)" before use.

Storage Provided by Title Cloud Storage

# Applied Examples of Title Cloud Storage

Examples of the title cloud storage usage are described as follows.

## Reference Counts and Voting for User Content

By preparing a TCS variable that others can write to, and using `addAndGetVariable`, you can see how many times you have been referenced.

The TCS variable of an "anyone" user can be counted up using `addAndGetVariable` to realize a vote-casting mechanism.

If you use this mechanism, however, adopt a scheme on the application side where each user's number of references or votes can be limited. For example, you might make a recording when the save data or title cloud storage is used to make a reference or to cast a vote and control the count or frequency of such operations.

Note that if you do not exercise any control at all, it could have unnatural results, such as biased voting, in addition to imposing excessive load on the server.

## Display New User Content

After a piece of user content is stored to TCS data, the date and time can be registered as a score to display pieces of user content in the order that they arrive.

Depending on the user content, however, there may need to be a process by which inappropriate content can be rejected.

## Total Number of Clears for All Users

The total number of times a game stage has been cleared in the world, for example, can be counted by counting up the TCS variable of a specific "anyone" user every time the stage is cleared, using `addAndGetVariable`.

However, the addition of a large value by even a single player due to a bug can easily corrupt the count; program your application with care. Additionally, you must implement your application in such a way that an unexpected numerical value being set to a TCS variable will not render further progress in the title impossible or cause other significant issues.

## Controlling the Access Privilege

The access privilege of a TCS variable or TCS data is set and fixed in advance. However, a specific TCS variable can be used as an application's unique access privilege flag and its operation can be determined by the application to dynamically control accesses to it. For example, the reference of a TCS data can be permitted to an opponent fought immediately before.

## Check for Game Abandonment

It is conceivable that a user might unplug the network cable or switch the power off to abandon the game without losing upon finding themselves in a disadvantageous position during online play. To check for this type of game abandonment, use `addAndGetVariable` and add 1 to their TCS variable upon game start. Subtract 1 from the same TCS variable when the game completes normally, without a sign-out occurring for example. In this way, the number of times a user has abandoned a game can be counted. Switching the power off or deleting save data can be checked in this manner as well.

However, there are cases when abnormal termination occurs contrary to the user's intention, such as because of a network problem or a power outage. Make sure that game abandonment is not immediately deemed as illegal behavior.

## Keeping Users' Best Scores

By using "greater" as the condition for a write in `setVariableWithConditions`, a user's highest score can be recorded in a TCS variable. Unlike the Leaderboards service, there is no limit placed on the number of players whose scores can be recorded, as each user's score can be stored in their respective TCS variables, and the value will immediately be reflected, but the values are not collected for analysis. Use the Title Cloud Storage service in conjunction with the Leaderboards service to complement the drawbacks of each service.

## Online Save Data

TCS data can be used as online save data. Features are provided for checking the last update time and preventing conflicts.

## Distributing Common Data/Variables to All Players

By using the Title Cloud Storage Management Web API and setting specific values or data to specific slots for the "anyone" user - either beforehand or at a predetermined time - you can distribute common data or variables to all players of a given title.

# Access Restrictions for Different Platforms

For each slot, access privileges for different platforms can be configured separately. For example, you could set up a slot that can be updated only from PlayStation®5 but that can be referenced from both PlayStation®5 and PlayStation®4. Access privilege can be configured using the Title Cloud Storage Tool.