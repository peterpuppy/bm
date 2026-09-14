# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/ps-vr.html

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

# Network － Route Information

This feature is used to display routing information.

# Network － Network Emulation

Refer to [Net Library Overview - Network Emulation](../Net-Overview/network-emulation.html) for details.

# Network － Network Packet Capture

Refer to [Network Overview - Debug-Related Features - Usage With ★Debug Settings](../Network-Overview/usage-with-debug-settings.html) for details.

# Network － mDNS

This feature is for switching the multicast DNS feature supported by the system software "On" and "Off".

# Network － IPv6 DNS

Refer to [Network Overview - Debug-Related Features - Usage With ★Debug Settings](../Network-Overview/usage-with-debug-settings.html) for details.

# Network － IP Version Debug

Refer to [Net Library Overview - IPv6](../Net-Overview/ipv6.html) for details.

# Network (DEV) － Single Cable Mode

Refer to [Network Overview - Development Machine Network Configuration](../Network-Overview/development-machine-network-configuration.html) for details.

# Network (DEV) － IP Address Settings (DEV)

This network setting corresponds to [Development Kit Setup Guide - Set Up the Development Kit - Network Settings for the DEV LAN Port](../DevKit-Setup_Guide/network-settings-for-the-dev-lan-port.html) and [Testing Kit Setup Guide - Set Up the Testing Kit - Network Settings for the DEV LAN Port](../TestKit-Setup_Guide/network-settings-for-the-dev-lan-port.html).

# Network (DEV) － Default Gateway (DEV)

Refer to [Network Overview - Development Machine Network Configuration](../Network-Overview/development-machine-network-configuration.html).

# Network (DEV) － Override TLS certifications for communication with Host Tools

TLS certifications for communication with Host Tools will be overrided with the certification files in /sce\_host\_tools on the USB storage device. Refer to "Target\_Manager\_CLI-Users\_Guide - Mutual TLS Encryption" for details about encrypted communication.

| File name | Description |
| --- | --- |
| client.crt | A client certificate |
| client.key | A client private key (Keys encrypted with a passphrase are not supported; place a decrypted key.) |
| server.crt | A server certificate |
| server.key | A server private key (Keys encrypted with a passphrase are not supported; place a decrypted key.) |
| root\_ca.crt | A root CA certificate |

# PlayStation VR

The following settings can be configured. For details, refer to [Virtual Reality System Overview - Appendix A: Development Support Features](../Virtual_Reality_System-Overview/appendix-a-development-support-features.html).

* Social Screen Output Setting for Debug
* Auto Power On
* Change Eye-to-Eye Distance
* Show Eye-to-Eye Distance Setting Status
* Ignore Social Screen Separate Mode
* Tutorial and Safety Warning
* Enable notifications for incorrect usage of library
* Min Color Values for Reprojection

# PlayStation VR2

For details, refer to [Virtual Reality System Overview - Appendix A: Development Support Features](../Virtual_Reality_System-Overview/appendix-a-development-support-features.html).

# Power Save Settings － Disable Idle Power Save

This feature is not required for general development. Use it when directed by SIE.

# Remote Play － User Assign Mode

Refer to [Remoteplay Library Overview - Remote Play Mechanism - Registering a Client Device](../Remoteplay-Overview/registering-a-client-device.html) for details.

# Remote Play － Ignore Prohibition

This feature allows you to disable the setting to prohibit remote play.

Refer to [Remoteplay Library Overview - Using the Library - Setting to Prohibit Remote Play](../Remoteplay-Overview/setting-to-prohibit-remote-play.html) for the setting to prohibit remote play.

# Share － Contents Sharing Test from Share Function

This feature controls the sending of content to servers for various services using the Share feature.

When set to "Disable" (the default), nothing is sent. When set to "Enable", content is sent to servers.

Because this setting is reset to "Disable" when the PlayStation®5 is turned off, it needs to be set to "Enable" every time the system is started.

# Share － Enable Control Share Range

This feature controls the level of privacy when video is uploaded, or gameplay is broadcast, to YouTube by using the Share feature.

When set to "Disable" (default), upload or broadcast will only be possible with the privacy level of "Private".

When set to "Enable", upload or broadcast will be possible with an arbitrary privacy level specification as on a retail unit.

Because this setting is reset to "Disable" when the PlayStation®5 is turned off, it needs to be set to "Enable" every time the system is started.

