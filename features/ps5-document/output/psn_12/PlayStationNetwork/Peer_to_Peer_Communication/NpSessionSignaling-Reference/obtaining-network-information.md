# NpSessionSignaling Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Reference/obtaining-network-information.html

# Obtaining Network Information

# SceNpSessionSignalingNetInfo

Network information

## Definition

```
#include <np.h>
typedef struct SceNpSessionSignalingNetInfo {
    size_t size;
    SceNetInAddr localAddr;
    SceNetInAddr mappedAddr;
    int natStatus;
    int stunStatus;
} SceNpSessionSignalingNetInfo;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `localAddr` | Local IP address |
| `mappedAddr` | External IP address |
| `natStatus` | NAT status type |
| `stunStatus` | STUN status |

## Description

This structure represents network information. A variable of this type is used when obtaining network information with `sceNpSessionSignalingGetLocalNetInfo()`.

For `size`, specify the size of this structure before use.

One of the following values will be stored in `natStatus`.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_NETINFO_NAT_STATUS_UNKNOWN` | 0 | Unknown |
| `SCE_NP_SESSION_SIGNALING_NETINFO_NAT_STATUS_TYPE1` | 1 | Type 1 |
| `SCE_NP_SESSION_SIGNALING_NETINFO_NAT_STATUS_TYPE2` | 2 | Type 2 |
| `SCE_NP_SESSION_SIGNALING_NETINFO_NAT_STATUS_TYPE3` | 3 | Type 3 |

One of the following values will be stored in `stunStatus`.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_NETINFO_STUN_STATUS_UNCHECKED` | 0 | STUN hasn't completed yet |
| `SCE_NP_SESSION_SIGNALING_NETINFO_STUN_STATUS_FAILED` | 1 | STUN failed |
| `SCE_NP_SESSION_SIGNALING_NETINFO_STUN_STATUS_OK` | 2 | STUN succeeded |

# sceNpSessionSignalingGetLocalNetInfo

Gets the user's own network information

## Definition

```
#include <np.h>
int sceNpSessionSignalingGetLocalNetInfo(
    SceNpSessionSignalingContextId ctxId,
    SceNpSessionSignalingNetInfo *info
)
```

## Arguments

|  |  |
| --- | --- |
| `ctxId` | Context ID |
| `info` | Destination to store the obtained network information |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. Note, however, that the application must not malfunction even if other error codes are returned.

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_SESSION_SIGNALING_ERROR_NOT_INITIALIZED` | 0x80553301 | Not initialized.  `sceNpSessionSignalingInitialize()` may not have been called yet. Check the calling order |
| `SCE_NP_SESSION_SIGNALING_ERROR_INVALID_ARGUMENT` | 0x80553303 | Invalid argument   * `info` is NULL * Incorrect value is specified to the `size` member of the `SceNpSessionSignalingNetInfo` structure |

## Description

This function obtains the user's own network information.

## Examples

```
// Assuming that appropriate values are stored
SceNpSessionSignalingContextId ctxId;

int ret;
SceNpSessionSignalingNetInfo info;
info.size = sizeof(info);

ret = sceNpSessionSignalingGetLocalNetInfo(ctxId, &info);
if ( ret < 0 ) {
    // Error handling
}
```

## Notes

An error will not occur even if STUN hasn't completed yet or if STUN failed. This function will store `SCE_NP_SESSION_SIGNALING_NETINFO_STUN_STATUS_UNCHECKED` or `SCE_NP_SESSION_SIGNALING_NETINFO_STUN_STATUS_FAILED` to `info->stunStatus`, `SCE_NET_INADDR_ANY` to `info->mappedAddr`, `SCE_NP_SESSION_SIGNALING_NETINFO_NAT_STATUS_UNKNOWN` to `info->natStatus`, and return `SCE_OK`.