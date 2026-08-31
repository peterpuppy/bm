# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/sce-np-check-premium-parameter.html

# Communication Processing

# sceNpGetAccountLanguage2

Gets the language code

## Definition

```
#include <np.h>
int sceNpGetAccountLanguage2(
	int reqId,
	SceUserServiceUserId userId,
	SceNpLanguageCode2 *pLangCode
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID (IN) |
| `userId` | User ID (IN) |
| `pLangCode` | Destination to store the obtained language code (OUT) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0), or NULL was specified to `userId` or `pLangCode` |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |
| `SCE_NP_ERROR_ABORTED` | 0x80550012 | Processing was aborted |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function obtains the language code of the language used by the specified user.

This function carries out synchronous or asynchronous processing depending on the request argument.

When executed as a synchronous processing, the function is blocking until communication ends and the language code is obtained. When synchronous processing completes, call `sceNpDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain the result from the server. Processing result must be obtained using `sceNpWaitAsync()` or `sceNpPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

When this function is executed as a synchronous processing, a long blocking time may be entailed. This function must not be called from a time-critical thread.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`, `sceNpAbortRequest()`

# sceNpGetAccountAge

Obtains the age

## Definition

```
#include <np.h>
int sceNpGetAccountAge(
	int reqId,
	SceUserServiceUserId userId,
	uint8_t *age,
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID (IN) |
| `userId` | User ID (IN) |
| `age` | Destination to store the obtained age (OUT) |

## Return Values

Stores the user's age in `*age` and returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0), or NULL was specified to `userId` or `age` |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |
| `SCE_NP_ERROR_ABORTED` | 0x80550012 | Processing was aborted |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function obtains the age of the specified user.

This function carries out synchronous or asynchronous processing depending on the request argument.

When executed as a synchronous processing, the function will block until the result is obtained. Once synchronous processing completes, call `sceNpDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain the result. Processing result must be obtained using `sceNpWaitAsync()` or `sceNpPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

When this function is executed as a synchronous processing, a long blocking time may be entailed. This function must not be called from a time-critical thread.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`, `sceNpAbortRequest()`

# sceNpCheckNpReachability

Checks PlayStation™Network reachability

## Definition

