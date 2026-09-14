# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/environment-variables-in-target-manager-cli.html

# Environment Variables in Target Manager CLI

The command line tools are built on Target Manager API, utilizing inter-process communication with `prospero-tm.exe`, which in turn communicates with the Target.

When launching a process or application, the process environment is cached so that environment variables are resolved using the same environment that `prospero-ctrl` or `prospero-run` were originally using, rather than the one from `prospero-tm.exe`.

The calling process environment is cached and used to resolve environment variables in the following circumstances:

* "`/host/`" file access from an Application or Process running on the Target.
* Launching a process on the Host PC using `sceDeci5CreateHostProcessAndWait()` or `sceDeci5CreateHostProcess()`.
* Environment variables in Host source paths when launching processes or deploying with GP5 files.

In previous versions of PlayStation®5 Target Manager Server, only global environment variables would be cached and used. From SDK 8.00 onwards, Target Manager Server will now also use any locally updated environment variables.

## Examples

If the global (User or System) environment variables are updated after environment variables are cached, `prospero-tm.exe` will update the cached environment using the updated environment variables when next called. For example, in the following case:

```
set MYVARIABLE=C:/initial.txt
prospero-ctrl process spawn game.elf
// game.elf <--- MYVARIABLE is C:/initial.txt
set MYVARIABLE=C:/new.txt
// game.elf <--- MYVARIABLE is C:/initial.txt
prospero-ctrl process spawn game.elf
// game.elf <--- MYVARIABLE is C:/new.txt
```

The environment from the current command prompt will be cached by `prospero-tm.exe`, so `/host/%MYVARIABLE%` will resolve to `/host/C:/initial.txt` for the first process spawn and `/host/C:/new.txt` for the second.

If the global environment is updated by setx:

```
set MYVARIABLE=C:/initial.txt
prospero-ctrl process spawn game.elf
// game.elf <--- MYVARIABLE is C:/initial.txt
setx MYVARIABLE=C:/new.txt
// game.elf <--- MYVARIABLE is C:/new.txt
prospero-ctrl process spawn game.elf
// game.elf <--- MYVARIABLE is C:/initial.txt (Note: setx does not affect the command prompt environment!)
```

Then `prospero-tm.exe` will update its cached environment to reflect the new global environment and `/host/%MYVARIABLE%` will subsequently resolve to `/host/C:/new.txt`.

Note:

The locally set environment variables in a command line environment will override the values set using `setx`.