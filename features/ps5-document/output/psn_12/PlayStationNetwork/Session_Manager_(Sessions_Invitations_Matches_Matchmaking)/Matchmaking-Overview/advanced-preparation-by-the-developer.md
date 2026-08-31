# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/advanced-preparation-by-the-developer.html

# Development Process and Processing Flow

# Advanced Preparation by Developers

Developers must create rulesets that represent the matchmaking conditions in advance and apply them to the matchmaking server. Up to 100 rulesets can be created per application; create as many as you need based on the specifications of your game. For details, refer to "[Configuring Rulesets](configuring-rulesets.html)".

How you create rulesets depends on the network architecture used.

## When Using the Sandbox Network Architecture

Use the Matchmaking Tool or NP Service Config to create rulesets. Rulesets are activated automatically.

## When Using the Legacy Network Architecture

Follow the steps below to create and activate rulesets.

1. **Create a ruleset**

   Use the Matchmaking Tool to create a ruleset.
2. **Activate the ruleset**

   Activate the created ruleset using the Matchmaking Tool. When activation completes, the ruleset will be applied to the matchmaking server and will be available for use by the application.

# Processing Conducted by the Application and Responses from the Matchmaking Server

1. **[Application] Create a matchmaking ticket**

   The application creates a matchmaking ticket and issues a submitTicket request to ask the server to conduct matchmaking. The matchmaking ticket sets up the target ruleset, the values of the player attributes defined by the ruleset, and the values of the ticket attributes. If there are specific players with whom the local player would like to play, the information for those players is also set up in the ticket. Additionally, to fill empty slots in an existing Game Session with supplemental players (backfilling), specify the target Game Session ID and the information of the players already participating in the Game Session in the ticket.

   When it receives a ticket, the server issues a matchmaking ticket ID. By specifying this ID, the application can cancel the ticket or check the progress of the matchmaking process.

   To cancel a matchmaking request, the application issues a cancelTicket request.
2. **[Server] Detect matchmaking candidates**

   The server places the matchmaking tickets it receives in a pool and searches for a combination of the tickets within the pool that would fulfill the conditions set forth in the ruleset. Each matchmaking ticket is deleted from the pool as matchmaking is achieved, it is canceled by the application, or the time limit established in the ruleset elapses without matchmaking being achieved.
3. **[Server] Achieving matchmaking**

   If matchmaking is achieved, the server creates a Game Session and puts the players who were matched together during matchmaking in ready-to-join status. The server also sends a Push notification (datatype: psn:sessionManager:gs:invitations:created) to the players who were matched together during matchmaking.

   When matchmaking for backfilling purposes is achieved, the server will not create a new Game Session, instead it will make a reservation for the supplemental players who were matched to join the backfilling-target Game Session. Furthermore, in the following conditions, a Push notification will be sent to all players who were matched together during matchmaking.

   * To players who have already joined: Sends a Push notification with datatype: psn:sessionManager:gs:matchmaking:updated.
   * To supplemental players: Sends a datatype: psn:sessionManager:gs:invitations:created Push notification (sends a psn:sessionManager:gs:matchmaking:updated Push notification).
4. **[Application] Confirm the matchmaking completion results**

   When the application receives the Push notification mentioned above, it issues a getGameSessions request with the Game Session ID included in the notification specified and obtains an offer ID. The matchmaking completion results can be confirmed if the application issues a getOffer request with the offer ID specified. The completion results include the team-splitting results, lists of players included in the teams, and the Game Session ID.
5. **[Application] Join the Game Session**

   The application issues a joinGameSessionAsPlayer request, making the player join the Game Session.

# Applying Rulesets to the Production Environment (RETAIL)

How you apply rulesets to the production environment (RETAIL) depends on the network architecture used.

## When Using the Sandbox Network Architecture

Once you have finished adjusting and testing a ruleset in the development environment (DEV), publish it using the Matchmaking Tool or NP Service Config. When the Publish operation completes, all rulesets in the development environment (DEV) will be applied to the matchmaking server in the production environment (RETAIL) and will be available for use by the application.

## When Using the Legacy Network Architecture

Once you have finished adjusting and testing a ruleset in the development environment (sp-int), publish it using the Matchmaking Tool. When the Publish operation completes, the ruleset will be applied to the matchmaking server in the production environment (RETAIL) and will be available for use by the application.