# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/json-schema-for-ruleset.html

# Configuring Rulesets

This chapter describes the items that are needed when defining rulesets that represent matchmaking conditions. You can create up to 100 rulesets per application.

For information about applying rulesets to the matchmaking server, refer to "[Applying Rulesets (in the Legacy Network Architecture)](using-rulesets.html)" and "[Applying Rulesets (in the Sandbox Network Architecture)](using-rulesets-in-sandbox-mode.html)".

# Components of a Ruleset

A ruleset is composed of the following elements:

* Ruleset name
* Team definitions
* Attribute declarations
  + Ticket attributes: Declarations of the attribute values that you want to be specified in matchmaking tickets
  + Player attributes: Declarations of the attribute values that you want to be specified for each player
* Definition of the matchmaking rules
* Relaxed rule definitions

# Ruleset Name

A ruleset name is the internal name of the ruleset, defined uniquely within the application. This is a name used internally by the application, not one displayed to users. Therefore, feel free to define any name that is easy to identify.

Note that, once a ruleset name has been established, the ruleset cannot be renamed.

# Team Definitions

In a team definition, describe the composition and size of the team to be used in matchmaking. Every ruleset must have at least one team, with the maximum number of teams that can be defined being 128.

Set the following information for each team:

* Team name (required)

  Assign a team name that is unique within the ruleset. The application uses this team name when specifying the team in a matchmaking ticket. This is a name used internally by the application, not one displayed to users. Therefore, feel free to define any name that is easy to identify.
* Minimum number of players (required)

  Specify the minimum number of players who can be assigned to the team.
* Maximum number of players (required)

  Specify the maximum number of players who can be assigned to the team. Make specifications so that the total number of players in teams is 256 or less.

A team must be defined in a ruleset, even if splitting players among teams is not required as part of gameplay. For instance, in a case such as a tennis singles match, define one team and assign the two players to it. (It would also be possible to define two teams and to assign one player, each, to them, but this is not recommended, because matchmaking performance may be adversely affected.)

# Attribute Declarations

Declare data points used as conditions for matchmaking as player attributes or as ticket attributes.

## Player Attributes

If you would like to use attribute values specified for each player as matchmaking conditions, declare them as player attributes. Make such declarations when you would like to include, for example, the players' skill levels and roles among the matchmaking conditions. Up to 10 player attributes can be declared. The following items are required in a player attribute declaration:

* Attribute name (required)

  Define a name that is unique among all player attributes. This is a name used internally by the application, not one displayed to users. Therefore, feel free to define any name that is easy to identify.
* Type (required)

  This the datatype for the attribute value. Define the attribute as either a NUMBER (a base-10 integer or real number) or a STRING.
* Default value (required)

  Define the default value that will be applied if the value is not specified in the matchmaking ticket.

## Ticket Attributes

If you would like to use attribute values common among all players as matchmaking conditions, declare them as ticket attributes. Make such declarations when you would like to include, for example, a stage or map among the matchmaking conditions. Up to 10 ticket attributes can be declared. The following items are required in a ticket attribute declaration:

* Attribute name (required)

  Define a name that is unique among all ticket attributes. This is a name used internally by the application, not one displayed to users. Therefore, feel free to define any name that is easy to identify.
* Type (required)

  This the datatype for the attribute value. Define the attribute as either a NUMBER (a base-10 integer or real number) or a STRING.
* Default value (required)

  Define the default value that will be applied if the value is not specified in the matchmaking ticket.

# Matchmaking Rule Definitions

A maximum of 20 matchmaking rules can be defined. Each matchmaking rule is defined as a comparison between one of the player attributes or ticket attributes and either a fixed value or the attribute value for the other player. Matchmaking is achieved when all defined matchmaking rules are satisfied. (Thus, the matchmaking rules are AND conditions.)

* Matchmaking rule name (required)

  Define a name that is unique within the ruleset. This is a name used internally by the application, not one displayed to users. Therefore, feel free to define any name that is easy to identify.
* Target attribute (required)

  Define the player attribute or ticket attribute that will be subject to comparison.
