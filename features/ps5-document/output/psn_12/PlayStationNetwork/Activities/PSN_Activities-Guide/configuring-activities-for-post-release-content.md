# PlayStation™Network Activities Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Activities-Guide/configuring-activities-for-post-release-content.html

# Configuring Activities for Post Release Content

This chapter provides guidance on creating activities for games that feature post-release content such as downloadable content and user generated content.

When creating activities for post-release content, follow the guidance that most applies to the game modes featured in that content:

* [Configuring Activities for Campaign and Story Modes](configuring-campaign-or-story-modes.html "This chapter provides details on how to configure activities for games that feature campaign and story modes.")
* [Configuring Activities for Repeatable and Endless Modes](configuring-repeatable-or-endless-modes.html "This chapter provides guidance on configuring activities for games that feature repeatable or endless modes.")
* [Configuring Activities for PVP Online Multiplayer Modes](configuring-multiplayer-activities.html "This chapter provides guidance on creating activities for games with online multiplayer modes.")

As well as the extended guidance below:

* Adding activities requires updates to your game, so it may be helpful to have these ready when you are submitting your game for the update certification process.
* If you’ve configured activities to cover post-release content, they are visible as soon as they are published to production. If you don’t want players to see these activities until the content is available, [use the *Available From* field to indicate a date from when content is available](hiding-activities.html "This topic provides information on hiding activities in the PlayStation®5 UI.").
* If you’re adding progress activities for new campaign or story content, consider when to enable **Is Required For Completion**. Setting new activities as required impacts the game progress percentage displayed on the Game Hub. Adding new required activities will affect this percentage for all players. If your content is optional, do not enable **Is Required For Completion**, especially if the content requires additional payment to access.