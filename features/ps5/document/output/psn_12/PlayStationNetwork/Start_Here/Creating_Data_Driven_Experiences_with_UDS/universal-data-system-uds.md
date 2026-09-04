# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/universal-data-system-uds.html

# Universal Data System (UDS)

This topic provides an overview of the Universal Data System and how it differs from
previous APIs provided by SIE.

Developers can provide these data-driven experiences for PlayStation®5 games via the
Universal Data System (UDS). UDS is a PlayStation™Network service that provides games
with the ability to transmit player data from the game to PlayStation™Network servers,
which enables data-driven experiences in real time.

In the past, implementing support for PlayStation™Network feature experiences required
development teams to use bespoke APIs for each PlayStation™Network feature experience.
Using different APIs to send often-overlapping information required game teams to
duplicate significant amounts of work.

Using Bespoke APIs to Integrate Features Separately (PlayStation®4)

UDS simplifies this work by providing a single set of APIs that streamlines the configuration
of multiple data-driven experiences.

UDS Provides a Single Integration for Multiple Experiences (PlayStation®5)

# UDS Data Model

This topic provides an overview of the UDS data model.

The types of data that you define in the UDS Management Tool comprise the UDS data
model that underpins the data-driven experiences. Learning about this UDS data model
is covered in the [UDS Workflow](uds-workflow.html "This section provides a workflow that you can follow for designing, configuring, and delivering data-driven experiences.") section. Below is a basic summary of the PSN objects and UDS entities so you are
aware of the basic types of data you will be asked to define. You can find more information
on all these types of data in the relevant documents that are listed in the next section
for each workflow task.

* **PlayStation™Network Objects** - PlayStation™Network objects represent static information used in a game such as the story's missions and locations. You define these objects in the UDS Management Tool or Universal Data System Configuration Web API.

  + **Activity** - An activity is a unit of gameplay that is inherent to the structure of a game, such as a level, chapter, quest, or multiplayer mode. You can define tasks and sub-tasks to break activities down into smaller objectives.
* **UDS Events** - Events are used to track game progress and a player's actions in the game. Examples include game state management and trophy unlocking. You define these in the UDS Management Tool or UniversalDataSystem Configuration Web API.
* **UDS Stats** - Stats are information that is extracted and aggregated from UDS events that your game sends. Such information is stored as statistics, which various platform features can then use. You define these in the UDS Management Tool or UniversalDataSystem Configuration Web API.
* **UDS State** - States apply to the various PSN objects and track the player's in-game actions. For example, the activities the player has ever played or the zone the player is currently in. You do not manually define states because they are automatically tracked based on a player's actions.