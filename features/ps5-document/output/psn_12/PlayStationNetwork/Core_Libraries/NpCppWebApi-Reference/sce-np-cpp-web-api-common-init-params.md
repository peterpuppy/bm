# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/sce-np-cpp-web-api-common-init-params.html

# Class sce::Np::CppWebApi::Common::InitParams

# Summary

# sce::Np::CppWebApi::Common::InitParams

Initialization parameters

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class InitParams {};
            }
        }
    }
}
```

## Description

This class stores initialization parameters.

## Members

## Public Instance Member Variables

|  |  |
| --- | --- |
| `numWorkers` | Number of worker threads. (Default is 0. If this is 1, the library will use asynchronous processing. Values of 2 or greater are not yet supported.) |
| `mask` | CPU affinity mask of worker thread |
| `threadPriority` | Thread priority of worker thread |
| `threadStackSize` | Thread stack size of worker thread |
| `poolSize` | Pool size reserved internally by the library for heap allocation |

## Notes

The `SCE_NP_CPPWEBAPI_ERROR_OUT_OF_MEMORY` error may occur while using the library when the `poolSize` setting is insufficient. Check the required pool size using `sce::Np::CppWebApi::Common::LibContext::getMemoryStats()` and set a sufficient value for `poolSize`.

## See Also

`sce::Np::CppWebApi::Common::initialize()`