# Share － Fake Generated Error

Refer to [Share Library Overview - Development Support Features](../Share-Overview/development-support-features.html) and [VideoRecording Library Overview - Notes](../VideoRecording-Overview/notes.html) for details.

# Share － Recording Capture Target

Refer to [Share Library Overview - Development Support Features](../Share-Overview/development-support-features.html) for details.

# Share － Recording Capture Area

Refer to [Share Library Overview - Development Support Features](../Share-Overview/development-support-features.html) for details.

# Share － Recording Prohibition

Refer to [Share Library Overview - Development Support Features](../Share-Overview/development-support-features.html) for details.

# Share － Service Availability Check

This feature is not required for general development. Use it when directed by SIE.

# Sound and Screen － Set HDCP Encryption

This setting is for choosing whether or not to encrypt the HDMI signal. Setting this to "Off" will remove the encryption.

This feature will not have any effect when encryption is forcibly disabled; however, "Settings" > "System" > "Enable HDCP" will have an effect on the operation of applications that handle DRM content.

# Sound and Screen － Play Dummy Music

This feature plays back a test BGM that is equivalent to the user operating the system music player in the background. Use this feature to confirm that application operation and BGM playback can be carried out as intended.

When using a DevKit, a wav file in the following format will be played back as BGM when it is placed on the development host computer as /host/MusicPlayer.wav.

* Data expression: signed 16-bit linear PCM
* Number of channels: 2ch stereo (interleaved L-R order per sample)
* Sampling frequency: 48000 Hz
* Endian: little endian

Note that other Music application sounds will not be played back while test BGM is being played back with this feature.

## On

You can perform a test equivalent to running the system music player in the background.

## On(System Prior)

You can perform a test equivalent to BGM output being prioritized by the system.

In some cases, the system will prioritize BGM output even if the application is calling `sceSystemServiceDisableMediaPlay()` (example: during video playback in an action card). In these kinds of cases, confirm that application operations and BGM playback take place as intended. If the application has not called `sceSystemServiceDisableMediaPlay()`, there is no difference between this setting and "On".

# Sound and Screen － Audio Output Format

This feature sets the audio output format. Select from the following:

## Auto

Automatically selects the format according to the setting of "Settings" > "Sound and Screen" > "Audio Output Settings" > "Audio Format (Priority)".

## LPCM 2ch

## LPCM 5.1ch

## LPCM 7.1ch

## Dolby Digital 5.1ch

## Dolby Atmos 7.1.4ch

## DTS 5.1ch

## LPCM 2ch (Headphone 3D Audio)

## LPCM 2ch (TV Virtual Surround)

# Sound and Screen － Audio Process Mode [DevKit Only]

This feature sets the audio processing mode. Select from the following:

## Release Mode

Normal mode

## Debug - Capture Mode

This mode captures audio using the Sulpha Tool.

