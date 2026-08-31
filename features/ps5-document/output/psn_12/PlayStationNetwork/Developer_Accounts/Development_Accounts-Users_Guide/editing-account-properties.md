# Development Accounts User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Development_Accounts-Users_Guide/editing-account-properties.html

# Editing Account Properties

This section describes how to edit account properties in the Development Accounts Library.

After an account has been added to the library it can be modified with various editors and the Social Restriction toggle can be used. The editors can be accessed either from the **Editors** drop-down menu at the top of the page or the Options menu (⋮) in the library itself.

# Account Editor

This topic describes the Development Accounts Account Editor.

To access the Account Editor, click the **Editors** drop-down next to the **Account Library** button in the upper top left hand corner of the screen.

The Account Editor in Development Accounts (see this [Figure](online-id-history.html#development-accounts-users-guide_4_4__0_ref53756998)) offers you the ability to make the following account updates:

* Real Name
* Verified Account Status
* Online ID/ID History
* Set/Reset Password
* Close Accounts

The Account Editor also displays the following un-changeable account attributes:

* Sign-in ID
* Account ID
* Locale - Country/Region and Language
* Date of Birth

Note that changing the online ID of an account requires you to unlock the account again with the sign-in ID and password.

# Changing Password

This topic describes how to change the password for a Development Account.

Changing the password sets the password for the account.

To Edit the password:

1. Click the **Change Password** button.
2. Type in the new password in the dialog box that appears.
3. Click the **Save** button

# Changing Online ID

This topic describes how to change the Online ID for a Development Account.

It may be necessary to test the effect on entitlements that changing the online ID may or may not have on an account. This can be done in Development Accounts. Be aware that the new online ID must be unique. Note that changing the online ID is instant but may take time to replicate across servers in the development environment. The change may not be reflected instantly in some places but should not take longer than 10-15 minutes. It is recommended that in order to clear all caches that you restart the console after changing the online ID.

You can use Development Accounts to change the online ID of an account:

1. Type in the requested changes into the online ID text box.
2. Click the **Update** button.

# Online ID History

This topic describes how to view the online ID history for a Development Account.

Development Accounts supports viewing the history of online ID changes for an account. To view the online ID history:

1. Click the blue text labeled **Show Online ID History**.
2. View the history.

Previous online IDs associated with an account can be reclaimed and released using Development Accounts.

To reclaim or release an online ID:

1. Click the icon that resembles a clock to the left on the Online ID.
2. View the History
3. Click the **Reclaim** or **Release** buttons next to the online IDs you wish to reclaim or release.

Account Editor

# Verified Account Management

This topic describes how to manage the verified status for a Development Account.

Development Accounts allows users to manage verified status for accounts in the development environment.

To add verified status to an account:

1. Click the drop-down under the **Is this Account Verified** text next to verified role.
2. Select **Yes** or **No** from the drop-down menu.
3. Set the display name for the account.
4. Click **Save**.

To remove verified status from an account:

1. Click the drop-down menu next to verified role.
2. Click **No** and then **Save**.

# Commerce Editor

This topic describes the use of the Commerce Editor in Development Accounts.

The Commerce Editor allows you to manage entitlements on your account(s). To access the Commerce Editor, click the **Editors** drop-down next to the **Account Library** button in the upper top left hand corner of the feature.

The Commerce Editor can be accessed by either clicking the drop-down menu item from clicking the Options menu (⋮) in line with account on the library page or by clicking the **Editors** tab at the top and selecting the **Commerce Editor** option.

# Commerce/Account Editor Environment Switcher

This topic describes the use of the Commerce Editor Environment Switcher in Development Accounts.

You may have access to data in environments other than SP-INT. If your account has access to different environments, the Environment Switcher will appear in the upper left-hand corner of the Account Library, directly under the "Commerce/Account Editor" title. Click on the environment name and select the desired environment from the drop-down menu. The page will refresh and only data from your selected environment will appear on the Editor page.

# Clearing and Revoking Entitlements

This topic describes how to clear and revoke entitlements in Development Accounts.

In the NP commerce system, the product list displayed in a store and the category content data are updated according to whether or not a product has been purchased and the addition of new eligibility rules. Because of this, it is necessary to delete each account's entitlement information (whether or not a content or service entitlement has already been purchased and is owned) during development. Use the Commerce Editor to confirm or delete entitlements. The Commerce editor also allows for the revoking of single entitlements.

To clear entitlements for an account:

1. Click **Clear all Entitlements** (this deletes all entitlements).
2. Click **Yes** in the confirmation dialog.

To revoke a single entitlement for an account:

1. Click the ellipsis in the line of the single entitlement you wish to revoke. All entitlements are found in the entitlement table.
2. Once the drop down menu appears, click the selection for "Revoke Entitlement".
3. A confirmation dialog box will appear. Click Confirm to revoke the entitlement or Cancel to exit the dialog box.

# Aging an Account

This topic describes how to age an account for testing in Development Accounts.

When developing a subscription-type product, while it is necessary to test what happens when the validity period ends, it is not realistic to wait for the actual subscription period to pass.

Use the Commerce Editor to adjust (advance) the validity period of a purchased subscription.

By adjusting the validity period of a purchased subscription type product to the end of the subscription duration, you are able to test the behavior when the subscription ends.

To age an account:

1. Select the days, months, or years from the drop-down.
2. Type the quantity of selected days, months, or years you would like to age the account.
3. Click the **Age Account** button.