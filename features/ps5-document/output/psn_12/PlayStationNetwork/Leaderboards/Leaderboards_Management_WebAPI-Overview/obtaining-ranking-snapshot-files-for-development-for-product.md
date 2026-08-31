# Leaderboards Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards_Management_WebAPI-Overview/obtaining-ranking-snapshot-files-for-development-for-product.html

# Usage

This topic explains how to use the Leaderboards Management Web API along with use cases.

# Registering Scores [for Development]

A leaderboard can be specified, and scores can be registered.

This feature is intended for various testing purposes in the development environment including registering scores for the maximum number of users set for a leaderboard, registering the highest possible score that can be registered, registering the lowest score that can be registered, and registering scores for a user that is a friend.

Note:

A comment can optionally be recorded when a score is recorded. The content of the specified comment will be checked on the server side; if any inappropriate words are included, they will be masked automatically. The official ranking of the score will not be calculated or made public until checking and masking of the comment is complete. Although the official ranking is calculated at the point when any comment has finished being checked and masked, that calculation will be based on the time when the score finished being recorded, not on the time when the comment is finished being checked and masked.

# Uploading Attachment Data [for Development]

A leaderboard can be specified, and attachment data can be uploaded to a score that has a high enough ranking that the uploading of data is permitted. The attachment data can be tested in the development environment without having to upload attachment data from the application.

# Deleting Scores [for Development] [for Production]

A leaderboard can be specified and scores of a specified user can be deleted. This feature is intended for deleting test data in the development environment and for deleting invalid scores (for example) in the production environment.

# Obtaining a List of Ranking Snapshots [for Development] [for Production]

A leaderboard can be specified, and a list of ranking snapshots created by setting schedules using the Leaderboards Tool can be obtained. This feature is expected be used in the production environment for collecting information to bulk-download ranking snapshots for the purpose of, for example, automating the distribution of rewards based on rankings. Use it for testing such automated solutions in the development environment.

# Obtaining Ranking Snapshot Files [for Development] [for Production]

Snapshot files (zip) can be obtained by specifying unique ranking snapshot identifiers. Like the feature for obtaining a list of ranking snapshots described earlier, this feature is expected be used in the production environment for collecting information to bulk-download ranking snapshots for the purpose of, for example, automating the distribution of rewards based on rankings. Use it for testing such automated solutions in the development environment.