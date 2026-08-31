# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/class-sce-np-cpp-web-api-common-transaction-base.html

# Class sce::Np::CppWebApi::Common::TransactionBase

# Summary

# TransactionBase

Transaction base template class

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {};
            }
        }
    }
}
```

## Description

This is the transaction base template class.

This object is used for the following purposes for the duration of the transaction.

* Calling functions corresponding to PlayStation™Network Web APIs ("Web APIs")
* Aborting blocking

Like other NpCppWebApi library template classes, this template class can only accept types provided by the NpCppWebApi library as template arguments.

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
| `finish()` | Ends a transaction |
| `abort()` | Aborts a transaction |
| `getResponseHeaders()` | Gets the response headers |
| `getId()` | Gets the transaction ID |
| `setResponseInformationOption()` | Sets the destination to store optional response information |
| `getResponseInformationOption()` | Obtains a pointer to the destination to store optional response information |

# Public Member Functions

# TransactionBase::start()

Start a transaction

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    int32_t start(LibContext *ctx);
                };
            }
        }
    }
}
```

## Description

This function starts a transaction.

Actual network communication is not carried out and only the preparation required for communication is carried out.

## Arguments

|  |  |
| --- | --- |
| `ctx` | Library context |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::TransactionBase::finish()`, `sce::Np::CppWebApi::Common::TransactionBase::abort()`

# TransactionBase::finish()

End a transaction

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    int32_t finish();
                };
            }
        }
    }
}
```

## Description

This function ends a transaction.

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::TransactionBase::start()`, `sce::Np::CppWebApi::Common::TransactionBase::abort()`

# TransactionBase::abort()

Abort a transaction

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    int32_t abort();
                };
            }
        }
    }
}
```

## Description

This function aborts a transaction.

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::TransactionBase::start()`, `sce::Np::CppWebApi::Common::TransactionBase::finish()`

# TransactionBase::getResponseHeaders()

Get the response headers

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    int32_t getResponseHeaders(RHT &headers) const;
                };
            }
        }
    }
}
```

## Description

This function gets the response headers.

This function blocks until an actual response is obtained from the Web API. Therefore, call this function after you are certain that the Web API has returned a response (for example, after `sce::Np::CppWebApi::Common::Transaction::hasResponse()` has returned `true`).

## Arguments

|  |  |
| --- | --- |
| `headers` | Response header |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::EmptyHeader`

# TransactionBase::getId()

Get the transaction ID

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    TransactionId getId() const;
                };
            }
        }
    }
}
```

## Description

This function gets the transaction ID.

When a transaction instance is copied, a shallow copy is performed so only a pointer to an internal management structure is copied. By comparing IDs obtained by this function, you can determine whether the underlying internal management structures of different transaction instances are the same.

## Return Values

Returns the transaction ID. Returns 0 if the transaction has not been started.

# TransactionBase::setResponseInformationOption()

Set the destination to store optional response information

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    void setResponseInformationOption(
                        SceNpWebApi2ResponseInformationOption *respInfoOpt
                    );
                };

            }
        }
    }
}
```

## Description

This function sets the destination to store optional response information function.

Set the destination to store the HTTP status code or error Json object from when a PlayStation™Network Web API returns an error and you want to obtain that status code or Json object.

Make sure the `SceNpWebApi2ResponseInformationOption` structure provided as an argument is maintained during the lifetime of `TransactionBase`. In other words, do not free memory during the period after the call of `TransactionBase::start()` until the call of `TransactionBase::finish()`.

For details about the `SceNpWebApi2ResponseInformationOption` structure, which is passed as the function's argument, refer to [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html).

## Arguments

|  |  |
| --- | --- |
| `respInfoOpt` | Destination to store optional response information |

## See Also

`sce::Np::CppWebApi::Common::TransactionBase::getResponseInformationOption()`

# TransactionBase::getResponseInformationOption()

Obtain a pointer to the destination to store optional response information

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T, typename RHT = Common::EmptyHeader >
                class TransactionBase {
                    SceNpWebApi2ResponseInformationOption* getResponseInformationOption();
                };
            }
        }
    }
}
```

## Description

This function obtains a pointer to the destination to store optional response information function.

With this function, you can obtain a pointer to the `SceNpWebApi2ResponseInformationOption` structure set using `sce::Np::CppWebApi::Common::TransactionBase::setResponseInformationOption()`.

## Return Values

Returns a pointer to the destination to store optional response information.

## See Also

`sce::Np::CppWebApi::Common::TransactionBase::setResponseInformationOption()`