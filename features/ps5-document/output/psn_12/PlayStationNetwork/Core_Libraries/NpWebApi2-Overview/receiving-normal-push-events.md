# NpWebApi2 Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Overview/receiving-normal-push-events.html

# Using the Library

# Summary of Procedures

## [Initialization/Pre-processing](initialization-pre-processing.html)

1. **[Set the NP Title ID/NP Title Secret](initialization-pre-processing.html#np-web-api2-library-overview_2_2__np-web-api2-library-overview_2_2_1)**
2. **[Initialize the Http2 library](initialization-pre-processing.html#np-web-api2-library-overview_2_2__np-web-api2-library-overview_2_2_2)**
3. **[Initialize the NpWebApi2 library](initialization-pre-processing.html#np-web-api2-library-overview_2_2__np-web-api2-library-overview_2_2_3)**: `sceNpWebApi2Initialize()`
4. **[Create the user contexts](initialization-pre-processing.html#np-web-api2-library-overview_2_2__np-web-api2-library-overview_2_2_4)**: `sceNpWebApi2CreateUserContext()`

## [Web API Execution](web-api-execution.html)

1. **[Prepare request data](web-api-execution.html#np-web-api2-library-overview_2_3__np-web-api2-library-overview_2_3_1)**: `SceNpWebApi2ContentParameter`
2. **[Create a request](web-api-execution.html#np-web-api2-library-overview_2_3__np-web-api2-library-overview_2_3_2)**: `sceNpWebApi2CreateRequest()`
3. **[Send the request and obtain the error code](web-api-execution.html#np-web-api2-library-overview_2_3__np-web-api2-library-overview_2_3_3)**: `sceNpWebApi2SendRequest()`
4. **[Receive response data](web-api-execution.html#np-web-api2-library-overview_2_3__np-web-api2-library-overview_2_3_4)**: `sceNpWebApi2ReadData()`
5. **[Delete request](web-api-execution.html#np-web-api2-library-overview_2_3__np-web-api2-library-overview_2_3_5)**: `sceNpWebApi2DeleteRequest()`

## [Receiving Normal Push Events](receiving-normal-push-events.html)

1. **[Create a Push event filter](receiving-normal-push-events.html#np-web-api2-library-overview_2_4__np-web-api2-library-overview_2_4_1)**: `sceNpWebApi2PushEventCreateFilter()`
2. **[Register Push event callback functions](receiving-normal-push-events.html#np-web-api2-library-overview_2_4__np-web-api2-library-overview_2_4_2)**: `sceNpWebApi2PushEventRegisterCallback()`
3. **[Monitor for Push event notifications](receiving-normal-push-events.html#np-web-api2-library-overview_2_4__np-web-api2-library-overview_2_4_3)**: `sceNpCheckCallback()`
4. **[Processing when it's no longer necessary to receive push events](receiving-normal-push-events.html#np-web-api2-library-overview_2_4__np-web-api2-library-overview_2_4_4)**: `sceNpWebApi2PushEventUnregisterCallback()`, `sceNpWebApi2PushEventDeleteFilter()`

## [Receiving Order-Guaranteed Push Events](receiving-order-guaranteed-push-events.html)

1. **[Create a Push event filter](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_1)**
2. **[Register Push context callback functions](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_2)**: `sceNpWebApi2PushEventRegisterPushContextCallback()`
3. **[Create a Push context](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_3)**: `sceNpWebApi2PushEventCreatePushContext()`
4. **[Record the Push context on the server](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_4)**
5. **[Start Push context callback functions](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_5)**: `sceNpWebApi2PushEventStartPushContextCallback()`
6. **[Monitor for Push event notifications](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_6)**: `sceNpCheckCallback()`
7. **[Processing when it's no longer necessary to receive push events](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_7)**: `sceNpWebApi2PushEventUnregisterPushContextCallback()`, `sceNpWebApi2PushEventDeleteFilter()`

## [Termination/Post-processing](termination-post-processing.html)

1. **[Delete user contexts](termination-post-processing.html#np-web-api2-library-overview_2_6__np-web-api2-library-overview_2_6_1)**: `sceNpWebApi2DeleteUserContext()`
2. **[Terminate the library](termination-post-processing.html#np-web-api2-library-overview_2_6__np-web-api2-library-overview_2_6_2)**: `sceNpWebApi2Terminate()`

# Initialization/Pre-processing

1. **Set the NP Title ID/NP Title Secret**

   Before using the NpWebApi2 library, the NP Title ID/NP Title Secret must be set. For details, refer to [Np Library Overview](../Np-Overview/__document_toc.html) and [Np Library Reference](../Np-Reference/__document_toc.html).
2. **Initialize the Http2 library**

   Initialize the Http2 library. For details, refer to [Http2 Library Overview](../Http2-Overview/__document_toc.html) and [Http2 Library Reference](../Http2-Reference/__document_toc.html). When the Http2 library is properly initialized, a context ID for the Http2 library will be issued.

   Note:

   The NpWebApi2 library doesn't support the Http library. Don't use the NpWebApi2 library in combination with the Http library; always use the Http2 library.
3. **Initialize the NpWebApi2 library**

   Call `sceNpWebApi2Initialize()` to initialize the NpWebApi2 library. Specify the context ID of the Http2 library initialized in the previous step, and specify the memory pool size to be used by the NpWebApi2 library.

   Note:

   The memory pool size required varies depending on the application implementation and Web API execution frequency. Investigate using `sceNpWebApi2GetMemoryPoolStats()` to determine the required size.

   When initialization of the NpWebApi2 library is complete, a library context ID will be issued.

   ```
   #define NP_WEBAPI2_POOL_SIZE ( 64 * 1024 )
   int libHttp2CtxId; // Http2 library context ID

   int32_t ret = 0;
   int32_t libCtxId = 0;

   ret = sceNpWebApi2Initialize(libHttp2CtxId, NP_WEBAPI2_POOL_SIZE);
   if (ret < 0) {
       // Error handling
   }
   libCtxId = ret;
   ```
4. **Create the user contexts**

   Create a user context for each user calling a Web API. To create a user context, execute `sceNpWebApi2CreateUserContext()` with the library context ID and the user ID of the user calling the Web API specified.

   When the user context is properly created, the user context ID will be issued.

   ```
   int32_t libCtxId;         // Library context ID
   SceUserServiceUserId userId; // User ID of the user calling the Web API

   int32_t ret = 0;
   int32_t userCtxId = 0;

   ret = sceNpWebApi2CreateUserContext(libCtxId, userId);
   if (ret < 0) {
       // Error handling
   }
   userCtxId = ret;
   ```

# Web API Execution

1. **Prepare request data**

   When sending request data to the server upon Web API execution, store the request data in memory in advance. In addition, the content parameters represented with the `SceNpWebApi2ContentParameter` structure must be prepared.

   The content parameters are comprised of Content-Length which represents the request data size and Content-Type which represents the request data type. These are set in the NpWebApi2 library as the Content-Length and Content-Type values in the HTTP request header.

   For example, in many Web APIs, request data is defined in JSON format with UTF-8 encoded character strings, therefore Content-Type is specified as "`application/json; charset=utf-8`". In the NpWebApi2 library, this character string is defined as the macro `SCE_NP_WEBAPI2_CONTENT_TYPE_APPLICATION_JSON_UTF8`, therefore applications can use this macro as the Content-Type value.
2. **Create a request**

   To execute Web APIs, a request must be created and sent every time a Web API is executed. First, specify the following parameters for creating a request then execute `sceNpWebApi2CreateRequest()`. When the request has been properly created, a request ID will be issued.

   * User context ID

     Specify the user context ID issued with `sceNpWebApi2CreateUserContext()`.
   * API group

     The Web APIs are divided into a number of API groups according to their features. Specify the character string that represents the API group where the Web API you want to execute belongs to. For details on API groups, refer to [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html).
   * Path

     Specify the path of the Web API you want to execute. The path is a character string that links the resource path and query string.
   * HTTP method

     Specify the constant that represents the HTTP method when executing the Web API.
   * Content parameters

     If sending request data to the server when executing the Web API, specify the content parameters prepared in step [(1)](web-api-execution.html#np-web-api2-library-overview_2_3__np-web-api2-library-overview_2_3_1).

   ```
   // Character string that represents the API group of the User Profile Web API
   #define API_GROUP "userProfile"

   // Path of the Web API to execute (resource path and query string)
   #define PATH "/v1/users/1234567890123456789/friends"

   // User context ID
   int32_t userCtxId;

   int32_t ret = 0;
   int64_t requestId = 0;

   // Create request for obtaining friends list
   ret = sceNpWebApi2CreateRequest(
       userCtxId,
       API_GROUP,
       PATH,
       SCE_NP_WEBAPI2_HTTP_METHOD_GET,
       NULL, // Specify NULL if not sending request data
       &requestId
   );
   if (ret < 0) {
       // Error handling
   }
   ```
3. **Send the request and obtain the error code**

   Execute `sceNpWebApi2SendRequest()` to send the created request to the server. If sending request data to the server, specify the buffer and size of the data to send. If the total size of the request data to send is large, the request data can be partitioned then sent by calling this function multiple times.

   Note:

   `sceNpWebApi2SendRequest()` is a blocking function. For the timing when this function returns, refer to the description of `sceNpWebApi2SendRequest()` in the [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html) document.

   Note:

   NpWebApi2 requests do not have a defined timeout and will time out at an undefined time in the event of an upstream network failure.

   If you need to monitor the communication processing time, specify the timeout value with `sceNpWebApi2SetRequestTimeout()` before calling `sceNpWebApi2SendRequest()`, and call `sceNpWebApi2CheckTimeout()` at regular intervals. It is possible to make communication processing time out based on an arbitrary timeout value defined by the application. For details, refer to the "Timeout" chapter of the [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html) document.

   ```
   int64_t requestId; // Request ID of the request to send

   int32_t ret = 0;

   ret = sceNpWebApi2SendRequest(
       requestId,
       NULL,  // Specify NULL if not sending request data
       0,     // Specify 0 if not sending request data
       NULL   // Specify NULL if not obtaining response information upon server error
   );
   if (ret < 0) {
       // Error handling
   }
   ```

   When sending a request and a server error has occurred as a result of executing the Web APIs, `sceNpWebApi2SendRequest()` will internally receive the response data, an error code that represents the server error will be generated from the error object included in the response data, and will return with the error code as the return value. The upper 8 bits of this error code are 0x82 and the lower 24 bits are the server error code represented by a decimal integer.

   Note:

   When a pointer to an `SceNpWebApi2ResponseInformationOption` structure is specified for the 4th argument in `sceNpWebApi2SendRequest()`, it will be possible to obtain the response data upon server error. Use this for when investigating the details of a server error during development, etc.
4. **Receive response data**

   When the request sending is complete and `sceNpWebApi2SendRequest()` is successful, it will be possible to use `sceNpWebApi2ReadData()` to receive the response data.

   Note:

   `sceNpWebApi2ReadData()` is a blocking function. For details on the timing when this function returns, refer to the description of `sceNpWebApi2ReadData()` in the [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html) document.

   If the request succeeds and the executed Web API is of the kind that returns response data, read the response data and process it.

   ```
   int64_t requestId; // Request ID of the sent request

   int32_t ret = 0;

   char buf[BUFFER_SIZE];

   ret = sceNpWebApi2ReadData(requestId, buf, sizeof(buf)-1);
   if (ret < 0) {
       // Error handling
   }
   ```

   For details on HTTP status codes, response data, and server error codes regarding Web APIs, refer to the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document and each Web API reference document.
5. **Delete request**

   When the request sending/receiving is complete, execute `sceNpWebApi2DeleteRequest()` to delete the request.

   ```
   int64_t requestId; // Request ID of request to delete

   int32_t ret = 0;

   if (requestId > 0) {
       ret = sceNpWebApi2DeleteRequest(requestId);
       if (ret < 0) {
           // Error handling
       }
   }
   ```

# Receiving Normal Push Events

1. **Create a Push event filter**

   To create a push event filter, execute `sceNpWebApi2PushEventCreateFilter()` and specify the data type, NP service name, and extended data key of the Push events you intend to receive. Note that this function is a blocking function in accordance with network access. When a Push event filter is created, a filter ID will be issued.

   Note:

   It is not guaranteed that Push events will reach the receiver. In addition, the arrival order may be different; consider this when designing your application so that Push events are appropriately handled. Some Web APIs provide Push events with guaranteed order by taking advantage of the Push context scheme. For details on how these are received, refer to the "[Receiving Order-Guaranteed Push Events](receiving-order-guaranteed-push-events.html)" section.

   The following is an example of code for creating a Push event filter without specifying an NP service name.

   ```
   int32_t ret = 0;
   int32_t libCtxId;
   int32_t handleId = 0;
   int32_t filterId = 0;

   SceNpWebApi2PushEventFilterParameter filterParam[2];
   SceNpWebApi2PushEventDataType dataType[2];
   SceNpWebApi2PushEventExtdDataKey extdDataKey;

   // Data types to receive
   memset(dataType, 0, sizeof(dataType));
   snprintf(dataType[0].val, SCE_NP_WEBAPI2_PUSH_EVENT_DATA_TYPE_LEN_MAX,
   	"np:service:friendlist:friend"); // In case of a friend-update event
   snprintf(dataType[1].val, SCE_NP_WEBAPI2_PUSH_EVENT_DATA_TYPE_LEN_MAX,
   	"xx:xxxxxxx:xxxxxxxxxx:xxxxxx"); // Multiple specifications allowed

   // Extended data key to receive
   memset(extdDataKey, 0, sizeof(extdDataKey));
   snprintf(extdDataKey.val,
   	SCE_NP_WEBAPI2_PUSH_EVENT_EXTD_DATA_KEY_LEN_MAX, "trigger");

   // Push event filter parameters
   memset(filterParam, 0, sizeof(filterParam));	
   memcpy(&filterParam[0].dataType, &dataType[0],
   	sizeof(SceNpWebApi2PushEventDataType));
   filterParam[0].pExtdDataKey = NULL;
   filterParam[0].extdDataKeyNum = 0;
   memcpy(&filterParam[1].dataType, &dataType[1],
   	sizeof(SceNpWebApi2PushEventDataType));
   filterParam[1].pExtdDataKey = &extdDataKey;
   filterParam[1].extdDataKeyNum = 1;

   // Create handle
   ret = sceNpWebApi2PushEventCreateHandle(libCtxId);
   if(ret < 0){
   	// Error handling
   }
   handleId = ret;

   // Create Push event filter. Note that this is a blocking function. 
   ret = sceNpWebApi2PushEventCreateFilter(
   	libCtxId, handleId,
   	SCE_NP_WEBAPI2_NP_SERVICE_NAME_NONE, // Indicates that there is no NP service name
   	SCE_NP_INVALID_SERVICE_LABEL,        // Indicates that there is no NP service label
   	filterParam, 2);
   if(ret < 0){
   	// Error handling
   }
   filterId = ret;

   // Delete handle
   ret = sceNpWebApi2PushEventDeleteHandle(libCtxId, handleId);
   if(ret < 0){
   	// Error handling
   }
   ```

   If specifying an NP service name or NP service label, the part where `sceNpWebApi2PushEventCreateFilter()` is called will be as follows.

   ```
   #define NP_SERVICE_NAME "presence2"  // If the NP service name is "presence2". For other NP service names, refer to the documentation for the respective Web APIs.
   #define SERVICE_LABEL (0)  // NP service label set upon requesting PlayStation(TM)Network service usage

   // Create Push event filter. Note that this is a blocking function. 
   ret = sceNpWebApi2PushEventCreateFilter(
   	libCtxId, handleId,
   	NP_SERVICE_NAME,     // NP service name
   	SERVICE_LABEL,       // NP service label
   	filterParam, 2);
   if(ret < 0){
   	// Error handling
   }
   filterId = ret;
   ```
2. **Register Push event callback functions**

   Execute `sceNpWebApi2PushEventRegisterCallback()` to register a callback function to receive Push events. Specify the NpWebApi2 library user context and the filter ID issued when the Push event filter was created as arguments. This will cause the registered Push event callback function to be called when a Push event that matches the data type and NP service indicated by the Push event filter is received for the user indicated by the user context. In addition, extended data will be notified with a Push event callback function argument if extended data that matches the extended data key specified in the Push event filter is included in the Push event.

   When a callback function is registered, a callback ID will be issued.

   Note:

   Do not call NpWebApi2 library functions within Push event callback functions defined on the application side.

   ```
   void
   pushEventCallbackFunc(
   	int32_t userCtxId,
   	int32_t callbackId,
   	const char *pNpServiceName,
   	SceNpServiceLabel npServiceLabel,
   	const SceNpPeerAddressA *pTo,
   	const SceNpOnlineId *pToOnlineId,
   	const SceNpPeerAddressA *pFrom,
   	const SceNpOnlineId *pFromOnlineId,
   	const SceNpWebApi2PushEventDataType *pDataType,
   	const char *pData,
   	size_t dataLen,
   	const SceNpWebApi2PushEventExtdData *pExtdData,
   	size_t extdDataNum,
   	void *pUserArg
   	)
   {
   	// If you do not specify an NP service name or NP service label
   	// pNpServiceName is NULL
   	// npServiceLabel is SCE_NP_INVALID_SERVICE_LABEL
   }

   int32_t ret = 0;
   int32_t userCtxId;
   int32_t filterId;
   int32_t callbackId = 0;

   // Register a Push event callback function
   ret = sceNpWebApi2PushEventRegisterCallback(
   	userCtxId, filterId, pushEventCallbackFunc, NULL);
   if(ret < 0){
   	// Error handling
   }
   callbackId = ret;
   ```

   The relationships of callbacks registered by `sceNpWebApi2PushEventRegisterCallback()` with Push event filters that are created by the `sceNpWebApi2PushEventCreateFilter()` function that is linked to each callback and Push events from the server are shown in the figure below. A match with the data type (and extended data key) is checked and the relevant callback is triggered.
3. **Monitor for Push event notifications**

   After registering a Push event callback function, periodically call `sceNpCheckCallback()`. The Push event callback function will be called in the thread that called `sceNpCheckCallback()`.
4. **Processing when it's no longer necessary to receive push events**

   Once it's no longer necessary to receive Push events, deregister the Push event callback function and delete the Push event filter.

   Note:

   It's also possible to associate one filter ID with multiple Push event callback functions. However, don't forget to deregister the associated Push event callback functions when deleting the Push event filter. When the Push event filter is deleted, the associated Push event callback functions will no longer be called.

   ```
   // Deregister a Push event callback function
   ret = sceNpWebApi2PushEventUnregisterCallback(
   	userCtxId, callbackId);
   if(ret < 0){
   	// Error handling
   }

   // Delete a Push event filter
   ret = sceNpWebApi2PushEventDeleteFilter(
   	libCtxId, filterId);
   if(ret < 0){
   	// Error handling
   }
   ```

# Receiving Order-Guaranteed Push Events

1. **Create a Push event filter**

   Run `sceNpWebApi2PushEventCreateFilter()` to create a Push event filter indicating the data type and extended data of the Push events you intend to receive. This step is the same as for regular Push events; therefore, refer to "[Create a Push event filter](receiving-normal-push-events.html#np-web-api2-library-overview_2_4__np-web-api2-library-overview_2_4_1)" in the "[Receiving Normal Push Events](receiving-normal-push-events.html)" section.
2. **Register Push context callback functions**

   Notifications for "order-guaranteed Push events" are received by a Push context callback function (`SceNpWebApi2PushEventPushContextCallback`).

   Note:

   Do not call NpWebApi2 library functions within Push context callback functions defined on the application side.

   ```
   void
   pushContextCallbackFunc(
   	int32_t userCtxId,
   	int32_t callbackId, // The pair of callbackId and pPushCtxId are called back in an order-guaranteed state
   	const SceNpWebApi2PushEventPushContextId *pPushCtxId, // Level at which order-guaranteeing is managed
   	SceNpWebApi2PushEventPushContextCallbackType cbType, // Flag for detecting the lack of an event
   	const char *pNpServiceName,
   	SceNpServiceLabel npServiceLabel,
   	const SceNpPeerAddressA *pTo,
   	const SceNpOnlineId *pToOnlineId,
   	const SceNpPeerAddressA *pFrom,
   	const SceNpOnlineId *pFromOnlineId,
   	const SceNpWebApi2PushEventDataType *pDataType,
   	const char *pData,
   	size_t dataLen,
   	const SceNpWebApi2PushEventExtdData *pExtdData,
   	size_t extdDataNum,
   	void *pUserArg
   	)
   {
   	// Error handling may be required,
   	// based on SceNpWebApi2PushEventPushContextCallbackType,
   	// in Push context callbacks that receive "order-guaranteed Push events"
   	switch (cbType) {
   	case: SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_RECEIVED: 
   		// Because the Push event has been received in a state with the
   		// order guaranteed, the Push event is processed normally
   		break;
   	case: SCE_NP_WEBAPI2_PUSH_EVENT_PUSH_CONTEXT_CALLBACK_TYPE_DROPPED: 
   		// Because the Push event was dropped without the order being 
   		// guaranteed, and thus, because the Push event that should have been received was unable to be received, perform the appropriate
   		// error handling based on the specifications of the Web API
   		break;
   	default: 
   		// Do nothing
   		break;
   	}
   }

   int32_t ret = 0;
   int32_t userCtxId;
   int32_t filterId;
   int32_t callbackId = 0;

   // Register a Push context callback function
   ret = sceNpWebApi2PushEventRegisterPushContextCallback(
   	userCtxId, filterId, pushContextCallbackFunc, NULL);
   if(ret < 0){
   	// Error handling
   }
   callbackId = ret;
   ```

   It's possible to register multiple Push context callback functions. Note that for Push context callback functions registered multiple times, Push events (after being filtered by a Push event filter) addressed to the same Push context ID (`pPushCtxId`) will be duplicated and notified. The relationships of callbacks, Push event filters, Push context IDs, and the triggering of callbacks are indicated in the figure below.

   If the drop of an order-guaranteed Push event is detected in one of the Push contexts, the drop will be notified to all registered Push event callback functions irrespective of the Push event filters. Push event callback functions must appropriately handle the notified drop using the value of the Push context ID (`pPushCtxId`).
3. **Create a Push context**

   Use `sceNpWebApi2PushEventCreatePushContext()` to create a Push context. The following example code demonstrates how to create a Push context.

   ```
   int32_t ret = 0;
   int32_t userCtxId;

   SceNpWebApi2PushEventPushContextId pushCtxId;
   memset(&pushCtxId, 0, sizeof(pushCtxId));

   // Create a Push context
   ret = sceNpWebApi2PushEventCreatePushContext(
   	userCtxId, &pushCtxId);
   if(ret < 0){
   	// Error handling
   }
   ```
4. **Record the Push context on the server**

   Record the Push context ID of the created Push context (that is, the `uuid` member of the `SceNpWebApi2PushEventPushContextId`) on the Web API server. For the details of how to record this ID, refer to the documentation for the Web API (e.g., [Session Manager Web API Overview](../../../WebAPI/latest/Session_Manager_WebAPI-Overview/__document_toc.html)).

   Note:

   Make sure to perform [(1) Create a Push event filter](receiving-order-guaranteed-push-events.html#np-web-api2-library-overview_2_5__np-web-api2-library-overview_2_5_1) before you record the Push context on the server. It won't be possible to receive order-guaranteed Push events if the procedural steps (1) and (4) are reversed.

   An example of registering a Push context ID in a createPlayerSessions API call using the Session Manager Web API is provided below:

   ```
   int32_t userCtxId; // NpWebApi2 user context ID already created
   SceNpWebApi2PushEventPushContextId pushCtxId; // Already created in the previous section

   // Include the Push Context Id in the request for the createPlayerSessions API
   SceNpWebApi2ContentParameter param = {};
   char buf[512] = {}; // A buffer large enough to embed Json
   const char jsonTemplate[] = {
       "{" \
           "\"playerSessions\": [" \
               "{" \
                   "\"localizedSessionName\": {" \
                       "\"defaultLanguage\": \"en-US\"," \
                       "\"localizedText\": {" \
                           "\"en-US\": \"en-US Session Name\"," \
                           "\"ja-JP\": \"ja-JP Session Name\"" \
                       "}" \
                  "}," \
                  "\"maxPlayers\": 10," \
                  "\"maxSpectators\": 10," \
                  "\"member\": {" \
                      "\"players\": [" \
                          "{" \
                              "\"accountId\": \"me\"," \
                              "\"platform\": \"PS5\"," \
                              "\"pushContexts\": [" \
                                  "{" \
                                      "\"pushContextId\": \"%s\"" \
                                  "}" \
                              "]" \
                          "}" \
                      "]" \
                  "}," \
                  "\"supportedPlatforms\": [" \
                      "\"PS5\"," \
                      "\"PS4\""\
                  "]" \
               "}" \
           "]" \
       "}" \
   };
   snprintf(buf, sizeof(buf), jsonTemplate, pushCtxId.uuid); // **Embed**
   param.contentLength = strlen(buf);
   param.pContentType = SCE_NP_WEBAPI2_CONTENT_TYPE_APPLICATION_JSON_UTF8;

   // Call the Web API (Register the Push context ID with the Session Manager server)
   int64_t reqId = 0;
   ret = sceNpWebApi2CreateRequest(
       userCtxId, "sessionManager", "/v1/playerSessions",
       SCE_NP_WEBAPI2_HTTP_METHOD_POST, &param, &reqId);
   if (ret < 0) {
       // Error handling
   }
   ret = sceNpWebApi2SendRequest(reqId, buf, strlen(buf), NULL);
   if (ret < 0) {
       // Error handling
   }
   ret = sceNpWebApi2DeleteRequest(reqId);
   if (ret < 0) {
       // Error handling
   }
   ```
5. **Start Push context callback functions**

   Immediately after a Push context is recorded on a Web API server, Push events will start to arrive directed to that Push context. By using `sceNpWebApi2PushEventStartPushContextCallback()` to start Push context callbacks, the events that arrive will become receivable by the callback.

   The following example code demonstrates how to start a Push context callback.

   ```
   int32_t ret = 0;
   int32_t userCtxId;
   SceNpWebApi2PushEventPushContextId pushCtxId;

   // Start the Push context callback
   ret = sceNpWebApi2PushEventStartPushContextCallback(
   	userCtxId, &pushCtxId);
   if(ret < 0){
   	// Error handling
   }
   ```

   Note:

   Start the Push context callback promptly once a Push context has been recorded on the Web API server. If a long time elapses before the callback is started, a large number of Push events will remain in the Push context, which risks causing the queue to overflow and Push events to be dropped.

   It is also possible to first start a Push context callback and then record the Push context on the Web API server. In that case, however, be aware that no problems will occur even if Push events arrive ahead of responses whose recording is complete.
6. **Monitor for Push event notifications**

   After registering a Push context callback function, call `sceNpCheckCallback()` periodically. The Push context callback function will be called from the thread that called `sceNpCheckCallback()`.

   Note:

   If Push events aren't notified, check the following.

   * Whether there is an error in the datatype used upon creating the Push event filter
   * Whether the filter prepared for "order-guaranteed Push events" has been registered using `sceNpWebApi2PushEventRegisterPushContextCallback()` (or if `sceNpWebApi2PushEventRegisterCallback()` has been used incorrectly)

   Be careful as an error will not occur when making a mistake upon creating the Push event filter or registering the callback function.
7. **Processing when it's no longer necessary to receive push events**

   Once it's no longer necessary to receive Push events, deregister the Push context callback function and delete the Push event filter.

   Note:

   It's also possible to associate one filter ID with multiple Push context callback functions. However, don't forget to deregister the associated Push context callback functions when deleting the Push event filter. When the Push event filter is deleted, the associated Push context callback functions will no longer be called.

   ```
   // Deregister a Push context callback function
   ret = sceNpWebApi2PushEventUnregisterPushContextCallback(
   	userCtxId, callbackId);
   if(ret < 0){
   	// Error handling
   }

   // Delete a Push event filter
   ret = sceNpWebApi2PushEventDeleteFilter(
   	libCtxId, filterId);
   if(ret < 0){
   	// Error handling
   }
   ```

# Termination/Post-processing

1. **Delete user contexts**

   When the user contexts are no longer required, execute `sceNpWebApi2DeleteUserContext()` to delete the user contexts.

   ```
   int32_t userCtxId; // User context ID of user context to delete

   int32_t ret = 0;

   if (userCtxId > 0) {
       ret = sceNpWebApi2DeleteUserContext(userCtxId);
       if (ret < 0) {
           // Error handling
       }
   }
   ```
2. **Terminate the library**

   When the NpWebApi2 library is no longer needed, call `sceNpWebApi2Terminate()` to perform termination processing.

   ```
   int32_t libCtxId; // Library context ID

   int32_t ret = 0;

   if (libCtxId > 0) {
       ret = sceNpWebApi2Terminate(libCtxId);
       if (ret < 0) {
           // Error handling
       }
   }
   ```