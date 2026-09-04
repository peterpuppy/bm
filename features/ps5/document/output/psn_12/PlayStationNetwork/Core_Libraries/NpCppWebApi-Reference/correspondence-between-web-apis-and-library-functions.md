# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/correspondence-between-web-apis-and-library-functions.html

# Correspondences with Web APIs

# Correspondence Between Namespaces and Web APIs

List of namespaces and their corresponding Web API

## Definition

| **Namespace** | **Web API** |
| --- | --- |
| `sce::Np::CppWebApi::Activities` | Active Activities Web API |
| `sce::Np::CppWebApi::AdvancedPlayerProfile` | Advanced Player Profile Web API |
| `sce::Np::CppWebApi::CommunicationRestrictionStatus` | Communication Restriction Status Web API |
| `sce::Np::CppWebApi::Entitlement` | Entitlements Web API |
| `sce::Np::CppWebApi::InGameCatalog` | In-Game Catalog Web API |
| `sce::Np::CppWebApi::Leaderboards` | Leaderboards Web API |
| `sce::Np::CppWebApi::Matches` | Matches Web API |
| `sce::Np::CppWebApi::Matchmaking` | Matchmaking Web API |
| `sce::Np::CppWebApi::ProfanityFilter` | Profanity Filter Web API |
| `sce::Np::CppWebApi::SessionManager` | Session Manager Web API |
| `sce::Np::CppWebApi::TitleCloudStorage` | Title Cloud Storage Web API |
| `sce::Np::CppWebApi::UserProfile` | User Profile Web API |

# Correspondence Between Web APIs and Library Functions

Web API endpoints and their corresponding NpCppWebApi library functions

## Description

Each Web API endpoint corresponds to a single NpCppWebApi library function. The following tables show these relationships.

**Active Activities Web API⇔sce::Np::CppWebApi::Activities**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `getUserActivities` | GET | `/v1/users/activities` | `ActivityApi` | `V1::UserActivities::ActivityApi::getUserActivities()` |

**Advanced Player Profile Web API⇔sce::Np::CppWebApi::AdvancedPlayerProfile**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `getStats` | GET | `/v1/users/me/stats` | `StatsApi` | `V1::StatsApi::getStats()` |

**Entitlements Web API⇔sce::Np::CppWebApi::Entitlement**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `listEntitlements` | GET | `/v2/users/me/entitlements` | `Entitlements Api` | `V2::EntitlementsApi::listEntitlements()` |
| `getEntitlement` | GET | `/v2/users/me/entitlements/{entitlementLabel}` | `EntitlementsApi` | `V2::EntitlementsApi::getEntitlement()` |

**Communication Restriction Status Web API⇔sce::Np::CppWebApi::CommunicationRestrictionStatus**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `getCommunicationRestrictionStatus` | GET | `/v3/users/{account_id_or_me}/communication/restriction/status` | `CommunicationRestrictionStatusApi` | `V3::CommunicationRestrictionStatusApi::getCommunicationRestrictionStatus()` |

**In Game Catalog Web API<=>sce::Np::CppWebApi::InGameCatalog**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `getContainer` | GET | `/v5/container` | `ContainerApi` | `V5::ContainerApi::getContainer()` |

**Leaderboards Web API<=>sce::Np::CppWebApi::Leaderboards**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `getBoardDefinition` | GET | `/v1/apps/myApp/boards/{boardId}/definition` | `BoardsApi` | `V1::BoardsApi::getBoardDefinition()` |
| `recordLargeData` | POST | `/v1/apps/myApp/boards/{boardId}/users/me/largeData` | `RecordApi` | `V1::RecordApi::recordLargeData()` |
| `recordScore` | POST | `/v1/apps/myApp/boards/{boardId}/users/me/score` | `V1::RecordApi::recordScore()` |
| `getLargeDataByObjectId` | GET | `/v1/apps/myApp/objects/{objectId}/largeData` | `ViewApi` | `V1::ViewApi::getLargeDataByObjectId()` |
| `getRanking` | POST | `/v1/apps/myApp/boards/{boardId}/entries/view` | `V1::ViewApi::getRanking()` |

