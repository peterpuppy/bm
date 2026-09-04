# Np Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Overview/master-account-and-sub-account.html

# Accounts

Each user on PlayStation™Network is allocated with an account. Services of the PlayStation™Network can be used while signing onto the PlayStation™Network with this allocated account.

Note:

Signing to PlayStation™Network differs from logging in to the console. In typical cases, signing in will be performed automatically after logging in but be sure to distinguish between the two.

# Signup

Signup refers to the creation of a new account for PlayStation™Network. Signup can be performed using the PlayStation®5/PlayStation®4/PlayStation®3/PlayStation®Vita/PSP™ (PlayStation®Portable) system software or a PC web browser.

Note:

An account for PlayStation™Network can be shared between platforms.

# Master Account and Sub Account

The account for PlayStation™Network makes a distinction between the master account and the sub account.

A master account refers to an account for an adult that is created by users above a certain age (standards for this age level differ by country/region).

A sub account refers to an account for a child that is issued to users who are considered underage. A sub account is issued with the understanding that an adult will supervise PlayStation™Network usage of the sub account. Thus, several functions of the sub account are limited by parental control settings.

## Family

Users can combine master accounts and sub accounts to create a family.

In each family, there is one master account holder who is the family manager. The family manager can newly create sub accounts as accounts for children in the family. The family manager can also register other master account holders as adult family members, as well as remove family members from the family.

The family manager can set parental control for sub accounts in the family. Moreover, the family manager can set another master account holder in the family as the "guardian" and delegate the right to set parental control to them.

# Basic Information for Accounts

Basic information regarding an account includes the following.

## Account ID (SceNpAccountId)

An account ID is the primary key used in identifying accounts, and it does not change during the account's existence. It is used for management purposes and is not visible to the user.

Applications can obtain the account IDs of logged in users from their user IDs.

## Online ID (SceNpOnlineId)

The Online ID is used to identify accounts and is chosen by the user upon signup. The Online ID is displayed onscreen by the system software and by applications. It is a 3- to 16-character string composed of alphanumeric characters (A - Z, a-z, 0-9), hyphens, and/or underscores. The Online ID is guaranteed to be unique. However, there is a possibility that it will change upon a request from the system or user.

Applications can obtain the Online IDs of logged in users from their user IDs.

## Region

Region refers to the country/region of residence selected by the user upon signup. It cannot be changed after signup.

## Language Used

This is the "Language" selected by the user upon signup.

## Age

The user's age is calculated from the birth date input by the user and the customs of the country/region of residence selected upon signup. The birth date cannot be changed after signup.