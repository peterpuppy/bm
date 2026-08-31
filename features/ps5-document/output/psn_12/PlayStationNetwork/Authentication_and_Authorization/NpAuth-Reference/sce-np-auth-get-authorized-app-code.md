# NpAuth Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Reference/sce-np-auth-get-authorized-app-code.html

# Communication Processing

# SceNpAuthGetAuthorizationCodeParameterV3

Authorization code obtainment parameters

## Definition

```
#include <np/np_auth.h>
typedef struct SceNpAuthGetAuthorizationCodeParameterV3 {
	size_t size;
	SceUserServiceUserId userId;
	uint8_t padding[4];
	const SceNpClientId *clientId;
	const char *scope;
} SceNpAuthGetAuthorizationCodeParameterV3;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID |
| `padding` | Not used (clear with 0's) |
| `clientId` | Client ID of the application server |
| `scope` | Entitlement scope for obtaining authorization codes |

## Description

This structure indicates the parameters specified during an `sceNpAuthGetAuthorizationCodeV3()` call.

For `size`, specify the size of this structure.

For `userId`, set the access target user's user ID.

For `clientId`, specify the client ID of the application server attempting to access the user's user information. Specify the client ID issued upon request in advance.

For `scope`, specify the entitlement scope for obtaining authorization codes. If there is more than one item for the information to obtain, specify them by inserting a space between items as in the following example.

```
"psn:s2s openid id_token:psn.basic_claims"
```

# sceNpAuthGetAuthorizationCodeV3

Get authorization code

## Definition

```
#include <np/np_auth.h>
int sceNpAuthGetAuthorizationCodeV3(
	int reqId,
	const SceNpAuthGetAuthorizationCodeParameterV3 *param,
	SceNpAuthorizationCode *authCode,
	int *issuerId
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID (IN) |
| `param` | Authorization code obtainment parameters (IN) |
| `authCode` | Destination to store the obtained authorization code (OUT) |
| `issuerId` | Destination to store the obtained issuer ID. NULL can be specified (OUT) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

If the error code is 0x82XXXXXX, it means it is a server error code. For details, refer to [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0), NULL was specified to `param` or `authCode`, or NULL was specified to a member of `param` |
| `SCE_NP_AUTH_ERROR_INVALID_SIZE` | 0x80550302 | `param`->`size` is invalid |
| `SCE_NP_AUTH_ERROR_OUT_OF_MEMORY` | 0x80550303 | Not enough free memory |
| `SCE_NP_AUTH_ERROR_ABORTED` | 0x80550304 | Processing aborted |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | Called in the signed-out state |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user does not exist |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a state where the user is not signed up |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged-out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |

## Description

This function obtains the authorization code. Transfer the obtained authorization code and Issuer ID to the application server. The application server can use this to obtain the access token and access user information managed by the PlayStation™Network servers. The Issuer ID is used for identifying the PlayStation™Network environment.

This function carries out synchronous or asynchronous processing depending on the request argument.

When executed as a synchronous processing, the function is blocking until communication ends and the authorization code is obtained (or an error is generated). When synchronous processing completes, call `sceNpAuthDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain results from the server. The processing result must be received using either `sceNpAuthWaitAsync()` or `sceNpAuthPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

When this function is executed synchronously, blocking may be performed for long periods of time. This function must not be called from a time-critical thread.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`, `sceNpAuthAbortRequest()`

# SceNpAuthGetIdTokenParameterV3

ID token obtainment parameters

## Definition

```
#include <np/np_auth.h>
typedef struct SceNpAuthGetIdTokenParameterV3 {
	size_t size;
	SceUserServiceUserId userId;
	uint8_t padding[4]
	const SceNpClientId *clientId;
	const SceNpClientSecret *clientSecret;
	const char *scope;
} SceNpAuthGetIdTokenParameterV3;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID |
| `padding` | Not used (clear with 0's) |
| `clientId` | Client ID of the application server |
| `clientSecret` | Application server client secret |
| `scope` | Entitlement scope for obtaining ID token |

## Description

This structure indicates the parameters specified during an `sceNpAuthGetIdTokenV3()` call.

For `size`, specify the size of this structure.

For `userId`, set the access target user's user ID.

For `clientId`, specify the client ID of the application server attempting to access the user's user information. Specify the client ID issued upon request in advance.

For `clientSecret`, specify the client secret for the application server that will be attempting to access the user information of the user. Specify the client secret issued upon request in advance.

For `scope`, specify the scope required for the user information the application server will obtain from the PlayStation™Network servers. If there is more than one item for the information to obtain, specify them by inserting a space between items as in the following example. For details about ID token scopes, refer to [Auth Web API Overview - User Authentication Using an ID Token](../../../WebAPI/latest/Auth_WebAPI-Overview/user-authentication-using-an-id-token.html).

```
"openid id_token:psn.basic_claims"
```

# sceNpAuthGetIdTokenV3

Get ID token

## Definition

```
#include <np/np_auth.h>
int sceNpAuthGetIdTokenV3(
	int reqId,
	const SceNpAuthGetIdTokenParameterV3 *param,
	SceNpIdToken *idToken
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID (IN) |
| `param` | ID token obtainment parameters (IN) |
| `idToken` | Destination to store the obtained ID token (OUT) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

If the error code is 0x82XXXXXX, it means it is a server error code. For details, refer to [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | `reqId` is not a positive number (>0), NULL was specified for `param` or `idToken`, or NULL was specified for a member of `param` |
| `SCE_NP_AUTH_ERROR_INVALID_SIZE` | 0x80550302 | `param`->`size` is invalid |
| `SCE_NP_AUTH_ERROR_OUT_OF_MEMORY` | 0x80550303 | Not enough free memory |
| `SCE_NP_AUTH_ERROR_ABORTED` | 0x80550304 | Processing aborted |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |
| `SCE_NP_AUTH_ERROR_NO_TOKEN_RECEIVED` | 0x80550308 | Token did not return from server |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | Called in the signed-out state |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user does not exist |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a state where the user is not signed up |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged-out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |

## Description

This function obtains an ID token. ID tokens are based on the OpenID Connect ID token specifications which allow token verification with signature verification formats, therefore user authentication without calling Web APIs is possible. For details, refer to [Auth Web API Overview - User Authentication Using an ID Token](../../../WebAPI/latest/Auth_WebAPI-Overview/user-authentication-using-an-id-token.html).

This function carries out synchronous or asynchronous processing depending on the request argument.

When executed as a synchronous processing, the function is blocking until communication ends and the authorization code is obtained (or an error is generated). When synchronous processing completes, call `sceNpAuthDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain results from the server. The processing result must be received using either `sceNpAuthWaitAsync()` or `sceNpAuthPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

* In order to use this function, settings for the corresponding Client ID are required to assign a scope. If they are not set, an error will be returned. Make a request on the PlayStation®5 Developer Network. For details, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).
* When this function is executed synchronously, blocking may be performed for long periods of time. This function must not be called from a time-critical thread.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`, `sceNpAuthAbortRequest()`

# SceNpAuthAccessType

Access type to PlayStation™Network

## Definition

```
#include <np/np_auth.h>
typedef enum SceNpAuthAccessType {
    SCE_NP_AUTH_ACCESS_TYPE_ONLINE = 0,
    SCE_NP_AUTH_ACCESS_TYPE_OFFLINE
} SceNpAuthAccessType;
```

## Description

Constant that shows how an Authorized App accesses user information managed by PlayStation™Network.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ACCESS_TYPE_ONLINE` | 0 | User information can be accessed only when the user is online on PlayStation™Network. |
| `SCE_NP_AUTH_ACCESS_TYPE_OFFLINE` | 1 | User information can be accessed even when the user is offline from PlayStation™Network. |

If an access token is issued using an authorization code obtained by specifying `SCE_NP_AUTH_ACCESS_TYPE_OFFLINE`, a refresh token is also issued. Using the refresh token, the access token can be updated even if the user is offline.

## See Also

`SceNpAuthGetAuthorizedAppCodeParameter`, `SceNpAuthAuthorizedAppDialogParam`

# SceNpAuthGetAuthorizedAppCodeParameter

Authorization code obtainment parameters for an Authorized App

## Definition

```
#include <np/np_auth.h>
typedef struct SceNpAuthGetAuthorizedAppCodeParameter {
    size_t size;
    SceUserServiceUserId userId;
    uint8_t padding[4];
    const SceNpClientId *authorizedAppClientId;
    const char *scope;
    SceNpAuthAccessType accessType;
    uint8_t padding2[4];
} SceNpAuthGetAuthorizedAppCodeParameter;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID |
| `padding` | Not used (clear with 0's) |
| `authorizedAppClientId` | Authorized App client ID |
| `scope` | Entitlement scope for obtaining authorization codes |
| `accessType` | Access type to be requested |
| `padding2` | Not used (clear with 0's) |

## Description

This structure represents the parameters to specify during an `sceNpAuthGetAuthorizedAppCode()` call.

For `size`, specify the size of this structure.

For `userId`, set the access target user's user ID.

`authorizedAppClientId` specifies the client ID of the Authorized App attempting to access the user's user information. Specify the client ID issued upon request in advance. Note that this is different from the client ID specified with `SceNpAuthGetAuthorizationCodeParameterV3` and `SceNpAuthGetIdTokenParameterV3`.

For `scope`, specify the entitlement scope for obtaining authorization codes. If there is more than one item for the information to obtain, specify them by inserting a space between items as in the following example.

```
"openid id_token:psn.basic_claims psn:s2s.authorizedApp"
```

Specify the PlayStation™Network access type for the Authorized App for `accessType`. For details about access types, refer to `SceNpAuthAccessType`.

# sceNpAuthGetAuthorizedAppCode

Get authorization code for an Authorized App

## Definition

```
#include <np/np_auth.h>
int sceNpAuthGetAuthorizedAppCode(
    int reqId,
    const SceNpAuthGetAuthorizedAppCodeParameter *param,
    SceNpAuthorizationCode *authCode,
    int *isserId,
    bool *consentRequiredError
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | NpAuth request ID (IN) |
| `param` | Authorization code obtainment parameters for the Authorized App (IN) |
| `authCode` | Destination to store the obtained authorization code (OUT) |
| `issuerId` | Destination to store the obtained issuer ID. NULL can be specified (OUT) |
| `consentRequiredError` | Destination to store a flag regarding whether an error that occurs requires requesting the user's consent (OUT) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

If the error code is 0x82XXXXXX, it means it is a server error code. For details, refer to [PlayStation™Network Web APIs Overview - Usage - Error Processing](../PSN_WebAPI-Overview/error-processing.html).

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_AUTH_ERROR_INVALID_ARGUMENT` | 0x80550301 | * `reqId` is not a positive number (>0) * NULL specified for `param`, `authCode`, or `consentRequiredError`. * NULL specified for the `param` member |
| `SCE_NP_AUTH_ERROR_INVALID_SIZE` | 0x80550302 | `param`->`size` is invalid |
| `SCE_NP_AUTH_ERROR_OUT_OF_MEMORY` | 0x80550303 | Not enough free memory |
| `SCE_NP_AUTH_ERROR_ABORTED` | 0x80550304 | Processing aborted |
| `SCE_NP_AUTH_ERROR_REQUEST_NOT_FOUND` | 0x80550306 | Request specified for `reqId` does not exist |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | Called in the signed-out state |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user does not exist |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a state where the user is not signed up |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged-out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |

## Description

This function obtains an authorization code for an Authorized App. Transfer the obtained authorization code and Issuer ID to the Authorized App. The Authorized App can use the authorization code to obtain the access token and access user information managed by the PlayStation™Network servers. The Issuer ID is used for identifying the PlayStation™Network environment.

`consentRequiredError` will be set to true if an error requiring user consent occurs. If that happens, call this function again after obtaining user consent using the NpAuthAuthorizedAppDialog library.

This function carries out synchronous or asynchronous processing depending on the request argument.

When executed as a synchronous processing, the function is blocking until communication ends and the authorization code is obtained (or an error is generated). When synchronous processing completes, call `sceNpAuthDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain results from the server. The processing result must be received using either `sceNpAuthWaitAsync()` or `sceNpAuthPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

When this function is executed synchronously, blocking may be performed for long periods of time. This function must not be called from a time-critical thread.

## See Also

`sceNpAuthCreateRequest()`, `sceNpAuthCreateAsyncRequest()`, `sceNpAuthAbortRequest()`