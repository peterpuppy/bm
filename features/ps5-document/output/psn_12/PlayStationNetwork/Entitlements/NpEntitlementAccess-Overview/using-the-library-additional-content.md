# NpEntitlementAccess Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Overview/using-the-library-additional-content.html

# Using the Library: Additional Content

This topic describes how to use the NpEntitlementAccess library to handle additional content. Also provided are how to use entitlement keys that have been added to additional content and an explanation of testing features.

# Additional Content Identifiers

For identifying additional content in the NpEntitlementAccess library, specify the "NP service label" and the "unified entitlement label". Refer to [AppContent Library Overview - Using the Library: Additional Content - Additional Content Identifiers](../AppContent-Overview/additional-content-identifiers.html) for details.

# Accessing Additional Content

Whether or not an entitlement is valid for additional content can be checked using an NpEntitlementAccess library function.

Initialize the library using `sceNpEntitlementAccessInitialize()` as explained in "[Procedure to Initialize the NpEntitlementAccess Library](procedure-for-initializing-the-library.html)" for accessing additional content.

## Obtaining a List of Additional Content and Checking Entitlement Validity

Use `sceNpEntitlementAccessGetAddcontEntitlementInfoList()` to obtain a list of additional content for which the entitlement is valid or, in other words, additional content that can be accessed by the application. The list is obtained as an array of `SceNpEntitlementAccessAddcontEntitlementInfo` structures. In an application that supports a large number of additional content, the following sequence of actions is recommended. First, obtain the number of additional content. Then, after preparing the corresponding number of buffers, obtain the list.

```
/* Obtain the number of additional content information for which the entitlement is valid */
SceNpServiceLabel serviceLabel = 0;
SceNpEntitlementAccessAddcontEntitlementInfo *list = NULL; // If NULL is specified, only the number can be obtained
uint32_t listNum = 0;
uint32_t hitNum;
ret = sceNpEntitlementAccessGetAddcontEntitlementInfoList(serviceLabel, list, listNum, &hitNum);

/* Prepare the required buffers */
list = (SceNpEntitlementAccessAddcontEntitlementInfo *)malloc(sizeof(SceNpEntitlementAccessAddcontEntitlementInfo) * hitNum);
listNum = hitNum;

/* Obtain a list of additional content information for which the entitlement is valid */
ret = sceNpEntitlementAccessGetAddcontEntitlementInfoList(serviceLabel, list, listNum, &hitNum);
```

Note:

* The maximum number of additional content that can be obtained with `sceNpEntitlementAccessGetAddcontEntitlementInfoList()` is 2499. It is possible to support an even higher number of additional content by using multiple NP service labels, but the NP service labels that can be used are from 0 to 7 (for a total of 8); therefore, the maximum number of additional content that a single application can support is 19992.
* If an NP service label other than 0 is specified in the development environment, you must be signed in to PlayStation™Network in a state where network connection is possible upon application start.
* If an NP service label other than 0 exists in addition to an application that corresponds to that NP service label, that application's entitlement label will also be included in the list.

## Directly Checking the Validity of an Entitlement for Additional Content

An application with a limited number of supported additional content, for example, an application that only supports one additional content, can use `sceNpEntitlementAccessGetAddcontEntitlementInfo()` to directly specify the unified entitlement label and check the validity of the entitlement without obtaining a list.

```
SceNpServiceLabel serviceLabel = 0;
SceNpUnifiedEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "0000111122223333", SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE);
SceNpEntitlementAccessAddcontEntitlementInfo info;

/* Directly obtain additional content information for which the entitlement is valid */
ret = sceNpEntitlementAccessGetAddcontEntitlementInfo(serviceLabel, &entitlementLabel, &info);
if(ret != SCE_OK){
    // Error handling
}
```

Note:

`sceNpEntitlementAccessGetAddcontEntitlementInfoList()` or `sceNpEntitlementAccessGetAddcontEntitlementInfo()`must always be used to check whether or not an additional content entitlement is valid. (Do not use information saved to non-volatile storage such as save data to check.) With the DRM in PlayStation®5, additional content entitlements may become invalid again after becoming valid. TRC [R5116](../../../TRC/latest/TRC/R5116.html) requires that applications must appropriately restrict access to the corresponding additional content even in such cases. However, there is a possibility that this will be difficult depending on the specifications of the additional content; therefore, thorough consideration is recommended at early stages of game/specification design.

