# NpUniversalDataSystem Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpUniversalDataSystem-Reference/sce-np-universal-data-system-event-property-object-set-uint3.html

# Creating and Manipulating Objects

# SceNpUniversalDataSystemEventPropertyObject

Object

## Definition

```
#include <np.h>
typedef struct SceNpUniversalDataSystemEventPropertyObject SceNpUniversalDataSystemEventPropertyObject;
```

## Description

This structure represents a single object to attach to an event.

Refer to [NpUniversalDataSystem Library Overview - Using the Library - Sending Events](../NpUniversalDataSystem-Overview/sending-events.html) for the typical procedure to create an event, attach an object, and send the event.

## See Also

`sceNpUniversalDataSystemCreateEventPropertyObject()`, `sceNpUniversalDataSystemDestroyEventPropertyObject()`

# sceNpUniversalDataSystemCreateEventPropertyObject

Create an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemCreateEventPropertyObject(
    SceNpUniversalDataSystemEventPropertyObject **newObject
)
```

## Arguments

|  |  |
| --- | --- |
| `newObject` | [Out] Destination to store the created object |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_ARGUMENT` | 0x80553102 | Invalid argument |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function creates an empty object.

## Examples

```
SceNpUniversalDataSystemEventPropertyObject *object = NULL;
int ret;

ret = sceNpUniversalDataSystemCreateEventPropertyObject(&object);
if (ret < 0) {
    // Error handling
}
```

## See Also

`sceNpUniversalDataSystemDestroyEventPropertyObject()`

# sceNpUniversalDataSystemDestroyEventPropertyObject

Destroy an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemDestroyEventPropertyObject(
    SceNpUniversalDataSystemEventPropertyObject *object
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In] Object to destroy, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |

## Description

This function destroys the object specified in `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` obtained with `sceNpUniversalDataSystemCreateEventPropertyObject()` or specify NULL. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified. This function will not do anything and terminate normally when NULL is specified for `object`.

## Notes

The pointer to `SceNpUniversalDataSystemEventPropertyObject` obtained with `sceNpUniversalDataSystemEventPropertyObjectSetObject()` or `sceNpUniversalDataSystemEventPropertyArraySetObject()` cannot be destroyed with this function because it is pointing to a value that is being assembled in the library.

# sceNpUniversalDataSystemEventPropertyObjectSetString

