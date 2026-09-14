# System Software User's Guide (Application Development Support) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Development_Support/information-display-features-for-development.html

# Development Support Features by Application

While the support features provided in "★Debug Settings" are common to all applications, there are also development support features provided that can be individually set for each application.

Note:

As a rule, only English text is supported in the setting names and options of development support features.

# Package Installation Feature

A feature is provided for installing application packages and additional content packages on development machines. The procedure is as follows:

1. Store the package (PKG) file(s) in the root directory of a USB drive
2. Connect (insert) the USB drive (in)to the development machine
3. From [Settings] - [★Debug Settings] in the system software, select [Game] - [Package Installer]
4. Package files stored on the USB drive will be displayed in a list. Installation of a given package file will begin when it is selected
5. If everything finishes normally, the installation is complete

Note:

Create PKG files using the Publishing Tools. Refer to a simple summary that is provided in [Publishing Tools Overview - Quick Start: Package Creation](../Publishing_Tools-Overview/quick-start-package-creation.html). The [PlayStation®5 Packaging Tutorial](../PS5_Packaging-Tutorial/__document_toc.html) document, which provides a more thorough explanation is also available, so refer to it as necessary.

# Information Display Features for Development

The options menu for an application is displayed by focusing on the icon of the package-installed application under development and pressing the options button. The user uses this screen of the system software when checking application information. Additional information is displayed on development machines.

## "★PlayGo Debug"

For details, refer to [PlayGo Library Overview - Features to Assist Development of PlayGo Compatible Applications](../PlayGo-Overview/features-to-assist-development-of-play-go-compatible-applica.html).

## "★Delete"

This feature individually deletes game content. When this menu is selected, a dialog for deleting each individual content will be displayed.

* ★Delete Patch:

  Deletes a patch of the corresponding application. If a patch package has been applied to the application but rebasing has not been performed when this feature is called, the application will be reverted to the state it was in before the patch package was applied. Nothing will happen if the feature is called when a reference package has been installed, when a remastered package has been installed, when a package has been rebased, or when the application has been updated via "Check for Update" from its options menu.
* ★Delete Addcont Extra Data:

  Deletes the extra data of additional content of the corresponding application.
* ★Delete Temp Data:

  Deletes temporary data.
* ★Delete Download Data:

  Deletes download data of the corresponding application.
* ★Delete User's All Save Data:

  Deletes the current user's save data for all applications. Note that the save data of all applications will be affected, not just the save data of the corresponding application.
* ★Delete All Users' All Save Data:

  Deletes all users' save data for all applications. Note that the save data of all applications will be affected, not just the save data of the corresponding application.

## "★Switch Content Config"

This feature switches the content config of a shared binary format application. A list of the application's content configs is displayed when "★Switch Content Config" is selected and you can switch the content config to use. Refer to [Content Packaging and Updating Guide - Packages Overview - Shared Binary: Packages for Multiple Countries/Regions](../Content_Packaging_and_Updating-Guide/shared-binary-packages-for-multiple-countries-regions.html) for details about the shared binary format.

Note:

"★Switch Content Config" can be used only by applications that have been installed by either of the methods described below.

However, even if the application has been installed by either of the methods described below, a content config can't be switched if the application has been moved to USB extended storage or if any of the application's PlayGo scenarios or languages have been deleted.

* Applications installed using "Settings" > "★Debug Settings" > "Game" > "Package Installer" in the system software.
* Applications installed using the install package feature of Target Manager

Note:

If the target application to be switched with "★Switch Content Config" is already installed, the new installation will overwrite the existing application install. When this happens, any patch package applied to the target application to be switched will be deleted. This feature does not support switching the content configs of additional content packages. Therefore, the content configs of any related additional content packages will not be switched despite the content config of the application being switched.

The list displayed when "★Switch Content Config" is selected includes the following information:

* ContentId:

  The content of contentId included in the param.json file is displayed. For the currently set content config, current will be displayed in addition to contentId.
* Config Label:

  The content config label will be displayed.

## "★Show Activity Configuration"

Refer to [GameIntent System Overview - Debugging Support for Developing Game Intent-Compatible Applications - Activity Configuration Screen for Checking Activity Configurations and for Performing Various Operations](../Game_Intent_System-Overview/activity-configuration-screen.html) for details.

## "★Activity Preview"

Refer to [GameIntent System Overview - Debugging Support for Developing Game Intent-Compatible Applications - Activity Preview Screen](../Game_Intent_System-Overview/activity-preview-screen.html) for details.

## "★Check"

This feature verifies the application and displays the result.

It is equivalent to the feature for verifying package files using the Publishing Tools (prospero-pub-cmd.exe img\_verify command, for example) but with the following differences:

