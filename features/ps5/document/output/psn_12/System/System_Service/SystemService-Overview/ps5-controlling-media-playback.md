# SystemService Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Overview/ps5-controlling-media-playback.html

# Using the Library

# Initializing and Terminating the SystemService Library

Use of the SystemService library does not require library initialization or termination. The system software will automatically perform the required processing upon application startup and termination.

# Obtaining System Parameters

Use `sceSystemServiceParamGetInt()` or `sceSystemServiceParamGetString()` to obtain system parameters. Specify the ID of the system parameter you want to obtain as an argument. The following example shows the obtainment of language settings.

```
/* Obtain the language settings set to the system software */
int32_t language;
ret = sceSystemServiceParamGetInt( SCE_SYSTEM_SERVICE_PARAM_ID_LANG, &language );
```

For other system parameters that can be obtained, refer to the [SystemService Library Reference](../SystemService-Reference/__document_toc.html) document.

## API Summary

The API features used for obtaining system parameters are shown below.

API Features for Obtaining System Parameters

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceParamGetInt()` | Function to obtain a system parameter (integer value) |
| `sceSystemServiceParamGetString()` | Function to obtain a system parameter (string) |
| `SceSystemServiceParamId` | System parameter ID |

# Obtaining the Notification of Events Occurring Outside the Application

1. **Check for events**

   First, use `sceSystemServiceGetStatus()` to check if events have occurred. The number of events that have occurred can be obtained using this function.

   ```
   SceSystemServiceStatus status;
   sceSystemServiceGetStatus(&status);
   if (status.eventNum > 0) {
       // Event occurrence handling
   }
   ```

   The number of events will be assigned to the member `eventNum` in the `SceSystemServiceStatus` structure.

   Performing this processing is recommended for every frame in order to quickly handle events.
2. **Obtain event occurrence notifications**

   After an event has occurred, use `sceSystemServiceReceiveEvent()` to check what kind of event has occurred. This function will insert and return information about the event that has occurred in the `SceSystemServiceEvent` structure.

   This function returns information about just one event for each call. If multiple events have occurred, repeatedly call this function for each event.

   ```
   SceSystemServiceStatus status;
   ret = sceSystemServiceGetStatus(&status);
   if (status.eventNum > 0) {
       for  (unsigned int i = 0; i < status.eventNum; i++) {
           SceSystemServiceEvent event;
           sceSystemServiceReceiveEvent(&event);
           switch (event.eventType) {
               // Handling according to event type
           }
       }
   }
   ```
3. **Handle occurred events**

   When an event occurrence notification is received, have the application perform processing according to the event type. The event type will be assigned to the member `eventType` in the `SceSystemServiceEvent` structure.

   This document does not explain individual events. For details, refer to the relevant documents.

## API Summary

The API features used for obtaining notification of events that have occurred outside the application are shown below.

API Features for Obtaining Events Occurring Outside the Application

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetStatus()` | Function to obtain the number of events that have occurred |
| `SceSystemServiceStatus` | Structure for storing the above information |
| `sceSystemServiceReceiveEvent()` | Function to obtain information from one event that has occurred |
| `SceSystemServiceEvent` | Structure for storing the above information |

# Obtaining the UI Status of the System Software

Use `sceSystemServiceGetStatus()` to obtain the system software UI status.

```
SceSystemServiceStatus status;
ret = sceSystemServiceGetStatus(&status);
if (status.isSystemUiOverlaid) {
    // Handling processing for system software UI overlay
}
```

`isSystemUiOverlaid` will be true when the controller input is being intercepted from system software UI in a state where the application is running in the foreground. It is possible for small displays that do not request user operation to be overlaid on application screens, but `isSystemUiOverlaid` will not be true in such cases.

## API Summary

The API features used for obtaining the system software UI status are shown below.

