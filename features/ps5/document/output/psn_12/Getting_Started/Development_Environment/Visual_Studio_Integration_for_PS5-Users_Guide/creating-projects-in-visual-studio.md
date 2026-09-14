# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/creating-projects-in-visual-studio.html

# Creating Projects and Configurations in Visual Studio

Visual Studio Integration provides project templates for common project types. You can also add new project or solution configurations. The following topics explain how:

* [Creating Projects in Visual Studio](creating-projects-in-visual-studio.html)
* [Build Configurations in Visual Studio](build-configurations-in-visual-studio.html)

# Creating Projects in Visual Studio

To create a new project in Visual Studio 2019, Visual Studio 2022, or Visual Studio 2026:

1. On the **File** menu, point to **New**, and then click **Project**.
2. In the **Create a new project** window, type **PS5** in the search window.
3. Select a project template, then click **Next**.
4. In the **Configure your new Project** window, in the **Project Name** box, type the name of the new project.
5. In the **Location** box, type or browse to the location of the new project, and then click **OK**.
6. Click **Create**.

## Project Templates

There are three types of project templates:

| **Project Template** | **Description** |
| --- | --- |
| **Makefile Project** | Enables you to edit code in Visual Studio, whilst using an external, custom build system. |
| **PS5 Debug only** | Enables you to debug executables not built with the extensions to Visual Studio, but with an external build system. You must select the executable file by using a wizard. To set breakpoints in the source for debugging, you must add the source to the new project by using the Add Existing Item command. |
| **PS5 Project** | The standard template for creating **PlayStation®5** applications, and static or dynamic libraries. The default is an ELF project, select a different project type as required. Refer to [Project Types](creating-projects-in-visual-studio.html#visual-studio-integration-for-ps5-users-guide_1_1__section_mcn_lbv_xgc). |

## Project Types

If the **PS5 Project** template is selected, three project types are available:

| **Project Type** | **Description** |
| --- | --- |
| **ELF project** | Enables you to create an ELF application. |
| **PRX project** | Enables you to create a PRX dynamic library project. After you have built your PRX, it must be dynamically loaded by another module at run time. |
| **Static library project** | Enables you to create a static library project. |

# Build Configurations in Visual Studio

Build configurations enable you to specify multiple versions of solution and project properties, and to switch quickly between them. Build configurations can be created at both the solution and project level.

## Solution Configurations

A solution configuration lists which projects to build and which project configuration they should use.

To manage the solution configurations:

1. On the **Build** menu, click **Configuration Manager**.
2. Set the solution configuration by using the **Active solution configuration** list.
3. Set project configurations by selecting a project, and then using the **Configuration** list.

To add a solution configuration:

1. On the **Build** menu, click **Configuration Manager**.
2. Click the **Active solution configuration** list, and then click **New**.
3. In the **Name** box enter a name for the new solution configuration.
4. In the **Copy** settings from list choose an existing solution to duplicate the settings from if required.
5. Select **Create new project configurations** if you want to add project configurations to each project within the solution with the same name as the solution configuration.
6. Click **OK**.

## Project Configurations

Project configurations specify the settings to use when building an individual project. Adding new project configurations is especially useful when you want to port existing projects to new Targets because you do not need to create new projects.

To add a project configuration:

1. On the **Build** menu, click **Configuration Manager.**
2. In the **Configuration Manager** dialog box, click the **Configuration** list for the project you wish to add a configuration to, and then click **New**.
3. In the **Name** box enter a name for the new project configuration.
4. In the **Copy** settings from list choose an existing project to duplicate the settings from if required.
5. Select **Create new solution configurations** if you want to add a solution configuration to the parent solution with the same name as the project configuration.
6. Click **OK**.