# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/network-dev-default-gateway-dev.html

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