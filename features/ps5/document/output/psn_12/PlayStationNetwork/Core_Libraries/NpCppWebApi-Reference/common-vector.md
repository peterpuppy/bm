# NpCppWebApi Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCppWebApi-Reference/common-vector.html

# Class sce::Np::CppWebApi::Common::Vector

# Summary

# Common::Vector

Class representing a variable-length array

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {};
            }
        }
    }
}
```

## Description

This class represents a variable-length array.

## Members

## Public Instance Member Functions

|  |  |
| --- | --- |
| `pushBack()` | Adds an element to the end |
| `size()` | Returns the size of the array |
| `clear()` | Clears the array |
| `operator[]()` | Operator[] |
| `empty()` | Determines whether the array is empty |
| `begin()` | Returns an iterator pointing to the starting element of the array |
| `end()` | Returns an iterator pointing to the next position after the end of the array |
| `reserve()` | Changes the capacity |
| `capacity()` | Returns the capacity |
| `resize()` | Changes the number of elements |
| `popBack()` | Deletes an element from the end |
| `insert()` | Inserts an element |
| `erase()` | Deletes an element |

# Public Member Functions

# Vector::pushBack()

Adds an element to the end

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    int pushBack(const T & x) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function adds an element to the end of the variable-length array.

It allocates memory and copies the given element internally. If there is insufficient memory for allocating memory, an error code is returned.

## Arguments

|  |  |
| --- | --- |
| `x` | Element to append |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# Vector::size()

Return the number of elements of the variable-length array

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    size_t size() const;
                };
            }
        }
    }
}
```

## Description

This function returns the number of elements of the variable-length array.

## Return Values

Returns the number of elements of the variable-length array.

# Vector::clear()

Clear the variable-length array

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    void clear();
                };
            }
        }
    }
}
```

## Description

This function clears the variable-length array.

# Vector::operator[]()

Return a reference to the element at a specified index

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    const T& operator[](size_t n) const;
                    T& operator[](size_t n);
                };
            }
        }
    }
}
```

## Description

This function returns a reference to the element at a specified index.

## Arguments

|  |  |
| --- | --- |
| `n` | Index |

## Return Values

Returns a reference to the element at the specified index.

# Vector::empty()

Return whether the array is empty

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    bool empty() const;
                };
            }
        }
    }
}
```

## Description

This function returns whether the variable-length array is empty.

## Return Values

Returns `true` if the array is empty. Otherwise, returns `false`.

# Vector::begin()

Return an iterator pointing to the starting element

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    Iterator<T> begin();
                    ConstIterator<T> begin() const;
                };
            }
        }
    }
}
```

## Description

This function returns an iterator pointing to the starting element of the variable-length array.

## Return Values

Returns an iterator that points to the starting element.

# Vector::end()

Return an iterator pointing to the next element after the end of the array

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    Iterator<T> end();
                    ConstIterator<T> end() const;
                };
            }
        }
    }
}
```

## Description

This function returns an iterator pointing to the next position after the last element of the variable-length array.

## Return Values

Returns an iterator pointing to the next position after the last element.

# Vector::reserve()

Change the maximum number of elements (capacity) that can be stored without reallocating memory

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    int32_t reserve(size_t n) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function changes the capacity of the variable-length array. Capacity is the maximum number of elements that can be stored without reallocating memory.

If the capacity is insufficient when an element is added to the variable-length array, memory will be reallocated. This function is used to allocate the required capacity in advance before adding an element.

## Arguments

|  |  |
| --- | --- |
| `n` | Required capacity. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# Vector::capacity()

Return the maximum number of elements (capacity) that can be stored without reallocating memory

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    size_t capacity() const;
                };
            }
        }
    }
}
```

## Description

This function returns the capacity of the variable-length array. Capacity is the maximum number of elements that can be stored without reallocating memory.

## Return Values

Returns the maximum number of elements (capacity) that can be stored without reallocating memory.

# Vector::resize()

Change the number of elements

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    	int32_t resize(uint32_t n) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function changes the number of elements of the variable-length array.

## Arguments

|  |  |
| --- | --- |
| `n` | Number of elements. |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# Vector::popBack()

Delete the last element

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public VectorVal<T>, public RefObject {
                    void popBack();
                };
            }
        }
    }
}
```

## Description

This function deletes the last element of the variable-length array.

# Vector::insert()

Insert an element

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public RefObject {
                    int32_t insert(VectorVal<T>::iterator position, const T& x, VectorVal<T>::iterator & result) __attribute__((warn_unused_result));
                    int32_t insert(VectorVal<T>::const_iterator position, const T& x, VectorVal<T>::const_iterator<T> & result) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function inserts an element into the variable-length array and returns an iterator pointing to the inserted element.

## Arguments

|  |  |
| --- | --- |
| `position` | Iterator pointing to insertion position. |
| `x` | Element to insert |
| `result` | Storage location of the iterator pointing to the inserted element |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)

# Vector::erase()

Delete an element

## Definition

```
#include <np_cppwebapi.h>
namespace sce {
    namespace Np {
        namespace CppWebApi {
            namespace Common {
                template <typename T>
                class Vector : public VectorVal<T>, public RefObject {
                    int32_t erase(VectorVal<T>::iterator position, VectorVal<T>::iterator & result) __attribute__((warn_unused_result));
                    int32_t erase(VectorVal<T>::const_iterator position, VectorVal<T>::const_iterator<T> & result) __attribute__((warn_unused_result));
                };
            }
        }
    }
}
```

## Description

This function deletes an element from the variable-length array and returns an iterator pointing to the next element.

## Arguments

|  |  |
| --- | --- |
| `position` | Iterator pointing to the element to be deleted. |
| `result` | Storage location of the iterator that points to the next element after the deleted element |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to the "[Return Codes](return-codes.html)" section for details.)