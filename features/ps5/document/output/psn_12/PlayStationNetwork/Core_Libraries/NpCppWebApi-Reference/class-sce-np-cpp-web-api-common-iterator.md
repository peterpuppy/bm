# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/class-sce-np-cpp-web-api-common-iterator.html

# Class sce::Np::CppWebApi::Common::Iterator

# Summary

# Common::Iterator

Iterator

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public ConstIterator<T> {};
            }
        }
    }
}
```

## Description

This is the iterator template class. Only types specified by the library are supported as template arguments.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `operator*()` | Operator`*` |
| `operator->()` | Operator`->` |
| `operator++()` | Operator`++` |
| `operator--()` | Operator`--` |
| `operator==()` | Operator`==` |
| `operator!=()` | Operator`!=` |

## See Also

`sce::Np::CppWebApi::Common::Vector`

# Public Member Functions

# Iterator::operator\*()

Operator\*

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public RefObject {
                    T& operator*() const;
                };
            }
        }
    }
}
```

## Description

Operator\* returns a reference to the object pointed to by the iterator.

## Return Values

Returns a reference to the object pointed to by the iterator.

# Iterator::operator->()

Operator->

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public RefObject {
                    T* operator->() const;
                };
            }
        }
    }
}
```

## Description

Operator-> returns the address of the object pointed to by the iterator.

## Return Values

Returns the address of the object pointed to by the iterator.

# Iterator::operator++()

Operator++

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public RefObject {
                    Iterator<T> operator++() const;
                };
            }
        }
    }
}
```

## Description

This operator increments the iterator.

## Return Values

Returns a const iterator.

# Iterator::operator--()

Operator--

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public RefObject {
                    Iterator<T> operator--() const;
                };
            }
        }
    }
}
```

## Description

This operator decrements the iterator.

## Return Values

Returns a const iterator.

# Iterator::operator==()

Operator==

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public RefObject {
                    bool operator==(const This& right) const;
                };
            }
        }
    }
}
```

## Description

This operator determines whether the iterators are pointing to the same element.

## Arguments

|  |  |
| --- | --- |
| `right` | Right |

## Return Values

Returns `true` if the iterators are pointing to the same element.

# Iterator::operator!=()

Operator!=

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Iterator : public RefObject {
                    bool operator!=(const This& right) const;
                };
            }
        }
    }
}
```

## Description

This operator determines if the iterators are not pointing to the same element.

## Arguments

|  |  |
| --- | --- |
| `right` | Right |

## Return Values

Returns `true` if the iterators are not pointing to the same element.