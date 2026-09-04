# NpWebApi2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Reference/sce-np-web-api-2get-memory-pool-stats.html

# Memory

# SceNpWebApi2MemoryPoolStats

NpWebApi2 library memory information

## Definition

```
#include <np/np_webapi2.h>
typedef struct SceNpWebApi2MemoryPoolStats {
	size_t poolSize;
	size_t maxInuseSize;
	size_t currentInuseSize;
	int32_t reserved;
} SceNpWebApi2MemoryPoolStats;
```

## Members

|  |  |
| --- | --- |
| `poolSize` | Memory pool size for the NpWebApi2 library |
| `maxInuseSize` | Maximum memory size used by the NpWebApi2 library |
| `currentInuseSize` | Size of the memory currently being used by the NpWebApi2 library |
| `reserved` | Reserved area |

## Description

This is a structure for obtaining memory information pertaining to the NpWebApi2 library using `sceNpWebApi2GetMemoryPoolStats()`.

# sceNpWebApi2GetMemoryPoolStats

Get NpWebApi2 library memory information

## Definition

```
#include <np/np_webapi2.h>
int32_t sceNpWebApi2GetMemoryPoolStats(
	int32_t libCtxId,
	SceNpWebApi2MemoryPoolStats *pCurrentStat
);
```

## Arguments

|  |  |
| --- | --- |
| `libCtxId` | Library context ID of the NpWebApi2 library |
| `pCurrentStat` | Storage destination for memory information obtain results |

## Return Values

Stores the obtained memory information in `*pCurrentStat` and returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (For details, refer to the "[Return Codes](return-codes.html)" section.)

## Description

This function obtains NpWebApi2 library memory information. Use it when determining the memory pool size to specify during initialization, etc.

## Examples

```
int32_t ret = 0;
int32_t libCtxId;
SceNpWebApi2MemoryPoolStats stats;

memset(&stats, 0, sizeof(stats));
ret = sceNpWebApi2GetMemoryPoolStats(libCtxId, &stats);
if(ret < 0){
	/* Error handling */
}
```