# Leaderboards Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards-Overview/reference-information.html

# Reference Information

The main differences between the Leaderboards service and the old score ranking service are as follows:

* The standard NpWebApi2/NpCppWebApi libraries and the Leaderboards Web API are used instead of the dedicated NpScore library
* "Data unique to a game" (`GameInfo`) and "attached data" (`GameData`) have been renamed as "small-volume attachment data" and "large-volume attachment data", respectively
* Scores and large-volume attachment data can now be recorded atomically
* The amount of time it takes to tabulate scores has been reduced
* The word filter feature is now an independent service

Be aware that the Leaderboards service and the score ranking service lack data-compatibility with one another.