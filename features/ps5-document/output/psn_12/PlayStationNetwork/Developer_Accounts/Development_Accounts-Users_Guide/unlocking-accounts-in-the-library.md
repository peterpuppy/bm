# Development Accounts User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Development_Accounts-Users_Guide/unlocking-accounts-in-the-library.html

# Unlocking Accounts in the Library

This topic describes account unlocking in the Development Accounts Library.

Account unlocking is required to make changes to most account attributes (online ID, password, email address, physical address etc.). Unlocking is single factor in nature (email address and password are required) and Development Accounts does not support multi-factor authentication for the foreseeable future. PlayStation™Network developers can test with multiple test accounts.

Development Accounts allows you to add accounts without unlocking them. Unlocking is required for modifying some but not all account attributes. Accounts stay unlocked for up to 30 days from the day you first unlock. This allows you to modify attributes for the entire duration of the unlock window. At the end of the window you can unlock again which lasts for another 30 days.

Some attributes (such as Advanced Player Profile attributes) do not require unlocking to be modified.

To unlock any of the accounts in your library:

1. Modify an account attribute that requires unlocking (such as Communication Restriction).
2. A dialog box appears (see figure below) displaying the sign-in ID (email address).
3. Enter the sign-in ID for your account.
4. Enter the password for your account.
5. Click **Submit**.

Your selected account is now unlocked.

Note:

Accounts for PlayStation™Network with 2-step verification cannot be unlocked in the account library. Contact your developer support representative with any other account unlocking issues.

For more information on Advanced Player Profile refer to the [Advanced Player Profile Overview](../../../WebAPI/latest/Advanced_Player_Profile-Overview/__document_toc.html) and [Advanced
Player Profile Editor User's Guide](../Advanced_Player_Profile_Editor-Users_Guide/__document_toc.html). For more information for Communication Restriction refer to the [Communication Restriction Status
Web API Overview](../../../WebAPI/latest/Communication_Restriction_Status_WebAPI-Overview/__document_toc.html) or, alternatively, to TRC [R5061](../../../TRC/latest/TRC/R5061.html).

Unlock Account Dialog