Set a String type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetString(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    const char *value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a String type value to the object specified in `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a String type value (string) (UTF-8).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

## See Also

`sceNpUniversalDataSystemCreateEventPropertyObject()`

# sceNpUniversalDataSystemEventPropertyObjectSetInt32

Set an int32 type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetInt32(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    int32_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds an int32 type value to the object specified for `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify an int32 type value (32-bit signed integer).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetUInt32

Set a uint32 type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetUInt32(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    uint32_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a uint32 type value to the object specified for `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a uint32 type value (32-bit unsigned integer).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetInt64

Set an int64 type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetInt64(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    int64_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds an int64 type value to the object specified for `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify an int64 type value (64-bit signed integer).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetUInt64

Set a uint64 type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetUInt64(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    uint64_t value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a uint64 type value to the object specified for `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a uint64 type value (64-bit unsigned integer).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetFloat32

Set a Float32 type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetFloat32(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    float value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a Float32 type value to the object specified for `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a Float32 type value (32-bit floating point number).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetFloat64

Set a Float64 type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetFloat64(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    double value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a Float64 type value to the object specified for `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a Float64 type value (64-bit floating point number).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetBool

Set a bool type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetBool(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    bool value
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a bool type value to the object specified in `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a bool type value (boolean).

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetBinary

Set a binary type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetBinary(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    const void *value,
    size_t valueSize
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value |
| `valueSize` | [In] Size of value (in bytes) |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function adds an element that holds a binary type value to the object specified in `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify a binary type element value. Data of the size specified in `valueSize` will be set as the binary type element value.

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

# sceNpUniversalDataSystemEventPropertyObjectSetObject

Set an object type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetObject(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    const SceNpUniversalDataSystemEventPropertyObject *value,
    SceNpUniversalDataSystemEventPropertyObject **valuePtr
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value or NULL |
| `valuePtr` | [Out] Destination to store the pointer to the value copied to the object, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function sets an element that holds an object type value to the object specified in `object`.

For `object` and `value`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified. The same operation as when an empty object is specified will be applied when NULL is specified for `value`.

For `key`, specify the element key (UTF-8).

For `value`, specify an object type value.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called. For an object type value, all of its child elements will also be copied.

For `valuePtr`, the pointer to the object type value copied to the object will be stored. Specify it if you want to make changes to the copied value after the value is set to the object. Specify NULL for `valuePtr` if this is not required.

## Notes

It is not a problem to add an element to the object type value pointed to by `valuePtr` using `sceNpUniversalDataSystemEventPropertyObjectSetString()` or another function; however, the object type value cannot be deleted using `sceNpUniversalDataSystemDestroyEventPropertyObject()`.

Even if you don't explicitly delete it, the existing value will be deleted when a value holding the same key name is set. The behavior is undefined when `sceNpUniversalDataSystemEventPropertyObjectSetString()` or another function that manipulates objects is called with the pointer to the deleted value specified. Be careful as there is no method provided for checking whether or not a value has been deleted.

# sceNpUniversalDataSystemEventPropertyObjectSetArray

Set an array type element to an object

## Definition

```
#include <np.h>
int sceNpUniversalDataSystemEventPropertyObjectSetArray(
    SceNpUniversalDataSystemEventPropertyObject *object,
    const char *key,
    const SceNpUniversalDataSystemEventPropertyArray *value,
    SceNpUniversalDataSystemEventPropertyArray **valuePtr
)
```

## Arguments

|  |  |
| --- | --- |
| `object` | [In/Out] Object |
| `key` | [In] Key |
| `value` | [In] Value or NULL |
| `valuePtr` | [Out] Destination to store the pointer to the value copied to the object, or NULL |

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns a negative value for an error. The main error codes are shown below. (The application must not malfunction even if other error codes are returned.)

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_OUT_OF_MEMORY` | 0x80553101 | Insufficient memory |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_KEY` | 0x80553114 | Invalid key |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_VALUE` | 0x80553115 | Invalid value |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_NOT_INITIALIZED` | 0x80553117 | Not initialized |
| `SCE_NP_UNIVERSAL_DATA_SYSTEM_ERROR_INVALID_OBJECT` | 0x80553119 | Invalid object |

## Description

This function sets an element that holds an array type value to the object specified in `object`.

For `object`, specify a pointer to `SceNpUniversalDataSystemEventPropertyObject` that has been created by `sceNpUniversalDataSystemCreateEventPropertyObject()` or obtained using `sceNpUniversalDataSystemCreateEvent()`, `sceNpUniversalDataSystemEventPropertyObjectSetObject()`, or `sceNpUniversalDataSystemEventPropertyArraySetObject()`. The behavior is undefined when another pointer is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyObject` is specified.

For `key`, specify the element key (UTF-8).

For `value`, specify an array type value, in other words, a pointer to `SceNpUniversalDataSystemEventPropertyArray` that has been created by `sceNpUniversalDataSystemCreateEventPropertyArray()` or obtained using `sceNpUniversalDataSystemEventPropertyObjectSetArray()` or `sceNpUniversalDataSystemEventPropertyArraySetArray()`. The behavior is undefined when another value is specified or when a pointer to an already deleted `SceNpUniversalDataSystemEventPropertyArray` is specified. The same operation as when an empty array is specified will be applied when NULL is specified for `value`.

If the same key element as the specified key is already set to the object, the old value will be deleted, and the new value will be overwritten.

The specified key and value will be copied to the object; it is not a problem to delete them after this function is called. For an array type value, all of its child elements will also be copied.

For `valuePtr`, the pointer to the array type value copied to the object will be stored. Specify it if you want to make changes to the copied value after the value is set to the object. Specify NULL for `valuePtr` if this is not required.

## Notes

It is not a problem to add an element to the array type value pointed to by `valuePtr` using `sceNpUniversalDataSystemEventPropertyArraySetString()` or another function; however, the array type value cannot be deleted using `sceNpUniversalDataSystemDestroyEventPropertyArray()`.

Even if you don't explicitly delete it, the existing value will be deleted when a value holding the same key name is set. The behavior is undefined when `sceNpUniversalDataSystemEventPropertyArraySetString()` or another function that manipulates arrays is called with the pointer to the deleted value specified. Be careful as there is no method provided for checking whether or not a value has been deleted.