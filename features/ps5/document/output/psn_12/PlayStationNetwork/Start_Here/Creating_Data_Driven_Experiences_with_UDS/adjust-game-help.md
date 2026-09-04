# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/adjust-game-help.html

# Launch Prep / Post Launch

You can perform various "launch prep" or "post launch" tasks that do not require creating a
patch package or a new NP Config Tag. However, any change to trophy configuration, including
localization, requires a patch package and new NP Config Tag.

In general, adding new PSN
objects or supported languages will require a patch package and a new NP Config Tag.
Conversely, updating localization for existing supported languages or updating existing PSN
objects does not require a patch. For more information, see [Universal Data System Guide -
Preparing a Package for Release - Configuration Change After the Release](../Universal_Data_System-Guide/configuration-change-after-the-release.html) and [Universal Data
System Guide - Using the UDS Management Tool - Configuring the UDS Data Model](../Universal_Data_System-Guide/configuring-the-uds-data-model.html).

# Adjust Game Help

This topic provides information on adjusting game help configuration. If you have already configured Game Help hints as part of your development and internal QA process, then you can use the Game Help Tool to adjust them pre-launch or post-launch.

You can update the Game Help hints that correspond to your existing activities without
submitting a patch to update your product. Typically, the final media assets used for hints
will not be available during development. Therefore, you can use the Game Help Tool to add
them before your game launch.

If you have not configured any Game Help hints by the time you package and submit
your product, then you can still do so before or after launch. Note, however, that
you will be limited to the defined activity entities and their associated properties.
While these defined activity entities can be updated without a patch, if you require
new activity entities for your hints, then you must submit a patch update to add them.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Game Help Guide](../PSN_Game_Help-Guide/__document_toc.html) | Explains how to create hints and upload media assets. |

# Adjust Localization (Activities)

This topic provides information on adjusting localization for activities. If you have already provided the localization of your activities as part of your development and internal QA process, then you can adjust them pre-launch or post-launch.

You can update the localized text through the UDS Management Tool, Universal Data System
Configuration Web API or UBP for each of your existing supported languages and activities
without submitting a patch to update your product.

If you have not provided any localized text by the time you package and submit your
product, then you can still do so before launch. Note, however, that you will be limited
to the defined supported languages and activity entities.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) | Contains information on localizing PSN objects and subcategories. For specific sections, see Add Localization (Activities, Subcategories, and Trophies). |
| [Universal Data System Guide - Preparing a Package for Release - Configuration Change After the Release](../Universal_Data_System-Guide/configuration-change-after-the-release.html) and [Universal Data System Guide - Using the UDS Management Tool - Configuring the UDS Data Model](../Universal_Data_System-Guide/configuring-the-uds-data-model.html) | For adjusting localization purposes, the "Edit" entries on this page show the entities you can update after the Platform Certification and Operations review is completed. |