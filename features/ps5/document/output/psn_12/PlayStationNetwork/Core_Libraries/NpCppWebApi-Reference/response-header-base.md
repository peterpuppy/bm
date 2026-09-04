# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/response-header-base.html

# Class sce::Np::CppWebApi::Common::ResponseHeaderBase

# Summary

# ResponseHeaderBase

Response header base class

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ResponseHeaderBase : public Common::RefObject {};
            }
        }
    }
}
```

## Description

This is the base class of the response header.

An arbitrary header field name can be specified, and an arbitrary header field can be obtained, via this base class.

Use a member function of this base class to obtain standard response headers that are used by Web APIs in general.

For response headers specific to a service, use the getter API feature provided by the derived class inheriting this base class.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `getHeaderValue()` | Gets the header value |

# Public Member Functions

# ResponseHeaderBase::getHeaderValue

Get an arbitrary response header value

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ResponseHeaderBase {
                    int32_t getHeaderValue(const char *fieldName, IntrusivePtr<Common::String> &value);
                };
            }
        }
    }
}
```

## Description

This function specifies an arbitrary field name from the response header field returned from a Web API and obtains the field value.

Response headers that don't have getter APIs defined can still be obtained using this function.

## Arguments

|  |  |
| --- | --- |
| `fieldName` | Response header field name |
| `value` | Response header value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)