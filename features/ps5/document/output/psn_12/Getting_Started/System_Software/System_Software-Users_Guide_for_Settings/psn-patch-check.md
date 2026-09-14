# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/psn-patch-check.html

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

# Activation － Activate from USB

This feature is not required for general development. Use it when directed by SIE.

# Activation － Activate Using Internet － Activate Automatically

When this feature is set to "On", a connection will be made to the PlayStation®5 Developer Network at regular intervals through a network, and the expiration date will be updated. Activation will be performed in the background. The default state is "On". Because the status of a development machine will not change even if activation through a network fails, it won't be a problem to leave this feature "On".

To ensure automatic activation, it is recommended that you perform activation in advance from the "Activate Immediately" menu and confirm that activation through a network is possible.

# Activation － Activate Using Internet － Activate Immediately

When this feature is enabled, a connection will immediately be made to the PlayStation®5 Developer Network through a network and the expiration date will be updated.

Nothing in particular will be displayed when activation succeeds, but in cases where activation cannot be performed such as when network connection fails, an error message will be displayed.

# Activation － Activate Using Internet － Show Background Activation Result

This feature shows the results of activation performed in the background.

When "Activate Automatically" is set to "On", the results of activation performed at regular intervals in the background will be saved. The execution timing and execution results of the most recent activation can be checked with this feature.

# Activation － Show Expiration Date

This feature displays the expiration date of a development machine.

**Display examples:**

* "5 day +10:00:00"

  This indicates that the expiration date is 5 days and 10 hours from now.
* "This DevKit/TestKit is expired. Contact hardware administrator of your company, or see Activation Guide on PlayStation®5 Developer Network web site."

  This indicates that the expiration date has passed.
* "Cannot check clock. Set clock via Internet."

  The time is not set correctly in the development machine. Select "Date and Time" > "Set Date and Time" > "Set Using Internet" > "Set Now" to set the date and time.

A program that was built using the SDK can no longer be executed on a development machine for which the expiration date has passed. Refer to the activation guide posted on the PlayStation®5 Developer Network for information about how to update the expiration date.

# Activation － Show Activation Key

This feature displays the internal ID to be used when updating the expiration date of a development machine. Normally, this feature need not be used by a user, but it is one of the information items that the manager should be notified of for troubleshooting.

# Activation － System Passcode Management

To help mitigate the risk of a development machine (including applications installed on it) being stolen at exhibitions and other events, it is possible to set a system passcode. A system passcode is a simple 4-digit numerical string. If it is incorrectly entered five times in a row, the development machine will enter an activation expired state that would require a new activation to make the development machine usable again, thus protecting the installed applications. For details, refer to the [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html) document or the [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html) document.

# AV Content Management － Fake Generated Error

Refer to [ContentExport Library Overview - Reference Information - Development Support Features](../ContentExport-Overview/ps5-development-support-features.html) and [ContentSearch Library Overview - Reference Information - Development Support Features](../ContentSearch-Overview/ps5-development-support-features.html) for details.

# Boot Parameters － Release Check Mode

This setting relates to enabling/disabling the debug features and host tool development support features. DevKits have three options: "Release Mode", "Assist Mode", and "Development Mode". TestKits have two options: "Release Mode" and "Assist Mode". The current mode will be displayed in the upper left section of the home screen.

## Release Mode

When "Release Mode" is set, an application will be executed in an environment equivalent to that of a retail unit. The host file system cannot be accessed, debug features and workspaces cannot be used, and the memory size will become the same as that of a retail unit. Operation tests in the "Release Mode" are required in the final stages of development.

## Assist Mode

When "Assist Mode" is set, the following host tool development support features can be used. (However, debug trace features cannot be used.) Note that DEV LAN is used for communication with the host tool.

* Console (TTY) output to a host PC:

  Target console output (TTY) display will be possible from the Console Output application of the Target Manager or from the prospero-ctrl target console. In addition, input with STDIN will also be possible.
* Remote target control from a host PC:

  Remote control of the target (automatic target detection, connection, and disconnection) will be possible from the Target Manager.
* Target status display:

  Target status (target name/IP address, power status, activation expiration date, release check mode status) display will be possible from the Target Manager.
