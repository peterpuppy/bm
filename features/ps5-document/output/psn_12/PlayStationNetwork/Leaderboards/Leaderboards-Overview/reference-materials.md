# Leaderboards Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards-Overview/reference-materials.html

# Feature Overview

This topic provides basic information for using the Leaderboards service, explaining its purpose and characteristics, main features, sample programs that use this service, and related documents.

# Purpose and Characteristics

The Leaderboards service provided by PlayStation™Network provides multiple leaderboards onto which scores can be recorded for an application per user (player) and on which rankings are calculated. Settings can be configured for each of the leaderboards - with the settings including the number of users for whom scores can be recorded, conditions for updating scores, and whether to sort in the scores in ascending or descending order. Scores can each be recorded with an attached comment. Arbitrary data within the scope determined by the total size limit can also be attached to scores; this can be used, for example, to add replay data or character data from the time a high score was obtained. There are 3 types of ranking: serial ranking (where identical scores are ranked according to the order by which they are recorded; a score recorded earlier gets a higher ranking), ranking (where identical scores are ranked the same), and all-time highest rankings.

Although Score Ranking is available as a score ranking service for the PlayStation®4 generation, Leaderboards are recommended due to the following benefits.

* Leaderboards reflect tabulated rankings in almost real time, whereas with Score Ranking this can take from few minutes to over ten minutes.
* Leaderboards have a larger storage limit than Score Ranking for large-volume attachment data.
* The same implementation can be used for PlayStation®5 and PlayStation®4 versions.

Note:

To allow the reader to understand the Leaderboards service as a whole, in places, this document describes features that are not yet supported. For details, refer to the release notes.

# Main Features

The main features provided by the Leaderboards service are as follows.

* The Leaderboards Web API, which is primarily used by console-based applications
  + Recording scores
  + Obtaining rankings
  + Recording and obtaining large-volume attachment data
  + Obtaining leaderboard information
* The Leaderboards Tool, with which you can configure the title and each leaderboard and create test data
  + Configuring services
  + Configuring leaderboards
  + Creating score data for testing
  + Applying settings
  + Configuring ranking snapshot output schedules
  + Configuring score reset schedules
* The Leaderboards Management Web API, which is for managing recorded scores
  + Recording and deleting scores
  + Recording large-volume attachment data
  + Obtaining ranking snapshots

# Sample Program

The following sample program using the Leaderboards service is available for your reference. Refer to [Sample Program Overview](../../../SDK/latest/Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

## sample\_code/playstation\_network/api\_webapi\_leaderboards

This sample shows the basic procedure for using the Leaderboards service.

# Reference Materials

For information about the NpWebApi2 library and the NpCppWebApi library, which are used when calls are made by an application to the Leaderboards Web API, refer to the following documents:

* [NpWebApi2 Library Overview](../../../SDK/latest/NpWebApi2-Overview/__document_toc.html), [NpWebApi2 Library Reference](../../../SDK/latest/NpWebApi2-Reference/__document_toc.html)
* [NpCppWebApi Library Overview](../../../SDK/latest/NpCppWebApi-Overview/__document_toc.html), [NpCppWebApi Library Reference](../../../SDK/latest/NpCppWebApi-Reference/__document_toc.html)

In addition to this document, refer to the following document for information about the Leaderboards Web API:

* [Leaderboards Web API Reference](../Leaderboards_WebAPI-Reference/__document_toc.html)

In addition to this document, refer to the following documents for information about the Leaderboards Management Web API:

* [Leaderboards Management Web API Overview](../Leaderboards_Management_WebAPI-Overview/__document_toc.html) and [Leaderboards Management Web API Reference](../Leaderboards_Management_WebAPI-Reference/__document_toc.html)

Refer to the following documents for details about the Sandbox network architecture:

* [Sandbox Network Architecture Guide](../../../SDK/latest/Sandbox_Network_Architecture-Guide/__document_toc.html)
* [NP Service Config User's Guide](../../../SDK/latest/NP_Service_Config-Users_Guide/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Leaderboards Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Leaderboards_WebAPI-ReleaseNotes.html)
* [Release Notes - Leaderboards](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Leaderboards-ReleaseNotes.html)