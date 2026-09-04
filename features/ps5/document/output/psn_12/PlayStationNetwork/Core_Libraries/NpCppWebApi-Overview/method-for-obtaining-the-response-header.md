# NpCppWebApi Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Overview/method-for-obtaining-the-response-header.html

# Reference Information

# Correspondence Between Web APIs and Web API Call Functions

Web API call functions are incorporated into the `XxxxApi` classes (referred to as "Api classes"), under the namespace `sce::Np::CppWebApi::ApiGroup::Version` (or `sce::Np::CppWebApi::ApiGroup::Version::Label`). The namespaces and Api classes are arranged hierarchically and named based on the following rules.

* `ApiGroup`: The namespace corresponding to the API group of the Web API
* `Version`: The namespace corresponding to the version in the Web API path. (Example: The namespace corresponding to the path "v1" of "`/v1/users/{accountId}/profiles`" is "`V1`")
* `Label`: (Unused hierarchical layer)
* `Xxxx`: The name corresponding to the section name that distinguishes each Web API.

Note that the name of the header file for an Api class consists of `Xxxx` followed by "Api.h" (XxxxApi.h).

The function name is the value of an identifier called operationId, which is uniquely assigned (within an API group) to each Web API endpoint.

If the preceding rules are kept in mind, it is easy to find the desired function among the various Web API call functions. A list of Web API endpoints and Web API call functions for the NpCppWebApi library is shown for reference in the "Correspondence Between Web APIs and Library Functions" section in the [NpCppWebApi Library Reference](../NpCppWebApi-Reference/__document_toc.html) document.

# Instantiating Special-Purpose Templates and Smart Pointers

Templates and smart pointers of the NpCppWebApi library can only provide classes of the NpCppWebApi library to template arguments.

However, because template implementation is concealed by the library, the combinations of template arguments that can be instantiated are limited. If a combination of a template class and a template argument type that isn't expected by the NpCppWebApi library is declared, the template class cannot be instantiated, and an error will occur upon linking.

# Instance Lifetime

The following two types of lifetime management are performed for the instances of each class of the NpCppWebApi library:

## Lifetime management of classes that are used via a smart pointer

A class that corresponds 1:1 with a JSON object used for input/output with Web APIs and its components are the target. They will be instantiated using the library context heap and passed to the application in the form of smart pointers.

Smart pointers are responsible for discarding instances, and it is not necessary to worry about forgetting to release them.

Note:

The heap (mspace) managed by the library context is used to instantiate an instance pointed to by a smart pointer.

Because of this, the reference count of the smart pointer must be 0 (state where the smart pointer is not holding an instance that was instantiated using the applicable heap) to call `sce::Np::CppWebApi::Common::terminate()`, which terminates the library context.

## Lifetime management of classes with explicit initialization and termination functions

The following classes, for which lifetimes are managed by the application, are the target.

* `sce::Np::CppWebApi::Common::LibContext`
* `sce::Np::CppWebApi::Common::TransactionBase` class and its derived class
* `sce::Np::CppWebApi::Common::ParameterBase` that represents input parameters of Web API call functions and its derived class

Note:

Classes with explicit initialization and termination functions are not expected to be managed by smart pointers. Make sure to call a function that is equivalent to termination processing on the application side.

# getter and setter Functions that Handle sce::Json::Object for Input/Output

The NpCppWebApi library provides classes that correspond 1:1 with Json objects used by the Web APIs. The member structures of these classes are statically fixed as Web API interface specifications, and there are corresponding getter and setter functions for each.

On the other hand, there are some objects for which members aren't statically fixed (for example, when the applicable structure is one that has been arbitrarily selected by the application or when the structure is dynamically determined according to the state of the server's database). When handling such objects, the `sce::Json::Object` type will be handled as the input/output type within the getter and setter functions. When handling the `sce::Json::Object` type, check descriptions of the related Web API document and the Json2 library documents, and obtain/set the required values.

# Method for Specifying the Request Header

