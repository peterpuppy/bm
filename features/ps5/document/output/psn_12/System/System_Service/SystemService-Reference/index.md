# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/__toc.html

1. Obtaining System Parameters
   1. [SceSystemServiceParamId](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-param-id.html "SceSystemServiceParamId")
   2. [SceSystemParamLang](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-param-lang.html "SceSystemParamLang")
   3. [sceSystemServiceParamGetInt](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-param-get-int.html "sceSystemServiceParamGetInt")
   4. [sceSystemServiceParamGetString](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-param-get-string.html "sceSystemServiceParamGetString")
2. Obtaining Information for Each Rendering Frame
   1. [sceSystemServiceGetStatus](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-get-status.html "sceSystemServiceGetStatus")
   2. [SceSystemServiceStatus](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-status.html "SceSystemServiceStatus")
   3. [sceSystemServiceReceiveEvent](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-receive-event.html "sceSystemServiceReceiveEvent")
   4. [SceSystemServiceEvent](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-event.html "SceSystemServiceEvent")
   5. [SceSystemServiceEventType](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-event-type.html "SceSystemServiceEventType")
3. Switching Executable Files
   1. [sceSystemServiceLoadExec](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-load-exec.html "sceSystemServiceLoadExec")
4. Controlling Media Playback
   1. [sceSystemServiceDisableMediaPlay](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-disable-media-play.html "sceSystemServiceDisableMediaPlay")
   2. [sceSystemServiceReenableMediaPlay](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-reenable-media-play.html "sceSystemServiceReenableMediaPlay")
   3. [sceSystemServiceDisableMusicPlayer](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-disable-music-player.html "sceSystemServiceDisableMusicPlayer")
   4. [sceSystemServiceReenableMusicPlayer](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-reenable-music-player.html "sceSystemServiceReenableMusicPlayer")
5. Controlling GPU Load of the System Software
   1. [sceSystemServiceSetGpuLoadEmulationMode](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-set-gpu-load-emulation-mode.html "sceSystemServiceSetGpuLoadEmulationMode")
   2. [sceSystemServiceGetGpuLoadEmulationMode](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-get-gpu-load-emulation-mode.html "sceSystemServiceGetGpuLoadEmulationMode")
   3. [SceSystemServiceGpuLoadEmulationMode](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-gpu-load-emulation-mode.html "SceSystemServiceGpuLoadEmulationMode")
6. Obtaining the Display's Safe Area
   1. [sceSystemServiceGetDisplaySafeAreaInfo](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-get-display-safe-area-info.html "sceSystemServiceGetDisplaySafeAreaInfo")
   2. [SceSystemServiceDisplaySafeAreaInfo](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-display-safe-area-info.html "SceSystemServiceDisplaySafeAreaInfo")
7. Controlling the Power
   1. [sceSystemServicePowerTick](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-power-tick.html "sceSystemServicePowerTick")
8. Handling a Fatal Abnormal State
   1. [sceSystemServiceReportAbnormalTermination](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-report-abnormal-termination.html "sceSystemServiceReportAbnormalTermination")
9. Starting Controller Settings
   1. [sceSystemServiceShowControllerSettings](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-show-controller-settings.html "sceSystemServiceShowControllerSettings")
10. Obtaining HDR Display Parameters
    1. [sceSystemServiceGetHdrToneMapLuminance](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-get-hdr-tone-map-luminance.html "sceSystemServiceGetHdrToneMapLuminance")
    2. [SceSystemServiceHdrToneMapLuminance](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-hdr-tone-map-luminance.html "SceSystemServiceHdrToneMapLuminance")
11. Launching Player Dialogs
    1. [sceSystemServiceInitializePlayerDialogParam](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-initialize-player-dialog-param.html "sceSystemServiceInitializePlayerDialogParam")
    2. [sceSystemServiceLaunchPlayerDialog](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-launch-player-dialog.html "sceSystemServiceLaunchPlayerDialog")
    3. [SceSystemServicePlayerDialogParam](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-player-dialog-param.html "SceSystemServicePlayerDialogParam")
    4. [SceSystemServicePlayerDialogMode](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-player-dialog-mode.html "SceSystemServicePlayerDialogMode")
12. Clearing the Splash Screen
    1. [sceSystemServiceHideSplashScreen](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/sce-system-service-hide-splash-screen.html "sceSystemServiceHideSplashScreen")
13. Controlling the Notice Screen Skip Flag
    1. [sceSystemServiceGetNoticeScreenSkipFlag](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-get-notice-screen-skip-flag.html "sceSystemServiceGetNoticeScreenSkipFlag")
    2. [sceSystemServiceDisableNoticeScreenSkipFlagAutoSet](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-disable-notice-screen-skip-auto.html "sceSystemServiceDisableNoticeScreenSkipFlagAutoSet")
    3. [sceSystemServiceSetNoticeScreenSkipFlag](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-set-notice-screen-skip-flag.html "sceSystemServiceSetNoticeScreenSkipFlag")
14. Displaying Challenge Activity Cards
    1. [sceSystemServiceInitializeChallengeActivityParam](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-initialize-challenge-activity-param.html "sceSystemServiceInitializeChallengeActivityParam")
    2. [sceSystemServiceOpenChallengeActivity](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-open-challenge-activity.html "sceSystemServiceOpenChallengeActivity")
    3. [SceSystemServiceChallengeActivityParam](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-challenge-activity-param.html "SceSystemServiceChallengeActivityParam")
    4. [SceSystemServiceChallengeActivityScreen](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-challenge-activity-screen.html "SceSystemServiceChallengeActivityScreen")
    5. [SceSystemServiceChallengeActivityCohort](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-challenge-activity-cohort.html "SceSystemServiceChallengeActivityCohort")
15. Displaying Tournament Activity Cards
    1. [sceSystemServiceInitializeTournamentOccurrenceParam](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-init-tournament-occurrence-param.html "sceSystemServiceInitializeTournamentOccurrenceParam")
    2. [sceSystemServiceOpenTournamentOccurrence](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-open-tournament-occurrence.html "sceSystemServiceOpenTournamentOccurrence")
    3. [SceSystemServiceTournamentOccurrenceParam](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-tournament-occurrence-param.html "SceSystemServiceTournamentOccurrenceParam")
16. Launching Specific System Features
    1. [sceSystemServiceLaunchSystemDeeplink](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-launch-system-deeplink.html "sceSystemServiceLaunchSystemDeeplink")
17. Common Constants
    1. [Return Codes](https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-return-codes.html "Return Codes")