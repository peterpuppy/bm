# NpEntitlementAccess Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Overview/using-the-library-consuming-entitlements.html

# Using the Library: Consuming Entitlements

This topic describes how to use the NpEntitlementAccess library to handle consumable entitlements.

The package type of consumable entitlements that can be used by applications is "PSCONS". (For details about package types, refer to [Entitlements Overview - Entitlements Web API Overview - Entitlement Types](../../../WebAPI/latest/Entitlements-Overview/entitlement-types.html).) However, because of how the server operates, service entitlements cannot be used with PlayStation®5-format applications alone. Only service entitlements that are used by a PlayStation®4-format application, that have been set up for PSSDC, and that are meant to be shared across platforms can be used with PlayStation®5.

Entitlements can be consumed by using the NpEntitlementAccess library to communicate with the PlayStation™Network server.

Precautions for use are similar to when using the library with a game server. Refer to [Entitlements Overview - Handling Consumable Entitlements](../../../WebAPI/latest/Entitlements-Overview/handling-consumable-entitlements.html).

# Procedure for Consuming an Entitlement

Before you can consume entitlements, you must initialize the library with `sceNpEntitlementAccessInitialize()`, as described in "[Procedure to Initialize the NpEntitlementAccess Library](procedure-for-initializing-the-library.html)".

The communication function for consuming entitlements is non-blocking. The procedure to consume an entitlement is as follows:

1. **Generate a transaction ID**

   A transaction ID is required to consume an entitlement. Generate a transaction ID using `sceNpEntitlementAccessGenerateTransactionId()`. Specify this transaction ID again upon a network error to guarantee idempotence. Refer to "Ensuring Resiliency" in [Entitlements Overview - Handling Consumable Entitlements - Procedure for Consuming Entitlements](../../../WebAPI/latest/Entitlements-Overview/procedure-for-consuming-entitlements.html) for details about idempotence.

   ```
   // Generate a transaction ID
   ret = sceNpEntitlementAccessGenerateTransactionId(
       &transactionId // Destination to store the generated transaction ID
   );
   if (ret < 0) {
       // Error handling
   }
   ....
   ```
2. **Create and execute a request**

   Create a communication request to consume an entitlement and execute it using `sceNpEntitlementAccessRequestConsumeUnifiedEntitlement()` or `sceNpEntitlementAccessRequestConsumeServiceEntitlement(()`. These functions are non-blocking and will return after starting the request without waiting for user information to be obtained from the server.

   ```
   // Request
   ret = sceNpEntitlementAccessRequestConsumeUnifiedEntitlement(
       userId,            // User ID of the access-target user
       serviceLabel,       // NP service label of the target entitlement
       &entitlementLabel, // Unified entitlement label of the target entitlement
       &transactionId,    // generated transaction ID
       useCount,          // Number of entitlement counts to consume
       &requestId         // The ID of the created list will be stored
       );
   if (ret < 0) {
       // Error handling
   }
   ....
   ```
3. **Wait for the communication function to complete**

   Call `sceNpEntitlementAccessPollConsumeEntitlement()` to check for request completion. If the request has not completed, `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned. The request will conclude when the function returns `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` and the application receives the results of the communication processing.

   ```
   // Confirm that the communication function completed
   int32_t useLimit;
   int32_t amountConsumed;
   int32_t result;
   ret = sceNpEntitlementAccessPollConsumeEntitlement(requestId, &result, &useLimit, &amountConsumed);
   if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING) {
       // Check for completion again after some time passes
   } else if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED) {
       // Use the results of the completed communication stored in result and useLimit
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
4. **Delete the request**

   When the request completes, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpEntitlementAccessDeleteRequest(requestId);
   ```

## Communication Processing

Communication processing will be carried out in the background by the system.

Note that the `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` error will be returned when multiple requests are executed at the same time.