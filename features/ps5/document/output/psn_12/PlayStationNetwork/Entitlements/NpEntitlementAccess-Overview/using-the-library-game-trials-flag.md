# NpEntitlementAccess Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Overview/using-the-library-game-trials-flag.html

# Using the Library: GameTrials Flag

This topic describes how to use the NpEntitlementAccess Library to handle the GameTrials flag that is set in each application in relation to PlayStation®Plus time-limited game trials. Features for testing are also described.

# Procedure for Obtaining the GameTrials Flag

The procedure for obtaining the GameTrials flag is shown below.

1. **Initialize the library**

   Initialize the library as explained in "[Procedure to Initialize the NpEntitlementAccess Library](procedure-for-initializing-the-library.html)".
2. **Obtain the GameTrials flag**

   Use `sceNpEntitlementAccessGetGameTrialsFlag()` to obtain the GameTrials flag.

   ```
   /* Obtain the GameTrials flag */
   SceNpEntitlementAccessGameTrialsFlag  GameTrialsflag;
   ret = sceNpEntitlementAccessGetGameTrialsFlag( &GameTrialsflag );
   ```

## GameTrials Flag Update Event

The GameTrials flag may change to "`SCE_NP_ENTITLEMENT_ACCESS_GAME_TRIALS_FLAG_OFF`" while the application is running due to the user purchasing the full game from the PlayStation™ Store. The SystemService library notifies the application of updates to the GameTrials flag using an event (`SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE`). The application, if it is using the GameTrials flag, can re-check the value of the GameTrials flag when it receives this event.

Note:

The AppContent library must be initialized to receive this event.

During the development stage, you can use "★Debug Settings" > "Game" > "Fake Game Trials Mode" to be notified of update events. For details, refer to the "[Development Support Feature for Obtaining the GameTrials Flag](procedure-for-obtaining-the-game-trials-flag.html#np-entitlement-access-library-overview_5_1__np-entitlement-access-library-overview_5_1_4)" section.

## Development Support Feature for Obtaining the GameTrials Flag

The GameTrials flag value can be set using "★Debug Settings" > "Game" > "Fake Game Trials Mode" as follows:

* Off: Set to `SCE_NP_ENTITLEMENT_ACCESS_GAME_TRIALS_FLAG_OFF`
* On: Set to `SCE_NP_ENTITLEMENT_ACCESS_GAME_TRIALS_FLAG_ON`

Use this feature for local testing. If the application is running, the set value will be reflected immediately in the GameTrials flag value that can be obtained using `sceNpEntitlementAccessGetGameTrialsFlag()`, and the application will be notified of the `SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE` event by the SystemService library.