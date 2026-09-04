# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/typedef.html

# Namespace sce::Np::CppWebApi::Common

# Summary

# sce::Np::CppWebApi::Common

The namespace for NpCppWebApi library common functions

## Definition

```
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {}
        }
    }
}
```

## Description

The namespace for NpCppWebApi library common functions.

## Inner Classes, Structures, and Namespaces

| **Item** | **Description** |
| --- | --- |
| `sce::Np::CppWebApi::Common::InitParams` | Initialization parameter class. |
| `sce::Np::CppWebApi::Common::LibContext` | Library context class. |
| `sce::Np::CppWebApi::Common::TransactionBase` | Transaction base class. |
| `sce::Np::CppWebApi::Common::Transaction` | Transaction class. |
| `sce::Np::CppWebApi::Common::UpStreamTransaction` | Upload stream transaction class. |
| `sce::Np::CppWebApi::Common::DownStreamTransaction` | Download stream transaction class. |
| `sce::Np::CppWebApi::Common::UpDownStreamTransaction` | Upload/download stream transaction class. |
| `sce::Np::CppWebApi::Common::DefaultResponse` | Default response. |
| `sce::Np::CppWebApi::Common::EmptyHeader` | Empty header. |

# Functions

# sce::Np::CppWebApi::Common::initialize()

Initialize the library

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
               int32_t initialize(
                  const InitParams &params, 
                  LibContext &ctx
               );
            }
        }
    }
}
```

## Description

Initializes the library.

## Arguments

|  |  |
| --- | --- |
| `params` | Initialization parameters |
| `ctx` | Library context |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::terminate()`

# sce::Np::CppWebApi::Common::terminate()

Terminate the library

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
               int32_t terminate(
                  LibContext &ctx
               );
            }
        }
    }
}
```

## Description

Terminates the library.

## Arguments

|  |  |
| --- | --- |
| `ctx` | Library context |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::initialize()`

# sce::Np::CppWebApi::Common::isWebApiError()

Function that determines whether an error code in a return value from when a response is obtained is a Web API error

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
               bool isWebApiError(
                  int32_t error
               );
            }
        }
    }
}
```

## Description

This function determines whether an error code in a return value from when a response is obtained is a Web API error.

If it is a Web API error, the error object can be obtained using `getError()` from the response obtained with `Transaction::getResponse()`.

## Arguments

|  |  |
| --- | --- |
| `error` | A Transaction::getResponse() return value error code |

## Return Values

Returns true if `error` is a Web API error.

# typedef

## Definition

```
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                typedef int64_t TransactionId;
                typedef int32_t ReturnCode;
            }
        }
    }
}
```

## Description

| **typedef** | **Type** | **Description** |
| --- | --- | --- |
| `TransactionId` | `int64_t` | Transaction ID |
| `ReturnCode` | `int32_t` | Return code |