API Features for Obtaining the System Software UI Status

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetStatus()` | Function to obtain the system software UI status |
| `SceSystemServiceStatus` | Structure for storing the above information |

# Obtaining the Execution Status of an Application

Use `sceSystemServiceGetStatus()` to obtain the application's execution status.

```
SceSystemServiceStatus status;
ret = sceSystemServiceGetStatus(&status);
if (status.isInBackgroundExecution) {
    // Handling for running in background status
}
```

## API Summary

The API features used for obtaining the application's execution status are shown below.

API Features for Obtaining the Application's Execution Status

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetStatus()` | Function to check if the application is running in the background |
| `SceSystemServiceStatus` | Structure for storing the above information |

# Obtaining the Display Status of the VR Play Area Boundary

Use `sceSystemServiceGetStatus()` to obtain the display status of the VR play area boundary.

```
SceSystemServiceStatus status;
ret = sceSystemServiceGetStatus(&status);
if (status.isVrPlayAreaBoundaryOverlaid) {
    // Handling of the display of the play area boundary
}
```

The system software displays the play area boundary when the VR headset or PlayStation VR2 Sense™ controller approaches the play area boundary. The system software consumes more GPU resources than usual only if the system software UI and the play area boundaries are displayed at the same time.

For details about GPU resources when rendering the play area, refer to the [Programming Startup Guide](../Programming-Startup_Guide/__document_toc.html) document.

Refer to the [VrTracker2 Library Overview](../VrTracker2-Overview/__document_toc.html) document for details about the VR play area.

## API Summary

The API features used for obtaining the display status of the VR play area boundary are shown below.

API Features for Obtaining the Display Status of the VR Play Area Boundary

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetStatus()` | Function to check the display status of the VR play area boundary |
| `SceSystemServiceStatus` | Structure for storing the above information |

# Switching Executable Files

To switch the currently executed program with a different ELF file, use `sceSystemServiceLoadExec()`.

```
ret = sceSystemServiceLoadExec("/app0/foo.elf", nullptr);
if (ret = SCE_OK) {
    // Handling when failing to switch
}
```

To protect save data, executable files cannot be switched while the application is updating save data.

## API Summary

The function used to switch executable files is as follows.

Function for Switching Executable Files

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceLoadExec()` | Function to switch the application's executable files |

# Controlling Media Playback

To enable users to enjoy music or videos of their choice at the same time as the game, media playback by the system software is in the enabled state immediately after application startup. However, media playback can be prohibited by calling `sceSystemServiceDisableMediaPlay()` during the last scene of a game or at other times when you want the user to be immersed in the world of the game.

When it is no longer necessary to prohibit background playback, call `sceSystemServiceReenableMediaPlay()` to re-enable it.

## API Summary

API features used for controlling media playback are provided below.

API Features Used for Controlling Media Playback

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceDisableMediaPlay()` | Function to prohibit media playback by the system software |
| `sceSystemServiceReenableMediaPlay()` | Function to re-enable media playback by the system software |

# Controlling the GPU Load of the System Software

## Disturbance Rejection upon Performance Analysis

The system software uses the GPU irrespective of applications' operating states, and applications have no way of knowing before the fact when the system software will do so. Behavior by the system software such as this can interfere with performance analysis of applications. The system software can be instructed not to use the GPU to avoid such a situation by calling the following function:

```
sceSystemServiceSetGpuLoadEmulationMode
(SCE_SYSTEM_SERVICE_GPU_LOAD_EMULATION_MODE_OFF);
```

This instruction is only valid during application development.

## Other Methods to Change GPU Load

"★Debug Settings" in the system software and "Target Settings" in Target Manager for PlayStation®5 can also be used to change the GPU load.

## API Summary

The functions used for controlling the GPU load of the system software are as follows.

Functions for Controlling the GPU Load of the System Software

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceSetGpuLoadEmulationMode()` | Function to change the GPU load mode |
| `sceSystemServiceGetGpuLoadEmulationMode()` | Function to obtain the GPU load mode |

# Obtaining the Display's Safe Area

## Timing to Obtain the Safe Area

Make your application call `sceSystemServiceGetDisplaySafeAreaInfo()` upon startup to obtain information about the safe area to make adjustments as necessary, or use 0.90 as a value, to render important display contents within the safe area.

## API Summary

