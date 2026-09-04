# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/design-your-tournaments.html

# Design Features and Define Data Model

This topic provides an overview of the procedure for defining the data model for your
application. This includes creating and configuring activities, trophies, UDS events, and
other PlayStation™Network objects.

The goal of this phase is to understand the data-driven experiences and define the
data model that enables them. These tasks are often performed concurrently, because
the design of an experience must consider the definition of the data that is required
to configure it. While the tasks for this workflow phase imply that you should first
understand and design each experience before defining the underlying data model, in
practice, these are often concurrent tasks.

Your involvement with this phase can vary depending on your immediate goals. For example,
you might be in the early design phase of your game and seeking more information about
data-driven experiences and how they can drive user engagement with your products.
On the other hand, you might be ready to package and submit your game and are looking
to quickly implement the features required by the Technical Requirements Checklist
(TRC). For this reason, how much time you spend learning about and designing each
experience will depend on your specific circumstances.

Even though this workflow phase has discrete tasks for learning about and designing
each experience, you can decide to tackle the design and development of each experience
individually. Consider this workflow phase a requirement for each individual feature.
In practice, you can apply your own process for understanding and designing each feature.

# Design Your Activities

This topic links to the services you'll use when creating and designing
activities.

This step entails designing the activities that you want to make available to players.
The different types of activities are: progress-based, open-ended, competitive, or
challenges. For challenge activities, see [Design Your Challenge Activities](design-your-challenge-activities.html "This topic links to the services you'll use when creating and designing challenge activities for your game. Challenge activities are a specific type of activity that displays rankings in a leaderboard format.").

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html) | Describes what activities are, explains the technical concepts related to their configuration, and provides examples of the user experience. Provides asset specifications and best practices for creating high-quality visuals for your activities.  This document also provides design considerations and configuration guidance for when you start developing your activities. This is a helpful document to reference when you start implementing your activities. |

# Design Your Tournaments

This topic links to the services you'll use when creating and configuring tournaments for your game.

This step entails designing the tournaments you want to make available to players.
Tournaments combine a competitive activity with a set of rules to create a unique
experience.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation®5 Tournaments Guide](../PS5_Tournaments-Guide/__document_toc.html) | Provides relevant information about the tournament system with a focus on integration, design, and testing requirements. This document focuses on how the tournament object combines with competitive activity design to determine the final experience for players in a tournament. |

# Design Your Trophies

This topic links to the services you'll use when creating and designing trophies for
your game.

This step entails designing the types of trophies you will have in your game. You
can create either non-progressive or progressive trophies. For an overview of the
trophy system, refer to the Data-Driven Experiences section. Trophies have various
attributes and configuration data that you configure using the UDS Management Tool,
via bulk import, or via the UDS Configuration Web API. These attributes are described
in the document listed below.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Trophy System Overview](../Trophy_System-Overview/__document_toc.html) | Targets readers in the planning and design stages of development. The first half of the document describes the overall behavior of the trophy system and contains an explanation on the rules for configuring trophies based on game content. The second half of the document provides an overview of the development process and specifications of trophy configuration data, including names and icons. |

# Design Your Game Help

This topic links to the services you'll use when configuring game help for your game.

The UDS Management Tool is used to configure the activities and trophies that your
official hints correspond to. Consider and design these before or alongside your hints.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Game Help Guide](../PSN_Game_Help-Guide/__document_toc.html) | Provides a high-level workflow for implementing Game Help and describes the PSN objects and UDS events related to Game Help. This document also describes the best practices for planning, configuring, and managing Game Help. Provides suggestions for designing activities, structure, and content to optimize the experience. This document is useful to reference during both the design and development phases. |

# Design Your Challenge Activities

This topic links to the services you'll use when creating and designing challenge activities for your game. Challenge activities are a specific type of activity that displays rankings in a leaderboard
format.

Challenge activities are created using the UDS Management Tool by following the standard
way of creating a new activity object and choosing challenge as your category.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [PlayStation™Network Activities Guide](../PSN_Activities-Guide/__document_toc.html) | Contains a section that describes how to implement challenge activities. This is a helpful document to reference alongside the [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) when developing challenge activities. |

# Define Your UDS Data Model

As you learn about and begin designing each of the data-driven experiences you want to offer, you can start defining the UDS data model entities that enable them. These entities correspond to your game's various content and each have their own purpose, properties, and use cases depending on the experiences you want to provide.

The more robust and prolific these entities are, the easier it is to configure enriching
experiences for the player. If you are in the early stages of development, read and
understand how the UDS data model is set up so that your development team can plan and
implement the appropriate entities into your game's code.

Perhaps your team has developed most of your game already, and you are looking to
implement experiences to satisfy the requirements in the TRC. In this case, you still
must read and understand how the UDS data model works so that at a minimum you can
define the data that is needed to implement the required functionality. The documentation
linked below discusses various implementation methods, some of which can be implemented
more quickly depending on your needs.

Related Content

| **Document / Help Content** | **Description** |
| --- | --- |
| [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html) | Describes the entities and components that comprise the UDS and the requirements for each. Provides a high-level overview of the UDS development process and appendices for PSN object and UDS event type definitions. |