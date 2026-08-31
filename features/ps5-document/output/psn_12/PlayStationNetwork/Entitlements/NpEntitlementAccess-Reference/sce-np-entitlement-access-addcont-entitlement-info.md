# NpEntitlementAccess Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Reference/sce-np-entitlement-access-addcont-entitlement-info.html

# Accessing Additional Content

# SceNpEntitlementAccessAddcontEntitlementInfo

Additional content information

## Definition

```
#include <np_entitlement_access.h>

typedef uint32_t SceNpEntitlementAccessPackageType;
typedef uint32_t SceNpEntitlementAccessDownloadStatus;

typedef struct SceNpEntitlementAccessAddcontEntitlementInfo {
	SceNpUnifiedEntitlementLabel entitlementLabel;
	SceNpEntitlementAccessPackageType packageType;
	SceNpEntitlementAccessDownloadStatus downloadStatus;
} SceNpEntitlementAccessAddcontEntitlementInfo;
```

## Members

|  |  |
| --- | --- |
| `entitlementLabel` | Unified entitlement label |
| `packageType` | Package type |
| `downloadStatus` | Download status |

## Description

This structure represents information for an instance of additional content.

When `sceNpEntitlementAccessGetAddcontEntitlementInfoList()` or `sceNpEntitlementAccessGetAddcontEntitlementInfo()` terminates normally, the entitlement label, which is an identifier of the additional content, and the package type will be stored in this structure.

For `packageType`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_NONE` | 0 | Undefined type |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSGD` | 1 | Application |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSAC` | 2 | Additional content with extra data |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSAL` | 3 | Additional content without extra data |

For `downloadStatus`, the following value will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_DOWNLOAD_STATUS_NO_EXTRA_DATA` | 0 | This additional content does not include any data to be downloaded |
| `SCE_NP_ENTITLEMENT_ACCESS_DOWNLOAD_STATUS_NO_IN_QUEUE` | 1 | There is data to be downloaded, but it has not been installed |
| `SCE_NP_ENTITLEMENT_ACCESS_DOWNLOAD_STATUS_DOWNLOADING` | 2 | There is data to be downloaded, and it is currently being downloaded |
| `SCE_NP_ENTITLEMENT_ACCESS_DOWNLOAD_STATUS_DOWNLOAD_SUSPENDED` | 3 | There is data to be downloaded, and the download is currently paused |
| `SCE_NP_ENTITLEMENT_ACCESS_DOWNLOAD_STATUS_INSTALLED` | 4 | There is data to be downloaded, and installation is complete |

# SceNpEntitlementAccessEntitlementKey

Entitlement key

## Definition

```
#include <np_entitlement_access.h>
#define SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_KEY_SIZE (16)

typedef struct SceNpEntitlementAccessEntitlementKey {
	char data[ SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_KEY_SIZE ];
} SceNpEntitlementAccessEntitlementKey;
```

## Members

|  |  |
| --- | --- |
| `data` | Entitlement key |

## Description

This structure represents an entitlement key. Use it when obtaining an entitlement key with `sceNpEntitlementAccessGetEntitlementKey()`.

# sceNpEntitlementAccessGetAddcontEntitlementInfo

Gets additional content information

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessGetAddcontEntitlementInfo(
	SceNpServiceLabel serviceLabel,
	const SceNpUnifiedEntitlementLabel *entitlementLabel,
	SceNpEntitlementAccessAddcontEntitlementInfo *info
)
```

## Arguments

|  |  |
| --- | --- |
| `serviceLabel` | NP service label |
| `entitlementLabel` | Unified entitlement label of the target additional content |
| `info` | Destination to store the obtained additional content information |

## Return Values

Stores the obtained additional content information in `*info` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NO_ENTITLEMENT` | 0x817D0007 | Entitlement of the additional content is invalid |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |

## Description

This function obtains information about the additional content specified in `entitlementLabel`. If NULL is specified for `entitlementLabel`, a parameter error will occur.

For `serviceLabel`, specify the NP service label of the additional content. Specify 0 when the additional content is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

When this function call is successful, the obtained additional content information will be stored in `*info`. If NULL is specified for `info`, a parameter error will occur.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpUnifiedEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "0000111122223333", SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE);
SceNpEntitlementAccessAddcontEntitlementInfo info;

/* Obtain additional content information */
ret = sceNpEntitlementAccessGetAddcontEntitlementInfo(serviceLabel, &entitlementLabel, &info);
if(ret != SCE_OK){
    // Error handling
}
```