* Turning on/off the power and rebooting from a host PC:

  Remotely turning on/off the power and rebooting the target will be possible from the Target Manager or prospero-ctrl.
* Target activation from a host PC:

  Target activation will be possible from the Target Manager or prospero-ctrl.
* Displaying and changing target settings from a host PC:

  Displaying/changing target settings and importing/exporting configuration values will be possible from [Target Settings] of the Target Manager or prospero-ctrl.
* Updating the system software from a host PC:

  Remotely updating the system software using a system software update file located on a host PC will be possible with the Target Manager or with prospero-ctrl target update.
* Management of installed packages from a host PC (installing/uninstalling, displaying a list):

  Remotely installing/uninstalling a package file located on a host PC and displaying a list of installed packages will be possible with the Target Manager or prospero-ctrl package install/uninstall/list.
* Controlling (displaying/enabling/disabling/deleting) entitlements from a host PC:

  Remotely displaying, enabling, disabling, and deleting entitlements from a host PC will be possible with the Target Manager or prospero-ctrl package entitlement-list/entitlement-enable/entitlement-disable/entitlement-delete.
* Starting a package-installed application from a host PC:

  Remotely starting a package (\*.pkg) installed on the target will be possible from the host PC (example: prospero-ctrl application start).
* Accessing the target file system from a host PC:

  Accessing the file system on the target will be possible from Windows Explorer.
* Accessing a host PC file system from the target:

  Accessing the file systems (/host) on the host PC from a target application will be possible. In addition, specifying a file system on the host as a working directory will be possible.
* Creating, deleting, and managing workspaces from the host PC:

  Creating, deleting, and managing workspaces can be performed from Workspace Explorer or prospero-ctrl; the same tools can be used for pushing files from the host PC to workspaces and for pulling files from workspaces to the host PC.
* Running a program on a host PC from a host PC:

  Remotely running (debug operations will not be possible) a program (ELF) on a host PC will be possible in the following ways. When doing so, it will also be possible to specify a workspace as the working directory.

  + "Start Without Debugging" (Ctrl + F5) in Visual Studio
  + Running from prospero-run without /debug
  + Using the program load feature of the Target Manager
* Using workspaces for PlayGo emulation:

  You can use the PlayGo emulation feature by creating a PlayGo chunk definition file (playgo-chunks.xml) and placing it in the system directory (under WorkingDir) of a workspace.
* Forced termination of a running program and suspending/resuming an application from a host PC:

  Currently running programs can be forcibly terminated with prospero-ctrl process kill, and application suspend/resume operations can be performed with prospero-ctrl application suspend / resume.
* Running a program located in the workspace from the target home screen:

  Directly running a program located in the workspace without installing the package can be done from the ★Workspace icon displayed on the home screen.
* Accessing /devlog/app from an application:

  Accessing /devlog/app will be possible from an application. In addition, it will also be possible to access the demo work space from a host PC using Windows Explorer.
* Accessing game content installed in console storage from a host PC:

  Using Windows explorer, accessing game content for an application will be possible by mounting the specified application from a host PC.
* Obtaining screenshots from a host PC:

  It will be possible to take screen captures using the Screen Capture application of the Target Manager or prospero-ctrl target screenshot.
* Core dumps from a host PC:

  Using prospero-ctrl process-dump trigger, it will be possible to execute a core dump at the time of your choice.

## Development Mode

"Development Mode" can only be selected on a DevKit. All debugging/host tool support features can be used in the "Development Mode". Specify "Development Mode" during normal development.

# Controller Setting － Enable USB Connection

Refer to [Pad Library Overview - DualSense® Wireless Controller Features and Specifications - DualSense® Wireless Controller Connection Specifications](../Pad-Overview/connection-specifications.html) for details.

# Controller Setting － Pad Auto Detect

Refer to [Pad Library Overview - DualSense® Wireless Controller Features and Specifications - DualSense® Wireless Controller Connection Specifications](../Pad-Overview/connection-specifications.html) for details.

# Controller Setting － Enable Controllers for PS4 in Native Games

