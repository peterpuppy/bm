# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/vsi-support-for-clang-fix-it-hints.html

# Building, Running and Debugging an Application in Visual Studio

After you have added source files to your project, you can build, run, and debug projects and solutions in Visual Studio as normal.

## Building an Application

To perform a local build:

* On the **Build** menu, click **Build Solution**.

To perform a distributed build:

* On the **Build** menu, click **Distributed Solution Build**.

For information on command line builds, refer to [Building Projects from the Command Line](building-projects-from-the-command-line.html).

## Running and Debugging an Application

To run an executable:

* On the **Debug** menu, click **Start Without Debugging**.

To debug an executable:

* On the **Debug** menu, click **Start Debugging**.

Note:

On the Debug menu, click **Step Into** or **Step Over** to start the debugger and stop it at the `main` function.

## Debugging with Multiple DevKits

Normally, a single instance of Visual Studio can connect the debugger to a single DevKit. However, it is possible to connect the debugger for a solution with multiple executable projects to a different DevKit for each project by using the **Target** project property.

For more information on setting the **Target** project property, refer to [Debugging](vsi-project-settings-debugging.html) in [Project Settings](project-settings-in-visual-studio.html).

To use multiple projects to debug multiple DevKits:

1. Open a solution with multiple executable projects in an instance of **Visual Studio**.
2. Right click on each project and select **Properties,** or on the **Project** menu, click **Properties**.
3. In the left pane, expand **Configuration Properties**, and then click **Debugging**.
4. In the right pane, edit the **Target Name** property, enter the **DevKit IP** address or host name, and then click **OK**.
5. Repeat steps 2 to 4 above for each executable project in the solution.
6. Right click on the solution and select **Properties**, then select **Startup Project** in the left pane.
7. Select the **Multiple startup projects** radio button.
8. Set the desired executable projects to have the **Start** action then click **OK**.
9. On the **Debug** menu, click **Start Debugging**.

# Viewing Statistical Performance of CPU Instructions using LLVM-MCA

You can view statistical analysis by `llvm-mca` of sections of CPU instructions from your C++ source. It is not possible to perform the analysis directly on the C/C++ source, so you will need to generate an assembly before analyzing.

To view statistical analysis:

1. In **Solution Explorer**, right-click the current source file, then click **Show file Assembly**. A `.s` file will open to display the assembly code that Clang has generated from the C++ source code.
2. Find the corresponding section of interest in the assembly file, then select the region containing just the instructions you want to be analyzed, then select **Analyze Assembly with llvm-mca** from the context menu.

The `llvm-mca` tool will be invoked, and its analysis will be displayed in a new text file.

**Example of llvm-mca analysis output:**

Note:

The output for Assembly generated in Step 1 assumes that Link Time Optimization (LTO) is not used. If LTO is enabled for the current build configuration, the Assembly output generated may not match the instructions that are used in the final executable, and so the analysis by `llvm-mca` could be inaccurate. If this is the case, we recommend using the `llvm-mca` feature in Razor that will generate analysis from live instructions.

To configure llvm-mca settings for projects:

1. On the **Tools** menu, click **Options**.
2. In the left pane, expand **PlayStation**, and then select **General**.
3. In the right pane, make any changes in the **llvm-mca options** section, and then click **OK**.

# Formatting C/C++ Source Code with ClangFormat

You can reformat source code directly from the text editor using the ClangFormat tool.

To format text:

In the currently open source file:

* To format a region of text, right-click, and then choose **Format Selected Text** (or press **Ctrl+R**, **Ctrl+F**).

- OR -

* To format the whole document text, right-click, and then choose **Format Document** (or press **Ctrl+R**, **Ctrl+D**).

The text will be replaced with the output from the prospero-clang-format tool using the current style options. You can control the style options to be used by ClangFormat by specifying the required options in Visual Studio, or by providing a separate configuration file alongside the source being formatted.

Note:

If you have also installed a version of **VSI for PlayStation®4** SDK 7.000 or earlier, then the options left pane will show **ProDG VSI** instead of **PlayStation**. This can be resolved by updating **VSI for PlayStation®4** to a newer version when released.

