# Matches Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matches_WebAPI-Overview/reference-materials.html

# Web API Overview

# Purpose and Characteristics

The Matches Web API is for recording/reflecting information about multi-play sessions in which players have engaged on PlayStation™Network servers. In this context, "multi-play" includes local play versus the computer, as well as online competitive/cooperative play.

Included within multi-play information are game modes ("team deathmatch", "capture-the-flag", etc.), participants (including computer-controlled participants and players on other platforms), conditions during play, and results. The Matches Web API provides features for compiling this information into "matches," updating the information contained therein, and recording the information on servers for PlayStation™Network. Via the Matches Web API, users can view this recorded information as their own gameplay histories on the system software.

The Matches Web API can be called from an application server (client-credentialed), as well as from an application for PlayStation®5. To make calls from an application server, you must be issued a Client ID; to ask for this to be done, make an inquiry via Private Support's "Post new issue" page (<https://game.develop.playstation.net/support>).

# Main Features

The main features provided by the Matches Web API are as follows.

* A feature to create matches
* A feature to update match details
* A feature to update match statuses
* A feature to update information concerning match participants and participating teams
* A feature to report match results and stats
* A feature to obtain detailed information concerning matches

# Sample Program

A sample program using the Matches Web API is as follows.

## sample\_code/playstation\_network/api\_webapi\_session\_manager

This sample exemplifies basic usage of Player Sessions/Game Sessions and the Matches Web API.

# Reference Materials

For common rules for Web APIs, how to use them, and so forth, refer to the following document.

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

Refer to the following documents if using the Web API from an application.

* [NpWebApi2 Library Overview](../../../SDK/latest/NpWebApi2-Overview/__document_toc.html)
* [NpCppWebApi Library Overview](../../../SDK/latest/NpCppWebApi-Overview/__document_toc.html)

For how to define activities used for matches, refer to the following documents.

* [Universal Data System Guide](../../../SDK/latest/Universal_Data_System-Guide/__document_toc.html)

For information about other multi-play-related services, refer to the following document.

* [Session Manager Service Overview](../../../SDK/latest/Session_Manager_Service-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Matches Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Matches_WebAPI-ReleaseNotes.html)