# PlayStation™Network Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN-Overview/data-platform.html

# Data Platform

The Data Platform, which includes the Universal Data System (UDS), Trophies, Server Storage, Leaderboards, and Game Help, is a suite of services that helps to create a strong engagement loop between the game experience and the platform experience.

This can keep players engaged with their games, even when they are not in the game or are away from their console. It can also keep players focused on their games when they are playing, by reducing the time spent looking for help. For example:

* Recommending next best game activities or Trophies based on current game progress.
* Estimating playtime to complete next game activities, to encourage players to play more frequently.
* Providing contextual help when players are stuck in a game section, to get back to the game quickly.

# Universal Data System

The Universal Data System (UDS) is a service that transmits player data from a game to the console, uploads it to PlayStation™Network servers, stores it securely, and uses it to power real-time, player-facing and developer-facing experiences.

UDS provides a streamlined way for games to integrate with multiple data-driven experiences by using a single API set to transmit all of the game data. For details, refer to the following document:

* [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html)

## Universal Data System Configuration Web API

The Universal Data System Configuration Web API provides features for managing back-office servers and for configuring PlayStation™Network objects, UDS events and UDS stats. The ability to call these Web APIs from your own code provides additional flexibility for your development efforts. For details, refer to the following document:

* [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html)

# Trophies

Trophies are unlocked when users complete activities set in an application. Players can share the trophies that they have unlocked with their friends on PlayStation™Network, and compete with each other to achieve higher levels.

Levels are determined by accumulating points, which correspond to the number and grades of
trophies unlocked. The trophy system on PlayStation®5 is powered by the Universal Data
System and progress towards unlocking a trophy is tracked and shown on PlayStation®5
platform. For details of the trophy system, refer to the [Trophy System Overview](../Trophy_System-Overview/__document_toc.html).

## NPTrophy2 Library

The NPTrophy2 library provides an API for the application to obtain the configuration and unlock state of trophies. For details, refer to the following documents:

* [NpTrophy2 Library Overview](../NpTrophy2-Overview/__document_toc.html)
* [NpTrophy2 Library Reference](../NpTrophy2-Reference/__document_toc.html)

# Server Storage

The PlayStation™Network provides server storage where an application can store and reference arbitrary data. A space is allocated to each title, and an area is allocated to each user of a title. Together, the user and title spaces are called the Title Cloud Storage.

The space allocated to a title can be used to implement functionality, for example dynamically changing the game regulations of an online session, or calculating the average or total score of all players worldwide. The space allocated to each user can, for example, be used to store attributes online.

## Title Cloud Storage Web API

The Title Cloud Storage Web API is used for accessing title cloud storage. Game applications can use the Web API to upload and download binary or numeric data from the cloud storage. For details, refer to the following documents:

* [Title Cloud Storage Service Overview](../../../WebAPI/latest/TCS-Overview/__document_toc.html)
* [Title Cloud Storage Web API Reference](../../../WebAPI/latest/TCS_WebAPI-Reference/__document_toc.html)

## Title Cloud Storage Management Web API

The Title Cloud Storage Management Web API is used by back office websites to upload, modify or delete data in title cloud storage. Its main purpose is managing data in production environments. It can also be used to upload data to title cloud storage for application testing in the development environment. For details, refer to the following documents:

* [Title Cloud Storage Management Web API Overview](../../../WebAPI/latest/TCS_Management_WebAPI-Overview/__document_toc.html)
* [Title Cloud Storage Management Web API Reference](../../../WebAPI/latest/TCS_Management_WebAPI-Reference/__document_toc.html)

# Leaderboards

PlayStation™Network provides leaderboards where users can register high scores and compete with each other.

Developers can create multiple leaderboards per title and can customize each leaderboard -
such as deciding to rank by highest scores or fastest times, setting the number of top
registration entries that can be made, choosing whether or not to enable comments or replay
data attachments, and so on. Applications can register and reference leaderboard data using
an API.

## Leaderboards Web API

Game applications and application servers can use the Leaderboards Web API to register and read scores on leaderboards. For details, refer to the following documents:

* [Leaderboards Overview](../../../WebAPI/latest/Leaderboards-Overview/__document_toc.html)
* [Leaderboards Web API Reference](../../../WebAPI/latest/Leaderboards_WebAPI-Reference/__document_toc.html)

## Leaderboards Management Web API

Back office websites can use the Leaderboards Management Web API in the development environment to register multiple scores in bulk and upload attachment data, and in both the development and production environments to delete registered scores. For details, refer to the following documents:

* [Leaderboards Management Web API Overview](../../../WebAPI/latest/Leaderboards_Management_WebAPI-Overview/__document_toc.html)
* [Leaderboards Management Web API Reference](../../../WebAPI/latest/Leaderboards_Management_WebAPI-Reference/__document_toc.html)

# Game Help

Game Help provides on-demand, spoiler-free help to players based on knowledge of where
they are in the game, to get them back into the game as quickly and seamlessly as
possible.

Game Help is powered by the Universal Data System. For details, refer to the following
document:

* [PlayStation™Network Game Help Guide](../PSN_Game_Help-Guide/__document_toc.html)

# Challenge Activities

This topic links to resources for learning more about challenge activities. A
challenge activity is a repeatable activity that displays rankings in leaderboard format based
on the outcome of asynchronous gameplay results.

Leaderboards are shown at the platform level and the system generates appropriate cohorts
(global and friends-only) according to user-specific data. For details, refer to the
following document:

* [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html)