The function used for obtaining the display's safe area is as follows.

Function for Obtaining the Display's Safe Area

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetDisplaySafeAreaInfo()` | Function to obtain information about the safe area |

# Reporting a Fatal Abnormal State and Terminating the Application

When entering a fatal abnormal state in which the application program cannot properly continue its operation, `sceSystemServiceReportAbnormalTermination()` can be called to request the system software to forcefully terminate the application. The system software will report the occurrence of an error to the user and behave in the same manner as when the application generates a problem such as an invalid memory access.

Be aware that you must follow requirements that will be defined elsewhere to use `sceSystemServiceReportAbnormalTermination()`.

## API Summary

The function used for reporting a fatal abnormal state and terminating the application is as follows.

Function Used for Reporting a Fatal Abnormal State and Terminating the Application

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceReportAbnormalTermination()` | Function to report a fatal abnormal state and terminate the application |

# Launching the Controller Settings Screen

## Calling the Settings Screen

The system software is equipped with a "Controllers" settings feature that allows users to adjust various settings for controllers. Applications can call `sceSystemServiceShowControllerSettings()` in order to allow users to use this feature.

## API Summary

The function used for starting the controller settings is shown below.

Function Used for Starting the Controller Settings

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceShowControllerSettings()` | Function to show the "Controllers" settings screen |

# Obtaining HDR Display Parameters

## HDR Display Parameters

The system software comes with an "Adjust HDR" feature that allows users to set the HDR display parameters listed below. Applications can obtain the values that the user has set by calling `sceSystemServiceGetHdrToneMapLuminance()`.

HDR Display Parameters

| **Parameter** | **Description** |
| --- | --- |
| Max Full Frame Tone Map Luminance (MaxFFTML) | Maximum input luminance at which gradation is preserved even when the entire screen is bright |
| Max Tone Map Luminance (MaxTML) | Maximum input luminance at which gradation is preserved when 10% of the screen is bright |
| Min Tone Map Luminance (MinTML) | Minimum input luminance at which gradation is identifiable |

Based on these parameters, the primary HDR range (the range in which gradation is preserved in most scenes) and the extended HDR range (the range in which gradation is preserved depending on conditions, such as scenes where the majority of the screen is dark) can be obtained.

Note:

Using "★Debug Settings" > "Sound and Screen" > "Adjust HDR", application developers can set the values of MaxFFTML, MaxTML, and MinTML, either by selecting from lists for each item individually or by selecting a Display Category to set preset values for all three.

Example of a Tone Map

By rendering while targeting the primary HDR range, instances where the tones and shading of some objects would not be displayed properly - which would negatively affect the game experience - can be avoided. However, by rendering while targeting the extended HDR range, you can produce HDR representations that fully leverage the peak performance that the TV/display is capable of.

Note:

Be aware that the values for MaxFFTML, MaxTML, and MinTML each represent the luminance value input to the TV/display, rather than the luminance actually output by the TV/display. In many cases, these values are the signal ranges that the TV/display expects as input; internal signal processing by the TV/display replaces these with and then displays luminance levels appropriate for the TV/display.

Typically, the value of MaxFFTML is smaller than that of MaxTML; however, there are some TVs/displays for which MaxFFTML and MaxTML have extremely close values. In such cases, you can produce more appropriate HDR representations by, for instance, making the boundary between the primary HDR range and the extended HDR range min(MaxFFTML, 600), rather than MaxFFTML.

Note that displaying these HDR display parameter values on the screen as numerical values is prohibited, because doing so could confuse consumers about display performance. The values of HDR display parameters can only be used as the target parameters for graphics rendering.

This feature follows the guidelines of the HDR Gaming Interest Group. For information about the guidelines, refer to the link below:

* <https://www.hgig.org/>

## API Summary

The function used for obtaining HDR display parameters is provided below.

Function Used for Obtaining HDR Display Parameters

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetHdrToneMapLuminance()` | Function to obtain HDR display parameters |

# Launching Player Dialogs

