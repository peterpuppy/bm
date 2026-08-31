# NpAuthAuthorizedAppDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuthAuthorizedAppDialog-Reference/parameter-settings.html

# Parameter Settings

# SceNpAuthAuthorizedAppDialogParam

NpAuth Authorized App dialog parameters

## Definition

```
#include <np_auth_authorized_app_dialog.h>
typedef struct SceNpAuthAuthorizedAppDialogParam {
    SceCommonDialogBaseParam baseParam;
    size_t size;
    SceUserServiceUserId userId;
    int : 32;
    const SceNpClientId* authorizedAppClientId;
    const char* scope;
    SceNpAuthAccessType accessType;
    int : 32;
    uint8_t reserved[32];
} SceNpAuthAuthorizedAppDialogParam;
```

## Members

|  |  |
| --- | --- |
| `baseParam` | Common dialog shared parameters |
| `size` | Size of the structure |
| `userId` | User ID |
| `authorizedAppClientId` | Authorized App client ID |
| `scope` | Entitlement scope for obtaining authorization codes |
| `accessType` | Access type to request |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure is for specifying dialog parameters when displaying the NpAuth Authorized App dialog with `sceNpAuthAuthorizedAppDialogOpen()`. After initializing this structure in advance with `sceNpAuthAuthorizedAppDialogParamInit()`, set appropriate values to the necessary members.

`baseParam` specifies common dialog shared parameters sizes, and `size` specifies structure sizes. However, because appropriate values are stored when an instance of the structure is initialized using `sceNpAuthAuthorizedAppDialogParamInit()`, it is not necessary to specify these members explicitly within your program.

For `userId`, specify the user ID of the target user from whom consent is to be requested. The user ID can be obtained using the UserService library API, among other means.

For `authorizedAppClientId`, specify the client ID of the Authorized App that is trying to access the user information for that user. Specify the client ID issued upon request in advance.

For `scope`, specify the scope required for the user information the Authorized App will obtain from the PlayStation™ Network servers. If there is more than one item of information that must be obtained, specify them by inserting a space between items as in the following example.

```
"openid id_token:psn.basic_claims psn:s2s.authorizedApp"
```

For `accessType`, specify the access type for the Authorized App PlayStation™ Network. For details, refer to `SceNpAuthAccessType`.

For `userId`, `authorizedAppClientId`, `scope`, and `accessType`, specify the same values as those of the `SceNpAuthGetAuthorizedAppCodeParameter` that was specified when calling `sceNpAuthGetAuthorizedAppCode()`.

# sceNpAuthAuthorizedAppDialogParamInit

Initialize NpAuth Authorized App dialog parameters

## Definition

```
#include <np_auth_authorized_app_dialog.h>
void sceNpAuthAuthorizedAppDialogParamInit(
SceNpAuthAuthorizedAppDialogParam *param
);
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters to be initialized |

## Return Values

None

## Description

This function initializes NpAuth Authorized App dialog parameters.

Be sure to use this function to initialize the structure before setting the various parameters. Calling this function sets the appropriate default value for each member of `*param`, so the application does not need to explicitly set a value for any unused members, such as the reserved area.

For details about each parameter, refer to `SceNpAuthAuthorizedAppDialogParam`.