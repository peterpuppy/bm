# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/uds-event-reference.html

# Reference

This chapter contains reference information such as PlayStation™Network object attribute
descriptions and UDS event property descriptions.

# PlayStation™Network Object Reference

This topic contains PlayStation™Network object names and attribute
descriptions.

## Activity

The following table describes PlayStation™Network object attributes.

PlayStation™Network Object Attributes

| **Attribute** | **Localization** | **Editable when Lock Status is "Locked"** | **Editable when 　Lock Status is "Partially Unlocked"** | **Description** |
| --- | --- | --- | --- | --- |
| object id | N/A | No | No | Object ID of activity. The partner can self-define object ID. The object ID is a string of 1 to 32 characters comprising alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| type | N/A | No | No | The type of activity.   * activity * task * subTask |
| category | N/A | No | No | The category of activity.   * progress * openEnded * competitive * challenge |
| subcategory | Yes | No | Yes | The subcategory of activity. This is used for classifying activities. |
| name | Yes | Yes | Yes | The name of activity.  Note: If `type` is `subTask`, this attribute is `optional`. |
| description | Yes | Yes | Yes | The description of activity. |
| images | N/A | Yes | Yes | The image of activity. Three types of images can be set.   * activity large image    + Dimension : 3840x2160 px * activity card image    + Dimension : 864x1040 px * mini activity card image    + Dimension : 944x332 px   Image Format : PNG, 24 bit non-interlaced |
| available by default | N/A | Yes | Yes | Whether or not to make the activity available to the user without explicitly changing the setting to available. |
| Is required for completion | N/A | Yes | Yes | Whether or not the player must complete the activity to complete the main story. Note: If `category` is `openEnded` or `challenge`, this attribute must be `false`. |
| rewards | N/A | No | Yes | Reward that the player can obtain when the activity is completed. Up to 10 rewards can be specified. |
| name | Yes | Yes | Yes | The name of reward. |
| images | N/A | Yes | Yes | The image of reward.  Dimension : 512x512 px  Image Format : PNG, 32 bit or 24 bit non-interlaced. |
| hidden | N/A | Yes | Yes | **Discontinued**. This property is no longer used.  Whether or not the activity is a target for spoiler block.  The activity is a target for Spoiler Block when TRUE is set. |
| available from | N/A | Yes | Yes | Date and time when the activity becomes available. |
| available until | N/A | Yes | Yes | Date and time when the activity becomes unavailable. |
| Is online multiplay | N/A | No | No | Whether or not the activity supports online multi-play. |
| supported platforms | N/A | No | Yes | Select from the following:   * PS5 * PS4  Note: Cannot be set if `numberOfPlayers` is   1 or `isOnlineMultiplay` is   false.   Only the following combinations are allowed:   * PS5 only * PS5 and PS4 |
| number of players | N/A | No | Yes | Number of players that can join the activity together as a single group.  **Example:**  Imagine a game where 4 users can join up together in a lobby and queue to play in a game mode with a max of 64 players. That game mode's activity would have the following configuration:   * Number of players: 4 * Number of total players: 64 |
| number of total players | N/A | No | Yes | Total number of players that can play the activity at the same time.  **Example:**  Imagine a game where 4 users can join up together in a lobby and queue to play in a game mode with a max of 64 players. That game mode's activity would have the following configuration:   * Number of players: 4 * Number of total players: 64 |
| Is team activity | N/A | No | Yes | Whether the activity (used in matches) is a team activity or a single player activity. |
| score statistic | N/A | No | Yes | The score statistic is displayed in system UI in order to report the progress of Match and also report the final score of Challenge.  Note: Once the locked status is locked, it can not be added/deleted. |
| name | Yes | Yes | Yes | The name of the score statistic. |
| display format | N/A | No | Yes | The format of score. Select from the following:   * time * numeric |
| decimal places | N/A | Yes | Yes | Number of digits after decimal. Select from the following:   * 0 * 1 * 2 * 3  Note: the default value is 0 and the value can be set when   "`displayFormat`" is "numeric". |
| sort | N/A | No | Yes | Sort options to display in the chart.   * asc (ascending order) * desc (descending order)  Note: "Ascending" should be used when smaller values   indicate better performances, and "Descending"   should be used when larger values indicate better   performances.  If the “category” is “challenge”, this is   non-editable even if the locked status is “Partially   Unlocked”. |
| additional statistics | N/A | No | No | The additional statistics is displayed in System UI in order to report the additional statistics that are relevant to the activity. Up to 4 additional statistics can be specified.  Note: Once the locked status is locked, it can not be added/deleted. |
| name | Yes | Yes | Yes | The name of additional score statistic. |
| stats key | N/A | No | No | The identifier which is used in Matches API to report an additional statistic. |
| leaderboard | N/A | N/A | N/A | The leaderboard for Activity Challenge. |
| board id | N/A | No | No | The board ID for the activity. The board ID is issued by the system when an activity (category : challenge) is created. |
| default playtime estimate | Integer | Yes | Yes | The default playtime estimate is displayed in System UI when the system has not determined the estimated playtime. Once the system determines the estimated playtime, the value may be switched over from the default playtime that is specified. You can specify the time in minute at the activity, task and subtask level.   * When the category is not "challenge", allow the value at   5-minute intervals. (e.g. 5, 10, 15); * When the category is "challenge", allow the value at   1-minute intervals (e.g. 1, 2, 3); * When the type is "task" or "subTask", allow the value at   1-minute intervals (e.g. 1, 2, 3). |
| challenge | N/A | N/A | N/A | The configuration for the challenge activities. |
| personal best notification only | N/A | Yes | Yes | The notification setting for the challenge activities. When TRUE is set, the pop-up notification is displayed only if the player beats their best score. |
| enable global cohort | N/A | Yes | Yes | Enable the global cohort for the challenge leaderboards. When FALSE is set, players can only see the challenge leaderboards for their friend |
| game intent type | N/A | Yes | Yes | **Discontinued**. This property is no longer used.  The configuration is for Game Intent. There are two types.   * minimal * standard |
| support non-PSN players | N/A | No | Yes | Determines whether the activity allows non-PSN players to join the player session. |
| is collectable | N/A | No | Yes | Determines whether the activity is collectable. |

