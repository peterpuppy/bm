# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/4-example-of-a-ruleset-for-a-co-op-survival-game-where-playe.html

# Example Rulesets

This chapter provides examples of rulesets.

# (1) Example of a Ruleset for a Singles Tennis Game in Which a Match Is Played in a Specified Court with an Opponent Close in Skill Level

A game of singles does not require splitting into teams. However, for the purposes of the ruleset, one team with two players is defined. Because matchmaking is performed based on skill levels, "skill" is declared as a player attribute. Additionally, "court" is declared as a ticket attribute to specify the type of court on which to have the match. To conduct matchmaking with opponents who have specified the same court, the attribute "court" is defined as being "EQUAL" for the "Same\_court" rule. To conduct matchmaking with opponents who are close in skill level, the "MAX\_DISTANCE" for "skill" is defined as "5.0" for the "Similar\_skill\_levels" rule. However, if no opponent is found within 15 seconds after the ticket is created, the relaxed rule allows a difference in skill level up to "10.0." If no opponent is found within 30 seconds, any difference in skill level is allowed.

## Ruleset

```
{
  "rulesetName": "Singles_Match_Ignoring_NatType",
  "settings": {
    "supportedPlatforms": [
      "PS4",
      "PS5"
    ],
    "ticketTimeout": 180,
    "gameSession": {
      "usePlayerSession": true,
      "reservationTimeout": 60
    }
  },
  "teams": [
    {
      "teamName": "ALL",
      "minPlayers": 2,
      "maxPlayers": 2
    }
  ],
  "playerAttributes": [
    {
      "name": "skill",
      "type": "NUMBER",
      "defaultValue": "0.0"
    }
  ],
  "ticketAttributes": [
    {
      "name": "court",
      "type": "STRING",
      "defaultValue": "Grass court"
    }
  ],
  "rules": [
    {
      "ruleName": "Same_court",
      "target": "ticketAttributes.court",
      "operator": "EQUAL"
    },
    {
      "ruleName": "Similar_skill_levels",
      "target": "playerAttributes.skill",
      "operator": "MAX_DISTANCE",
      "value": "5.0"
    }
  ],
  "expansions": [
    {
      "target": "rules.Similar_skill_levels.value",
      "steps": [
        {
          "waitTime": 15,
          "value": "10.0"
        },
        {
          "waitTime": 30,
          "ignore": "true"
        }
      ]
    }
  ]
}
```

## Matchmaking Ticket

The application creates and submits a matchmaking ticket specified with the player's own skill level and their desired type of court.

```
{
  "rulesetName": "Singles_Match_Ignoring_NatType",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5",
      "playerAttributes": [
        {
          "name": "skill",
          "type": "NUMBER",
          "value": "3.0"
        }
      ]
    }
  ],
  "ticketAttributes": [
    {
      "name": "court",
      "type": "STRING",
      "value": "Grass court"
    }
  ]
}
```

# (2) Example of a Ruleset for a Doubles Tennis Game in Which a Match Is Played in a Specified Court with Opponents Close in Skill Level

For a doubles tennis game, two teams of two players, each, are defined. Because the matchmaking feature with consideration for P2P communication is used, the P2P connection topology (full mesh) must be specified. The rest is similar to Example 1

## Ruleset

```
{
  "rulesetName": "Doubles_Match_for_Mesh_Topology",
  "settings": {
    "supportedPlatforms": [
      "PS4",
      "PS5"
    ],
    "ticketTimeout": 180,
    "useNatTypeForTopology": "MESH",
    "gameSession": {
      "usePlayerSession": true,
      "reservationTimeout": 60
    }
  },
  "teams": [
    {
      "teamName": "Blue",
      "minPlayers": 2,
      "maxPlayers": 2
    },
    {
      "teamName": "Red",
      "minPlayers": 2,
      "maxPlayers": 2
    }
  ],
  "ticketAttributes": [
    {
      "name": "court",
      "type": "STRING",
      "defaultValue": "Grass court"
    }
  ],
  "playerAttributes": [
    {
      "name": "skill",
      "type": "NUMBER",
      "defaultValue": "0.0"
    }
  ],
  "rules": [
    {
      "ruleName": "Same_court",
      "target": "ticketAttributes.court",
      "operator": "EQUAL"
    },
    {
      "ruleName": "Similar_skill_levels",
      "target": "playerAttributes.skill",
      "operator": "MAX_DISTANCE",
      "value": "5.0"
    }
  ],
  "expansions": [
    {
      "target": "rules.Similar_skill_levels.value",
      "steps": [
        {
          "waitTime": 15,
          "value": "10.0"
        },
        {
          "waitTime": 30,
          "ignore": "true"
        }
      ]
    }
  ]
}
```

## Matchmaking Ticket

The application creates and submits matchmaking tickets specified with the players' own skill levels and their desired type of court for the two players making up a prospective doubles pair. Not specifying a team name effectively specifies that the two will be assigned to the same team. (Whether to assign them to the "Red" team or to the "Blue" team is determined by the server; the assumption is that neither possibility will change the gameplay.) Because P2P connection topology (full mesh) is specified in the ruleset, the NAT type of each player must be specified. However, be careful not to include two or more players of NAT type 3 in one ticket. (An error will occur when the ticket is submitted because it will not be possible to establish a full mesh P2P connection.)

```
{
  "rulesetName": " Doubles_Match_for_Mesh_Topology",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5",
      "natType": 3,
      "playerAttributes": [
        {
          "name": "skill",
          "type": "NUMBER",
          "value": "3.0"
        }
      ]
    },
    {
      "accountId": "987654321",
      "platform": "PS5",
      "natType": 1,
      "playerAttributes": [
        {
          "name": "skill",
          "type": "NUMBER",
          "value": "5.0"
        }
      ]
    }
  ],
  "ticketAttributes": [
    {
      "name": "court",
      "type": "STRING",
      "value": "Grass court"
    }
  ]
}
```