**Matches Web API<=>sce::Np::CppWebApi::Matches**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `createMatch` | POST | `/v1/matches` | `MatchApi` | `V1::MatchApi::createMatch()` |
| `getMatchDetail` | GET | `/v1/matches/{matchId}` | `V1::MatchApi::getMatchDetail()` |
| `joinMatch` | POST | `/v1/matches/{matchId}/players/actions/add` | `V1::MatchApi::joinMatch()` |
| `leaveMatch` | POST | `/v1/matches/{matchId}/players/actions/remove` | `V1::MatchApi::leaveMatch()` |
| `reportResults` | POST | `/v1/matches/{matchId}/results` | `V1::MatchApi::reportResults()` |
| `updateMatchDetail` | PATCH | `/v1/matches/{matchId}` | `V1::MatchApi::updateMatchDetail()` |
| `updateMatchStatus` | PUT | `/v1/matches/{matchId}/status` | `V1::MatchApi::updateMatchStatus()` |

**Matchmaking Web API<=>sce::Np::CppWebApi::Matchmaking**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `cancelTicket` | DELETE | `/v1/tickets/{ticketId}` | `Api` | `V1::Api::cancelTicket()` |
| `getOffer` | GET | `/v1/offers/{offerId}` | `V1::Api::getOffer()` |
| `getTicket` | GET | `/v1/tickets/{ticketId}` | `V1::Api::getTicket()` |
| `listUserTickets` | GET | `/v1/users/{accountId}/tickets` | `V1::Api::listUserTickets()` |
| `submitTicket` | POST | `/v1/tickets` | `V1::Api::submitTicket()` |

**Profanity Filter Web API⇔sce::Np::CppWebApi::ProfanityFilter**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `filterProfanity` | POST | `/v2/profanity/filter/{locale}/{serviceLabel}` | `ProfanityApi` | `V2::ProfanityApi::filterProfanity()` |
| `testForProfanity` | POST | `/v2/profanity/test/{locale}/{serviceLabel}` | `V2::ProfanityApi::testForProfanity()` |

