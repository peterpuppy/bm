# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/class-sce-np-cpp-web-api-common-binary.html

# Class sce::Np::CppWebApi::Common::Binary

# Summary

# Binary

Binary data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class Binary : public Common::RefObject{};
            }
        }
    }
}
```

## Description

This class represents binary data.

Json objects have fields that contain Base64-encoded binary data as values. This class represents these values.

Binary data is used for communication across the application-library interface, however, since the library properly handles Base64 encoding internally for communication with Web APIs, the application does not need to implement its own processing for Base64 encoding/decoding.

## Members

## Public Static Functions

`intrusive_ptr_add_ref()` and `intrusive_ptr_sub_ref()` have been implemented, however, the application does not directly use them.

## Public Instance Member Functions

|  |  |
| --- | --- |
| `size()` | Returns the size of the binary data |
| `clear()` | Clears the binary data |
| `getBinary()` | Returns the starting address of the binary data |
| `setBinary()` | Sets the binary data |

# Public Member Functions

# Binary::size()

Return the size of the binary data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class Binary {
                    size_t size() const;
                };
            }
        }
    }
}
```

## Description

This function returns the size of the binary data.

## Return Values

Returns the size of the binary data.

# Binary::clear()

Clear the binary data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class Binary {
                    void clear();
                };
            }
        }
    }
}
```

## Description

This function clears the binary data.

## Return Values

None

# Binary::getBinary()

Return the starting address of the binary data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class Binary {
                    const void* getBinary() const;
                };
            }
        }
    }
}
```

## Description

This function returns the starting address of the binary data.

## Return Values

Returns the starting address of the binary data.

# Binary::setBinary()

Set the binary data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class Binary {
                    int32_t setBinary(const void* p, size_t size) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function sets the binary data.

Memory is allocated internally, and the binary data is copied and stored. If memory allocation fails, an error code is returned.

## Arguments

|  |  |
| --- | --- |
| `p` | Starting address of the binary data to set |
| `size` | Size of the binary data to set |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)