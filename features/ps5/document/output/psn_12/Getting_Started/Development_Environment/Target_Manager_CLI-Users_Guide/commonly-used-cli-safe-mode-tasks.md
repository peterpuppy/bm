# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/commonly-used-cli-safe-mode-tasks.html

# Controlling Safe Mode through prospero-ctrl

Both Development Kits (DevKits) and Testing Kits (TestKits) can be booted into CLI Safe Mode from `prospero-ctrl`. It is then possible to select/run Safe Mode menu items via keyboard input from the Host PC.

This feature is supported in DevKit Development Mode, DevKit Assist Mode and TestKit Assist Mode.

Note:

When in CLI Safe Mode, the Safe Mode screen will be displayed similar to normal Safe Mode operations. However, using the controller will interfere with CLI remote operations, potentially causing unforeseen errors to occur. Please be sure to perform all operations from the Host PC only.

## Booting into Safe Mode

To boot into CLI Safe Mode, run the following command.

```
prospero-ctrl power safe-mode menu
```

The system will boot after this command and display the following in the `prospero-ctrl` output.

```
safemode>
```

## Using CLI Safe Mode

Once in CLI Safe Mode, the system is able to receive keyboard input, and this is reflected in the `prospero-ctrl` output. A list of usable commands can be displayed by entering '`help`' and pressing the enter key.

```
safemode> help
reboot      Restart PS5                            (menu option 1)
video       Change Video Output                    (menu option 2)
repair      Repair Console Storage                 (menu option 3)
update      Update System Software via HTTP        (menu option 4)
restore     Restore Settings or System             (menu option 5 or 7)
rebuilddb   Rebuild Database                       (menu option 6)
clearcache  Clear Cache for System Operations      (menu option 6)
reinstall   Reinstall System Software via HTTP     (menu option 8)
shutdown    Shutdown PS5
settings    Set Settings (single_cable_mode)
network     Test Network Setting
show        Display PUP Build Number
help        Show Help
```

If further details about a command are needed, a detailed explanation can be displayed by entering the command name as a parameter after '`help`' (for example `help update`) and pressing the enter key.

```
safemode> help update
Update $url (menu option 4)
```

## Example of Use

```
update http://192.168.0.100/PS5UPDATE.PUP
```

# Commonly Used CLI Safe Mode Tasks

## Rebooting From CLI Safe Mode

In the `prospero-ctrl` output, enter '`reboot`' and
press the enter key. Safe Mode will exit and the system will be rebooted.

```
safemode> reboot
```

Note:

It is possible to forcibly power off the system from the Host PC whilst in Safe
Mode, however it will re-enter Safe Mode when powered on.
Exit
Safe Mode cleanly using CLI Safe Mode commands.

## Updating System Software From Safe Mode

In the `prospero-ctrl` output, enter '`update <PUP file
URL on HTTP server>`' and press the enter key. System
software will be updated using the update file placed on the HTTP server specified
at `<PUP file URL on HTTP server>`.

```
safemode> update <PUP file URL on HTTP server>
```

Note:

When Single Cable Mode is not enabled, the HTTP server needs to be accessible
from the LAN. When Single Cable Mode is enabled, the HTTP server must be
accessible from the DEV LAN.

For more detail about Single Cable Mode, refer to [Network Overview - Development
Machine Network Configuration - Single Cable Mode](../Network-Overview/single-cable-mode-2.html).

## Rebuilding the Database From Safe Mode

In the `prospero-ctrl` output, enter '`rebuilddb`' and
press the enter key. The database managed by the system will be rebuilt.

```
safemode> rebuilddb
```

# List of CLI Safe Mode Commands

| **Command** | **Explanation** |
| --- | --- |
| `clearcache` | Clears cache for system operations. |
| `help [<command_name>]` | Displays the list of commands supported by CLI Safe Mode.  `<command_name>` - Displays details of the specified command. |
| `network test` | Runs network test. |
| `reboot` | Exits Safe Mode and perform a normal reboot. |
| `rebuilddb` | Rebuilds the database managed by the system. |
| `reinstall <PUP file URL on HTTP server>` | Initializes the system to factory default settings, and performs a system software update using the update file placed on the HTTP server specified at `<PUP file URL on HTTP server>`. |
| `repair` | Repair the console storage. |
| `restore {settings|system}` | * `settings` - Will perform the same as selecting "Settings" > "System" > "System Software" > "Reset Options" > "Reset Your Console" in the system software menu. * `system` - Will return system to initial state. |
| `settings single_cable_mode {on|off}` | Changes Single Cable Mode settings. Changes will be reflected the next time the system is restarted.   * `on` - Enables Single Cable Mode. * `off` - Disables Single Cable Mode. |
| `show` | Displays system software PUP Build Number. |
| `shutdown` | Exits Safe Mode and powers off the system. |
| `update <PUP file URL on HTTP server>` | System software will be updated using the update file placed on the HTTP server specified at `<PUP file URL on HTTP server>`. |
| `video {resetresolution|hdcpauto|hdcp1.4}` | * `resetresolution` - Resets display output resolution to 480p. * `hdcpauto` - Changes HDCP Mode to "Automatic" setting. * `hdcp1.4` - Changes HDCP Mode to "HDCP 1.4 Only" setting. |