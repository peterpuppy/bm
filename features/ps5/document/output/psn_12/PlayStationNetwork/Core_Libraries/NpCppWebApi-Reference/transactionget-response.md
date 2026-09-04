# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/transactionget-response.html

# Class sce::Np::CppWebApi::Common::Transaction

# Summary

# Transaction

Transaction template class

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class Transaction {};
            }
        }
    }
}
```

## Description

This is the transaction class.

A response can be obtained via this object during the duration of the transaction.

## Template Arguments

|  |  |
| --- | --- |
| `T` | Specifies the response type |
| `RHT` | Specifies the response header type |

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `getResponse()` | Gets the response |
| `hasResponse()` | Checks whether the response has arrived |
| `setOnFinishedCallback()` | Sets the callback function for receiving the response asynchronously |

# Public Member Functions

# Transaction::getResponse()

Gets the response

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
            template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class Transaction {
                    int32_t getResponse(T &response) const;
                };
            }
        }
    }
}
```

## Description

This function gets the response.

This function blocks until an actual response is obtained from the Web API. Therefore, call this function after you are certain that the Web API has returned a response (for example, after `sce::Np::CppWebApi::Common::Transaction::hasResponse()` has returned `true`).

## Arguments

|  |  |
| --- | --- |
| `response` | Response |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

If the error code is a Web API error, you can obtain the error object from `response` to learn the details of the error.

## See Also

`sce::Np::CppWebApi::Common::Transaction::hasResponse()`

`sce::Np::CppWebApi::Common::isWebApiError()`

# Transaction::hasResponse()

Check whether the response has arrived

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class Transaction {
                    bool hasResponse() const;
                };
            }
        }
    }
}
```

## Description

This function checks whether the response has arrived.

## Return Values

Returns `true` if the response has arrived. Otherwise, returns `false`.

## See Also

`sce::Np::CppWebApi::Common::Transaction::getResponse()`

# Transaction::setOnFinishedCallback()

Set the callback to be called when asynchronous processing finishes

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::IntrusivePtr<Common::ResponseHeaderBase> >
                class Transaction {
                    int32_t setOnFinishedCallback(
                       void (*onSucceededCallback)(
                          TransactionId, ReturnCode, T, void*),
                       void (*onFailedCallback)(
                          TransactionId, ReturnCode, void*),
                       void *userdata
                    );
                };
            }
        }
    }
}
```

## Description

This function sets the callback to be called when asynchronous processing finishes.

## Arguments

|  |  |
| --- | --- |
| `onSucceededCallback` | Callback when processing succeeds |
| `onFailedCallback` | Callback when processing fails |
| `userdata` | User data |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::InitParams::numWorkers`