* Additional content packages that have the same title ID as the application will also be verified.
* The content of some system files won't be verified.
* A log of the verification result will be stored on a USB drive if it is connected to the development machine before the verification is performed.

Note the following points:

* The entire package must be installed for the package file to be verified. A package may be installed in parts when the package download feature or Blu-ray Disc is used. Package file verification can't be performed in such cases.
* Execute "★Check" after terminating the application to be verified.
* If multiple applications with the same title ID are installed, "★Check" will always verify the application in slot #0.

# Installing Multiple Applications with the Same Title ID

This feature allows multiple applications with the same title ID to be installed on a single development machine. It is useful for testing the differences in behavior between builds, testing whether save data handling has changed, and so forth.

## Application Content for which Multiple Installations Are Possible

The only application content with the same title IDs that can be installed multiple times are application file sets and patch file sets. When the save data area, additional content file sets, download data area, temporary data area, trophy data, and so forth, are the same, they will be shared among multiple application file sets and patch file sets.

## Multiple Installations of an Application

Set "Settings" > "★Debug Settings" > "Game" > "Enable Multiple Installation with Same Title" to "On". This will allow up to 16 application packages with the same title ID to be installed without being overwritten.

## Switching Enabled Applications with "★Change Current Slot #"

Even if there are multiple installs, only one application will be displayed in the system software. When you place the focus on the displayed application icon and press the options button is, the options menu will be displayed, allowing you to switch the enabled application by selecting from the list displayed in "★Change Current Slot #".

In addition, you can then individually delete applications in the displayed list.

The following information will be included in the list displayed in "★Change Current Slot #".

* Slot Number:

  Displays the application slot number. "(current)" will be displayed for the enabled application if it is selected.
* Build Info:

  Normally displays the development build information for the application but will display the development build information set for the package file of the corresponding patch if a patch is applied.
* Last Updated:

  Normally displays the date/time of creation for the application but will display the date/time of creation for the package file of the corresponding patch if a patch is applied.
* Link:

  Displays the configuration status for the "Link Slot" feature of Target Manager for PlayStation®5. If the application's status is "linked", the slot number of the original, linked application will be displayed. (Example: "(linked to slot #0)".)

## Multiple Installations of a Patch

Patches will be installed to the slot set for the enabled application. Only one patch can be installed for each application that is installed. To install multiple patches and switch between them to perform operation testing, you will need to install multiple copies of the corresponding application or use the "Link Slot" feature of Target Manager for PlayStation®5.

## Deleting Applications

When an application is deleted from a system software screen, all the applications with the same title ID will be deleted. Note that it is possible to individually delete applications in the list displayed in "★Change Current Slot #".

## Handling of Applications on Blu-ray Discs

The feature for installing multiple applications with the same title ID does not support applications on Blu-ray Discs. Regardless of how "Settings" > "★Debug Settings" > "Game" > "Enable Multiple Installation with Same Title" is configured, the application on an inserted disc will be the one that runs. If there are differences with an already installed application, the application will be overwritten by an installation from the disc.

## How Package Downloader Is Handled

The feature for installing multiple applications with the same title ID does not support downloading using the Package Downloader feature. Regardless of what is set for "Enable Multiple Installation with Same Title", installations will result in the application being overwritten if a download is executed. In addition, downloading from an HTTP server using the `prospero-ctrl playgo initiate-download` command will result in an error if an application with the same title ID is already installed.

## How ★Switch Content Config Is Handled

Using ★Switch Content Config will result in an error if the feature for installing multiple applications with the same title ID has been used to install an application in any slot other than slot #0.

## How Moving Application Packages Is Handled

Attempting to move an application of the target title will result in an error if the feature for installing multiple applications with the same title ID has been used to install an application in any slot other than slot #0.

## Downgrading to a Version of the System Software that Does Not Support This Feature

If the feature for installing multiple applications with the same title ID has been used to install an application in any slot other than slot #0, errors may occur when launching applications or installing packages if the system software is downgraded to a version that does not support this feature (any version earlier than 6.00). If you are downgrading the system software, uninstall any applications that are installed in a slot other than slot #0. If you have already downgraded without uninstalling such applications, keep uninstalling packages until no application is displayed with the `prospero-ctrl package list` command.

# Feature for Setting States for Development

This feature causes specific states for performing application operation tests.

## "★Saved Data Management"

This is a shortcut to the "Save Data (PS5)" screen in "Settings". Among other things, on this screen you can set the corrupted state for save data. Refer to [SaveData Library Overview - Handling of Save Data during Development](../SaveData-Overview/handling-of-save-data-during-development.html) for details about save data-related development support features.