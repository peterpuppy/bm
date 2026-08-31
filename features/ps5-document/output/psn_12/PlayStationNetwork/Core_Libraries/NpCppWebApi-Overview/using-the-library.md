# NpCppWebApi Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Overview/using-the-library.html

# Using the Library

# Basic Procedure

The basic procedure for using the NpCppWebApi library to access a Web API is described here. An outline of the processing flow is as provided below. It is split into four blocks: initialization/pre-processing, using the Web API, sending and receiving binary data, and termination processing.

1. **Initialization/Pre-processing**: [Initialize the NpWebApi2 Library and Create a User Context](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_2)
2. **Initialization/Pre-processing**: [Initialize the Json2 Library](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_3)
3. **Initialization/Pre-processing**: [Initialize the NpCppWebApi Library](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_4)
4. **Using Web APIs**: [Start a Transaction](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_6): `sce::Np::CppWebApi::Common::Transaction::start()`
5. **Using Web APIs**: [Initialize the Input Parameters](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_7):

   (Example) `sce::Np::CppWebApi::UserProfile::V1::BasicProfileApi::ParameterToGetBasicProfile::create()`
6. **Using Web APIs**: [Call the Web API Call Function](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_8):

   (Example) `sce::Np::CppWebApi::UserProfile::V1::BasicProfileApi::getBasicProfile()`
7. **Using Web APIs**: [Get the Response](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_9):

   (Example) `sce::Np::CppWebApi::Common::Transaction::getResponse()`
8. **Using Web APIs**: [End the Transaction](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_10): `sce::Np::CppWebApi::Common::Transaction::finish()`:
9. **Using Web APIs**: [Get the Data from the Response](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_11):

   (Example) `sce::Np::CppWebApi::UserProfile::V1::GetBasicProfileResponse::getOnlineId()`
10. **Sending and Receiving Binary Data**: [Using Stream Transactions](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_13)
11. **Termination Processing**: [Terminate the Library](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_15): `sce::Np::CppWebApi::Common::``terminate()`

## Initialization/Pre-processing

## (1) Initialize the NpWebApi2 Library and Create a User Context

Perform the required pre-processing for the NpWebApi2 library and then initialize the library. Create an NpWebApi2 user context and obtain a user context ID. For details concerning this procedure, refer to the [NpWebApi2 Library Overview](../NpWebApi2-Overview/__document_toc.html) and [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html) documents. The NpWebApi2 user context ID that was created is required in the next step.

## (2) Initialize the Json2 Library

Initialize the Json2 library. For details concerning this procedure, refer to the [Json2 Library Overview](../Json2-Overview/__document_toc.html) and [Json2 Library Reference](../Json2-Reference/__document_toc.html) documents.

## (3) Initialize the NpCppWebApi Library

Call `sce::Np::CppWebApi::Common::``initialize()` to initialize the NpCppWebApi library. Since the `sce::Np::CppWebApi::Common::LibContext` instance that is initialized at this time is required in subsequent steps, make sure that it is not deleted by the application until termination processing is performed.

Note:

When an `sce::Np::CppWebApi::Common::LibContext` instance is copied, a shallow copy is performed. Since only a pointer to the internal structure is copied, keep in mind that for multiple instances copied from the same instance, termination processing can be performed only once for any one instance.

Sample code is shown below.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
Common::InitParams initParams;
Common::LibContext libCtx; // Used later

ret = Common::initialize(initParams, libCtx);
if (ret < 0) {
	// Error handling
}
```

The sample code provided above is an example of initializing the library for use with synchronous processing.

To enable asynchronous processing, set 1 for `InitParam::numWorkers`, as shown below. A worker thread will be created within the library and will handle the network processing corresponding to Web API call functions.

```
Common::InitParams initParams;

initParams.numWorkers = 1;
```

Note:

A value greater than 1 cannot be specified for `InitParam::numWorkers`.

## Using Web APIs

## (4) Start a Transaction

Prepare an instance of `sce::Np::CppWebApi::Common::``Transaction` and call `sce::Np::CppWebApi::Common::Transaction::start()` (note that although this is called "starting a transaction", no communication has actually been sent over the network yet).

`sce::Np::CppWebApi::Common::``Transaction` is the template class. Specify the template argument type according to the Web API call function that will be called during this transaction.

Note:

You can perform this step or the next step [(5)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_7) in either order; the result will be the same regardless.

Sample code is shown below.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
// Common::LibContext libCtx; // LibContext previously initialized

// Declared using the Transaction instance type that is to be used in the subsequent API call
// sce::Np::CppWebApi::UserProfile::V1::BasicProfileApi::getPublicProfile()

Common::Transaction <
	Common::IntrusivePtr<
	UserProfile::V1::GetPublicProfileResponse
	> > trans; 

ret = trans.start(&libCtx);
if (ret < 0) {
	// Error handling
}
// Subsequently, have the application manage the Transaction instance until finish() is called
```