## Actor

The following table describes actor attributes.

Actor Attributes

| **Attribute** | **Localization** | **Editable when Lock Status is "Locked"** | **Editable when Lock Status is "Partially Unlocked"** | **Description** |
| --- | --- | --- | --- | --- |
| object id | N/A | No | No | Object ID of actor. The partner can self-define object ID. The object ID is a string of 1 to 32 characters comprising alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| name | Yes | Yes | Yes | The name of actor. |
| images | N/A | Yes | Yes | The image of actor. It's displayed in System UI.  Dimension : 512 x 512 px.  Image Format : PNG, 32 bit or 24 bit non-Interlaced. |
| hidden | N/A | Yes | Yes | **Discontinued**. This property is no longer used.  Whether or not the activity is a target for spoiler block.  The activity is a target for Spoiler Block when TRUE is set. |

## Mechanic

The following table describes mechanic attributes.

Mechanic Attributes

| **Attribute** | **Localization** | **Editable when Lock Status is "Locked"** | **Editable when Lock Status is "Partially Unlocked"** | **Description** |
| --- | --- | --- | --- | --- |
| object id | N/A | No | No | Object ID of mechanic. The partner can self-define object ID. The object ID is a string of 1 to 32 characters comprising alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| name | Yes | Yes | Yes | The name of mechanic. |
| images | N/A | Yes | Yes | The image of mechanic. It's displayed in System UI.  Dimension : 512 x 512 px.  Image Format : PNG, 32 bit or 24 bit non-Interlaced. |
| hidden | N/A | Yes | Yes | **Discontinued**. This property is no longer used.  Whether or not the activity is a target for spoiler block.  The activity is a target for Spoiler Block when TRUE is set. |

