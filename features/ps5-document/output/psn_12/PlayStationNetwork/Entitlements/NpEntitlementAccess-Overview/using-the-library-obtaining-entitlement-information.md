# NpEntitlementAccess Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Overview/using-the-library-obtaining-entitlement-information.html

# Using the Library: Obtaining Entitlement Information

This topic describes how to use the NpEntitlementAccess library to handle entitlement information.

PlayStation®5-format applications can use the NpEntitlementAccess library to communicate with the PlayStation™Network server to obtain information concerning service entitlements and unified entitlements of the PSCONS, PSVC, and PSSUBS package types.

Notes on usage are the same as for usage via a game server. Refer to [Entitlements Overview - Using the Entitlements Web API](../../../WebAPI/latest/Entitlements-Overview/using-entitlements-web-api.html).

Note that because of how the server operates, service entitlements cannot be used with PlayStation®5-format applications alone. Only service entitlements that are used by a PlayStation®4-format application, that have been set up for PSSDC, and that are meant to be shared across platforms can be used with PlayStation®5.

Note:

Contact SIE via "Post a new issue" (<https://game.develop.playstation.net/support/>) of Private Support regarding how to register PSCONS, PSVC, and PSSUBS package type entitlements in the development environment.

# Procedure for Obtaining Entitlement Information

Initialize the library using `sceNpEntitlementAccessInitialize()` as explained in "[Procedure to Initialize the NpEntitlementAccess Library](procedure-for-initializing-the-library.html)" to obtain entitlement information.

The communication function for obtaining entitlement information is non-blocking. The procedure for obtaining entitlement information is as follows:

1. **Create and execute a request**

   Create a request to obtain entitlement information and execute it using `sceNpEntitlementAccessRequestUnifiedEntitlementInfo()` or `sceNpEntitlementAccessRequestServiceEntitlementInfo()`. These functions are non-blocking and will return after starting the request without waiting for user information to be obtained from the server.

   ```
   // Request
   ret = sceNpEntitlementAccessRequestUnifiedEntitlementInfo(
       userId,            // User ID of the access-target user
       serviceLabel,      // NP service label of the target entitlement
       &entitlementLabel, // Unified entitlement label of the target entitlement
       &requestId         // The ID of the created list will be stored
       );
   if (ret < 0) {
       // Error handling
   }
   ....
   ```
2. **Wait for the communication function to complete**

   Call `sceNpEntitlementAccessPollUnifiedEntitlementInfo()` or `sceNpEntitlementAccessPollServiceEntitlementInfo()` to check for request completion. If the request has not completed, `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned. The request will conclude when these functions return `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` and the application receives the results of the communication processing.

   ```
   // Confirm that the communication function completed
   SceNpEntitlementAccessUnifiedEntitlementInfo info;
   int32_t result;
   ret = sceNpEntitlementAccessPollUnifiedEntitlementInfo(requestId, &result, &info);
   if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING) {
       // Check for completion again after some time passes
   } else if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED) {
       // Use the results of the completed communication stored in result and info
   } else {
       // Error handling
   }
   ....
   ```

   For the purpose of preventing user operation from being blocked for extensive periods of time, it is recommended to use `sceNpEntitlementAccessAbortRequest()` and implement timeouts and user cancellation in the application.

   ```
   // Abort the request
   sceNpEntitlementAccessAbortRequest(requestId);
   ```
3. **Delete the request**

   When the request completes, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpEntitlementAccessDeleteRequest(requestId);
   ```

## Communication Processing

Communication processing will be carried out in the background by the system.

Note that the `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` error will be returned when multiple requests are executed at the same time.

# Procedure for Obtaining a List of Entitlement Information

The communication functions for obtaining lists of entitlement information are non-blocking. The procedure for obtaining such lists of information is as follows:

1. **Create and execute a request**

   Create and execute a request to obtain a list of entitlement information using `sceNpEntitlementAccessRequestUnifiedEntitlementInfoList()` or `sceNpEntitlementAccessRequestServiceEntitlementInfoList()`. These functions are non-blocking and will return after starting the request without waiting for user information to be obtained from the server.

   ```
   // Request
   ret = sceNpEntitlementAccessRequestUnifiedEntitlementInfoList(
       userId,            // User ID of the access-target user
       serviceLabel,      // NP service label of the target entitlement
       NULL, 		  // List of the unified entitlement labels for the target entitlements. If NULL is specified, a list of all entitlements will be obtained
       0,                 // The number of elements of the above list. Because that value is NULL, specify 0. 
       &param,            // Parameters for obtaining the list of entitlement information
       &requestId         // The ID of the created list will be stored
       );
   if (ret < 0) {
       // Error handling
   }
   ....
   ```
2. **Wait for the communication function to complete**

   Call `sceNpEntitlementAccessPollUnifiedEntitlementInfoList()` or `sceNpEntitlementAccessPollServiceEntitlementInfoList()` to check for request completion. If the request has not completed, `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned. The request will conclude when these functions return `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` and the application receives the results of the communication processing.

   ```
   // Confirm that the communication function completed
   SceNpEntitlementAccessUnifiedEntitlementInfo list[100];
   int32_t result;
   uint32_t hitNum;
   int32_t nextOffset;
   int32_t previousOffset;

   ret = sceNpEntitlementAccessPollUnifiedEntitlementInfoList(requestId, &result, list, 100, &hitNum, &nextOffset, &previousOffset);
   if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING) {
       // Check for completion again after some time passes
   } else if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED) {
       // Use the results of the completed communication stored in result and info
   } else {
       // Error handling
   }
   ....
   ```

   For the purpose of preventing user operation from being blocked for extensive periods of time, it is recommended to use `sceNpEntitlementAccessAbortRequest()` and implement timeouts and user cancellation in the application.

   ```
   // Abort the request
   sceNpEntitlementAccessAbortRequest(requestId);
   ```
3. **Delete the request**

   When the request completes, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpEntitlementAccessDeleteRequest(requestId);
   ```

## Communication Processing

Communication processing will be carried out in the background by the system.

Note that the `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` error will be returned when multiple requests are executed at the same time.

# Entitlement Information Update Events

Information regarding unified entitlements and service entitlements of the PSCONS, PSVC, and PSSUBS package types can be updated while the application is running due to the following reasons.

* The user logged in or logged out
* An entitlement was purchased from the PlayStation™Store
* An entitlement was consumed
* A subscription was updated

The SystemService library will notify the application of these entitlement updates as events (shown below); you can thus recheck entitlements by receiving such events.

* `SCE_SYSTEM_SERVICE_EVENT_UNIFIED_ENTITLEMENT_UPDATE` for unified entitlements of the PSCONS, PSVC, and PSSUBS package types
* `SCE_SYSTEM_SERVICE_EVENT_SERVICE_ENTITLEMENT_UPDATE` for service entitlements

When an entitlement is updated, it is not necessary to change the behavior of the application immediately; before attempting to use unified entitlements and service entitlements of the PSCONS, PSVC, and PSSUBS package types (e.g., when the application has been launched), it is mandatory to check entitlements to choose the appropriate behavior. However, whether to use the event described in the preceding paragraph to change application behavior is a matter for which you should consider how gameplay would be affected and then adopt the right specification for your application.