# Cross-generation Application Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Cross_Generation_Application-Tutorial/overview-of-multiplayer-mode.html

# Multiplayer Mode

This topic describes the techniques for implementing real-time multiplayer gameplay (such as competitive activities and premium features, the invitation feature, and network communication) using the "multiplayer mode" of the tutorial sample supporting cross-generation gameplay between PlayStation®5 and PlayStation®4.

# Overview of Multiplayer Mode

The multiplayer mode allows real-time multiplayer gameplay with players who are playing the game on other consoles.

Select "Multiplayer" in the Title Menu view and press the "Start Game" button. A transition will be made to the Lobby menu after a Premium check is performed. In the lobby, you can invite friends or start a random match.

A random match is an individual match. Up to four players compete against each other over who can shoot the highest number of targets.

The multiplayer mode supports the following PlayStation™Network-related features:

* [Competitive Activities](competitive-activities.html)
* [Premium Features](premium-features.html)
* [Player Sessions and Game Sessions](player-sessions-and-game-sessions.html)
* [Trophies Set in This Tutorial](trophies.html "This topic describes how to configure and manage the trophies set in the tutorial sample supporting cross-generation gameplay between PlayStation®5 and PlayStation®4.")

# Competitive Activities

Competitive activities are set for multiplayer gameplay, and multiplayer gameplay information is recorded and reflected to the PlayStation™Network server using the Matches Web API. Multiplayer gameplay information is updated in accordance with [R5302](../../../TRC/latest/TRC/R5302.html) and in line with progress in the match.

## Activity Setup

One competitive activity (online\_match) is set up in this tutorial. The main attributes of this activity are shown in the table below. Tasks and subtasks are not set for the activity.

Main Attributes of the Multiplayer Mode Competitive Activity

| **Attributes** | **Activity** |
| --- | --- |
| Object Id | online\_match |
| Category | competitive |
| Available by Default | true |
| Required for Completion | false |
| Name | online match |
| Description | Shoot ducks! |
| Has Online Multiplayer | true |
| Is Team Activity | false |
| Number Of Players | none |
| Total Number Of Players | 4 |
| Supported Platforms | PS5, PS4 |

## Starting and Ending the Activity

To update the competitive activity, `createMatch` is called when multiplayer gameplay starts. Register all users playing the match to the `createMatch` in-game roster. Because the game starts straight away after the match is created, call `updateMatchStatus` and change the match status to `PLAYING`. The Matches Web API is called by the leader of the game session (`representative`).

When multiplayer gameplay ends, call `reportResults` to report the results. The content of the report must match the results displayed in the game.

Call `updateMatchStatus` and cancel the match when multiplayer gameplay ends because of a network error (for example).

In this tutorial, the number of participants in the game session cannot be changed after the match starts. If even one player leaves the game session, multiplayer gameplay ends. If your application supports changing the number of players during a match, call `updateMatchDetail` and change the in-game roster to the appropriate number.

```
// After joining the Game Session, the representative creates a match
const char* activityID = "online_match";
createMatch(activityID);

// After the match is created, change the match status to PLAYING
updateMatchStatus(kMatchStatusRequestPlaying);

// After the game ends, report the match results. Processing to enter the match results in competitiveResult is omitted here.
MatchCompetitiveResult competitiveResult;

reportMatchResult(competitiveResult);
```

# Premium Features

Because the real-time multiplayer feature in this tutorial is a Premium feature, a Premium check must be performed in accordance with [R5063](../../../TRC/latest/TRC/R5063.html) to verify that the user has the right to access the Premium feature before the feature is actually accessed. The Premium check flow is described in [Premium Features Guidelines - Application Design - Example 1: Premium Check upon Menu Selection](../Premium_Features_Guidelines/example-1-premium-check-upon-menu-selection.html).

This tutorial does not support in-engine spectating and cross-platform play (with non-PlayStation® platforms). When calling `sceNpNotifyPremiumFeature()`, specify `SCE_NP_REALTIME_MULTIPLAY_PROPERTY_NONE` in `properties`. `sceNpNotifyPremiumFeature()` is repeatedly called during the Game Scene at 1-second intervals. As there is not yet any interaction between players in the Count Down view before the game starts, `sceNpNotifyPremiumFeature()` calls start after the countdown.

# Player Sessions and Game Sessions

This tutorial uses the invitation feature of player sessions to support the use of invitations.

Only the Online IDs and platform information of the player session information are displayed in the game. All the values below are specified in `exclusiveLeaderPrivileges` for the call of `createPlayerSessions`.

* `UPDATE_JOINABLE_USER_TYPE`
* `UPDATE_INVITABLE_USER_TYPE`
* `PROMOTE_TO_LEADER`

Therefore, "Who can join" and "Who can invite" cannot be changed from the player session card in the system software, and the "Promote to Leader" menu cannot be selected.

Game sessions are used to implement automatic matchmaking.

A player session is created when transitioning to the Lobby menu (Multiplayer Menu view), and the same player session continues until the Title Menu view is returned to. Game sessions are destroyed each time a multiplayer session ends.

# Invitations

To receive an invitation game intent event (`joinSession`), the type of game intent events supported by the application must be specified in the parameter file (param.json). For details, refer to [Game Intent System Overview - Application Support for Game Intent Events](../Game_Intent_System-Overview/application-support-for-game-intent-events.html).