* Comparison operator (required)

  Define the comparison operator as one of the following operators:

  + "EQUAL": The attribute values subject to comparison are all the same
  + "NOT\_EQUAL": The attribute values subject to comparison are all different
  + "MAX\_DISTANCE": The difference between the attribute values subject to comparison is less than or equal to the specified value
* Value (arbitrary)

  Define the value against which to compare the attribute value. This value can be omitted if the operator is "EQUAL" or "NOT\_EQUAL"; in that case, the attribute value will be compared against the attribute values of the players subject to matchmaking.
* Values treated as wildcards (arbitrary)

  Define the values to treat as wildcards. This can only be defined when the operator is "EQUAL". Tickets where attributes specified as matchmaking rules are themselves specified as wildcards will be treated as satisfying the rules, regardless of which values are compared.

## Examples of Matchmaking Rule Definitions

**Example 1: Matchmaking Rule to Look for Players Whose Skill Level Is Close to (Has a Difference No Greater Than 5 with) One's Own**

* Player attribute declaration
  + Attribute name: skill
  + Type: NUMBER
  + Default value: 10
* Matchmaking rule definition
  + Rule name: Close\_skill\_level
  + Target attribute: playerAttributes.skill
  + Comparison operator: MAX\_DISTANCE
  + Value: 5

**Example 2: Matchmaking Rule to Look for Players with the Same Application Version**

* Player attribute declaration
  + Attribute name: application\_version
  + Type: STRING
  + Default value: 01.00
* Matchmaking rule definition
  + Rule name: Same\_application\_version
  + Target attribute: playerAttributes.application\_version
  + Comparison operator: EQUAL
  + Value: (Not specified)
  + Values treated as wildcards: (Not specified)

**Example 3: Matchmaking Rule to Look for Players Who Want to Play a Match on the Same Map**

* Ticket attribute declaration
  + Attribute name: map
  + Type: STRING
  + Default value: Jungle
* Matchmaking rule definition
  + Rule name: Same\_map
  + Target attribute: ticketAttributes.map
  + Comparison operator: EQUAL
  + Value: (Not specified)
  + Values treated as wildcards: ANY

**Example 4: Matchmaking Rule Where Players Request to Join as Supplemental Players via Backfilling**

* Ticket attribute declaration
  + Attribute name: allow\_backfill
  + Type: STRING
  + Default value: true
* Matchmaking rule definition
  + Rule name: Same\_backfill\_preference
  + Target attribute: ticketAttributes.allow\_backfill
  + Comparison operator: EQUAL
  + Value: (Not specified)
  + Values treated as wildcards: ANY

This matchmaking rule allows players to indicate on each matchmaking ticket whether they want to join matchmaking as supplemental players for backfilling purposes as follows:

* Matchmaking ticket for enlisting supplemental players ⇒ allow\_backfill : true
* Matchmaking ticket for players who do not want to join as supplemental players ⇒ allow\_backfill : false
* Matchmaking ticket for players who do not mind whether they join as supplemental players ⇒ allow\_backfill : ANY

Usage examples of these matchmaking rules can be found in the "[Example Rulesets](example-rulesets.html)" chapter.

# Relaxed Rule Definitions

Relaxed rules are a mechanism for making it easier to achieve matchmaking by loosening the conditions if matchmaking is not successful within a certain amount of time after a ticket is created. A maximum of 20 relaxed rules can be defined.

Relaxed rules are composed of the following elements:

* Target (required)

  Set "minimum team size", "value of the rule using the MAX\_DISTANCE operator", or the rule itself as the target for relaxing.
* Step (required)
  + Elapsed time (required)
  + Value after change (optional)
  + Ignore flag (optional)

    This defines how the target changes over time. You can define up to 10 steps and specify either the value after a change has been made or an ignore flag.

If the target is set to "minimum team size" or "value of the rule using the MAX\_DISTANCE operator", the value can be changed over time. If the target is set to "value of the rule using the MAX\_DISTANCE operator" or the rule itself, the rule can be disabled by applying the ignore flag once an amount of time has elapsed. However, once a rule has been disabled, it cannot be enabled again after more time has passed.

