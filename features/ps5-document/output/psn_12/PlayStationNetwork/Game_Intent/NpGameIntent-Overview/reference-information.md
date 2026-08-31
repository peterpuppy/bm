# NpGameIntent Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpGameIntent-Overview/reference-information.html

# Reference Information

This topic provides reference information for using the NpGameIntent library, including definitions of the parameter file (param.json) and an example of how to write it.

# Parameter File (param.json)

A parameter file (param.json) describing the types of game intent events that can be received must be created for an application to receive game intent events. The system will not send game intent events of types not described in the parameter file to the application. In other words, an application can use this parameter file to only receive game intent events of the types that it permits.

Refer to [Param.json File Specification - Using the Param File (param.json)](../Param_Json-Specification/using-the-param-file-paramjson.html) for instructions on how to create a parameter file (param.json).

## Parameter Definitions

A parameter file is a JSON-format file named "param.json". Inside this JSON file, game intent-related settings must be made in accordance with the format described below.

Format of gameIntent Objects in a param.json File

| **Parameter** | | | **Description** |
| --- | --- | --- | --- |
| `gameIntent` | | | Settings for game intents (object type, optional) |
|  | `permittedIntents` | | Array of permitted game intent event types to receive (object type array, required) |
|  |  | `intentType` | Game intent event type (string type, required) |

Note:

Refer to the [Game Intent System Overview - Game Intent Event Types and Properties](../Game_Intent_System-Overview/game-intent-event-types-and-properties.html) chapter for a list of game intent event types.

## Example

A typical example of what to include for a `gameIntent` object in a param.json file is provided below:

```
{
    ...
    "gameIntent": {
       "permittedIntents": [
          {
              "intentType": "joinSession"
          },
          {
              "intentType": "launchActivity"
          }
       ]
    },
    ...
}
```