## Zone

The following table describes zone attributes.

Zone Attributes

| **Attribute** | **Localization** | **Editable when Lock Status is "Locked"** | **Editable when Lock Status is "Partially Unlocked"** | **Description** |
| --- | --- | --- | --- | --- |
| object id | N/A | No | No | Object ID of zone. The partner can self-define object ID. The object ID is a string of 1 to 32 characters comprising alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| name | Yes | Yes | Yes | The name of zone. |
| images | N/A | Yes | Yes | The image of zone. It's displayed in System UI.  Dimension : 864 x 1040 px.  Image Format : PNG, 24 bit non-Interlaced. |
| map images | N/A | Yes | Yes | Map Image which is used for location help on Game Help.  Dimension : 3840 x 2160 px.  Image Format : PNG, 24 bit non-Interlaced. |
| hidden | N/A | Yes | Yes | **Discontinued**. This property is no longer used.  Whether or not the activity is a target for spoiler block.  The activity is a target for Spoiler Block when TRUE is set. |

## Tournament

The following table describes tournament attributes.

| Attribute | Localization | Editable when Lock Status is "Locked" | Editable when Lock Status is "Partially Unlocked" | Description |
| --- | --- | --- | --- | --- |
| object id | N/A | N/A | No | Object ID of tournament. The partner can self-define object ID. The object ID is a string of 1 to 32 characters comprising alphanumeric characters with an "\_" (underscore) and a "-" (hyphen). Names starting with an "\_" (underscore) are reserved for the system and cannot be used. |
| tournament format | N/A | N/A | No | The format of the tournament. Only "symmetricSingleElimination" is supported in this release. |
| name | Yes | N/A | Yes | The name of the tournament. |
| rules | Yes | N/A | Yes | The rules of the tournament.  Note: The system sets `default rule` if user doesn’t set any rules. However, the system doesn't allow use to publish a tournament object with `default rule`. Need to set by yourself. |
| is required rule acceptance | N/A | N/A | Yes | Determines whether accepting tournament rules is required for a player to register for the tournament. |
| images | N/A | N/A | Yes | The image of tournament. Four types of images can be set.   * tournament large image    + Dimension : 3840x2160 px * tournament card image    + Dimension : 864x1040 px * tournament logo image    + Dimension: 944x320 px * mini tournament card image    + Dimension : 944x332 px   Image Format : PNG, 24 bit non-interlaced |
| activity id | N/A | N/A | No | The object ID of the associated activity.  Note: The category of the specified activity must be `competitive`.  Note: When `isTeamTournament` is `true`, `isTeamActivity` on the specified activity must be set to `true`. When `isTeamTournament` is `false`, `isTeamActivity` on the specified activity must be set to `false`.  Note: The status of the activity must be `formatQaCompleted` or `inProduction` for submission. |
| zone id | N/A | N/A | No | The object ID of the associated zone.  Note: The status of the zone have to be `formatQaCompleted` or `inProduction` for submission. |
| minimum number of rounds | N/A | N/A | No | The minimum number of rounds. You can specify up to 6 and cannot be less than 1. Note: Must be greater than or equal to 2 in order to publish. |
| maximum number of rounds | N/A | N/A | No | The maximum number of rounds. You can specify up to 7 and cannot be less than 3.  Note: Must be greater than the `minimum number of rounds`. |
| maximum match length | N/A | N/A | No | The maximum length of the match. You can specify the time in seconds. The maximum is 3 hours (10,800 seconds), but less than one hour (3,600 seconds) is recommended.  Note: Cannot be less than 60. |
| waiting expiration time | N/A | N/A | No | The time allowed before an invitation to the match expires, which results in automatically forfeiting the match to the opponent. You can specify the time in seconds. The maximum is 3 hours (10,800 seconds).  Note: Cannot be less than 60. |
| repeatable | N/A | N/A | Yes | Whether the tournament is repeatable or one-off. |
| available from | N/A | N/A | Yes | Date and time when the tournament becomes available. |
| available until | N/A | N/A | Yes | Date and time when the tournament becomes unavailable.  Note: When `repeatable` is `true`, `available until` is required.  When `repeatable` is `false`, `available until` must not be set. |
| country age requirements | N/A | N/A | No | Only accounts that are from the specified country/region and that meet the minimum age are allowed to play in the tournament.   * country    + Country/region of residence of the player. Value is     the two-letter uppercase country code as defined in     ISO 3166-1 alpha-2. * age    + The minimum age for players from this country/region     to play in the tournament. The minimum value is     0. Note: The tournament must define at least one country age   requirement. |
| rewards | N/A | N/A | No | Reward that the player can obtain when they complete the tournament. Up to 10 rewards can be specified. |
| name | Yes | N/A | No | The name of the reward. |
| images | N/A | N/A | No | The image for the reward.  Dimensions: 512x512 px  Image format: PNG, 32 bit or 24 bit, non-interlaced. |
| minimum rank | N/A | N/A | No | The minimum rank of qualifying to earn this reward.  The player must get at least this rank or higher in the tournament.  This value must be less than or equal to `maximum rank`. |
| maximum rank | N/A | N/A | No | The maximum rank of qualifying to earn this reward.  The player must get at most this rank or lower in the tournament.  This value must be greater than or equal to `minimum rank`. |
| skus | N/A | N/A | No | This attribute support to configure multiple `skuIds`.  Note: If no `skuIds`, this reward is given manually (not automated).  If both `minimum rank` and `maximum rank` are not configured, all ranked players can get the reward. |
| stat requirements | N/A | N/A | No | Qualifying criteria that players must meet to be eligible for the tournament. Up to 10 requirements can be specified.  `uds stat name`: Specifies the name of the stat. The stat must have either `formatQaCompleted` or `inProduction` status.  `comparator`: Specifies how the player's stat value should be compared to the target value. Can specify `ge`, `gt`, `le` and `lt`.  `target value`: The target value of the comparison. |
| availability before start | N/A | N/A | No | The time is visible to players and enables them to register the match. You can specify the time in seconds. The maximum is 2 weeks (1,209,600 seconds).  Note: Cannot be less than 60. |
| active time slots | N/A | N/A | Yes | The active time slots for multiple occurrences per tournament. You can specify the duration and day of the week.  Note: Maximum of 2 slots can be set per day. Time format is HH:MMZ.  Note: Duration is up to 24 hours (86,400 seconds). Cannot be less than 60 seconds. |
| frequency | N/A | N/A | Yes | The frequency allows how often the tournament occurs during an active time slot. You can specify the time in seconds. The maximum is 24 hours (86,400 seconds).  Note: Cannot be less than 900. When `repeatable` is `true`, `frequency` is required. When `repeatable` is `false`, not allowed to be set. |
| subcategory for tournament | N/A | N/A | No | The subcategory of the tournament. This is used for classifying tournaments. |
| game mode | Yes | N/A | Yes | The game mode of the tournament. |
| is team tournament | N/A | N/A | N/A | Specifies whether the tournament is “Team vs. Team” or not. |
| team size | N/A | N/A | N/A | Defines how many players can play on the same team together.  Team sizes must be at least two players, and no more than 12.  Note: When `isTeamTournament` is set to `true`, `teamSize` is required. |