## Notes

This is a blocking function. Call this function from a subthread, as processing may take time.

## See Also

`SceNpServiceLabel` (in the [Np Library Reference](../Np-Reference/__document_toc.html) document)

# sceNpEntitlementAccessGetAddcontEntitlementInfoList

Gets a list of additional content information for which the entitlement is valid

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessGetAddcontEntitlementInfoList(
	SceNpServiceLabel serviceLabel,
	SceNpEntitlementAccessAddcontEntitlementInfo *list,
	uint32_t listNum,
	uint32_t *hitNum
)
```

## Arguments

|  |  |
| --- | --- |
| `serviceLabel` | NP service label |
| `list` | Array to store the obtained additional content information, or NULL |
| `listNum` | Number of elements in `list` |
| `hitNum` | Destination to store the total number of additional content for which the entitlement is valid |

## Return Values

Stores the obtained additional content information in `*list`, the total number of additional content for which the entitlement is valid in `*hitNum` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |

## Description

This function obtains a list of additional content information for which the entitlement is valid.

For `serviceLabel`, specify the NP service label of the additional content. Specify 0 when the additional content is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

For `list` and `listNum`, specify the array for storing the obtained additional content information and its size. If the number of additional content for which the entitlement is valid is greater than the value of `listNum`, the obtainment of additional content information will be stopped when `listNum` pieces of information are obtained, and the total number of additional content for which the entitlement is valid, including those for which no information was obtained, will be stored in `*hitNum`.

If NULL is specified for `list`, only the number of additional content for which the entitlement is valid will be obtained.

## Examples

```
/* Obtain the number of additional content information for which the entitlement is valid */
SceNpServiceLabel serviceLabel = 0; 
SceNpEntitlementAccessAddcontEntitlementInfo *list = NULL; // If NULL is specified, only the number can be obtained
uint32_t	listNum = 0;
uint32_t	hitNum;
ret = sceNpEntitlementAccessGetAddcontEntitlementInfoList(serviceLabel, list, listNum, &hitNum);

/* Prepare required buffers */
list = (SceNpEntitlementAccessAddcontEntitlementInfo *)malloc(sizeof(SceNpEntitlementAccessAddcontEntitlementInfo) * hitNum);
listNum = hitNum;

/* Obtain a list of additional content information for which the entitlement is valid */
ret = sceNpEntitlementAccessGetAddcontEntitlementInfoList(serviceLabel, list, listNum, &hitNum);
```

## Notes

This is a blocking function. Call this function from a subthread, as processing may take time.

## See Also

`SceNpServiceLabel` (in the [Np Library Reference](../Np-Reference/__document_toc.html) document)

# sceNpEntitlementAccessGetEntitlementKey

Gets the entitlement key of additional content

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessGetEntitlementKey(
	SceNpServiceLabel serviceLabel,
	const SceNpUnifiedEntitlementLabel *entitlementLabel,
	SceNpEntitlementAccessEntitlementKey *key
)
```

## Arguments

|  |  |
| --- | --- |
| `serviceLabel` | NP service label |
| `entitlementLabel` | Unified entitlement label of the target additional content |
| `key` | Destination to store the obtained entitlement key |

## Return Values

Stores the obtained entitlement key in `*key` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NO_ENTITLEMENT` | 0x817D0007 | Entitlement of the additional content is invalid |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |

## Description

This function obtains the entitlement key of additional content.

For `serviceLabel`, specify the NP service label of the additional content. Specify 0 when the additional content is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

When this function call is successful, the entitlement key will be stored in `*key`. If NULL is specified for `key`, a parameter error will occur.

Refer to [NpEntitlementAccess Library Overview - Using the Library: Additional Content - Usage of an Entitlement Key](../NpEntitlementAccess-Overview/usage-of-an-entitlement-key.html) for usage of entitlement keys and how to create them.

## Examples

```
SceNpServiceLabel serviceLabel = 0; 
SceNpUnifiedEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "0000111122223333", SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE);
SceNpEntitlementAccessEntitlementKey key;

/* Obtain the entitlement key of additional content */
ret = sceNpEntitlementAccessGetEntitlementKey(serviceLabel, &entitlementLabel, &key);
if(ret != SCE_OK){
    // Error handling
}
```

## Notes

This is a blocking function. Call this function from a subthread, as processing may take time.