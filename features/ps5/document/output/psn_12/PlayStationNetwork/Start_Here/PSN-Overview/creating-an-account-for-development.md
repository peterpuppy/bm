# PlayStation™Network Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN-Overview/creating-an-account-for-development.html

# Reference Information

This section provides reference information for certain workflows when developing with PlayStation™Network.

# NP IDs For PlayStation®5

This topic describes identifiers used by PlayStation®5 applications that use the PlayStation™Network, along with data used for identifying applications and services.

## IDs Used in Applications

**NP Title ID**

The NP Title ID represents a single title. It is in the format XXXXYYYYY\_00 (with letters for XXXX and numbers for YYYYY). The NP Title ID is assigned by SIE. Unique NP Title IDs are also assigned to application servers, websites, and companion applications that use features of the PlayStation™Network.

**NP Title Secret**

The NP Title Secret is the secret information that is paired with an NP Title ID. It is used to prove ownership of the NP Title ID. Use sufficient precaution to make sure that it is not leaked to third parties.

**NP Service Label**

The NP Service Label is used to identify instances of the same service on the same NP Title ID. It is a decimal integer between 1 and 12 digits long. You must specify an NP service label when you make a service request for some PlayStation™Network services. For the range of valid NP service labels for each service, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

Multiple NP service labels are used for a single NP Title ID in the following cases:

* The title references a leaderboard belonging to a title released in the past, in addition to its own leaderboard.
* The title is to be released for multiple platforms, and it is necessary to set title cloud storage for users per platform for mutual use.
* The title references additional contents that are shared with another title, in addition to its own additional contents.

**NP Communication ID**

The PlayStation™Network server uses the NP Communication ID as an ID for some services including the title cloud storage. However, there is no need to directly specify the NP Communication ID in a program; the appropriate NP Communication ID is selected for each service according to the NP Title ID and NP service label.

Relationships of the NP Title ID, NP Service Label, and NP Communication ID

**Service ID**

The PlayStation™Network server uses the Service ID as an ID for the PlayStation™Store Delivered Content (PSSDC) service. However, there is no need to directly specify the Service ID in a program; the appropriate Service ID is selected for each service according to the NP Title ID and NP service label.

Relationships of the NP Title ID, NP Service Label, and Service ID

**Entitlement Label**

Entitlement Labels are identifiers assigned to downloadable products or products that have an expiration date. They are assigned by content providers, rather than by SIE, and the only characters allowed are numbers and upper-case letters and (A-Z, 0-9).

* For unified entitlements, the entitlement labels are 16 digits long. Applications pass the entitlement label and the NP service label of the PlayStation™Store Delivered Content service (PSSDC) to the AppContent library to determine the player's entitlement privileges before mounting and accessing additional content data. When registering a package applicable to a unified entitlement on a server, the label of the Content ID is used as the entitlement label for the package. Therefore, specify the entitlement label for the label of the Content ID upon creating the package.
* For service entitlements, the entitlement labels are 6-digits long. Service entitlements are used for products that are shared with PlayStation®3 or PlayStation®Vita. Applications can obtain entitlement information for service entitlements by passing the entitlement label and the NP service label into the Entitlements Web API. The Entitlements Web API is also used for updating the usage count for consumable products.

Note that the Service ID and entitlement label are joined by a hyphen and registered as the entitlement ID when registering a unified entitlement or service entitlement.

**Example:** Entitlement ID of a unified entitlement

IV0002-NPXS00004\_00-ENTITLEMENT00001 (the "ENTITLEMENT00001" part is the entitlement label part)

**Example:** Entitlement ID of a service entitlement

IV0002-NPXS00004\_00-SVC001 (the "SVC001" part is the entitlement label part)

## IDs Used When Creating a Package

**Service ID**

The Service ID is an ID derived from the NP Title ID. It consists of a combination of the SIE-assigned 6-character label and the NP Title ID, separated by a hyphen.

**Example:** IV0002-NPXS00004\_00

**Content ID**

The Content ID is a combination of the Service ID and a 16-character label, separated by a hyphen. The label is assigned by the content provider, not by SIE. The only characters allowed for the label are numbers and upper-case letters (A-Z, 0-9).

Specify the Content ID label in the Publishing Tools when creating a package file.

**Example:** IV0002-NPXS00004\_00-0000111122223333 (where "0000111122223333" is the label)

When a package is registered with the server, the label part of the Content ID is used as the Entitlement label for the package.

## IDs Handled in the PlayStation™Store

**Category ID**