## Examples of Relaxed Rule Definitions

**Example 1: Relaxed Rule for Skill Level Matchmaking Rules**

* Matchmaking rule definition: Matchmaking is achieved if the difference in skill level is no greater than 5
  + Rule name: Close\_skill\_level
  + Target attribute: playerAttributes.skill
  + Comparison operator: MAX\_DISTANCE
  + Value: 5
* Relaaxed rule definition
  + Target: rules.Close\_skill\_level.value
  + Step 1: After 15 seconds, allow a difference in skill level up to 10

    Elapsed time: 15 seconds, Value after change: 10
  + Step 2: After 30 seconds, allow any difference in skill level

    Elapsed time: 30 seconds, Ignore flag

**Example 2: Relaxed Rule for Minimum Team Size**

* Team definition: Matchmaking is achieved when 4 hunters join
  + Team name: Hunters
  + Minimum number of players: 4
  + Maximum number of players: 4
* Relaaxed rule definition
  + Target: teams.Hunters.minPlayers
  + Step 1: After 30 seconds, matchmaking is achieved with only 2 players

    Elapsed time: 30 seconds, Value after change: 2

# Matchmaking with Consideration for P2P Communication

The matchmaking feature with consideration for P2P communication can be used by applications performing P2P communication using the NpSessionSignaling library. In other words, by specifying the P2P connection topology expected by the application (full mesh or star) and each player's NAT type with a ticket, the server will select players and perform matchmaking so that the expected P2P connection can be established.

P2P connection topologies that can be specified and the condition by which the server selects players for each are as follows.

* Full mesh: even if there are many NAT type 3 players, players will be selected so that there will only be one NAT type 3 player. (An error will occur when a ticket is issued containing two or more NAT type 3 players.)
* Star: players will be selected so that there is at least one or more NAT type 1 or NAT type 2 players.

The NAT type of each player can be obtained using the NpSessionSignaling library. Refer to the following documents for details:

* [NpSessionSignaling Library Overview](../../../SDK/latest/NpSessionSignaling-Overview/__document_toc.html)
* [NpSessionSignaling Library Reference](../../../SDK/latest/NpSessionSignaling-Reference/__document_toc.html)

