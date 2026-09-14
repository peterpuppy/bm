# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-assignment-of-the-enter-button.html

# Application Specification Guidelines

This topic provides guidelines concerning several aspects that should be considered at the stage of application specification design. This topic discusses assignment of the Enter button, making use of game presets and accessibility settings, displaying the Notice Screen at launch, language support, mutual exclusion for BGM, and switching audio output.

# Assignment of the Enter Button

The Enter button of the system software is assigned to the cross button regardless of the license territory. Because of this, unify the assignment of the Enter button to the cross button in the application, as well, regardless of the license territory.

# Using Game Presets

In the system software, [Settings] > [Games and Apps] > [Game Presets] provides configuration items that can be commonly used by games, including items such as "Difficulty" and "Performance and Resolution". These configuration items are provided for the purpose of eliminating the user's burden of having to make settings for each game as much as possible. An application can obtain the configuration content using a UserService library function and reflect the configuration content onto the game. The handling of the configuration items can be freely determined by the application. Refer to the [UserService Library Overview](../UserService-Overview/__document_toc.html) document for details.

# Using Accessibility Settings

[Settings] > [Accessibility] in the system software provides configuration items that are essentially always applied to system screens and features. These items include "Text Size" and "Chat Transcription". Some of these settings, such as "Color Correction" and "Controller", are automatically reflected in games. Some of the settings can be obtained by the application using the SystemService library or UserService library API. The handling of the configuration items can be freely determined by the application. For example, an application can perform processing to modify in-game settings to match what has been configured in the system settings, such as by obtaining what has been set for "Text Size" and changing the in-application font size setting to a large size if that is what has been configured in the system settings. Alternatively, the application can recommend that the user change the settings. For details, refer to the [UserService Library Overview](../UserService-Overview/__document_toc.html) document and the [SystemService Library Reference](../SystemService-Reference/__document_toc.html) document.

# Notice Screen upon Application Startup

When an application uses middleware or other technical elements to which the rights are held by another company, it is sometimes necessary to display a Notice Screen such as a logo or warning text, as required by the rights holder. Generally, it is required to display the Notice Screen for a certain time upon application startup, but from a user experience point of view it is not desirable for it to be displayed every time the application is started, and the trend is now for such requirements be relaxed.

Therefore, the SystemService library provides a feature to skip the Notice Screen.

SIE has no specific rules concerning the use of this feature. Use it to reduce startup time within a range conforming to the requirements of the rights holder. For details about this feature, refer to [SystemService Library Overview - Using the Library - Controlling the Notice Screen Skip Flag](../SystemService-Overview/ps5-controlling-the-notice-screen-skip-flag.html).

# Language Support

The language used in the application can be freely determined. It is also not a problem for the language to be changed while the application is running; however, consistency must be maintained. Do not adopt specifications in which the language changes without explicit user operation.

The console language set by the user can be obtained with `sceSystemServiceParamGetInt()`. For details, refer to [SystemService Library Overview - Using the Library - Obtaining System Parameters](../SystemService-Overview/obtaining-system-parameters.html).

## Language Setting for SIE Dialogs

The language of SIE dialogs will always be displayed using the console language. Therefore, the application cannot specify a language.

## Examples of Language Setting Specifications

**Enabling language switches using the options menu in the application**

This example implements a menu for switching languages in the application's options menu. The application will not reference the console language at all.

**Obtaining and using the console language**

This example switches the language used in the application according to the console language obtained by using `sceSystemServiceParamGetInt()`. If the console language is not supported by the application, the application will select an appropriate language.

**Obtaining the console language and making it the default for the language setting menu**

This example implements a menu for switching languages in the application's options menu and uses the console language, obtained with `sceSystemServiceParamGetInt()` when the application starts as the default language. Because the console language is selected by the user, making that the default language for the application will free the user from having to switch the application language in most cases. If the console language is not supported by the application, the application will select an appropriate language in the same manner as the above implementation example.

## Language Mask Settings

The settings of the languages to be installed (language mask) are determined for each application at the start of installation. If the console language is changed after the start of installation, the system will not automatically change the language mask, and installation will not be performed. When an application supporting multiple languages assigns assets of each language to different PlayGo chunks, change the language mask explicitly in the application so that the required PlayGo chunk is installed. For details, refer to [PlayGo Library Overview - PlayGo System Overview - Selective Installation](../PlayGo-Overview/selective-installation.html).

# Multiple Region Support

A feature that is useful for applications to be sold in multiple regions is explained below.

## User-Defined Parameters of param.json

Use the user-defined parameters of param.json to change behavior for each package while using the same program file.

Any four 32-bit integers defined by the title developer can be included in param.json. These parameters can be obtained by the application with `sceAppContentAppParamGetInt()`.

By using this feature, param.json can be changed - while the program file included in the package file remains the same - to change the behavior of the application. For example, the following processing corresponding to each region can be carried out without having to change the program.

* Change the color of the blood flowing from the monster according to the value of the user-defined parameter 1
* Change the default game server according to the value of the user-defined parameter 2

# Mutual Exclusion for BGM