The Category ID is used to identify nodes in the PlayStation™Store catalog, which has a tree-like structure. This catalog defines the application's Title Store, which can be browsed by using screen displays or by using the In-Game Catalog Web API.

The top node of the catalog is identified by the Title Top Category ID, which has the same format and value as the Service ID for the application. For other nodes in the catalog, the Category ID is a combination of the Service ID and a 4 to 16-character label, separated by a hyphen. The label is assigned by the content provider, not by SIE. The only characters allowed for the label are numbers and upper-case letters (A-Z, 0-9).

**Example:** IV0002-NPXS00004\_00 (for the Title Top Category)

**Example:** IV0002-NPXS00004\_00-CATG000011112222 (for all other categories; where "CATG000011112222" is the label)

**Product ID**

A Product represents digital data and services that belong to a given Service ID. This could include additional data or services with monthly charges, as an example.

The Product ID is a combination of the Service ID and a 16-character label, separated by a hyphen. The label is assigned by the content provider, not by SIE. The only characters allowed for the label are numbers and upper-case letters (A-Z, 0-9).

**Example:** IV0002-NPXS00004\_00-0000111122223333 (where "0000111122223333" is the label)

**SKU ID**

A SKU is a sales unit that associates prices with a product. It is used to set the prices in a store for countries and regions within a SIE region.

The SKU ID is a combination of the Product ID and a 4-character label, separated by a hyphen. This 4-character value is called the "SKU label".

**Example:** IV0002-NPXS00004\_00-0000111122223333-J001 (where "J001" is the SKU label)

The SKU label is assigned by SIE. The only characters allowed for the SKU label are
numbers and upper-case letters (A-Z, 0-9). The first character of the SKU label is fixed
per SIE region as shown in the table below.

First Character of SKU by SIE Region

| **Region** | **First Character of the Label** |
| --- | --- |
| SIEA | U |
| SIEE | E |
| SIEJA (Japan) | J |
| SIEJA (excluding Japan) | H (K used for Korea) |

The format for the other three characters is also fixed per SIE region.

Applications must obtain the SKU IDs for additional content using the In-Game Catalog Web API and use them for purchase processing. Note that applications must always obtain the SKU ID programmatically, and not assume that it has a fixed value.

## IDs Handled on Websites and in Companion Applications

**Client ID**

The Client ID identifies a unique application server or website, or a companion application on a smartphone or tablet, that uses PlayStation™Network Web APIs. The Client ID is assigned by SIE. Clients use the Client ID to obtain access tokens using the OAuth2.0 protocol.

**Client Secret**

This is the secret information that is paired with a Client ID. It is used to prove ownership of the Client ID. Use sufficient precaution to make sure that it is not leaked to third parties.

# NP Environments

This topic provides an overview of the NP environments available during development.
Multiple NP environments are provided for PlayStation™Network services, and each has a
different purpose.

The provided environments are as follows (the environment name is encased with []).

* **Development environment [sp-int]:** This environment is used by developers for
  developing and debugging applications.

* **Certification environment [prod-qa]:** This environment is used by SIE for performing platform certification on submitted masters.

* **Production environment [np]:** This environment is used by end users to execute
  released titles.

You can switch the currently active NP environment by selecting [Settings] - [★Debug Settings] - [PlayStation™Network] - [NP Environment]. The default setting on the PlayStation®5 Development Kit and Testing Kit is sp-int.

The Client ID, Title ID, and other related settings are shared over NP environments. However, user accounts are specific to each NP environment. For example, even if a programmer has an account in the production environment, a separate account is needed to use the development environment.

# Creating an Account for Development

This topic covers how to create an account for PlayStation™Network application
development.

To develop an application that uses PlayStation™Network, you must have an account in the
PlayStation™Network development environment. Accounts can only be used on one PlayStation®5
Development Kit that is accessing the PlayStation™Network at any one time. Accounts are not
specific to the platform on which they were created, so the same account can be used to
develop applications for PlayStation®5, PlayStation®4, PlayStation®3, and PlayStation®Vita.
Accounts are specific to each NP environment, so you must create an account in the
development environment even if you already have one in the production environment. An
email address is used as the sign-in ID for an account. Accounts in different environments
can use the same sign-in ID.

You can create an account using one of the following:

* System software
* PC web browser
* Host Tools (`prospero-ctrl`)

## Items Set upon Account Creation

**Sign-in ID and Password**

Accounts for PlayStation™Network use an email address as a sign-in ID. You can specify
any e-mail address and password when creating an account. However, when using a PC web
browser to create an account, a confirmation e-mail is sent to the registered address,
so the e-mail address must be valid. E-mails may be sent to the sign-in ID address for
other purposes as well, so avoid using another person's e-mail address. Make sure to
remember this e-mail address as you need it to sign in to the PlayStation™Network.