Audio output to HDMI, optical digital output terminal, speaker on the wireless controller, etc., can be captured. For use of the Sulpha Tool, refer to [Sulpha Tool User's Guide](../Sulpha_Tool-Users_Guide/__document_toc.html).

# Sound and Screen － Adjust HDR

Refer to [SystemService Library Overview - Using the Library - Obtaining HDR Display Parameters](../SystemService-Overview/ps5-obtaining-hdr-display-parameters.html) for details.

# Sound and Screen － Fake Monitor Capability

For details, refer to [VideoOut Library Overview - Appendix C: Tips for Developing with the Fake Monitor Feature](../VideoOut-Overview/appendix-c-tips-for-developing-with-the-fake-monitor-feature.html).

# Sound and Screen － Disable HDMI

For details, refer to [VideoOut Library Overview - Appendix C: Tips for Developing with the Fake Monitor Feature](../VideoOut-Overview/appendix-c-tips-for-developing-with-the-fake-monitor-feature.html).

# Sound and Screen － Remote Play 3D/Multichannel Audio

This feature sets whether to output 3D audio or multi-channel audio when outputting audio to a client device that is connected by remote play or to Remote Viewer.

Its use is assumed, for example, for developing 3D audio or multi-channel audio from a remote location.

## Off

Standard channel audio is output.

## On(Headphone 3D Audio)

3D audio for headphones is output.

Note that when this feature is set to "On", 3D audio for headphones will also be output for HDMI output.

## On(TV Virtual Surround)

3D audio for a TV is output.

Note that when this feature is set to "On", 3D audio for a TV will also be output for HDMI output.

## On(LPCM 5.1ch)

Linear PCM 5.1ch multi-channel audio is output.

Note that when this feature is set to "On", HDMI output will be linear PCM 2ch stereo audio.

## On(LPCM 7.1ch)

Linear PCM 7.1ch multi-channel audio is output.

Note that when this feature is set to "On", HDMI output will be linear PCM 2ch stereo audio.

## On(LPCM 7.1.4ch)

Linear PCM 7.1.4ch multi-channel audio is output.

Note that when this feature is set to "On", HDMI output will be linear PCM 2ch stereo audio.

# Sound and Screen － VRR Debug Override

This feature overwrites the application's VRR settings. Refer to [VideoOut Library Overview - VRR - System Settings](../VideoOut-Overview/system-settings.html) for details.

# Sound and Screen － Limit Monitor VRR Range

This feature limits the variable range of a VRR monitor for evaluation purposes. Refer to [VideoOut Library Overview - VRR - System Settings](../VideoOut-Overview/system-settings.html) for details.

# Sound and Screen － VRR Debug Peg to Fixed Rate

This feature temporarily fixes the refresh rate for debugging purposes during VRR. Refer to [VideoOut Library Overview - VRR - System Settings](../VideoOut-Overview/system-settings.html) for details.

# Sound and Screen － Restrict 8K Output [PS5® Pro Dedicated]

This feature is for testing application behavior when a switch cannot be made to 8K 60 Hz output due to insufficient system resources. Refer to [VideoOut Library Overview - Usage of Various Features (Primary Block) - 8K 60 Hz Output](../VideoOut-Overview/8k-60-hz-output.html) for details.

# System Update － Update Server URL

Refer to [Development Kit Setup Guide - Update the System Software](../DevKit-Setup_Guide/update-the-system-software.html) for details.

# Web － Enable URL Editing

This feature enables URL editing with a simple Internet browser feature. The following settings are possible.

* Off: The feature will be disabled.
* On: The feature will be enabled.

This feature is set to "Off" by default.

# Web － Root Certificate Loading Mode

This mode configures the root certificate used in TLS communication.

## System Default

This uses the root certificate included in the system software.

## System Default + Debug Root CA

This uses root certificates for development in addition to the root certificates included in the system software.

Using root certificates for development:

1. Prepare the root certificate (in PEM format) that you want to add
2. Save the root certificate from (1) as DEBUG\_CA\_LIST.cer
3. Copy the file from (2) to the root of a USB memory device
4. Set the USB memory device from (3) in the DevKit

## Nothing

The root certificate is not used (always results in an error when connecting using TLS communication).

# Web － Certificate Verification Mode

This mode configures the server-certificate verification in TLS communication.

## Ignore verification

The results of the server-certificate verification are ignored. Even if an abnormality is found in the verification results, this is not reported as an error.

## Verify certificate

This setting processes the TLS connection in accordance with the results of the server certificate verification.

# Web － SSL Error Behavior on Web Pages

This sets the method used to display the status of TLS communication errors occurring when webpage root documents provided through HTTPS are obtained.

## Show Errors

TLS communication errors are displayed.

## Ignore Errors

TLS communication errors are not displayed. A similar result can be obtained by setting "Certificate Verification Mode" to "Ignore verification".

# Web － Enable WebDriver

This feature is not required for general development. Use it when directed by SIE.

# Debug Settings List

A list of the features in "★Debug Settings" is shown below. DevKits set to Development Mode can use essentially all settings, but only the debug settings respectively marked with "Yes" can be used with DevKits set to Release Mode or Assist Mode and with TestKits.

| **Game** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Package Downloader** | | | | |  |  |  |  |
|  | | Download Request | | | Yes | Yes | Yes | Yes |
| Json URL of Content List | | | Yes | Yes | Yes | Yes |
| Auto Download and Install pkg | | | Yes | Yes | Yes | Yes |
| Download a Package | | | Yes | Yes | Yes | Yes |
| Package Installer | | | | | Yes | Yes | Yes | Yes |
| **SaveData** | | | | |  |  |  |  |
|  | | Debug Notification | | | Yes | Yes | Yes | Yes |
| Fake Free Space | | | Yes | Yes | Yes | Yes |
| Fake Owner | | | Yes | Yes | Yes | Yes |
| Ignore Broken Status | | | No | No | No | No |
| Rebuild Database | | | Yes | Yes | Yes | Yes |
| Rebuild Database on Launching Application | | | No | No | No | No |
| Set Fingerprint | | | No | No | No | No |
| Add Content Manager | | | | | Yes | Yes | Yes | Yes |
| Slow SSD Mode | | | | | Yes | Yes | Yes | Yes |
| Instant App Suspending | | | | | Yes | Yes | Yes | Yes |
| Enable Multiple Installation with Same Title | | | | | Yes | No | Yes | No |
| Enhanced Display Buffer Attributes and VideoOut Features | | | | | Yes | No | Yes | No |
| Internal Memory Dump | | | | | Yes | No | Yes | No |
| CPU/GPU Frequency | | | | | No | No | No | No |
| **Notice Screen Skip Flag** | | | | |  |  |  |  |
|  | | Reset Notice Screen Skip Flag (for all users, for all games) | | | Yes | Yes | Yes | Yes |
| Reset Notice Screen Skip Flag (for current user, for specific games) | | | Yes | Yes | Yes | Yes |
| Force Notice Screen Skip Flag False to Return | | | Yes | Yes | Yes | Yes |
| **SSD Write Throttling** | | | | |  |  |  |  |
|  | | Debug Notification | | | Yes | Yes | Yes | Yes |
| Mode | | | Yes | No | Yes | No |
| Reset Write Count | | | Yes | No | Yes | No |
| Fake Game Trials Mode | | | | | Yes | Yes | Yes | Yes |
| **Performance overlay** | | | | |  |  |  |  |
|  | | Enable | | | Yes | No | Yes | No |
| Position | | | Yes | No | Yes | No |
| Port | | | Yes | No | Yes | No |
| Output | | | Yes | No | Yes | No |
| **FPS** | | |  |  |  |  |
|  | Range | | Yes | No | Yes | No |
| SIE Reserved A | | | | | Yes | No | Yes | No |
| SIE Reserved C | | | | | Yes | No | Yes | No |
| SIE Reserved XYZ | | | | | Yes | Yes | Yes | Yes |
| Force PS5 Base Mode [Trinity DevKit only] | | | | | Yes | Yes | No | No |
| Enable Low Energy Mode | | | | | Yes | Yes | Yes | Yes |

| **System** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | TRC Check Notifications | | | | | Yes | Yes | Yes | Yes |
| Export Error/Notification History to USB Mass Storage | | | | | Yes | Yes | Yes | Yes |
| Region Settings | | | | | Yes | Yes | Yes | Yes |
| Use Default PRX Runtime Library | | | | | Yes | No | Yes | No |
| Debug Network Clock | | | | | Yes | Yes | Yes | Yes |
| Reset Network Clock | | | | | Yes | Yes | Yes | Yes |
| Debug NPDRM Clock | | | | | Yes | Yes | Yes | Yes |
| Fake parameter for PlayStation Camera calibration | | | | | Yes | Yes | Yes | Yes |
| Export setting info to USB Mass Storage | | | | | Yes | Yes | Yes | Yes |
| Boot History | | | | | Yes | Yes | Yes | Yes |
| Enable Pause key on keyboard | | | | | No | No | No | No |
| Enable Print Screen key on keyboard | | | | | No | No | No | No |
| GPI Switch | | | | | Yes | No | Yes | No |
| Fake Device Settings | | | | | Yes | Yes | Yes | Yes |
| Display Title ID on Home Screen | | | | | Yes | Yes | Yes | Yes |
| Force PlayStation VR Version | | | | | Yes | No | Yes | No |
| Sce Module Debug | | | | | No | No | No | No |
| Skip Warning Screen after Improper Shutdown | | | | | Yes | No | Yes | No |
| Skip Adjust Display Area/Adjust HDR Screen on New Monitor Connection | | | | | Yes | No | Yes | No |
| RNPS Config | | | | | Yes | Yes | Yes | Yes |
| Built-in System Applications | | | | | Yes | Yes | Yes | Yes |
| Video Resource Arbitration | | | | | Yes | Yes | Yes | Yes |
| Trigger Workspace Dump | | | | | Yes | No | Yes | No |
| Display Package Asset on Home Screen | | | | | Yes | Yes | Yes | Yes |
| Enable write cache for high speed workspace file transferring | | | | | Yes | No | No | No |
| Enable Workspace Garbage Collection | | | | | Yes | No | Yes | No |
| Disable SCE Module Version Check | | | | | Yes | No | Yes | No |
| Ignore PRX SDK Version Check | | | | | Yes | No | Yes | No |

| **Multi User** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Switch User Group | | | | | Yes | Yes | Yes | Yes |
| Display Account Information | | | | | Yes | Yes | Yes | Yes |
| Use Auto Assign & Login Feature in Debug Settings | | | | | Yes | No | Yes | No |
| Auto Assign Controller | | | | | No | No | No | No |
| Auto Assign Move | | | | | No | No | No | No |
| Auto Assign Audio Device | | | | | No | No | No | No |
| Auto Assign PlayStation VR | | | | | No | No | No | No |
| Auto Assign PlayStation VR2 | | | | | No | No | No | No |
| Auto Assign PlayStation VR2 Sense Controllers | | | | | No | No | No | No |
| **User XX** | | | | |  |  |  |  |
|  | | Edit Comments for This Account | | | Yes | Yes | Yes | Yes |
| Auto Login User | | | Yes | No | Yes | No |
| **PlayStation Network** | | |  |  |  |  |
|  | | Fake Plus Subscription Status | Yes | Yes | Yes | Yes |
| Fake [sceNpCheckPremium](../Np-Reference/sce-np-check-premium.html) result | | | Yes | Yes | Yes | Yes |

| **PlayStation Network** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | NP Environment | | | | | Yes | Yes | Yes | Yes |
| In-Game Commerce Debug | | | | | Yes | Yes | Yes | Yes |
| Patch Check | | | | | Yes | Yes | Yes | Yes |
| Update Test | | | | | No | No | No | No |
| Upgradable App Debug | | | | | Yes | Yes | Yes | Yes |
| Require purchased license | | | | | Yes | Yes | Yes | Yes |
| Disable Account Check in Media Space | | | | | No | No | No | No |
| Ignore NpTitleId set by API in Development Mode | | | | | No | No | No | No |
| Premium Recheck Event Interval | | | | | Yes | Yes | Yes | Yes |
| **Universal Data System data** | | | | |  |  |  |  |
|  | | Delete data of all users (console) | | | Yes | Yes | Yes | Yes |
| Delete data of this user (console) | | | Yes | Yes | Yes | Yes |
| Delete data of this user (console and server) | | | Yes | Yes | Yes | Yes |
| Universal Data System Development Mode | | | | | Yes | No | Yes | No |
| Universal Data System Debug Log | | | | | Yes | No | Yes | No |
| Universal Data System Rate Limit Notification | | | | | Yes | Yes | Yes | Yes |
| Show Activity Configuration | | | | | Yes | Yes | Yes | Yes |
| Tournaments | | | | | Yes | Yes | Yes | Yes |
| Activity Preview | | | | | Yes | Yes | Yes | Yes |
| WebTrace | | | | | No | No | No | No |
| Web API Force Rate Limit | | | | | Yes | Yes | Yes | Yes |
| Web API Force Rate Limit Target | | | | | Yes | Yes | Yes | Yes |

| **Activation** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Activate from Host | | | | | No | No | No | No |
| Activate from USB | | | | | Yes | Yes | Yes | Yes |
| **Activate Using Internet** | | | | |  |  |  |  |
|  | | Activate Automatically | | | Yes | Yes | Yes | Yes |
| Activate Immediately | | | Yes | Yes | Yes | Yes |
| Show Background Activation Result | | | Yes | Yes | Yes | Yes |
| Show Expiration Date | | | | | Yes | Yes | Yes | Yes |
| Show Activation Key | | | | | Yes | Yes | Yes | Yes |
| System Passcode Management | | | | | Yes | Yes | Yes | Yes |

| **AV Content Management** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Fake Generated Error | | | | | Yes | Yes | Yes | Yes |

| **Boot Parameters** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Release Check Mode | | | | | Yes | Yes | Yes | Yes |

| **Controller Setting** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Enable USB Connection | | | | | Yes | No | Yes | No |
| Pad Auto Detect | | | | | Yes | No | Yes | No |
| Enable Controllers for PS4 in Native Games | | | | | Yes | No | Yes | No |
| Enable Play/Pause Button Emulation | | | | | Yes | Yes | Yes | Yes |
| Disable Tracking LED battery saver of VR Controller | | | | | Yes | No | Yes | No |
| Disable VR controller battery check in pair connection dialog | | | | | Yes | No | Yes | No |

| **Core Dump** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Core Dump Mode | | | | | No | No | No | No |
| Dump Level | | | | | Yes | Yes | Yes | Yes |
| System Dump Level | | | | | Yes | Yes | Yes | Yes |
| Copy & Delete | | | | | Yes | Yes | Yes | Yes |
| Data Request | | | | | Yes | Yes | Yes | Yes |
| Upload | | | | | Yes | Yes | Yes | Yes |
| Upload Status | | | | | Yes | Yes | Yes | Yes |
| Video Duration | | | | | Yes | Yes | Yes | Yes |
| Screenshot | | | | | Yes | Yes | Yes | Yes |
| Gpu Mini Capture on Mini Coredump | | | | | Yes | Yes | Yes | Yes |
| CPU Trace Capture | | | | | No | No | No | No |
| Skip error screen when triggering a core dump by the application | | | | | Yes | Yes | Yes | Yes |

| **Crash Reporting** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Enable System Crash Reporting | | | | | Yes | Yes | Yes | Yes |
| Keep Corefiles | | | | | Yes | Yes | Yes | Yes |

| **Game Live Streaming** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Live Streaming Mode | | | | | Yes | Yes | Yes | Yes |
| Broadcast URL | | | | | Yes | Yes | Yes | Yes |
| Embedded Server URL | | | | | Yes | Yes | Yes | Yes |
| Social Feedback Latency | | | | | Yes | Yes | Yes | Yes |
| Social Feedback Mode | | | | | Yes | Yes | Yes | Yes |
| Social Message01(-10) | | | | | Yes | Yes | Yes | Yes |
| IRC Server URL | | | | | Yes | Yes | Yes | Yes |
| IRC Server Channel | | | | | Yes | Yes | Yes | Yes |
| IRC Server User Name | | | | | Yes | Yes | Yes | Yes |
| IRC Server Password | | | | | Yes | Yes | Yes | Yes |
| Embedded Broadcast Server | | | | | No | No | No | No |
| View Debug Broadcast | | | | | No | No | No | No |

| **Graphics** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | PA Debug | | | | | No | No | No | No |
| System Load Control | | | | | No | No | No | No |
| **PSML** [Trinity DevKit only] | | | | |  |  |  |  |
|  | PSML Debug [Trinity DevKit only] | | | | No | No | No | No |
| Runtime validation of vertex export restrictions in Primitive & Mesh shaders for Standard PlayStation®5 compatibility | | | | | No | No | No | No |
| GPU Transcoding for Workarounds [Trinity DevKit only] | | | | | Yes | Yes | No | No |

| **M.2 SSD** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Set Encryption Key for Mount | | | | | Yes | Yes | Yes | Yes |
| Set New Encryption Key and Format | | | | | Yes | Yes | Yes | Yes |

| **MCS Setting** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Media Core Debug | | | | | No | No | No | No |
| Allow BGM on Remote Viewer | | | | | No | No | No | No |

| **Media SDK** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Disable ESVM | | | | | Yes | No | Yes | No |

| **Memory** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Extended DMEM size setting | | | | | No | No | No | No |

| **Network** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | NetCtlAp Wi-Fi Password for QA | | | | | Yes | Yes | Yes | Yes |
| NAT Traversal Information | | | | | Yes | Yes | Yes | Yes |
| Ifconfig Information | | | | | Yes | Yes | Yes | Yes |
| Route Information | | | | | Yes | Yes | Yes | Yes |
| Network Emulation | | | | | Yes | Yes | Yes | Yes |
| **Network Packet Capture** | | | | |  |  |  |  |
|  | | Capture | | | Yes | No | Yes | No |
| Capture Type | | | Yes | No | Yes | No |
| mDNS | | | | | Yes | Yes | Yes | Yes |
| IPv6 DNS | | | | | Yes | Yes | Yes | Yes |
| IP Version Debug | | | | | Yes | No | Yes | No |

| **Network (DEV)** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Single Cable Mode | | | | | Yes | Yes | Yes | No |
| IP Address Settings (DEV) | | | | | Yes | Yes | Yes | No |
| Default Gateway (DEV) | | | | | Yes | Yes | Yes | No |
| Override TLS certifications for communication with Host Tools | | | | | Yes | No | Yes | No |

| **PlayStation VR** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Social Screen Output setting for Debug | | | | | Yes | No | Yes | No |
| Auto Power On | | | | | Yes | No | Yes | No |
| Change Eye-to-Eye Distance | | | | | Yes | Yes | Yes | Yes |
| Show Eye-to-Eye Distance Setting Status | | | | | Yes | Yes | Yes | Yes |
| Ignore Social Screen Separate Mode | | | | | Yes | Yes | Yes | Yes |
| Tutorial and Safety Warning | | | | | Yes | No | Yes | No |
| Enable notifications for incorrect usage of library | | | | | No | No | No | No |
| Min Color Values for Reprojection | | | | | Yes | No | Yes | No |

| **PlayStation VR2** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | VR headset Version Information | | | | | Yes | Yes | Yes | Yes |
| Firmware Update | | | | | Yes | Yes | Yes | Yes |
| Support VR headset connection in Testkit Assist Mode [TestKit only] | | | | | No | No | Yes | No |
| Fake Mount Information | | | | | Yes | No | Yes | No |
| Disable VR headset connectivity and play area check on VR mode | | | | | Yes | No | Yes | No |
| Fake Lens Separation Distance | | | | | Yes | Yes | Yes | Yes |
| Auto Power On | | | | | Yes | No | Yes | No |
| Show Safe Area Guide | | | | | Yes | Yes | Yes | Yes |
| Enable Play Area Editor Dump | | | | | No | No | No | No |
| Tutorial and Safety Warning | | | | | Yes | No | Yes | No |
| Enable Visual Brightness Adaptation | | | | | Yes | Yes | Yes | Yes |
| Emulate Max VR System Load | | | | | No | No | No | No |
| Disable VR headset Vibration Check Notification | | | | | Yes | No | Yes | No |
| Force VR App launch | | | | | No | No | No | No |
| Reprojection Background Control | | | | | No | No | No | No |
| Show Gaze Pointer | | | | | Yes | No | Yes | No |
| Show Angle Indicator | | | | | Yes | No | Yes | No |

| **Power Save Settings** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Disable Idle Power Save | | | | | Yes | No | Yes | No |

| **Remote Play** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | User Assign Mode | | | | | Yes | Yes | Yes | Yes |
| Ignore Prohibition | | | | | Yes | Yes | Yes | Yes |

| **Share** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Contents Sharing Test from Share Function | | | | | Yes | Yes | Yes | Yes |
| Enable Control Share Range | | | | | Yes | Yes | Yes | Yes |
| Fake Generated Error | | | | | Yes | Yes | Yes | Yes |
| Recording Capture Target | | | | | Yes | Yes | Yes | Yes |
| Recording Capture Area | | | | | Yes | Yes | Yes | Yes |
| Recording Prohibition | | | | | Yes | Yes | Yes | Yes |
| Service Availability Check | | | | | Yes | Yes | Yes | Yes |

| **Sound and Screen** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Set HDCP Encryption | | | | | Yes | Yes | Yes | Yes |
| Play Dummy Music | | | | | Yes | Yes | Yes | Yes |
| Audio Output Format | | | | | Yes | Yes | Yes | Yes |
| Audio Process Mode | | | | | No | No | No | No |
| Adjust HDR | | | | | Yes | Yes | Yes | Yes |
| Fake Monitor Capability | | | | | Yes | No | Yes | No |
| Disable HDMI | | | | | Yes | No | Yes | No |
| Remote Play 3D/Multichannel Audio | | | | | Yes | No | Yes | No |
| VRR Debug Override | | | | | Yes | No | Yes | No |
| Limit Monitor VRR Range | | | | | Yes | Yes | Yes | Yes |
| VRR Debug Peg to Fixed Rate | | | | | Yes | Yes | Yes | Yes |
| Restrict 8K Output [PS5® Pro Dedicated] | | | | | Yes | Yes | Yes | Yes |

| **System Update** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Update Server URL | | | | | Yes | Yes | Yes | Yes |

| **Web** | | | | | | DevKit  Assist Mode | DevKit  Release Mode | TestKit  Assist Mode | TestKit  Release Mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Enable URL Editing | | | | | Yes | No | Yes | No |
| Root Certificate Loading Mode | | | | | Yes | No | Yes | No |
| Certificate Verification Mode | | | | | Yes | No | Yes | No |
| SSL Error Behavior on Web Pages | | | | | Yes | No | Yes | No |
| Enable WebDriver | | | | | Yes | No | Yes | No |