If obtaining a callback response when performing asynchronous processing, call `sce::Np::CppWebApi::Common::Transaction::setOnFinishedCallback()` after calling `sce::Np::CppWebApi::Common::Transaction::start()`.

```
// After trans.start() has been called
ret = trans.setOnFinishedCallback(
	[](
	int64_t id,
	int32_t retcode,
	Common::IntrusivePtr< UserProfile::V1::GetPublicProfileResponse> res,
	void *userdata)
{
	// Callback processing when successful. 
	// Definition of the processing that gets the required data from res. 
},
	[](
	int64_t id,
	int32_t retcode,
	void *userdata
	)
{
	// Callback processing when an error occurs
},
this); // Arbitrary data whose lifetime continues even when a callback is called (Example: this)
if (ret < 0) {
	// Error handling
}
```

## (5) Initialize the Input Parameters

Initialize the input parameters specific to the API call that corresponds to the Web API.

**a. Input parameters when a Web API is used to get information**

The following sample code initializes `ParameterToGetPublicProfile` in order to call `sce::Np::CppWebApi::UserProfile::V1::BasicProfileApi::getPublicProfile()`.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
// Common::LibContext libCtx; // Context initialized in the previous step
SceNpAccountId accountId = GetMyAccountId(); // For example, your own account ID

// When the subsequent API call is
// sce::Np::CppWebApi::UserProfile::V1::BasicProfileApi::getPublicProfile(),
// a ParameterToGetPublicProfile object is required
UserProfile::V1::BasicProfileApi::ParameterToGetPublicProfile param;

ret = param.initialize(&libCtx, accountId);
if (ret < 0) {
	// Error handling
}
```

To call a Web API directly, you must specify the following parameters of various formats: a path parameter that will be part of the URL path, a query parameter given by a query string and a header parameter given by the HTTP request header, a request body, and a Json object. When the NpCppWebApi library is used, all of these input parameters can be stored in an instance of the input parameter class having the prefix "`ParameterTo`" (for example, `ParameterToGetPublicProfile`) and passed to the Web API call function.

Specify the required parameters for that Web API as arguments in the initialization function of the input parameter object.

Optional parameters can be set using the relevant setter functions after the input parameter object is initialized. Provided below is an example of calling setter functions—after initializing `ParameterToGetFriends`—to set the optional parameters `offset` and `limit`, which can be passed when calling `sce::Np::CppWebApi::UserProfile::V1::FriendsApi::getFriends()`.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;

int32_t offset = 0;
int32_t limit = 10;
// Common::LibContext libCtx; // Context initialized in the previous step

UserProfile::V1::FriendsApi::ParameterToGetFriends param;

ret = param.initialize(&libCtx, "me");
if (ret < 0) {
	// Error handling
}
param.setoffset(offset);
param.setlimit(limit);
```

Initialized input parameter classes can be reused until `terminate()` is called.

**b. Input parameters when a Web API is used to register information**

The following sample code initializes `Leaderboards::V1::Api::ParameterToRecordScore` in order to call `sce::Np::CppWebApi::Leaderboards::V1::Api::``recordScore()`.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
Common::LibContext libCtx; // Context initialized in the previous step
int64_t score = 12345; // Score to be registered in Leaderboards

// When the subsequent API call is
// sce::Np::CppWebApi::Leaderboards::V1::Api::recordScore(),
// a ParameterToRecordScore object is required 
Leaderboards::V1::Api::ParameterToRecordScore param;

// To initialize ParameterToRecordScore, a RecordScoreRequestBody 
// object is required. Declare a smart pointer for handling that object. 
Common::IntrusivePtr <
	Leaderboards::V1::RecordScoreRequestBody 
	> requestBody;

// The RecordScoreRequestBody class has a 1:1 correspondence with the Json object. 
// It is instantiated by the create() function of a class with a "Factory" suffix. 
ret = Leaderboards::V1::RecordScoreRequestBodyFactory::create(
	&libCtx,
	score, // Information required for this object
	&requestBody);
