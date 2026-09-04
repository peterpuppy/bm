# Premium Feature Gating Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Premium_Feature_Gating-Tutorial/summary.html

# Summary

This topic summarizes the important steps and guidelines you should remember when implementing feature gating.

This tutorial has covered the steps needed to handle premium gated features in your game, presenting some real code snippets to understand each step.

To summarize some of the important guidelines and best practices:

* Initialize Common Dialog framework early on in game.
* Use an asynchronous request type for doing the premium check.
* Always upsell the subscription for any unauthorized users.
* Notify the system of the premium feature usage.