# Advanced Player Profile Editor User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Advanced_Player_Profile_Editor-Users_Guide/using-the-advanced-player-profile-editor.html

# Using the Advanced Player Profile Editor

Users can access the Advanced Player Profile tool through PlayStation®5 DevNet or by accessing the Development Accounts tool's editor menu.

# Adding and Selecting an Account

This topic provides information on how to select an account to view player profile
properties.

To view the player profile properties for a specific account you will need to select the account in the account selector. The online ID can be changed in the tool. Any account in your account library can be edited in the Advanced Player Profile Editor.

Any account you add to the account selector in Advanced Player Profile will automatically be added to the account library. If you already have an account on PlayStation™Network, you may add the account to the account selector in Advanced Player Profile. In order to make this process as easy as possible, authentication is not required to add the account, however authentication is required to access protected properties of the account.

Note: At this time, the Advanced Player Profile Editor does not require any additional authentication, however this may change in the future. For all other tasks in the Development Accounts, accounts cannot be edited until authenticated, as described in the [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html).

1. Click **Add Account**.
2. In the resulting dialog, select what method you want to use to add the account.
3. There are three methods you can use to add accounts:
   * Account ID

     You can add an account if you have the numeric Account ID. Account
     IDs are useful when working with certain APIs.
   * Online ID

     You can add an account if you have the Online ID as it would be
     displayed on the client.
   * Email (Sign-In ID)

     You can add an account if you have the email.

For more information on the Account Library, see [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html).

# Selecting an NP Communication ID

This topic provides information on selecting specific NP Communication IDs to use with
the Advanced Player Profile Editor.

Accessing the tool through DevNet will by default open the tool in the context of a
specific NP Communication ID. You can change the NP Communication ID by selecting it from
the NP Communication ID drop down in the tool

To Select an NP Communication ID:

1. Click the drop-down menu under **NPCommID**.
   Figure 1. Selecting an Online ID or NP Communication ID
2. Select the NP Communication ID from the list of NP Communication ID's you have access to.
3. Press **Enter**.