if (ret < 0) [
	// Error handling
}
// To provide other information besides score in the RecordScoreRequestBody object,
// call the appropriate setter function as shown below. 
ret = requestBody->setComment("Comment for the score");
if (ret < 0) {
	// Error handling
}
```

When the Web API is called directly, a Json object with the information to be registered must be assembled (serialized). However, if you use the NpCppWebApi library, a C++ class instance corresponding to the Json object is prepared and appropriate values are assigned to it. Since the library serializes the Json object, the application does not need to perform serialization on its own.

## (6) Call the Web API Call Function

Web API call functions are incorporated into the `XxxxApi` classes (referred to as "Api classes"), under the `sce::Np::CppWebApi::Aaaa::Vb` (or `sce::Np::CppWebApi::Aaaa::Vb::Cccc`) namespace, according to the Web API.

The NpWebApi2 user context ID that was created in step [(1)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_2), the `Transaction` instance that was set up in step [(4)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_6), and the input parameters that were initialized in step [(5)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_7) are passed as arguments to the Web API call function.

The following sample code calls `sce::Np::CppWebApi::UserProfile::V2::BasicProfileApi::getPublicProfile()`.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
int32_t npWebApi2UserCtxId; // NpWebApi2 user context ID created earlier.
				// Will control the Web API as the corresponding user

UserProfile::V1::BasicProfileApi::ParameterToGetPublicProfile param; // Input parameters prepared earlier

// Transaction instance type (described earlier)
// Common::Transaction<
//	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponse >, 
//	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponseHeaders > > trans; 

ret = sce::Np::CppWebApi::UserProfile::V2::BasicProfileApi::getPublicProfile(
	npWebApi2UserCtxId, 
	param,
	trans); // This Transaction instance can be used to abort network
		 // processing initiated by this function or to get the response.
if (ret < 0) {
	// Error handling
}

ret = param.terminate();	// terminate() is possible for input parameters
				// immediately after the call of the Web API call function
if (ret < 0) {
	// Error handling
}
```

Note:

* By default, a Web API call function executes as a blocking function (using synchronous processing). Since execution may be blocked for a long time, be sure to call these functions from a thread that will not impact screen drawing.
* If the library was set up when it was initialized so that it would perform asynchronous processing, Web API call functions will not be blocked; however, the possibility that blocking may occur when responses are being obtained must be considered. For details, refer to the next section in this document, "[Get the Response](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_9)".

Note:

* Data stored by the input parameter instance will be deep-copied within the Web API call function. Because of this, `terminate()` for the input parameter class can be called after the Web API call function returns.

## (7) Get the Response

To get the response, call `getResponse()` on the `sce::Np::CppWebApi::Common::Transaction` instance. At the same time, prepare a smart pointer (`sce::Np::CppWebApi::Common::IntrusivePtr`) with the proper type for receiving the response in the template argument, and pass it to `getResponse()`. Sample code is shown below.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
// Transaction instance type (described earlier)
// Common::Transaction<
// 	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponse >, 
// 	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponseHeaders > > trans; 

// Smart pointer with the proper type for receiving the response in the template argument
Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponse > respPtr;

ret = trans.getResponse(respPtr);
if (ret < 0) {
	// Error handling
}
```

Note:

When writing code where a smart pointer (`respPtr` above), which has the proper type for receiving the response in a template argument, is accessed at a stage when the normal termination of `Transaction::getResponse()` cannot be confirmed (when not implemented or if it failed), it is necessary to consider the fact that the instance pointed to by the smart pointer is a NULL pointer.

When the Web API call function is called synchronously, `Transaction::getResponse()`, mentioned above, will return immediately, and the response can be received. This is because network processing will end during the Web API call function.

However, if the library was set up when it was initialized so that it would perform asynchronous processing, `Transaction::getResponse()` may be blocked. That is to say, the function will return immediately if network processing by the internal library thread has finished but will be blocked if that processing is ongoing. You can check whether network processing has finished using `Transaction::hasResponse()`. Thus, confirm that the response has been received before calling `Transaction::getResponse()`, as shown below.

```
if (trans.hasResponse()) { // Poll periodically
	ret = trans.getResponse(respPtr);
	if (ret < 0) {
		// Error handling
	}
}
else {
	// Do not get the response
}
```

If the library has been set up to perform asynchronous processing and `Transaction::setOnFinishedCallback()` was called in step [(4)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_6), you can obtain the response object with the argument of the callback function.

## (8) End the Transaction

After obtaining the response, call `finish()` on the `sce::Np::CppWebApi::Common::Transaction` instance to end the transaction and release internal library resources. Sample code is shown below.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
// Transaction instance type (described earlier)
// Common::Transaction<
// 	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponse >, 
// 	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponseHeaders > > trans; 

ret = trans.finish();
if (ret < 0) {
	// Error handling
}
```

Note:

If `Transaction::setOnFinishedCallback()` has been used to receive the response with a callback function, the callback function will not be called again after `Transaction::finish()` is called.

## (9) Get the Data from the Response

Various getter functions are provided for getting data from the response instance. Use these to get data from the response for use in application processing. Sample code is shown below.

