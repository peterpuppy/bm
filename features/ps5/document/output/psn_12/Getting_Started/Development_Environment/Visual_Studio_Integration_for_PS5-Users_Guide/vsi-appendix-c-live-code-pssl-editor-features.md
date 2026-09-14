# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/vsi-appendix-c-live-code-pssl-editor-features.html

# Visual Studio Integration for PlayStation®5 User's Guide Appendix C - Live Code PSSL Editor Features

The PSSL Editor included in VSI has been improved to provide Word Completion and Parameter Information for types and functions defined both in the PSSL source being edited, and in the PSSL Standard Library.

Word Completion is provided for type names, variable names, functions and namespaces. List Completions are also available for members when using instances of structs and classes. Scope Completions are available for namespaces, enums, nested types, and static type members.

## Richer Syntax Coloring

Syntax coloring is extended to include: local and global variables, user types, enumerators, user functions, parameters, fields, methods, and namespaces. The colors used in the editor match the equivalent C++ items under the **Fonts and Colors** dialog.

## Go To Definition

The Go To Definition feature is available for PSSL, and works in a similar way to the feature provided for C++. Place the cursor on the name of a local variable, function parameter, method name etc, and select **Go To Definition** from the context menu to show the location that defines it elsewhere in source.

## Show File Disassembly

You can view the file disassembly for a .pssl file in your project by right clicking and choosing the **Show file Disassembly** option from the menu.

## Limitations

The Live Code Features work by querying the Wave PSSL Compiler in the background, using its information of the source code being edited. Depending on the complexity or size of the PSSL source code, the results provided may be incomplete or incorrect at times. If this becomes an issue when editing source code, they can be disabled.

To disable Live Code features:

1. On the **Tools** menu, click **Options**.
2. Expand **Text Editor**, then **PSSL**, then **Advanced**.
3. Under **Live Code Features**, set **Enable Live Code Features** to **False**, then click **OK**.

When disabled, Word Completion and Parameter Information are limited to just known types and functions provided at global scope in the PSSL Standard Library. List Completions and the Go To Definition features are not available.

Known issues with this release:

* Completions are not supported for anonymous structs and unions:
* Completion information may not always be offered, or be correct for the type in use, depending on context.
* Parameter help is not provided for Template functions, or struct/class constructors.