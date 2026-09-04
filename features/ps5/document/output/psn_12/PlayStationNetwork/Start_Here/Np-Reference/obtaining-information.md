# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/obtaining-information.html

# Obtaining Information

# sceNpGetAccountIdA

Gets the account ID

## Definition

```
#include <np/np_common.h>
int sceNpGetAccountIdA(
	SceUserServiceUserId userId,
	SceNpAccountId *pAccountId
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID (IN) |
| `pAccountId` | Destination to store the obtained account ID (OUT) |

## Return Values

Stores the account ID in `*pAccountId` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |

## Description

This function obtains the account ID.

# sceNpGetUserIdByAccountId

Gets the user ID from the account ID

## Definition

```
#include <np/np_common.h>
int sceNpGetUserIdByAccountId(
	SceNpAccountId accountId,
	SceUserServiceUserId *userId
);
```

## Arguments

|  |  |
| --- | --- |
| `accountId` | Account ID (IN) |
| `userId` | User ID (OUT) |

## Return Values

Stores the user ID in `*userId` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |

## Description

This function obtains the user ID (in the current console) of the user whose account ID was specified with `accountId`.

An error will occur if this function is called for a user that is not signed in, and `SCE_NP_ERROR_SIGNED_OUT` or `SCE_NP_ERROR_NOT_SIGNED_UP` will be returned.

## Example

```
int ret = 0;
SceNpAccountId accountId;
SceUserServiceUserId userId;

/* btain accountId with callback, etc. */

ret = sceNpGetUserIdByAccountId(accountId, &userId);
if (ret < 0){
	/* Error handling */
}
```

# sceNpGetOnlineId

Gets the Online ID from the user ID

## Definition

```
#include <np/np_common.h>
int sceNpGetOnlineId(
	SceUserServiceUserId userId,
	SceNpOnlineId *onlineId
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID (IN) |
| `onlineId` | Destination to store the obtained Online ID (OUT) |

## Return Values

Stores the Online ID in `*onlineId` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |

## Description

This function obtains the Online ID of the user specified with `userId`.

An error will occur if this function is called for a user that is not signed in, and `SCE_NP_ERROR_SIGNED_OUT` or `SCE_NP_ERROR_NOT_SIGNED_UP` will be returned.

## Example

```
int ret = 0;
SceUserServiceUserId userId = 0x10000000;
SceNpOnlineId onlineId;

ret = sceNpGetOnlineId(userId, &onlineId);
if (ret < 0){
	/* Error handling */
}
```

# sceNpGetAccountCountryA

Gets the country/region code

## Definition

```
#include <np/np_common.h>
int sceNpGetAccountCountryA(
	SceUserServiceUserId userId,
	SceNpCountryCode *pCountryCode
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID (IN) |
| `pCountryCode` | Destination to store the obtained country/region code (OUT) |

## Return Values

Stores the country/region code in `*pCountryCode` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_SIGNED_OUT` | 0x80550006 | The specified user was signed out |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |
| `SCE_NP_ERROR_NOT_SIGNED_UP` | 0x8055000a | Called in a non-signed up state |

## Description

This function obtains the country/region code.

# sceNpHasSignedUp

Checks if the user has signed up

## Definition

```
#include <np/np_common.h>
int sceNpHasSignedUp(
	SceUserServiceUserId userId,
	bool *hasSignedUp
);
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID (IN) |
| `hasSignedUp` | Destination to store the determination results for whether or not the user has signed up (OUT) |

## Return Values

Stores the determination results for whether or not the user has signed up in `*hasSignedUp` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ERROR_INVALID_ARGUMENT` | 0x80550003 | Argument is invalid |
| `SCE_NP_ERROR_USER_NOT_FOUND` | 0x80550007 | The specified user was not found |

## Description

This function returns the results determined regarding whether or not the user specified with `userId` has signed up.

## Example

```
int ret = 0;
SceUserServiceUserId userId = 0x10000000;
bool hasSignedUp = false;

ret = sceNpHasSignedUp(userId, &hasSignedUp);
if (ret < 0){
	/* Error handling */
}
```