While an application is running in the foreground, users can play videos, music, or other content from other applications. The following explains the specifications recommended for applications to allow for proper exclusion/coexistence of application BGM with playback of these media.

## Recommended Specifications: Outputting to the BGM Virtual Device

Output to the BGM virtual device is recommended for application BGM. With BGM virtual device output, playback of media (music, video, etc.) by the system software, etc., will be prioritized automatically; therefore, applications will not need to perform processing, such as that for switching BGM.

## Alternate Specifications: Determining the Port Status and Outputting to the MAIN Virtual Device

If it will be difficult to separate BGM from the main game audio, it is also possible to output audio including BGM to the MAIN virtual device. However, in such cases the BGM virtual device port status must be determined, and control must be performed so that audio, including BGM, is output only when application BGM can be output.

Specifically, application BGM can be output to the MAIN virtual device when `sceAudioOutGetPortState()` is called with the handle of the BGM virtual device port as an argument and then the member `output` of the returned `SceAudioOutPortState` structure is a value other than `SCE_AUDIO_OUT_STATE_OUTPUT_UNKNOWN`. When output is `SCE_AUDIO_OUT_STATE_OUTPUT_UNKNOWN`, music from the system software (or other audio from the system) is being output; therefore, the application must output audio that does not include BGM.

## Disabling Media Playback by the System Software

In cases in which it is desired to prioritize the application worldview over users' preferred music or in cases in which playback of unspecified music or images will cause presentation problems, the playback of other media by the system software can be temporarily disabled by calling `sceSystemServiceDisableMediaPlay()`.

This feature must be used only when required. Once it is no longer required to disable media playback, call `sceSystemServiceReenableMediaPlay()`.

Even if the system software disables media playback, there is no guarantee that the application BGM will continue to be output. There are cases where application BGM will be temporarily overridden by audio output from the system software or another application. An applicable case would be, for example, when a movie is played on an action card.

[★Debug Settings] > [Sound and Screen] > [Play Dummy Music] is provided to check operation when media playback is disabled and to check cases where application BGM is temporarily overridden on DevKit or TestKit. For details, refer to the [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html) document.

# Switching Audio Output in Conformance with the System Software

An application can use one of the functions provided below to obtain the current system software audio output format, output attributes, or both.

* `sceAudioOutGetPortState()`
* `sceAudioOut2PortGetState()`
* `sceAudioOut2UserGetSupportedAttributes()`
* `sceAudioOut2GetSpeakerInfo()`

Using the information that is obtained, an application can perform processing such as conforming with the system software if it is outputting 2ch output by changing the audio output generated within the application itself to 2ch. It is permissible to structure your application so that it obtains the audio output format or the output attributes of the system software only when the application is launched and then continues outputting in conformance with that format or those attributes consistently afterward.

If your application performs processing like this in which it conforms with the audio output of the system software, confirm that, if the audio output format of the system software is changed, the application conforms appropriately and its audio is played back from connected devices.

Also take care to perform checks concerning audio output formats and output attributes for which your application does not follow the system software. For example, even if your application does not conform to 3D audio output attributes, perform operational checks for all the cases provided below, including when [Audio Output Format] is set to "LPCM 2ch (TV Virtual Surround)" or "Dolby Atmos 7.1.4ch" and when [Enable 3D Audio for Headphones] is set to "Enabled".

## Operational Checks Using an HDMI Device

Connect an HDMI device that supports the linear PCM 7.1ch and Dolby™ Atmos audio formats, then set [★Debug Settings] > [Sound and Screen] > [Audio Output Format] to one of the options provided below, and then launch the application and confirm that its audio is played back by the HDMI device. Do this for all the settings.

1. "LPCM 2ch"
2. "LPCM 5.1ch"
3. "LPCM 7.1ch"
4. "LPCM 2ch (TV Virtual Surround)"
5. "Dolby Atmos 7.1.4ch"

## Operational Checks Using Headphones

Connect a pair of stereo headphones (or a stereo headset) with a 3.5 mm plug via an analog audio connection to the headphone jack of a DualSense® wireless controller, and set the following settings:

* Set [Settings] > [Sound] > [Audio Output] > [Output Device] to "Headphones Connected to Controller "
* Set [Settings] > [Sound] > [Audio Output] > [Headphones] > [Output to Headphones] to "All Audio"
* Set [Settings] > [Sound] > [Audio Output] > [Headphones] > [Mono Audio for Headphones] to "Disabled"
* Set [★Debug Settings] > [Sound and Screen] > [Audio Output Format] to "Auto"

Additionally, set [Settings] > [Sound] > [3D Audio for Headphones] > [Enable 3D Audio for Headphones] to one of the options provided below, launch the application, and confirm that its audio is played back through the headphones. Do this for both settings.

1. "Enabled"
2. "Disabled"

For details, refer to the [AudioOut Library Overview](../AudioOut-Overview/__document_toc.html), [AudioOut Library Reference](../AudioOut-Reference/__document_toc.html), [AudioOut2 Library Overview](../AudioOut2-Overview/__document_toc.html), and [AudioOut2 Library Reference](../AudioOut2-Reference/__document_toc.html) documents.