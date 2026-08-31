# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/develop-experiences.html

# Develop Experiences

This topic provides an overview of the general procedure for developing data-driven
experiences.

The outcome from the previous workflow phase is that you have begun to define the UDS data
model by identifying some of the data and entities that will be required to create your
designed experiences. The next step is to configure the PlayStation™Network data objects
and UDS entities.

You can use any combination of the following methods for defining PSN objects and
UDS entities:

1. Create individual entities using the UDS Management Tool.
2. Use the UDS Management Tool bulk import features.
3. Use the User Bucket for Partners (UBP) to bulk upload files via SFTP.
4. Use the UDS Configuration Web API to create and manage entities in bulk.

   Note:
   Each of the bulk configuration methods uses its own JSON schema, which are detailed
   in the applicable documents listed in the following sections.

As you begin developing your experiences, consider viewing the UDS Lessons Learned
- Ratchet & Clank: Rift Apart video on DevNet at the following link. This video can
give you an idea of what to expect during the development process.

<https://p.siedev.net/docs/uds_lesson_learned#uds_lessons_learned>

# Configure UDS Data (PSN objects, UDS events, UDS stats)

This topic provides an overview of the general procedure for configuring UDS entities.

Configuring UDS data entails defining the individual properties that comprise your various
PlayStation™Network objects, UDS events, and UDS stats. At this stage, it is assumed that
you understand the distinction and purpose of each of these entities. If you do not, then
please refer to [Define Your UDS
Data Model](define-your-uds-data-model.html "As you learn about and begin designing each of the data-driven experiences you want to offer, you can start defining the UDS data model entities that enable them. These entities correspond to your game's various content and each have their own purpose, properties, and use cases depending on the experiences you want to provide.") and its related documentation.

A typical workflow for creating entities is as follows:

1. Add the supported languages for your product.
2. Define the subcategories that your activities will be assigned to.
3. Create your activity objects.
4. Define your UDS events.
5. (Optional) Define any UDS stats needed for progress-based trophies.
6. (Optional) Create your zone, mechanic, and actor objects.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) | Provides explanations and descriptions of the various UDS entities that comprise the UDS data model. This is required reading if you have not already done so as part of Define Your UDS Data Model.  You can use the UDS Management Tool to configure entities in bulk. See [Universal Data System Guide - Using the UDS Management Tool - Bulk Configuring UDS Entities](../Universal_Data_System-Guide/bulk-configuring-uds-entities.html). |
| [Universal Data System Configuration Web API Overview](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Overview/__document_toc.html) and [Universal Data System Configuration Web API Reference](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Reference/__document_toc.html) | The overview document explains the usage of the Web API, which enables you to configure PSN objects, UDS events and UDS stats. This Web API aids in flexibility in the development pipeline by enabling you to embed the API into your own system.  The reference document provides the operations you can perform to configure UDS entities. |
| [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html) | Provides useful best practices and examples for creating different types of activities. |

# Configure Trophies

This topic links to the services you'll use when creating and configuring trophies.
You can create trophies in the UDS Management Tool and include trophy configuration
information in the package file that is required for internal QA testing and
submission.

As a result, your trophies, including valid icon images, must be configured before you
create your package files for final QA or submission. Any changes to trophies after your
game has been published require a patch to be submitted. Note that for progress-based
trophies, you will need to define the UDS events and UDS stats that can trigger a trophy
unlock condition.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Trophy System Overview](../Trophy_System-Overview/__document_toc.html) | Provides relevant information about the entire trophy system and the overall trophy development process. This is required reading if you have not already done so as part of [Design Your Trophies](design-your-trophies.html "This topic links to the services you'll use when creating and designing trophies for your game."). |
| [Universal Data System Guide - Using the UDS Management Tool - Trophy Tool](../Universal_Data_System-Guide/trophy-tool.html) | Contains a section on how to use the Trophy Tool component of the UDS Management Tool, which is used for creating and managing your trophies. |

# Configure Tournaments

This topic provides links to services you'll use when configuring tournaments.

You can create PlayStation®5 tournaments in the UDS Management Tool after requesting
the PlayStation®5 Tournaments Service for your title. Proper configuration of tournaments
requires updates to game intent, the matches web API integration, and activities.
Once title integration is complete, you can configure tournaments using UDS. Configuration
is split between tournament rules, metadata, and scheduling. Rules define who will
be eligible for tournaments based on game stats, age, and country requirements, as
well as the size of the tournament brackets the tournament service creates. Metadata
gives your players information about the tournament such as name and game mode. Scheduling
defines when tournaments take place.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation®5 Tournaments Guide](../PS5_Tournaments-Guide/__document_toc.html) | Provides relevant information about the tournament system with a focus on integration, design, and testing requirements. |

# Configure Game Help

This topic provides an overview of the procedure for configuring game help hints. Game help hints correspond to specific activities and trophies that you have defined.

Game help hints correspond to specific activities and trophies that you have defined.
Game help configuration is performed in the following stages:

1. Set up UDS data, as described in Configure UDS Data (PSN objects, UDS events, UDS
   stats).

   This step is essentially the configuration of the activities that your hints will
   correspond to. These activities must be finalized before the creation of your release-ready
   package file.
2. Configure your Game Help hints.

   This step involves defining your hints using the Game Help Tool. If desired you can
   define your hints during development so that they can be internally tested before
   package creation. However, hint configuration is not required for the submission process
   or your game launch. You can define your hints and certain properties belonging to
   their associated activities after the submission process and before or after your
   game launch.