Session Manager Web API<=>sce::Np::CppWebApi::SessionManager

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `createGameSessions` | POST | `/v1/gameSessions` | `GameSessionsApi` | `V1::GameSessionsApi::createGameSessions()` |
| `deleteGameSession` | DELETE | `/v1/gameSessions/{sessionId}` | `V1::GameSessionsApi::deleteGameSession()` |
| `getGameSessions` | GET | `/v1/gameSessions` | `V1::GameSessionsApi::getGameSessions()` |
| `getJoinedGameSessionsByUser` | GET | `/v1/users/{accountId}/gameSessions` | `V1::GameSessionsApi::getJoinedGameSessionsByUser()` |
| `joinGameSessionAsPlayer` | POST | `/v1/gameSessions/{sessionId}/member/players` | `V1::GameSessionsApi::joinGameSessionAsPlayer()` |
| `joinGameSessionAsSpectator` | POST | `/v1/gameSessions/{sessionId}/member/spectators` | `V1::GameSessionsApi::joinGameSessionAsSpectator()` |
| `leaveGameSession` | DELETE | `/v1/gameSessions/{sessionId}/members/{accountId}` | `V1::GameSessionsApi::leaveGameSession()` |
| `patchGameSessionsSearchAttributes` | PATCH | `/v1/gameSessions/{sessionId}/searchAttributes` | `V1::GameSessionsApi::patchGameSessionsSearchAttributes()` |
| `postGameSessionsSearch` | POST | `/v1/gameSessions/search` | `V1::GameSessionsApi::postGameSessionsSearch()` |
| `postGameSessionsTouch` | POST | `/v1/gameSessions/{sessionId}/touch` | `V1::GameSessionsApi::postGameSessionsTouch()` |
| `putGameSessionsSearchAttributes` | PUT | `/v1/gameSessions/{sessionId}/searchAttributes` | `V1::GameSessionsApi::putGameSessionsSearchAttributes()` |
| `sendGameSessionMessage` | POST | `/v1/gameSessions/{sessionId}/sessionMessage` | `V1::GameSessionsApi::sendGameSessionMessage()` |
| `setGameSessionMemberSystemProperties` | PATCH | `/v1/gameSessions/{sessionId}/members/{accountId}` | `V1::GameSessionsApi::setGameSessionMemberSystemProperties()` |
| `setGameSessionProperties` | PATCH | `/v1/gameSessions/{sessionId}` | `V1::GameSessionsApi::setGameSessionProperties()` |
| `addPlayerSessionJoinableSpecifiedUsers` | POST | `/v1/playerSessions/{sessionId}/joinableSpecifiedUsers` | `PlayerSessionsApi` | `V1::PlayerSessionsApi::addPlayerSessionJoinableSpecifiedUsers()` |
| `changePlayerSessionLeader` | PUT | `/v1/playerSessions/{sessionId}/leader` | `V1::PlayerSessionsApi::changePlayerSessionLeader()` |
| `createPlayerSessions` | POST | `/v1/playerSessions` | `V1::PlayerSessionsApi::createPlayerSessions()` |
| `deletePlayerSessionJoinableSpecifiedUsers` | DELETE | `/v1/playerSessions/{sessionId}/joinableSpecifiedUsers` | `V1::PlayerSessionsApi::deletePlayerSessionJoinableSpecifiedUsers()` |
| `deletePlayerSessionsMemberNonPsnPlayer` | DELETE | `/v1/playerSessions/{sessionId}/member/nonPsnPlayers/{playerId}` | `V1::PlayerSessionsApi::deletePlayerSessionsMemberNonPsnPlayer()` |
| `getJoinedPlayerSessionsByUser` | GET | `/v1/users/{accountId}/playerSessions` | `V1::PlayerSessionsApi::getJoinedPlayerSessionsByUser()` |
| `getPlayerSessionInvitations` | GET | `/v1/users/{accountId}/playerSessionsInvitations` | `V1::PlayerSessionsApi::getPlayerSessionInvitations()` |
| `getPlayerSessions` | GET | `/v1/playerSessions` | `V1::PlayerSessionsApi::getPlayerSessions()` |
| `getPlayerSessionsShareableUrl` | GET | `/v1/playerSessions/{sessionId}/shareableUrl` | `V1::PlayerSessionsApi::getPlayerSessionsShareableUrl()` |
| `joinPlayerSessionAsPlayer` | POST | `/v1/playerSessions/{sessionId}/member/players` | `V1::PlayerSessionsApi::joinPlayerSessionAsPlayer()` |
| `joinPlayerSessionAsSpectator` | POST | `/v1/playerSessions/{sessionId}/member/spectators` | `V1::PlayerSessionsApi::joinPlayerSessionAsSpectator()` |
| `leavePlayerSession` | DELETE | `/v1/playerSessions/{sessionId}/members/{accountId}` | `V1::PlayerSessionsApi::leavePlayerSession()` |
| `putPlayerSessionsNonPsnLeader` | PUT | `/v1/playerSessions/{sessionId}/nonPsnLeader` | `V1::PlayerSessionsApi::putPlayerSessionsNonPsnLeader()` |
| `sendPlayerSessionInvitations` | POST | `/v1/playerSessions/{sessionId}/invitations` | `V1::PlayerSessionsApi::sendPlayerSessionInvitations()` |
| `sendPlayerSessionMessage` | POST | `/v1/playerSessions/{sessionId}/sessionMessage` | `V1::PlayerSessionsApi::sendPlayerSessionMessage()` |
| `setPlayerSessionMemberSystemProperties` | PATCH | `/v1/playerSessions/{sessionId}/members/{accountId}` | `V1::PlayerSessionsApi::setPlayerSessionMemberSystemProperties()` |
| `setPlayerSessionProperties` | PATCH | `/v1/playerSessions/{sessionId}` | `V1::PlayerSessionsApi::setPlayerSessionProperties()` |