# (3) Monster vs. Hunters Quick Match

This is an example of a quick match to brings together one player in the role of a monster and two to four players in the roles of hunters. The numbers of players differ between the monster team and the hunter team. Therefore, the teams are defined in a way that reflects this difference. No matchmaking rules are defined, because this is a quick match that only requires that enough players be matched with one another. To get as many players to join as possible, the minimum number of hunters is initially set to 4. However, if 4 players have not joined within 30 seconds after the ticket is created, the relaxed rule allows matchmaking to be achieved with only 2 players.

```
{
  "rulesetName": "Monster_vs_Hunter_QuickMatch_Ignoring_NatType",
  "settings": {
    "supportedPlatforms": [
      "PS4",
      "PS5"
    ],
    "ticketTimeout": 180,
    "gameSession": {
      "usePlayerSession": true,
      "reservationTimeout": 60
    }
  },
  "teams": [
    {
      "teamName": "Monster",
      "minPlayers": 1,
      "maxPlayers": 1
    },
    {
      "teamName": "Hunters",
      "minPlayers": 4,
      "maxPlayers": 4
    }
  ],
  "expansions": [
    {
      "target": "teams.Hunters.minPlayers",
      "steps": [
        {
          "waitTime": 30,
          "value": "2"
        }
      ]
    }
  ]
}
```

## Matchmaking Ticket (Monster Role)

When the player would like to play as the monster, the application submits a matchmaking ticket like the one that follows.

```
{
  "rulesetName": "Monster_vs_Hunter_QuickMatch_Ignoring_NatType",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5",
      "teamName": "Monster"
    }
  ]
}
```

## Matchmaking Ticket (Hunter Role)

When two players would like to play together as hunters, the application submits a matchmaking ticket like the one that follows.

```
{
  "rulesetName": "Monster_vs_Hunter_QuickMatch_Ignoring_NatType",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5",
      "teamName": "Hunters"
    },
    {
      "accountId": "987654321",
      "platform": "PS5",
      "teamName": "Hunters"
    }
  ]
}
```

# (4) Example of a Ruleset for a Co-Op Survival Game Where Players Can Request to Join as Supplemental Players via Backfilling

A co-op game does not require splitting into teams. However, for the purposes of the ruleset, one team with two to four players is defined. So that players can indicate whether they want to join as supplemental players via backfilling, declare "allow\_backfill" as a ticket attribute (for details, refer to "Examples of Matchmaking Rule Definitions"). To prevent players who do not want to join as supplemental players form being matched with a matchmaking ticket that solicits supplemental players, define "allow\_backfill" as "EQUAL" as a "Same\_backfill\_preference" rule. For players who do not mind whether they are supplemental players, define "ANY", a value that will be treated as a wildcard.

```
{
  "rulesetName": "Coop_Survival_Ignoring_NatType",
  "settings": {
    "supportedPlatforms": [
      "PS4",
      "PS5"
    ],
    "ticketTimeout": 180,
    "gameSession": {
      "usePlayerSession": true,
      "reservationTimeout": 60
    }
  },
  "teams": [
    {
      "teamName": "Survivors",
      "minPlayers": 2,
      "maxPlayers": 4
    }
  ],
  "ticketAttributes": [
    {
      "name": "allow_backfill",
      "type": "STRING",
      "defaultValue": "true"
    }
  ],
  "rules": [
    {
      "ruleName": "Same_backfill_preference",
      "target": "ticketAttributes.allow_backfill",
      "operator": "EQUAL",
      "wildcard": "ANY"
    }
  ]
}
```

## Matchmaking Ticket for Enlisting Supplemental Players

For example, suppose you start a game in a Game Session with four players, and one player quits gameplay partway through and leaves the Game Session. If you want to fill the empty slot with a supplemental player, the application will specify the Game Session ID and details of the players already participating as shown below. It will then submit a matchmaking ticket specifying the "allow\_backfill" attribute as "true" to prevent players who do not want to join as supplemental players from being matched.

```
{
  "rulesetName": "Coop_Survival_Ignoring_NatType",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5"
    },
    {
      "accountId": "234567890",
      "platform": "PS5"
    },
    {
      "accountId": "345678901",
      "platform": "PS5"
    }
  ],
  "ticketAttributes": [
    {
      "name": "allow_backfill",
      "type": "STRING",
      "value": "true"
    }
  ],
"location": {
    "gameSessionId": "47664463-1040-4d51-bbcd-10179393896e"
  }
}
```

## Matchmaking Ticket for Players Who Want to Avoid Joining as a Supplemental Player

For players who do not want to join a game in progress, or in other words, those who do not want to join as supplemental players via backfilling, the application will submit a matchmaking ticket specifying the "allow\_backfill" attribute as "false."

```
{
  "rulesetName": "Coop_Survival_Ignoring_NatType",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5"
    }
  ],
  "ticketAttributes": [
    {
      "name": "allow_backfill",
      "type": "STRING",
      "value": "false"
    }
  ]
}
```

## Matchmaking Ticket for Players Who Do Not Mind Whether They Join as Supplemental Players

For players who do not mind whether they are supplemental players or not, the application will submit a matchmaking ticket with a value treated as a wildcard ("ANY").

```
{
  "rulesetName": "Coop_Survival_Ignoring_NatType",
  "players": [
    {
      "accountId": "123456789",
      "platform": "PS5"
    }
  ],
  "ticketAttributes": [
    {
      "name": "allow_backfill",
      "type": "STRING",
      "value": "ANY"
    }
  ]
}
```