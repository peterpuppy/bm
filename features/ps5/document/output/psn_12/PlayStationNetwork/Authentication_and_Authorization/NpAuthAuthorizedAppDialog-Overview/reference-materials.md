# NpAuthAuthorizedAppDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuthAuthorizedAppDialog-Overview/reference-materials.html

# Library Overview

# Purpose and Characteristics

The NpAuthAuthorizedAppDialog library provides the features for Authorized Apps to request consent from users to obtain access to user information managed by PlayStation™ Network.

The NpAuthAuthorizedAppDialog library provides the "NpAuth Authorized App dialog", a common dialog feature, and handles GUI display and user operations. The main usage flow is as follows.

1. Set the necessary parameters to call the dialog
2. Use polling to monitor when the dialog closes
3. Obtain the dialog polling results

Use this library when attempting to obtain authorization codes for Authorized Apps using the NpAuth library and user consent is required. For details about obtaining authorization codes for Authorized Apps, refer to the [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html) document.

# Main Features

The main features provided by the NpAuthAuthorizedAppDialog library are as follows.

* Feature for an Authorized App to request consent from users to obtain access to user information managed by PlayStation™ Network

# Embedding into a Program

Include np\_auth\_authorized\_app\_dialog.h in the source program. In addition, before calling any NpAuthAuthorizedAppDialog library API features in the program, load the PRX module with the relevant Sysmodule library function, as follows:

```
if (sceSysmoduleLoadModule(SCE_SYSMODULE_NP_AUTH_AUTHORIZED_APP_DIALOG) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceNpAuthAuthorizedAppDialog\_stub\_weak.a.

Additionally, embedding of the CommonDialog library is required in order to use the NpAuthAuthorizedAppDialog library. Link libSceCommonDialog\_stub\_weak.a. Note that loading of the CommonDialog library PRX module is performed automatically when executing the application. The CommonDialog library header file is also included automatically when np\_auth\_authorized\_app\_dialog.h is included.

# Sample Programs

Sample programs using the NpAuthAuthorizedAppDialog library are as follows.

## sample\_code/playstation\_network/api\_np\_auth\_authorized\_app

This sample program obtains authorization codes for an Authorized App using the NpAuth library and NpAuthAuthorizedAppDialog library.

# Reference Materials

For information such as common specifications and restrictions for common dialog features, refer to the following documents.

* [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html)
* [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html)

For details about Authorized Apps and obtaining authorization codes for Authorized App, refer to the following documents.

* [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html)
* [NpAuth Library Reference](../NpAuth-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpAuthAuthorizedAppDialog Library](../ReleaseNotes/PlayStation_Network-NpAuthAuthorizedAppDialog-ReleaseNotes.html)