Refer to [Pad Library Overview - Controller Devices That the Pad Library Supports - Support for DUALSHOCK®4 Wireless Controllers During Development Only](../Pad-Overview/limited-use-of-dualshock4-wireless-control.html) for details.

# Controller Setting － Enable Play/Pause Button Emulation

This setting allows the Play button a remote control to be used as a Play/Pause button.

When the setting is turned "On", the system will act as though the Play/Pause button had been pressed when the Play button has been pressed.

This setting can be used when using the Play button on a remote control while developing an application that supports the Play/Pause button.

# Controller Setting － Disable Tracking LED battery saver of VR Controller

This feature disables the light control for the infrared LEDs built into the PlayStation VR2 Sense™ controller. It is set to "Off" by default and controls the state of the infrared LEDs. Setting it to "On" disables the light control and makes it so the infrared LEDs are always on.

In cases in which the PlayStation VR2 Sense™ controller cannot be correctly captured when developing applications that use VR, this feature can be used to determine whether the problem is caused by the system.

To reduce PlayStation VR2 Sense™ controller battery consumption, this feature should normally be set to "Off".

# Controller Setting － Disable VR controller battery check in pair connection dialog

This setting suppresses the displaying of the system dialog that is displayed when the battery of a PlayStation VR2 Sense™ controller is running low on charge to avoid the PlayStation VR2 Sense™ controller from being disconnected.

The PlayStation VR2 Sense™ controller restricts new connections based on a charging threshold that is higher compared to that of the DualSense® wireless controller so that it does not become unusable because of a lack of sufficient charge immediately after it starts being used. If application development work is interfered with by the system dialog that is displayed when a connected PlayStation VR2 Sense™ controller has insufficient charge left, turn this setting "On".

# Core Dump

Refer to [Core Dump System Overview - Appendix A: Setting the Core Dump Feature Using Debug Settings](../Core_Dump_System-Overview/ps5-setting-core-dump-feature-using-debug-settings.html) for details.

# Crash Reporting

Refer to [Core Dump System Overview - Appendix A: Setting the Core Dump Feature Using Debug Settings](../Core_Dump_System-Overview/ps5-setting-core-dump-feature-using-debug-settings.html) for details.

# Game Live Streaming

Refer to [GameLiveStreaming System Overview - GameLiveStreaming and Application Development - Settings for Development (★Debug Settings)](../GameLiveStreaming_System-Overview/settings-for-development-debug-settings.html) for details.

# Graphics － PA Debug [DevKit Only]

This setting enables or disables the PA Debug feature. When enabled, the GPU performance monitoring feature can be used. Select from the following:

* No
* Yes

# Graphics － System Load Control [DevKit Only]

This feature sets the system software GPU load. Refer to the [SystemService Library Overview](../SystemService-Overview/__document_toc.html) document and the [SystemService Library Reference](../SystemService-Reference/__document_toc.html) document for details about GPU load control in the system software.

The system software GPU load is normally 0.5 msec. Select "On" to apply the normal load.

# Graphics － PSML － PSML Debug [Trinity DevKit Only]

This feature controls whether to use the debugging version of the PSML library. The debugging version of the PSML library is provided together in a common interface with the release version of the library. You can switch between the debugging and release versions from this setting without having to rebuild the application.

Select "On" to load the debugging version of the library.

Refer to [PSML MFSR Overview - Basic Usage of the Psml Library - Debugging Version of the Library](../PSML_MFSR-Overview/debugging-version-of-the-library.html) for details.

# Graphics － Runtime validation of vertex export restrictions in Primitive & Mesh shaders for Standard PlayStation®5 compatibility [DevKit Only]

Refer to [Shader Programming User's Guide - Shader Specification - Hardware Limitations for Primitive and Mesh Shaders](../Shader_Programming-Users_Guide/hardware-limitations-for-primitive-and-mesh-shaders.html) for details.

# Graphics － GPU Transcoding for Workarounds [Trinity DevKit Only]

If you are using a shader compiled for the Standard PlayStation®5, set this setting to "On" to avoid hardware issues present on the Proto1 Trinity Development Kit.

If "GPU Transcoding for Workarounds" is enabled, game processes will use 512 MiB of tool memory.