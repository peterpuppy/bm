# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/sound-and-screen-fake-monitor-capability.html

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