# System Software User's Guide (Application Development Support) – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-Users_Guide_for_Development_Support/application-startup-using-the-workspace-icon.html

# Application Startup Using the ★Workspace Icon

# Starting Up an Application Saved in a Workspace

An application before package creation that is saved to a workspace in a development machine's console storage or M.2 SSD storage can be started up by selecting the ★Workspace icon.

1. **Prepare the workspace**

   Refer to the [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html) document and create a workspace in the development machine's console storage or M.2 SSD storage. Eight workspaces (workspace0 to workspace7) each can be used from console storage and M.2 SSD storage; note that workspaces with names other than workspace0 to workspace7 will not be startup targets.

   Rename the elf file to start up as eboot.bin and save it in the created workspace.

   Save the system parameter file (param.json) created using the "Param Editor" included in the Publishing Tools in the following folder:

   * /(root directory of the workspace)/sce\_sys/param.json

   Note:

   A system file format error will occur upon application startup when the format of param.json is invalid.
2. **Set the startup target workspace**

   Display the options menu by focusing on the ★Workspace icon on the system software screen and pressing the options button. Select "★Workspace Setting" from the options menu to display a list of workspaces that can be started up (the respective sets consisting of workspace0 to workspace7 from console storage and M.2 SSD storage). The workspace to start up (the workspace whose "Status" is "current") can be changed on this list.

   The list displayed when "★Workspace Setting" is selected includes the following information:

   * Title Name:

     The content of a titleName included in the param.json file is displayed. Regardless of the console language settings, the titleName specified as the defaultLanguage will be displayed.
   * Workspace Name:

     The workspace names of workspace0 to workspace7 are displayed. The workspace names of workspaces that are in M.2 SSD storage will be displayed prefixed with "[M.2]".
   * Title Id:

     The content of the titleId included in the param.json file is displayed.
   * Content Version:

     The content of the contentVersion included in the param.json file is displayed.
   * Status:

     The installation statuses of the workspaces are displayed. The workspace that is set to start up will have its status displayed as "current".

   Note:

   A workspace (workspace0 to workspace7 from either console storage or M.2 SSD storage) can be deleted by focusing on it, pressing the options button, and selecting "UnInstall" from the options menu that is then displayed.
3. **Launch the application**

   Select the ★Workspace icon to start up the application.

   From the launched application, the root directory of the workspace will appear to be mounted as /app0.

   Note:

   If you have used Workspace Explorer to copy the workspace, the startup image will not be displayed when the application is launched. If you have used the feature from "[Batch Copying from a USB Mass Storage Device to Workspaces](starting-up-an-application-saved-in-a-workspace.html#system-software-users-guide-application-development-support_1_1__system-software-users-guide-application-development-support_1_1_4)" described later in this document to copy an application that includes a startup image, the startup image will be displayed when the application is launched. For details about startup images, refer to [Content Information Specifications - Startup Image [Application Information]](../Content_Information-Specifications/startup-image-application-information.html).

## Batch Copying from a USB Mass Storage Device to Workspaces

All directories following the naming scheme from /PS5/workspace/workspace0 to /PS5/workspace/workspace7 on a USB mass storage device can be batch copied to corresponding workspaces in the development machine's console storage (workspaces that don't exist will be created) by selecting the "install all from usb mass storage" button on the "★Workspace Setting" screen. The USB mass storage device must be formatted in the exFAT format or FAT32 format.

Similarly, all directories following the naming scheme from /PS5/workspace/workspace0 to /PS5/workspace/workspace7 on a USB mass storage device can be batch copied to corresponding workspaces in M.2 SSD storage (workspaces that don't exist will be created) by selecting the "install all from usb mass storage to M.2" button. Note, however, that the "install all from usb mass storage to M.2" button cannot be selected if an M.2 SSD is not connected to the development machine.

# Conditions for Using the ★Workspace Icon

The conditions for using the ★Workspace icon feature is indicated below.

|  | **DevKit**  **Development Mode** | **DevKit**  **Assist Mode** | **DevKit**  **Release Mode** | **TestKit**  **Assist Mode** | **TestKit**  **Release Mode** |
| --- | --- | --- | --- | --- | --- |
| Application startup using the ★Workspace icon | Possible | Possible | Not possible | Possible | Not possible |
| Setting/deleting the startup target workspace | Possible | Possible | Not possible | Possible | Not possible |
| Batch copying from a USB mass storage device to workspaces | Possible | Possible | Not possible | Possible | Not possible |

For information of configuring the DevKit, refer to the [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html) document.