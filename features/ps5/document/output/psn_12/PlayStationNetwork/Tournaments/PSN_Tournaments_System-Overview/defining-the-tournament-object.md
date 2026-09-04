# PlayStation™Network Tournaments System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Tournaments_System-Overview/defining-the-tournament-object.html

# Configuring Tournaments

This chapter provides information on how to add tournaments to your game.

To add tournaments to your title:

1. Request the Tournament and Universal Data System (UDS) services.
2. Define Tournament and UDS objects.
3. Download and place the configuration file.
4. Implement your tournament configuration using the Matches Web API.
5. Test and debug your tournament implementation.
6. Publish your tournament object using the GEMS tool.

For the general development process of UDS, see [Universal Data System Guide - Development Process Overview](../Universal_Data_System-Guide/development-process-overview.html).

## Publishing to NP

To publish a tournament object:

1. Use the GEMS tool to publish all linked activities. For more information, see [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html).
2. From the UDS Management tool, navigate to **Tournaments.**
3. Find the tournament you want to publish, then click **More Options**.
4. Click **Publish**.

You can publish both **In Development** and **Published** tournaments. After you publish a tournament, you can no longer edit certain properties. If any of the locked properties need updates, you must create and publish a new tournament. See [Universal Data System Guide - Reference - PlayStation™Network Object Reference](../Universal_Data_System-Guide/psn-object-reference.html) for details on the locked properties in Tournaments Objects.

You cannot unpublish published tournaments. Instead, you can make a tournament unavailable by updating its **Available To** parameter from the **Scheduling** tab, then re-publishing it.

## Downloading and Placing a Configuration File

When creating, modifying, or deleting activities, use the GEMS tool to download a new configuration file (npconfig.zip) to be bundled with your application. See [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) for more information.

When you add, modify, or delete a tournament, you do not need to download a new npconfig.zip via GEMS.

# Defining the Tournament Object

This topic provides information on how to define tournament objects.

A tournament is a PlayStation™Network object type which is tied to an existing competitive activity. For information on defining activities, see [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html).

You can use the UDS Management tool or the UDS Configuration Web API to create tournament objects after you have defined the competitive activity the tournament will link to.

The following tables refer to the information which must be provided using the UDS Management tool to create a tournament object.

Tournament Attributes

| **Field** | **Description** |
| --- | --- |
| Object Id | Object ID of the tournament. You can self-define object ID. The object ID is a string of 1 to 32 characters comprising of alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| Subcategory (optional) | An additional description line to the tournament which appears on the activity card, under the display name. Although this property is optional, it's advised to include it for user clarity. In most cases, when missing, the game name is used instead of this value. |
| Display Name | The name of the tournament. This field can be localized. |
| Game Mode (optional) | Free text description about the tournament game mode. This information appears in the detailed area of the activity card. |
| Tournament Format | The format of the tournament. Only supports `symetricSingleElimination`. |
| Activity Id | Refers to the Activity ID related to the tournament. The activity must exist before assignment. The referenced activity must be a competitive activity. |
| Zone Id (optional) | Zone ID of the tournament. The zone ID must exist before assignment. |
| Tournament Large Image (optional) | Full screen image used in promoting tournaments.  Dimension: 3840x2160 px  Image Format: PNG  24-bit non-Interlaced |
| Tournament Card Image (optional) | Image used for tournament action cards and in notifications triggered for a tournament.  Dimension: 864x1040 px  Image Format : PNG  24 bit non-Interlaced |
| Tournament Logo Image  (optional) | Image used when expanding a tournament action card.  Dimension: 944x320 px  Image Format: PNG  32 bit non-Interlaced |
| Tournament UAM Mini Image  (optional) | Image used when displaying the mini variation of the tournament action card.  Dimension: 944x260 px  Image Format: PNG  32 bit non-Interlaced |

Tournament Rules

| **Field** | **Description** |
| --- | --- |
| Minimum Number of Rounds | Controls the minimum number of players in a single bracket. Cannot be less than two rounds (i.e., four players) on NP.  One round is allowed for testing on SP-INT. |
| Maximum Number of Rounds | Controls the maximum number of players in a single bracket. Cannot be more than seven rounds (i.e., 128 players). |
| Maximum Match Length | Time, in seconds, of a tournament match. Optimum value depends on the title. The maximum value is three hours, but SIE recommends values less than one hour. |
| Waiting Expiration Time | Time, in seconds, allowed before an invitation to the match expires, which results in automatically forfeiting the match to the opponent. |
| Age | Minimum age requirements. Users who do not meet this criterion cannot register for the tournament. You must add at least one age restriction. Age requirements can be specified for all regions/countries, or on a per region/country basis. |
| Rules | Must be a .txt file, which the client renders. The client renders the following subset of HTML tags: `<b>, <br>, <div>, <em>, <font>, <i>, <p>, <span>,` and `<strong>` tags.  Supported attributes are `color` for `<font>` and `style` for other tags. Supported styles are `font-weight`, `font-style`, and `color`. You can localize rules files.  Rules files are optional during development, only if the *Rules Acceptance Required* field is set to *No*. In that case, the system supplies a temporary default rules file. If *Rules Acceptance Required* is set to *Yes*, the file must be present, even during development. For submission, the rules file is always required. |
| Rules Acceptance Required | If set to *Yes*, users must accept the defined rules before registering for a tournament. If set to *No*, rules are provided to users during registration but acceptance is not required. |

