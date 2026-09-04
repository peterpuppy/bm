# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2add-web-trace-tag.html

# WebTrace

# sceNpWebApi2AddWebTraceTag

Set a WebTrace tag

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2AddWebTraceTag(
	int64_t requestId,
	const char *pValue
);
```

## Arguments

|  |  |
| --- | --- |
| `requestId` | Request ID |
| `pValue` | Value of the tag to add (ASCIIZ string) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function is for adding tag information that is used by the "★Debug Setttings" > "WebTrace" feature when a Web API is executed. Refer to the [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html) document for details.

## Examples

```
int32_t ret = 0; 
int64_t requestId;

ret = sceNpWebApi2AddWebTraceTag (
	requestId, "Tag-Name");
if(ret < 0){
	/* Error handling */
}
```