# UDS Event Reference

This topic contains UDS event names and property descriptions.

## activityStart

The event indicates that the player started an activity. The following table describes
`activityStart` properties.

activityStart Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `activityId` | No | string | Yes | Specifies the object ID of activity when the player starts. |
| `primaryActor` | No | string | No | Specifies the object ID of actor (primary actor). |
| `secondaryActors` | Yes | string | No | Specifies the list of object IDs of actor (secondary actor). |
| `equippedMechanics` | Yes | string | No | Specifies the list of equipped mechanics in mechanic loadout. |
| `zoneId` | No | string | No | Specifies the zone ID where the activity is started. |
| `mapPosition` | Yes | float32 | No | **Discontinued**. This property is no longer used.  Specifies the position [x,y] on the zone's map image where activity is started. |
| `difficultySetting` | No | Int32 | No | **Discontinued**. This property is no longer used.  Specifies the difficulty settings the player uses. The high number means harder difficulty and the value range is between 0 and 255. |

**Post Event
Sample**

```
{
  "properties": {
    "activityId": "activity_0001",
    "primaryActor": "actor_0001",
    "secondaryActors": [
      "actor_0002",
      "actor_0003"
    ],
    "equippedMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ],
    "zoneId": "zone_0001"
  }
}
```

## activityEnd

