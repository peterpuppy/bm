# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-event-property-array-set-float3.html

# Creating and Manipulating Arrays

# SceNpUniversalDataSystemEventPropertyArray

Array

## Definition

```
#include <np.h>
typedef struct SceNpUniversalDataSystemEventPropertyArray SceNpUniversalDataSystemEventPropertyArray;
```

## Description

This structure represents a single array. This structure is used when a function that manipulates arrays is called.

## See Also

`sceNpUniversalDataSystemCreateEventPropertyArray()`, `sceNpUniversalDataSystemDestroyEventPropertyArray()`

# sceNpUniversalDataSystemCreateEventPropertyArray

Create an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemCreateEventPropertyArray(
    SceNpUniversalDataSystemEventPropertyArray **newArray
)
```

## Arguments

|  |  |
| --- | --- |
| `newArray` | [Out] Destination to store the created array |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function creates an empty array.

## Examples

```
SceNpUniversalDataSystemEventPropertyArray *array = NULL;
int ret;

ret = sceNpUniversalDataSystemCreateEventPropertyArray(&array);
if (ret < 0) {
    // Error handling
}
```

## See Also

`sceNpUniversalDataSystemDestroyEventPropertyArray()`

# sceNpUniversalDataSystemDestroyEventPropertyArray

Destroy an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemDestroyEventPropertyArray(
    SceNpUniversalDataSystemEventPropertyArray *array
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In] Array to destroy, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function destroys the array specified in `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` obtained with `sceNpUniversalDataSystemCreateEventPropertyArray()` or specify NULL. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified. This function will do nothing and terminate normally when NULL is specified for `array`.

## Notes

The pointer to `SceNpUniversalDataSystemEventPropertyArray` obtained with `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()` cannot be destroyed with this function because it is pointing to a value that is being assembled in the library.

# sceNpUniversalDataSystemEventPropertyArraySetString

Set a string type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetString(
    SceNpUniversalDataSystemEventPropertyArray *array,
    const char *value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a String type value to the end of the array specified in `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a string type value (UTF-8).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetInt32

Set an int32 type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetInt32(
    SceNpUniversalDataSystemEventPropertyArray *array,
    int32_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds an int32 type value to the end of the array specified with `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify an int32 type value (32-bit signed integer).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetUInt32

Set a uint32 type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetUInt32(
    SceNpUniversalDataSystemEventPropertyArray *array,
    uint32_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a uint32 type value to the end of the array specified with `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a uint32 type value (32-bit unsigned integer).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetInt64

Set an int64 type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetInt64(
    SceNpUniversalDataSystemEventPropertyArray *array,
    int64_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds an int64 type value to the end of the array specified with `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify an int64 type value (64-bit signed integer).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetUInt64

Set a uint64 type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetUInt64(
    SceNpUniversalDataSystemEventPropertyArray *array,
    uint64_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a uint64 type value to the end of the array specified with `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a uint64 type value (64-bit unsigned integer).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetFloat32

Set a Float32 type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetFloat32(
    SceNpUniversalDataSystemEventPropertyArray *array,
    float value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a Float32 type value to the end of the array specified with `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a Float32 type value (32-bit floating point number).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetFloat64

Set a Float64 type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetFloat64(
    SceNpUniversalDataSystemEventPropertyArray *array,
    double value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a Float64 type value to the end of the array specified with `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a Float64 type value (64-bit floating point number).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetBool

Set a bool type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetBool(
    SceNpUniversalDataSystemEventPropertyArray *array,
    bool value
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a bool type value to the end of the array specified in `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a bool type value (boolean).

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetBinary

Set a binary type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetBinary(
    SceNpUniversalDataSystemEventPropertyArray *array,
    const void *value,
    size_t valueSize
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value |
| `valueSize` | [In] Size of value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function adds an element that holds a binary type value to the end of the array specified in `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify a binary type element value. Data of the size specified in `valueSize` will be set as the binary type element value.

The specified value will be copied to the array; it is not a problem to delete it after this function is called.

# sceNpUniversalDataSystemEventPropertyArraySetObject

Set an object type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetObject(
    SceNpUniversalDataSystemEventPropertyArray *array,
    const SceNpUniversalDataSystemEventPropertyObject *value,
    SceNpUniversalDataSystemEventPropertyObject **valuePtr
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value or NULL |
| `valuePtr` | [Out] Destination to store the pointer to the value copied to the array, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function sets an element holding an object type value to the end of the array specified in `array`.

For `array`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified.

For `value`, specify an object type value, in other words a pointer to `SceNpUniversalDataSystemEventPropertyObject` obtained with `sceNpUniversalDataSystemCreateEventPropertyObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified. The same operation as when an empty object is specified will be applied when NULL is specified for `value`.

The specified value and its child elements will all be copied to the array; it is not a problem to delete them after this function is called.

For `valuePtr`, a pointer to the object type value copied to the array will be stored. Specify it if you want to make changes to the copied value after the value is set to the array. Specify NULL for `valuePtr` if this is not required.

## Notes

It is not a problem to add an element to the object type value pointed to by `valuePtr` using `sceNpUniversalDataSystemEventPropertyObjectSetString()` or another function; however, the object type value cannot be deleted using `sceNpUniversalDataSystemDestroyEventPropertyObject()`.

Normally, when you delete the array pointed to by `array`, the object type value pointed to by `valuePtr` will also be deleted. The behavior is undefined when `sceNpUniversalDataSystemEventPropertyObjectSetString()` or another function that manipulates objects is called with the pointer to the deleted value specified. Be careful as there is no method provided for checking whether or not a value has been deleted.

# sceNpUniversalDataSystemEventPropertyArraySetArray

Set an array type element to an array

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyArraySetArray(
    SceNpUniversalDataSystemEventPropertyArray *array,
    const SceNpUniversalDataSystemEventPropertyArray *value,
    SceNpUniversalDataSystemEventPropertyArray **valuePtr
)
```

## Arguments

|  |  |
| --- | --- |
| `array` | [In/Out] Array |
| `value` | [In] Value or NULL |
| `valuePtr` | [Out] Destination to store the pointer to the value copied to the array, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARRAY` | 0x8055311a | Invalid array |

## Description

This function sets an element holding an array type value to the end of the array specified in `array`.

For `array` and `value`, specify a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified. The same operation as when an empty array is specified will be applied when NULL is specified for `value`.

The specified value and its child elements will all be copied to the array; it is not a problem to delete them after this function is called.

For `valuePtr`, a pointer to the array type value copied to the array will be stored. Specify it if you want to make changes to the copied value after the value is set to the array. Specify NULL for `valuePtr` if this is not required.

## Notes

It is not a problem to add an element to the array type value pointed to by `valuePtr` using `sceNpUniversalDataSystemEventPropertyArraySetString()` or another function; however, the array type value cannot be deleted using `sceNpUniversalDataSystemDestroyEventPropertyArray()`.

Normally when you delete the array pointed to by `array`, the array type value pointed to by `valuePtr` will also be deleted. The behavior is undefined when `sceNpUniversalDataSystemEventPropertyArraySetString()` or another function that manipulates arrays is called with the pointer to the deleted value specified. Be careful as there is no method provided for checking whether or not a value has been deleted.