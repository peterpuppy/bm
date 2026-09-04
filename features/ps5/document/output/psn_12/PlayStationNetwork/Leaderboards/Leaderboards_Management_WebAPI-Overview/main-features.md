# Leaderboards Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards_Management_WebAPI-Overview/main-features.html

# Feature Overview

This topic provides basic information for using the Leaderboards Management Web API, explaining its purpose and characteristics, development support features and operation support features, and related documents.

# Purpose and Characteristics

The Leaderboards Management Web API is one of the Management features for back office servers, and it provides a feature that registers multiple score data at the same time, a feature that uploads attachment data in the development environment, a feature to delete scores in the development environment and production environment, and a feature to obtain ranking snapshots. It can be used to provide self-management of the Leaderboards service of PlayStation™Network.

# Main Features

Back office servers can use the Leaderboards Management Web API to perform the following.

* Development support
  + Register scores in the development environment
  + Upload attachment data in the development environment
  + Delete scores registered in the development environment
  + Obtain a list of snapshots of rankings aggregated in the development environment
  + Download snapshots of rankings aggregated in the development environment
* Operation support
  + Delete (invalid or abnormal) scores registered in the production environment
  + Obtain a list of snapshots of rankings aggregated in the production environment
  + Download snapshots of rankings aggregated in the production environment

# Reference Materials

Refer to the following document for information about the Leaderboards service as a whole:

* [Leaderboards Overview](../Leaderboards-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Leaderboards Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Leaderboards_WebAPI-ReleaseNotes.html)