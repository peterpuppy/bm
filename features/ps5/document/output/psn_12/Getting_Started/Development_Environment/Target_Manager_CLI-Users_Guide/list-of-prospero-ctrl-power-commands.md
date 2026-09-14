# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/list-of-prospero-ctrl-power-commands.html

# Controlling Targets Using the Command Line

Target utilities enable you to control Targets on your network from the command prompt. You can control multiple Targets connected either to your Host PC or via other computers on your network.

Note:

Ensure that your terminal shell (powershell, cmd, etc) uses a code page that supports at least UTF-8 output. If not, characters may not display properly.

Most Windows installations do not use the UTF-8 code page by default in their terminals. You can check the currently active code page using the `chcp` command. You should configure your terminal to use the UTF-8 code page (`chcp 65001`)

## Changing the File-Serving Root Directory

On PlayStation®4, it was possible to change the File Serving Root at the same time as running an ELF file in a single `orbis-run` command.

With PlayStation®5, the process to change File Serving Root is as follows:

1. Disconnect from the Target (`prospero-ctrl target disconnect [/target:<target> ...]`).
2. Change the File Serving Root (`prospero-ctrl target set-fileserving-root
   <path> [/target:<target> ...]`).
3. Reconnect to the Target (`prospero-ctrl target connect [/force] [/target:<target> ...]`).
4. Run the ELF file using `prospero-run`.

# Running Executables with prospero-run

The prospero-run utility (`prospero-run.exe`) enables you to run executables (ELF) from the command prompt. This utility is located in `%SCE_ROOT_DIR%\Prospero\Tools\Target Manager Server\bin` by default.

## Syntax

The `prospero-run` utility has the following syntax:

```
prospero-run [<option> [...]] /elf<input_elf_file> [arg1] [arg2] ...
```

If an argument is repeated, then the last (rightmost) one is used. The exceptions to this rule are `/show` which can be specified multiple times and `/exitOnText` that enables multiple search strings.

Use `prospero-run /help` to display a list of command line options.

Note:

You can also use hyphens (-) instead of slashes (/) to indicate the start of an option.

## List of Options

All option names are case insensitive as are values that are restricted to a predefined list, for example, values for `/elfPathFormat`.

