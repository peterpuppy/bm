# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/game-enhanced-display-buffer-attributes-and-video-out-featur.html

# Features of the ★Debug Settings Menu

"★Debug Settings", which is one of the "Settings" items, is provided only for development machines and includes various features for development support. Some features are provided for specific models and for specific operation modes. This topic introduces the setting items in "★Debug Settings" and also provides a list summarizing the conditions under which each setting feature can be used.

Note:

Only English is supported for feature names and available choices in "★Debug Settings".

# Game － Package Downloader

For details, refer to [PlayGo Library Overview - Appendix C: Package Downloader](../PlayGo-Overview/appendix-c-package-downloader.html).

# Game － Package Installer

Refer to [System Software User's Guide (Application Development Support) - Development Support Features by Application - Package Installation Feature](../System_Software-Users_Guide_for_Development_Support/package-installation-feature.html) for details.

# Game － SaveData

Refer to [SaveData Library Overview - Handling of Save Data during Development](../SaveData-Overview/handling-of-save-data-during-development.html) for details.

# Game － Add Content Manager

Refer to [AppContent Library Overview - Using the Library: Additional Content - Development Support Features for Additional Content](../AppContent-Overview/development-support-features-for-additional-content.html) for details.

# Game － Slow SSD Mode

Refer to [Kernel Overview - File System - Slow SSD Mode](../Kernel-Overview/slow-ssd-mode.html) for details.

# Game － Instant App Suspending

Refer to [Programming Startup Guide - Application State Transitions - Suspension Operations During Development](../Programming-Startup_Guide/ps5-suspension-operations-during-development.html) for details.

# Game － Enable Multiple Installation with Same Title

This setting allows multiple applications with the same title ID to be installed.

When this menu item is set to "On", redundant applications will be added without being overwritten. For details, refer to [System Software User's Guide (Application Development Support) - Development Support Features by Application - Installing Multiple Applications with the Same Title ID](../System_Software-Users_Guide_for_Development_Support/installing-multiple-applications-with-the-same-title-id.html).

# Game － Enhanced Display Buffer Attributes and VideoOut Features

Refer to [VideoOut Library Overview - Usage of Various Features (Primary Block) - Expanded Features for Use During Development](../VideoOut-Overview/expanded-features-for-use-during-development.html) for details.

# Game － Internal Memory Dump

Refer to [Core Dump System Overview - Appendix A: Setting the Core Dump Feature Using Debug Settings](../Core_Dump_System-Overview/ps5-setting-core-dump-feature-using-debug-settings.html) for details.

# Game － CPU/GPU Frequency [DevKit Only]

Refer to [Kernel Overview - CPU Management - Power Management Through Control of Frequencies](../Kernel-Overview/power-management-through-control-of-frequencies.html) for details.

# Game － Notice Screen Skip Flag

Refer to [SystemService Library Overview - Using the Library - Controlling the Notice Screen Skip Flag](../SystemService-Overview/ps5-controlling-the-notice-screen-skip-flag.html) for details.

# Game － SSD Write Throttling

Refer to [Kernel Overview - File System - SSD Write Throttling](../Kernel-Overview/ssd-write-throttling.html) for details.

# Game － Fake Game Trials Mode

Refer to [NpEntitlementAccess Library Overview - Using the Library: GameTrials Flag - Procedure for Obtaining the GameTrials Flag](../NpEntitlementAccess-Overview/procedure-for-obtaining-the-game-trials-flag.html) for details.

# Game － Performance overlay

Refer to [Performance Overlay User's Guide - Using Performance Overlay](../PerformanceOverlay-Users_Guide/using-performance-overlay.html) for details.

# Game － SIE Reserved A

This feature is not required for general development. Use it when directed by SIE.

# Game － SIE Reserved C

This feature is not required for general development. Use it when directed by SIE.

# Game － SIE Reserved XYZ

This feature is not required for general development. Use it when directed by SIE.

# Game － Force PS5 Base Mode [Trinity DevKit Only]

Refer to "Force PS5 Base Mode Feature" in [Programming Startup Guide - Basic Information on Application Execution Environments - Application Operation Modes](../Programming-Startup_Guide/ps5-application-operation-modes.html) for details.

# Game － Enable Low Energy Mode

This setting enables low energy mode. Refer to "Low Energy Mode" in [Programming Startup Guide - Basic Information on Application Execution Environments - Application Operation Modes](../Programming-Startup_Guide/ps5-application-operation-modes.html) for details.

# System － TRC Check Notifications

This feature is for changing the display method of TRC Check Notifications. Refer to "TRC Check Notifications" of [Technical Requirements Checklist for PlayStation®5 - Test Case Overview](../../../TRC/latest/TRC/Test-Case-Overview.html) for details.

# System － Export Error/Notification History to USB Mass Storage

This feature saves the list of errors and notifications that can be viewed in "Settings" > "System" > "Error History" to a USB drive. When this feature is enabled, the error history will be saved as /notification/error\_notification\_log\_[console name]\_yyyymmdd\_hhmmss.txt (where yyyymmdd\_hhmmss is the file creation timestamp). This feature can also be used to check the notifications received when "[System － TRC Check Notifications](system-trc-check-notifications.html)" is enabled.

# System － Region Settings

This feature matches various system software settings such as "Console Language" and "Time Zone" to the specifications for a specific country/region.

When the setting for this feature is changed, the system will restart, and the various system software settings will be batch-changed to the default values for the respective country/region.

| **Configuration Value** | **Country/Region** | **License Territory** |
| --- | --- | --- |
| `Japan` | Japan | SIEJA |
| `North America` | North America | SIEA |
| `Oceania` | Oceania | SIEE |
| `UK` | UK | SIEE |
| `Southeast Asia` | Southeast Asia | SIEJA |
| `Russia` | Russia | SIEE |
| `Brazil` | Brazil | SIEA |
| `China` | China | SIEJA |
| `Off` | Off (DevKit only) | (Undefined) |

When this feature is set to "Off", the various settings will be returned to default values for DevKit.

Once this feature is configured, the default values for the selected country/region will be used every time initialization is performed with "Settings" > "Initialization" > "Restore Default Settings".

Note this feature only determines the default values of various system software settings, it does not affect application operation. There is no need for an application to obtain the configuration values for a country/region, and a method for obtaining them is not provided.

# System － Use Default PRX Runtime Library

Refer to [Sysmodule Library Overview - Package Installation](../Sysmodule-Overview/package-installation.html) for details.

# System － Debug Network Clock

Refer to [Rtc Library Overview - Using the Library - Referencing Network Time](../Rtc-Overview/referencing-network-time.html) for details.

# System － Reset Network Clock

Refer to [Rtc Library Overview - Using the Library - Referencing Network Time](../Rtc-Overview/referencing-network-time.html) for details.

# System － Debug NPDRM Clock

For details, refer to [PlayStation™Network Commerce Programming Guide - Development Support Functions - Operation Test upon Expiration of the Validity Period](../PSN_Commerce-Programming_Guide/operation-test-upon-expiration-of-the-validity-period.html).

# System － Fake parameter for PlayStation Camera calibration

This feature is for checking the Depth library's calibration data that is implemented on a PlayStation®4 application. When set to "On", the currently retained calibration data will be considered to be insufficient for the Depth library. When set to "Off", the normal status will be enabled.

Be sure to adjust PlayStation®Camera ("Settings" > "Devices" > "Camera" > "Adjust PlayStation Camera") before setting this feature to "On". If PlayStation®Camera is not adjusted, this setting cannot be set to "On".

# System － Export setting info to USB Mass Storage

This feature saves information about the execution environment to a USB drive. This feature is useful when you want to confirm in what kind of execution environment a problem occurred. When this feature is enabled, a file that includes the following information will be saved as /settings/settings\_[console name]\_yyyymmdd\_hhmmss.txt (where yyyymmdd\_hhmmss is the file creation timestamp) in the USB drive.

* System software version
* Console type
* Model number
* Serial number
* Online ID of currently logged in users
* Current video output settings
* Current audio output settings
* "Settings" > "Network" > "View Connection Status" results
* "Settings" > "★Debug Settings" > "Network" > "NAT Traversal Information" results
* "★Debug Settings" values in Release Mode that affect application execution

# System － Boot History

This feature displays the system software startup history.

# System － Enable Pause key on keyboard [DevKit Only]

This feature sets whether or not to use the Pause key of an external keyboard in an application.

The Pause key of an external keyboard is reserved by the system software to function in a manner equivalent to the PS button. Because of this, it is not normally possible for applications to use the Pause key of an external keyboard with the Ime library.

When this setting is "On", the Pause key can be used, but only on DevKits in Development Mode for debug purposes.

Note that the Pause key cannot be used on DevKits in Release Mode or Assist Mode, nor on TestKits or retail units.

# System － Enable Print Screen key on keyboard [DevKit Only]

This feature sets whether or not to use the Print Screen key of an external keyboard in an application.

The Print Screen key of an external keyboard is reserved by the system software to function in a manner equivalent to the create button. Because of this, it is not normally possible for applications to use the Print Screen key of an external keyboard with the Ime library.

When this setting is "On", the Print Screen key can be used, but only on DevKits in Development Mode for debug purposes.

Note that the Print Screen key cannot be used on DevKits in Release Mode or Assist Mode, nor on TestKits or retail units.

# System － GPI Switch

Refer to [Kernel Overview - Development Support - GPI Switch](../Kernel-Overview/gpi-switch.html) for details.

# System － Fake Device Settings

This feature is not required for general development. Use it when directed by SIE.

# System － Display Title ID on Home Screen

This feature displays the title ID over the content icon on the home screen and in libraries.

# System － Force PlayStation VR Version

This feature is not required for general development. Use it when directed by SIE.

# System － Sce Module Debug [DevKit Only]

Refer to [Sysmodule Library Overview - Package Installation](../Sysmodule-Overview/package-installation.html) for details.

# System － Skip Warning Screen after Improper Shutdown

When the power is not turned off properly, a warning screen will be displayed at the next startup. This feature specifies whether or not to automatically close this warning screen after the duration of a certain time.

* Off: Warning screen will not be closed unless by controller operation. (Default)
* On: The warning screen will be closed automatically without controller operation after the duration of a certain time.

Note:

When the power of the console is not turned off properly, it may cause system damage or data corruption/loss. Make sure to turn the power off properly and also to avoid a power interruption.

Note that, when this setting is set to "On", it is assumed that the warning is always agreed to. Make sure to use this setting with this in mind.

# System － Skip Adjust Display Area/Adjust HDR Screen on New Monitor Connection

When the system software detects that a new display has been connected, it will automatically display the display area settings screen and the HDR adjustment screen (the latter only during HDR output).

In situations in which these screens being displayed would be inconvenient, such as during automatic tests, setting this to "On" will stop them from appearing automatically.

This feature is set to "Off" by default.

# System － RNPS Config

This feature is not required for general development. Use it when directed by SIE.

# System － Built-in System Applications

This feature displays a list of built-in system application title IDs and versions.

Built-in system applications can be updated via "Check for Update" in the options menu.

# System － Video Resource Arbitration

This feature is not required for general development. Use it when directed by SIE.

# System － Trigger Workspace Dump

For details, refer to "Workspaces Overview - Workspace Dump - Triggering a Workspace Dump".

# System － Display Package Asset on Home Screen

For a given application, data uploaded to Content Pipeline is ordinarily displayed for the following assets: the still-image icon and title name displayed on the home screen and the background image displayed in the game hub

When this setting is "On", the displaying of data from Content Pipeline is disabled, and the data within the package installed on the console will be displayed onscreen instead.

This can be used, for instance, to check the assets within a patch package.

# System － Enable write cache for high speed workspace file transferring [DevKit Only]

Refer to "Workspaces Overview - High Speed Workspace File Transferring - Configuring High Speed Workspace File Transferring".

# System － Enable Workspace Garbage Collection

For details, refer to [Workspaces Overview - Workspace Garbage Collection](../Workspaces-Overview/workspace-garbage-collection.html)

# System － Disable SCE Module Version Check

For details, refer to "Version Checking in PS4 Test Mode" of [Sysmodule Library Overview - Package Installation - Version Checking PRX Files](../Sysmodule-Overview/ps5-version-checking-prx-files.html).

# System － Ignore PRX SDK Version Check

For details, refer to [Kernel Overview - Dynamic Libraries - Version Checking PRX Files](../Kernel-Overview/version-checking-prx-files.html) and [Sysmodule Library Overview - Package Installation - Version Checking PRX Files](../Sysmodule-Overview/ps5-version-checking-prx-files.html).

# Multi User － Switch User Group

Up to 16 users can be registered on a retail unit. When this feature is used, up to 64 users can be registered on DevKit. This feature is useful for checking operation when using multiple accounts with a variety of country/region and age settings.

This feature registers up to four user groups and can make any one of them active. The number of users that can be registered per group, that is, the number of users that can be simultaneously active, is still 16 as on a retail unit. To use a given account, select the user group that account is in, and then log in as that user.

# Multi User － Display Account Information

This feature displays detailed account information for PlayStation™Network on the login screen.

When this setting is "On", the account information of the selected user for PlayStation™Network will be displayed at the bottom section of the login screen.

# Multi User － Use Auto Assign & Login Feature in Debug Settings

This setting indicates which of the automatic login settings to enable: the settings specified with "Settings" > "★Debug Settings" > "Multi User" or the settings specified with "Settings" > "Login Settings".

The former allows up to four target users to be specified, while the latter allows only one target user to be specified.

If this feature is set to "On", the automatic login setting specified with "Settings" > "★Debug Settings" > "Multi User" will be enabled, and the automatic login setting specified with "Settings" > "Users" > "Login Settings" will be ignored.

If this feature is set to "Off", the automatic login setting specified with "Settings" > "★Debug Settings" > "Multi User" will be ignored, and the automatic login setting specified with "Settings" > "Users" > "Login Settings" will be enabled.

In addition, the "Auto Assign Controller" and "Auto Assign Audio Device" settings in "Settings" > "★Debug Settings" > "Multi User" will only work when this feature is set to "On".

# Multi User － Auto Assign Controller [DevKit Only]

This setting is for skipping the user confirmation screen for a controller.

* Off: A controller will not be automatically assigned.
* On: A controller will be automatically assigned. (Default)

When a controller is connected with this setting "On", the system software will search for a user without a controller from among the logged in users, and the newly connected controller will be automatically assigned to that user.

If such a user does not exist, UI for user confirmation will be displayed as usual.

This feature will only function when "Settings" > "★Debug Settings" > "Multi User" > "Use Auto Assign & Login Feature in Debug Settings" is set to "On".

Note:

Automatic assignment may still be performed when this feature is set to "Off", depending on the number of logged in users.

# Multi User － Auto Assign Move [DevKit Only]

# Multi User － Auto Assign Audio Device [DevKit Only]

This setting is for skipping the user confirmation screen for audio devices (headsets, headphones, microphones).

* Off: An audio device will not be automatically assigned. (Default)
* On: An audio device will be automatically assigned.

When an audio device is connected with this setting "On", the system software will search for a user without an audio device from among the logged in users, and the newly connected audio device will be automatically assigned to that user.

If such a user does not exist, UI for user confirmation will be displayed as usual.

This feature will only function when "Settings" > "★Debug Settings" > "Multi User" > "Use Auto Assign & Login Feature in Debug Settings" is set to "On".

Note:

Automatic assignment may still be performed when this feature is set to "Off", depending on the number of logged in users.

# Multi User － Auto Assign PlayStation VR [DevKit Only]

This setting is for skipping the user confirmation screen for VR headsets for PlayStation®VR.

* Off: A VR headset for PlayStation®VR will not be automatically assigned. (Default)
* On: A VR headset for PlayStation®VR will be automatically assigned.

When the power of a VR headset for PlayStation®VR is turned on with this setting "On", the system software will automatically select a user from among the currently logged in users and assign the VR headset to that user.

This feature will only function when "Settings" > "★Debug Settings" > "Multi User" > "Use Auto Assign & Login Feature in Debug Settings" is set to "On".

Note:

Even when this feature is set to "Off", the system may automatically assign a device without displaying the login screen if only one user is logged in.

# Multi User － Auto Assign PlayStation VR2 [DevKit Only]

This setting is for skipping the user confirmation screen for VR headsets for PlayStation®VR2.

* Off: A VR headset for PlayStation®VR2 will not be automatically assigned. (Default)
* On: A VR headset for PlayStation®VR2 will be automatically assigned.

When a VR headset for PlayStation®VR2 is powered on while this setting "On", the system software will automatically select a user from among the currently logged in users and assign the VR headset to that user.

This feature will only function when "Settings" > "★Debug Settings" > "Multi User" > "Use Auto Assign & Login Feature in Debug Settings" is set to "On".

Note:

Even when this feature is set to "Off", the system may automatically assign a device without displaying the login screen if only one user is logged in or if there is a user to whom a VR headset for PlayStation®VR2 or PlayStation VR2 Sense™ controller is assigned.

# Multi User － Auto Assign PlayStation VR2 Sense Controllers [DevKit Only]

This setting is for skipping the user confirmation screen for the PlayStation VR2 Sense™ controller.

* Off: A PlayStation VR2 Sense™ controller will not be automatically assigned. (Default)
* On: A PlayStation VR2 Sense™ controller will be automatically assigned.

When a PlayStation VR2 Sense™ controller is powered on while this setting "On", the system software will automatically select a user from among the currently logged in users and assign the pair of controllers to that user.

This feature will only function when "Settings" > "★Debug Settings" > "Multi User" > "Use Auto Assign & Login Feature in Debug Settings" is set to "On".

Note:

Even when this feature is set to "Off", the system may automatically assign a device without displaying the login screen if only one user is logged in or if there is a user to whom a VR headset for PlayStation®VR2 or PlayStation VR2 Sense™ controller is assigned.

# Multi User － User XX － Edit Comments for This Account

This feature adds a string to account information. The string set here is handled as a value set for the user currently operating the console, and, if "Settings" > "★Debug Settings" > "Multi User" > "Display Account Information" is set to "On", the string will be displayed as part of the user's account information when the focus is played on the user in the login screen.

# Multi User － User XX － Auto Login User

This setting automatically logs in one or more users without UI operation when the system starts. Up to four registered users can be set for automatic logins.

This feature will only function when "Settings" > "★Debug Settings" > "Multi User" > "Use Auto Assign & Login Feature in Debug Settings" is set to "On".

Note:

At least one or more users must be logged in for an application to be executed on the system. It is recommended that this feature be used to automatically log in a user when an application is started from a debugger (for example).

# Multi User － User XX － PlayStation Network － Fake Plus Subscription Status

Refer to [SaveData Library Overview - Using the Library - Notes About Loading Save Data on Other Consoles](../SaveData-Overview/notes-about-loading-save-data-on-other-consoles.html) for details.

# Multi User － User XX － Fake sceNpCheckPremium result

This feature checks the operation of Premium features and can be set per user.

When set to "On", the result for the user of `sceNpCheckPremium()` is always `authorized` being returned as true.

When set to "Off", the operation will be the same as a retail unit and a check will be performed to see if the user has entitlements to use Premium features as required.

# PlayStation Network － NP Environment

This feature sets environmental variables of the PlayStation™Network. Do not change the settings unless directed otherwise.

# PlayStation Network － In-Game Commerce Debug

For details, refer to [PlayStation™Network Commerce Programming Guide - Development Support Functions](../PSN_Commerce-Programming_Guide/development-support-functions.html).

# PlayStation Network － Patch Check

# PlayStation Network － Update Test [DevKit Only]

Refer to [GameUpdate Library Overview - Notes - Debug Settings](../GameUpdate-Overview/debug-settings.html) for details.

# PlayStation Network － Upgradable App Debug

Refer to [NpEntitlementAccess Library Overview - Using the Library: SKU Flags - Procedure for Obtaining the SKU Flag](../NpEntitlementAccess-Overview/procedure-for-obtaining-the-sku-flag.html) for details.

# PlayStation Network － Require purchased license

License purchase checks for applications and additional content will be performed in the same manner as on retail units when a choice other than "Off" is selected for this feature.

The same application startup check as on a retail unit will be performed when "Applications" is selected.

The same check for using additional content as on a retail unit will be performed when "Additional Contents" is selected.

The same checks for both applications and additional content as on a retail unit will be performed when "All" is selected.

# PlayStation Network － Disable Account Check in Media Space [DevKit Only]

This feature is for disabling the check for whether a user has signed up for PlayStation™Network when an application in the Media category starts.

# PlayStation Network － Ignore NpTitleId set by API in Development Mode [DevKit Only]

Refer to the description of `sceNpSetNpTitleId()` for details.

# PlayStation Network － Premium Recheck Event Interval

Refer to [Premium Features Guidelines - Application Processing - Recheck after Premium Check](../Premium_Features_Guidelines/recheck-after-premium-check.html) for details.

# PlayStation Network － Universal Data System data

Refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html) for details.

# PlayStation Network － Universal Data System Development Mode

Refer to [Universal Data System Guide - Local Development Workflow](../Universal_Data_System-Guide/local-development-workflow.html) for details.

# PlayStation Network － Universal Data System Debug Log

Refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html) for details.

# PlayStation Network － Universal Data System Rate Limit Notification

Refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html) for details.