The event indicates that the player ended an activity.
The following table describes `activityEnd` properties.

activityEnd Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `activityId` | No | string | Yes | Specifies the object ID of activity when the player ends. |
| `outcome` | No | string | No | Specifies the outcome in order to report the result when the activity ends. Values that can be specified are:   * completed * failed * abandoned  Note: The outcome property must be specified if the `activityId` references a progress activity, task, or sub-task under a progress or open-ended activity.  When the activity is completed, send an `activityEnd` event with `outcome: completed`. `activityEnd` is optional if an activity fails or is abandoned. |
| `score` | No | Int32 | No | Specifies the score when the activity ends. |
| `zoneId` | No | string | No | Specifies the zone ID where the activity is ended. |
| `mapPosition` | Yes | float32 | No | **Discontinued**. This property is no longer used.  Specifies the position [x,y] on the zone's map image where activity is ended. |
| `difficultySetting` | No | Int32 | No | Specifies the difficulty settings the player uses. The high number means harder difficulty and the value range is between 0 and 255. |

**Post Event
Sample**

```
{
  "properties": {
    "activityId": "activity_0001",
    "outcome": "completed",
    "zoneId": "zone_0001",
    "difficultySetting": 10
  }
}
```

## activityResume

You can use this event to resume an activity by specifying the status of its tasks and sub-tasks. You can post the event once for each in-progress activity (`type: activity`).

The following table describes `activityResume` properties.

activityResume Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `activityId` | No | string | Yes | Specifies the object ID of an activity that is active. |
| `inProgressActivities` | Yes | string | No | Specifies the list of object IDs of tasks and/or sub-tasks that are in progress under an active activity. |
| `completedActivities` | Yes | string | No | Specifies the list of object IDs of tasks and/or sub-tasks that are completed under an active activity. |

**Post Event Sample**

```
{
  "properties": {
    "activityId": "activity_0001",
    "completedActivities": [
      "activity_task_0001",
      "activity_subTask_0001"
    ],
    "inProgressActivities": [
      "activity_task_0002",
      "activity_subTask_0002"
    ]
  }
}
```

## activityTerminate

Use this event to clear all in-progress activities. No properties are required.

## activityAvailabilityChange

The event indicates that an activity or activities became playable or unplayable. The
following table describes `activityAvailabilityChange` properties.

activityAvailabilityChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `availableActivities` | Yes | string | No | List of object IDs of activities that are playable by the player. |
| `unavailableActivities` | Yes | string | No | List of object IDs of activities that are not playable by the player. |
| `mode` | No | string | Yes | Specifies the update mode.   * full   Replaces all the values in the state.   * delta   Instead of replacing all the values, the system calculates the difference and adds/removes the value to/from the state. |

Note:

Either the `availableActivities` property or
`unavailableActivities` property must be specified when the event
is posted.

**Post Event
Sample**