By calling `sceSystemServiceLaunchPlayerDialog()`, applications can launch player dialogs, initiating actions concerning players on the PlayStation™Network. Player dialogs support the following modes.

* `SCE_SYSTEM_SERVICE_LAUNCH_PROFILE`:

  Launches a profile screen to display detailed information about the specified player
* `SCE_SYSTEM_SERVICE_SEND_FRIEND_REQUEST`:

  Sends a friend request from the user currently operating the system to the specified player
* `SCE_SYSTEM_SERVICE_BLOCK_USER`:

  Blocks the specified player

## API Summary

The functions used for controlling player dialogs are shown below.

Functions Used for Controlling Player Dialogs

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceInitializePlayerDialogParam()` | Function to initialize the player dialog structure |
| `sceSystemServiceLaunchPlayerDialog()` | Function to launch a player dialog in the specified mode |

# Clearing the Splash Screen

Upon application startup, the system software displays the startup image included in the application package as a splash screen. While this startup image is displayed, video output of the application will not be displayed.

To stop the system software from displaying the startup image, call `sceSystemServiceHideSplashScreen()`.

For information about startup images, refer to [Content Information Specifications - Startup Image [Application Information]](../Content_Information-Specifications/startup-image-application-information.html).

## API Summary

The function used for clearing the splash screen is as follows.

Function for Clearing the Splash Screen

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceHideSplashScreen()` | Function to stop the display of the startup image |

# Controlling the Notice Screen Skip Flag

## The Notice Screen Skip Flag

An application generally must at times display the logos of middleware that it employs, various warning messages, and other notice screens after its splash screen has been dismissed. However, displaying notice screens is not desirable from a user experience perspective. The Notice Screen Skip flag is a mechanism for leaving out as much of the showing of such screens as possible.

The application and the system software jointly manage the Notice Screen Skip flag, which is a non-volatile flag. The flag is set separately for each application and user account. When an application is first launched, the value of the flag is set to false.

The condition that must be met for the Notice Screen Skip flag to toggle to true is for a certain amount of time (2 minutes) to elapse after the application has been launched. The system software modifies the value of the flag automatically.

Have your application call `sceSystemServiceGetNoticeScreenSkipFlag()` immediately after it launches to obtain the value of the flag, and if it is true, skip the display of notice screens.

## Manually Setting the Notice Screen Skip Flag to true

A method of manually setting the Notice Screen Skip flag is provided for applications for which it would be unsuitable for the system software to invariably change the flag to true. With this method, the application, itself, can determine when and if to call an API feature to change the flag to true.

After the application launches, you must first promptly call `sceSystemServiceDisableNoticeScreenSkipFlagAutoSet()` so that the system software does not automatically change value of the flag (manually set mode). Then, call `sceSystemServiceSetNoticeScreenSkipFlag()` at the appropriate time to change the Notice Screen Skip flag to true.

## Notice Screen Skip Flag Behavior During Application Updates

The Notice Screen may change due to application updates. Since the system software is unable to detect Notice Screen updates, the Notice Screen Skip flag value will, by default, return to false when the application updates as a safety measure. If there are no changes to the Notice Screen following the application update, you can override the default behavior of the Notice Screen Skip flag when the application is updated by configuring the Notice Screen Version in the parameter file (param.json).

Notice Screen Version is a positive integer value that can be freely set by the application. If the Notice Screen Version is the same before and after the application is updated, the system software will assume that no changes have been made to the Notice Screen and use the Notice Screen Skip flag value from before the update. If the Notice Screen has changed following the application update and you want to display the Notice Screen, have the Notice Screen Version change so that its value differs before and after the application is updated. However, if the Notice Screen Version is set to 0, it is the same as if the Notice Screen Version is not set. Therefore, even if the Notice Screen Version is the same before and after the application is updated, the Notice Screen Skip flag value will revert to false.

Notice Screen Version and Notice Screen Skip Flag Examples for Before and After an Application Update