A request header is specified using the setter function of the input parameter class that has "`ParameterTo`" as a prefix. (Refer to [Initialize the Input Parameters](basic-procedure.html#np-cpp-web-api-library-overview_1_1__np-cpp-web-api-library-overview_1_1_7).)

If a need arises to specify an arbitrary request header that doesn't have a setter prepared for it, setting will be possible by calling the ParameterBase::setRequestHeader() function prepared in the base class. An example is shown below.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;

// Common::LibContext libCtx; // Context initialized in the previous step

UserProfile::V1::FriendsApi::ParameterToGetFriends param;

ret = param.initialize(&libCtx, "me");
if (ret < 0) {
	// Error handling
}

// Specify an arbitrary key using the setRequestHeader() function of the ParameterBase base class
ret = param.setRequestHeader("TestHeaderKey", "TestHeaderValue"); 
// Note: Currently, there are no header keys or values that are actually used, but they will be implemented in the future.

if (ret < 0) {
	// Error handling
}
```

# Method for Obtaining the Response Header

An instance of a class with the "ResponseHeaders" suffix can be obtained by calling the Transaction::getResponseHeaders() function. Obtain the response header by using the getter function prepared for that instance.

If a need arises to obtain an arbitrary response header that is not defined by an individual Web API (for example, the Retry-After header), the value of the arbitrary response header can be obtained by calling the ResponseHeaderBase::getHeaderValue() function prepared in the base class. An example is shown below.

```
using namespace sce::Np::CppWebApi;

int32_t ret = 0;
// Transaction instance type (described earlier)
// Common::Transaction<
// 	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponse >, 
// 	Common::IntrusivePtr < UserProfile::V1::GetBasicProfileResponseHeaders > > trans; 

// Smart pointer with the proper type for receiving the response header in the template argument
Common::IntrusivePtr<Common::ResponseHeaderBase> header;

ret = trans.getResponseHeaders(header);
if (ret < 0) {
	// Error handling
}

Common::IntrusivePtr<Common::String> headerValue;

// Specify an arbitrary key using the getHeaderValue() function of the ResponseHeaderBase base class
ret = header->getHeaderValue("Retry-After", headerValue); 
if (ret < 0) {
	// Error handling
}

// Hereafter, write application code that uses headerValue
```

# Notes on Passing an Instance Dynamically Allocated by the Application to the Library with a Smart Pointer

In typical use cases of this library, a C++ class instance (imitating the configuration of a Json object) is allocated on the library side and passed to the application with a smart pointer.

In some use cases, however, an instance that is dynamically allocated on the application side is passed to the library with a smart pointer. For example, there are cases where `sce::Np::CppWebApi::Common::Vector` is passed to the library with a smart pointer.

In such cases, the library must be notified on how to free the instance that has been allocated on the application side. To do so, a deleter (`delete` or `free()` paired with `new` or `malloc()`) must be passed, along with the dynamically allocated instance, upon declaring the smart pointer. An example is shown below.

```
using namespace sce::Np::CppWebApi;
extern Common::LibContext libCtx; // Already initialized

// When using Common::IntrusivePtr to pass Common::Vector < Common::String >
// to the library, dynamically allocate Common::Vector
// using new on the application side
Common::Vector< Common::String >* fields = new Common::Vector< Common::String >(&libCtx);
if (!fields) {
	// Error handling
}

Common::String param1(&libCtx);
ret = param1.append("param1string");
if (ret < 0) {
	// Error handling
}

Common::String param2(&libCtx);
ret = param2.append("param2string");
if (ret < 0) {
	// Error handling
}

ret = fields->pushBack(param1);
if (ret < 0) {
	// Error handling
}

ret = fields->pushBack(param2);
if (ret < 0) {
	// Error handling
}

Common::IntrusivePtr < Common::Vector < Common::String > > fieldsPtr(
	fields,
	// Specify a function pointer or lambda expression deleter to the second argument below
	[](Common::Vector< Common::String > *ptr) {
	delete ptr; // delete paired with new of fields
	return;
	},
	nullptr);
```

# IsSet() for Classes That Correspond 1:1 with a Json Object

Of the classes provided by this library that correspond 1:1 with a JSON object, there are classes for which `IsSet()` is or isn't provided depending on the fields as indicated below.

```
namespace sce {
namespace Np {
namespace CppWebApi {
namespace SessionManager {
namespace V1 {

class PlayerSessionSpectator : public Common::RefObject
{
public: 
	// "accountId"
	SceNpAccountId getAccountId() const;
	void setAccountId(const SceNpAccountId &accountId);

// Omitted

	// "joinState"
	bool joinStateIsSet() const;
	void unsetJoinState();
	JoinState getJoinState() const;
	void setJoinState(const JoinState &joinState);
```

In the above example, the `PlayerSessionSpectator` class provides the `"accountId"` field and `"joinState"` field. While `"accountId"` doesn't have `IsSet()`, `"joinState"` has the `joinStateIsSet()` function. This indicates that `"accountId"` is a required field and that it always exists for the `PlayerSessionSpectator` class. On the other hand, `"joinState"` is an optional field and its existence must be checked for using `joinStateIsSet()` before a value can be obtained.

Use fields with `IsSet()` by first checking their existence as follows.

```
using namespace sce::Np::CppWebApi;

extern Common::IntrusivePtr < SessionManager::V1::PlayerSessionSpectator > playerSessionSpectatorPtr;
SessionManager::V1::JoinState joinState = 0;

if (playerSessionSpectatorPtr.get()) {

	// accountId can be used without having to check its existence
	SceNpAccountId accountId = playerSessionSpectatorPtr->getAccountId();

	// joinState can be used after checking its existence
	if (playerSessionSpectatorPtr->joinStateIsSet()) {
		joinState = playerSessionSpectatorPtr->getJoinState();
		// Code using joinState
	}
}
```

Whether a field is required or not is also noted in each Web API reference document. Fields with true in the Required column in the table that shows the structure of the Json object returned by the server always exist and don't require an existence check. Fields with false in the Required column are optional and require an existence check.

# How to Get NpCppWebApi to Parse PlayStation™Network Web API Server Error Common Objects

All PlayStation™Network Web APIs have a common object definition for returning server error responses to applications. Even in cases in which a common error object is returned, it is often sufficient to process the error by converting the SDK library error code to a Web API error code. (See [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html) for details.)

A common error object can be obtained by passing an `SceNpWebApi2ResponseInformationOption` to `TransactionBase::setResponseInformationOption()` and setting the destination to store optional response information. An error object that can be obtained with an `SceNpWebApi2ResponseInformationOption` is an unparsed Json string. To obtain a parsed version, do the following:

```
trans.setResponseInformationOption(&respOpt);
// Omitted
int32_t ret = sce::Np::CppWebApi::UserProfile::V1::BasicProfileApi::getPublicProfile(
	ctxId,
	param,
	trans);
// Omitted
ret = trans.getResponse(respPtr);
if (ret < 0) {
	// Error handling
	if (WebApi::Common::isWebApiError(ret)) {
		// Web API Error
		auto error = respPtr->getError();
		if (error != nullptr) {
			// code
			uint64_t code = error->getCode();
			// message
			std::string message = error->getMessage().c_str();
			//reference
			std::string reference = error->getReferenceId().c_str();
		}
	} else {
		// Other errors
	}
}
```

You can verify whether the server returned a common error object by passing the error in the return value when the response is obtained to `isWebApiError()`.

The response class inherits from the error response class. If a common error object is returned from the server, use the `getError()` error response class to obtain the error object.

Note that the `SceNpWebApi2ResponseInformationOption` must be set with a buffer large enough to store the Json object. If it is not large enough, the return value of the error response class `getError()` will be a NULL pointer even if the server returns a common error object, so perform a NULL pointer check when accessing the error object.