# PlayerSelectionDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerSelectionDialog-Overview/reference-materials.html

# Library Overview

# Purpose and Characteristics

The PlayerSelectionDialog library displays a user's friend list (managed on the system) or various player lists, and obtains the account ID of the player selected by the user from among these lists. In addition to selecting them from friend list, players can be displayed by searching for them.

The PlayerSelectionDialog library provides the "player selection dialog", which is one of the common dialog features. It conceals handling of GUI display and user operation. Usage flow is summarized below.

1. Set the required parameters and call the dialog
2. Monitor the closing of the dialog by polling
3. Obtain the result of calling the dialog

# Main Features

The main features provided by the PlayerSelectionDialog library are as follows.

* Features to display a user's friend list and to obtain the account ID of the player the user has selected

# Embedding into a Program

Include player\_selection\_dialog.h in the source program. In addition, before calling any PlayerSelectionDialog library function in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_PLAYER_SELECTION_DIALOG) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libScePlayerSelectionDialog\_stub\_weak.a.

In addition, the CommonDialog library must be embedded to use the PlayerSelectionDialog library. Link libSceCommonDialog\_stub\_weak.a. The PRX module of the CommonDialog library is automatically loaded upon application execution. Moreover, the header file of the CommonDialog library will be automatically included by including player\_selection\_dialog.h.

# Sample Programs

The sample program using the PlayerSelectionDialog library is as follows.

## sample\_code/playstation\_network/api\_player\_selection\_dialog

This program is an example showing the basic usage of the PlayerSelectionDialog library.

# Reference Materials

For information regarding specifications, restrictions, etc., that are common to the common dialog features, see the documents below.

* [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html)
* [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - PlayerSelectionDialog Library](../ReleaseNotes/PlayStation_Network-PlayerSelectionDialog-ReleaseNotes.html)