3. Provide hint assets, as described under [Adjust Game Help](adjust-game-help.html "This topic provides information on adjusting game help configuration. If you have already configured Game Help hints as part of your development and internal QA process, then you can use the Game Help Tool to adjust them pre-launch or post-launch.").

   This step is the addition of the final image and video assets that can be included
   in your hints. This task can be performed in the Game Help Tool and does not require
   repackaging or patching your product.

You can use draft hints and assets for testing your hints in the development environment.
Typically, however, the hint assets will not be final because your game is still in
development. Therefore, the pre-launch task of providing your final hint assets is
expected to occur as part of the Adjust Game Help task.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Game Help Guide](../PSN_Game_Help-Guide/__document_toc.html) | Provides useful best practices and suggestions for creating different types of Game Help. |
| [PlayStation™Network Game Help Guide](../PSN_Game_Help-Guide/__document_toc.html) | Explains how to create hints and add media assets. Note that bulk configuration of hints has its own JSON schema and UBP upload procedure, which are detailed in this document. |

# Implement and Debug

This topic links to the libraries and services you'll use to send data from your game
to the UDS server.

You can use the various SDK libraries highlighted below to implement the functionality
that sends data from your game to the UDS server. Likewise, the documents and specific
sections mentioned below are important to read and understand when debugging your
experiences during development. During the development process, it is a good idea
to be aware of the TRC checks that are made for these experiences, which you can find
detailed in the [Create and Submit Package](create-and-submit-package.html "This topic provides an overview of the procedure for creating and submitting a package.") section.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html) and [NpUniversalDataSystem Library Reference](../NpUniversalDataSystem-Reference/__document_toc.html) | This library provides functions for sending various information (UDS events) in an application to the UDS server.  For debugging, read the following section: [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html). This section explains how to delete UDS-related data (for example unsent events and UDS stats) from the system for testing purposes. |
| [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html) | Explains the purpose of the game intent system, which includes the game intent events that you create. Game intent events let players quickly join sessions, accept invitations, and launch activities. |
| [NpGameIntent Library Overview](../NpGameIntent-Overview/__document_toc.html) and [NpGameIntent Library Reference](../NpGameIntent-Reference/__document_toc.html) | Explains how to use the NpGameIntent library, which lets your game receive game intent events from the system. |
| [Active Activities Web API Overview](../../../WebAPI/latest/Active_Activities_WebAPI-Overview/__document_toc.html) and [Active Activities Web API Reference](../../../WebAPI/latest/Active_Activities_WebAPI-Reference/__document_toc.html) | Explains how to use the Active Activities Web API, which lets you obtain information about activities that a player is playing. |
| [NpTrophy2 Library Overview](../NpTrophy2-Overview/__document_toc.html) and [NpTrophy2 Library Reference](../NpTrophy2-Reference/__document_toc.html) | Explains how to use the NpTrophy2 library, which lets your game obtain trophy data and trophy unlock states. This library does not provide any features for unlocking trophies, which is instead handled via UDS using UDS Stats. |
| [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) | For debugging purposes, this document describes the various logs you can use as part of your debugging process. Read [Universal Data System Guide - Using the UDS Management Tool - Viewing UDS Data](../Universal_Data_System-Guide/viewing-uds-data.html) for information on how to view logs for UDS events, UDS stats, and UDS state. |
| [Workspaces Overview](../Workspaces-Overview/__document_toc.html) | Explains the usage of workspaces, which let you quickly test and debug your application during development without having to create an entire package file. Workspaces are not just for testing UDS-related experiences. |
| "Package/Disc Management Tools (GEMS) Overview" | For debugging during development, you are only using GEMS to create the `npconfig.zip` file that includes your UDS and trophy configuration information. Use the "(latest config) - for development only" when downloading the `npconfig.zip` for this purpose. This is covered in the [Package/Disc Management Tool (GEMS) Overview - Downloading Configuration Files](../Package_Disc_Management_Tool_GEMS-Overview/downloading-configuration-files.html) section. |
| [Universal Data System Guide - FAQ](../Universal_Data_System-Guide/faq.html) | Lists various frequently asked questions, many of which pertain to the development of UDS-related experiences. |

# Add Localization (Activities, Subcategories, and Trophies)

This topic provides information on adding localization to your application. You can localize activity, subcategory, and trophy information as part of your data
configuration in the UDS Management Tool.

Activity localization is not included in the package file and thus can be adjusted
for all of your provided supported languages after package creation and before launch.
However, adding a new supported language does require a patch. Trophy localization,
however, is included as part of the trophy configuration in the package file, which
is required for internal QA testing and submission. Therefore, adjustments to trophy
localization require creating and submitting a new package file.

Updating activity localization is covered in [Adjust Localization (Activities)](adjust-localization-activities.html "This topic provides information on adjusting localization for activities. If you have already provided the localization of your activities as part of your development and internal QA process, then you can adjust them pre-launch or post-launch."). You can only add localization information for languages that you've included as
supported languages in the UDS Management Tool. Therefore, all supported languages
must be added for each NP Communication ID before you perform the submission process.

While you can perform this localization step concurrently with activity and trophy
creation, it is typical that the final localization will become available after you
have finalized your activities and trophies. Therefore, localization is listed here
as a separate step.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) | Contains information on localizing PSN objects, trophies, and subcategories. Relevant sections include:   * [Universal Data System Guide - Using the UDS Management Tool - Configuring Metadata](../Universal_Data_System-Guide/configuring-metadata.html) * [Universal Data System Guide - Using the UDS Management Tool - Configuring the UDS Data Model](../Universal_Data_System-Guide/configuring-the-uds-data-model.html) * [Universal Data System Guide - Using the UDS Management Tool - Trophy Tool](../Universal_Data_System-Guide/trophy-tool.html) |