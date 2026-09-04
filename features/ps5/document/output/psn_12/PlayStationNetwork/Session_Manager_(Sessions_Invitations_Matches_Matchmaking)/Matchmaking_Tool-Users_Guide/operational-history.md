# Matchmaking Tool User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Matchmaking_Tool-Users_Guide/operational-history.html

# Using the Matchmaking Tool

This chapter provides information on how to use the Matchmaking Tool.

# Managing Rulesets

This topic provides information on importing, activating, and deactivating
rulesets.

## Importing Rulesets

The Matchmaking Tool allows you to upload rulesets in JSON format. For example:

```
{
  "rulesetName": "team_deathmatch",
  "settings": {
    "ticketTimeout": 180,
    "supportedPlatforms": [
      "PS4",
      "PS5"
    ],
    "useNatTypeForTopology": "STAR",
    "gameSession": {
      "usePlayerSession": true,
      "reservationTimeout": 30
    }
  },
  "teams": [
    {
      "teamName": "the_seven",
      "minPlayers": 1,
      "maxPlayers": 7
    },
    {
      "teamName": "others",
      "minPlayers": 7,
      "maxPlayers": 7
    }
  ],
  "ticketAttributes": [
    {
      "name": "map",
      "type": "STRING",
      "defaultValue": "Rose Creek"
    }
  ],
  "playerAttributes": [
    {
      "name": "skill",
      "type": "NUMBER",
      "defaultValue": "0"
    },
    {
      "name": "firearm",
      "type": "STRING",
      "defaultValue": "peacemaker"
    }
  ],
  "rules": [
    {
      "ruleName": "same_map",
      "target": "ticketAttributes.map",
      "operator": "EQUAL",
      "wildcard": "ANY"
    },
    {
      "ruleName": "near_skill_level",
      "target": "playerAttributes.skill",
      "operator": "MAX_DISTANCE",
      "value": "5"
    }
  ],
  "expansions": [
    {
      "target": "teams.others.minPlayers",
      "steps": [
        {
          "waitTime": 10,
          "value": "5"
        },
        {
          "waitTime": 20,
          "value": "1"
        }
      ]
    },
    {
      "target": "rules.near_skill_level.value",
      "steps": [
        {
          "waitTime": 15,
          "value": "10"
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

To upload a ruleset:

1. Click **Import Ruleset (.json)**.
2. Select the file you want to upload.
3. Click **Continue**. The Matchmaking tool validates the JSON for schema
   errors.
4. Once validation is complete, click **Import**. The tool displays a success message upon completion.

Importing a New Ruleset

## Activating Rulesets

When importing a ruleset, it is inactive by default. To activate a ruleset:

1. Navigate to the **Ruleset List View** page.
2. Click the ellipsis icon in the row of the ruleset you wish to activate.
3. Click **Activate**. It may take up to 10 minutes for rulesets to become
   completely active.

Activating, Editing, and Deleting an Inactive Ruleset

## Editing Rulesets

Note: When editing an *Active* ruleset, you are only able to modify or expand on existing rules. If you want to update the entire ruleset, deactivate the ruleset before editing.

To edit a ruleset:

1. Navigate to the **Ruleset List View** page.
2. Click the ellipsis icon in the row of the ruleset to edit.
3. Make any necessary edits to the ruleset's JSON.
4. Click **Save**.

Editing Rulesets

## Deleting or Deactivating Rulesets

Note: You can only delete *Inactive* rulesets.

To delete or deactivate a ruleset:

1. Navigate to the **Ruleset List View** page.
2. Click the ellipsis icon in the row of the ruleset to delete or deactivate.
3. Click **Delete** or **Deactivate**.

Editing and Deactivating an Active Ruleset

# Publishing Rulesets

This topic provides information on publishing rulesets to different environments.

The Matchmaking Tool allows you to promote rulesets from the Development Environment (SP-INT) to the Production Environment (NP). You can also unpublish previously published rulesets.

## Environment Switcher

The Matchmaking Tool allows you to view which rulesets you have published in each environment (either Development or Production). To view different environments, click the Environment Switcher in the upper left-hand corner of the tool.

Environment Switcher

Once you are familiar with how to use the Environment Switcher you can begin publishing and unpublishing rulesets to the Production Environment.

## Publishing a Ruleset

To publish a ruleset:

1. Use the Environment Switcher to go to the Development Environment (sp-int).
2. Select the ruleset you wish to publish, then click the vertical ellipses next to the table.
3. Click **Publish**. A dialog box appears informing you that you are about to publish your selected ruleset to the Production Environment.
4. Click **Yes** to publish or **Cancel** to cancel publishing at this time.

Note:

Be aware that it can take several minutes for a ruleset to completely publish to the Production Environment.

## Unpublishing a Ruleset

To unpublish a ruleset:

1. Use the Environment Switcher to switch to the Development Environment (sp-int).
2. Select the ruleset you wish to unpublish in the table, then click the vertical ellipses.
3. Click **Unpublish**. A dialog box appears warning you that you are unpublishing your selected ruleset.
4. Click **Yes** to unpublish or click **Cancel** to unpublish at another time.

Note: It can take several minutes for a ruleset to completely unpublish from a production environment.

## Status Indicators

Each ruleset has publish and activation statuses in each environment that provide information on where the ruleset is in the publishing process. Statuses are displayed in a table in the row of the corresponding ruleset.

Note: Each status has a colored indicator circle to help distinguish it from the others.

**Publish Status**

Publish statuses include:

* **Not Published** - The ruleset is not currently published in the indicated environment.
* **Publishing** - The ruleset is in the process of being published.
* **Published** - The ruleset is currently published in the indicated environment.
* **Unpublishing** - The ruleset is in the process of no longer being published in the indicated environment.
* **Error Publishing** - There was an error while attempting to publish a ruleset
* **Error Unpublishing** - There was an error while attempting to unpublish a ruleset.

Publishing Status Indicators

**Activation Status**

Activation statuses include:

* **Activating** - The ruleset is currently being made *Active*.
* **Active** - The ruleset is *Active*.
* **Deactivating** - The ruleset is currently being made *Inactive*.
* **Inactive** - The ruleset is *Inactive*.
* **Error** - There was an error activating and/or deactivating the ruleset.

# Viewing Operational History

This topic provides information on how to view operational history of the Matchmaking tool.

The Matchmaking Tool keeps an audit log or operational history so you can view the changes that have been made to the service for a given NP Communication ID. To access the audit log:

1. Click **Operational History**.
2. To toggle back to your rulesets, click **Rulesets**.

Operational History Tab

## Operational History List View

The operational history list view has multiple data points that you can sort by:

* **Date and Time** - The date and time the action occurred.
* **Log Level** - Either *INFO* for information or *ERROR* for errors.
* **Actor** - The name of the individual that took the action.
* **Action** - What the action was that the individual took.
* **Target** - Item the action was taken upon.
* **Summary** - Brief plain text description of the action taken.

## JSON Detail View

You can also view the JSON of the logs themselves. To view the JSON, click the arrow of the log you wish to view.

Operational History