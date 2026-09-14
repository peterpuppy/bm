# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/enabling-tab-completion-in-powershell-for-prospero-ctrl.html

# Enabling Tab Completion in Powershell for prospero-ctrl

Tab completion in Windows PowerShell for `prospero-ctrl` is supported and can be activated through the PowerShell user profile.

To activate the tab completion:

1. Open a PowerShell window.
2. Create the user profile file if it doesn't exist:

   ```
   if (!(Test-Path -Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
   ```
3. Open the Windows PowerShell user profile in a text editor:

   ```
   notepad $PROFILE
   ```
4. In the text editor, add the following to the file:

   ```
   $prosperoCtrlTabComplete = { 
       param($commandName, $wordToComplete, $cursorPosition);
       (prospero-ctrl complete $cursorPosition "$wordToComplete").split("_") | ForEach-Object {
           [System.Management.Automation.CompletionResult]::new($_, $_, 'ParameterValue', $_)
       }
   }
   Register-ArgumentCompleter -Native -CommandName prospero-ctrl.exe -ScriptBlock $prosperoCtrlTabComplete
   Register-ArgumentCompleter -Native -CommandName prospero-ctrl -ScriptBlock $prosperoCtrlTabComplete
   ```

Note:

To activate, you will need to have the execution of scripts policy enabled for PowerShell. Run a PowerShell window as Administrator and run:

```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```