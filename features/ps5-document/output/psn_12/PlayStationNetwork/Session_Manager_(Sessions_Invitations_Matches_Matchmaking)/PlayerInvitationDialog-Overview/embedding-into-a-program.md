# PlayerInvitationDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerInvitationDialog-Overview/embedding-into-a-program.html

# Library Overview

This topic provides the library's purpose and characteristics, its main features, how to embed the library into an application, a sample program provided by SIE, and reference materials containing relevant information. These are provided as basic information that you should understand when using the PlayerInvitationDialog library.

# Purpose and Characteristics

The PlayerInvitationDialog library provides a feature for sending invitations to Player Sessions. For details on the invitation feature, refer to the [Session Manager Service Overview](../Session_Manager_Service-Overview/__document_toc.html) document.

The PlayerInvitationDialog library provides the "player invitation dialog", which is one of the common dialog features. It conceals the handling of GUI displays and user operations. The usage flow is summarized below:

1. Set the required parameters and call the dialog
2. Monitor the closing of the dialog by polling
3. Obtain the result of calling the dialog

The system sends invitations at appropriate timings according to parameters set by the application and user operations.

Note:

The Session Manager Web API can be used to send/receive invitations if you want to build your own UI.

# Main Features

The main features provided by the player invitation dialog are as follows.

## Sending Invitations

This feature sends invitations to users selected in the dialog according to the send parameters set in advance by the application.

The application can obtain whether the user sent the message or canceled the operation from the dialog call result.

## Sharing Player Sessions Using URLs

If it is possible to share a Player Session using an URL, the URL of the web page for joining the Player Session and a QR code for sharing the Player Session will be displayed after the user selects "Share Link" on the screen after the dialog is displayed. Note that the sharing of Player Sessions using URLs is not possible for PlayStation®4 applications.

For the details of the conditions under which it is possible to share Player Sessions using URLs, refer to [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html).

# Embedding into a Program

Include player\_invitation\_dialog.h in the source program. In addition, before calling any PlayerInvitationDialog library function in the program, load the PRX module with the Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_PLAYER_INVITATION_DIALOG) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libScePlayerInvitationDialog\_stub\_weak.a.

The CommonDialog library must be embedded to use the PlayerInvitationDialog library. Link libSceCommonDialog\_stub\_weak.a. The PRX module of the CommonDialog library is automatically loaded upon application execution. Moreover, the header file of the CommonDialog library will be automatically included by including player\_invitation\_dialog.h.

# Sample Program

A sample program that uses the PlayerInvitationDialog library is as follows. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

## sample\_code/playstation\_network/api\_webapi\_session\_manager

This program exemplifies basic usage of the PlayerInvitationDialog library.

# Reference Materials

For information regarding specifications, restrictions, etc., that are common to the common dialog features, see the documents below.

* [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html)
* [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - PlayerInvitationDialog Library](../ReleaseNotes/PlayStation_Network-PlayerInvitationDialog-ReleaseNotes.html)