| **Option** | **Description** |
| --- | --- |
| `/app` | Indicates that the rest of the command line is the title ID of the application to run and arguments to pass to it.  Note: It is possible to use both `/app` and `/elf` in the same command, but `/app` must be used first. See the examples of use below. |
| `/console:{all|process|main}` | Console output filter. Use `all` for all channels, `process` (default) for the same output as PlayStation®5 Debugger or `main` for just the main process, excluding any sub-processes. |
| `/contentConfig:<label​>​` | Specifies the content config `<label>` to use when deploying the `<GP5_File>`. |
| `/debug` | Loads the ELF with full debugging enabled. |
| `/elf` | Indicates that the remainder of the command line is the name of the executable to run and any arguments to be passed to it. |
| `/elfPathFormat:{local|workspace|package}` | Indicates whether the path to the ELF is a `local` Windows path (default), the Standalone `workspace` specified by [/workspace](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0workspace), or a path in the installed `package`. |
| `/executableOverlay:<path>` | If `/executableOverlay` is specified, all executable loads by the process (for example `sceSystemServiceLoadExec()`, `sceKernelLoadStartModule()`) will be redirected to the specified host path instead of `/app0/`. |
| `/exitOnText:<msg>` | Checks the ELF process output for the specified `<msg>` and exit if seen.  This argument may be specified multiple times to exit on different `<msg>` values. |
| `/extendedDirectMemory:<size>` | Overrides the extended direct memory size available. `<size>` must be supplied in MiB. |
| `/flexibleMemory:<size>` | Overrides the flexible memory size available. `<size>` must be supplied in MiB. |
| `/gp5File:<GP5_File>` | Specifies a `<GP5_File>` to define the layout of the working directory (`/app0/`).  Note: This argument cannot be specified if [/workingDirectory](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0workingdirectory) or [/mappingFile](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0mappingfile) is specified. |
| `/help`, `/?` | Displays the help message which lists the available options. |
| `/input:<file>` | Sends the contents of `<file>` to the launched process.  By default if `/input` is not used, `stdin` is sent to the launched process. |
| `/kill` | Terminates the process if an exception occurs.  Note: Killing the process can reduce the time Target Manager Server waits for TTY to flush. |
| `/launchOptions[:<file>]` | Specifies a `.ps5launch` options file to use for ELF launch.  This option cannot be used with the `/elfPathFormat`, `/workingDirectory`, `/workspace`, `/gp5File`, `/mappingFile`, `/saveDataRootDirectory`, `/slv`, `/flexibleMemory`, `/nodebug`, `/mirrorMode`, `/storage`, `/elf` or `/app` options.  For more details on `.ps5launch` files, refer to the [Target Manager GUI User's Guide](../Target_Manager_GUI-Users_Guide/__document_toc.html). |
| `/log:<file>` | Logs console output to a `<file>`. |
| `/mappingFile:<file>` | Specifies a path mapping `<file>` to use.  Note: This argument cannot be specified if [/workingDirectory](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0workingdirectory) or [/gp5File](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0gp5file) is specified. |
| `/mirrorMode:{whole-file|on-demand}` | Indicates the Mirroring mode of the System Managed Host Mirror.   * Use `whole-file` (default) to have APR resolve or `sceKernelOpen()` block until whole file is transferred. * Use `on-demand` to enable APR resolve or `sceKernelOpen()` to unblock immediately and transfer data for each read requested by the process. |
| `/nokill` | Prevents Target Manager from terminating the targeted ELF process if the `Ctrl^C` event is used to terminate `prospero-run`. |
| `/noprogress` | Hides the progress of a reboot or load. |
| `/overrideParam:<path>` | If `/overrideParam:<path>` is specified, supported `sce_sys/param.json` parameters for the application launch are loaded from the `param.json` file on the Host PC, rather than the installed package. |
| `/saveDataRootDirectory:<path>` | Specifies a `<path>` to use as an override for the save data root. |
| `/show:<filter>` | Filters the output to only show certain objects.  `<filter>` may be one of:   * `All` * `Basic` * `Modules` * `Threads` * `Files` * `VirtualMemory`   Multiple `/show` entries can be provided to include multiple types of objects. |
| `/slv:{warn|abort}` | Enables System Library Verification.   * If `warn` is specified SLV will generate TTY messages. * If `abort` is specified, SLV will generate an exception. |
| `/storage:{internal|m2}` | If `/workspace` or `/workspaceOverlay` are specified, `/storage` will be selected automatically based on the name of the Standalone workspace.  If a Standalone workspace with the given name exists on both the console ("`internal`") storage and the M.2 SSD storage, `/storage` must be explicitly specified. |
| `/target:<target>` | Specifies a `<target>` to use.  You can use the hostname or IP address that was used to add the Target or its system name. If no Target is specified, the default Target will be used. |
| `/timeout:<secs>` | Maximum number of `<secs>` to wait for the application to exit. |
| `/timestamp` | If `/timestamp` is specified, timestamps are displayed next to each line of console output. |
| `/workingDirectory:<path>` | Sets the working directory of the process to `<path>`.  If this is an empty string or not specified, the ELF load directory will be used. Otherwise this must be a local Windows path.  Note: The specified path must be absolute, not relative.  Note: This argument cannot be specified if [/gp5File](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0gp5file) or [/mappingFile](running-executables-with-prospero-run.html#target-manager-cli-users-guide_1_1__0mappingfile) is specified. |
| `/workspace:<workspace>` | Selects a Standalone `<workspace>` for the lifetime of this process. |
| `/workspaceOverlay:<workspace>` | Overlays files from the Standalone workspace `<workspace>` when running an installed application. Note: Overlaying files in `/app0/sce_sys` is not supported.  This option may only be specified when launching an installed application with `/app`. |

## Examples

Run the executable '`hello_world.elf`' on the Target `DevKit1`:

```
prospero-run /target:DevKit1 /elf hello_world.elf
```

Launch the executable '`hello_world.elf`' on Target `DevKit2` in debug mode and log the console output to a file called '`log_file`':

```
prospero-run /target:DevKit2 /debug /log:log_file /elf hello_world.elf
```

Run the installed application '`ABCD12345`' with the command line arguments `arg1` and `arg2`:

```
prospero-run /app ABCD12345 arg1 arg2
```

Run the installed application '`ABCD12345`' using '`hello_world.elf`' as the main module, and pass the command line arguments `arg1` and `arg2`:

```
prospero-run /app ABCD12345 /elf hello_world.elf arg1 arg2
```

## Exit Codes

The following codes will be returned by `prospero-run`:

| **Return Code** | **Description** |
| --- | --- |
| `240` | Load failed but may succeed after a reboot of the Target |
| `241` | Load failed |
| `242` | The text specified by /exitOnText was seen |
| `243` | Timeout |
| `244` | Process killed |
| `245` | Process stopped |
| `246` | Target in use |
| `247-254` | Reserved for future use |
| `255` | Some other error occurred |

Otherwise the game exit code is returned.

# Controlling Targets with prospero-ctrl

The `prospero-ctrl` utility (`prospero-ctrl.exe`) enables you to control Targets from the command prompt. This utility is located in `%SCE_ROOT_DIR%\PROSPERO\Tools\Target Manager Server\bin` by default.

## Syntax

```
prospero-ctrl <group> <command> [<option> ...]
```

`prospero-ctrl` requires both `<group>` and `<command>` arguments except when using `help` or `interactive`. Refer to [Common Commands](controlling-targets-with-prospero-ctrl.html#target-manager-cli-users-guide_1_2__section_m1f_kjg_zgc) for more information.

Use `prospero-ctrl ?` or `prospero-ctrl help` to display a list of the command groups.

Use `prospero-ctrl help
<group>` to display a list of command line options for the command group.

The help text for a command may contain arguments which are within square brackets, angled brackets or braces. The help text syntax can be interpreted as follows:

* Square Brackets `[ ]`: Indicate that the argument is not mandatory for the command to function. Arguments which are not shown in square brackets are mandatory and positional. An ellipsis before the closing square bracket indicates that you can supply more than one instance of that argument.
* Angled Brackets `< >`: Indicate parts of the argument which can be replaced with whatever text is appropriate for your needs. Each argument in angle brackets supports a single space-delimited value. If you need to supply a value containing spaces, it must be placed in quotes.
* Braces `{ }`: Indicate parts of the argument where one or more options from a predefined set must be specified. The possible options are separated by the pipe "`|`" character.

For example, the "`prospero-ctrl target example-command`" help shows that the following arguments are available:

```
target example-command <file> [/setting:{ALPHA|BETA}] [</target:<target>]
```

* The positional argument "`<file>`" is mandatory and must be supplied immediately after "`example-command`".
* The "`/setting:`" argument is optional and must be specified as either: "`/setting:ALPHA`" or "`/setting:BETA`".
* The "`/target:`" argument is optional, and can accept any Target name or IP address you want the command to operate on.
* The two optional arguments do not need to be supplied in a specific order.

Note: If there are commands which do not follow the specific rules described above, it is noted in the help text of the individual command.

Note: You can press **Ctrl+C** to stop continuous `prospero-ctrl` commands such as `controller record`.

## Common Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `help [<group> [<command>]|<command>|ALL]` | Displays the general help file or help on a specified group of commands or individual command. Using `help ALL` will display help for every command in every group. |
| `interactive` | Executes `prospero-ctrl` in `REPL/interactive` mode.  Note: REPL mode enables you to type commands without having to start new instances of `prospero-ctrl.exe`. |

## Common Options

| **Option** | **Description** |
| --- | --- |
| `[/target:<target>]` | Option to run the command on a specific Target. If no `/target` is specified, the command will be run on the default Target. |
| `[/target:<target> ...]` | Option to run the command on one or more Targets.  `/target` can be specified multiple times to run the command on multiple Targets.  For example `/target:T1 /target:T2`  If no `/target` is specified, the command will be run on the default Target. Use `'*'` for all Targets. |
| `<application>` | Option to target a specific application.  Replace `<application>` with one of the following:   * The Application ID of the application. * The Name of the application. * The Title ID of the application. * The Process ID of the application. |
| `<process>` | Option to target a specific process.  Replace `<process>` with one of the following:   * The Process ID of the process. * The Name of the process. |
| `[/noprogress]` | Option to prevent progress bars from being displayed while running a command. |

`<target>` is either the hostname or IP address or System name of the Target.

`<target>` is first matched against the hostname or IP addresses of the Targets in Target Manager’s Target list, then against the system names.

## Exit Codes

The following codes will be returned by `prospero-ctrl`:

| **Return Code** | **Description** |
| --- | --- |
| `0` | Success |
| `255` | Error |

Otherwise, the game exit code is returned.

Note:

If an operation applies to multiple Targets, `prospero-ctrl` will return 255 if any instance fails.

## Display Terminology

In the SDK documentation, the terminology `'DEBUG SUSPENDED'` corresponds to `'Frozen'` in the `prospero-ctrl` output.

## Case Sensitivity when File Serving

File serving is case insensitive by default. The case sensitivity can change in the following situations:

* A TM API command is received to change sensitivity.

# List of prospero-ctrl Command Groups

prospero-ctrl commands are organized into related groups of commands:

| **Group** | **Purpose** |
| --- | --- |
| [`application`](list-of-prospero-ctrl-application-commands.html) | Commands related to an application running on or to be run on the Target. |
| [`controller`](list-of-prospero-ctrl-controller-commands.html) | Commands related to controller inputs. |
| [`diagnostics`](list-of-prospero-ctrl-diagnostic-commands.html) | Commands related to Target diagnostic information. |
| [`filesystem`](list-of-prospero-ctrl-filesystem-commands.html) | Commands related to the filesystem of the Target. |
| [`kitmanager`](list-of-prospero-ctrl-kitmanager-commands.html) | Commands related to the use of the Kit Manager system. |
| [`network`](list-of-prospero-ctrl-network-commands.html) | Commands related to the network connection of the Target. |
| [`package`](list-of-prospero-ctrl-package-commands.html) | Commands related to a package running on or to be run on the Target. |
| [`playgo`](list-of-prospero-ctrl-playgo-commands.html) | Commands related to PlayGo data. |
| [`power`](list-of-prospero-ctrl-power-commands.html) | Commands related to the power status of the Target. |
| [`process`](list-of-prospero-ctrl-process-commands.html) | Commands related to the running process on the Target. |
| [`process-dump`](list-of-prospero-ctrl-process-dump-commands.html) | Commands related to a process dumpfile. |
| [`psn`](list-of-prospero-ctrl-psn-commands.html) | Commands related to PlayStation™Network operations. |
| [`savedata`](list-of-prospero-ctrl-savedata-commands.html) | Commands related to save data on the Target. |
| [`settings`](list-of-prospero-ctrl-settings-commands.html) | Commands related to the Target settings. |
| [`target`](list-of-prospero-ctrl-target-commands.html) | General commands related to Target management. |
| [`user`](list-of-prospero-ctrl-user-commands.html) | Commands related to managing users and accounts for PlayStation®5 on a Target. |
| [`video`](list-of-prospero-ctrl-video-commands.html) | Commands for configuring video stream output from a Target. |
| [`workspace`](list-of-prospero-ctrl-workspace-commands.html) | Commands related to workspace management on the Target. |

# List of prospero-ctrl application Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `application delete-all-passcodes` | Deletes all the stored passcode fingerprints that are used for mounting application data. |
| `application delete-data {TROPHY|UDS} {CONSOLE|ALL} [/user:<user>] [/target:<target>]` | Deletes the specified type(s) of application data for all titles from the specified locations.  If data is only deleted from the console, it is deleted for all users unless a username or user ID is specified using `<user>`.  If data is deleted from all locations, it is removed from both the console and server, and `<user>` must be specified.  Note: Refer to [NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html) and [Trophy System Overview - Debugging Support Provided by the System Software](../Trophy_System-Overview/debugging-support-provided-by-the-system-software.html) for more details. |
| `application delete-passcode <titleId>` | Deletes the stored passcode fingerprints that are used for mounting the `<titleId>`'s application data. |
| `application info <application> [/target:<target>]` | Displays detailed information about the given application. `<application>` may be either a Title ID, Application ID, Application Name or Process ID. |
| `application kill <application> [/target:<target>]` | Kills the `<application>` and all its associated processes. |
| `application list [/target:<target>]` | Lists the debuggable applications on the default Target or specified `<target>`.  For each application the following data is returned:   * `Name` - The `appName` of the application. * `titleId` - The `titleId` of the application. * `Id` - The `appId` of the application. * `Processes` - Lists the processes associated with the application identified by ProcessID (`pid`). |
| `application list-passcodes` | Lists the stored passcode fingerprints for each application. |
| `application mount-data <titleId> [/fingerprint:<fingerprint>] [/target:<target>]` | Mounts the application data of the specified title so it can be accessed from the Host PC.   * `<titleId>` - The Title ID for the given application.   `/fingerprint` - Sets the passcode for the application to be mounted.  The passcode `<fingerprint>` can be obtained from the Publishing Tools. Refer to [Publishing Tools Command Line Version User's Guide - Commands for Other Files - pc\_fingerprint Command](../Publishing_Tools_CL-Users_Guide/pcfingerprint-command.html) for more information.  Note: A `/fingerprint` may be required the first time application data for each `<titleID>` is mounted, after which the passcode fingerprint value will be stored, and may be omitted. The fingerprint is not required to mount application data if the package has been uninstalled. |
| `application resume <application> [/target:<target>]` | Resumes the `<application>` on the default Target or specified `<target>`. |
| `application set-passcode <titleId> <fingerprint>` | Stores the passcode `<fingerprint>` for mounting the application data of the specified `<titleId>`. |
| `application start <titleId> [/elf:<elf>] [/elfPathFormat:{LOCAL|PACKAGE}] [/executableOverlay:<path>] [/flexibleMemory:<size>] [/extendedDirectMemory:<size>] [/nodebug] [/overrideParam:<path>] [/workspaceOverlay:<workspace>] [/storage:{internal|m2}] [/target:<target>] [/args <arg> ...]` | Starts the application `<titleId>` on the default Target or specified `<target>`.  If `/elf` is specified and `/elfPathFormat` is either not specified or `LOCAL`, the ELF file on the Host PC will be launched instead of `eboot.bin` from the installed package.  If `/elf` is specified and `/elfPathFormat` is `PACKAGE`, the ELF file from installed package will be used instead of `eboot.bin`.  If `/executableOverlay` is specified, all executable loads by the game process (for example, `sceSystemServiceLoadExec()` or `sceKernelLoadStartModule()`) will be redirected to the specified host path instead of `/app0/`.  `/flexibleMemory` - Overrides the flexible memory size available to the application. `<size>` must be supplied in MiB.  `/extendedDirectMemory` - Overrides the extended direct memory size available to the application. `<size>` must be supplied in MiB.  `/nodebug` - Identifies the process to be spawned is not debuggable.  `/overrideParam:<path>` - loads system parameters from the `param.json`file on the Host PC, rather than the installed package. Note: Not all parameters can be overridden. Refer to [Param.json File Specification - Using the Param File (param.json) - Overriding the Param File of the Application Package (Application Development Support)](../Param_Json-Specification/overriding-the-param-file-of-the-application-package-applica.html) for the full list of possible parameters. If you try to override a restricted parameter, an error message will be displayed.  `/workspaceOverlay` - Overlays files from a Standalone Workspace. Overlaying files in /app0/sce\_sys is not supported.  `/storage` - If `/workspaceOverlay` is specified, `/storage` will be selected automatically unless a standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  `/args <arg> ...` - Specifies any argument(s) required to run the application. Multiple arguments can be added after `/args` and any arguments will be sent to the application exactly as written.  Note: `/args` must be the last option specified for the command. |
| `application suspend <application> [/target:<target>]` | Suspends the `<application>` on the default Target or specified `<target>`. |
| `application system-event <application> [/link:<url>] [/target:<target>]` | Trigger a system event for an `<application>` on the default Target or specified `<target>`.  `/link` is used to supply a deeplink URL in psgm format. |
| `application unmount-data<titleId> [/target:<target>]` | Unmounts the application data of the specified `<titleId>` installed on the default Target or specified `<target>` from the Host PC. |

# List of prospero-ctrl controller Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `controller capture-to-json <capturefile> <jsonfile> [/delta]` | Converts a Controller Capture format `<capturefile>` to a JSON capture `<jsonfile>`.  `/delta` - Enables **delta mode** where only differences from the previous frame will be written to the output.  Note: A capture can be a combination of controller, keyboard and mouse inputs. |
| `controller json-to-capture <jsonfile> <capturefile>` | Converts a source JSON capture `<jsonfile>` to a Controller Capture format `<capturefile>`.  Note: The command expects an input file containing a single array of JSON controller capture events, such as a file generated by the command '`prospero-ctrl controller capture-to-json`'.  Note: A capture can be a combination of controller, keyboard and mouse inputs. |
| `controller playback <file> [/noskip] [/nowait] [/target:<target>]` | Play the controller events stored in `<file>` on the default Target or specified `<target>`.  Note: `<file>` can be filename, or path and filename. The `.ps5ctrlp` extension will be added automatically if an extension is not provided. `<file>` must exist on the Host PC.   * `/noskip` - By default, the playback automatically skips the time delay before the first event in the file. Adding `/noskip` turns off this functionality.   Note: Adding `noskip` may cause a long delay before the first event is played back.   * `/nowait` - By default, this command will wait for playback to complete before ending. Adding `/nowait` will end this command once the playback data has been transferred to the Target. |
| `controller record <file> [/device:{all|controller|mouse|keyboard|vrcontroller} ...] [/deadzone:<value>] [/overwrite] [/target:<target>]` | Records controller events on the default Target or specified `<target>` and outputs the data to `<file>`.  `/device:` - Specifies which controllers to record from.   * `all` - Records inputs from all configured input devices. * `controller` - Records inputs from controller only. * `mouse` - Records inputs from the mouse only. * `keyboard` - Records inputs from the keyboard only. * `vrcontroller` - Records inputs from the vr controller only.   Default is `all`.  Note: `/device` can be specified multiple times.  E.g. `/device:mouse /device:keyboard`    `/deadzone` - Sets the dead zone filtering for the controller analog sticks.   * `<value>` can be any value in the range `0 -> 127`. Default is `13`.   `/overwrite` - Sets this command to overwrite existing files.  Note: Recording stops when **Ctrl+C** is hit. |

# List of prospero-ctrl diagnostics Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `diagnostics clear-logs [/tool:{CONSOLE-OUTPUT|CONTROLLER-CAPTURE|DEBUGGER|GP5-EDITOR|HDR-SCOPES|MEMORY-ANALYZER|PARAM-EDITOR|PUBTOOL-GUI|RAZORCPU|RAZORCPU-LIVE|REMOTE-VIEWER|RV-SERVER|SCREEN-CAPTURE|TARGET-MANAGER|TARGET-SETTINGS|TASKBAR-APP|TM-EXPLORER|TM-SERVER|VSI|WFM-DRIVER|WORKSPACE-EXPLORER} ...]` | Attempts to delete any existing log file data for the specified host tools.  `/tool` may be specified multiple times to delete log file data for multiple tools.  E.g. `/tool:DEBUGGER /tool:TARGET-MANAGER`  If `/tool` is not specified, then log file data will be deleted for all tools.  Note: Some logs may not be able to be cleared because the respective tool still has a handle on the file. These deletion errors will be displayed but will not interrupt the deleting of other logs. |
| `diagnostics clients` | Displays a list of TM API clients currently running on Target Manager Server. |
| `diagnostics collect-logs <file>` | Collects log information for installed tools and then packages the logs into a .zip archive named `<file>`, which can be shared with Developer Support. |
| `diagnostics cp-dump <file> [/target:<target>]` | Generate a Communication Processor (CP) log, and write it to the specified `<file>`. |
| `diagnostics dump-title-metadata <file> [/titleID:<titleId>] [/fingerprint:<fingerprint>] [/target:<target>]` | Dumps APR metadata for the specified installed package to `<file>` so that it can be sent to SIE for analysis.  `/titleId` - Sets the package to dump APR metadata from. If `/titleId` is not specified, metadata will be dumped for the currently running application.  `/fingerprint` - Sets the passcode for the application to be mounted. The passcode `<fingerprint>` can be obtained from the Publishing Tools. Refer to [Publishing Tools Command Line Version User's Guide - Commands for Other Files - pc\_fingerprint Command](../Publishing_Tools_CL-Users_Guide/pcfingerprint-command.html) for more information.  Note: A `/fingerprint` is required the first time application data for each `<titleID>` is mounted, after which the passcode fingerprint value will be stored, and may be omitted. |
| `diagnostics dump-workspace-metadata <file> [{/guid:<guid>|/workspace:<workspace>}] [/target:<target>]` | Dumps APR metadata for the specified workspace to `<file>` so that it can be sent to SIE for analysis.  `/guid` - Specifies the `<guid>` for the System Managed Host Mirror Workspace from which the metadata will be dumped.  `/workspace` - Specifies the standalone `<workspace>` from which the metadata will be dumped.  Note: If neither `/guid` nor `/workspace` are specified, metadata for the current Host PC's System Managed Host Mirror Workspace will be dumped. |
| `diagnostics get-server-logging-level` | Gets the logging level used by Target Manager Server. |
| `diagnostics hdmi-dump <file> [/target:<target>]` | Generates a diagnostic dump of HDMI data from the default Target or specified `<target>` and writes it to the specified `<file>`. This data may be sent to SIE for investigation of HDMI-related issues. |
| `diagnostics health-check [/mode:{quick|full}] [/noreport] [/target:<target>]` | Run a Target connectivity health check on the default Target or specified `<target>`.  By default this will run in `quick` mode, `full` mode may be optionally specified to run more detailed checks, which may take a long time and change the state of the Target.  If the health check fails, diagnostic information will be collected in a file generated by this tool in the current working directory. This file will have a filename of the format `diag-<IP/Hostname>-YYMMDDHHMMSS.zip`  If `/noreport` is specified, diagnostic information will only be written to `STDOUT`. |
| `diagnostics installed-tools [/format:{XML|YAML}] [/filename:<file>]` | Lists details of the currently installed PlayStation®5 SDK tools. By default this is output to `STDOUT` in `YAML` format, but can optionally be output to `<file>`.  `/format` - Sets the output format if outputting to a file. There are two options available.   * `XML` - Sets the output file format to `XML` * `YAML` - Sets the output file format to `YAML`   `/filename` - Sets the name of the `<file>` to be used if outputting to a file. |
| `diagnostics io-dump <file> [/target:<target>]` | Generate an I/O controller log from the default Target or specified `<target>` and write it to the specified `<file>`. |
| `diagnostics io-dump-upload [/target:<target>]` | Generate an I/O controller log for upload to the Crash Reporting System.  The Target will generate a dump, power itself off and the core dump file will be automatically uploaded to SIE the next time the Target is booted. |
| `diagnostics monitor [/target:<target>]` | Monitor notifications from the default Target or specified `<target>`. |
| `diagnostics pcap-begin <file1> [/file2:<file2> /size:<mb>] [/target:<target>]` | Starts logging Target communications for the default Target or specified `<target>`.  Use `pcap-begin /target:*` to log communications for all available Targets.  If `/file2:<file2>` is specified, logging will alternate between `<file1>` and `<file2>` after reaching specified log `/size` in mebibytes. |
| `diagnostics pcap-end [/target:<target>]` | Stops logging all communications for the default Target or specified `<target>`.  Use `pcap-end /target:*` to stop logging communications for all available Targets. |
| `diagnostics set-debug-agent-logging {ERROR|MINIMAL|VERBOSE} {PCAP|TTY} [/target:<target>]` | Set the Debug Agent logging configuration for the default Target or specified `<target>`.   * `ERROR` - Sets logging level to log only Errors. * `MINIMAL` - Sets logging level to minimum. * `VERBOSE` - Sets logging level to maximum.  * `PCAP` - Logs to network packet capture (for example `prospero-ctrl diagnostics pcap-start`). * `TTY` - Logs to Console output (for example `prospero-ctrl target console`).   Note: Changes made by this command will be reset when the Target is rebooted or powered off. |
| `diagnostics set-filesystem-agent-logging {ERROR|MINIMAL|VERBOSE} {PCAP|TTY} [/target:<target>]` | Set the FileSystem Management Agent logging configuration for the default Target or specified Target.   * `ERROR` - Sets logging level to log only Errors. * `MINIMAL` - Sets logging level to minimum. * `VERBOSE` - Sets logging level to maximum. * `PCAP` - Logs to network packet capture (for example `prospero-ctrl pcap`). * `TTY` - Logs to Console output (for example `prospero-ctrl console`).   Note: Changes made by this command will be reset when the Target is rebooted or powered off. |
| `diagnostics set-server-logging-level {DEFAULT|FULL}` | Sets the logging level used by Target Manager Server to either `Default` or `Full`.  Note: Use when requested by Support only. |
| `diagnostics show-usage [/target:<target>]` | Displays stream usage information for the default Target or specified `<target>`. |
| `diagnostics start-logging [/tool:{CONSOLE-OUTPUT|CONTROLLER-CAPTURE|DEBUGGER|GP5-EDITOR|HDR-SCOPES|MEMORY-ANALYZER|PARAM-EDITOR|PUBTOOL-GUI|RAZORCPU|RAZORCPU-LIVE|REMOTE-VIEWER|RV-SERVER|SCREEN-CAPTURE|TARGET-MANAGER|TARGET-SETTINGS|TASKBAR-APP|TM-EXPLORER|TM-SERVER|VSI|WFM-DRIVER|WORKSPACE-EXPLORER} ...]` | Starts generating verbose log information for the specified host tools.  `/tool` may be specified multiple times to generate verbose logs for multiple tools.  E.g. `/tool:DEBUGGER /tool:TARGET-MANAGER`  If `/tool` is not specified, then verbose logging is enabled for all tools.  Note: Some tools may require programs to be closed in order for their log level change to take effect. |
| `diagnostics stop <pid>` | Stops a specific `prospero-ctrl` process, identified with `<pid>`.  Note: Cannot be used to stop an interactive session. |
| `diagnostics stop-logging [/tool:{CONSOLE-OUTPUT|CONTROLLER-CAPTURE|DEBUGGER|GP5-EDITOR|HDR-SCOPES|MEMORY-ANALYZER|PARAM-EDITOR|PUBTOOL-GUI|RAZORCPU|RAZORCPU-LIVE|REMOTE-VIEWER|RV-SERVER|SCREEN-CAPTURE|TARGET-MANAGER|TARGET-SETTINGS|TASKBAR-APP|TM-EXPLORER|TM-SERVER|VSI|WFM-DRIVER|WORKSPACE-EXPLORER} ...]` | Disables verbose logging for the specified host tools.  `/tool` may be specified multiple times to disable verbose logs for multiple tools.  E.g. `/tool:DEBUGGER /tool:TARGET-MANAGER`  If `/tool` is not specified, then verbose logging is disabled for all tools.  Note: Some tools may require programs to be closed in order for their log level change to take effect. |
| `diagnostics system-dump [/target:<target>]` | Writes system coredump file(s) to `/devlog/system/sce_coredumps/…` on the default Target or specified `<target>`. |
| `diagnostics version` | Displays the version information for Target Manager Server and components. |
| `diagnostics workspace-dump [/target:<target>]` | Trigger a diagnostic core dump file for the currently mounted, or most recently mounted Workspace.  The Target will automatically reboot after the core dump file is generated.  The core dump file may be uploaded to SIE from the System Software UI. |
| `diagnostics workspace-performance{NETWORK|WORKSPACE|MIRROR|FULL} [/target:<target>]` | Tests Workspace performance for the default Target or specified `<target>`.   * `NETWORK` - Tests the host's network send/receive speed. * `WORKSPACE` - Tests the Target's write speed to a Standalone workspace. * `MIRROR` - Tests the Target's write speed to a System Managed Host Mirror workspace. * `FULL` - Runs all tests. |

# List of prospero-ctrl filesystem Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `filesystem delete <target_path> [/recursive] [/target:<target>]` | Deletes files at a given *<target\_path>* on the default Target or specified `<target>`.  `/recursive` will delete the folder structure in addition to the files. Note: `<target_path>` must be a unix-style path on the Target, e.g. "`/devlog/app/myfile.bin`", not a path on the Host PC's filesystem. |
| `filesystem get <target_path> <local_path> [/target:<target>]` | Retrieves the file or directory from `<target_path>` on the default Target or specified `<target>` and writes it to the Host PC as *`<local_path>`*.  If `<target_path>` is a file, and `<local_path>` represents an existing directory on the Host PC, the file will be written to that directory. Note: `<target_path>` must be a unix-style path on the Target, e.g. "`/data/myfile.bin`", not a path on the Host PC's filesystem. |
| `filesystem list <target_path> [/target:<target>]` | Lists the files and directories at a given path on the default Target or specified `<target>`. Note: `<target_path>` must be a unix-style path on the Target, e.g. "`/devlog/app/myfile.bin`", not a path on the Host PC's filesystem. |
| `filesystem map <drive> [/display`:`{ip|name}]` | Maps the Target file system to a drive letter on the Host PC.   * `<drive>` - The drive letter on the   Host PC to which you wish to map Target file systems.   `/display` controls how mapped Target folders appear in the host-side directory tree. If this is not specified, the previous setting is used or IP on first use.   * `ip` - Names the folder using the next available   identification in the order IP -> hostname -> Target   Name. * `name` - Names the folder using the next   available identification in the order Target Name -> hostname   -> IP.   Refer to [Target Manager GUI User's Guide - Using Target Manager to Manage Targets - Accessing the File System of Targets](../Target_Manager_GUI-Users_Guide/accessing-the-file-system-of-targets.html). |
| `filesystem put <local_path> <target_path> [/target:<target>]` | Writes the file or directory contents (recursively) from `<local_path>` on the Host PC to the `<target_path>` on the default Target or specified `<target>`. Note: `<target_path>` must be a unix-style path on the Target, not a path on the Host PC's file system. For example, `/ABCD12345/savedata/slot001`. "ABCD12345" in this example represents a title ID for some mounted application data. For more information, refer to [Target Manager GUI User's Guide - Using Target Manager to Manage Targets - Accessing the File System of Targets](../Target_Manager_GUI-Users_Guide/accessing-the-file-system-of-targets.html). |
| `filesystem unmap` | Unmaps all mapped Target file systems. |

# List of prospero-ctrl kitmanager Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `kitmanager acquire <name> [/wait:<wait>]` | Acquires a Target from the Kit Manager Server pool for the Virtual Target `<name>` in Target Manager Server's Target List.  `/wait` may be optionally specified to indicate the maximum length of time in seconds the request should wait for a Target in the pool to become available (not including the time required to apply the Target configuration after it is acquired). |
| `kitmanager login <url> [/username:<username>] [/password:<password>] [/service:{OKTA|GITHUB}] [/nobrowser]` | Allows the Host PC to use the Kit Manager Server hosted at `<url>`, optionally using the supplied username and password.  The `<url>` should be preceded by either **http://** (for a non-secure connection) or **https://** (for a secure connection), followed by the server address. The server address can be either an IP address or a hostname, followed by an optional port number. If not specified, the default port number of 50051 is used.  If `/username` and `/password` are omitted, the command will request user credentials interactively.  The `/service` option is used to authenticate via OAuth2 using the specified provider. Note: `/username` and `/password` are mutually exclusive with `/service`.  If in environments without a browser, `/nobrowser` can be used to output the authorization URL which the user can enter into a browser of their choice to perform authentication. |
| `kitmanager logout` | Logs this Host PC out of the Kit Manager Server. Any Virtual Targets in pools associated with this server will no longer be available. |
| `kitmanager pool-list` | Lists all available pools on the Kit Manager Server. |
| `kitmanager release <name>` | Releases an acquired Virtual Target back to the pool. |
| `kitmanager resource-templates-list` | Lists all available Resource Templates on the Kit Manager Server. |
| `kitmanager target-add <name> [/pool:<pool>] [/template:<template>] [/template-file:<template-file>]` | Adds a new Virtual Target to Target Manager Server's Target List associated with a Kit Manager Server pool.  `/pool` may be omitted if there is only one pool associated with the currently logged-in user.  To use a Resource Template to define the Virtual Target, use one of the following:  * `/template` to supply the name of the Template `<template>` on the Kit Manager Server. * `/template-file` to supply a full file path `<template-file>` to the Resource Template accessible on the Host PC.   Note: `/template` and `/template-file` are mutually exclusive. |
| `kitmanager target-delete <name>` | Deletes a Virtual Target added from a Kit Manager Server. |

# List of prospero-ctrl network Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `network get-devlan-settings [/target:<target>]` | Displays the current values of the DevLan Settings for the default Target or specified `<target>`. |
| `network get-nat-traversal-info [/target:<target>]` | Displays the NAT Traversal information for the default Target or specified `<target>`. |
| `network get-network-emulation-preset <option> [/output:<file>] [/target:<target>]` | Get one of the three system-wide preset network emulation options.  `<option>` - Sets the network emulation preset. The valid range is `1` to `3`.  `/output` - If `/output` is specified, the preset values will be written to the specified `<file>`. |
| `network get-process-network-emulation <process> <policy> [/output:<file>] [/target:<target>]` | Get one of the process specific policy table settings for the specified `<process>`. `<process>` may be either Process ID or Name.  `<policy>` - Sets the required policy table. The valid range is `0` to `15`.  `/output` - Sets the output `<file>` to which the emulation settings will be written. |
| `network ip-config [/interface:{loopback|eth0|dbg0|wlan0|wlan1|pppoe}] [/target:<target>]` | Displays information about available network interfaces or those specified by `/interface`, their current status and configuration. |
| `network set-devlan-settings [/address:<ip>] [/subnetMask:<subnet>] [/hostname:<name>] [/defaultGateway:<gateway>] [/ipMode:{AUTO|MANUAL}] [/arpInterval:<minutes>] [/target:<target>]` | Sets or changes individual DevLan settings of the default Target or specified `<target>`.  `/address` - Sets the IP address of the Target to `<ip>`.  `/subnetMask` - Sets the Subnet Mask of the Target to `<subnet>`.  `/hostname` - Sets the Host Name of the Target to `<name>`.  `/defaultGateway` - Sets the Debug Default Gateway for the Target to `<gateway>`.  If `/ipMode` is "AUTO", the Target will use DHCP.  If `/ipMode` is "MANUAL" the Target will use a fixed IP address specified by `/address`.  If `/arpInterval` is greater than 0, gratuitous ARP packets will be sent every `/arpInterval` minutes. If `/arpInterval` is set to zero, gratuitous ARP is disabled.  Note: When "IP Address Settings(DEV)" is "Manual" or `/ipMode:MANUAL` is specified, at least one of `/address`, `/subnetMask`, `/hostname`, or `/defaultGateway` is required. |
| `network set-hostname <name> [/target:<target>]` | Switches how Target Manager Server refers to the default Target or specified `<target>`.  `<name>` can be either the Target's hostname or the Target's IP address. |
| `network set-network-emulation {<option>|<file>} [/target:<target>]` | Sets all policy table entries for the default Target or specified `<target>`.   * `<file>` - Identifies a file   containing the policy table entries. * `<option>` - Specifies the preset   values. The valid range is `0` to   `3`. |
| `network set-packet-capture {on|off} [/type:{LAN|LAN+DEVLAN}] [/target:<target>]` | Turns network packet capture on/off for the default Target or specified `<target>`. The network interfaces to be captured are defined by `/type`. Note: Capture Type cannot be altered while capture is enabled. |
| `network set-process-network-emulation <process> <policy> {<option>|<file>} [/target:<target>]` | Sets the `<policy>` table entry for the specified `<process>`. `<process>` may be either Process ID or Name.   * `<policy>` - The policy to be   applied to the selected process. The valid range for   `<policy>` is   `0` to `15`.  * `<option>` - Applies a set of preset   values specified by the `<option>`   number. The valid range for `option` is   `1` to `3`. * `<file>` - Applies a set of values   contained in the `<file>`. |
| `network status [/target:<target>]` | Displays information about the network library status, including DNS resolution and memory usage. |

# List of prospero-ctrl package Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `package entitlement-delete <contentId> [/target:<target> ...]` | Deletes the entitlement with the specified `<contentId>` from the default Target or specified `<target>`(s). |
| `package entitlement-details [/target:<target> ...]` | Displays information about all available entitlements for the default Target or specified `<target>`(s). |
| `package entitlement-disable <contentId> [/target:<target> ...]` | Disables the entitlement with the specified `<contentId>` from the default Target or specified `<target>`(s). |
| `package entitlement-enable <contentId> [/target:<target> ...]` | Enables the entitlement with the specified `<contentId>` from the default Target or specified `<target>`(s). |
| `package entitlement-list [/titleId:<titleId>] [/target:<target> ...]` | Displays installed entitlements for one or all specified packages for the default Target or specified `<target>`(s).  `/titleId` - Sets a specific package to display the entitlements for. If `<titleId>` is omitted, all installed entitlements are listed. |
| `package install <path> [/slotId:<slot>] [/target:<target> ...]` | Installs the package located at `<path>` to the default Target or specified `<target>`(s).  `/slotId` specifies which package slot the package should be installed into. If the specified slot is not the current slot, the current slot used by the system software will automatically be set to `<slot>`.  `<slot>` must be a value in the range 0-15. |
| `package link <contentId> <srcSlotId> <dstSlotId> [/target:<target>]` | Link slots for an application identified by `<contentId>` for the default Target or specified `<target>`.  `<srcSlotId>` must be a slot where a reference package is installed. `<dstSlotId>` may reference any slot, but if it is already in use the existing package will be uninstalled by the system before making the link.  `<srcSlotId>` and `<dstSlotId>` must be values in the range 0-15.  Note: This command cannot be used to make a link to an update package. If the specified `<srcSlotId>` consists of a reference package and a patch, only the reference package will be linked. |
| `package list [/target:<target>]` | Lists all installed packages on the default Target or specified `<target>`. |
| `package list-content-config <contentId> [/target:<target>]` | Lists the content config labels available for the specified `<contentId>` on the default Target or specified `<target>`. |
| `package move <titleId> {INTERNAL|EXTERNAL|M2} [/target:<target> ...]` | Moves a package with `<titleId>` to either the Target's `INTERNAL` console storage, `EXTERNAL` USB extended storage, or M.2 SSD storage.  If the specified `<titleId>` has an associated patch or additional content, these will also be moved to the destination storage. |
| `package rebase <contentId> [/slotId:<slot>] [/target:<target> ...]` | Rebases all application or additional content packages for the specified `<contentId>` into a single remastered package.  `/slotId` will rebase the application packages in the specified `<slot>`.  If the specified `<slot>` is a link slot, the original package will be uninstalled from the source slot along with any other linked slots, and `<slot>` will contain the rebased package.  If the specified `<slot>` is not the current slot, the current slot used by the system software will automatically be set to `<slot>`.  `<slot>` must be a value in the range 0-15. |
| `package set-current-slot <contentId> <slotId> [/target:<target>]` | Sets an application identified by `<contentId>` to use `<slotId>` as its current slot. If the application is running, it will automatically be terminated by the system software.  `<slotId>` must be a value in the range 0-15. |
| `package slot-info <contentId> [/target:<target>]` | Retrieve all slot information for the specified `<contentId>` for the default Target or specified `<target>`. |
| `package switch-content-config <contentId> <label> [/target:<target>]` | Switches the content identified by `<contentId>` to use the content configuration specified by the configuration `<label>` for the default Target or specified `<target>`. |
| `package uninstall <titleId> [/type:{AC|AC_PATCH|ALL|PATCH}] [/contentId:<contentId>] [/slotId:<slot>] [/target:<target> ...]` | Uninstalls the package with `<titleId>` from the default Target or specified `<target>`(s).  `/type` - Specifies the package type to be uninstalled:   * `AC` - Specifies that only additional content type   packages are to be uninstalled. * `AC_PATCH` - Specifies that only additional content patch   type packages are to be uninstalled. * `ALL` - Specifies that all package types are to be   uninstalled. * `PATCH` - Specifies that only patch packages are uninstalled.   `/contentId` - Specifies additional content to uninstall. If `<contentId>` is not specified all additional content for the `<titleId>` will be removed.  If `/type` is not specified, all package types for the given `<titleId>` are to be uninstalled.  If `/type` is `AC` or `AC_PATCH`, `/contentId` may be specified to indicate specific additional content to uninstall. If `<contentId>` is not specified then all additional content for the given `<titleId>` is removed.  If `/type` is `PATCH` then only the update package for the given `<titleId>` is uninstalled.  `/slotId` specifies the slot from which the package should be uninstalled. If `<slot>` is the current slot, the current slot will be automatically updated by the system software when the slot becomes empty.  `<slot>` must be a value in the range 0-15. |

# List of prospero-ctrl playgo Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `playgo get-status [/titleId:<titleId>] [/target:<target>]` | Gets the current PlayGo status for the specified `<titleId>`.  The PlayGo status includes: the speed restriction, chunk status and transfer status of the currently active PlayGo transfer.  If /`titleId` is not specified, returns PlayGo status for the currently running application. |
| `playgo initiate-download [/install:INITIAL|TRIGGER|ALL] [/url:<package_URL>] [/contentId:<contentId>] [/scenarioId:<scenarioId>] [/target:<target>]` | Initiates a PlayGo download.  `/install` - Controls the PlayGo download behavior.  If `/install` is set to `INITIAL`, this command will wait for the initial payload to be installed. After the initial payload is installed, the remaining PlayGo chunks will continue to be installed, but will not block this command.  If `/install` is set to `ALL`, this command will block until all chunks for the current content configuration are installed.  Otherwise, if `/install` is set to `TRIGGER` or not specified, this command will initiate the PlayGo download and return immediately.  `/url` - Sets the `<package_URL>` for the PlayGo download.  `/contentId` - Sets the `<contentId>` for the package to be downloaded.  `/scenarioId` - Sets the `<scenarioId>` for the PlayGo download.  Note: If `<package_URL>`, `<contentId>` or `<scenarioID>` are not specified, the corresponding values from the system software settings will be used. |
| `playgo load-snapshot <file> <titleId> [/target:<target>]` | Loads a saved PlayGo chunk status snapshot `<file>` for the specified `<titleId>` on the specified `<target>`.  Snapshot files can be created by using the `playgo save-snapshot` command. Snapshot files are named `playgo-status.xml` by default.  If `<titleId>` is not specified, the PlayGo snapshot will be loaded for the currently running application. |
| `playgo next-chunk <count> [/titleId:<titleId>] [/target:<target>]` | Completes the install of the specified number of chunks from the top of the **PlayGo to-do list** for the specified `<titleID>`.  `<count>` - Details how many chunks should be installed. Fewer chunks than the requested `<count>` may be installed if all chunks have been installed, or the PlayGo transfer is running in 'MANUAL' mode (Refer to [playgo start-transfer](list-of-prospero-ctrl-playgo-commands.html#target-manager-cli-users-guide_1_2_10__0playgo_start_transfer)).  If `/titleId` is not specified, the PlayGo snapshot will be loaded for the currently running application. |
| `playgo save-snapshot <directory> [/target:<target>]` | Writes the current chunk status to a file (`playgo-status.xml`) in the specified `<directory>`.  If this file is placed next to `playgo-chunks.xml` in the working directory when launching an ELF, the PlayGo status represented by the core dump file will automatically be applied to the ELF the next time it is run. |
| `playgo set-chunk-status <titleId> {INITIAL|COMPLETED} [/scenarioId:<scenario_ID>] [/language:<language_mask>|<language_codes>] [/target:<target>]` | Sets the status of a PlayGo chunk for the specified `<titleId>`.   * `INITIAL` - Sets the chunk to only install the initial payload of the `<titleId>` for the requested scenario and language. * `COMPLETED` - Sets the chunk to install the entire payload of the `<titleId>` for the requested scenario and language.   `/scenarioId` - Sets the `<scenario_ID>` for the PlayGo download.  `/language` - Specifies a language to be downloaded. This can either be a `<langauge_mask>` or a comma-seperated list of language codes. For a list of the available language codes, refer to [PlayGo Library Overview - Appendix A: PlayGo Chunk Definition File Specifications - Numbers and Language Codes for Languages Usable in the Language Setting Attributes](../PlayGo-Overview/numbers-and-language-codes-for-languages-usable-in-the-langu.html).  `<language_mask>` sets the language. `<language_mask>` is defined by `scePlayGoLanguageMask`.  The chunks for the specified language(s) are installed, otherwise chunks for the current system language are installed.  Note: For more information on `<scenario_mask>` and `<language_mask>`, refer to [PlayGo Library Overview](../PlayGo-Overview/__document_toc.html) and [PlayGo Library Reference](../PlayGo-Reference/__document_toc.html).  Note: If the package data for the specified `<titleId>` is only partially downloaded, this command will wait for the remaining data to be downloaded. |
| `playgo start-transfer [/titleId:<titleId>] [/mode:{HIGH|MEDIUM|LOW|CUSTOM|MANUAL}] [/speed:<KiBs>] [/target:<target>]` | Starts a PlayGo transfer for the specified `<titleId>` from the current chunk status.  `/titleId` - Sets the application for the PlayGo transfer.  If `/titleId` is not specified, a PlayGo transfer will be started for the currently running application.  `/mode` - Sets the transfer mode.   * `HIGH` - Up to   300Mbps. * `MEDIUM` - Up to   70Mbps. * `LOW` - Up to   10Mbps. * `CUSTOM` - Sets a custom transfer speed. Requires the   `/speed` argument to be set. * `MANUAL` - Pauses PlayGo installation before downloading   each chunk until it is explicitly requested (for example, using a [playgo next-chunk](list-of-prospero-ctrl-playgo-commands.html#target-manager-cli-users-guide_1_2_10__0playgo_next_chunk) command).   If /`mode` is not specified, the default PlayGo transfer speed setting from the system software settings is used.  If `/mode` is used with the `CUSTOM` option, the `/speed` argument is required. If `/speed` is not set, the default PlayGo transfer speed setting from the system software settings is used.  Note: `High`, `Medium` and `Low` transfer mode values can vary depending on the PlayGo specification. |
| `playgo stop-transfer [/titleId:<titleId>] [/target:<target>]` | Stop a PlayGo transfer for the specified `<titleId>`.  If `/titleId` is not specified any PlayGo transfers for the currently running application will be stopped. |

# List of prospero-ctrl power Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `power off [/force] [/target:<target> ...]` | Powers off the default Target or specified `<target>`(s).  Use `'off /target:*'` to power off all available Targets.  `/force` - Forcibly powers off the default Target or specified Targets. |
| `power on [/target:<target> ...]` | Powers on the default Target or specified `<target>`(s).  Use `'on /target:*'` to power on all available Targets. |
| `power reboot [/target:<target> ...]` | Reboots the default Target or specified `<target>`(s).  Use `'reboot /target:*'` to reboot all available Targets. |
| `power rest-mode[/target:<target> ...]` | Puts the default Target or specified `<target>`(s) into rest mode.  Use `'rest-mode /target:*'` to put all available Targets into rest mode. |
| `power safe-mode {MENU|INITIALIZE|REINSTALL} [/pup:<file>] [/target:<target>]` | Boot the default Target or specified `<target>` into safe mode, and run the corresponding safe mode option, without requiring confirmation with the controller.  Note: If the Target is not powered off, it will be put into the 'off' state before attempting this operation.   * `MENU` - Reboots the Target into Safe Mode and displays the CLI Safe Mode menu. * `INITIALIZE` - Reboots the Target into Safe Mode and returns the system to the initial state. This is equivalent to **Option 7. Reset PS5** on the Target's Safe Mode Menu. * `REINSTALL` - Reboots the   Target   into Safe Mode and initializes the system to the factory default   settings, then performs a system software setup. This is   equivalent to   **Option   8.   Reset PS5 (Reinstall System   Software)**   on the   Target's   Safe Mode Menu.   If `MENU` is specified, this command enables control of the Safe Mode menu remotely by typing on the command line. Menu control is aborted when CTRL+C is pressed.  If `REINSTALL` is specified, a PUP `<file>` on the Host PC may be supplied using the '`/pup`' argument, otherwise Safe Mode will attempt to use the PUP file located under '`/PS5/UPDATE/PS5UPDATE.PUP`' on a USB drive attached to the Target.  For more information on the `MENU` option, refer to [Controlling Safe Mode through prospero-ctrl](controlling-safe-mode-through-prospero-ctrl.html). |

# List of prospero-ctrl process Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `process command-buffers {AMM|APR} [/process:<process>] [/id:<id> ...] [/target:<target>]` | Displays information about AMM or APR command buffers in the specified process for the default Target or specified `<target>`.   * `AMM` - Displays AMM command buffer   information. * `APR` - Displays APR command buffer   information.   `/process` - Display command buffer information for a selected `<process>`.  `/id` - Specifies which command buffer(s) should be displayed. `/id` is only valid when querying APR command buffer information.   * `<id>` - Identifies which command   buffers should be displayed.   `/id` can be specified multiple times to display multiple buffers.  Note: If `/process` isn't specified and only one process is running, the information for that process will be displayed. If `/process` is not specified and more than one process is running, an error is returned. |
| `process console <process> [/history] [/target:<target>]` | Displays the console output of the specified process for the default Target or specified `<target>`.  `/history` - Displays historical console output before continuing with live output.  Keyboard input or `stdin` will also be sent to `stdin` of the process. |
| `process info [/show:{All|Basic|Modules|Threads|Files|VirtualMemory} ...] [/process:<process>] [/target:<target>]` | Displays information about the state, modules and virtual memory regions of the specified process running on the default Target or specified `<target>`.  `/process` - Displays process information for a selected `<process>`.  To only include certain objects in the output, use `/show`, which can be used multiple times.  By default, all objects are included in the output.  For example to only include threads and files, use `/show:Threads /show:Files`.  Note: If `/process` is omitted and only one process is running on the Target, the command displays info on that process. |
| `process kill [/process:<process>] [/target:<target>]` | Kills the specified `<process>` running on the default Target or specified `<target>`.  Note: If `/process` is omitted and only one process is running on the Target, the command kills that process. |
| `process list [/target:<target>]` | Lists processes running on the default Target or specified `<target>`. |
| `process objects <process> {all|sync|ult-runtimes|fiber|jobmanager|files} [/justmyobjects] [/target:<target>]` | Dumps the kernel objects owned by the `<process>` running on the default Target or specified `<target>`.   * `all` - Dumps all objects associated with the process. * `sync` - Dumps only kernel synchronization   objects associated with the process. * `ult-runtimes` - Dumps only ULT-runtimes   associated with the process.   Refer   to the [Ult Library Overview](../Ult-Overview/__document_toc.html) for more   information. * `fiber` - Dumps only fibers associated with the   process. * `jobmanager` - Dumps only job manager objects   associated with the process.   Refer   to the [Job Library Overview - Original Job   Manager Development](../Job-Overview/original-job-manager-development.html) for more information. * `files` - Dumps only files associated with the process.   `/justmyobjects` restricts the output to ignore non-user code, such as external libraries. This mimics the Just My Code support from the Debugger. Refer to [Debugger User's Guide - Customizing the Debugger - Debugger Support for Just My Code](../Debugger-Users_Guide/debugger-support-for-just-my-code-support.html) for more information. |
| `process sockets [/process:<process>] [/target:<target>]` | Displays socket information for the specified `<process>`.  Note: If no arguments are provided and only one process is running on the Target, the command displays info on that process. |
| `process spawn <file> [/workspace:<workspace>] [/storage:{INTERNAL|M2}] [/elfPathFormat:{LOCAL|WORKSPACE}] [/gp5File: <GP5_File>]`  `[/contentConfig:<label>] [/saveDataRootDirectory:<path>] [/workingDirectory:<path>] [/systemLibraryVerification:{WARN|ABORT}] [/flexibleMemory:<size>] [/extendedDirectMemory:<size>] [/nodebug] [/mirrorMode:{WHOLE-FILE|ON-DEMAND}] [/target:<target>] [/args <arg> ...]` | Spawns a process from the specified `<file>` on the default Target or specified `<target>` with the arguments given by `/args`.  `<file>` must be either a `.elf` or `.ps5launch` file.  Note: If `<file>` is a `.ps5launch` file, selecting any options other than `/target` will cause the command to fail.   * `/workspace` - Selects a standalone Workspace for   the lifetime of this process. * `/storage` - If `/workspace` is specified, `/storage` will be selected automatically unless a standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified. * `/elfPathFormat` - Indicates whether the path to the ELF is a local Windows path (default) or a workspace path specified by `/workspace`. * `/gp5File` - Specifies the local Windows path to a GP5 File to define the layout of the working directory. Note: This argument cannot be specified if `/workingDirectory` is specified. * `/contentConfig` - Specifies which content config   `<label>` to use in the GP5   File. * `/saveDataRootDirectory` - Specifies a   `<path>` to use as an   override for the save data root. * `/workingDirectory` - Sets the working   directory of the executable to   `<path>`.    + If this is an empty string or not specified, the ELF     load directory will be used.   + Otherwise, this must be a local Windows path. Note: The specified path must be absolute, not     relative. * `/systemLibraryVerification` - Enables System   Library Verification.    + If `WARN` is specified, SLV will generate     TTY messages.   + If `ABORT` is specified, SLV will     generate an exception. * `/flexibleMemory` - Overrides the size of the flexible memory available to the application. `<size>` must be supplied in MiB. * `/extendedDirectMemory` - Overrides the size of the extended direct memory available to the application. `<size>` must be supplied in MiB. * `/nodebug` - Identifies the process to be spawned   is not debuggable. * `/mirrorMode` - Sets the mirroring mode of the System Managed Host Mirror.    + Use `WHOLE-FILE` (default) to have APR     resolve or [sceKernelOpen()](../Kernel-Reference/sce-kernel-open.html) block until the whole file is     transferred.   + Use `ON-DEMAND` to allow APR resolve or     [sceKernelOpen()](../Kernel-Reference/sce-kernel-open.html)     to unblock immediately and transfer data as required by     the game.   Note: `/args` must be the final argument, and all values passed to `/args` will be treated as arguments for the launched process. |

# List of prospero-ctrl process-dump Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `process-dump console <dumpfile> [/timestamp]` | Displays the console output from the specified `<dumpfile>`.  `/timestamp` - Includes the timestamps in the output. |
| `process-dump extract-controller-data <dumpfile> <outfile> [/deadzone:<width>] [/overwrite]` | Extracts controller data from the specified `<dumpfile>` and stores it in `<outfile>`.  `/deadzone` filters unwanted data for the controller analog sticks and may be any value between 0 and 127. Default value is 13.  Overwrites existing files by specifying `/overwrite`. |
| `process-dump extract-structured-userdata <dumpfile> [/output:<jsonfile>]` | Extracts structured user data from the specified `<dumpfile>`, converts it to JSON and writes it to `<jsonfile>`.  Note: If no `<jsonfile>` is specified, the output is directed to the console. |
| `process-dump extract-userdata <dumpfile> <file>` | Extracts user data from the specified `<dumpfile>` and writes it to `<file>`. |
| `process-dump extract-userfile <dumpfile> <userfile> <output>` | Extracts a single `<userfile>` from the specified `<dumpfile>` and writes it to the specified `<output>` path. |
| `process-dump extract-userfiles <dumpfile> <path>` | Extracts all the user files from the specified `<dumpfile>` and writes them to `<path>`. |
| `process-dump list-userfile <dumpfile>` | Extracts a list of user files from the specified `<dumpfile>`. |
| `process-dump trigger <process> <directory> {mini|full} [/basename:<basename>] [/target:<target>]` | Generates a `full` or `mini` core dump file of the specified `<process>` running on the default Target or specified `<target>` and saves the core dump file to the specified `<directory>`.   * `mini` - Sets the core dump to mini dump. * `full` - Sets the core dump to full dump.   `/basename` enables you to specify the prefix for the generated file names.  Note: If you experience problems with core dumps, try saving them to a directory on the Host PC that contains fewer files. |
| `process-dump view <dumpfile> [/show:{ALL|BASIC|MODULES|THREADS|OBJECTS|VIRTUALMEMORY|CONSOLE|SYSTEM|VIDEO||AMPR} ...] [/justmyobjects]` | Views detailed information from the specified `<dumpfile>`.  Available information includes console output, missing memory dumps, system, application, virtual memory, and process information.  `/show` filters the output to the information type selected.  This option can be added multiple times.  E.g. `/show:CONSOLE /show:SYSTEM`  By default, all information will be displayed.  `/justmyobjects` restricts the information output to ignore non-user code, such as external libraries. This mimics the Just My Code support from the Debugger. Refer to [Debugger User's Guide - Customizing the Debugger - Debugger Support for Just My Code](../Debugger-Users_Guide/debugger-support-for-just-my-code-support.html) for more information. |

# List of prospero-ctrl psn Commands

All commands are case insensitive.

Note: In these commands, `<psnSignInID>` refers to the email address or ID used to sign in to the account on PlayStation™Network for the user. See the [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html) for more information.

| **Command** | **Description** |
| --- | --- |
| `psn add-blocked-user <psnSignInID> <password> <userPsnOnlineID> [/target:<target>]` | Add the specified `userPsnOnlineID` as a blocked user.  Note: A user account on the Target is not required for this operation. |
| `psn add-friend <psnSignInID> <password> <friendPsnSignInID> <friendPassword> [/relationship:{FRIEND|CLOSE-FRIEND}] [/target:<target>]` | Create a friendship between two accounts for PlayStation™Network.  Note: The relationship will default to `FRIEND`. A `CLOSE-FRIEND` relationship cannot be downgraded to `FRIEND`.  Note: A user account on the Target is not required for this operation. |
| `psn delete-blocked-user <psnSignInID> <password> <userPsnOnlineID> [/target:<target>]` | Unblock the specified `userPsnOnlineID`.  Note: A user account on the Target is not required for this operation. |
| `psn delete-friend <psnSignInID> <password> <friendPsnOnlineID> [/target:<target>]` | End a friendship between two accounts for PlayStation™Network.  Note: A user account on the Target is not required for this operation. |
| `psn list-blocked-users <psnSignInID> <password> [/target:<target>]` | List the accounts for PlayStation™Network blocked by the specified account for PlayStation™Network.  Note: A user account on the Target is not required for this operation. |
| `psn list-friends <psnSignInID> <password> [/target:<target>]` | Get a list of all the PlayStation™Network friends for the specified account for PlayStation™Network.  Note: A user account on the Target is not required for this operation. |

# List of prospero-ctrl savedata Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `savedata delete <titleId> [/directory:<path> ...] [/target:<target>]` | Deletes save data directories for the user that is currently logged in for the specified `<titleID>`.   * `/directory` - Specifies a save data directory `<path>` to delete.   `/directory` can be specified multiple times to delete multiple save data directories from the Target.  Note: If `/directory` is not specified, all save data directories for the given `<titleID>` will be deleted. If any `<path>`s are specified using the `/directory` option, only those specified save data directories will be deleted. |
| `savedata export <titleId> <path> [/directory:<path> ...] [/target:<target>]` | Exports save data directories for the user that is currently logged in for the specified `<titleID>` to the specified Host PC `<path>`.   * `/directory` - Specifies a save data directory   `<path>` to export.   `/directory` can be specified multiple times to export multiple save data directories from the Target.  Note: If `/directory` is not specified, all save data directories for the given `<titleID>` will be exported. If any `<path>`s are specified using the `/directory` option, only those specified save data directories will be exported. |
| `savedata export-raw <titleId> <path> [/keystone:<path>] [/fingerprint:<fingerprint>] [/directory:<directory> ...] [/target:<target>]` | Exports unencrypted save data for the specified `<titleId>` to the save data directory `<path>` on the Host PC. If the application is currently installed, you can specify the title ID of the installed application with `<titleId>`, and the exported save data will use the title ID specified by the '`titleIdForSharing`' variable in the application's `param.json`.  `/keystone` specifies the path to a keystone file on the Host PC (which may be generated using the"ks\_create" command in the Publishing Tools).  `/fingerprint` specifies a passcode fingerprint (which may be obtained using the "pc\_fingerprint" command in the Publishing Tools).  If neither `/keystone` nor a passcode `/fingerprint` are supplied, exporting save data is only possible if it was created by an application without a keystone file.  `/directory`may be specified zero or more times. If no directories are provided, all save data directories for the given title ID will be exported, otherwise only the specified directories will be exported. |
| `savedata import <path> [/directory:<path> ...] [/target:<target>]` | Imports save data for the user that is currently logged in from the specified Host PC `<path>`.   * `/directory` - Specifies a save data directory   `<path>` to import.   `/directory` can be specified multiple times to import multiple save data directories from the Target.  Note: If `/directory` is not specified, all save data directories for the given `<titleID>` will be imported. If any `<path>`s are specified using the `/directory` option, only those specified save data directories will be imported. |
| `savedata import-raw <titleId> <path> [/keystone:<path>] [/fingerprint:<fingerprint>] [/directory:<directory> ...] [/target:<target>]` | Imports unencrypted save data for the specified `<titleId>` and save data directory `<path>` on the Host PC. If the application is currently installed, you can specify the title ID of the installed application with `<titleId>`, and the imported save data will use the title ID specified by the '`titleIdForSharing`' variable in the application's `param.json`.  `/keystone` specifies the path to a keystone file on the Host PC (which may be generated using the "ks\_create" command in the Publishing Tools).  `/fingerprint` specifies a passcode fingerprint (which may be obtained using the "pc\_fingerprint" command in the Publishing Tools).  If neither `/keystone` nor a passcode `/fingerprint` are supplied, importing save data is only possible if it was created by an application without a keystone file.  Note: If the specified `<titleId>` does not refer to a currently-installed application, `/keystone` must be used.  The save data directories given by `/directory` are relative to `<path>`, and may be specified zero or more times. If no directories are provided, all save data directories will be imported, otherwise only the specified directories will be imported. |
| `savedata list [/validate] [/target:<target>]` | List all the save data directories for the user that is currently logged in for all titles on the default Target or specified `<target>`.  Use `/validate` to check if the save data is corrupted. Using `/validate` may cause the command to take significantly longer to run. |

# List of prospero-ctrl settings Commands

All commands are case insensitive.

Note: Target settings can be changed using these commands or from the system software **Settings** feature. If both methods are used at the same time, system operation can become damaged and require settings to be restored from safe mode. Refer to [System Software User's Guide (Settings) - Features of the Settings Menu](../System_Software-Users_Guide_for_Settings/features-of-the-settings-menu.html) for more details.

| **Command** | **Description** |
| --- | --- |
| `settings boot-parameters [/target:<target>]` | Displays the current boot parameters for the default Target or specified `<target>`. If the current boot parameters differ from the defaults, the default value will also be displayed. |
| `settings export <file> [/target:<target>]` | Exports the settings of the default Target or specified `<target>` to an XML `<file>`. |
| `settings get-hostexec` | Displays whether support for launching a process on this Host PC from a process running on a Target is `enabled` or `disabled`.  Refer to [settings set-hostexec](list-of-prospero-ctrl-settings-commands.html#target-manager-cli-users-guide_1_2_16__0set_hostexec). |
| `settings get-mirroring-progress` | Displays whether support for displaying host mirroring progress in the Windows Action Center is enabled or disabled. |
| `settings import <file> [/reboot] [/target:<target>]` | Imports the settings `<file>` to the default Target or specified `<target>`.   * `/reboot` - Permits the Target to reboot if necessary. |
| `settings set-hostexec {enable|disable}` | Enables/Disables support for launching a process on this Host PC from a process running on a Target. Refer to the [Deci5 Library Overview](../Deci5-Overview/__document_toc.html) for more information.   * `enable` - Enables `hostexec` on   this Host PC. * `disable` - Disables `hostexec` on   this Host PC. |
| `settings set-mirroring-progress {enable|disable}` | Enables/Disables support for displaying host mirroring progress in the Windows Action Center. |
| `settings set-release-check-mode {release|assist|development} [/target:<target>]` | Sets the Release Check mode of the default Target or specified `<target>`.   * `release` - Sets Target into Release mode. * `assist` -Sets Target into Assist mode. * `development` - Sets Target into Development mode. |

# List of prospero-ctrl target Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `target activate-now [/target:<target>]` | Update the activation expiration date of the default Target or specified `<target>` from the network.  This is equivalent to selecting "\*Debug Settings - Activation - Activate Using Internet - Activate Immediately" from the system software. |
| `target add [/key:<key>] [/clientCertificatePath:<clientCertificatePath>] [/clientKeyPath:<clientKeyPath>] [/rootCertificatePath:<rootCertificatePath>] <target> [<target> ...]` | Adds the specified `<target>`(s), identified by IP address or hostname, to the Target list.  This is necessary for all subsequent operations which accept a `/target` argument.  The specified Target(s) will be validated against existing entries in Target Manager's list of Targets. If any existing entries are inaccessible this can cause adding Targets to take a long time. If an entry exists that has the same MAC address as the Target being added then the existing entry will have its stored hostname/IP updated if either:  * The new hostname/IP resolves to the same address as the existing hostname/IP. * No open connections exist.  `/key` sets the authentication `<key>` which will be used when connecting to a Target in Private Mode. `<key>` must be 32 characters long with each character in the set `[a-zA-Z0-9-_]`.  If you add multiple Targets in the same command, the same `<key>` will be used for all added Targets.  If the correct key is not supplied, a Private Mode Target will report "This Host PC is not authorized to use the target".  For more information on Private Mode, refer to the Private Mode for Targets section of [Target Manager GUI User's Guide - Using Target Manager to Manage Targets - Connecting to Targets Through Target Manager](../Target_Manager_GUI-Users_Guide/connecting-to-targets-through-target-manager.html).  `/clientCertificatePath`, `/clientKeyPath` and `/rootCertificatePath` respectively set the `<clientCertificatePath>`, `<clientKeyPath>` and `<rootCertificatePath>` properties used by [TLS Encryption](target-manager-cli-mutual-tls-encryption.html). This enables you to add Targets which have overridden encryption, as the [`target set-encryption-certificates`](list-of-prospero-ctrl-target-commands.html#target-manager-cli-users-guide_1_2_17__set-encryption-certificates) command only works if the Target is already in the Target list. |
| `target connect [/force] [/target:<target> ...]` | Connects to the default Target or specified `<target>`(s).   * `/force` - Forces the command to the default Target or specified `<target>`(s), disconnecting any connected users.   Note: Use `'connect /target:*'` to connect to all available Targets. |
| `target console [/timestamp] [/history] [/channel:{stdout|stderr|user[2-14]}] [/target:<target>]` | Displays the console output of default Target or specified `<target>`.   * `/timestamp` - Includes the timestamps in the output. * `/history` - Displays historical console output before continuing with live output. * `/channel` - Limits the output displayed to the specified console output channel. |
| `target delete [/target:<target> ...]` | Deletes the default Target or specified `<target>`(s) from the Target list.  Note: Use `delete /target:*` to delete all Targets.  Note: Using `delete` without specifying a `<target>` will delete the default Target and arbitrarily assign another available Target from the Target list to be the default. |
| `target disconnect [/target:<target> ...]` | Disconnects from the default Target or specified `<target>`(s).  Note: Use `'disconnect /target:*'` to disconnect from all Targets. |
| `target find [/start:<startIP> [/end:<endIP> /subnet:<subnetIP>]` | Discovers Targets available on the Host PC's subnet or optionally filtered by the specified IP address range or subnet.   * If no arguments are provided, this command finds Targets on the Host PC's subnet. * If `/start` and `/end` are provided, this command finds Targets with that address range. * If `/start` and `/subnet` are provided, this command will use a subnet broadcast address derived from both `<startIP>` and `<subnetIP>` to discover Targets.   Note: Using a subnet broadcast is quicker but may not function correctly in all network environments.  Note: The address specified for `<endIP>` should not be greater than `<startIP>`or `0.0.255.255`.  Refer to [Target Manager GUI User's Guide - Using Target Manager to Manage Targets - Connecting to Targets Through Target Manager](../Target_Manager_GUI-Users_Guide/connecting-to-targets-through-target-manager.html) for more information. |
| `target get-default` | Displays the hostname of the default Target. |
| `target info [/target:<target> ...]` | Displays detailed information for the default Target or specified `<target>`(s), includes the expiry time of the last activation.  Note: Use `'info /target:*'` to display information for all your discovered Targets. |
| `target list [/update]` | Lists all Targets added to the Target Manager Target list.   * `/update` - Updates the cached info for each Target. |
| `target locate [/mode:{AUDIO|VISUAL|BOTH}] [/delay:<seconds>] [/target:<target>]` | Places the Target into Locator mode until this command is cancelled, or the joystick button next to the front panel display is pressed.  The value of `/mode` determines which Locator functions are active:   * `AUDIO` - Causes the Target to beep. * `VISUAL` - Flash the backlight on the front panel display banner on and off. * By default, `BOTH` actions will be performed.   If `/delay` is specified, this command will wait for the specified number of `<seconds>` before starting Locator mode on the Target. Maximum delay allowed is 3600 seconds. |
| `target m2-format <encryptionKey> [/target:<target>]` | Requests the Target to format the M.2 SSD storage connected to the default Target or specified `<target>`, with the given encryption key. The Target will reboot to process this request. |
| `target m2-mount <encryptionKey> [/target:<target>]` | Requests the Target to mount the M.2 SSD storage connected to the default Target or specified `<target>`, with the given encryption key. The Target will reboot to process this request. |
| `target m2-status <encryptionKey> [/target:<target>]` | Retrieve status information for the M.2 SSD connected to the default Target or specified `<target>`. |
| `target name <name> [/target:<target>]` | Sets the System Name of the default Target or specified `<target>` to `<name>`.  **Warning**: When you change the System Name setting, the setting takes immediate effect, but only persists after a system reboot. |
| `target screenshot <filename> [/mode:{game|system|auto|main-only|tv-with-system|tv-without-system}] [/device:{TV|HMD}] [/target:<target>]` | Captures a screenshot from the default Target or specified `<target>`.   * `<filename>` - The name of the saved image.  * `/mode` - Sets the screenshot mode. Refer to [VideoOut Library Overview - Bus Overlay and Tap Point Branching](../VideoOut-Overview/bus-overlay-and-tap-point-branching.html) for more information:    + `game` - Takes a screenshot of the running game.   + `system` - Takes a screenshot of the System software, even if a game is being played.   + `auto` - Takes a screenshot of whatever is currently being displayed on the screen.   + `main-only` - Takes a screenshot of the contents of the main display bus.   + `tv-with-system` - Takes a screenshot of the main TV output including the system software.   + `tv-without-system` - Takes a screenshot of the main TV output excluding the system software.   Default is `auto`.   * `/device` - Sets which device to take the screenshot from:    + `HMD` - The screenshot will be taken in VR mode if available.   + `TV` - The screenshot will be the normal TV output. This is the default.   Note: `<filename>` requires the file extension to determine the image format. Supported extensions are:  `.jxr`, `.exr`, `.jpg`, `.jpeg`, `.bmp`, `.tga` and `.png`.  Refer to [Screen Capture User's Guide - Capturing Images Using Screen Capture - Specifying Screenshot Mode in Screen Capture](../Screen_Capture-Users_Guide/specifying-screenshot-mode-in-screen-capture.html) for more information. |
| `target set-authentication-key <key> [/force] [/target:<target>]` | Sets the authentication `<key>` to be used by the Host PC whenever connecting to a Target that requires one for connection.  `<key>` must be 32 characters long with each character in the set `[a-zA-Z0-9-_]`.  `/force` will overwrite an existing key for the Target if one already exists. |
| `target set-default <target>` | Sets `<target>` as the default. |
| `target set-encryption-certificates <clientCertificatePath> <clientKeyPath> <rootCertificatePath> [/global] [/target:<target>]` | Sets the TLS certificates for the specified or default `<target>`which will be used to secure the Target network communication as described in [Target Manager CLI Mutual TLS Encryption](target-manager-cli-mutual-tls-encryption.html).  Note: The Private Mode configuration tool is required to enable encrypted communication.  A root CA certificate which has signed both the client (Host PC) and server (Target) certificates must be supplied, as well as the client certificate and private key.  If `/global` is specified, the supplied certificates and keys are used for all encrypted Target communication.  If the private key is protected by a password, this must be supplied interactively.  Note: The supplied private key passwords will be accessible to the user account which is currently using `prospero-ctrl`. |
| `target set-fileserving-root <path> [/target:<target> ...]` | Sets the File-Serving Directory of default Target or specified `<target>`(s) to `<path>`.  This is the same as the instructions contained in the [Target Manager GUI User's Guide - Using Target Manager to Manage Files and Targets - Setting the File-Serving Directory](../Target_Manager_GUI-Users_Guide/004_setting-the-file-serving-directory.html) section. |
| `target unset-authentication-key [/target:<target>]` | Removes the authentication key for the default Target or specified `<target>`. |
| `target unset-encryption-certificates [/global] [/target:<target>]` | Disables custom certificate overrides for the default Target or the specified `<target>` and reverts to using the default certificates for all encrypted Target communication.  If `/global` is specified, the global certificate overrides are disabled, and `/target` is ignored. |
| `target update <file-or-http-url> [/target:<target> ...]` | Performs a system update on the default Target or specified `<target>`(s).  `<file-or-http-url>` - The file name and location of the update file (`.pup`) to apply. This can either be a file path on the Host PC or a HTTP URL.  Note: The default location for update files is `%SCE_ROOT_DIR%\PROSPERO\System Update Files`. |
| `target update-cp <file> [/target:<target> ...]` | Updates the Communication Processor (CP) firmware of the default Target or specified `<target>`(s) with the update `<file>` specified. |
| `target video <filename> [/bandwidth:<kilobits per second>] [/frame-rate:{60|30}] [/resolution:{360p|540p|720p|1080p|1440p|2160p}] [/limit-buffer:{5|10|15} [/length:<time>] [/force-net-test] [/no-connect] [/force-stop-stream] [/get-streaming-status] [/hdr] [/target:<target>]` | Captures video from the default Target or specified `<target>` to the `<file>`.  `/bandwidth:<kilobits per second>` - Specifies the maximum bandwidth to use. Default = 10000 kbps.  `/frame-rate:{60|30}` - Specifies the frame rate. Default = 60.  `/resolution:{360p|540p|720p|1080p|1440p|2160p}` - Specifies the capture resolution. Default = 1080p.  `/limit-buffer:{5|10|15}` - Specifies the time period in minutes to be used as a buffer for continuously recording footage.  `/length:<time>` - Specifies the duration of the capture. The default unit is seconds, but optional unit suffixes can be used for days(d), hours(h), minutes(m), seconds(s), for example: 1d2h32m16s. If this parameter is omitted, the capture continues until the user presses **Ctrl+C**.  `/force-net-test` - Forces network tests prior to starting the capture. The capture will not start if the network test fails. By default, the network test is not performed.  `/no-connect` - Specifies that the Host PC should not take ownership of the default Target or specified `<target>` while capturing video.  `/force-stop-stream` - Forcefully stops a remote host's streaming session. This has no effect on streaming sessions started by the current Host PC.  `/get-streaming-status` - Retrieves the streaming status of a remote session.  `/hdr` - Specifies the capture is HDR. Note: This option can only be used if the `/resolution` is set to 1440p or 2160p. |

# List of prospero-ctrl user Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `user create [/user:<name>] [/target:<target>]` | Creates a new local user account on the default Target or specified `<target>`. A username can be optionally supplied using `<name>`. |
| `user delete <user> [/target:<target>]` | Delete the local user account specified by `<user>` on the default Target or specified `<target>`.  `<user>` may be either a username or a user ID. |
| `user login <user> [/target:<target>]` | Logs in the user local account specified by `<user>`.  `<user>` may be either a username or a user ID that has been defined on the default Target or specified `<target>`.  Up to four users may be logged in at the same time. |
| `user logout <user> [/target:<target>]` | Logs out the user local account specified by `<user>`.  `<user>` may be either a username or a user ID that has been defined on the default Target or specified `<target>`. |
| `user list [/target:<target>]` | Lists details about all known user local accounts on the default Target or specified `<target>`. |
| `user psn-associate <user> <psnId> <password> [/target:<target>]` | Associates the local user account specified by `<user>` with the account for PlayStation™Network identified by the PlayStation™Network sign-in ID `<psnId>` and `<password>`.  `<user>` may be either a user name, or a user ID on the default Target or specified `<target>`. |
| `user psn-signup <user> <country> [/dateOfBirth:<dateOfBirth>] [/signin:<Id>] [/password:<password>] [/onlineid:<Id>] [/subaccount] [/target:<target>]` | Signs the local user account specified by `<user>` up to PlayStation™Network.  `<user>` may be either a user name, or a user ID on the default Target or specified `<target>`.  `<country>` must be a PlayStation™Network-supported ISO 3166-1 alpha-2 country code.  `/onlineid` may be specified to create an account with the specified online ID.  `/signin` may be specified to define the sign-in ID (email address) of the new PSN account, and `/password` may be used to create an account with the specified password. Note: If `/onlineid`, `/signin` or `/password` are omitted, the Target will generate them.  `/subaccount` may be specified to sign up for a sub account (a family-managed account will be created automatically).  `/dateOfBirth` is only valid if `/subaccount` is specified, and will set the default age-restriction settings for the age specified by `<dateOfBirth>`. `<dateOfBirth>` should be formatted in YYYY-MM-DD format. |
| `user psn-signin <user> [/password:<password>] [/target:<target>]` | Signs the specified user in to PlayStation™Network.  `<user>` may be either a username, or a user ID on the default Target or specified `<target>`.  `<password>` may be used to optionally specify a password if one is not saved on the Target. |
| `user psn-signout <user> [/target:<target>]` | Signs the specified user out from PlayStation™Network.  `<user>` may be either a username, or a user ID on the default Target or specified `<target>`. |

# List of prospero-ctrl video Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `video watermark-set <passphrase> <watermark-file> [/target:<target> ...]` | Applies text or graphical watermarks defined in a `<watermark-file>` to the video output of the default Target or specified `<target>`(s).  `<passphrase>` - Sets the authentication `<passphrase>` that is required to remove watermarks with the `video watermark-unset` command. `<passphrase>` must be 32 characters long with each character in the set `[a-zA-Z0-9-_]`.  If you add multiple Targets in the same command, the same `<passphrase>` will be used for all added Targets.  `<watermark-file>` - Path to a specified `.ps5rvwatermark` file containing the configuration for the watermarks to be applied. `.ps5rvwatermark` files are JSON files that specify graphics, text and animations for watermarking. Refer to [Remote Viewer User's Guide - Watermarking in Remote Viewer](../Remote_Viewer-Users_Guide/watermarking-in-remote-viewer.html) for more information. |
| `video watermark-unset<passphrase>[/target:<target> ...]` | Removes text or graphical watermarks from the video output of the default Target or specified `<target>`(s).  `<passphrase>` - The authentication `<passphrase>` defined when applying watermarks to the Target(s) with the `video watermark-set` command. |

# List of prospero-ctrl workspace Commands

All commands are case insensitive.

| **Command** | **Description** |
| --- | --- |
| `workspace create <workspace> [/storage:{INTERNAL|M2}] [/reservedSize: <MiB>] [/maxSize: <MiB>] [/fixed] [/force] [/target:<target> ...]` | Creates a Standalone workspace named `<workspace>` on the default Target or specified `<target>`(s).  By default, Standalone workspaces have no maximum size, and will grow as required to fill the space available on the Target storage.  `/storage` - Selects whether the Standalone workspace should be created on console storage, or the M.2 SSD storage. Console storage is used by default.  `/reservedSize` - Causes `<workspace>` to always occupy at least the defined `<MiB>` on the Target storage.  `/maxSize` - If `/maxSize` is specified, the Standalone workspace will grow on demand up to `/maxSize` in `<MiB>`. If `/maxSize` is omitted or set to `0` there is no limit to the amount of SSD space available to `<workspace>`.  `/fixed` - Causes the Standalone workspace to always occupy exactly the size you specify with `/reservedSize`. If you omit `/fixed`, you can optionally specify either `/reservedSize` or `/maxSize` to have the Standalone workspace grow from an initial starting point to a maximum size.  If `/force` is specified, then this operation will return a success, even if a Standalone workspace with the specified name already exists. In that case, the existing data within the Standalone workspace will be unchanged. |
| `workspace deploy <workspace> <GP5_File> [/launch:<path>] [/storage:{INTERNAL|M2}] [/diff:{accurate|quick}] [/contentConfig:<label>][/target:<target> ...]` | Populates the specified Standalone `<workspace>` on default Target or specified `<target>`(s) with files and directories defined by the given `<GP5_File>`.  Use `/launch` to specify the ELF directory. This is used to expand the `launch_path` attribute in the GP5 File.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  `/diff` - Selects how file differences should be calculated:   * `accurate` - Considers files to be the same if   their hash matches. * `quick` - Considers files to be the same if they   have the same size and their modification times are within 10µs   of each other.   Default is `quick`.  If `/contentConfig` is specified then only sce\_sys entries with a corresponding "`content_config_label`" in the GP5 File will be deployed. `/contentConfig` defaults to "`primary`". |
| `workspace destroy <workspace> [/storage:{INTERNAL|M2}] [/target:<target> ...]` | Deletes the Standalone workspace named `<workspace>` on the default Target or specified `<target>`(s).  `/storage` will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified. |
| `workspace diff <workspace> <source> [/storage:{INTERNAL|M2}] [/filter:<path>] [/diff:{accurate|quick}] [/target:<target>]` | Displays a list of files in `<source>` on the Host PC which are different in `<workspace>`.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  `/filter` - Limits diffing to specific subdirectories with `<path>`.  `/diff` - Selects how file differences should be calculated:   * `accurate` - Considers files to be the same if   their hash matches. * `quick` - Considers files to be the same if they   have the same size and their modification times are within 10µs   of each other.   Default is `quick`. |
| `workspace explore <workspace> <location> [/storage:{INTERNAL|M2}] [/target:<target>]` | Explores the directories in `<workspace>` on the default Target or specified `<target>` specified by `<location>`. To view the root directory, `<location>` must be '/'.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified. |
| `workspace files <workspace> [/storage:{INTERNAL|M2}] [/filter:<path>] [/full] [/target:<target>]` | Lists files in `<workspace>` on the default Target or specified `<target>`.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  `/filter` - Limits listing to specific subdirectories with `<path>`.  `/full` - displays detailed metadata for each file. |
| `workspace filesystem-check <workspace> [/storage:{INTERNAL|M2}] [/target:<target>]` | Triggers a filesystem check on the `<workspace>` on the default Target or specified `<target>`.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified. |
| `workspace hash <file>` | Obtains a hash of a `<file>` on the Host PC. The hash algorithm is the default one used by Target Manager Server when working with workspaces. |
| `workspace info <workspace> [/storage:{INTERNAL|M2}] [/target:<target>]` | Displays detailed status information for the specified `<workspace>` on the default Target or specified `<target>`.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified. |
| `workspace list [/full] [/target:<target>]` | Lists workspaces on the default Target or specified `<target>`.  `/full` - Displays the full workspace status information. |
| `workspace mirror-deploy <GP5_File> [/launch:<path>] [/contentConfig:<label>] [/target:<target>]` | Pre-populates files and directories defined by the given `<GP5_File>`.  `/launch` - Specifies the ELF `<path>`. This is used to expand the `launch_path` attribute in the `<GP5_File>`.  `/contentConfig` - Specifies the content config `<label>` to use when deploying the `<GP5 File>`. |
| `workspace mirror-filesystem-check [/target:<target>]` | Triggers a filesystem check on the current Host PC's System Managed Host Mirror workspace on the default Target or specified `<target>`. |
| `workspace mirror-guid` | Prints the host mirror GUID for the current Host PC. |
| `workspace mirror-info <guid> [/target:<target>]` | Displays detailed status information for the specified System Managed Host Mirror workspace (using `<guid>`) on the default Target or specified `<target>`. |
| `workspace mirror-purge [/guid:<guid>] [/target:<target>...]` | Deletes the current Host PC's System Managed Host Mirror workspace for the default Target or specified `<target>`(s), or the one specified by `<guid>`. |
| `workspace mirror-push <path> [/norecurse] [/target:<target>]` | Pre-populates files from `<path>` on the Host PC to the console storage on the default Target or specified `<target>`.  `/norecurse` - Copies `<path>` non-recursively. |
| `workspace mirror-validate <path> [/target:<target>]` | Performs a cache validation to ensure that the cache on the default Target or specified `<target>` is the same as `<path>` on the Host PC.  Note: This command is only valid if a process running on the default Target or specified `<target>` is using the specified `<path>` as its working directory (`/app0`). |
| `workspace pull <workspace> <source_path> <destination_path> [/storage:{INTERNAL|M2}] [/target:<target>]` | Copy files from the `<source_path>` within the `<workspace>` of the default Target or specified `<target>` to the `<destination_path>` on the Host PC.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  Note: The `<source_path>` is always relative to the root of `<workspace>`. |
| `workspace push <workspace> <source_path> <destination_path> [/storage:{INTERNAL|M2}] [/norecurse] [/compressionLevel:<level>] [/diff:{accurate|quick}] [/sync] [/target:<target> ...]` | Copies files from the `<source_path>` on the Host PC to `<destination_path>` within the `<workspace>` on the default Target or specified `<target>`(s).  Note: The `<destination_path>` is always relative to the root of `<workspace>`.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  `/compressionLevel` - Compresses the file(s) in `<source_path>` before transfer.  Acceptable values are in the range `-4` to `9`. Negative values favor compression speed.  Positive values favor compression ratio.  Default compression level is `0`, which is no compression.  `/norecurse` - Copies `<source_path>` non-recursively.  `/diff` - Defines how file differences should be calculated:   * `accurate` - Considers files to be the same if   their hash matches. * `quick` - Considers files to be the same if they   are the same size and their modification times are within 10µs   of each other.   Default is `quick`.  `/sync` - Deletes any files present on the `<destination_path>` which are not present in the `<source_path>` on the Host PC. |
| `workspace system-storage-status [/target:<target>]` | Gets information about the console storage and M.2 SSD storage on the default Target or specified `<target>`.  Information returned includes:   * `TotalCapacity` * `AllocatedSize` * `ReservedSize` * `GarbageSize` |
| `workspace unlink <workspace> <path> [/storage:{INTERNAL|M2}] [/target:<target>]` | Deletes files or directories recursively from `<path>` within `<workspace>`.  `/storage` - This will be selected automatically unless a Standalone workspace with the given name exists on both the console storage and the M.2 SSD storage, in which case `/storage` must be explicitly specified.  Note: `<path>` is always relative to the root of `<workspace>`. |