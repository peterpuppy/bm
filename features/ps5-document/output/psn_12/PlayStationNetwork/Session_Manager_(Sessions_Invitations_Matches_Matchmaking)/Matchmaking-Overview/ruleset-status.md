# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/ruleset-status.html

# Ruleset Statuses

This chapter explains the activation statuses and publish statuses of rulesets.

# Ruleset Activation Status

Rulesets can have any of the following five activation statuses:

* Inactive
* Activating
* Active
* Deactivating
* Error

Transitions Among Ruleset Activation Statuses

When using the Legacy network architecture, developers must use the Matchmaking Tool to pre-activate the rulesets they wish to use. When activation completes and the ruleset becomes Active, the ruleset will be applied to the matchmaking server, and the application will be able to use the ruleset.

The editing operations that can be performed on a ruleset differ depending on its activation status.

* Inactive:
  + All items except for the ruleset name are editable.
  + The ruleset can be deleted.
* Active:
  + Only the matchmaking rule definitions can be edited. When editing is finished, the edited rule is applied immediately.

The following activation statuses cannot be edited whatsoever.

* Activating:
  + The server is currently conducting activation processing.
* Deactivating:
  + The server is currently conducting deactivation processing.
* Error:
  + When a server error of some sort occurs during activation processing, the status of the ruleset transitions to Error. If the status transitions to Error, the ruleset is no longer being applied, but deactivation must be performed again to resolve the server error.

# Ruleset Publish Status

Rulesets in the development environment (sp-int) of the Legacy network architecture have publish statuses. (Rulesets in the Sandbox network architecture do not have publish statuses). Rulesets can have any of the following six publish statuses:

* Not Published
* Publishing
* Published
* Unpublishing
* Publish Error
* Unpublish Error

Transitions Among Ruleset Publish Statuses

In order for a ruleset to be applied to the production environment (RETAIL), it must first be activated and published using the Matchmaking Tool. When the Publish operation completes and the status changes to Published, the ruleset will be applied to the matchmaking server in the production environment (RETAIL) and will be available for use by the application.

The editing operations that can be performed on a ruleset differ depending on its publish status.

* Not Published:
  + Refer to the editing operations that can be performed for each activation status.
* Published:
  + Only the matchmaking rule definitions can be edited. In order for the rules to be applied to the production environment (RETAIL) after editing, the ruleset must be re-published.

The following publish statuses cannot be edited whatsoever.

* Publishing:
  + The server is currently in the process of publishing.
* Unpublishing:
  + The server is currently in the process of unpublishing.
* Publish Error:
  + If a server error of some sort occurs during the publishing process, the status of the ruleset will transition to Publish Error. If you have a Publish Error, publishing must be performed again to resolve the server error.
* Unpublish Error:
  + If a server error of some sort occurs during the unpublishing process, the status of the ruleset will transition to Unpublish Error. If you have an Unpublish Error, publishing must be performed again to resolve the server error.