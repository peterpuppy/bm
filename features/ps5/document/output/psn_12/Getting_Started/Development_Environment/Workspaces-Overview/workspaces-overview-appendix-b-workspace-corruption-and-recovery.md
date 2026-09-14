# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/workspaces-overview-appendix-b-workspace-corruption-and-recovery.html

# Workspaces Overview Appendix B - Workspace Corruption and Recovery

When using a workspace for development, corruption on the Target may occur. This can cause error messages to be delivered when attempting to use the workspace.

The following section provides a number of steps that can be taken to help recover the workspace.

Note:

This is not an exhaustive list of fixes, and is not guaranteed to fix every underlying corruption issue.

## Error Messages

The following error messages can be received if a workspace has become corrupted. Each error message in this table indicates which [troubleshooting actions](troubleshooting-actions-for-workspace-corruption-and-recovery.html) should be attempted and in which order.

| **Error Message** | **Recovery Steps** |
| --- | --- |
| Target error - Timed out waiting for the Target to reply. | Try Troubleshooting Actions in the order: [1](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_ozl_wnm_zgc), [2](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_a3k_xnm_zgc) then [3](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_xd4_xnm_zgc). |
| Target Manager Server does not have an open connection for this protocol. | Try Troubleshooting Actions in the order: [2](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_a3k_xnm_zgc) then [1](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_ozl_wnm_zgc). |
| Target Manager Server is busy, and cannot process this request. | Try Troubleshooting Actions in the order: [1](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_ozl_wnm_zgc) then [2](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_a3k_xnm_zgc). |
| Target Manager Server is not connected to the Target. | Try Troubleshooting Actions in the order: [1](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_ozl_wnm_zgc) then [2](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_a3k_xnm_zgc). |
| The operation could not be completed due to unrecoverable corruption. | Try Troubleshooting Actions in the order: [3](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_xd4_xnm_zgc) then [4](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_q3q_xnm_zgc). |
| Operation could not be performed because something required to complete the operation was in use by something else. | Try Troubleshooting Actions number [4](troubleshooting-actions-for-workspace-corruption-and-recovery.html#workspaces-overview_8_2__section_q3q_xnm_zgc). |

# Troubleshooting Actions for Workspace Corruption and Recovery

Full information about the `prospero-ctrl` commands listed here can be found in [Target Manager CLI User's Guide - Controlling Targets Using the Command Line - Controlling Targets with prospero-ctrl](../Target_Manager_CLI-Users_Guide/controlling-targets-with-prospero-ctrl.html).

Some troubleshooting actions will require the Target to be rebooted into Safe mode. For more information on this, refer to [Development Kit Setup Guide - Safe Mode Features](../DevKit-Setup_Guide/safe-mode-features.html) or [Testing Kit Setup Guide - Safe Mode Features](../TestKit-Setup_Guide/safe-mode-features.html).

## (1) The problem may be caused by incorrect state in Target Manager Server

Try the following process:

1. Run the `prospero-ctrl target disconnect` command from the
   command line.
2. If step 1 doesn't improve the situation, ensure all Target Manager UI
   applications are fully closed (for example
   `ProsperoTargetManager.exe`,
   `ProsperoConsoleOutput.exe`), then run `prospero-tm
   shutdown` from the command line, and wait for all
   `prospero-tm.exe` processes to exit safely.
3. If `prospero-tm.exe` doesn't exit 30 seconds after step 2, try to
   kill the `prospero-tm.exe` process.

## (2) The problem may be caused by incorrect Target state or a crash

Try the following process:

1. Attempt a safe reboot from the command line using the `prospero-ctrl
   power reboot` command.
2. If step 1 cannot be completed, run `prospero-ctrl power off
   /force` then `prospero-ctrl power on` from the
   command line.
3. If step 1 or step 2 don't improve the situation, try to unplug the power cable
   from the Target, wait 10 seconds and then plug the power cable back in.

## (3) The problem may be caused by filesystem corruption

Try the following process:

1. Attempt to remove a corrupted
   Standalone
   workspace using the `prospero-ctrl workspace destroy` command, or
   `prospero-ctrl workspace-mirror-purge` for a System Managed
   Host Mirror.
2. If step 1 doesn't improve the situation, boot into safe mode and select option 7
   - **Reset PS5**.
3. If step 2 doesn't improve the situation, boot into safe mode and select option 8
   - **Reset PS5 (Reinstall System Software)**.

## (4) The problem may be caused by resource contention

Try the following process:

1. If there is a game process running, run the `prospero-ctrl process
   kill` command from the command line.
2. If Workspace Explorer is running, close Workspace Explorer.