To control the style options used by ClangFormat:

1. On the **Tools** menu, click **Options**.
2. In the left pane, expand **PlayStation**, and then click **ClangFormat**.
3. In the right pane, you can click **Based On Style** and then select one of the default styles from the drop-down list. You can also optionally select any of the three options that will override relevant settings from the specified **Based On Style** selection (**Specify Bracing Style**, **Format Column Limit** and **Apply Tab Preferences from C/C++ Editor**). You can also specify additional style settings to control formatting options. Alternatively, click **Source Relative ".clang-format" File** to provide style settings in a separate file.
4. Click **OK**.

## ClangFormat

| **Setting** | **Description** | Style Option Names |
| --- | --- | --- |
| **Based On Style** | If selected, enables you to select one of the default styles provided by ClangFormat.  The default is ‘Chromium’. | BasedOnStyle |
| **Specify Bracing Style** | If selected, enables you to select one of the default styles dictating where curly braces should be placed around code blocks. This will override the specified **BasedOnStyle** default value.  The default is ‘Allman’ which places braces on a new line, and indents code blocks. | BreakBeforeBraces |
| **Format Column Limit** | If selected, enables you to specify a column width limit to decide where lines should break. This will override the specified **BasedOnStyle** default value.  The default is ‘160’. | ColumnLimit |
| **Apply Tab Preferences from C/C++ Editor** | If selected, the current settings for the C/C++ Editor will override the specified **BasedOnStyle** defaults. These settings, controlling tab size, indentation, and the use of tabs and spaces will be used during formatting.  The default setting is ‘On’. | TabWidth  IndentWidth  UseTab |
| **Additional Style Settings** | Any additional style settings can be provided to control formatting options. Style information must be in the "`style: value, …`" format used by ClangFormat. |  |
| **Source Relative ".clang-format" File** | If selected, style settings can be provided in a separate `.clang-format` file. This file must be located alongside the source code, or in a parent directory. |  |

# VSI Support for Clang Fix-It Hints

Visual Studio Integration supports Clang's "Fix-It" hints. When enabled VSI will now collect and display any "Fix-It" hints that are generated by the compiler for a compile error.

To enable Fix-It hints:

1. In **Visual Studio**, in the **Project Menu**, click **Properties**.
2. In the **Property Pages** dialog, in the left-hand menu, expand **C/C++** and click **General.**
3. In the right-hand menu, set **Enable Fix-It hints** to **Yes**.
4. Click **Apply**, then **Ok.**

Using Fix-It with VSI

Note:

This process assumes you have the Issues Window visible and your build has failed.

1. The error will be flagged with the **Error icon** and **Fix hint** in the Issues Window and the **Error identifier** and **Fix-It hint** in the Error List and highlighted in the Code Window.
2. In the Code Window, position the Insertion Point over the error, then click the **Caret** drop-down list, or click the "**Show potential fixes**" hyperlink, or press **Alt+Enter**, or press **Ctrl+.** (Ctrl and period).

- OR -

* In the Issue Window, select either the Error message or the Fix hint, then click **Fix** from the shortcut menu, or press **Ctrl+F**.

# Integration Between VSI and other PlayStation® Tools

Visual Studio Integration makes working with a range of tools provided in the PlayStation® Development Environment easier, for example you can view assembly, disassembled or preprocessed files.

To view the assembly for a file:

* In **Solution Explorer**, right-click one or more source files, and then click **Show file Assembly**.

To view the disassembly for a file:

* In **Solution Explorer**, right-click one or more source files, and then click **Show file Disassembly**.

To view the preprocessed source for a file:

* In **Solution Explorer**, right-click one or more source files, and then click **Show file Preprocessed**.

Source files are compiled as necessary and the preprocessed source of the selected files is displayed in a new tab in Visual Studio.

These options will display output for the current build configuration selected in the IDE.

Note:

The output shown for Assembly assumes that Link Time Optimization (LTO) is not being used and the compiler will be performing all optimizations itself. If LTO is enabled for the current build configuration, the shown Assembly output may not match the instructions that are used in the final executable.