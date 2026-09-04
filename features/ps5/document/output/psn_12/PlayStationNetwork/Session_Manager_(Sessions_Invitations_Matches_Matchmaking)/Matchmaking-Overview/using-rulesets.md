# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/using-rulesets.html

# Applying Rulesets (in the Legacy Network Architecture)

When using the Legacy network architecture, use the Matchmaking Tool to create, change and remove rulesets and to apply them to the development environment (sp-int) or the production environment (RETAIL). Refer to the [Matchmaking Tool User's Guide](../../../SDK/latest/Matchmaking_Tool-Users_Guide/__document_toc.html) document for details about the Matchmaking Tool.

## Applying Rulesets

Ruleset application must be carried out separately for each environment. An applied ruleset will be available for use by the application on the matchmaking server of each environment. A ruleset to be applied to the production environment (RETAIL) must also always be applied to the development environment (sp-int).

1. Development environment (sp-int): "Activate"

   "Activate" the application-target ruleset. Once the activation status transitions from "Activating" to "Active" (this may take a few minutes), the ruleset will be applied to the matchmaking server in the development environment (sp-int) and will be available for use by the application.
2. Production environment (RETAIL): "Publish"

   "Publish" the ruleset you want to apply to the production environment (RETAIL) from the development environment (sp-int). The applicable ruleset must be set to "Activate" in the development environment (sp-int) in advance. Once the publish status transitions from "Publishing" to "Published" (this may take a few minutes), the ruleset will be applied to the matchmaking server in the production environment (RETAIL) and will be available for use by the application.

## Removing Rulesets

Rulesets must be removed separately for each environment. Once a ruleset is removed, it can no longer be used by the application on the matchmaking server of each environment. A ruleset that is applied to the production environment (RETAIL) can't be removed from the development environment (sp-int). Even if a ruleset is removed, its entry will remain in the Matchmaking Tool and can be re-applied as necessary.

1. Production environment (RETAIL): "Unpublish"

   "Unpublish" the ruleset to be removed. Once the publish status transitions from "Unpublishing" to "Not Published" (this may take a few minutes), the ruleset can no longer be used by the application on the matchmaking server in the production environment (RETAIL).
2. Development environment (sp-int): "Deactivate"

   "Deactivate" the ruleset to be removed. Once the activation status transitions from "Deactivating" to "Inactive" (this may take a few minutes), the ruleset can no longer be used by the application on the matchmaking server in the development environment (sp-int). In addition, because a ruleset applied to the production environment (RETAIL) can't be removed from the development environment (sp-int), it must first be removed from the production environment (RETAIL).

## Changing Matchmaking Rules or Relaxed Rules

Defined matchmaking rules and relaxed rules can't be changed without the removal of the applied ruleset. The method to change matchmaking rules differs between the development environment (sp-int) and the production environment (RETAIL). A change can't be made just in the production environment (RETAIL). A change must first be made in the development environment (sp-int) and then applied to the production environment (RETAIL).

1. Making changes in the development environment (sp-int)

   Change the matching rules or relaxed rules of the applicable ruleset (using the Matchmaking Tool in the same manner as when the rules were defined). When changes are successfully made, the changed ruleset will be applied to the matchmaking server in the development environment (sp-int) and will be available for use by the application.
2. "Re-publish" to the production environment (RETAIL)

   After making changes to the ruleset in the development environment (sp-int), "Re-publish" it to the production environment (RETAIL). When "Re-publish" succeeds, the ruleset will be applied to the matchmaking server in the production environment (RETAIL) and will be available for use by the application.

## Changing Team Definitions or Attribute Definitions

To change team definitions or attribute definitions of an applied ruleset, the ruleset must first be removed from the applicable environment. To change team or attribute definitions of a ruleset applied to the production environment (RETAIL), follow the procedure below to remove the ruleset from both the production environment (RETAIL) and development environment (sp-int), make the changes, and reapply the ruleset.

1. "Unpublish" in the production environment (RETAIL)
2. "Deactivate" in the development environment (sp-int)
3. Make changes in the development environment (sp-int)
4. "Activate" in the development environment (sp-int)
5. "Publish" to the production environment (RETAIL)