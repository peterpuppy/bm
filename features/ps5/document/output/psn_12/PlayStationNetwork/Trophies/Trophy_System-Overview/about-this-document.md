# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/about-this-document.html

# About This Document

This section describes who this document is intended for and the kind of background knowledge the target audience is expected to have.

## Audience

The behavior of the entire trophy system and the rules for configuring trophies to match game content are explained in each of the following topics, which are intended primarily for game designers.

* [Game Play and the Trophy System](game-play-and-the-trophy-system.html "This topic provides an overview of the trophy system. The configuration and behavior of the system will be explained in relation to game play.")
* [Trophy Set Configuration](trophy-set-configuration.html "This topic describes the set of trophies prepared for a single title, as well as the multilingual support for each trophy's attributes and text information.")
* [Trophy Set Design Policy](trophy-set-design-policy.html "This topic describes the policy for how many trophies to make available and when to make them obtainable in the game.")

An overview of the development process is explained in each of the following topics, which are intended primarily for game developers and managers.

* [Overview of Application Development](overview-of-application-development.html "This topic describes trophy-related processing you need to perform during the application development process.")
* [Debugging Support Provided by the System Software](debugging-support-provided-by-the-system-software.html "This topic describes the debugging support features provided by the system software that are related to trophies.")

Specifications of the trophy configuration data (trophy assets), including trophy names and icons, are explained in the following topics, which are intended primarily for artists.

* [Creating Trophy Configuration Data](creating-trophy-configuration-data.html "This topic describes the composition of trophy configuration data (trophy assets) and a summary of how to create this data, along with the specifications for the data. An example of what is displayed onscreen is provided in \"Reference: Displaying of Trophies by the System Software\" for you to refer to if necessary.")

## Background Knowledge

This document has been written with the assumption that the reader has a small degree of background knowledge. This background knowledge is explained in the following documents, which you can refer to as needed.

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html): An overview of PlayStation™Network features is provided.
* [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html): An overview of the Universal Data System that forms the basis of the trophy system, the procedure for developing applications, and the procedure for using a tool for defining and configuring trophy sets are provided.
* [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html): Methods for obtaining trophy configuration files are explained.
* [NpTrophy2 Library Overview](../NpTrophy2-Overview/__document_toc.html) and [NpTrophy2 Library Reference](../NpTrophy2-Reference/__document_toc.html): Descriptions are provided regarding the NpTrophy2 library used to allow applications to obtain trophy configuration data and trophy records.
* [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html) and [NpUniversalDataSystem Library Reference](../NpUniversalDataSystem-Reference/__document_toc.html): Descriptions are provided regarding the NpUniversalDataSystem library, which is used to award trophies to users.
* [Release Notes - NpTrophy2 Library](../ReleaseNotes/PlayStation_Network-NpTrophy2-ReleaseNotes.html): Provides information about bugs, notes, restrictions, and announcements.