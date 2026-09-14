# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/workspace-dump.html

# Workspace Dump

Workspace dump is a diagnostic feature that captures information about a workspace for analysis by SIE.

A workspace dump captures information about the workspace that the running process is launched from and all workspaces that are mounted as additional content. If no workspace is launched, the system captures information about the most recently launched workspace, enabling a workspace dump to be used for analyzing a workspace that caused a process launch failure.

## Triggering a Workspace Dump

A workspace dump can be triggered from the system software by navigating to "★Debug Settings > System > Trigger Workspace Dump", or by the CLI host tools using:

```
prospero-ctrl diagnostics workspace-dump [/target:<target>]
```

A workspace dump can be triggered at any time. Once triggered, the system will begin the process of generating a workspace dump which will take a few minutes. The system will be restarted automatically during this process.

## Crash Reporting System

After the system has restarted as part of the workspace dump generation, the Crash Reporting System UI will be displayed. This UI can be used to send the workspace dump to SIE in the same way as other system software crashes.

This UI can be disabled to avoid user interaction in scenarios such as automatic testing. To disable this UI set:

* "★Debug Settings > Crash Reporting > Enable System Crash Reporting" to "OFF"
* "★Debug Settings > Crash Reporting > Keep Corefiles" to "ON"

For further information on these settings refer to [Core Dump System Overview - Appendix A: Setting the Core Dump Feature Using Debug Settings](../Core_Dump_System-Overview/ps5-setting-core-dump-feature-using-debug-settings.html).