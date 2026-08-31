# SigninDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SigninDialog-Overview/reference-materials.html

# Library Overview

# Purpose and Characteristics

The SigninDialog library is a library that displays a sign-in screen for PlayStation™Network and causes users to be signed-in to PlayStation™Network.

Since localized text will be used in this sign-in screen in accordance with the console language, it will be possible to display messages for users in the appropriate language without the application independently providing messages in each language.

In addition to providing a sign-in screen that simply prompts users to enter their e-mail address and password, the SigninDialog library is fully equipped with the features required for starting usage of PlayStation™Network, such as a feature for users to have their password reset if it has been forgotten, and a feature that creates a new account if a user does not have an account for PlayStation™Network. By using the SigninDialog library, applications will be able to easily implement the procedures required for users to use PlayStation™Network.

The SigninDialog library hides GUI display and the handling of user operations. The basic usage flow is to first initialize dialog, then set the user ID of the user to sign in in the parameters, display the dialog, monitor for the closing of the dialog through polling, and finally perform termination processing for the dialog once it is closed.

# Main Features

The main features provided by the SigninDialog library are as follows.

* Feature to display a sign-in screen and cause a user to be signed-in to PlayStation™Network.

# Embedding into a Program

Include signin\_dialog.h in the source program. In addition, before calling any SigninDialog library APIs in the program, load the PRX module with the relevant Sysmodule library API, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_SIGNIN_DIALOG) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceSigninDialog\_stub\_weak.a.

# Sample Programs

Sample programs using the SigninDialog library are as follows.

## sample\_code/playstation\_network/api\_signin\_dialog

This sample shows the signin dialog.

# Reference Materials

For details on sign-in to PlayStation™Network, refer to the following document.

* [Np Library Overview](../Np-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - SigninDialog Library](../ReleaseNotes/PlayStation_Network-SigninDialog-ReleaseNotes.html)