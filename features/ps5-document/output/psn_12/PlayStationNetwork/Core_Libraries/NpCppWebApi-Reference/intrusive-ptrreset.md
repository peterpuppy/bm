# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/intrusive-ptrreset.html

# Class sce::Np::CppWebApi::Common::IntrusivePtr

# Summary

# Common::IntrusivePtr

Intrusive smart pointer

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class IntrusivePtr {};
            }
        }
    }
}
```

## Description

This is the intrusive smart pointer template class.

Like other NpCppWebApi library template classes, this template class can only accept types provided by the NpCppWebApi library as template arguments.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `reset()` | Resets the smart pointer |
| `get()` | Returns the address of the object owned by the smart pointer |
| `get_deleter()` | Returns the deleter |

## See Also

`sce::Np::CppWebApi::Common::RefObject`

# Public Member Functions

# IntrusivePtr::reset()

Reset the smart pointer

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class IntrusivePtr {
                    void reset();
                };
            }
        }
    }
}
```

## Description

This function resets the smart pointer.

# IntrusivePtr::get()

Return the address of the object owned by the smart pointer

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class IntrusivePtr {
                    void* get();
                };
            }
        }
    }
}
```

## Description

This function returns the address of the object owned by the smart pointer.

## Return Values

Returns the address of the object owned by the smart pointer.

# IntrusivePtr::get\_deleter()

Return the deleter

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class IntrusivePtr {
                    void (*get_deleter())(T*);
                };
            }
        }
    }
}
```

## Description

This function returns the deleter of the resource owned by the smart pointer.