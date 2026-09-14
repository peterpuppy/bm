# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/activation-system-passcode-management.html

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

# M.2 SSD － Set Encryption Key for Mount

For details, refer to the "★Debug Settings" > "M.2 SSD" > "Set Encryption Key for Mount" section of [M.2 SSD Storage Setup Guide - M.2 SSD-Related Features in ★Debug Settings](../M2_SSD_Storage-Setup_Guide/m2-ssd-related-features-in-debug-settings.html).

# M.2 SSD － Set New Encryption Key and Format

For details, refer to the "★Debug Settings" > "M.2 SSD" > "Set New Encryption Key for Format" section of [M.2 SSD Storage Setup Guide - M.2 SSD-Related Features in ★Debug Settings](../M2_SSD_Storage-Setup_Guide/m2-ssd-related-features-in-debug-settings.html).

# MCS Setting － Media Core Debug [DevKit Only]

This feature is for switching the debug feature of the Media Core "On" and "Off" when developing Media Core.

# MCS Setting － Allow BGM on Remote Viewer [DevKit Only]

This feature is not required for general development. Use it when directed by SIE.

# Media SDK － Disable ESVM

This feature is not required for general development. Use it when directed by SIE.

# Memory － Extended DMEM size setting

Refer to [Tool Memory Overview - Configuration of Tool Memory Using the Target Settings Application](../Tool_Memory-Overview/configuration-using-the-target-settings-application.html) for details.

# Network － NetCtlAp Wi-Fi Password for QA

Refer to [NetCtlAp Library Overview - Reference Information - PlayStation®5 Wi-Fi AP Information](../NetCtlAp-Overview/ps5-wi-fi-ap-information.html) for details.

# Network － NAT Traversal Information

Refer to [NpSessionSignaling Library Overview - Reference Information of the NpSessionSignaling Library - NAT Traversal Feature](../NpSessionSignaling-Overview/nat-traversal-feature.html) for details.

# Network － Ifconfig Information

Refer to [Net Library Overview - Internal Operations - Hints for Looking into Network Problems](../Net-Overview/hints-for-looking-into-network-problems.html) for details.