# NpAuth Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Overview/procedure-for-obtaining-authorization-code-synchronous-proce.html

# Using the NpAuth Library

This topic explains the procedure for obtaining authorization codes for application servers using the NpAuth library. It provides this procedure for two cases, one in which synchronous processing is performed and the other in which asynchronous processing is performed.

# Procedure for Obtaining Authorization Code (Synchronous Processing)

By creating a synchronous processing request, the communication functions will be processed with blocking. Follow the procedure below in such cases.

1. **Create synchronous processing request**

   Create a synchronous processing request. A request must be created per communication process and deleted after the communication process ends.

   ```
   int ret, reqId;

   ret = sceNpAuthCreateRequest ();
   if (ret < 0) {
   	// Error handling
   }
   reqId = ret;
   ```
2. **Issue request**

   Call `sceNpAuthGetAuthorizationCodeV3()`. In the case of a synchronous processing request, this function will perform blocking until the authorization code can be obtained from the server. For the purpose of preventing user operation from being blocked for extensive periods of time, it is recommended that `sceNpAuthAbortRequest()` be used to implement timeouts and user cancellation in the application.

   ```
   // Request
   SceNpAuthGetAuthorizationCodeParameterV3 param;
   SceNpAuthorizationCode authCode;
   int issuerId;

   // userId and clientId assumed to store an appropriate value
   memset(&param, 0, sizeof(param));
   param.size = sizeof(param);
   param.userId = userId;	// Access target user's user ID
   param.clientId = &clientId;	// Client program's client ID
   param.scope = "psn:s2s openid id_token:psn.basic_claims"; 	// Entitlement scope for obtaining authorization codes

   ret = sceNpAuthGetAuthorizationCodeV3 (
   	reqId,	// Request ID
   	&param,	// Authorization code obtainment parameters
   	&authCode,	// Stores the obtained authorization code
   	&issuerId	// Stores the obtained issuer ID
   	);
   if (ret < 0) {
   	// Error handling
   }
   ....
   ```
3. **Delete request**

   When the request ends, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpAuthDeleteRequest (reqId);
   ```

# Procedure for Obtaining Authorization Code (Asynchronous Processing)

By creating an asynchronous processing request, the communication functions will be non-block processed. Follow the procedure below when using the asynchronous function.

1. **Create asynchronous processing request**

   Create an asynchronous processing request using `sceNpAuthCreateAsyncRequest()`. A request must be created per communication process and deleted after the communication process ends.

   ```
   int ret, reqId;
   SceNpAuthCreateAsyncRequestParameter param;

   memset(&param, 0, sizeof(param));
   param.size = sizeof(param);

   ret = sceNpAuthCreateAsyncRequest (&param);
   if (ret < 0) {
   	// Error handling
   }
   reqId = ret;
   ```
2. **Issue request**

   Call `sceNpAuthGetAuthorizationCodeV3()`. When an asynchronous request is passed as an argument, this function will be non-block processed, and it will return immediately (without waiting until the user information can be obtained from the server) after the request starts.

   ```
   // Request
   ret = sceNpAuthGetAuthorizationCodeV3 (
   	reqId,	// Request ID
   	&param,	// Authorization code obtainment parameters
   	&authCode,	// Stores the obtained authorization code
   	&issuerId	// Stores the obtained issuer ID
   	);
   if (ret < 0) {
   	// Error handling
   }
   ....
   ```
3. **Wait for communication function to complete**

   To confirm the completion of the request, call either `sceNpAuthWaitAsync()` or `sceNpAuthPollAsync()`. `sceNpAuthWaitAsync()` will wait until the request ends if it has not yet ended. Meanwhile, `sceNpAuthPollAsync()` will immediately return 1 (`SCE_NP_AUTH_POLL_ASYNC_RET_RUNNING`) for the return value. The request will complete when one of these functions returns 0 and the application receives the result of the communication processing.

   For the purpose of preventing user operation from being blocked for extensive periods of time, it is recommended that `sceNpAuthAbortRequest()` be used to implement timeouts and user cancellation in the application.
4. **Delete request**

   When the request ends, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpAuthDeleteRequest (reqId);
   ```

## About Asynchronous Processing Internal Threads

When an asynchronous processing request is created and communication functions are executed, an internal thread will be generated. The internal thread will be terminated when the communication processing ends.

When multiple asynchronous processing requests are executed at the same time, note that the same number of internal threads as the number of requests will be generated.