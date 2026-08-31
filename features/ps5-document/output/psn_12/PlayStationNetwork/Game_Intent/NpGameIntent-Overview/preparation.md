# NpGameIntent Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpGameIntent-Overview/preparation.html

# Using the Library

This topic describes the preparations and basic procedure for using the NpGameIntent library, and also introduces a typical implementation example.

# Preparation

## Create a Parameter File (param.json)

Write the types of game intent events supported by the application in the parameter file. Create a parameter file by referring to the "[Parameter File (param.json)](parameter-file-paramjson.html)" section of the "[Reference Information](reference-information.html "This topic provides reference information for using the NpGameIntent library, including definitions of the parameter file (param.json) and an example of how to write it.")" chapter, and place it in the specified directory. (For details about the location to place the file, refer to the [Application Content Overview](../Application_Content-Overview/__document_toc.html) document.)

Refer to [Param.json File Specification - Using the Param File (param.json)](../Param_Json-Specification/using-the-param-file-paramjson.html) for instructions on how to create a parameter file (param.json).

# Basic Procedure

The basic procedure for using the NpGameIntent library is explained below:

1. **Initialize the library**

   Prepare a variable of the `SceNpGameIntentInitParam` type and initialize the library using `sceNpGameIntentInitParamInit()`. Specify this variable as an argument and call `sceNpGameIntentInitialize()`.
2. **Monitor game intent events**

   Use the SystemService library and monitor the occurrence of a game intent event. The game intent event will be notified as an instance of the `SCE_SYSTEM_SERVICE_EVENT_GAME_INTENT` event type.

   Refer to the [SystemService Library Overview](../SystemService-Overview/__document_toc.html) and [SystemService Library Reference](../SystemService-Reference/__document_toc.html) documents for usage of the SystemService library.
3. **Receive game intent information**

   When a game intent event is notified, call `sceNpGameIntentReceiveIntent()` with the variable of the `SceNpGameIntentInfo` type initialized using `sceNpGameIntentInfoInit()` specified as an argument. The game intent event type, game intent data, and the user ID of the user who made the game intent event occur will be stored in this variable when game intent information is successfully received.

   The receiving of game intent information can fail when, for example, a second game intent event occurs before information of the first event is received. The `SCE_NP_GAME_INTENT_ERROR_INTENT_NOT_FOUND` error will be returned in such cases. Ignore the game intent information that you failed to receive and continue monitoring game intent events.
4. **Obtain property values**

   Game intent properties are included in the game intent data received in step ([3](basic-procedure.html#np-game-intent-library-overview_1_2__np-game-intent-library-overview_1_2_3)) as part of the game intent information. Call `sceNpGameIntentGetPropertyValueString()` with the property name, game intent data, and buffer to store the property value specified as arguments. Specify a buffer capable of storing the maximum size for the specified property as the destination to store the property value. A string containing the NULL terminator will be stored in this buffer.

   Refer to the [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html) document for properties that can be obtained for each game intent event type and their maximum sizes.
5. **Perform processing based on the game intent event type**

   Perform required processing based on the game intent event type using the property values obtained in step ([4](basic-procedure.html#np-game-intent-library-overview_1_2__np-game-intent-library-overview_1_2_4)). For example, perform processing to join a Player Session for the Join Session game intent event type.

   Note:

   Refer to the [Game Intent System Overview - Game Intent Event Types and Properties](../Game_Intent_System-Overview/game-intent-event-types-and-properties.html) chapter for each game intent event type and the required processing for each type.
6. **Terminate the library**

   Call `sceNpGameIntentTerminate()` to terminate the library when you no longer need to receive game intent information.

# Implementation Example

A typical implementation of this library is shown below:

```
#define PLAYER_SESSION_ID_MAX_SIZE  (37)
#define MEMBER_TYPE_MAX_SIZE        (17)

SceNpGameIntentInitParam initParam;
sceNpGameIntentInitParamInit(&initParam);
ret = sceNpGameIntentInitialize(&initParam);
if (ret < 0) {
// Error handling
}

SceSystemServiceStatus status;
ret = sceSystemServiceGetStatus(&status);
if (ret == SCE_OK) {

   for (int32_t i = 0; i < status.eventNum; i++) {

       SceSystemServiceEvent event;
       ret = sceSystemServiceReceiveEvent(&event);
       if ((ret == SCE_OK)
          && (event.eventType == SCE_SYSTEM_SERVICE_EVENT_GAME_INTENT)) {

          SceNpGameIntentInfo intentInfo;
          sceNpGameIntentInfoInit(&intentInfo);
          ret = sceNpGameIntentReceiveIntent(&intentInfo);
          if (ret == SCE_OK) {

             printf("User ID : %d"\n, intentInfo.userId);
             printf("Intent Type : %s\n", intentInfo.intentType);

             if (strncmp(intentInfo.intentType, "joinSession",
                sizeof(intentInfo.intentType)) == 0) {

                char playerSessionId[PLAYER_SESSION_ID_MAX_SIZE];
                ret = sceNpGameIntentGetPropertyValueString(
                    &intentInfo.intentData, "playerSessionId",
                    playerSessionId, sizeof(playerSessionId));
                if (ret == SCE_OK) {

                    printf("Player Session ID : %s\n", playerSessionId);
                }

                char memberType[MEMBER_TYPE_MAX_SIZE];
                ret = sceNpGameIntentGetPropertyValueString(
                    &intentInfo.intentData, "memberType",
                    memberType, sizeof(memberType));
                if (ret == SCE_OK) {

                    printf("Member Type : %s\n", memberType);
                }

                if (strncmp(memberType, "player",
                   sizeof(memberType)) == 0) {

                   // Omitted: processing to join a Player Session as a player
                }
                else if (strncmp(memberType, "spectator",
                   sizeof(memberType)) == 0) {

                   // Omitted: processing to join a Player Session as a spectator
                }
             }
          }
       }
   }
}

sceNpGameIntentTerminate();
```