Tournament Scheduling

| **Field** | **Description** |
| --- | --- |
| Available From | Specifies when the first occurrence of the tournament is scheduled to start. |
| Available To (optional) | Specifies when the last occurrence of the tournament is scheduled. This value must be set if the `Repeatable` field is selected. |
| Availability Before Start (optional) | Time in seconds. Specifies the time a tournament occurrence is open for registration before it starts. If you do not specify this parameter, users can register as soon as the scheduler creates the tournament occurrence. |
| Repeatable | Used to create a cadence of tournament occurrences. If a tournament schedule is repeatable, you must enter additional information to allow the scheduler to schedule future occurrences. A non-repeatable tournament creates only one occurrence per tournament object. |
| Frequency (optional) | For repeatable tournaments, you must define the frequency (in seconds) of how often a new occurrence is scheduled within an active time slot. For example, a frequency of 3600 seconds generates a tournament occurrence every hour during an active time slot, or until the **Available To** date is reached, whichever occurs first. |
| Active Time Slots (optional) | Defines up to two active time slots per day. Fill in the **Start Time** (GMT) and **Duration** on a per day basis.  For example, to specify a tournament that occurs every hour from 6:00pm to 10:00pm (GMT) on Fridays and Saturdays:  Select **Repeatable** and set **Frequency** as 00:60:00 (3600 seconds). Set the Friday and Saturday time slots to 06:00pm, with a duration of 04:00:00 (14,400 seconds). |

Tournament Statistics

| **Field** | **Description** |
| --- | --- |
| Stat Name (optional) | Allows you to control who is eligible to participate in the tournament based on a previously defined game stat for the game. Only required if you want to use game stat for eligibility. |
| Comparator (optional) | Arithmetic operator used by the service to compare user stats. |
| Target Value (optional) | The value of the stat that must be met for the user to be eligible for tournament registration. For example, if a UDS "Level" game stat is maintained by the game, you can set "Level > 5" as a condition for allowing the user to register to a particular tournament. |

Tournament Rewards

| **Field** | **Description** |
| --- | --- |
| Reward Name (optional) | The name of the reward the winner of the tournament can receive. You can specify up to 10 rewards. Only required only if you want to use rewards. |
| Reward Image (optional) | A reward image displayed in the details section of the tournament action card and some notifications.  Dimension: 512x512 px  Image Format: PNG  24 bit non-Interlaced |
| Advanced Options (optional) | Used for automatic reward distribution. Selecting this allows you to enter minimum and maximum rank and SKU information for each reward. To distribute rewards, please reach out through DevNet. |

# Testing Using the Debug UI

This topic provides information on how to test tournaments using the debug UI.

Access the Debug UI from **Debug Settings > PlayStation Network > Tournaments**. The Debug UI shows you tournament objects and occurrences. From each occurrence, you can view registration, bracket, and result details. The Debug UI does not refresh automatically. If another user makes changes to a tournament object or occurrence, this may not be reflected on your UI. Use **Refresh**to update the UI with the latest changes.

## Tournament Object Screen

The tournaments screen shows you tournament objects and occurrences you've defined for this title.

An occurrence can be in one of five phases:

* `SCHEDULED` - Automatically created by the system when a tournament object has a defined schedule. Not relevant for debugging.
* `OPEN` - Occurrences transition to `OPEN` before the tournament starts, as determined by **Availability Before Start**. When an occurrence is `OPEN`, users can begin registering. If you do not set **Availability Before Start**, occurrences transition to `OPEN` as soon as the scheduler creates them, skipping the `SCHEDULED` phase.
* `STARTED` - The tournament begins, and the system begins creating brackets.
* `ENDED` - The tournament is over. For example, all brackets are complete for that occurrence and a winner has been declared.
* `CANCELED` - In some cases, the system may cancel a tournament. Users receive a notification, indicating the reason for the cancellation. See [Tournament Canceled](notifications.html#psn-tournaments-system-overview_2_2__psn-tournaments-system-overview_2_2_8) for details regarding the different conditions under which this may happen.

To create a new tournament occurrence:

1. Click **Create New Occurrence** for the selected tournament object. Once you create a tournament occurrence, it becomes `OPEN`, meaning players can register.
2. Set a value for **Automatically Start** to define whether you want the system to start the occurrence automatically, or sometime after creating the occurrence.
3. Select the occurrence to proceed to the **Tournament Occurrence**screen.

## Tournament Occurrence Screen

For each tournament occurrence, you can view **Registration**, **Brackets**, and **Results**. Use these tabs to manage and view the occurrence's phases and monitor their progression.

## Brackets

By default, the brackets tab shows the current logged-in user's tournament occurrence. Use the drop-down list to view other tournament brackets currently in progress. Use **Refresh** to see the latest bracket information, including current match status, if applicable.

The Tournament service creates brackets based on the tournament's object parameters and the number of players registered when the tournament beings. Each player is allocated a match with a registered opponent and must join and play to advance in the bracket. If players do not join the match on time, they forfeit the match and are retired from the tournament.

Only the logged-in user can join a match using **Join Now**, and only when there is a match ready for them at that time. Other registered players can join matches from their own accounts.

**Forfeit** allows the logged-in user to forfeit their match, granting their opponent a win and advancement through the bracket. This also causes the logged-in user to retire from the tournament.

## Results

The results tab shows the placements of all players in the bracket for a particular tournament occurrence.