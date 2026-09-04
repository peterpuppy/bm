# Sandbox Network Architecture Guide – SDK 13.000

Source: https://game.develop.playstation.net/resources/documents/SDK/latest/Sandbox_Network_Architecture-Guide/sandbox-management-on-devkit-testkit.html

# Managing Sandboxes in DevKit and TestKit

This topic provides an overview of managing PlayStation® environments on DevKits and TestKits. It details the differences between sandboxed and global data management, configuration of network architectures, and considerations when downgrading system software.

## Sandboxed Data and Global Data

Data in DevKit and TestKit consists of files and settings in storage. In Legacy, all files and settings in the console are global data which are shared across all environments (sp-int, prod-qa, and np). In Sandbox, most files and settings are isolated and treated as sandboxed data.

Only a few set of files and settings are shared between sandboxes as global data:

* Application contents (packages, additional content, download data) in USB Extended Storage. Application content in internal SSD and M.2 SSD are sandboxed data.
* Data that persists even when the user initializes the DevKit (installed PUP, etc.)
* Data related to devices physically attached to the DevKit (network settings, Bluetooth® settings, etc.)

Sandboxed Data Vs. Global Data

There are three isolated storage areas in DevKit and TestKit for sandboxed data. RETAIL and Legacy PlayStation® environments use identical files and settings.

## Managing Network Architecture Environments

Note: Currently, the *Network Architecture* setting is not available.

To set the network architecture and environment, do the following:

1. Select PlayStation® environments from **★Debug Settings** > **PlayStation** > **Network Architecture**.
2. Select the **Type**. The default is *Legacy*, allowing you to configure the traditional environments (sp-int, prod-qa, np). Select **Sandbox** to use the PlayStation® environment.
3. Select the **Environment**. If *Type* is set to *Legacy*, this uses Legacy PlayStation® environments. If *Type* is set to *Sandbox*, you can choose from three PlayStation® environments: *DEV*, *CERT*, or *RETAIL*.
4. Click **Set** to apply your changes. The system automatically restarts and launches in the selected environment.

Network Architecture Setting

You can also use `prospero-ctrl` to set the network architecture and environment from your host machine:

```
prospero-ctrl np set-network-architecture NP-SANDBOX DEV
```

The target reboots automatically if the command succeeds.

For details about `prospero-ctrl`, refer to [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html).

## Safe Mode Features in Sandbox

Safe mode initializes either an assigned Sandbox or the entire PlayStation® console, depending on the selected menu option. The table below describes each menu option, its effect, and the scope of that effect.

| Menu Option | Effect | Scope |
| --- | --- | --- |
| Restart PS5 | Reboots without changing the Sandbox assignment. | Console |
| Change Video Output | Changes video output settings of the assigned Sandbox. | Sandbox |
| Repair Console Storage | Repairs the file system across the entire console without changing the Sandbox assignment. | Console |
| Update System Software | Updates System Software without changing Sandbox assignment. Some cache data associated with the assigned Sandbox may also be cleared. | Console and Sandbox |
| Restore Default Settings | Restores settings within the assigned Sandbox. | Sandbox |
| Clear Cache and Rebuild Database | Clears cache and rebuilds the database. Both operations apply only to the assigned Sandbox. | Sandbox |
| Reset PS5 | Initializes the console and resets the console to factory settings. All PlayStation® environments in the console are cleared. | Console |
| Reset PS5 (Reinstall System Software) | Initializes the console, reinstalls the system software, and resets the console to factory settings. All PlayStation® environments in the console are cleared. | Console |

## Downgrading System Software

If you downgrade the system software, change *Network Architecture* to **RETAIL** or select a Legacy PlayStation® environment before downgrading the system software from 13.00 or later versions to a version below 13.00.

Be aware of the following unexpected behaviors that may occur on downgraded versions:

* The following settings, which should be sandboxed data, behave as global data on downgraded versions:

  + console language
  + time settings
  + accessibility settings
  + video output / audio output settings

  Values changed in DEV and CERT appear unchanged on the downgraded version and values modified on the downgraded version persist in DEV and CERT after upgrading back to version 13.00 or later.

* The following settings, which should be global data, behave as sandboxed data on downgraded versions:

  + network settings
  + Bluetooth® pairing information

  Values changed in DEV and CERT appear to be discarded, and any values modified on the downgraded version are also discarded after upgrading back to version 13.00 or later.

If you perform a downgrade without switching *Network Architecture* to *RETAIL* or selecting a Legacy PlayStation® environment, upgrade the console to version 13.00 or later, switch to *RETAIL* or a Legacy PlayStation® environment, then perform the downgrade again.

If you have modified any settings while on the downgraded version, reconfigure them again after upgrading. If no settings were changed in DEV and CERT, no issues will occur.