# JSON Schema for Rulesets

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": {
    "settings": {
      "type": "object",
      "properties": {
        "ticketTimeout": {
          "type": "number",
          "minimum": 10,
          "maximum": 3600
        },
        "supportedPlatforms": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PS5",
              "PS4"
            ]
          }
        },
        "useNatTypeForTopology": {
          "type": "string",
          "enum": [
            "MESH",
            "STAR"
          ]
        },
        "gameSession": {
          "type": "object",
          "properties": {
            "usePlayerSession": {
              "type": "boolean"
            },
            "reservationTimeout": {
              "type": "number",
              "minimum": 1,
              "maximum": 86400
            }
          }
        }
      },
      "required": [
        "supportedPlatforms"
      ]
    },
    "teams": {
      "type": "array",
      "minItems": 1,
      "maxItems": 128,
      "items": {
        "type": "object",
        "properties": {
          "teamName": {
            "type": "string",
            "pattern": "^[a-zA-Z][a-zA-Z0-9_]{0,63}$"
          },
          "minPlayers": {
            "type": "number",
            "minimum": 1,
            "maximum": 256
          },
          "maxPlayers": {
            "type": "number",
            "minimum": 1,
            "maximum": 256
          }
        },
        "required": [
          "teamName",
          "minPlayers",
          "maxPlayers"
        ]
      }
    },
    "attributes": {
      "type": "array",
      "minItems": 0,
      "maxItems": 10,
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[a-zA-Z][a-zA-Z0-9_]{0,63}$"
          },
          "type": {
            "type": "string",
            "enum": [
              "STRING",
              "NUMBER"
            ]
          },
          "defaultValue": {
            "type": "string",
            "maxLength": 64
          }
        },
        "required": [
          "name",
          "type",
          "defaultValue"
        ]
      }
    },
    "rules": {
      "type": "array",
      "minItems": 0,
      "maxItems": 20,
      "items": {
        "type": "object",
        "properties": {
          "ruleName": {
            "type": "string",
            "pattern": "^[a-zA-Z][a-zA-Z0-9_]{0,63}$"
          },
          "target": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9\\._]{0,128}$"
          },
          "operator": {
            "type": "string",
            "enum": [
              "EQUAL",
              "NOT_EQUAL",
              "MAX_DISTANCE"
            ]
          },
          "value": {
            "type": "string",
            "maxLength": 128
          },
          "wildcard": {
            "type": "string",
            "maxLength": 64
          }
        },
        "required": [
          "ruleName",
          "target",
          "operator"
        ]
      }
    },
    "expansions": {
      "type": "array",
      "minItems": 0,
      "maxItems": 20,
      "items": {
        "type": "object",
        "properties": {
          "target": {
            "type": "string",
            "pattern": "^(rules\\.[a-zA-Z][a-zA-Z0-9_]{0,63}(\\.value)?|teams\\.[a-zA-Z][a-zA-Z0-9_]{0,63}.minPlayers)$"
          },
          "steps": {
            "type": "array",
            "minItems": 1,
            "maxItems": 10,
            "items": {
              "type": "object",
              "properties": {
                "waitTime": {
                  "type": "integer",
                  "minimum": 5,
                  "maximum": 3600
                },
                "value": {
                  "type": "string",
                  "maxLength": 128
                },
                "ignore": {
                  "type": "string",
                  "enum": [
                    "true"
                  ]
                }
              },
              "required": [
                "waitTime"
              ]
            }
          }
        },
        "required": [
          "target",
          "steps"
        ]
      }
    }
  },
  "type": "object",
  "properties": {
    "rulesetName": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9][[a-zA-Z0-9\\-\\._~]{0,63}$"
    },
    "settings": {
      "$ref": "#/definitions/settings"
    },
    "teams": {
      "$ref": "#/definitions/teams"
    },
    "ticketAttributes": {
      "$ref": "#/definitions/attributes"
    },
    "playerAttributes": {
      "$ref": "#/definitions/attributes"
    },
    "rules": {
      "$ref": "#/definitions/rules"
    },
    "expansions": {
      "$ref": "#/definitions/expansions"
    }
  },
  "required": [
    "rulesetName",
    "settings",
    "teams"
  ]
}
```

Elements of root

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| rulesetName | Yes | "Random\_Match" | Ruleset name.  ^[a-zA-Z][a-zA-Z0-9\_]{0,63}$  Must be unique for each multiplayer game mode in the application. It also cannot be renamed. |
| settings | Yes | - | Overall settings for matchmaking operations. The objects in the settings table, below. |
| teams | Yes | - | Array of the objects in the teams table, below. 1 to 128 teams can be defined. |
| playerAttributes | No | - | Array of the objects in the playerAttribute table, below. 0 to 100 attributes can be declared. |
| ticketAttributes | No | - | Array of the objects in the ticketAttribute table, below. 0 to 100 attributes can be declared. |
| rules | No | - | Array of the objects in the rules table, below. 0 to 20 rules can be defined. |
| expansions | No | - | Relaxed rules. Array of the objects in the expansions table, below. 0 to 20 rules can be defined. |

Elements of settings

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| ticketTimeout | No | 10 | Ticket timeout [seconds]. 10 to 3600 can be specified. If nothing is set, 60 will be used. If matchmaking is not achieved during the time limit that is set, the "psn:matchmaking:ticket:timedOut" Push event will be sent from the server. |
| supportedPlatforms | Yes | [  "PS4",  "PS5"  ] | The platforms that will be targeted for matchmaking. "PS4" or "PS5" can be set. |
| useNatTypeForTopology | No | "MESH" | P2P connection topology. "MESH" or "STAR" can be set. If nothing is set, the server will perform matchmaking without consideration for P2P communication. |
| gameSession | No | - | The objects in the gameSession table, below. |

Elements of gameSession

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| usePlayerSession | No | true | Flag indicating whether the Game Session is dependent on a Player Session. Either "true" or "false" can be set. If nothing is set, it will be as though "true" had been set. |
| reservationTimeout | No | 300 | Period during which reservations to join a Game Session remain valid (seconds). 1 to 86400 can be specified. If nothing is set, it will be as though 300 had been set. During the set period, reservations to join a Game Session will remain valid for the players selected by matchmaking. |

Elements of teams

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| teamName | Yes | "Blue" | Team name.  ^[a-zA-Z][a-zA-Z0-9\_]{0,63}$  Must be unique within the ruleset. |
| minPlayers | Yes | 1 | Minimum number of players that can be assigned to the team. 1 to 256 can be specified. |
| maxPlayers | Yes | 256 | Maximum number of players that can be assigned to the team. 1 to 256 can be specified. Make specifications so that the total number of players in teams is 256 or less. |

Elements of playerAttribute

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| name | Yes | "skill" | Player attribute name.  ^[a-zA-Z][a-zA-Z0-9\_]{0,63}$  Must be unique within playerAttribute. This name is used in rule definitions. |
| type | Yes | "NUMBER" | Datatype of the player attribute. Either "STRING" or "NUMBER" can be specified. NUMBER is a numerical value (an integer or real number), and STRING is a string. |
| defaultValue | Yes | "0" | Default value for the player attribute. 1 to 64 characters can be specified. |

Elements of ticketAttribute

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| name | Yes | "map" | Ticket attribute name.  ^[a-zA-Z][a-zA-Z0-9\_]{0,63}$  Must be unique within ticketAttribute. This attribute is used in rule definitions. |
| type | Yes | "NUMBER" | Datatype of the ticket attribute. Either "STRING" or "NUMBER" can be set. NUMBER is a numerical value (an integer or real number), and STRING is a string. |
| defaultValue | Yes | "0" | Default value for the ticket attribute. 1 to 64 characters can be set. |

Elements of rules

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| ruleName | Yes | "CloseSkillLevel" | Matchmaking rule name.  ^[a-zA-Z][a-zA-Z0-9\_]{0,63}$  Must be unique within rules. |
| target | Yes | "playerAttributes.skill" | Player attribute or ticket attribute to compare.  ^[a-zA-Z0-9\.\_]{0,128}$ |
| operator | Yes | "MAX\_DISTANCE" | Comparison operator.  EQUAL: The attribute values specified in target are all the same.  NOT\_EQUAL: The attribute values specified in target are all different.  MAX\_DISTANCE: The difference between the attribute values specified in target is less than or equal to the specified value. The attribute type specified in target must be NUMBER. |
| value | No | "5" | Value targeted for comparison. 1 to 128 characters can be set. Can be omitted if the operator is EQUAL/NOT\_EQUAL. If the attribute type specified in target is NUMBER, a number must be specified. |
| wildcard | No | "ANY" | Values treated as wildcards. 1 to 64 characters can be set. Can only be specified if the operator is EQUAL. If the attribute type specified in target is NUMBER, a number must be specified. |

Elements of expansions

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| target | Yes | "rules.near\_skill\_level.value" | Target with matchmaking conditions that change over time. You can set the target as the team's minPlayers, a value in the rule, or the rule itself. |
| steps | Yes |  | Array of the objects in the steps table, below. 1 to 10 steps can be defined. If the target is the rule itself, only ignore can be specified. |

Elements of steps

| **Attribute** | **Required** | **Example** | **Description** |
| --- | --- | --- | --- |
| waitTime | Yes | 30 | Elapsed time. Of the elements with a value less than or equal to the time that has elapsed since the ticket was created, the one with the maximum waitTime is applied as a relaxed rule. |
| value | No | "10" | Value to which to update the target. 1 to 128 characters can be set. Cannot be used togethr with ignore. |
| ignore | No | "true" | Disables the rule for the target. Cannot be used if the target is the team definition. Cannot be used together with value. Ignore can be specified only for the element with the maximum waitTime. |