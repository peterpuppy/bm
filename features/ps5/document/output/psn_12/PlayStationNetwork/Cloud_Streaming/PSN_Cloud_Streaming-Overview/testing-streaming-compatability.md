# PlayStation™Network Cloud Streaming Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Cloud_Streaming-Overview/testing-streaming-compatability.html

# Using the Cloud Streaming Preview Application

This chapter provides details on how to use the Cloud Streaming Preview application.

With the Cloud Streaming Preview application, you can stream PlayStation®5 applications running on SIE cloud streaming servers in development environments.

To launch the Cloud Streaming Preview application, navigate to the home screen on your DevKit or TestKit and select **Cloud Streaming Preview**.

DevKit/TestKit Home Screen

After the application retrieves the accessible title list, it displays the following features:

* *Recent titles* - Displays the currently selected title.
* *Stream* - Activates streaming for the selected title.
* *View All Titles* - Displays all accessible titles.
* *View Session Log* - Displays logs of the streaming session.
* *Delete Download Data* - Deletes download data.
* *Help and Tips* - Displays instructions and support information.
  Cloud Streaming Preview Application Home Screen

When you are ready to begin streaming your application, navigate to [Streaming Applications in Development Environments](testing-streaming-compatability.html "This topic describes the procedure for streaming applications on cloud streaming servers in development environments, including features, options, and settings that are available during streaming.").

# Streaming Applications in Development Environments

This topic describes the procedure for streaming applications on cloud streaming servers in development environments, including features, options, and settings that are available during streaming.

Note: Before you begin streaming, ensure that you've reviewed [Prerequisites](before-you-begin.html#psn-cloud-streaming-guide_0__psn-cloud-streaming-guide_0_0_1) and [Compatibility Requirements for Streaming PlayStation®5 Applications on SIE Cloud Streaming Servers](getting-started-with-streaming.html#psn-cloud-streaming-guide_1_1__psn-cloud-streaming-guide_1_1_1).