```
{
  "properties": {
    "availableActivities": [
      "activity_0001",
      "activity_0002",
      "activity_0003"
    ],
    "mode": "delta"
  }
}
```

## activityPriorityChange

Note: This event is not currently used by the system.

Use this event to set a priority value for an activity. The following table describes its properties.

activityPriorityChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `prioritizedActivities` | Yes | object | Yes | Specifies the list of object IDs with suggested prioritization. |
| `activityId` | No | string | Yes | Specifies the object ID of the activity the game suggests to prioritize. |
| `priority` | No | Int32 | Yes | Specifies the activity's priority. Higher values mean higher priorities. The value range is between -128 and 128. |

**Post Event Sample**

```
{
  "properties": {
    "prioritizedActivities": [
      {
        "activityId": "activity_0001",
        "priority": 1
      },
      {
        "activityId": "activity_0002",
        "priority": 2
      },
      {
        "activityId": "activity_0003",
        "priority": 3
      }
    ]
  }
}
```

## locationChange

The event indicates that the player changed the zone
or location. The following table describes `locationChange`
properties.

locationChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `zoneId` | No | string | Yes | Specifies the object ID of zone of the player. |
| `mapPosition` | Yes | float32 | No | **Discontinued**. This property is no longer used.  Specifies the current position [x,y] of the player on the zone's map image. |

**Post Event
Sample**

```
{
  "properties": {
    "zoneId": "zone_0001"
  }
}
```

## mechanicUse

The event indicates that a mechanic has been used by the
Player. The following table describes `mechanicUse` properties.

mechanicUse Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `usedMechanics` | Yes | string | Yes | List of object IDs of mechanics the player uses. |

**Post Event
Sample**

```
{
  "properties": {
    "usedMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ]
  }
}
```

## mechanicUseBy

The event indicates that a mechanic has been used by
the game (for example, a Non-Player character). The following table describes
`mechanicUseBy` properties.

mechanicUseBy Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `usedMechanics` | Yes | string | Yes | List of object IDs of mechanic the non-player uses. |
| `initiatorActor` | No | string | No | Specifies an object ID of actor that uses mechanic. |

**Post Event
Sample**

```
{
  "properties": {
    "usedMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ],
    "initiatorActor": "actor_0001"
  }
}
```

## mechanicImpact

The event indicates that a mechanic Player used had
an impact on gameplay. The following table describes `mechanicImpact`
properties.

mechanicImpact Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `usedMechanics` | Yes | string | Yes | List of object IDs of mechanic the player uses. |
| `targetActors` | Yes | string | No | List of object IDs of actor that had an impact by mechanics the player used. |

**Post Event
Sample**

```
{
  "properties": {
    "usedMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ],
    "targetActors": [
      "actor_0001",
      "actor_0002",
      "actor_0003"
    ]
  }
}
```

## mechanicImpactBy

The event indicates that a mechanic used by the
game (e.g. Non-Player character) had an impact on gameplay. The following table has
`mechanicImpactBy` properties.

mechanicImpactBy Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `usedMechanics` | Yes | string | Yes | List of object IDs of mechanic the initiator uses. |
| `initiatorActor` | No | string | No | Specifies an object ID of actor that initiates an impact. |
| `targetActors` | Yes | string | No | List of object IDs of actor that had an impact by mechanics the initiator used. |

**Post Event
Sample**

```
{
  "properties": {
    "usedMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ],
    "initiatorActor": "actor_0001",
    "targetActors": [
      "actor_0001",
      "actor_0002",
      "actor_0003"
    ]
  }
}
```

## mechanicMitigate

The event indicates that mechanic(s) Player used
mitigates the impact of the mechanic Non-Player used. The following table has
`mechanicMitigate` properties.

mechanicMitigate Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `usedMechanics` | Yes | string | Yes | List of object IDs of mechanic the player uses in order to mitigate the impact. |
| `initiatorActor` | No | string | No | Specifies an object ID of actor that attempts to initiate an impact. |
| `usedMechanicsBy` | Yes | string | Yes | List of object IDs of actor that had an impact by mechanics the initiator used. |