**Title Cloud Storage Web API <=> sce::Np::CppWebApi::TitleCloudStorage**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `deleteMultiDataBySlot` | DELETE | `/v1/apps/myApp/users/data/slots/{slotId}` | `DataApi` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::deleteMultiDataBySlot()` |
| `deleteMultiDataByUser` | DELETE | `/v1/apps/myApp/users/{accountId}/data` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::deleteMultiDataByUser()` |
| `downloadData` | GET | `/v1/apps/myApp/users/{accountId}/data/slots/{slotId}` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::downloadData()` |
| `getMultiDataStatusesBySlot` | GET | `/v1/apps/myApp/users/data/slots/{slotId}/status` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::getMultiDataStatusesBySlot()` |
| `getMultiDataStatusesByUser` | GET | `/v1/apps/myApp/users/{accountId}/data/slots/status` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::getMultiDataStatusesByUser()` |
| `setDataInfo` | PUT | `/v1/apps/myApp/users/{accountId}/data/slots/{slotId}/info` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::setDataInfo()` |
| `uploadData` | PUT | `/v1/apps/myApp/users/{accountId}/data/slots/{slotId}` | `sce::Np::CppWebApi::TitleCloudStorage::V1::DataApi::uploadData()` |
| `addAndGetVariable` | POST | `/v1/apps/myApp/users/{accountId}/variables/slots/{slotId}/add` | `VariablesApi` | `sce::Np::CppWebApi::TitleCloudStorage::V1::VariablesApi::addAndGetVariable()` |
| `deleteMultiVariablesByUser` | DELETE | `/v1/apps/myApp/users/{accountId}/variables` | `sce::Np::CppWebApi::TitleCloudStorage::V1::VariablesApi::deleteMultiVariablesByUser()` |
| `getMultiVariablesBySlot` | GET | `/v1/apps/myApp/users/variables/slots/{slotId}` | `sce::Np::CppWebApi::TitleCloudStorage::V1::VariablesApi::getMultiVariablesBySlot()` |
| `getMultiVariablesByUser` | GET | `/v1/apps/myApp/users/{accountId}/variables` | `sce::Np::CppWebApi::TitleCloudStorage::V1::VariablesApi::getMultiVariablesByUser()` |
| `setMultiVariablesByUser` | PUT | `/v1/apps/myApp/users/{accountId}/variables` | `sce::Np::CppWebApi::TitleCloudStorage::V1::VariablesApi::setMultiVariablesByUser()` |
| `setVariableWithConditions` | POST | `/v1/apps/myApp/users/{accountId}/variables/slots/{slotId}` | `sce::Np::CppWebApi::TitleCloudStorage::V1::VariablesApi::setVariableWithConditions()` |

**User Profile Web API<=>sce::Np::CppWebApi::UserProfile**

| **Web API operationId** | **Web API HTTP method** | **Web API Path** | **NpCppWebApi Class** | **NpCppWebApi Function** |
| --- | --- | --- | --- | --- |
| `getPublicProfile` | GET | `/v1/users/{accountId}/profiles` | `BasicProfileApi` | `V1::BasicProfileApi::getPublicProfile()` |
| `getPublicProfiles` | GET | `/v1/users/profiles` | `V1::BasicProfileApi::getPublicProfiles()` |
| `getBlockingUsers` | GET | `/v1/users/me/blocks` | `BlocksApi` | `V1::BlocksApi::getBlockingUsers()` |
| `getFriends` | GET | `/v1/users/{accountId}/friends` | `FriendsApi` | `V1::FriendsApi::getFriends()` |
| `getBasicPresences` | GET | `/v1/users/basicPresences` | `PresenceApi` | `V1::PresenceApi::getBasicPresences()` |