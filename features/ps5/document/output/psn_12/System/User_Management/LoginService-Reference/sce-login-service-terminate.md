# LoginService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginService-Reference/sce-login-service-terminate.html

# Initialization/Termination

# sceLoginServiceInitialize

Initialize the LoginService library

## Definition

```
#include <login_service.h>
int32_t sceLoginServiceInitialize()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_SERVICE_ERROR_ALREADY_INITIALIZED` | 0x813A0002 | LoginService library is already initialized |

## Description

This function initializes the LoginService library.

When the LoginService library is called by another function when it is in an uninitialized state, the `SCE_LOGIN_SERVICE_ERROR_NOT_INITIALIZED` error will be returned.

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.

## See Also

`sceLoginServiceTerminate()`

# sceLoginServiceTerminate

Terminate the LoginService library

## Definition

```
#include <login_service.h>
int32_t sceLoginServiceTerminate()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns the following error code (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_LOGIN_SERVICE_ERROR_NOT_INITIALIZED` | 0x813A0001 | LoginService library is not initialized |

## Description

This function terminates the LoginService library.

After initializing the LoginService library with `sceLoginServiceInitialize()`, this function must ultimately be called to terminate the library.

## Notes

This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, subsequent library operation cannot be guaranteed. Make sure to program the application so that this function is not called at the same time by multiple threads.