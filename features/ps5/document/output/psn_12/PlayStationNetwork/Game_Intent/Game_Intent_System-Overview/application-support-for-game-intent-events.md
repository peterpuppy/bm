# Game Intent System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Game_Intent_System-Overview/application-support-for-game-intent-events.html

# Application Support for Game Intent Events

This topic explains the preparation required for an application to use game intent events and a general flow of processing to carry out in the application.

## Parameter File (param.json) Creation and Placement

A parameter file describing which game intent event types are supported by the application is required for the application to receive game intent events. Create a parameter file beforehand, and place it in the prescribed location. (For details about the location to place the file, refer to the [Application Content Overview](../Application_Content-Overview/__document_toc.html) document.)

The application can only receive game intent events of the types that are written in the parameter file. For specifications regarding the settings to be included in parameter files for use with game intent events, refer to [NpGameIntent Library Overview - Reference Information - Parameter File (param.json)](../NpGameIntent-Overview/parameter-file-paramjson.html).

## Processing Performed in the Application

1. **Initialize the NpGameIntent library**

   Embed the NpGameIntent library in the application and initialize the library. Refer to the [NpGameIntent Library Overview](../NpGameIntent-Overview/__document_toc.html) and [NpGameIntent Library Reference](../NpGameIntent-Reference/__document_toc.html) documents for details.
2. **Monitor game intent events**

   The system notifies the application of a game intent event when the cause of a game intent event occurs with the user operating the system software screen (for example). An application supporting the game intent system must monitor this event. Monitor for this event as much as is possible. In particular, be sure to implement your application in a manner that considers the possibility that there may be notifications of game intent events immediately after it is launched.

   Note:

   Refer to "[Activity Configuration Screen for Checking Activity Configurations and for Performing Various Operations](activity-configuration-screen.html "This topic provides an explanation of the Activity Configuration screen. For example, you can check the information set to activities and launch activities from this screen.")" for information about features for testing behavior when an application is notified of game intent events immediately after being launched.
3. **Receive game intent information**

   An application should speedily receive game intent information when a game intent event occurs. The game intent event type and properties based on the event type will be included in the received information.

   When a second game intent event occurs before information of the first one can be received, the receiving of information for the first game intent event may fail. Ignore the failure and receive information of the new game intent event.
4. **Perform processing based on the game intent event type**

   Perform the necessary processing based on the type and property values included in the received game intent information. For example, perform processing to join a Player Session for the Join Session type event.