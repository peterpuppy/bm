# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/stringappend.html

# Class sce::Np::CppWebApi::Common::String

# Summary

# Common::String

Class representing a variable-length string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {};
            }
        }
    }
}
```

## Description

This class represents a variable-length string.

## Members

## Public Static Variables

|  |  |
| --- | --- |
| `npos` | A value equal to the maximum length of the string |

## Public Instance Member Functions

|  |  |
| --- | --- |
| `copyFrom()` | Copies a string |
| `append()` | Appends a string |
| `size()` | Returns the length of the string |
| `length()` | Returns the length of the string |
| `find()` | Finds a string |
| `clear()` | Clears the string |
| `c_str()` | Returns the address of the string buffer |
| `replace()` | Replaces the string |
| `empty()` | Determines whether the string is empty |
| `setContext()` | Sets the library context |

# Public Member Functions

# String::copyFrom

Copy a string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    int32_t copyFrom(const char* src) __attribute__((warn_unused_result));
                    int32_t copyFrom(const String & src) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function copies a string. It allocates memory and copies the string into an instance. If there is insufficient memory for allocating memory, an error code is returned.

## Arguments

(`const char* src`)

|  |  |
| --- | --- |
| `src` | String buffer |

(`const String & src`)

|  |  |
| --- | --- |
| `src` | Variable-length string class |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# String::append()

Append a string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    int32_t append(const char* src) __attribute__((warn_unused_result));
                    int32_t append(const String & src) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function appends a string. Since memory is allocated to perform the append, an error is returned if there is insufficient memory available.

## Arguments

(`const char* src`)

|  |  |
| --- | --- |
| `src` | String buffer |

(`const String & src`)

|  |  |
| --- | --- |
| `src` | Variable-length string class |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# String::size()

Return the length of the string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    size_t size() const;
                };
            }
        }
    }
}
```

## Description

This function returns the length of a string. It returns the same result as `length()`.

# String::length()

Return the length of the string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    size_t length() const;
                };
            }
        }
    }
}
```

## Description

This function returns the length of a string. It returns the same result as `size()`.

# String::find()

Find a string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    size_t find(const String &s) const;
                    size_t find(const String &s, size_t position) const;
                };
            }
        }
    }
}
```

## Description

This function finds whether the specified string is contained in this String instance. If the specified string is found, its position where it was found is returned.

## Arguments

(`const String &s`)

|  |  |
| --- | --- |
| `s` | Search string |

(`const String & s, size_t position`)

|  |  |
| --- | --- |
| `s` | Search string |
| `position` | Search starting position |

## Return Values

Returns the position in the String instance where the search string was found, if the search string is contained in this String instance.

# String::clear()

Clear the string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    void clear();
                };
            }
        }
    }
}
```

## Description

This function clears the string.

## Return Values

None

# String::c\_str()

Return the address of the string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    const char* c_str() const;
                };
            }
        }
    }
}
```

## Description

This function returns the address of the string.

## Return Values

Returns the address of the string.

# String::replace()

Replace a string

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    int32_t replace(
                       size_t start, 
                       size_t end, 
                       String &str) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function replaces the specified number of characters with the replacement string starting at the specified position. If memory allocation occurs during the operation and there is insufficient memory available, an error is returned.

## Arguments

|  |  |
| --- | --- |
| `start` | Specified position |
| `end` | Specified number of characters |
| `str` | Replacement string |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# String::empty()

Determine whether the string is empty

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    bool empty() const;
                };
            }
        }
    }
}
```

## Description

This function determines whether the string is empty.

## Return Values

Returns `true` if the string is empty. Otherwise, returns `false`.

# String::setContext()

Set the library context

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                class String {
                    void setContext(Common::LibContext *context) const;
                };
            }
        }
    }
}
```

## Description

This function sets the library context of the NpCppWebApi library.

## Arguments

|  |  |
| --- | --- |
| `context` | NpCppWebApi library context. |