| **Before application update** | | **After application update** | |
| --- | --- | --- | --- |
| Notice Screen Version | The Notice Screen Skip Flag | Notice Screen Version | The Notice Screen Skip Flag |
| 1 | true | 1 | true |
| 1 | true | 2 | false |
| None (=0) | true | 1 | false |
| 1 | true | None (=0) | false |
| None (=0) | true | None (=0) | false |

**Parameter Definitions**

The parameter file is a file in the JSON format with the filename "param.json". The Notice Screen Version must be set in this JSON file according to the following format:

The Format of the noticeScreenVersion Object in param.json

| **Parameter** | | **Description** |
| --- | --- | --- |
| `systemService` | | Settings used for SystemService (object type, required) |
|  | `noticeScreenVersion` | Notice Screen Version (numerical value type, required) |

**Param File Examples**

```
{
  ...
  "systemService" : {
    "noticeScreenVersion" : 1
  },
  ...
}
```

## Development Support Features

There are settings for use during debugging that control the Notice Screen Skip flag: In "★Debug Settings" > "Game" > "Notice Screen Skip Flag" in the system software, features are provided that initialize the Notice Screen Skip flag, temporarily disable it, and so forth.

**Reset Notice Screen Skip Flag (for all users, for all games)**

This setting initializes the Notice Screen Skip flags for all users and all applications on the console.

**Reset Notice Screen Skip Flag (for current user, for specific games)**

This setting initializes the Notice Screen Skip flag for a specified application for the current user.

**Force Notice Screen Skip Flag False to Return**

When this setting is set to "On", the Notice Screen Skip feature is disabled, and applications are always treated as though it is first time they are being launched. The value of the Notice Screen Skip flag returned by `sceSystemServiceGetNoticeScreenSkipFlag()` will always be false.

The default setting is "Off".

## API Summary

API features used for controlling the Notice Screen Skip flag are shown below:

API Features Used with the Notice Screen Skip Flag

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceGetNoticeScreenSkipFlag()` | Function to obtain the value of the Notice Screen Skip flag |
| `sceSystemServiceDisableNoticeScreenSkipFlagAutoSet()` | Function to switch to the manually set mode |
| `sceSystemServiceSetNoticeScreenSkipFlag()` | Function to change the Notice Screen Skip flag to true |

# Displaying Challenge Activity Cards

By calling `sceSystemServiceOpenChallengeActivity()`, the application can open challenge activity cards on the screen and display interactions undertaken via challenges between users on PlayStation™Network. Challenge activity cards support the following modes:

* `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_DEFAULT`:

  Displays detailed information about the challenge
* `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_SCREEN_LEADERBOARD`:

  Displays the challenge leaderboard that shows global or friend rankings

You can specify the following cohorts when displaying a leaderboard on a challenge activity card:

* `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_DEFAULT`
* `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_FRIENDS`
* `SCE_SYSTEM_SERVICE_CHALLENGE_ACTIVITY_COHORT_GLOBAL`

Note:

If you select the global cohort, enable the global cohort in the activity settings.

## API Summary

The following API features are used to control challenge activity cards:

API Features Used to Control Challenge Activity Cards

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceInitializeChallengeActivityParam()` | Initializes a challenge activity card structure |
| `sceSystemServiceOpenChallengeActivity()` | Opens a challenge activity card with the specified parameters |

# Displaying Tournament Activity Cards

By calling `sceSystemServiceOpenTournamentOccurrence()`, you can open tournament activity cards onscreen. Users can join tournaments on PlayStation™Network from these action cards.

## API Summary

The following API features are used to control tournament activity cards:

API Features Used to Control Tournament Activity Cards

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceInitializeTournamentOccurrenceParam()` | Initializes a tournament occurrence structure |
| `sceSystemServiceOpenTournamentOccurrence()` | Opens a tournament activity card with the specified parameters |

# Launching Specific System Features

By calling `sceSystemServiceLaunchSystemDeeplink()`, an application can launch specific features that come standard as part of the system to allow users to use them.

## API Summary

The function used in launching specific system features is shown below.

Function Used in Launching Specific System Features

| **API feature** | **Description** |
| --- | --- |
| `sceSystemServiceLaunchSystemDeeplink()` | Launches a specific system feature |