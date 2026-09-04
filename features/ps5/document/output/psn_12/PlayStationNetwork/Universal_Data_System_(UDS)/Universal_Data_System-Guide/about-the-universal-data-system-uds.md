# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/about-the-universal-data-system-uds.html

# About the Universal Data System (UDS)

The Universal Data System (UDS) is a part of the data platform that collects various
in-game events as well as actions of players and standardizes this information as
UDS model data.

It then provides this data to various cross-title platform features.
PlayStation®5 is able to provide richer game experiences to users and enhance user
engagement with games.

Prior to PlayStation®5, in order to provide in-game information to platform features,
separate libraries and APIs had to be used per platform feature. UDS unifies the interface
for game developers. In some cases, it is possible for information provided by a game
application to be used as-is by a new platform feature without any changes or additions.

The following SDK features use UDS:

* **Trophy System** -- The Trophy System rewards users upon accomplishing various missions in the game
  and keeps a record of these accomplishments. When the user clears certain conditions
  in a game, such as defeating a certain boss, winning a particular race, or meeting
  a character in a specific situation, a trophy is awarded. The trophy collection is
  the system software's onscreen display of trophies earned by the user, as well as
  the trophies yet to be earned. Such a system can reward the user with a sense of accomplishment,
  and motivate the user to continue playing a game.
* **Game Help** -- Game Help provides on-demand, spoiler-free help based on the player's current
  game progress. This allows players to spend more of their console playtime on gameplay
  and minimizes the time spent looking for help content. It also minimizes the risk
  of encountering spoilers, and so increases their game satisfaction.
* **Matches** -- This feature displays the states as well as the results of competitive cooperative
  gameplay on the system software screen.
* **Media Auto-Tagging** -- This feature adds in-game contextual information to media such as screenshots
  taken or video clips recorded and edited by the user. For example, information that
  indicates the gameplay state (such as the stage name or character name) can be sent
  to UDS so that the information can be used as a tag to search media.
* **Spoiler Block** -- This feature is an extension of Media Auto-Tagging. It displays a warning when
  the user attempts to view content that is related to what the user has not yet played.
* **Perspectives** -- The Perspectives feature displays publicly available user-generated content (UGC)
  relevant to the user's current gameplay progress, based on the activities they have
  successfully completed. This enables users to learn new gameplay strategies by viewing
  personalized, spoiler-free videos.
* **Tournaments** -- The Tournaments service hosts organized competitions in a bracket format at the
  platform-level for applications. You can create and schedule automated tournaments
  related to competitive activities.

# Components of UDS

This topic highlights the components that make up the Universal Data System.

The Universal Data System consists of three key components.

* Data Processing
* Stats Management
* State Tracking

A UDS Event sent by a game application is validated and processed for use and dispatched
to each service.

# UDS Architecture

This topic shows where UDS fits in the application development lifecycle.

UDS Architecture

# Offline Support

UDS also supports operation in an offline environment. If a console is disconnected
from the Internet, UDS events sent by a game application are stored in temporary storage
and sent to the UDS server when the console goes online again.

Note:

There is a limit on the temporary storage space. When the upper limit of 1 MiB is
reached per game and per user, UDS events are deleted starting from the oldest.

# Data Reliability

This topic highlights different scenarios in which UDS event data is delayed or lost.

UDS events sent by game applications can be delayed or lost in the following cases:

* When a UDS event that exceeds the temporary storage's upper limit of 1 MiB is sent when offline.
* When the number of UDS events a game sends exceeds the rate limit, the system stops receiving the event for a while. The rate limit is 300 UDS events within 5 minutes (per instance of game).

  Note:

  Stats, state and trophy data are managed in a reliable storage and it is not affected even when a UDS event is lost.

If your game needs to send a large amount of UDS events at the same time, limit the number of events sent to under 300 every five minutes. Additionally, events that are sent simultaneously should be sent in batches of 64 events per batch, with five second intervals between each batch.

# Related Information

In addition to this document, SIE also provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements.

You can refer to the release notes below:

* [Release Notes - Universal Data System Management Tool](../ReleaseNotes/PlayStation_Network-UniversalDataSystem_Management_Tool-ReleaseNotes.html)