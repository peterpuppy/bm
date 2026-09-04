# Premium Feature Gating Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Premium_Feature_Gating-Tutorial/gating-functionality.html

# Overview

This tutorial demonstrates the premium feature gating use case for PlayStation®5.

Certain PlayStation®5 games have premium features such as online multiplayer which are gated behind a subscription service such as PlayStation®Plus. This tutorial describes how a game handles these features from end-to-end, including encouraging upselling of subscription services when the player does not have a subscription to the needed service and wants to unlock the feature.

This tutorial is for game developers handling premium feature gating for their games. Use it in conjunction with the tutorial game code provided, which demonstrates an end-to-end implementation of this feature.

The accompanying sample program for this tutorial is at the following location in the SDK:

```
sample_code/playstation_network/tutorial_np_premium
```

# Gating Functionality

This topic provides information on the services you'll need to implement feature gating.

The main functionality needed to implement premium feature gating is listed below:

* **Premium Feature Check.**`sceNpCheckPremium()`, provided by the Np library, is a function used to carry out a Premium check. It specifies the type of Premium feature and checks if the user is eligible to use it. Two types of users are identified by `sceNpCheckPremium()`:

  + Users who possesses a PlayStation®Plus subscription.
  + Users that have usage eligibility when there are special conditions during promotions.
* **NP Commerce Dialog.** The NpCommerceDialog library provides the mode `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM` to display a dialog encouraging the user to join PlayStation®Plus.
* **Premium Feature Notification.**
  `sceNpNotifyPremiumFeature()`, provided by the Np library, is an API used to carry out a Premium notification. This is to notify the system that a premium feature is being used.
* **Premium Event Callback.** The Np library provides the function `sceNpRegisterPremiumEventCallback()` to register a callback for events when a user's Premium Feature access needs to be rechecked.
* **User Service Event Handling.**
  `sceUserServiceGetEvent()`, provided by the UserService library, allows your game to handle certain user service events (in this case user logoffs).

# Setup

This topic provides guidance on setting up your development environment before attempting this tutorial.

This tutorial uses the SampleUtil framework as a foundation to build the tutorial application. For more information on setting up a Development environment for PlayStation®5 refer to the [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html).

This tutorial assumes you are familiar with the development environment for PlayStation®5, have already downloaded the latest system software SDKs, and set the environment variables needed to compile the application.