Note: When using the Cloud Streaming Preview application via Remote Viewer, ensure that you set the [desired video resolution](https://game.develop.playstation.net/resources/documents/SDK/latest/Remote_Viewer-Users_Guide/stream.html) to lower than 1440p.

To stream your game on cloud streaming servers, do the following:

1. Upload your application package (PSGD) and any additional content packages (PSAC) to the Package/Disc Management Tool (GEMS).
2. From GEMS, deploy the package to the cloud streaming server in the development environment. See [Package/Disc Management Tool (GEMS) Overview - Manage Cloud Streaming](../Package_Disc_Management_Tool_GEMS-Overview/streaming-management.html) for more information.
3. In the [Development Accounts tool](https://tools.partners.playstation.net/accntls/app/amt/), configure **Title Dev/Admin** roles for the accounts in the PlayStation™Network development environment. See [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html) for more information on configuring development accounts.
4. From your DevKit or TestKit, select **Cloud Streaming Preview**.
5. Select the title you want to stream from **Recent titles** or **View All Titles**.
6. Click **Stream**.

## Selecting Titles in the Cloud Streaming Preview Application

When selecting a title to stream, the Cloud Streaming Preview application provides two viewing options with different display logic:

**Recent titles**

*Recent titles* displays the currently selected title and recently deployed titles, up to a maximum of five. Each title is displayed in the format: `titleId` (`contentVersion`) - `titleName`. Only one entry per `titleId` and `contentVersion` is displayed. Deploying a new package that has the same `titleId` and the same `contentVersion` overwrites the previous entry. See [Param.json File Specification - Param File (param.json) Specifications - Parameter Definitions for Applications](../Param_Json-Specification/parameter-definitions-for-applications.html) for information and definitions of parameters such as `titleId` and `contentVersion`.

Recent Titles

**View All Titles**

*View All Titles* displays all titles accessible to the logged in account. You can input keywords in the search menu to filter by the `titleId`, `contentVersion`, or `titleName`. The selected title then appears at the top of *Recent titles*.

View All Titles

## Features Available While Streaming

After you begin a streaming session, the features listed below are available for you to use:

**Features Available in the Action Card**

During cloud streaming, you can display the *Action Card* by pressing the **PS button**. You can then select the following options:

* *Close Game* - Closes the cloud streaming session.
* *Resume Game* - Resumes the cloud streaming session.
* *Max Resolution* - Change the maximum resolution during streaming.
* *Troubleshoot > Test Connection* - Allows you to check the quality of your game streaming experience, displaying values such as, latency, jitter, download speed, and upload speed.
* *Troubleshoot > Restore License* - Restores the license saved on the cloud streaming server for the active title. This option does not restore the license saved locally. To return purchased products to a non-purchased state, [invalidate the purchase history using the Development Accounts tool](https://tools.partners.playstation.net/accntls/) before selecting this option.

**Log Overlay**

Activate the log overlay by pressing the **Touch Pad button** and the **R2 button** simultaneously. Move the overlay to the right side or the left side of the screen by pressing the **Touch Pad button** and **L2 button** simultaneously.

The log overlay provides insight into various network telemetry data, such as upstream and downstream bandwidth, resolutions, loss etc.

## Viewing the Session Log

From the Cloud Streaming Preview application's home screen, select **View Session Log** to view the history of previous cloud streaming sessions, including the *Date* of the session, the *Title ID*, *Content ID*, *Session ID*, and *Online ID*.

## Viewing the Help and Tips Screen

From the Cloud Streaming Preview application's home screen, select **Help and Tips** to view support information you may find useful when testing cloud streaming. For exmaple:

## Handling Save Data During Cloud Streaming

You can sync and transfer save data between the cloud streaming server and DevKit or TestKit. For more information, see [SaveData Library Overview - Handling of Save Data during Development - Handling of Save Data During Cloud Streaming](../SaveData-Overview/handling-of-save-data-during-cloud-streaming.html).

# Debug Settings Available During Streaming

This topic provides information on the debug settings available to you while streaming your applications in development environments.

The following debug settings are reflected in cloud streaming servers:

* System - TRC Check Notifications
* Game - SaveData - Debug Notification
* Game - SaveData - Fake Owner
* Game - Enable Low Energy Mode
* PlayStation™Network - In-Game Commerce Debug
* PlayStation™Network - Require purchased license

You must configure these settings before streaming, as they can't be changed during streaming.

Access these options from **★Debug Settings Menu**.

## System - TRC Check Notifications

Use this setting in the same way as local gaming environments. For more information, see [Technical Requirements Checklist for PlayStation®5 - Test Case Overview](../../../TRC/latest/TRC/Test-Case-Overview.html).

## Game - SaveData - Debug Notification

Use this setting in the same way as local gaming environments. For more information, see [SaveData Library Overview - Handling of Save Data during Development - Displaying Notifications for Developers](../SaveData-Overview/displaying-notifications-for-developers.html).

## Game - SaveData - Fake Owner

Use this setting in the same way as local gaming environments. For more information, see [SaveData Library Overview - Handling of Save Data during Development - Transferring Save Data between Systems](../SaveData-Overview/transferring-save-data-between-systems.html).

## Game - Enable Low Energy Mode

Use this setting in the same way as with local gaming environments. For more information, see [Hardware Overview - Hardware Overview for PlayStation®5 - Summary of PlayStation®5 Hardware Types and Operation Modes](../Hardware-Overview/summary-of-ps5-hardware-types-and-operation-modes.html).

## PlayStation Network - In-Game Commerce Debug

Use this setting in the same way as local gaming environments. For more information, see [PlayStation™Network Commerce Programming Guide - Development Support Functions - PlayStation™Network - In-Game Commerce Debug](../PSN_Commerce-Programming_Guide/psn-in-game-commerce-debug.html).

## PlayStation Network - Require purchased license

Use this setting in the local console environment to enable or disable entitlements based on the purchase history of the account.

For more information, see [System Software User's Guide (Settings) - Features of the ★Debug Settings Menu - PlayStation Network － Require purchased license](../System_Software-Users_Guide_for_Settings/psn-require-purchased-license.html).

To stream additional content purchased from the Store Preview application, set **Require purchased license** to **Additional Content**. This enables the entitlement license check for additional content.

To stream a development package of additional content, set **Require purchased license** to **Off**. This disables the entitlements based on purchase history of the account and allows you to stream additional content packages that have been deployed to cloud streaming servers even if the user does not have the entitlement in their purchase history.

When streaming with additional content disabled, set **Require purchased license** to **Additional Content** and use an account that does not own any entitlements to delete purchase history using the Dev Admin Tool.

Cloud streaming does not allow you to manage individual entitlements using the *Add Content Manager* debug setting. The *Require purchased license* setting allows you to enable or disable access to development packages for all titles, rather than individual titles. Additionally, streaming uses the development package of the application, so the *Require purchased license* options *All* and *application* are not used.

# Troubleshooting

This topic provides information and resolution steps for issues you may encounter while using the Cloud Streaming Preview application.

If unexpected issues occur when streaming your applications, [file a ticket with DevNet private support](https://game.develop.playstation.net/support). Include the cloud streaming session log information to help troubleshoot the issue.

To find session log information, do the following:

1. From the Cloud Streaming Preview application, select **View Session Log**.
2. Select the session you want to report. The system stores a maximum of 100 session logs per account/device.
3. Take a screenshot of the session log details page which includes the *Date*, *Title ID*, *Session ID* and *Online ID*.
4. Attach the screenshot to the DevNet support ticket.

## The Cloud Streaming Preview Application is Not Available on DevKit or TestKit

Ensure that the latest system software is installed (11.00 or later).

## A Game Package is Not Available in the Cloud Streaming Preview Application

Possible causes for this issue include:

* The package was not deployed from the GEMS tool to the cloud streaming servers or it is still being deployed. To resolve this, check the deployment status on the **Manage Streaming** screen in GEMS. If the package is in the *Deployment Requested* status for more than two hours, verify that the primary package has been deployed or deploy the primary package if it is missing. To verify if the primary package is deployed:
  1. Go to **Admin** > **Manage Streaming** and select the tag link for the package.
  2. Under **Tags of This Shared Binary**, verify if the primary package has been deployed. The tag labeled *(This Tag)* should appear in the same row as the package labeled *(Primary)*. If not, this means the currently selected tag is not the primary package and is not deployed.
  3. If the primary package has not been deployed, deploy it. For more information, see [Package/Disc Management Tool (GEMS) Overview - Manage Cloud Streaming](../Package_Disc_Management_Tool_GEMS-Overview/streaming-management.html).
  4. File a ticket with DevNet private support if the issue persists.
* The package was deployed, but *Title Dev/Admin* roles were not configured for the accounts in the PlayStation™Network development environment. To resolve this, use the [Development Accounts tool](https://tools.partners.playstation.net/accntls/app/amt/) to confirm whether the roles are appropriately configured for the necessary accounts.

## A Connection Error Appears when Attempting to Start a Stream

When the connection is not sufficient to support a stream, you may receive the following error message: "Your internet connection quality might not be sufficient to play streaming games. Try using a wired LAN connection to improve your connection speed and stability".

If you receive this error message, do the following:

1. Verify that the internet connection being used meets the minimum supported download speed (approximately five Mbps).
2. If the internet connection being used is sufficient to support the minimum specification, file a ticket with [DevNet private support](https://game.develop.playstation.net/support).

## The System Software Requires an Update

If you are using an older major version of PUP, you may receive the following error message:

"Your system software needs to be updated to continue. Go to [Settings] > [System] > [System Software] > [System Software Update and Settings]".

If you receive this error message, update your DevKit to the latest PUP.

## Online Services Are not Functioning Properly

If your game's online or network services are not functioning properly during streaming and you have restricted servers, your application may not be allowing the required IP addresses to access the cloud streaming server.

To resolve this, request the latest versions of IP addresses from [DevNet private support](https://game.develop.playstation.net/support) and add them to your server's IP allowlist.

## A Game is Not Streaming in the Desired Resolution

While streaming an application, the video resolution automatically adjusts depending on the quality of your internet connection. Cloud streaming requires a minimum internet speed of five Mbps, 15 Mbps for 1080p, and 38+ Mbps for 4K and HDR.

To adjust the resolution, do the following:

1. While streaming an application, press the **PS button** to display the *Action Card*.
2. Select **Max Resolution**.
3. Restart the stream to apply the new resolution.
4. Press the **Touch Pad button** and **R1 button** simultaneously to display the log overlay and verify the resolution.

## A Notification Indicates that the Internet Connection Quality Isn’t Sufficient for Streaming

This error is most common when there is a disruption in the network connection. When this error appears, it's possible for the network to recover automatically and the error could clear.

If the error does not clear, do the following:

1. Verify the network connection is stable and still at sufficient speed.
2. If the issue persists in a particular scene with a high network speed, file a ticket with [DevNet private support](https://game.develop.playstation.net/support).

## A Different Title Streams Instead of the Selected One

This issue may happen when you attempt to stream a different `contentVersion` of the same title. After streaming one `contentVersion`, you cannot launch the stream of a different `contentVersion`, as the first streaming session is still running in the background.

To resolve this issue, do the following:

1. Press the **PS button** to open the *Action Card*.
2. Select **Close Game**.
3. Restart the stream of the new title.