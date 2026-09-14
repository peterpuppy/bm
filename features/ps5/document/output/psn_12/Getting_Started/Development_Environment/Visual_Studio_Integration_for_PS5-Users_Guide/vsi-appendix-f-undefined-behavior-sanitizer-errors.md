# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/vsi-appendix-f-undefined-behavior-sanitizer-errors.html

# Visual Studio Integration for PlayStation®5 User's Guide Appendix F - Undefined Behavior Sanitizer Errors

| **Error** | **Description** |
| --- | --- |
| `Array index out of bounds` | The program has subscripted an array with an index that causes memory outside of the array's bounds to be accessed. |
| `Bit shift overflows` | The program has performed a bit shift that results in a value that cannot be represented by the type that stores it. |
| `Division by zero` | The program has performed a division by zero in integer arithmetic. |
| `Execution reached __builtin_unreachable` | The program's execution has reached a point that was annotated with `__builtin_unreachable`. |
| `Floating point cast overflows` | The program has performed a cast into a destination floating point type that is unable to represent the casted value. |
| `Incorrect alignment assumption` | The program has violated an alignment assumption specified by an `assume_aligned` or `alloc_align` attribute. |
| `Integer arithmetic overflows` | The program has performed an integer arithmetic operation that results in a value that cannot be represented by the type that stores it. |
| `Invalid bit shift exponents` | The program has performed a bit shift with an invalid exponent. This includes cases where the value of the bit shift exponent is negative or larger than the number of bits used to represent the type being bit shifted. |
| `Invalid builtin arguments` | The program has passed a value of 0 to `__builtin_clz` or `__builtin_ctz`. |
| `Invalid values for type` | The program has loaded a value into an object that is not valid for that object's type. This occurs when integer values other than 0 or 1 are stored in an object of type `bool`. |
| `Missing return statements` | The program has returned from a value-returning function without returning a value. |
| `Negative size variable length arrays` | The program has declared a variable length array with a negative number of elements. |
| `Non-null argument was null` | The program has passed a null value as an argument to a function with the `nonnull` attribute or `_Nonnull` annotation. |
| `Non-null return value was null` | The program returned a null value from a function with the `returns_nonnull` attribute or `_Nonnull` annotation. |
| `Null pointer creation` | The program has performed a pointer arithmetic or pointer subscript operation that has resulted in a null pointer. |
| `Pointer arithmetic overflows` | The program has performed a pointer arithmetic or pointer subscript operation that has overflowed. |
| `Use of address with insufficient space` | The program has interpreted an address as an object whose type is larger than the allocation at that address. This error can be detected when the address is used in a load operation, store operation, type cast, bound to a reference, or used as `this` in a member function call. |
| `Use of misaligned address` | The program has interpreted an address as an object whose type alignment requirements are not satisfied by that address. This error can be detected when the address is used in a load operation, store operation, type cast, bound to a reference, or used as `this` in a member function call. |
| `Use of null pointer` | The program has used an address of 0. This error can be detected when the address is used in a load operation, store operation, type cast, bound to a reference, or used as `this` in a member function call. |
| `Value changing implicit conversions` | An implicit conversion in the program has changed the value stored in the destination type as compared to the source type. Typically, this occurs when casting between signed and unsigned integer types. |