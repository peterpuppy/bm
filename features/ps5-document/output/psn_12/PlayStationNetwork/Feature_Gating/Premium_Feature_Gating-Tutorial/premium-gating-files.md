# Premium Feature Gating Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Premium_Feature_Gating-Tutorial/premium-gating-files.html

# Tutorial Application Files

This chapter provides details on the files contained in the tutorial game application.

# Premium Gating Files

This topic provides information on the files used for the premium feature gating feature.

The table below lists the primary files of the application along with a brief description of what each file does.

Premium Gating Files

| **Files** | **Description** |
| --- | --- |
| main.cpp | This file takes care of the initialization of the Common Dialog framework. As the Common Dialog can take some time to boot up, you should do the initialization early on if in-game commerce capabilities will be needed. |
| screen\_menu.cpp | This file contains the logic for the initial screen that is rendered in the application that triggers the premium gated feature. |
| screen\_check\_feature.cpp | This file contains the logic for triggering the premium check and upselling the subscription for unauthorized users. |
| premium\_checker.cpp | This file contains the logic for handling the premium check for each user and maintaining each user's authorization state. |
| screen\_multiplayer.cpp | This file contains the logic for the landing screen for any user that was authorized for the premium feature. It also handles system notifications. |
| screen\_message.cpp | This file contains the logic for displaying a message when the users are not authorized to use the multiplayer feature. |
| game\_session.h | This file contains shared multiplayer session data (for the purposes of this tutorial, this is just a list of players and a cross platform play flag). |

## UI Files

In addition to the above primary files, the project also contains some UI specific files such as ui\_button.cpp, ui\_panel.cpp, ui\_cursor.cpp, ui\_screen.cpp, and ui\_label.cpp.

These files contain layout code for the screens for the Tutorial game and as such do not demonstrate any use of the Premium Gating flow.