`joinSession` stores the Session ID of the player session for which the invite is for. In this tutorial, if the player receives a `joinSession`, they automatically transition to the multiplayer lobby to join a friend's player session.

If the player receives an invite but cannot start multiplayer gameplay for reasons such as that they are playing a different game, display a message to notify the player of the reason why they cannot transitions to the session.

An example is shown below of when a `joinSession` game intent event is received, but the transition to the session is aborted with a message display because matchmaking is in progress.

```
bool Scene::handleJoinSessionGameIntent(const SceNpGameIntentInfo* gameIntentInfo)
{
    auto &app = DuckShootingGame::m_singleton;
    // For each view, determine whether invitations can be received
    if (!m_pCurrentView->canAcceptInvitation())
    {
        app.setInformationMessage("Can not transition at this mode.");
        return true;
    }
    auto& playerSessionInfo = app.m_userContext.getPlayerSessionInfo();

    // If the user has already joined a player session, abort the transition to the invitation only if the user is is being matched or has joined a game session
    if (playerSessionInfo.isJoined()) {
        if (customData.m_multiplayerLobbyStatus == MultiplayerLobbyStatus::kReady ||
            app.m_userContext.getIsMatchingInProgress() ||
            app.m_userContext.getGameSessionInfo().isJoined()) {
            app.setInformationMessage("Invitations cannot be accepted while matchmaking is in progress.");
            return true;
        }
    }
}
```

# Network Communications

The multiplayer mode of the tutorial uses the NpSessionSignaling library and is a game format that uses a star topology based on UDPP2P to allow one host to play against up to three clients. This section describes the techniques used in this multiplayer mode to implement a real-time multiplayer gaming experience.

## Game State Synchronization

In this tutorial, the game is synchronized by sending data between the host and clients at every frame. Each client sends operation information to the host, while the host sends rendering information to all clients.

* **Queuing**

  In this tutorial, communication data is queued to counteract packet delays and packet loss caused by network environments.

  The host stores client operation information in separate queues for each client and also queues host operation information. Based on this information, the host calculates the rendering information (shooter, ducks, effects, etc.) required for the screen display and sends it to the clients.

  The clients sort the rendering information received from the host based on the time information and queue it. Rendering information is then extracted from the start of the queue, and calculations are performed for screen display.

  The above flow is shown in the following diagram.
* **Notes on Queuing Support**

  In this tutorial, synchronization control is based on network time, not the number of frames.

  For example, a control method that notifies the incremented number of frames each time data is sent does not guarantee that the duration of one frame is the same for the host and the clients. In addition, misalignment occurs when queued data increases or decreases due to packet loss. To prevent this, this tutorial uses network time (networkTime) instead of the number of frames.

  On the other hand, unlike the number of frames, with network time the values do not exactly match between the sender and receiver, so a certain amount of leeway is required for comparing times when packets are retrieved from the queue.

  The times used for synchronization and how they are used are described below.
  + `networkTime`: The reference time that always continues to advance after the game starts. Also used for the timestamp of sent packets.
  + `evaluateTime`: The time to determine whether the received data is used as current information
  + `deltaTime`: The time incremented per frame

  ```
  /* @brief Function to update time
   * @param isEmpty Whether the queue is empty
   * @param isAboveHighWatermark Whether the queue has exceeded the threshold
  */ 
  void NetworkDataQueue::updateTime(float deltaTime, bool isEmpty, bool isAboveHighWatermark)
  {
      m_deltaTime = deltaTime;
      m_networkTime += deltaTime;

      if (isEmpty)
      {
          deltaTime = 0; // Do not advance time if queue is empty
      } else if (isAboveHighWatermark)
      {
          deltaTime += deltaTime * 0.5; // Advance time because queue exceeds threshold
      }
      m_evaluateTime = std::min(m_evaluateTime + deltaTime, m_networkTime); // Do not exceed networkTime
  }

  /* @brief Compare data received with m_evaluateTime and store in queue if it is within range
   * @param data Received data
  */ 
  void NetworkDataQueue::push(DataType &&data)
  {
      if (m_evaluateTime - m_deltaTime <= data.getTime())
      {
          // Sort by time and insert into queue. Sort processing is omitted
          m_queueDataArray.insert(data);
      }
  }

  /* @brief Retrieve data within range from queue
   * @retval Data used for physics operation and rendering
  */ 
  const NetworkDataQueue::DataType &pop()
  {
      // Remove data older than m_evaluateTime. Delete processing is omitted

      // If queue data is within range, use queue data
      if (m_queueDataArray.size() > 0 &&
          m_queueDataArray.front().getTime() < m_evaluateTime + m_deltaTime)
      {
          // m_lastUsedData is the last used data. If no data is within range, reuse last used data
          m_lastUsedData = std::move(m_queueDataArray.front());
          m_queueDataArray.pop_front();
      }
      return m_lastUsedData;
  }
  ```
* **Countermeasures against Synchronization Misalignment until Play Start**

  In a four-person game, the host waits for the three clients to establish communication before the game starts. Because of the star topology, each client is not aware of whether the other clients have started communicating with the host.

  In this tutorial, once communication has been established with all clients, a start packet is sent to each client to synchronize the start timing.
* **Physics Operations**

  In this tutorial, the movements of the ducks (shooting targets) are rendered using physics operations. These physics operations are performed by the host only.

  When physics operations are also performed by the clients, rollback processing in the event of packet loss must be considered. However, in this tutorial, there is no rollback as only the host performs physics operations.