```
#include <np.h>
int sceNpCheckNpReachability(
	int reqId,
	SceUserServiceUserId userId
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID (IN) |
| `userId` | User ID (IN) |

## Return Values

Returns 0 in the case of normal termination with the application reachable PlayStation™Network.

If the application must not use network features, cannot connect to the servers of PlayStation™Network, or a network error has occurred, a negative value will be returned. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0) or `userId` is invalid |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |
| `SCE_NP_ERROR_ABORTED` | 0x80550012 | Processing was aborted |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |
| `SCE_NP_ERROR_TIMEOUT` | 0x8055001a | Timed out |
| `SCE_NP_PUSH_ERROR_NETWORK_NOT_AVAILABLE` | 0x8055a02a | Network is not available (It takes some time for the system software to detect this error even after WAN-side connectivity has, in fact, been lost) |

## Description

This function obtains whether or not an application can reach PlayStation™Network.

The system software is constantly checking the connectivity to PlayStation™Network. Therefore, whether or not PlayStation™Network is reachable will be automatically checked without calling this function.

Use this function only in situations where it is desired to explicitly and immediately check the reachability of PlayStation™Network by the application, such as immediately before transitions to an online multiplayer mode.

This function carries out synchronous or asynchronous processing depending on the request argument.

When executed as a synchronous processing, communication will stop, and blocking will be performed until whether the PlayStation™Network is reachable can be checked. When synchronous processing completes, call `sceNpDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain the result from the server. Processing result must be obtained using `sceNpWaitAsync()` or `sceNpPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

* Do not implement this function so that it is called at regular intervals. To monitor PlayStation™Network reachability states in cases such as when it is desired to detect disconnection from PlayStation™Network during an online multiplayer mode, use `sceNpGetNpReachabilityState()` or a callback function (which can be registered with `sceNpRegisterNpReachabilityStateCallback()`) to obtain the current reachability state.
* When this function is executed as a synchronous processing, a long blocking time may be entailed. This function must not be called from a time-critical thread.
* This function can check reachability inclusive of WAN connectivity. However, it takes a certain amount of time until the system software detects a loss of WAN connectivity. Thus, the function returns 0 immediately after a connection has, in fact, been lost.

## See Also

`sceNpCreateRequest()`, `sceNpCreateAsyncRequest()`, `sceNpAbortRequest()`

# SceNpCheckPremiumParameter

Parameters for checking eligibility to use a Premium feature

## Definition

```
#include <np/np_common.h>
typedef struct SceNpCheckPremiumParameter {
	size_t size;
	SceUserServiceUserId userId;
	char padding[4];
	uint64_t features;
	uint8_t reserved[32];
} SceNpCheckPremiumParameter;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `userId` | User ID |
| `padding` | Not used (clear with 0's) |
| `features` | Premium feature type |
| `reserved` | Not used (clear with 0's) |

## Description

This structure represents the parameters to specify upon calling `sceNpCheckPremium()`.

For `size`, specify the size of this structure.

For `features`, specify the value of the Premium feature type as a bit flag. Refer to the "[SCE\_NP\_PREMIUM\_FEATURE](scenppremiumfeature.html)" section for details.

Clear `padding` and `reserved` with 0's.

# SceNpCheckPremiumResult

Result of checking eligibility to use a Premium feature

## Definition

```
#include <np/np_common.h>
typedef struct SceNpCheckPremiumResult {
	bool authorized;
	uint8_t reserved[32];
} SceNpCheckPremiumResult;
```

## Members

|  |  |
| --- | --- |
| `authorized` | Result of checking eligibility to use a Premium feature |
| `reserved` | Not used |

## Description

This structure stores the result of the `sceNpCheckPremium()` call.

For `authorized`, the result of checking eligibility to use a Premium feature will be stored. If this is a true value, it means the Premium feature specified upon call of `sceNpCheckPremium()` can be used.

# sceNpCheckPremium

Checks eligibility to use a Premium feature

## Definition

```
#include <np.h>
int sceNpCheckPremium(
	int reqId,
	const SceNpCheckPremiumParameter *param,
	SceNpCheckPremiumResult *result
);
```

## Arguments

|  |  |
| --- | --- |
| `reqId` | Request ID (IN) |
| `param` | Parameters for checking eligibility to use a Premium feature (IN) |
| `result` | Result of checking eligibility to use a Premium feature (OUT) |

## Return Values

Returns 0 for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | `reqId` is not a positive number (>0), or NULL was specified to `param` or `result` |
| `SCE_NP_ERROR_OUT_OF_MEMORY` | 0x80550005 | Insufficient memory |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |
| `SCE_NP_ERROR_LOGOUT` | 0x8055000c | Called in a logged out state |
| `SCE_NP_ERROR_LATEST_SYSTEM_SOFTWARE_EXIST` | 0x8055000d | A new version of the system software update file exists |
| `SCE_NP_ERROR_ABORTED` | 0x80550012 | Processing was aborted |
| `SCE_NP_ERROR_REQUEST_NOT_FOUND` | 0x80550014 | Request specified for `reqId` does not exist |

## Description

This function performs a Premium check to see if the user has the eligibility to use the applicable Premium feature.

An application must perform a Premium check before executing a Premium feature to ensure the user has the eligibility to use the feature. Refer to the [Premium Features Guidelines](../Premium_Features_Guidelines/__document_toc.html) document regarding when and how often this function should be called.

Create the request ID (`reqId`) using `sceNpCreateRequest()` or `sceNpCreateAsyncRequest()`. This function will perform synchronous processing or asynchronous processing depending on the `reqId` argument.

When executed as a synchronous processing, this function will block until communication is completed and eligibility to use the Premium feature is confirmed. Once synchronous processing completes, call `sceNpDeleteRequest()` and delete the used request.

When executed as an asynchronous processing, the function returns after starting the request without waiting to obtain the result from the server. Processing result must be obtained using `sceNpWaitAsync()` or `sceNpPollAsync()`. After receiving the result with one of these functions, delete the request.

## Notes

* This function determines whether or not the user has the eligibility to use a Premium feature; it cannot be used to determine whether or not the user is a member of the PlayStation®Plus service. A user who is not a member of the PlayStation®Plus service can be given eligibility to use a Premium feature; in such cases, this function will return the result that the user has eligibility.

  Be careful not to broadly interpret the result returned by this function.
* When this function is executed as a synchronous processing, a long blocking time may be entailed. This function must not be called from a time-critical thread.

## See Also

`sceNpAbortRequest()`