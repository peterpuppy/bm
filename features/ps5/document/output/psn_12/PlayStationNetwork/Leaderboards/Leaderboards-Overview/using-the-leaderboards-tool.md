# Leaderboards Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards-Overview/using-the-leaderboards-tool.html

# Using the Service

This topic explains how to use the Leaderboards service. The standard development process, web tools for configuring and managing leaderboards, processing procedures for obtaining rankings and registering scores in games, notifications to users when errors occur, how to use the service on application servers, etc., are covered.

# Overview of the Development Process

The standard process for using the Leaderboards service is as follows.

1. **Applying for the service**

   You can use the Leaderboards service by applying to use it on the Developer Network website (<https://partners.playstation.net/>) (DevNet). After applying for the service, you will be able to acquire an ID and various data required for development.
2. **Developing**

   Use the NpWebApi2 library and NpCppWebApi library—while referring to references, sample code, and so forth as required—to develop an application that uses the Leaderboards service.

   You can use the Leaderboards Tool for setting up the leaderboards that will be used, creating test data, and for other such uses.

   Use the Leaderboards Management Web API to perform actions such as deleting the score of an arbitrary user.
3. **Testing**

   Perform tests by using the Leaderboards Tool and the Leaderboards Management Web API as appropriate.
4. **Submission (submission of the package, applying for QA, etc.)**

   Submit the developed application to SIE.

# Using the Leaderboards Tool

The Leaderboards Tool is a web tool that can be accessed from DevNet using a DevNet account with appropriately set permissions.

With the Leaderboards Tool, you can configure the service, configure each leaderboard, reset recorded scores and data, generate scores for testing, promote settings from the development environment (DEV or sp-int) to the production environment (RETAIL), set the ranking snapshot output and score reset schedules, and so forth.

Note:

About the service state switcher in the Sandbox network architecture:

* The service state switcher will be displayed for titles that have been migrated to the PlayStation® environments of the Sandbox network architecture. The descriptions provided in the subsequent chapters are for when "Published to DEV" is specified as the service state. Refer to [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html) for details about the service states.

Note:

Correspondence Table of Environment Names

| Legacy network architecture | | Sandbox network architecture |
| --- | --- | --- |
| Environment name displayed in the tool | Environment name | Environment name and the environment name displayed in the tool |
| Development | sp-int | DEV |
| QA | prod-qa | CERT |
| Production | RETAIL | RETAIL |

## Configuring Leaderboards

For example, suppose leaderboards are created as follows.

* Leaderboard for North America (Board ID: 0)
* Leaderboard for Japan (Board ID: 1)
* Leaderboard for round 1 (Board ID: 2)
* Global leaderboard (Board ID: 3)

Setting Up a Leaderboard with the Leaderboards Tool

After setting up the various parameters shown below for each Board ID, select "Send to Server" from the Actions menu to have the set values applied to the development environment (DEV or sp-int) server.

Configurable Leaderboard Parameters

| **Parameter Name** | **Description** |
| --- | --- |
| Board ID | ID for each leaderboard |
| Entry Limit | Maximum number of entries that can be recorded on the leaderboard |
| Update Mode | Switch for the behavior when recording scores  Always overwrite, or only overwrite when there is a new high score |
| Sort Mode | Switch between sorting scores in ascending (ASC) and descending order (DESC)  In descending order (DESC), 100 is a better score than 1. In ascending order (ASC), 1 is a better score than 100. |
| Score Limit | The range of scores that can be recorded on the leaderboard |
| Large Data Num Limit | Minimum rank for which large-volume attachment data can be recorded and attached to a score |
| Large Data Size Limit | Maximum size (bytes) for one large-volume attachment data |
| Shares To | Share-destination leaderboard ID for sharing scores with another leaderboard |
| Comment | Arbitrary comment (corresponds to the string that is displayed on the line under parameters such as the board ID: "North America", for example). If an arbitrary comment is attached, a checking and masking process will be executed on the comment string, which may cause variation in the time it takes for the recorded score to be reflected in the rankings. When using small-volume attachment data, these processes are not executed, so there is no variation in the time taken for them to be reflected. |

Shares To is a feature that automatically records scores that are recorded on a certain leaderboard on another leaderboard. For example, as shown in [Setting Up a Leaderboard with the Leaderboards Tool](using-the-leaderboards-tool.html#leaderboards-overview_2_2__e2d77f3c-576f-11ee-8c99-0242ac120002), it is possible to set it up so that updates to regional rankings (North America (Board ID: 0), Japan (Board ID: 1)) are reflected in the global rankings (Global (Board ID: 3)) automatically. The application can define leaderboard relationships in this manner and comprehensively manage the results of multiple leaderboards.

The following operations can be performed using the Actions menu on the Leaderboards Definitions screen:

* When you select Edit, you can create, modify, or delete a leaderboard.
* When you select Import/Export, you can batch-import/export settings values in JSON format. When you perform an import, the Revision number will rise even for a leaderboard that has had no changes.
* When you select Send to Server, you can apply the leaderboard settings of your choosing to the development environment (DEV or sp-int) server.
* By selecting "Publish to CERT and RETAIL" or "Publish" from the Action menu, you can apply the leaderboard settings of your choosing from the development environment (DEV or sp-int) to both the certification environment (CERT or prod-qa) and production environment (RETAIL) at once. Always publish the leaderboard settings before making use of the certification environment (CERT or prod-qa) and production environment (RETAIL). Failing to publish the settings may cause the service to function incorrectly.

Only the leaderboard settings are promoted. The scores recorded in a leaderboard are not promoted.

Leaderboard settings in the development environment (DEV or sp-int) can be deleted or modified if the feature for promoting settings has not yet been run. Once leaderboard settings have been promoted, their Lock Status changes from Unlocked to Locked, and you will no longer be able to delete or modify them. Updates through the Import feature will also be skipped for any leaderboard whose status is Locked. However, leaderboard settings can be deleted or modified even if the Lock Status is Locked for titles that have been migrated to the PlayStation® environments of the Sandbox network architecture.

The time "Last Updated" displayed on the Leaderboards Definitions screen is the update time for the leaderboard settings/ It is not the time when the latest score was recorded, nor is it the time when rankings were tabulated.

Note:

It is not possible to change a Lock Status to Unlocked using the Leaderboards Tool. Contact SIE if you would like to modify or delete leaderboard settings after they have been promoted.

Before modifying leaderboard settings, first reset that leaderboard and delete all score data contained therein. Normal operation is not guaranteed if settings are modified without deleting the score data.

However, when the Entry Limit setting is changed, there is no need to delete the score data and existing scores can be used as-is.

## Setting Up Services

Manage Service Configuration can be used to set up service availability times and temporarily suspend the service for maintenance.

Setting Up Services with the Leaderboards Tool

Having set the various service parameters below via Edit in the Actions menu on the Service Configuration screen, you can then select Update Service Configuration to reflect the values for the parameters onto the specified environment's server.

Configurable Service Parameters

| **Parameter Name** | **Description** |
| --- | --- |
| Service Period - Begin | The date and time when the service period begins |
| Service Period - End | The date and time when the service period ends |
| Maintenance Mode | Toggle the service between maintenance and in-use mode |

It is essential that services are configured for each environment. Services will not operate correctly if they have not been configured, even if leaderboard settings have been applied across each environment.

## Configuring Ranking Snapshot Output Schedules

Use Manage Snapshots to set up ranking backups or browse the ranking history.

Setting Up Ranking Snapshot Schedules with the Leaderboards Tool

Having set up the various snapshot schedule parameters below on the Manage Snapshot Schedules screen, you can then use Create Schedule/Update Schedule to reflect the configured values for the parameters onto the specified environment's server. Ranking snapshots are generated asynchronously when the conditions based on the configured values are satisfied and can be downloaded in a compressed file format.

Configurable Ranking Snapshot Schedule Parameters

| **Parameter Name** | **Description** |
| --- | --- |
| Name | Arbitrary name |
| Board ID | ID of leaderboard to snapshot |
| Description | Arbitrary description (e.g., usage) |
| Recurring Type | Toggle replication behavior  Either recurring or one-shot |
| Date Time | The snapshot output date and time |
| From | The start date/time if the replication behavior is set to recur |
| To | The end date/time if the replication behavior is set to recur |
| File Format | Switch the file format  JSON or CSV |
| Enabled | Toggle the snapshot between enabled and disabled |

Snapshot schedules can be set up for the development environment (sp-int) and production environment (RETAIL). Up to ten schedules can be set up in each environment. To create a new schedule when the maximum has already been set, you must either delete or disable an existing schedule. You can see a list of snapshot output results on the View Snapshots screen.

## Score Reset Schedule Settings

Use Manage Reset to make use of time-limited rankings.

Setting Up a Score Reset Schedule with the Leaderboards Tool

Having set up the various score reset schedule parameters below on the Manage Reset Schedules screen, you can then use Create Schedule/Update Schedule to reflect the configured values for parameters active onto the specified environment's server. Under normal circumstances, the score reset is completed immediately when the conditions based on the configured values are met.

Configurable Score Reset Schedule Parameters

| **Parameter Name** | **Description** |
| --- | --- |
| Name | Arbitrary name |
| Board ID | ID of leaderboard to reset |
| Description | Arbitrary description (e.g., usage) |
| Recurring Type | Toggle replication behavior  Either recurring or one-shot |
| Create Snapshot | Toggle whether or not a snapshot of the leaderboard is output just prior to the reset |
| File Format | Select the snapshot output format if a snapshot is configured to occur just prior to the reset  JSON or CSV |
| Date Time | The score reset date and time |
| From | The start date/time if the replication behavior is set to recur |
| To | The end date/time if the replication behavior is set to recur |
| Enabled | Toggle the snapshot between enabled and disabled |

Score reset schedules can be set up for the development environment (sp-int) and production environment (RETAIL). Within each environment, up to 10 schedules can be created if Create Snapshot is set to True. If that setting is not set to True, an unlimited number of schedules can be created. To create a new schedule with Create Snapshot: True when the maximum has already been set, you must either delete an existing schedule or disable the create snapshot setting. You can see a list of past score resets on the View Reset Histories screen. You can see a list of snapshot output results on the View Snapshots screen.

## Creating Scores for Testing

Scores can be created from the tool for testing purposes.

Record multiple scores Menu Screen

From the View Data menu, select the Record scores menu that appears by clicking on the vertical three-point dotted line on the right edge of the Custom board for which you want to create a score. The Record multiple scores screen will be displayed, so enter the required information as shown in [Record multiple scores Menu Screen](using-the-leaderboards-tool.html#leaderboards-overview_2_2__image_ddz_vdw_qzb) to create a score.

Note that the above method cannot be used to create test scores for AutoGen boards.

## Operational History

The Leaderboards Tool keeps audit logs and operational history. By clicking the [Operational History] tab, you can check the changes that have been made to a service with a particular NP communication ID.

[Operational History] Tab

There are multiple data items in the operational history list view, and these items can be sorted by each column. The data items included in the list view are provided below:

* **Date and Time** - The date and time that the operation was performed
* **Log Level** - The log level (INFO, WARN, or ERROR)
* **Actor** - The name of the person who performed the operation
* **Action** - The operation that was performed
* **Target** - The item on which the operation was performed
* **Status** - The state of progress of the operation
* **Summary** - A simple description of the operation that was performed

Logs of operations can also be displayed in JSON format. In the JSON format view, information is displayed when you click the blue arrows displayed on each row.

Operational History

## Feature Differences before and after Title Migration to the PlayStation® Environments of the Sandbox Network Architecture

|  | **Before title migration** | **After title migration** |
| --- | --- | --- |
| Deletion and modification of the leaderboard settings when the Lock Status is Locked | Not possible | Possible |

# Ranking Obtainment Processing

## Obtain Rankings through Rank Specification

Using `getRanking`, provided by the Leaderboards service, ranking information currently recorded on the leaderboard for a range specified as a certain number of ranks from a given rank can be obtained. Use `startSerialRank` to specify the first rank you would like to obtain (if omitted, defaulting to 1) and use `offset` and `limit` for paging.

Obtaining Rankings through Rank Specification

To lighten the server load, only obtain ranking information for the required range. (A detailed explanation is provided in the "[Notes Regarding Server Load and Request Frequency](notes-regarding-server-load-and-request-frequency.html)" section.)

Note that when a score is recorded from another console while multiple pages are being obtained, the rankings on multiple pages may become misaligned.

## Obtain Rankings of Specific Users

By using `getRanking`, you can obtain ranking information that only includes specific users, as described in the bullet items below.

* `group=friends` (ranking information that only includes friends of the current user)
* `users=`account ID (ranking information that only includes the specified user)
* `users=me` (ranking information that only includes the current user)

If a user is specified with `group=friends`, only the score for player character ID = 0 will be obtained, even if scores corresponding to multiple player character IDs are recorded on the leaderboard. Player character IDs can also be specified when users are specified with `users`.

Note that `group` and `users` can be specified at the same time, but this may adversely affect the latency of obtaining information.

## Obtain Rankings Centered around the Specified User

By using `getRanking`, you can obtain ranking information centered around the specified user, including the ranking of that user and the rankings above and below them. Specify the user to center around using `userCenteredAround`. (It's also possible to specify the current user using `userCenteredAround=me`.) Centered around the specified user's ranking, specify the number of scores above and below that ranking to obtain using `centerToEdgeLimit`.

Obtaining Rankings Centered around the Specified User

Ranking information can also be obtained by combining usage with `group=friends`. In this case, among the current user's friends' rankings, ranking information will be obtained within the range of `centerToEdgeLimit` above and below the ranking of the user specified in `userCenteredAround`.

## Obtain Attachment Data

There are two types of attachment data available for use: small-volume attachment data and large-volume attachment data. The maximum size of small-volume attachment data is small but, because it can be obtained along with score information, multiple instances can be obtained with a single Web API call. Meanwhile, the downside of the large maximum size for large-volume attachment data is that it must be obtained separately from score information, with one Web API call for each instance.

If large-volume attachment data has been added to a score recorded on a leaderboard, object ID information, which is the ID for the large-volume attachment data, is returned along with the score information. The large-volume attachment data can be obtained by using `getLargeDataByObjectId` with that object ID as a parameter. When doing so, features such as Range and If-Match that are available with ordinary HTTP GET calls can be used.

| **Category** | **Method of Obtaining** | **Maximum Size** | **Server Load** |
| --- | --- | --- | --- |
| Small-volume attachment data | Can be obtained along with scores | 189 bytes or less | Low |
| Large-volume attachment data | Must be obtained separately | 1 MiB per instance/1 GiB or less in total (based on settings) | High |

# Score Recording Processing

## Score Recording

Scores can be recorded using `recordScore`. Optionally, you can record comments and small-volume attachment data at the same time. A temporary rank is obtained when a score is recorded. Carry out appropriate processing - such as displaying it on the screen.

Note:

The content of the comment string specified upon registering a score will be checked on the server side; if any inappropriate words are included, they will be masked automatically. If more is required, you can use the Profanity Filter Web API to explicitly perform checking and masking.

The official ranking of the scores will not be calculated or made public until checking and masking of the comment is complete. Although the official ranking is calculated at the point when any comment has finished being checked and masked, that calculation will be based on the time when the score finished being recorded, not on the time when the comment is finished being checked and masked; official rankings calculated on this basis are what are included in the results when rankings are obtained.

## Recording of Large-Volume Attachment Data

If the temporary ranking obtained when recording a score is within the range for which large-volume attachment data can be recorded, `recordLargeData` can be used to record large-volume attachment data.

Additionally, scores and large-volume attachment data can be recorded atomically using the X-Psn-Atomic-Operation header. In that case, the procedure is as follows:

1. When using `recordScore` to record the score, specify the request header `X-Psn-Atomic-Operation: begin`.
2. If the request succeeds, an ID for managing an atomic recording session is issued, and the response header `X-Psn-Atomic-Operation-Id: {UUID}` is returned.
3. When using `recordLargeData` to record large-volume attachment data, the processing will occur atomically along with the recording of the score if an `X-Psn-Atomic-Operation-Id: {UUID}` header is specified.
4. When making the final request, specify an `X-Psn-Atomic-Operation: end` header in addition to the `X-Psn-Atomic-Operation-Id: {UUID}` header to end the atomic recording operation.

# Error Notification

Notify users of Leaderboards service errors in an appropriate manner. Especially in cases where the error greatly affects the user, such as when failing to record a record-breaking score, we strongly recommend that the user be notified of the error.

The user does not need to be notified of errors that are not fatal (for example, an error that occurs when attempting to record a score that is not a personal best onto a leaderboard for which scores are only recorded when one's best score is updated). In this case, however, it is recommended to locally check if the user's best score has been updated before attempting to record the score in order to lighten the server load.

Also make sure to handle errors returned when the Leaderboards service period ends ("Service Unavailable") in an appropriate manner. Be especially careful with applications that frequently switch between using and not using the Leaderboards service so that a problem doesn't occur when the service period ends.

# Obtaining Ranking Information with Application Servers

`getRanking`/`getLargeDataByObjectId` can be used from application servers. Expected use cases include posting users' scores, ranking data, and uploaded attachment data on fan sites and using those data with application servers.