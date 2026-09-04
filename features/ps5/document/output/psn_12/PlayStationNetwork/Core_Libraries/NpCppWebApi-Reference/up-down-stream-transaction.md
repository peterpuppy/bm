# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/up-down-stream-transaction.html

# Class sce::Np::CppWebApi::Common::UpDownStreamTransaction

# Summary

# UpDownStreamTransaction

Transaction for streaming uploads and downloads (not yet supported)

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpDownStreamTransaction {};
            }
        }
    }
}
```

## Description

This transaction is used for streaming uploads and downloads.

In contrast to `sce::Np::CppWebApi::Common::Transaction`, which encapsulates communication with Web APIs within the library, `UpDownStreamTransaction` provides an interface for handling the sending and receiving of data more directly.

This class is mainly used for sending and receiving data incrementally through an appropriately sized buffer when the Web API request and response bodies both contain massive amounts of binary data (such as an application/octet-stream or image/jpeg).

## Template Arguments

|  |  |
| --- | --- |
| `T` | Specifies the response type |
| `RHT` | Specifies the response header type |

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `start()` | Starts a transaction |
| `sendData()` | Sends data |
| `readData()` | Receives data |

# Public Member Functions

# UpDownStreamTransaction::start()

Start a transaction for streaming uploads and downloads

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpDownStreamTransaction {
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

This function starts a transaction for streaming uploads and downloads.

`UpDownStreamTransaction::sendData()` is mainly used for sending data incrementally by calling the function multiple times. The total length of the data should be entered in the `contentLength` argument of `start()`. This allows the data to be properly partitioned and sent.

## Arguments

|  |  |
| --- | --- |
| `contentLength` | Total length of data to be sent. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::UpDownStreamTransaction::sendData()`

# UpDownStreamTransaction::sendData()

Send data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpDownStreamTransaction {
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

`sce::Np::CppWebApi::Common::UpDownStreamTransaction::start()`

# UpDownStreamTransaction::readData()

Receive data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class UpDownStreamTransaction {
                    int32_t readData(
                        char *buf, size_t bufSize
                    );
                };
            }
        }
    }
}
```

## Description

This function receives data.

This function is a blocking function. This function calls `sceNpWebApi2ReadData()` internally. The conditions for this function to return are equivalent to those of `sceNpWebApi2ReadData()`.

## Arguments

|  |  |
| --- | --- |
| `buf` | Buffer for receiving data |
| `bufSize` | Size of the buffer for receiving data |

## Return Values

Stores the obtained response body in `*buf` and returns the size of the stored data on normal termination. Returns 0 if all response bodies have already been received and there is no data to be stored in the buffer.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)