# PlayStation™Network Multiplayer Best Practices – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Multiplayer_Best_Practices/before-you-reading.html

# Before Reading "PlayStation™Network Multiplayer Best Practices"

The [PlayStation™Network Multiplayer Best Practices](__document_toc.html) document covers the best practices for planning, configuring, and handling multiplayer experiences for a game. This topic describes the purpose of the document, who this document is intended for, and the kind of background knowledge the target audience is expected to have.

## Intended Audience

This document is targeted towards all members of a game team involved in the creation of multiplayer-focused experiences including designers, directors, engineers, and producers. Covered here are details including how to leverage our Session Manager service in order to enable players to find each other and group up inside the game, how to deal with unique game designs, and how to technically handle key edge cases.

## Background Knowledge

This document is written with the assumption that you have already read the [PlayStation™Network Multiplayer Platform Concept Overview](../PSN_Multiplayer_Platform_Concept-Overview/__document_toc.html) document.

Also refer to "[Overview of the Multiplayer Experiences on PlayStation®5](overview.html "The newly added Session Manager service and the experiences it provides help to deliver the best multiplayer experiences in games on PlayStation®5, as well as resolve issues encountered on previous generation platforms. This topic provides an overview of the Session Manager service's multiplayer experiences and covers key system features that are used to realize them.")" first.

# Overview of the Multiplayer Experiences on PlayStation®5

The newly added Session Manager service and the experiences it provides help to deliver the best multiplayer experiences in games on PlayStation®5, as well as resolve issues encountered on previous generation platforms. This topic provides an overview of the Session Manager service's multiplayer experiences and covers key system features that are used to realize them.

The goal of the multiplayer experiences on PlayStation®5 is to make the experiences consistent and efficient while also enhancing player control. We received a significant amount of feedback from the players of the previous generation that they struggled to get together safely and easily in games. Not enough tools were available at the platform level, and games were inconsistent in their systems and UI. The Session Manager service and the experiences it provides have been designed from the ground up to create a more universally approachable system for games to present multiplayer groups to players and for the players to create in-game groups more quickly and easily. The following key system features are provided to enable players to create groups and enjoy comfortable gameplay.

* **Sessions That Can Be Joined throughout the Platform UI**

  Players are able to see their friend's joinable sessions throughout the UX. This drives players to join each other in gameplay and play online games more regularly. Sessions can be joined from both the Control Center and from the games' hubs.

  Sessions That Are Displayed in the Control Center

* **Game Invitations That Are Sent from the Platform UI**

  Players now have the ability to initiate invites to other players and groups for their Player Session from the PlayStation®5 UI. They do this directly from the session card in the Control Center or from the player's or Game Base's group messages screen.

  Invitations That Are Sent from the Session Card

* **Game Invitations That Are Sent to Groups**

  Persistent, Game Base groups that a player creates enable text chat, voice chat, and direct media sharing. A player can send game invitations to their groups via the system UI (shown with the envelope icon button [Group Invitations](overview.html#overview__uuid-ee1b71ac-d432-458c-639e-e00fb02d7419_figure-idm232223362919776)). If you leverage the common dialog for invitations the player can also send invitations from within the game. In such cases, any player in the group can join the session from the same invitation, leading to a much simpler and quicker way to get large groups together.

  Group Invitations

* **Player-Controlled Session Settings**

  Players in sessions are able to take key actions at the platform level to change settings including who can join the session without an invitation and who can send invitations. Players are also able to kick players out from their session or promote a different player as the session leader. These controls are important as they allow the players a level of control over their group so they can stay safe and comfortable online.

  Session Settings

* **Improved Voice Chat Experience**

  Voice chat is now much more prominent in the user experience. Players can manage the chat channels available to them, including parties, in real time from the Control Center. If the platform's VoiceChat library is used, in-game voice chat channels and their controls are displayed in the Control Center along with party voice chat. The in-game voice chat experience enabled by this library runs entirely within system resources, using a high-quality codec, audio management, and network topology management, which are all handled by the system. Additional platform-level features are also supported, including text-to-speech and speech-to-text to meet accessibility needs.

  Chat Channel Switching

* **Improved First-Time Gameplay Experiences in Multiplayer Titles**

  Players who purchase a multiplayer game (or download a free-to-play title) tend to play significantly less on the second day compared to the first. A little under half the number of players who play a multiplayer game for the first time do not come back to play the game on the second day. The first-time gameplay experience is paramount in delivering a great multiplayer experience.

  To provide a better first-time gameplay experience for your games, the platform provides more information that is aggregated across many titles through a new feature called the Advanced Player Profile. This data enables you to know more about the player when they enter your game for the first time and gives you the opportunity to customize and tailor the experience to them.

* **Reporting and Moderation**

  It is not a stretch to say that there is a toxicity problem regarding online multiplayer games. This is seen in both competitive and cooperative games. Toxicity occurs not just in gameplay but also in communication. On PlayStation®5, users can report voice chat content to our safety and moderation teams. This allows for improved moderation and assists in preventing toxic behavior. Reporting and moderation are supported in the platform's party voice chat as well as in in-game voice chat that is enabled by the platform's VoiceChat library.

* **Improved Matchmaking**

  We want to help to make sure players get matched with the right players to play with. Our brand-new matchmaking service is built from the ground up within Session Manager to help you to get the right players together to play. It is built around a queue-based concept that allows you to have less setup/configuration time and more value for your game. To leverage system-based matching, you no longer have to deal with regions and lobbies but can now focus on making sure the right players get together as fast as possible. We plan on continuing to invest in the matchmaking service throughout the generation.