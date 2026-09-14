# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/high-speed-workspace-file-transferring.html

# High Speed Workspace File Transferring

From SDK 5.00 there is an option to increase the file transfer speed. This feature is useful for moving large files to the DevKit.

High Speed Workspace File Transferring can be used with both [Standalone](using-standalone-workspaces.html) and [System Managed Host Mirror](system-managed-host-mirror.html) workspaces.

High Speed Workspace File Transferring can be used with workspaces created with system software older than 5.00 and for workspaces created when the feature was not enabled.

The transfer rate will be improved for the following operations:

* File transfer using `prospero-ctrl workspace push`.
* File transfer using `prospero-ctrl workspace deploy`.
* File transfer using `prospero-ctrl workspace mirror-push`.
* File transfer using `prospero-ctrl workspace mirror-deploy`.
* File transfer from the Host PC to DevKit using Workspace Explorer.
* File transfer using mirroring with the System Managed Host Mirror.
* Bulk copy from USB drive to the workspace.

For further information about bulk copy from USB drive to the workspace, refer to
[System Software User's Guide (Application Development Support) - Application Startup Using the ★Workspace Icon](../System_Software-Users_Guide_for_Development_Support/application-startup-using-the-workspace-icon.html).

## Mechanism

When enabled, High Speed Workspace File Transferring will temporarily store file data in a high speed cache. The data cached is available for read operations, meaning that the ability to read from the application is not affected.

When there is no write operation being performed, the cached data is flushed to the workspace. The empty cache area is then reused for the next write operation.

The data in the cache will never be lost. This means that the following operations may be blocked by up to five minutes until the data has successfully been flushed from the cache to workspace:

* Deleting the workspace, or deleting files existing in the workspace.
* Shutting down the DevKit.
* Putting the DevKit into Rest Mode.
* Booting the DevKit after forcibly powering the machine off.

## Configuring High Speed Workspace File Tranferring

Before turning on High Speed Workspace File Transferring, connect the Host PC and the DevKit with as fast a network connection as possible. A 10Gbps network is recommended.

High Speed Workspace File Transferring is controlled from the system software.

To turn on High Speed Workspace File Transferring:

1. Open the **Target Settings** application, or using the DevKit System Software GUI, open **Settings**.
2. Set **★Debug Settings > System > Enable write cache for high speed workspace file transferring** to **On**.

## Limitations

High Speed Workspace File Transferring has the following limitations.

* High Speed Workspace File Transferring is only available for DevKits. TestKits are not supported.
* High Speed Workspace File Transferring is only available on workspaces hosted on the Console storage. M.2 SSD storage is not supported.
* High Speed Workspace File Transferring will not be actioned until the workspace is released by any action currently using it. Examples of such an action include a running application, on-going file transfer or Workspace Explorer session.
* The DevKit must have System Software 5.00 or newer. If you set up a workspace to use High Speed Workspace File Transferring and then connect to a DevKit running System Software older than 5.00, you will not be able to use that workspace until you update the DevKit to System Software 5.00 or newer.
* When repeatedly updating files in the workspace, you may find that the workspace will become larger than the total size of the files that the workspace contains. Refer to [Hot Loading Support](hot-loading-support-for-workspaces.html) for more information.
* If the write cache is filled, write operations may slow down temporarily until data is flushed to the workspace.