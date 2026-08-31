# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/down-stream-transaction.html

# Class sce::Np::CppWebApi::Common::DownStreamTransaction

# Summary

# DownStreamTransaction

Transaction for streaming a download

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class DownStreamTransaction {};
            }
        }
    }
}
```

## Description

This transaction is used for streaming a download.

In contrast to `sce::Np::CppWebApi::Common::Transaction`, which encapsulates communication with Web APIs within the library, `DownStreamTransaction` provides an interface for handling the receiving of data more directly.

This class is mainly used for receiving data incrementally through an appropriately sized buffer when the Web API response body contains a massive amount of binary data (such as an application/octet-stream or image/jpeg).

## Template Arguments

|  |  |
| --- | --- |
| `T` | Specifies the response type |
| `RHT` | Specifies the response header type |

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `readData()` | Receives data |

# Public Member Functions

# DownStreamTransaction::readData()

Receive data

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class DownStreamTransaction {
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