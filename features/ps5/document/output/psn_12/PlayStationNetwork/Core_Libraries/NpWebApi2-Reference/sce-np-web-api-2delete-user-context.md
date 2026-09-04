# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2delete-user-context.html

# User Context Operation

# sceNpWebApi2CreateUserContext

Create user context

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2CreateUserContext(
	int32_t libCtxId,
	SceUserServiceUserId userId
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `userId` | User ID of the user accessing PlayStation™Network Web APIs |

## Return Values

Returns the user context ID (positive value) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function creates the user context for the user accessing the PlayStation™Network Web APIs ("Web APIs" hereafter). In order to use this function, the user ID of the user must be obtained in advance.

## Examples

```
int32_t ret = 0;
SceUserServiceUserId userId; // Obtain in advance, for example by using sceUserServiceGetInitialUser()
int32_t userCtxId = 0;

ret = sceNpWebApi2CreateUserContext(libCtxId, userId);
if(ret < 0){
	/* Error handling */
}
userCtxId = ret;
```

## See Also

`sceNpWebApi2DeleteUserContext()`

# sceNpWebApi2DeleteUserContext

Delete user context

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2DeleteUserContext(
	int32_t userCtxId
);
```

## Arguments

|  |  |
| --- | --- |
| `userCtxId` | User context ID |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function deletes a user context.

If the user context is being used for sending/receiving data, `SCE_NP_WEBAPI2_ERROR_USER_CONTEXT_BUSY` will be returned. Execute this function after all processing completes.

## Examples

```
int32_t ret = 0;
int32_t userCtxId;

ret = sceNpWebApi2DeleteUserContext(userCtxId);
if(ret < 0){
	/* Error handling */
}
```

## See Also

`sceNpWebApi2CreateUserContext()`