```
using namespace sce::Np::CppWebApi;

// Type of smart pointer for receiving the response from step (7).
// Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponse > respPtr;

SceNpOnlineId onlineid = respPtr->getOnlineId();
// Processes that use onlineID can be performed later

if (respPtr->personalDetailIsSet()) { // Existence check for members that may not exist
	if (respPtr->getPersonalDetail()->firstNameIsSet()) { // Existence check
		// respPtr->getPersonalDetail()->getFirstName()
		// can be used to get the first name for later use
	}
}
```

Since response resources are released when the smart pointer (`sce::Np::CppWebApi::Common::IntrusivePtr`) is discarded, the application does not need to explicitly call a function to release these resources.

Note:

If you plan on using a string that was stored in the response after discarding the smart pointer, copy the actual string to application memory beforehand. If you only copy the pointer, there is a risk that invalid memory will be referenced after the smart pointer is discarded.

## Sending and Receiving Binary Data

## (10) Using Stream Transactions

Several Web APIs are available for sending and receiving large amounts of binary data, not just Json objects. To send and receive binary data, in addition to the steps described above, use `UpStreamTransaction` (for sending) and `DownStreamTransaction` (for receiving).

Note:

Be aware that, even if the library was set up when initialized so that it would perform asynchronous processing, `UpStreamTransaction` and `DownStreamTransaction` will perform synchronous processing.

For `UpStreamTransaction`, first specify the expected data size (`contentLength`) to be sent when starting the transaction in step [(4)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_6). Then, after calling the Web API call function in step [(6)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_8), use `UpStreamTransaction::sendData()` to send the binary data as follows.

```
using namespace sce::Np::CppWebApi;
namespace PsnLeaderboards = sce::Np::CppWebApi::Leaderboards::V1;
// Common::LibContext libCtx; // LibContext previously initialized

int32_t ret = 0;
size_t contentLength = get_content_length(); // Total size of data to be sent
char buf[512];

// UpStreamTransaction used for Leaderboards Web API recordLargeData()
Common::UpStreamTransaction <
	Common::IntrusivePtr <
	PsnLeaderboards::RecordLargeDataResponseBody >,
	Common::IntrusivePtr < 
	PsnLeaderboards::RecordApi::RecordLargeDataResponseHeaders > > trans;

// Instead of step (4)
ret = trans.start(&libCtx, contentLength);
if (ret < 0) {
	// Error handling
}

// Since steps (5) and (6) are similar to the ordinary case, the explanation is omitted here

// Step (10)
size_t remain = contentLength;
do {
	//
	// Insert code here to store data in buf (for example, read data from the file system)
	//

	// After executing the above code, use the stored buf to send the data
	ret = trans.sendData(buf, sizeof(buf));
	if (ret < 0) {
		// Error handling. Perform processing to exit the loop. 
		break;
	}
	offset += sizeof(buf);
	remain -= (remain > sizeof(buf)) ? sizeof(buf) : remain;
} while(remain > 0);

// Since steps (7), (8), and (9) are similar to the ordinary case, the explanation is omitted here
```

For `DownStreamTransaction`, call the Web API call function in step [(6)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_8), then use `DownStreamTransaction::readData()` as follows to receive the binary data.

```
using namespace sce::Np::CppWebApi;
namespace PsnLeaderboards = sce::Np::CppWebApi::Leaderboards::V1;
// Common::LibContext libCtx; // LibContext previously initialized

int32_t ret = 0;

// Steps (4), (5), and (6) are the same as the ordinary case. 
// For example, in step (6), call the Web API call function
// PsnLeaderboards::ViewApi::getLargeDataByObjectId(). 

// Step (10)
char buf[512];
do {
	memset(buf, 0, sizeof(buf));
	ret = trans.readData(buf, sizeof(buf));
	if (ret < 0) {
		// Error handling
	}

	//
	// Insert code here to perform operations such as writing the received data in buf to a file
	//
} while (ret > 0);

// All other steps are the same as the ordinary Transaction steps.
```

## Termination Processing

## (11) Terminate the Library

To terminate the library, perform termination processing for the instance in use (including discarding the smart pointer) and then call `sce::Np::CppWebApi::Common::terminate()`.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;

ret = Common::terminate(libCtx);
if (ret < 0) {
	// Error handling
}
```

## Aborting a Transaction

If a transaction must be aborted, call `sce::Np::CppWebApi::Common::Transaction::abort()`. After the transaction is aborted, execute step [(8)](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_10) to discard the transaction.

Note that `sce::Np::CppWebApi::Common::Transaction::hasResponse()` will return `true` after the transaction is aborted. In addition, `sce::Np::CppWebApi::Common::Transaction::getResponse()` will return immediately.