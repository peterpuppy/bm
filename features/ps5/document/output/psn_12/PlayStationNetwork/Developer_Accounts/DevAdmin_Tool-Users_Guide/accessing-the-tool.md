# DevAdmin Tool User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/DevAdmin_Tool-Users_Guide/accessing-the-tool.html

# Using the DevAdmin Tool

This chapter provides information on how to access and use the DevAdmin Tool.

# Accessing the DevAdmin Tool

This topic provides information on how to access the DevAdmin Tool.

Your developer support representative provides you access to the DevAdmin Tool. You must have an active PlayStation™Network account to access the DevAdmin Tool.

To access the tool, navigate to [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).

Accessing Login Page

Entitlements and basic account information are displayed on the main page.

Main Page

# Clearing Entitlements

This topic provides information on how to clear and delete entitlements using the DevAdmin Tool.

In the NP commerce system, the product list displayed in a store and the category content data obtained by the Commerce Service API are updated according to whether or not a product has been purchased, and the addition of new eligibility rules. Due to this, it is necessary to delete each account's entitlement information during development, regardless if a content or service entitlement has already been purchased and is owned.

Use the DevAdmin Tool to confirm or delete entitlements. To clear entitlements for an account:

1. From the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug), select **Clear all Entitlements**. This deletes all entitlements.
2. Select **Save Changes**.

Clearing Entitlements

# Aging an Account

This topic provides information on how to age accounts that have subscription-type products using the DevAdmin Tool.

When developing a subscription-type product, while it is necessary to test what happens when the validity period ends, it is not realistic to wait for the actual subscription period to pass. You can use the DevAdmin Tool to adjust the validity period of a purchased subscription.

By adjusting the validity period of a purchased subscription-type product to the end of the subscription duration, you can test the behavior of your implementation when the subscription ends.

During testing, entitlements are still attainable immediately after the end of the subscription. Entitlement are no longer attainable after a certain grace period passes after subscription ends.

To age an account:

1. Navigate to the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).
2. Select the days, months, or years from the drop down.
3. Enter the amount of days, months, or years you want to age the account by.
4. Click **Age Account**.

Aging an Account

You are notified if the account aging was successful.

Aging an Account Success Message

# Resetting a Password

This topic provides information on how to reset the password for an account using the DevAdmin Tool.

To reset the password for an account:

1. Navigate to the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).
2. Click **Reset Password**.
3. Enter the new password and click **Save Changes**.

Resetting a Password

# Changing an Online ID

This topic provides information on how to change a user's online ID using the DevAdmin Tool.

You can use the DevAdmin Tool to test the effects of changing a user's online ID.

Changing the online ID is instant but it typically takes between 10-15 minutes for the changes to propagate fully across servers in the development environment. SIE recommends that you restart the console after changing the online ID to clear all caches.

To change the Online ID of an Account:

1. Navigate to the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).
2. Type in the requested changes into the Online ID text box. The new online ID must be unique.
3. Click **Update**.

Changing Online ID

# Viewing Online ID Change History

This topic provides information on how to view the history of online ID changes in an account using the DevAdmin Tool.

The DevAdmin Tool supports viewing the history of online ID changes for an account. To view the online ID change history:

1. Navigate to the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).
2. Click the clock icon under **Online ID**.

You can reclaim and release previous online IDs associated with an account.

To reclaim or release an online ID:

1. Click the clock icon under **Online ID**.
2. Click **Reclaim** or **Release** for the online IDs you want to reclaim or release.

Online ID History

# Managing Verified Roles

DevAdmin Tool allows you to manage verified roles for accounts in the development environment.

To add a verified role to an account:

1. Click **Edit** next to verified role.
2. Select the verified role from the drop-down menu.
3. Set the display name for the account.
4. Click **Save Changes**.

To remove a verified role from an account:

1. Click the **Edit** button next to verified role.
2. Click **Un-Verify**.

# Restricting Social Features

This topic provides information on how to test the restriction of social features using the DevAdmin Tool.

The DevAdmin Tool allows you to test social feature restriction by limiting a PlayStation™Network account from interacting with other accounts in various social features. This setting cannot be used for verification for communication restriction on PlayStation®4, PlayStation®Vita, and PlayStation®3, as sign-in to PlayStation™Network with the setting is blocked on these platforms.

To test social feature restriction for an account in DevAdmin:

1. Navigate to the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).
2. Click **Edit** under **Communication Restriction**.
3. Select **Restricted** or **Unrestricted**.
4. Click **Save** to apply changes to the account.

Communication Restriction

# Closing an Account

This topic provides information on how to close an account using the DevAdmin Tool.

The DevAdmin Tool allows you to test closing an account on the PlayStation™Network. To do this:

1. Navigate to the [DevAdmin Tool](https://devadmin.sp-int.tools.playstation.net/?sid=26&pid=dtug).
2. Click **Close Account**.
3. Click **I Accept** to close the account. Closing an account is a permanent action.

Closing an Account