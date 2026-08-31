# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/class-sce-np-cpp-web-api-common-up-stream-transaction.html

# Class sce::Np::CppWebApi::Common::UpStreamTransaction

# Summary

# UpStreamTransaction

Transaction for streaming an upload

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpStreamTransaction {};
            }
        }
    }
}
```

## Description

This transaction is used for streaming an upload.

In contrast to `sce::Np::CppWebApi::Common::Transaction`, which encapsulates both the communication with Web APIs and Json object serialization/deserialization within the library, `UpStreamTransaction` provides a simple interface designed specifically for sending binary data.

This class is mainly used for sending data incrementally through an appropriately sized buffer when the Web API request body contains a massive amount of binary data (such as an application/octet-stream or image/jpeg).

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `start()` | Starts a transaction |
| `sendData()` | Sends data |

# Public Member Functions

# UpStreamTransaction::start()

Start a transaction for uploading

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpStreamTransaction {
                    int32_t start(
                        LibContext *ctx,
                        size_t contentLength
                    );
                };
            }
        }
    }
}
```

## Description

This function starts a transaction for uploading.

`UpStreamTransaction::sendData()` is mainly used for sending data incrementally by calling the function multiple times. The total length of the data should be entered in the `contentLength` argument of `start()`. This allows the data to be properly partitioned and sent.

## Arguments

|  |  |
| --- | --- |
| `ctx` | Library context |
| `contentLength` | Total length of data to be sent. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::UpStreamTransaction::sendData()`

# UpStreamTransaction::sendData()

Send data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpStreamTransaction {
                    int32_t sendData(
                        const void *buf, size_t bufSize
                    );
                };
            }
        }
    }
}
```

## Description

This function sends data.

## Arguments

|  |  |
| --- | --- |
| `buf` | Buffer containing data to be sent |
| `bufSize` | Size of data to be sent |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::UpStreamTransaction::start()`