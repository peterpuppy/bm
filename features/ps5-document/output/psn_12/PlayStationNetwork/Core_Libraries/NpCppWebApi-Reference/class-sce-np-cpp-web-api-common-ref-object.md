# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/class-sce-np-cpp-web-api-common-ref-object.html

# Class sce::Np::CppWebApi::Common::RefObject

# Summary

# Common::RefObject

Reference object

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class RefObject {};
            }
        }
    }
}
```

## Description

This is the base class for classes handled by `IntrusivePtr`.

Application developers should not use this class intentionally.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `GetRefCount()` | Returns the reference count |

## See Also

`sce::Np::CppWebApi::Common::IntrusivePtr`

# Public Member Functions

# RefObject::GetRefCount()

Return the reference count

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class RefObject {
                    int32_t GetRefCount() const;
                };
            }
        }
    }
}
```

## Description

This function returns the reference count.

## Return Values

Returns the reference count.