# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/introduction.html

# Target Manager CLI User's Guide Introduction

Development kits and Testing kits are controlled using Target Manager for PlayStation®5. Development kits (DevKit) and Testing kits (TestKit) are also known as Targets. You can control multiple Targets connected to your network.

Target Manager CLI utilities enable you to control Targets on your network from the command line. Target Manager for PlayStation®5 provides a GUI for these utilities and can be used instead of these utilities.

## Configuration and Log Files

Target Manager Server stores configuration and log files in the `%LOCALAPPDATA%\SCE\PROSPEROTM` folder. This folder also contains kernel crash logs in the format `PROSPEROCrashLog-HwID-DateandTime.log`.

## Long Path Support

Long path support in Target Manager Server is enabled by the Local Group Policy setting:

```
Local Computer Policy -> Computer Configuration -> Administrative Templates -> System -> Filesystem -> Win32 long paths.
```

Note: This setting applies only to Windows applications that have also opted-in for this feature.

## Hardware Support

The following table shows which features are supported by Development Kits (DevKits) and Testing Kits (TestKits), collectively known as Targets, when in various modes.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Development Kit**  **(DevKit)** | | | **Testing Kit (TestKit)** | |
| *Development* | *Assist* | *Release* | *Assist* | *Release* |
| View console output | **Yes** | **Yes** | **Yes** | **Yes** | *No* |
| Connect / Disconnect | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |
| Reboot / Power On / Power Off / Rest Mode | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |
| Safe Mode menu access | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Discover Targets | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |
| Acquire Target settings | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |
| Update system software from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Install / Uninstall package from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Capture screenshot from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Launch application installed on Target from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Launch application stored on Host PC from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Trigger core dump from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Control applications. For example, suspend, resume, or kill. | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Access Host PC file system from Target | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Access Target file system from Host PC | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Create Workspaces | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Delete Workspaces | **Yes** | **Yes** | *No* | **Yes** | *No* |
| Manage Workspaces | **Yes** | **Yes** | *No* | **Yes** | *No* |

Note:

When using a DevKit or TestKit in Release Mode, note that only **Boot Parameters** and **Network (DEV)** settings are available to be acquired.

For more information on setting up DevKits and TestKits, refer to:

* [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html)
* [Testing Kit Setup Guide](../TestKit-Setup_Guide/__document_toc.html)

## Installation

Target Manager for PlayStation®5 and the Target utilities can be installed by using the SDK Manager.

## Related Information

SIE provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements. You can refer to the release notes below:

* [Release Notes - Target Manager for PlayStation®5](../ReleaseNotes/Getting_Started-Target_Manager_Release_Notes.html)