**Post Event
Sample**

```
{
  "properties": {
    "usedMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ],
    "initiatorActor": "actor_0001",
    "usedMechanicsBy": [
      "actor_0001",
      "actor_0002",
      "actor_0003"
    ]
  }
}
```

## mechanicAvailabilityChange

This event indicates that the mechanics
available to the player have changed. Available means that the mechanic is available in
the game world for the player to use, but may require the player to go through some
steps to acquire it into inventory (e.g. buy from a shop, pick up from the world) before
using it. The following table describes `mechanicAvailabilityChange`
properties.

mechanicAvailabilityChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `availableMechanics` | Yes | string | No | List of object IDs of mechanic the player is able to acquire. |
| `unavailableMechanics` | Yes | string | No | List of object IDs of mechanic the player is not able to acquire. |
| `mode` | No | string | Yes | Specifies the update mode.   * full   Replaces all the values in the state.   * delta   Instead of replacing all the values, the system calculates the difference and adds/removes the value to/from the state. |

Note:

Either the `availableMechanics` property or
`unavailableMechanics` property must be specified when the event is
posted.

**Post Event
Sample**

```
{
  "properties": {
    "availableMechanics": [
      "mechanic_0001",
      "mechanic_0002",
      "mechanic_0003"
    ],
    "mode": "delta"
  }
}
```

## mechanicInventoryChange

This event indicates that the player's
inventory has changed. Inventory refers to mechanics that are immediately usable to the
player without having to take additional steps in the game before using it. The
following table describes `mechanicInventoryChange` properties.

mechanicInventoryChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `addedMechanics` | Yes | string | No | List of object IDs of mechanic that are added to the inventory. |
| `removedMechanics` | Yes | string | No | List of object IDs of mechanic that are removed from the inventory. |
| `mode` | No | string | Yes | Specifies the update mode.   * full   Replaces all the values in the state.   * delta   Instead of replacing all the values, the system calculates the difference and adds/removes the value to/from the state. |

Note:

Either the `addedMechanics` property or
`removedMechanics` property must be specified when the event is
posted.

**Post Event
Sample**

```
{
  "properties": {
    "removedMechanics": [
      "mechanic_0002",
      "mechanic_0004"
    ],
    "mode": "delta"
  }
}
```

## mechanicLoadoutChange

This event indicates that the player's loadout
has changed. Loadout represents the mechanics that are most immediately accessible to
the player. The following table has `mechanicLoadoutChange`
properties.

mechanicLoadoutChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `equippedMechanics` | Yes | string | No | Specifies the list of equipped mechanics in mechanic loadout. |
| `unequippedMechanics` | Yes | string | No | Specifies the list of unequipped mechanics from mechanic loadout. |
| `mode` | No | string | Yes | Specifies the update mode.   * full   Replaces all the values in the state.   * delta   Instead of replacing all the values, the system calculates the difference and adds/removes the value to/from the state. |

Note:

Either the `equippedMechanics` property or
`unequippedMechanics` property must be specified when the event is
posted.

**Post Event
Sample**

```
{
  "properties": {
    "equippedMechanics": [
      "mechanic_0001",
      "mechanic_0003"
    ],
    "mode": "delta"
  }
}
```

## actorChange

This event indicates that the player's selected actor(s)
have changed. Selected actors represent the actors the player is controlling in the
game. The following table has `actorChange` properties.

actorChange Properties

| **Property** | **Array** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| `primaryActor` | No | string | Yes | Primary actor player uses. |
| `secondaryActors` | Yes | string | No | Secondary actors player uses. |

**Post Event
Sample**

```
{
  "properties": {
    "primaryActor": "actor_0001",
    "secondaryActors": [
      "actor_0002",
      "actor_0003"
    ]
  }
}
```