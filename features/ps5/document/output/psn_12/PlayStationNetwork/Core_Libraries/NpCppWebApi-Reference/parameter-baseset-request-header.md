# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/parameter-baseset-request-header.html

# Class sce::Np::CppWebApi::Common::ParameterBase

# Summary

# ParameterBase

Parameter base class

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {};
            }
        }
    }
}
```

## Description

This is the base class for parameters that are commonly used in each Web API call function.

For each Web API call function, a query parameter, path parameter, and header parameter unique to the API are represented using a derived class from this base class.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `initialize()` | Initializes |
| `terminate()` | Terminates |
| `setRequestHeader()` | Sets a request header |
| `unSetRequestHeader()` | Cancels setting of the request header |
| `setWebtraceTagHeader()` | Sets a WebTrace tag header |
| `unSetWebtraceTagHeader()` | Undoes the setting of a WebTrace tag header |

# Public Member Functions

# ParameterBase::initialize

Initialize the parameter base class

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {
                    int32_t initialize(LibContext &ctx);
                };
            }
        }
    }
}
```

## Description

This function initializes the base class for parameters that are commonly used in each Web API call function.

## Arguments

|  |  |
| --- | --- |
| `ctx` | Library context |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::ParameterBase::terminate()`

# ParameterBase::terminate

Carry out termination processing of the parameter base class

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {
                    int32_t terminate();
                };
            }
        }
    }
}
```

## Description

This function carries out termination processing of the base class for parameters that are commonly used in each Web API call function.

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::ParameterBase::initialize()`

# ParameterBase::setRequestHeader

Set an arbitrary request header

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {
                    int32_t setRequestHeader(const char *fieldName, const char* value);
                };
            }
        }
    }
}
```

## Description

This function specifies an arbitrary field for a request header to be used for calling a Web API function and sets the request header.

If a request header of the same field name is set as a parameter on the derived class side, the setting on the derived class side will be prioritized and used upon execution of the Web API call function.

## Arguments

|  |  |
| --- | --- |
| `fieldName` | Request header field name |
| `value` | Request header value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::ParameterBase::unSetRequestHeader()`

# ParameterBase::unSetRequestHeader

Cancel setting of an arbitrary request header

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {
                    int32_t unSetRequestHeader(const char *fieldName);
                };
            }
        }
    }
}
```

## Description

This function specifies an arbitrary field name and cancels the set request header.

If a request header of the same field name is set as a parameter on the derived class side, even if its setting is canceled on the base class side, the setting on the derived class side will be prioritized and used upon execution of the Web API call function.

## Arguments

|  |  |
| --- | --- |
| `fieldName` | Request header field name |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::ParameterBase::setRequestHeader()`

# ParameterBase::setWebtraceTagHeader

Set a WebTrace tag header

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {
                    int32_t setWebtraceTagHeader(const char* value);
                };
            }
        }
    }
}
```

## Description

This function specifies and sets an arbitrary tag for a WebTrace tag header to be used for calling a Web API.

A WebTrace tag is tag information for use with the "★Debug Settings" > "WebTrace" feature. For details, refer to [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html).

## Arguments

|  |  |
| --- | --- |
| `value` | WebTrace tag value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::ParameterBase::unSetWebtraceTagHeader()`

# ParameterBase::unSetWebtraceTagHeader

Cancel the setting of a WebTrace tag header

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class ParameterBase {
                    int32_t unSetWebtraceTagHeader();
                };
            }
        }
    }
}
```

## Description

This function cancels a WebTrace tag header that has been set.

A WebTrace tag is tag information for use with the "★Debug Settings" > "WebTrace" feature. For details, refer to [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html).

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

## See Also

`sce::Np::CppWebApi::Common::ParameterBase::setWebtraceTagHeader()`