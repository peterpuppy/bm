# Np Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Overview/communication-procedure-synchronous-processing.html

# Using the Library

# Basic Procedure

1. **NP Title ID/NP Title Secret settings and nptitle.dat file placement**

   An NP Title ID, NP Title Secret, and nptitle.dat file will be issued for each application by making a request on the PlayStation®5 Developer Network. Call `sceNpSetNpTitleId()` to set the issued NP Title ID and NP Title Secret. The NP Title ID and NP Title Secret set with `sceNpSetNpTitleId()` will be valid only in a Development Kit with its Release Check Mode set to Development Mode. In Release Mode or Assist Mode, the `sceNpSetNpTitleId()` settings will be ignored, and the NP Title ID/NP Title Secret stored in the nptitle.dat file will be used. Place the nptitle.dat file appropriately according to the application boot method.

   * Booting from a game package or workspace

     Place nptitle.dat in the same directory as the application parameter file (param.json). For game package creation, booting from workspace, and parameter file placement directories, refer to the [Application Content Overview](../Application_Content-Overview/__document_toc.html) and [System Software User's Guide (Application Development Support)](../System_Software-Users_Guide_for_Development_Support/__document_toc.html) documents.
   * Booting in debugging mode

     Create a sce\_sys directory below the Visual Studio working directory, and place nptitle.dat in it.

   If the 0x82200284 or 0x82200182 error code is returned as an execution result of an Np library function or PlayStation™Network Web API call, it indicates that an invalid NP Title ID/NP Title Secret has been set. Check the set NP Title ID/NP Title Secret.

   If you place an nptitle.dat file in its directory, you must then place a parameter file in the proper location. If the parameter file is missing, the error code 0x8055001C will be returned by libraries that use the PlayStation™Network. Additionally, if the Title ID included in the parameter file does not match what is in nptitle.dat, the error code 0x8055001B will be returned. If either error is returned, confirm that you are using the appropriate files.

   Note that when using `sceNpSetNpTitleId()` in development mode, it is not a requirement to place a parameter file anywhere; if a parameter file is present and there is a mismatch between the Title IDs, the error code 0x8055001B will be returned.

   Note:

   The NP Title Secret and nptitle.dat file are secret information for verifying an NP Title ID owner. Take sufficient precautions so that they are not leaked to third parties. For example, ensure that these are removed when disclosing the source code/application package for support purposes on the PlayStation®5 Developer Network.
2. **Poll [sceNpCheckCallback()](../Np-Reference/sce-np-check-callback.html)**

   While using the Np library and some functionality (of a library related to PlayStation™Network), call `sceNpCheckCallback()` regularly. `sceNpCheckCallback()` detects events generated for event handlers registered to each library and calls the applicable event handler.

   Note:

   Note that some libraries related to PlayStation™Network may use their own callback check functions to check for callbacks.

# Communication Procedure (Synchronous Processing)

The Np library provides both a synchronous version and an asynchronous version of the function that performs communication with servers. Follow the procedure below when using the synchronous function.

1. **Create synchronous processing request**

   Create a synchronous processing request using `sceNpCreateRequest()`. A request must be created for each communication process and deleted after the communication process ends.

   ```
   int ret, reqId;

   ret = sceNpCreateRequest ();
   if (ret < 0) {
   	// Error handling
   }
   reqId = ret;
   ```
2. **Communication processing**

   Call the communication processing function. In the case of a synchronous processing request, this function will perform blocking until the result is obtained from the server. In order to prevent user operations from being blocked over long periods of time, it is recommended to use `sceNpAbortRequest()` to implement timeouts and allow users to cancel in the application.
3. **Delete request**

   When the request ends, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpDeleteRequest (reqId);
   ```

# Communication Procedure (Asynchronous Processing)

By creating an asynchronous processing request, the communication functions will be non-block processed.

Follow the procedure below when using the asynchronous function.

1. **Create asynchronous processing request**

   Create an asynchronous processing request using `sceNpCreateAsyncRequest()`. A request must be created for each communication process and deleted after the communication process ends.

   ```
   int ret, reqId;
   SceNpCreateAsyncRequestParameter param;

   memset(&param, 0, sizeof(param));
   param.size = sizeof(param);

   ret = sceNpCreateAsyncRequest (&param);
   if (ret < 0) {
   	// Error handling
   }
   reqId = ret;
   ```
2. **Communication processing**

   Call the communication processing function. When an asynchronous request is passed as an argument, this function will be non-block processed, and it will return immediately (without waiting until the result can be obtained from the server) after the request starts.
3. **Obtain results**

   Call `sceNpWaitAsync()` or `sceNpPollAsync()`. `sceNpWaitAsync()` will wait until the request ends if it has not yet ended. On the other hand, `sceNpPollAsync()` will immediately return `SCE_NP_POLL_ASYNC_RET_RUNNING` if the request has not yet ended. When these functions return `SCE_OK`, the request will end and the communication processing results will be stored in the variable specified with the argument `result`, so make sure the results are appropriately evaluated.

   In addition, in order to prevent user operations from being blocked over long periods of time, it is recommended to use `sceNpAbortRequest()` to implement timeouts and allow users to cancel in the application.
4. **Delete request**

   When the request ends, specify the request ID and delete the request.

   ```
   // Delete the request
   sceNpDeleteRequest (reqId);
   ```

## About Asynchronous Processing Internal Threads

When an asynchronous processing request is created and communication functions are executed, an internal thread will be generated. The internal thread will be terminated when the communication processing ends.

When multiple asynchronous processing requests are executed at the same time, note that the same number of internal threads as the number of requests will be generated.