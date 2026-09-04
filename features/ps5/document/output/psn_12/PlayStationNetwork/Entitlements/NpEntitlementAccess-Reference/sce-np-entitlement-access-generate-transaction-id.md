# NpEntitlementAccess Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Reference/sce-np-entitlement-access-generate-transaction-id.html

# Accessing Entitlements

# SceNpEntitlementAccessUnifiedEntitlementInfo

Unified entitlement information

## Definition

```
#include <np_entitlement_access.h>

typedef uint32_t SceNpEntitlementAccessEntitlementType;
typedef uint32_t SceNpEntitlementAccessPackageType;

typedef struct SceNpEntitlementAccessUnifiedEntitlementInfo {
	SceNpUnifiedEntitlementLabel entitlementLabel;
	SceRtcTick activeDate;
	SceRtcTick inactiveDate;
	SceNpEntitlementAccessEntitlementType entitlementType;
	int32_t useCount;
	int32_t useLimit;
	SceNpEntitlementAccessPackageType packageType;
	bool activeFlag;
	int8_t reserved[3];
} SceNpEntitlementAccessUnifiedEntitlementInfo;
```

## Members

|  |  |
| --- | --- |
| `entitlementLabel` | Unified entitlement label |
| `activeDate` | Start date |
| `inactiveDate` | End date |
| `entitlementType` | Entitlement type |
| `useCount` | Number of consumed entitlement counts |
| `useLimit` | Number of remaining entitlement counts that can be consumed |
| `packageType` | Package type |
| `activeFlag` | Active flag |
| `reserved` | Reserved area (fill with 0's) |

## Description

This structure represents information of a unified entitlement. It is used when information of a unified entitlement is obtained with `sceNpEntitlementAccessPollUnifiedEntitlementInfo()`.

For `entitlementType`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_NONE` | 0 | Undefined type |
| `SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_UNIFIED` | 2 | Unified entitlement |

For `packageType`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_NONE` | 0 | Undefined type |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSCONS` | 4 | Consumable |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSVC` | 5 | In-game currency |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSSUBS` | 6 | Subscription |

# SceNpEntitlementAccessRequestEntitlementInfoListParam

Parameters for obtaining a list of entitlement information

## Definition

```
#include <np_entitlement_access.h>

typedef uint32_t SceNpEntitlementAccessSortType;
typedef uint32_t SceNpEntitlementAccessDirectionType;
typedef uint32_t SceNpEntitlementAccessPackageType;

typedef struct SceNpEntitlementAccessRequestEntitlementInfoListParam {
	size_t size;
	SceNpEntitlementAccessEntitlementType entitlementType;
	int32_t offset;
	int32_t limit;
	SceNpEntitlementAccessSortType sort;
	SceNpEntitlementAccessDirectionType direction;
	SceNpEntitlementAccessPackageType packageType;
} SceNpEntitlementAccessRequestEntitlementInfoListParam;
```

## Members

|  |  |
| --- | --- |
| `size` | Size of this structure |
| `entitlementType` | Entitlement type |
| `offset` | Index (starting from 0) to a set of paged results. Responses start from the results at the specified offset. Result sets can be paged by using "offset" and "limit" in combination |
| `limit` | Specifies the maximum number of results that are returned   * Minimum value: 1 * Maximum value: 100 (`SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_INFO_LIST_MAX_SIZE`) |
| `sort` | If specified, specifies the field by which to sort results. |
| `direction` | If specified, specifies the sorting order. |
| `packageType` | Package type obtained |

## Description

This structure represents parameters for obtaining a list of unified entitlement information. It is used when using `sceNpEntitlementAccessRequestUnifiedEntitlementInfoList()` or `sceNpEntitlementAccessRequestServiceEntitlementInfoList()` to obtain a list of entitlement information.

For `entitlementType`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_SERVICE` | 1 | Service entitlement |
| `SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_UNIFIED` | 2 | Unified entitlement |

For `packageType`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_NONE` | 0 | Undefined type  Specify this in the case of a service entitlement, because such entitlements do not have a package type |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSCONS` | 4 | Consumable |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSVC` | 5 | In-game currency |
| `SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSSUBS` | 6 | Subscription |

For `sort`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_SORT_TYPE_NONE` | 0 | No specification |
| `SCE_NP_ENTITLEMENT_ACCESS_SORT_TYPE_ACTIVE_DATE` | 1 | Sorting by `activeDate` |

For `direction`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_DIRECTION_TYPE_NONE` | 0 | No specification |
| `SCE_NP_ENTITLEMENT_ACCESS_DIRECTION_TYPE_ASC` | 1 | Ascending order |
| `SCE_NP_ENTITLEMENT_ACCESS_DIRECTION_TYPE_DESC` | 2 | Descending order |

# SceNpEntitlementAccessServiceEntitlementInfo

Service entitlement information

## Definition

```
#include <np_entitlement_access.h>

typedef uint32_t SceNpEntitlementAccessEntitlementType;

typedef struct SceNpEntitlementAccessServiceEntitlementInfo {
	SceNpServiceEntitlementLabel entitlementLabel;
	SceRtcTick activeDate;
	SceRtcTick inactiveDate;
	SceNpEntitlementAccessEntitlementType entitlementType;
	int32_t useCount;
	int32_t useLimit;
	int32_t reserved1;
	bool activeFlag;
	bool isConsumable;
	int8_t reserved2[2];
} SceNpEntitlementAccessServiceEntitlementInfo;
```

## Members

|  |  |
| --- | --- |
| `entitlementLabel` | Service entitlement label |
| `activeDate` | Start date |
| `inactiveDate` | End date |
| `entitlementType` | Entitlement type |
| `useCount` | Number of consumed entitlement counts |
| `useLimit` | Number of remaining entitlement counts that can be consumed |
| `reserved1` | Reserved area (fill with 0's) |
| `activeFlag` | Active flag |
| `isConsumable` | Whether the service entitlement is consumable |
| `reserved2` | Reserved area (fill with 0's) |

## Description

This structure represents information of a service entitlement. It is used when information of a service entitlement is obtained with `sceNpEntitlementAccessPollServiceEntitlementInfo()`.

For `entitlementType`, one of the following values will be stored.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_NONE` | 0 | Undefined type |
| `SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_SERVICE` | 1 | Service entitlement |

# SceNpEntitlementAccessTransactionId

Transaction ID

## Definition

```
#include <np_entitlement_access.h>
#define SCE_NP_ENTITLEMENT_ACCESS_TRANSACTION_ID_MAX_SIZE (65)

typedef struct SceNpEntitlementAccessTransactionId {
	char transactionId[SCE_NP_ENTITLEMENT_ACCESS_TRANSACTION_ID_MAX_SIZE];
	char padding[7];
} SceNpEntitlementAccessTransactionId;
```

## Members

|  |  |
| --- | --- |
| `transactionId` | Transaction ID |
| `padding` | Padding area (fill with 0's) |

## Description

This structure represents a transaction ID that is used upon requesting to consume a consumable entitlement.

A transaction ID will be stored in this structure when `sceNpEntitlementAccessGenerateTransactionId()` terminates normally.

# sceNpEntitlementAccessAbortRequest

Aborts a request for an entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessAbortRequest(
	int64_t requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to abort |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function aborts the following requests:

* `sceNpEntitlementAccessRequestConsumeUnifiedEntitlement()`
* `sceNpEntitlementAccessRequestConsumeServiceEntitlement()`
* `sceNpEntitlementAccessRequestUnifiedEntitlementInfo()`
* `sceNpEntitlementAccessRequestServiceEntitlementInfo()`
* `sceNpEntitlementAccessRequestUnifiedEntitlementInfoList()`
* `sceNpEntitlementAccessRequestServiceEntitlementInfoList()`

For `requestId`, specify the request ID of the request you want to abort.

## Examples

```
/* Abort the request for an entitlement */
ret = sceNpEntitlementAccessAbortRequest(requestId);
```

# sceNpEntitlementAccessDeleteRequest

Deletes a request for an entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessDeleteRequest(
	int64_t requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to delete |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function deletes a request used by the library.

For `requestId`, specify the request ID of the request you want to delete.

## Notes

When asynchronous processing is being executed and this function is called in an attempt to delete a request before processing completes, blocking may be performed for long periods of time in order to abort the processing. If asynchronous processing has been executed, this function must not be called from a time-critical thread.

## Examples

```
/* Delete the request for an entitlement */
ret = sceNpEntitlementAccessDeleteRequest(requestId);
```

## See Also

`sceNpEntitlementAccessRequestConsumeUnifiedEntitlement()`, `sceNpEntitlementAccessRequestConsumeServiceEntitlement()`, `sceNpEntitlementAccessRequestUnifiedEntitlementInfo()`, `sceNpEntitlementAccessRequestServiceEntitlementInfo()`, `sceNpEntitlementAccessRequestUnifiedEntitlementInfoList()`, `sceNpEntitlementAccessRequestServiceEntitlementInfoList()`

# sceNpEntitlementAccessGenerateTransactionId

Generates a transaction ID

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessGenerateTransactionId(
	SceNpEntitlementAccessTransactionId *transactionId
)
```

## Arguments

|  |  |
| --- | --- |
| `transactionId` | Destination to store the generated transaction ID |

## Return Values

Stores the generated transaction ID in `*transactionId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |

## Description

This function generates a transaction ID that is used upon requesting to consume a consumable entitlement. If NULL is specified for `transactionId`, a parameter error will occur.

## Examples

```
SceNpEntitlementAccessTransactionId transactionId;
memset(&transactionId, 0, sizeof(transactionId));

/* Generate a transaction ID */
ret = sceNpEntitlementAccessGenerateTransactionId(&transactionId);
```

# sceNpEntitlementAccessPollUnifiedEntitlementInfo

Obtains the result of a request to obtain information of a unified entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessPollUnifiedEntitlementInfo(
	int64_t requestId,
	int32_t *pResult,
	SceNpEntitlementAccessUnifiedEntitlementInfo *info
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to obtain the result for |
| `pResult` | Destination to store the result of the request |
| `info` | Destination to store entitlement information |

## Return Values

Returns one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` | 0 | Request completed |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` | 1 | Request is still being executed |

Stores `SCE_OK` (=0) or an error code (negative value, refer to the "[Return Codes](return-codes.html)" section for details) in `*pResult` if the request has completed.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function obtains the execution result of a request executed with `sceNpEntitlementAccessRequestUnifiedEntitlementInfo()`.

For `requestId`, specify the request ID obtained with `sceNpEntitlementAccessRequestUnifiedEntitlementInfo()`.

`SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned as the return value if the request has not completed yet. The value of `*pResult` will not change in such cases.

The result of the request will be stored in `*pResult`, entitlement information will be stored in `*info`, and `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` will be returned as the return value if the request has completed. Make sure that the `*pResult` value is appropriately evaluated as a request execution result. If the `*pResult` value is 0x817D1XXX, it means a server error code. For details, refer to the "[Return Codes](return-codes.html)" section.

## Examples

```
SceNpEntitlementAccessUnifiedEntitlementInfo info;
int32_t result;

/* Obtain the result of a request to obtain information of a unified entitlement */
ret = sceNpEntitlementAccessPollUnifiedEntitlementInfo(requestId, &result, &info);
```

# sceNpEntitlementAccessPollUnifiedEntitlementInfoList

Obtain the results of a request to obtain a list of unified entitlement information

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessPollUnifiedEntitlementInfoList(
	int64_t requestId,
	int32_t *pResult,
	SceNpEntitlementAccessUnifiedEntitlementInfo *list,
	uint32_t listNum,
	uint32_t *hitNum,
	int32_t *nextOffset,
	int32_t *previousOffset
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to obtain the result for |
| `pResult` | Destination to store the result of the request |
| `list` | Destination to store the list of obtained entitlement information |
| `listNum` | Number of elements in `list` |
| `hitNum` | Destination to store the total number of valid entitlement information entries |
| `nextOffset` | Offset value for obtaining the next paged set of entitlements passed to succeeding requests.  If there is no applicable offset value, this argument will be `-1(SCE_NP_ENTITLEMENT_ACCESS_INVALID_OFFSET)`. |
| `previousOffset` | Offset value for obtaining the previous paged set of entitlements passed to succeeding requests.  If there is no applicable offset value, this argument will be `-1(SCE_NP_ENTITLEMENT_ACCESS_INVALID_OFFSET)`. |

## Return Values

Returns one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` | 0 | Request completed |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` | 1 | Request is still being executed |

Stores `SCE_OK` (=0) or an error code (negative value, refer to the "[Return Codes](return-codes.html)" section for details) in `*pResult` if the request has completed.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function obtains the execution result of a request executed with `sceNpEntitlementAccessRequestUnifiedEntitlementInfoList()`.

For `requestId`, specify the request ID obtained with `sceNpEntitlementAccessRequestUnifiedEntitlementInfoList()`.

`SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned as the return value if the request has not completed yet. The value of `*pResult` will not change in such cases.

The result of the request will be stored in `*pResult`, entitlement information will be stored in `*list`, `*hitNum`, `*nextOffet`, `*previousOffset`, and `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` will be returned as the return value if the request has completed. Make sure that the `*pResult` value is appropriately evaluated as a request execution result. If the `*pResult` value is 0x817D1XXX, it means a server error code. For details, refer to the "[Return Codes](return-codes.html)" section.

## Examples

```
SceNpEntitlementAccessUnifiedEntitlementInfo list[100];
int32_t result;
uint32_t hitNum;
int32_t nextOffset;
int32_t previousOffset;

/* Obtain the results of a request to obtain a list of unified entitlement information */
ret = sceNpEntitlementAccessPollUnifiedEntitlementInfoList(requestId, &result, list, 100, &hitNum, &nextOffset, &previousOffset);
```

# sceNpEntitlementAccessPollServiceEntitlementInfo

Obtains the result of a request to obtain information of a service entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessPollServiceEntitlementInfo(
	int64_t requestId,
	int32_t *pResult,
	SceNpEntitlementAccessServiceEntitlementInfo *info
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to obtain the result for |
| `pResult` | Destination to store the result of the request |
| `info` | Destination to store entitlement information |

## Return Values

Returns one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` | 0 | Request completed |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` | 1 | Request is still being executed |

Stores `SCE_OK` (=0) or an error code (negative value, refer to the "[Return Codes](return-codes.html)" section for details) in `*pResult` if the request has completed.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function obtains the execution result of a request executed with `sceNpEntitlementAccessRequestServiceEntitlementInfo()`.

For `requestId`, specify the request ID obtained with `sceNpEntitlementAccessRequestServiceEntitlementInfo()`.

`SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned as the return value if the request has not completed yet. The value of `*pResult` will not change in such cases.

The result of the request will be stored in `*pResult`, entitlement information will be stored in `*info`, and `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` will be returned as the return value if the request has completed. Make sure that the `*pResult` value is appropriately evaluated as a request execution result. If the `*pResult` value is 0x817D1XXX, it means a server error code. For details, refer to the "[Return Codes](return-codes.html)" section.

## Examples

```
SceNpEntitlementAccessServiceEntitlementInfo info;
int32_t result;

/* Obtain the result of a request to obtain information of a service entitlement */
ret = sceNpEntitlementAccessPollServiceEntitlementInfo(requestId, &result, &info);
```

# sceNpEntitlementAccessPollServiceEntitlementInfoList

Obtain the results of a request to obtain a list of service entitlement information

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessPollServiceEntitlementInfoList(
	int64_t requestId,
	int32_t *pResult,
	SceNpEntitlementAccessServiceEntitlementInfo *list,
	uint32_t listNum,
	uint32_t *hitNum,
	int32_t *nextOffset,
	int32_t *previousOffset
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to obtain the result for |
| `pResult` | Destination to store the result of the request |
| `list` | Destination to store the list of obtained entitlement information |
| `listNum` | Number of elements in `list` |
| `hitNum` | Destination to store the total number of valid entitlement information entries |
| `nextOffset` | Offset value for obtaining the next paged set of entitlements passed to succeeding requests |
| `previousOffset` | Offset value for obtaining the previous paged set of entitlements passed to succeeding requests |

## Return Values

Returns one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` | 0 | Request completed |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` | 1 | Request is still being executed |

Stores `SCE_OK` (=0) or an error code (negative value, refer to the "[Return Codes](return-codes.html)" section for details) in `*pResult` if the request has completed.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function obtains the execution result of a request executed with `sceNpEntitlementAccessRequestServiceEntitlementInfoList()`.

For `requestId`, specify the request ID obtained with `sceNpEntitlementAccessRequestServiceEntitlementInfoList()`.

`SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned as the return value if the request has not completed yet. The value of `*pResult` will not change in such cases.

The result of the request will be stored in `*pResult`, entitlement information will be stored in `*list`, `*hitNum`, `*nextOffet`, `*previousOffset`, and `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` will be returned as the return value if the request has completed. Make sure that the `*pResult` value is appropriately evaluated as a request execution result. If the `*pResult` value is 0x817D1XXX, it means a server error code. For details, refer to the "[Return Codes](return-codes.html)" section.

## Examples

```
SceNpEntitlementAccessServiceEntitlementInfo list[100];
int32_t result;
uint32_t hitNum;
int32_t nextOffset;
int32_t previousOffset;

/* Obtain the results of a request to obtain a list of service entitlement information */
ret = sceNpEntitlementAccessPollServiceEntitlementInfoList(requestId, &result, list, 100, &hitNum, &nextOffset, &previousOffset);
```

# sceNpEntitlementAccessPollConsumeEntitlement

Obtains the result of a request to consume a consumable entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessPollConsumeEntitlement(
	int64_t requestId,
	int32_t *pResult,
	int32_t *useLimit
)
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID of the request to obtain the result for |
| `pResult` | Destination to store the result of the request |
| `useLimit` | Destination to store the number of remaining entitlement counts that can be consumed |

## Return Values

Returns one of the following values for normal termination.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` | 0 | Request completed |
| `SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` | 1 | Request is still being executed |

Stores `SCE_OK` (=0) or an error code (negative value, refer to the "[Return Codes](return-codes.html)" section for details) in `*pResult` if the request has completed.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_REQUEST_NOT_FOUND` | 0x817D0015 | Request with the specified request ID does not exist |

## Description

This function obtains the execution result of a request executed with `sceNpEntitlementAccessRequestConsumeUnifiedEntitlement()` or `sceNpEntitlementAccessRequestConsumeServiceEntitlement()()`.

For `requestId`, specify the request ID obtained with `sceNpEntitlementAccessRequestConsumeUnifiedEntitlement()` or `sceNpEntitlementAccessRequestConsumeServiceEntitlement()`.

`SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING` will be returned as the return value if the request has not completed yet. The value of `*pResult` will not change in such cases.

The result of the request will be stored in `*pResult`, the number of entitlement counts remaining after consumption will be stored in `*useLimit`, and `SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED` will be returned as the return value if the request has completed. Make sure that the `*pResult` value is appropriately evaluated as a request execution result. If the `*pResult` value is 0x817D1XXX, it means a server error code. For details, refer to the "[Return Codes](return-codes.html)" section.

## Examples

```
int32_t useLimit;
int32_t result;

/* Obtain the result of a request to consume a consumable entitlement */
ret = sceNpEntitlementAccessPollConsumeEntitlement(requestId, &result, &useLimit);
```

# sceNpEntitlementAccessRequestUnifiedEntitlementInfo

Requests to obtain information of a unified entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessRequestUnifiedEntitlementInfo(
	SceUserServiceUserId userId,
	SceNpServiceLabel serviceLabel,
	const SceNpUnifiedEntitlementLabel *entitlementLabel,
	int64_t *requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `serviceLabel` | NP service label |
| `entitlementLabel` | Unified entitlement label |
| `requestId` | Destination to store the obtained request ID |

## Return Values

Stores the obtained request ID in `*requestId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Request is being executed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |

## Description

This function requests to obtain information of a unified entitlement. Entitlement information obtainment will be carried out by the system in the background, and the result can be checked by calling `sceNpEntitlementAccessPollUnifiedEntitlementInfo()` with the obtained request ID specified.

For `entitlementLabel`, specify the entitlement label of the unified entitlement that you want to obtain information of. If NULL is specified, a parameter error will occur.

For `serviceLabel`, specify the NP service label of the unified entitlement. Specify 0 when the entitlement is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

Requests are single-use objects: A request used for one communication function call must subsequently be deleted. Create a request before using a communication function and delete it using `sceNpEntitlementAccessDeleteRequest()` once communication processing ends.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpUnifiedEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "0000111122223333", SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE);
int64_t requestId;

/* Request to obtain information of a unified entitlement */
ret = sceNpEntitlementAccessRequestUnifiedEntitlementInfo(userId, serviceLabel, &entitlementLabel, &requestId);
```

# sceNpEntitlementAccessRequestUnifiedEntitlementInfoList

Requests to obtain a list of unified entitlement information

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessRequestUnifiedEntitlementInfoList(
	SceUserServiceUserId userId,
	SceNpServiceLabel serviceLabel,
	const SceNpUnifiedEntitlementLabel *list,
	uint32_t listNum;
	const SceNpEntitlementAccessRequestEntitlementInfoListParam *param,
	int64_t *requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `serviceLabel` | NP service label |
| `list` | List of unified entitlement labels that specify the entitlements that will be returned. If NULL is specified, all related entitlements will be returned |
| `listNum` | Number of elements in `list` |
| `param` | Specifies parameters for obtaining the list of entitlement information |
| `requestId` | Destination to store the obtained request ID |

## Return Values

Stores the obtained request ID in `*requestId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Request is being executed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |

## Description

This function requests that a list of unified entitlement information be obtained. The system obtains the list of entitlement information in the background; the results can be checked by calling `sceNpEntitlementAccessPollUnifiedEntitlementInfoList()` with the obtained request ID specified.

For `serviceLabel`, specify the NP service label of the unified entitlement. Specify 0 when the entitlement is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

For `list` specify the entitlement label for the unified entitlement information you would like to obtain. If NULL is specified, all related entitlements will be returned. To specify NULL, enter 0 for `listNum`.

For `param` specify the parameters for obtaining the list of information about the entitlements that you wish to obtain. If NULL is specified, a parameter error will occur.

Requests are single-use objects: A request used for one communication function call must subsequently be deleted. Create a request before using a communication function and delete it using `sceNpEntitlementAccessDeleteRequest()` once communication processing ends.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpEntitlementAccessRequestEntitlementInfoListParam param;
memset(&param, 0, sizeof(param));
param.size = sizeof(param);
param.entitlementType = SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_UNIFIED;
param.offset = 0;
param.limit = 10;
param.sort = SCE_NP_ENTITLEMENT_ACCESS_SORT_TYPE_NONE;
param.direction = SCE_NP_ENTITLEMENT_ACCESS_DIRECTION_TYPE_NONE;
param.packageType = SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_PSCONS;
int64_t requestId;

/* Request to obtain a list of unified entitlement information */
ret = sceNpEntitlementAccessRequestUnifiedEntitlementInfoList(userId, serviceLabel, NULL, 0, &param, &requestId);
```

# sceNpEntitlementAccessRequestServiceEntitlementInfo

Requests to obtain service entitlement information

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessRequestServiceEntitlementInfo(
	SceUserServiceUserId userId,
	SceNpServiceLabel serviceLabel,
	const SceNpServiceEntitlementLabel *entitlementLabel,
	int64_t *requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `serviceLabel` | NP service label |
| `entitlementLabel` | Service entitlement label |
| `requestId` | Destination to store the obtained request ID |

## Return Values

Stores the obtained request ID in `*requestId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Request is being executed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |

## Description

This function requests that service entitlement information be obtained. Entitlement information will be obtained by the system in the background, and the result can be checked by calling `sceNpEntitlementAccessPollServiceEntitlementInfo()` with the obtained request ID specified.

For `entitlementLabel`, specify the entitlement label of the service entitlement that you want to obtain. If NULL is specified, a parameter error will occur.

For `serviceLabel`, specify the NP service label of the service entitlement. Specify 0 when the entitlement is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

Requests are single-use objects: A request used for one communication function call must subsequently be deleted. Create a request before using a communication function and delete it using `sceNpEntitlementAccessDeleteRequest()` once communication processing ends.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpServiceEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "123456", SCE_NP_SERVICE_ENTITLEMENT_LABEL_SIZE);
int64_t requestId;

/* Request to obtain service entitlement information */
ret = sceNpEntitlementAccessRequestServiceEntitlementInfo(userId, serviceLabel, &entitlementLabel, &requestId);
```

# sceNpEntitlementAccessRequestServiceEntitlementInfoList

Requests to obtain a list of service entitlement information

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessRequestServiceEntitlementInfoList(
	SceUserServiceUserId userId,
	SceNpServiceLabel serviceLabel,
	const SceNpServiceEntitlementLabel *list,
	uint32_t listNum;
	const SceNpEntitlementAccessRequestEntitlementInfoListParam *param,
	int64_t *requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `serviceLabel` | NP service label |
| `list` | List of service entitlement labels that specify the entitlements to be returned. If NULL is specified, all related entitlements will be returned |
| `listNum` | Number of elements in `list` |
| `param` | Specifies parameters for obtaining the list of entitlement information |
| `requestId` | Destination to store the obtained request ID |

## Return Values

Stores the obtained request ID in `*requestId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Request is being executed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |

## Description

This function obtains a list of service entitlement information. The system obtains the entitlement information in the background; the results can be checked by calling `sceNpEntitlementAccessPollServiceEntitlementInfoList()` with the obtained request IDs specified.

For `serviceLabel`, specify the NP service label of the service entitlement. Specify 0 when the entitlement is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

For `list` specify the entitlement label for the service entitlement information you would like to obtain. If NULL is specified, all related entitlements will be returned. To specify NULL, enter 0 for `listNum`.

For `param` specify the parameters for obtaining the list of information about the entitlements that you wish to obtain. If NULL is specified, a parameter error will occur.

Requests are single-use objects: A request used for one communication function call must subsequently be deleted. Create a request before using a communication function and delete it using `sceNpEntitlementAccessDeleteRequest()` once communication processing ends.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpEntitlementAccessRequestEntitlementInfoListParam param;
memset(&param, 0, sizeof(param));
param.size = sizeof(param);
param.entitlementType = SCE_NP_ENTITLEMENT_ACCESS_ENTITLEMENT_TYPE_SERVICE;
param.offset = 0;
param.limit = 10;
param.sort = SCE_NP_ENTITLEMENT_ACCESS_SORT_TYPE_NONE;
param.direction = SCE_NP_ENTITLEMENT_ACCESS_DIRECTION_TYPE_NONE;
param.packageType = SCE_NP_ENTITLEMENT_ACCESS_PACKAGE_TYPE_NONE;
int64_t requestId;

/* Request to obtain service entitlement information */
ret = sceNpEntitlementAccessRequestServiceEntitlementInfoList(userId, serviceLabel, NULL, 0, &param, &requestId);
```

# sceNpEntitlementAccessRequestConsumeUnifiedEntitlement

Requests to consume a unified entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessRequestConsumeUnifiedEntitlement(
	SceUserServiceUserId userId,
	SceNpServiceLabel serviceLabel,
	const SceNpUnifiedEntitlementLabel *entitlementLabel,
	const SceNpEntitlementAccessTransactionId *transactionId,
	int32_t useCount,
	int64_t *requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `serviceLabel` | NP service label |
| `entitlementLabel` | Unified entitlement label |
| `transactionId` | Transaction ID |
| `useCount` | Number of entitlement counts to consume |
| `requestId` | Destination to store the obtained request ID |

## Return Values

Stores the obtained request ID in `*requestId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Request is being executed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |

## Description

This function requests to consume a unified entitlement. Entitlement consumption will be carried out by the system in the background, and the result can be checked by calling `sceNpEntitlementAccessPollConsumeEntitlement()` with the obtained request ID specified.

For `entitlementLabel`, specify the entitlement label of the unified entitlement that you want to consume. If NULL is specified, a parameter error will occur.

For `serviceLabel`, specify the NP service label of the unified entitlement. Specify 0 when the entitlement is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

For `transactionId`, specify the transaction ID generated using `sceNpEntitlementAccessGenerateTransactionId()`.

For `useCount`, specify the number of entitlement counts to consume.

Requests are single-use objects: A request used for one communication function call must subsequently be deleted. Create a request before using a communication function and delete it using `sceNpEntitlementAccessDeleteRequest()` once communication processing ends.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpUnifiedEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "0000111122223333", SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE);
int32_t useCount = 1;
int64_t requestId;

/* Request to consume a unified entitlement */
ret = sceNpEntitlementAccessRequestConsumeUnifiedEntitlement(userId, serviceLabel, &entitlementLabel, &transactionId, useCount, &requestId);
```

# sceNpEntitlementAccessRequestConsumeServiceEntitlement

Requests to consume a service entitlement

## Definition

```
#include <np_entitlement_access.h>
int32_t sceNpEntitlementAccessRequestConsumeServiceEntitlement(
	SceUserServiceUserId userId,
	SceNpServiceLabel serviceLabel,
	const SceNpServiceEntitlementLabel *entitlementLabel,
	const SceNpEntitlementAccessTransactionId *transactionId,
	int32_t useCount,
	int64_t *requestId
)
```

## Arguments

|  |  |
| --- | --- |
| `userId` | User ID |
| `serviceLabel` | NP service label |
| `entitlementLabel` | Service entitlement label |
| `transactionId` | Transaction ID |
| `useCount` | Number of entitlement counts to consume |
| `requestId` | Destination to store the obtained request ID |

## Return Values

Stores the obtained request ID in `*requestId` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_NOT_INITIALIZED` | 0x817D0001 | Library is not initialized |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_PARAMETER` | 0x817D0002 | Parameter error (see below) |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_BUSY` | 0x817D0003 | Request is being executed |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_INTERNAL` | 0x817D000A | Fatal internal error |
| `SCE_NP_ENTITLEMENT_ACCESS_ERROR_OUT_OF_MEMORY` | 0x817D0010 | Memory allocation failed |

## Description

This function requests to consume a service entitlement. Entitlement consumption will be carried out by the system in the background, and the result can be checked by calling `sceNpEntitlementAccessPollConsumeEntitlement()` with the obtained request ID specified.

For `entitlementLabel`, specify the entitlement label of the service entitlement that you want to consume. If NULL is specified, a parameter error will occur.

For `serviceLabel`, specify the NP service label of the service entitlement. Specify 0 when the entitlement is of the application itself. If an invalid NP service label is specified, a parameter error will occur.

For `transactionId`, specify the transaction ID generated using `sceNpEntitlementAccessGenerateTransactionId()`.

For `useCount`, specify the number of entitlement counts to consume.

Requests are single-use objects: A request used for one communication function call must subsequently be deleted. Create a request before using a communication function and delete it using `sceNpEntitlementAccessDeleteRequest()` once communication processing ends.

## Examples

```
SceNpServiceLabel serviceLabel = 0;
SceNpServiceEntitlementLabel entitlementLabel;
memset(&entitlementLabel, 0, sizeof(entitlementLabel));
strncpy(entitlementLabel.data, "123456", SCE_NP_SERVICE_ENTITLEMENT_LABEL_SIZE);
int32_t useCount = 1;
int64_t requestId;

/* Request to consume a service entitlement */
ret = sceNpEntitlementAccessRequestConsumeServiceEntitlement(userId, serviceLabel, &entitlementLabel, &transactionId, useCount, &requestId);
```