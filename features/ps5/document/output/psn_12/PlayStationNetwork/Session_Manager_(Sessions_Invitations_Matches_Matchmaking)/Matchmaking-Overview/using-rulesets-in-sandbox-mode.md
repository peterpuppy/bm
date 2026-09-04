# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/using-rulesets-in-sandbox-mode.html

# Applying Rulesets (in the Sandbox Network Architecture)

When using the Sandbox network architecture, use the Matchmaking Tool or NP Service Config to create, change and remove rulesets and to apply them to the development environment (DEV) or the production environment (RETAIL). Refer to the [Matchmaking Tool User's Guide](../../../SDK/latest/Matchmaking_Tool-Users_Guide/__document_toc.html) document for details about the Matchmaking Tool. Refer to the [NP Service Config User's Guide](../../../SDK/latest/NP_Service_Config-Users_Guide/__document_toc.html) document for details about NP Service Config.

## Applying Rulesets

Rulesets are written in a Draft in the Matchmaking Tool and in a Service Config file in NP Service Config. The written rulesets are applied to the matchmaking server in the target environment by a Publish operation. While the rulesets needed to be explicitly activated in the Legacy network architecture, this is done automatically in the Sandbox network architecture.

## Removing Rulesets

If you delete the description of the ruleset you wish to remove and perform a Publish operation, it will be applied to the matchmaking server.

## Details of the Processing Performed for a Publish Operation

* If a published ruleset does not exist in the target environment, the ruleset will be created and activated.
* If a ruleset existing in the target environment is excluded from the published content, the ruleset will be deactivated and deleted.
* If a ruleset already exists in the target environment and there are differences from the published content, the processing that is performed depends on whether the differences are in elements that are editable in the Active state. For information about elements that are editable in the Active state, refer to "[Ruleset Activation Status](ruleset-activation-status.html)".
  + If there are differences only in the elements that are editable in the Active state, the ruleset will remain in the Active state and be updated.
  + If there are differences in elements other than those that are editable in the Active state, the ruleset will be recreated. Do not access the ruleset from the application until the Publish operation completes.
* If the ruleset already exists in the target environment and there are no differences in content, the ruleset in the target environment will not be changed.

## Notes on Applying Rulesets to the Production Environment (RETAIL)

* A Publish operation to the production environment (RETAIL) applies all the rulesets in the development environment (DEV) to the matchmaking server in the production environment (RETAIL). Be careful not to include rulesets that you do not plan to use in the production environment (RETAIL).
* A Publish operation to the development environment (DEV) allows changes to be applied by recreating the ruleset even if there are differences in the ruleset that are not editable in the Active state. Note that an error will occur if the same differences exist when publishing to the production environment (RETAIL). This prevents rulesets from accidentally being recreated. If you need to make changes, delete the ruleset, publish, then add the newly changed ruleset and publish once more.