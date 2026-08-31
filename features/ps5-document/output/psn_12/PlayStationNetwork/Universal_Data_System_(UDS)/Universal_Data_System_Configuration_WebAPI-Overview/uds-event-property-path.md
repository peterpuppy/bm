# Universal Data System Configuration Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Universal_Data_System_Configuration_WebAPI-Overview/uds-event-property-path.html

# Using the UDS Configuration Web API

This chapter provides detailed information on using the UDS Configuration Web API.

Using the UDS Configuration Web API requires you to have properly set up UDS elements. Design data connections and references first, and then configure them in the following order so that your intended data connections remain.

1. Configure PlayStation™Network objects. PlayStation™Network objects represent static information used in a game such as the story's missions and locations.
2. Configure UDS events. UDS events track game progress and a player's actions in a game. Events are actions that take place on objects.
3. Configure UDS stats definitions. UDS Stats is a scheme for extracting and aggregating information from UDS events sent by a game application and for storing the information as statistics. UDS Stats is a collection of data units called "stat". Each stat has components. The definition of UDS Stats is a Stats Definition.
4. Configure UDS stats extractions. Extraction refers to extracting information from UDS events to send to UDS Stats. Stats Extraction is a rule for extracting information from UDS events to send to UDS Stats
5. Use the API to manage stats definitions and extractions. Use the various requests within the API to list, edit, create, and delete stats definitions and extractions.
6. Use the API to provide a diagnostics report of configurations and to check if configuration is set up to properly function.
7. Use the API to manage `npConfigTag`.
8. Use the API to upload media assets. Use generated asset URLs to associate media assets to UDS objects.

# UDS Event Property Path

This topic provides information on how to use expressions when defining UDS events.

Use the appropriate expression when expressing a specific property on UDS Events with Event Definitions or Stats Extractions.

Expression Method

| **Operator** | **Description** |
| --- | --- |
| `$` | The root element of "properties" object to query. This starts all path expressions. |
| `.<name>` | Dot-notated child. |

## Example

**Basic Usage**

If you want to specify `"questId"`, the expression in Property Path is `"$.questId"`.

```
{
    "eventName": "questStarted",
    "eventType": "activityStart",
    "properties": [
      {
        "questId": "questA",
        "customLevelId ": 39
      }
  ]
}
```

**Advanced Usage**

If you want to specify `"activityId"` in `prioritizedActivities` (`prioritizedActivity` object list), the expression in Property Path is `"$.prioritizedActivities[*].activityId"`.

```
{
    "eventName": "priorityChange",
    "eventType": "activityPriorityChange",
    "properties": [
      {
        "prioritizedActivities": [
          {
              "activityId": "questA",
              "priority": 1
          },
          {
              "activityId": "questB",
              "priority": 2
          }
        ]
    }
]
}
```

# Status of Entities

This topic provides information on the different statuses the UDS Configuration Web API can return for certain entities.

The entities `listObjects`, `listEvents`, `listCustomStatsDefinition`, and `listCustomStatsExtraction` return a status for each entity.

Meaning of Status Field

| **Status** | **Description** |
| --- | --- |
| `inDevelopment` | An entity is not in any status below. |
| `tagged` | `npConfigTag` is created against the entity. |
| `inFormatQa` | Platform Certification and Operations is preparing to start a review or a review is being performed against the entity. |
| `formatQaCompleted` | Platform Certification and Operations completed the review against the entity. |
| `inProduction` | The entity is published to the production environment. |

An entity which status is `inDevelopment` is editable. An entity in any other status is restricted from changing.