# PlayStation Network － Show Activity Configuration

Refer to [Game Intent System Overview - Debugging Support for Developing Game Intent-Compatible Applications](../Game_Intent_System-Overview/debugging-support-using-the-system-software.html) for details.

# PlayStation Network － Tournaments

This feature is not required for general development. Use it when directed by SIE.

# PlayStation Network － Activity Preview

Refer to [Game Intent System Overview - Debugging Support for Developing Game Intent-Compatible Applications](../Game_Intent_System-Overview/debugging-support-using-the-system-software.html) for details.

# PlayStation Network － WebTrace [DevKit Only]

Refer to the [Web API Tracer User's Guide](../Web_API_Tracer-Users_Guide/__document_toc.html) for details.

# PlayStation Network － Web API Force Rate Limit

This setting is for checking application behavior when the call rate limit of PlayStation™Network Web APIs is exceeded.

When this setting is set to "Enable", an error for when the call rate limit is exceeded will be returned for Web API calls that go through the NpWebApi2 and NpCppWebApi libraries.

Refer to the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document for details of the call rate limits of Web APIs.

# PlayStation Network － Web API Force Rate Limit Target

When "Web API Force Rate Limit" is enabled, this setting allows you to check the behavior of an API group when the call rate limit for PlayStation™Network Web APIs is exceeded.

If you specify the name of an API group in this setting, an error for when the call rate limit is exceeded will be returned for that API group regarding Web API calls that go through the NpWebApi2 and NpCppWebApi libraries.

When this setting is not specified, an error for when the call rate limit is exceeded will be returned for the Web API calls of all API groups.

For example, when "Web API Force Rate Limit" is enabled and "leaderboards" is specified in "Web API Force Rate Limit Target", an error for when the call rate limit is exceeded will only be returned for Leaderboards Web API calls. For Web API calls of other API groups, an error for when the call rate limit is exceeded will not be returned and the calls will be made as usual.

# Activation － Activate from Host [DevKit Only]

This feature is not required for general development. Use it when directed by SIE.