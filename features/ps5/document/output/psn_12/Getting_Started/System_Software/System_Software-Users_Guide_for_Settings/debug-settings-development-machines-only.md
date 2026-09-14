# System Software User's Guide (Settings) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Settings/debug-settings-development-machines-only.html

# Features of the Settings Menu

Various configuration features that are related to application and system software operations are provided in the "Settings" menu of DevKits and TestKits. This topic provides supplementary information for application development regarding the features of the "Settings" menu.

**Conflicts with the Target Manager for PlayStation®5**

A development machine can be configured using the "Settings" feature of the system software or by using the Target Manager for PlayStation®5 on the development host PC. Note, however, that system operation can become damaged due to conflicts in the set values when both configuration methods are used at the same time. It is not a problem to have both settings menus opened at the same time, but make sure not to perform settings in both at the same time.

**Restoring Settings**

Start safe mode and restore settings if configuration information seems to be corrupted such as when system or application operation does not adhere to settings. This type of corruption can occur, for example, when the power of the development machine is turned off while settings are being made. For details about safe mode, refer to the [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html) document.

# Guide & Tips, Health & Safety, and Other Information

# Accessibility

# Network

## "Set Up Internet Connection"

On TestKits set to Assist Mode and on DevKits, the internet connection settings can also be configured from the development host PC. Refer to the [Target Settings Application User's Guide for Development Kit/Testing Kit Configuration](../Target_Settings_Application-Users_Guide_for_DevKit_TestKit_Configuration/__document_toc.html) document for details.

## Relationship Between "Network" and an Application

A network connection will automatically be established by the system software as needed. Applications will not perform network connection.

An application can obtain the network connection status using a NetCtl library function. Connection information including whether the device used for network connection is wired or wireless, the IP address, netmask, BSSID, and security settings can also be obtained.

Applications cannot change the content of "Network" settings.

# User and Account

## "Log In to PS5 Automatically"

This setting enables the user to log in automatically. The setting of "[Multi User － Use Auto Assign & Login Feature in Debug Settings](multi-user-use-auto-assign-login-feature-in-debug-settings.html)" in "★Debug Settings" will be prioritized over this setting on DevKits.

# Family and Parental Controls

## Relationship Between "Family and Parental Controls" and an Application

The family manager or guardian can set parental control restrictions for children's accounts belonging to the family. Of them, the restrictions for the following settings may need to be checked by the application and the application's behavior may need to be appropriately controlled. Note that the parental control settings cannot be displayed if users who can set parental controls have not been registered.

* "[Communication and User Generated Content](family-and-parental-controls.html#system-software-users-guide-settings_1_5__0_ref41496573)": Chatting or exchanging messages with other players, and viewing or sharing video, images, and text on PlayStation™Network
* "[Age level for games and apps](family-and-parental-controls.html#system-software-users-guide-settings_1_5__0_ref41496621)": Using games or applications that exceed the age restriction set by the family manager or guardian
* "[Web Browsing](family-and-parental-controls.html#system-software-users-guide-settings_1_5__0_ref41649860)": Displaying a URL shared in a message or game on a browser

**Communication and User Generated Content**

Applications must use the Communication Restriction Status Web API to check the settings for each user. Appropriately control application behavior so that features to text or voice-chat with other players, post images or video via the PlayStation™Network, and view posts by other users are not provided to restricted users.

Note:

There are two different settings, "Communicating with Other Players" and "Viewing Content Created by Other Players", on PlayStation®4, and the restriction targets differ. The two settings have been unified on PlayStation®5 so that the restriction targets that are controlled with the two settings on PlayStation®4 can be controlled with one setting. For details, refer to TRC [R5061](../../../TRC/latest/TRC/R5061.html).

Note:

An application including the features described above must use the Communication Restriction Status Web API to check whether to provide the features to all accounts that use the application, regardless of whether they are classified as children's or adult's accounts.

From the end user's point of view, the value returned by the Communication Restriction Status Web API can only be changed for children's accounts. However, for users who are deemed to have violated the PlayStation™Network Terms of Service, primarily due to reasons such as malicious social activities, in some cases the PlayStation™Network may set the value returned by the Communication Restriction Status Web API to "true" (meaning use is prohibited).

For details, refer to the [Communication Restriction Status Web API Overview](../../../WebAPI/latest/Communication_Restriction_Status_WebAPI-Overview/__document_toc.html).

**Age level for games and apps**

The system software enables or disables the launch of an application by a user based on the game age information set in param.json of each PlayStation®5 format game, age restriction set for the user by the family manager or guardian, and the user's country/region information. For details, refer to TRC [R5005](../../../TRC/latest/TRC/R5005.html).

Note:

The mechanism of control that is applied differs for PlayStation®4 format applications and PlayStation®5 format applications. For PlayStation®4 format applications, game startup and the use of a game's online features are controlled with separate settings. By contrast, PlayStation®5 format applications are controlled only by the game's startup setting. Note that for PlayStation®4 format applications running on the PlayStation®5 console, both game startup and the use of the game's online features must be restricted. For details, refer to TRC R4005, R4208, and R4209 included in the PlayStation®4 SDK.

**Web Browsing**

The system software restricts the display of a URL shared in a message or game on a browser based on the web browsing restriction for the user set by the family manager or guardian. For details, refer to TRC [R5161](../../../TRC/latest/TRC/R5161.html).

# System

## System Software

## System Updates of Development Machines

Refer to the [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html) document for details about system updates for development machines.

## HDMI

## "Enable HDCP"

Encryption can be forcibly disabled on a development machine. For details, refer to "[Sound and Screen － Set HDCP Encryption](sound-and-screen-set-hdcp-encryption.html)".

## Language

## Relationship Between "Language" and an Application

The "Console Language" settings can be obtained using a SystemService library API feature.

## Date and Time

## Relationship Between "Date and Time" and an Application

Applications cannot change the current date/time.

An application can use a function of the Rtc library or C and C++ standard libraries to obtain the current time in UTC or local time; conversions between UTC and local time are also possible.

In addition, SystemService library functions can be used to obtain the "Time Zone" (offset from UTC), "Date Format", and "Time Format" settings, as well as whether or not daylight saving time is in effect.

# Storage

## "Move PS5 Games"

Content updated using a patch package cannot be moved.

If the content is updated using a remastered package or rebased after being updated using a patch package, it can be moved. Refer to the [Content Packaging and Updating Guide](../Content_Packaging_and_Updating-Guide/__document_toc.html) document for details about these update packages and how to handle them.

# Sound

# Screen and Video

## "VRR - Apply to Unsupported Games"

VRR Type A is automatically applied by the system to titles that don't support VRR. For more details, refer to "VRR Output Due to User-Selected Settings" in [VideoOut Library Overview - VRR - Feature Overview](../VideoOut-Overview/feature-overview.html).

# Accessories

# Saved Data and Game/Apps Settings

# Notifications

# Captures and Broadcasts

# ★Debug Settings [Development Machines Only]

This is one of the menu items in "Settings" that is provided for development machines only; it includes various features for development support. For details, refer to "[Features of the ★Debug Settings Menu](features-of-the-debug-settings-menu.html "\"★Debug Settings\", which is one of the \"Settings\" items, is provided only for development machines and includes various features for development support. Some features are provided for specific models and for specific operation modes. This topic introduces the setting items in \"★Debug Settings\" and also provides a list summarizing the conditions under which each setting feature can be used.")".