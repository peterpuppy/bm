# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/lib-contextget-memory-stats.html

# Class sce::Np::CppWebApi::Common::LibContext

# Summary

# sce::Np::CppWebApi::Common::LibContext

Library context

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class LibContext {};
            }
        }
    }
}
```

## Description

This class represents the library context.

The library context serves as a unit for managing the library's heap.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `getMemoryStats()` | Gets heap memory information of the library context |

# In-Class Structure

# LibContext::MemoryStats

Heap memory information of the library context

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class LibContext {
                    typedef struct MemoryStats {
                        size_t poolSize;
                        size_t_maxInuseSize;
                        size_t currentInuseSize;
                    } MemoryStats;
                };
            }
        }
    }
}
```

## Members

|  |  |
| --- | --- |
| `poolSize` | Memory pool size of the library context |
| `maxInuseSize` | Maximum memory size used by the library context |
| `currentInuseSize` | Memory size currently used by the library context |

## Description

This structure is used when heap memory information of the library context is obtained with `LibContext::getMemoryStats()`.

# Public Member Functions

# LibContext::getMemoryStats()

Get heap memory information of the library context

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class LibContext {
                    int32_t getMemoryStats(MemoryStats &stats);
                };
            }
        }
    }
}
```

## Description

This function obtains heap memory information of the library context.

Use this function, for example, for determining the memory pool size to specify upon initialization.

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)