# Workspace Explorer User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspace_Explorer-Users_Guide/troubleshooting-workspace-explorer.html

# Troubleshooting Workspace Explorer

The following techniques may help if you have issues when running Workspace Explorer.

## Log Files

Workspace Explorer stores log files in the `%LOCALAPPDATA%\SCE\PROSPERO\TMUI\Log` folder. This folder also contains kernel crash logs in the format `PROSPEROCrashLog-HwID-DateandTime.log`.

## Enabling Log File Generation

Log files are generated when the logging severity is set to a value other than **Off**.

The logging severity can be changed on the **About Workspace Explorer for PlayStation®5** dialog via the **Log severity** drop-down list.

| **Log severity** | **Description** |
| --- | --- |
| **Off** | The system logging is switched off. |
| **Error** | The system logging will record only errors. |
| **Info** | The system logging will record errors and events. |
| **Debug** | Note: The system logging will record everything (this option should only be enabled when directed by support as log files may become very large). |