# Entitlement Information Update Events for Additional Content

Entitlements to access additional content may be added/removed while an application is running for reasons such as the following:

* The user logged in or logged out
* An entitlement was purchased from the PlayStation™Store
* Additional content without extra data was installed
* The period of validity finished

An application will be notified of an update to entitlement information through an event (`SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE`) by the SystemService library; you can thus recheck entitlements by receiving such events.

When an entitlement is added/removed, it is not necessary to change the behavior of the application immediately; before attempting to use additional content following the procedures given in the "[Accessing Additional Content](accessing-additional-content.html)" section (e.g., when the application has been launched), it is mandatory to check entitlements to choose the appropriate behavior. However, whether to use the event described in the preceding paragraph to change application behavior is a matter for which you should consider how gameplay would be affected and then adopt the right specification for your application. The system will not, for instance, restrict access to additional content on its own when an entitlement has been removed.

A notification of an entitlement information update event is also issued when `sceAppContentInitialize()` is called.

Note:

The AppContent library must be initialized to receive this event.

During the development stage, you can use "★Debug Settings" > "Game" > "Package Installer" or "Add Content Manager" to make it so that there will be notifications for entitlement information update events. For details, refer to the "[Development Support Features for Additional Content](development-support-features-for-additional-content.html)" section.

# Usage of an Entitlement Key

It is possible to add an entitlement key to additional content.

An entitlement key can be obtained with `sceNpEntitlementAccessGetEntitlementKey()` only when a user owns the entitlement to use the additional content. Therefore, it can be used as restricted data linked to the additional content. Refer to the "Additional Content Packages" section of [Publishing Tools Overview - Package - Package Types](../Publishing_Tools-Overview/package-types.html) for details about entitlement keys.

# Development Support Features for Additional Content

## Local Testing

In order to perform local testing of applications that use additional content, use "Package Installer" or "★Debug Settings" > "Game" > "Add Content Manager".

With "Package Installer", additional content packages can be installed locally. For details, refer to [System Software User's Guide (Application Development Support) - Development Support Features by Application - Package Installation Feature](../System_Software-Users_Guide_for_Development_Support/package-installation-feature.html).

It is possible to perform the following operations for installed additional content with "Add Content Manager".

* Displaying a list of installed additional content
* Individually disabling/enabling entitlements for additional content by selecting additional content from the list.

  Additional content for which the entitlement has been disabled is displayed with a strikethrough and will no longer be included in the list obtained from `sceNpEntitlementAccessGetAddcontEntitlementInfoList()`. In addition, `sceNpEntitlementAccessGetAddcontEntitlementInfo()` will return the `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NO_ENTITLEMENT` error. Use this feature to test error handling when the entitlement for additional content has been removed.
* Individually deleting additional content entitlements

Note:

The "Manage Game Content" screen in the system software (the screen that appears when you focus on the application icon and press the options button) allows you to remove installed additional content. However, this feature is intended only for end users. It is not appropriate for operations required by developers, such as deleting or enabling/disabling additional content entitlements. Use the "Add Content Manager" mentioned above for testing during development.

The processing to be performed by the application with respect to additional content is prescribed in TRC [R5116](../../../TRC/latest/TRC/R5116.html). The test procedure is also shown in R5116 Test Case for reference.

## Testing in the Development Environment

In order to perform testing of applications that use additional content in the development environment, set "★Debug Settings" > "PlayStation Network" > "Require purchased license" to "Additional Contents". The "Add Content Manager" settings will be ignored and entitlements will be valid/invalid according to the purchase history in the development environment.

To return purchased products to unpurchased states, use the DevAdmin Tool to invalidate the purchase history in the development environment. (Refer to [DevAdmin Tool User's Guide - Using the DevAdmin Tool - Clearing Entitlements](../DevAdmin_Tool-Users_Guide/clearing-entitlements.html) for operation details.) After that, perform "Restore" at "Settings" > "Users and Accounts" > "Other" > "Restore Licenses". Entitlements may not return to the unpurchased state if this is not carried out.