**Account ID**

An Account ID is an arbitrary ID which uniquely identifies every user on the
PlayStation™Network. It is assigned automatically when the account is created and cannot
be changed. Game applications and application servers should use the Account ID to
manage the account information, because the user's Online ID may change.

**Online ID**

An Online ID is an arbitrary ID that can be set by the user when they create their
account. Users can also change their Online ID at any time after account creation.
Online IDs consist of 3 to 16 alphanumeric characters (A-Z, a-z, 0-9), hyphens (-), and
underscores (\_). The PlayStation™Network guarantees that Online IDs are unique, so a
user cannot set their Online ID to be the same as another one that is currently in use.
However, it is possible for a user to select an Online ID that was previously used by a
different user, but which is not currently in use.

**Billing Information**

Accounts for development do not need billing information.

**Notes on Creating Accounts for Korea**

You cannot use the system software or Host Tools (`prospero-ctrl`) to
create accounts for Korea. Create accounts for Korea on a PC web browser by following
the instructions in the [Creating a Master Account on a PC Web Browser](creating-an-account-for-development.html#psn-overview_8_3__psn-overview_8_3_4) and [Creating a Sub Account on a PC
Browser](creating-an-account-for-development.html#psn-overview_8_3__psn-overview_8_3_5) items.

Although when creating an account for Korea in the production environment requires an
Internet Personal Identification Number (i-PIN), an account for Korea can be created
without an i-PIN in the development environment.

## Creating Accounts Using the System Software

When the user currently operating the system software does not have an account for
PlayStation™Network, the **Sign-In to PlayStation™Network** option is displayed. When
the **Quick Account Sign-Up** button is selected, the signup process application is
launched. Follow the application instructions and complete signup.

## Quick Sign Up

You can create a new account with fewer input items by selecting **★Quick Sign Up**.
Both master accounts and sub accounts can be created using Quick Sign Up.

Note: When Quick Sign Up is used to create a sub account, a master account is also
automatically created as the family manager. When logging in with the sub account, this
master account may be displayed on system software screens (the "Family Management"
screen, for example). This master account is created as a matter of convenience for the
system; it cannot be used and should be ignored.

## Creating a Master Account on a PC Web Browser

1. Access the account creation page for the development environment at <https://account.sp-int.sonyentertainmentnetwork.com/>.

Note: For the browser, use the latest version of Internet Explorer, Firefox, Safari or
Chrome.

1. On the sign-in screen, select **Create a New Account** in the lower section of
   the screen.
2. On the **Create Account** screen, select **Start**, enter the required
   information for the new account, and click **I Agree. Create My Account.**

Note: When sub accounts are created with this master account, an e-mail is sent to the
Sign-In ID (e-mail address) of the master account. Use an existing e-mail address as the
Sign-In ID.

1. When the dashboard is displayed for the created account, enter detailed
   information.
2. Click the dashboard's **Update Account** and follow the instructions onscreen to
   enter the account information.
3. When all the information is entered, you can use the account to sign in to the
   PlayStation™Network.

## Creating a Sub Account on a PC Browser

When you have created a master account, you can create a sub account using the following
procedure:

1. Access the account creation page of the development environment at <https://account.sp-int.sonyentertainmentnetwork.com/> and sign
   in with the master account.
2. On the **Account** tab, click **Family Management**. Follow the instructions
   onscreen to move to the family management screen;
3. If prompted to sign in again on the family management screen, sign in with the same
   master account.
4. Click the **Set Up Now** or **Add Family Member** button.
5. Enter basic information for the sub and click **I Agree. Continue.**
6. Follow the instructions on the screen and configure the parental control settings.
   Depending on the age set for the sub account, a confirmation e-mail is sent to the
   master account's e-mail address. The URL in the confirmation e-mail must be clicked
   to continue.
7. Enter detailed information about the created sub account.
8. Access the start page with the created sub account and sign in.
9. Click the **Dashboard** tab and click the **Update Account** button.
10. Follow the instructions on the screen to enter the account information. When this
    information is entered, it becomes possible to sign in to the PlayStation™Network
    with the created sub account.

## Creating Accounts Using the Development Kit

Creating an account on the Development Kit is the same as creating an account using the
system software. Select **Sign-in to PlayStation™Network**. An application is started
to process sign-up; follow the application instructions.

Note: When creating an account using a web browser on a PC, name input and the
corresponding privacy settings are not supported. When creating an account on the
Development Kit, note that you are required to set this additional information.

## Creating Accounts Using Host Tools (`prospero-ctrl`)

When you create a new account using Host Tools, `prospero-ctrl` uses the
Quick Sign Up feature on DevKit/TestKit to create the account.

```
> prospero-ctrl user psn-signup User1 JP

1/1 Processing quick sign up....

0        20        40        60        80       100
|____.____|____.____|____.____|____.____|____.____|
===================================================
SignInId: <Sign-in ID of the created account>
Password: <Password of the created account>
```

See [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html) for more information on
`prospero-ctrl` commands.

## Switching Accounts

On PlayStation®5, multiple local users can be created, each with an account for
PlayStation™Network. When necessary, switch local users to use a specific account for
PlayStation™Network.

# Features Restricted by Title Dev/Title Admin Roles During Development

This topic covers how to restrict feature access during development by using the Title
Dev and Title Admin roles.

In order to prevent sensitive game title data from being exposed during development, some PlayStation®5 features rely on accounts for PlayStation™Network to have a Title Dev or Title Admin role assigned through either DevNet or Development Accounts.

## Configuring Access Privileges for Accounts in the Development Environment

**Steps when Using DevNet**

Title Dev and Title Admin can be configured from a DevNet product detail page using the following procedure:

1. Log in to DevNet with an account with Owner or Editor privileges.
2. Navigate to the product page.
3. Select the Title Admin/Title Dev tab on the product detail page.
4. To add access privileges for an account for PlayStation™Network, enter the e-mail address linked to the account in the development environment, select either **Title Dev** or **Title Admin** as a role, then click **Add**.

To remove a user that currently has access privileges, click on a registered user and select **Remove**.

**Steps when Using Development Accounts**

Users with collaborator permission (Editor or above) on a DevNet product can add Title Dev role in Development Accounts using the following procedure:

1. Access Development Accounts from the "DEVELOP" section in the Global Header of PlayStation™Partners.
2. Select either **Bulk Add Title Privileges** on the table header, or select **Manage Title Privileges** in the menu for individual accounts

For details, please refer to the [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html).

Note: To properly reflect changes, it is recommended to reboot the DevKit.

Note: There is a system limitation in that a single account can only be associated to 256 products.

## Features Currently Restricted by Title Dev/Admin Roles

The features listed in the table below are currently being restricted by Title Dev/Title
Admin roles in the development environment:

Features Restricted by Role

| **Feature/Functionality** | **Limitations** |
| --- | --- |
| Game Hub Preview | The Game Hub Preview Application requires Title Dev/Title Admin to be configured. Detailed usage can be found in the [PlayStation™Network Game Hub Preview Application Overview](../PSN_Game_Hub_Preview_Application-Overview/__document_toc.html). |
| Title Store/Regional Store Previews | The Title Store/Regional Store Previews require Title Dev/Title Admin to be configured. Detailed usage can be found in the [PlayStation™Network Commerce Programming Guide](../PSN_Commerce-Programming_Guide/__document_toc.html). |
| Activities | Activities require Title Dev/Admin roles to be configured when the application is not running on the DevKit. The Title Dev/Admin roles allow viewing of activities (including images of Activities) per the Universal Data System service. This restriction includes the control center UI as well as the debug UIs for activities provided in the debug settings.  The below issues occur if the user does not have title permissions.   * Action cards in the control center UI will not be shown. * WS-119115-8 will be shown in the debug UIs for activities. Refer to the [Game Intent System Overview - Debugging Support for Developing Game Intent-Compatible Applications](../Game_Intent_System-Overview/debugging-support-using-the-system-software.html) for details.   Note: This also applies to activities shown in correlation with other features. |
| Trophy | Trophy provides two modes (Online Mode and Offline Mode). When Online Mode is used, Trophy requires Title Dev/Admin roles to be configured when the application is not running on the DevKit. The Title Dev/Admin roles allow viewing of trophies (including the images). This restriction includes the system software UI as well as Preview Trophy UI provided in the debug settings.  Refer to the [Trophy System Overview - Debugging Support Provided by the System Software](../Trophy_System-Overview/debugging-support-provided-by-the-system-software.html) for details. |
| Profile | In order for the game to be visible in the "Recently played" area on the profile when viewing other user's profiles, the viewing user requires Title Dev/Admin roles to be configured. |
| Cloud Streaming Preview | The Cloud Streaming Preview Application requires Title Dev/Admin roles to be configured to access your PlayStation®5 applications that are deployed on cloud streaming servers. For more information, see [PlayStation™Network Cloud Streaming Overview](../PSN_Cloud_Streaming-Overview/__document_toc.html). |