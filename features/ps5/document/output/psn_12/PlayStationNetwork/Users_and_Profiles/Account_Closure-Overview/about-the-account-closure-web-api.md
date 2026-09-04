# Account Closure Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Account_Closure-Overview/about-the-account-closure-web-api.html

# About the Account Closure Web API

The Account Closure Web API provides information on
users who have closed their PlayStation™Network accounts, and
no longer wish to receive PlayStation™Network services.

The API covers accounts registered in the SIEE, SIEA, and
SIEJA regions, including Russia, India, Australia, and New Zealand.

**Important**: The General Data Protection Regulation (GDPR), went into effect in the
European Union on May 25, 2018. If your game servers store personal information obtained
through Sony Interactive Entertainment or PlayStation™Network of accounts in the SIEE
region, you must monitor the Account Closure Web API on a regular basis. Upon receipt of an
account closure request, you must act in accordance with applicable law, including any
requirements to erase the user's personal information.

Note: All licensed developers and publishers must comply with this requirement, regardless of
their region of operation. Account closure requests received through the Account Closure
Web API should be considered a request for account de-linking.

# PlayStation™Network Account Data Disclosure

This topic provides details on what types of
identifiable user information PlayStation™Network provides to third-party developers,
and how that information is handled.

SIE discloses certain pieces of identifiable user information to you for active
PlayStation™Network accounts. For example, the account's Online ID, Account ID, and basic
attributes. When a user requests account closure, the GDPR requires that a notification be
sent to anyone to whom personal information has been disclosed.

The Account Closure Web API requests return records of accounts closed within a certain
time frame. If you do not specify a time frame, the API uses the earliest possible date,
and the current time as the end date. The response appends all new records of closed
accounts to the end of the list. Entries are not inserted at an earlier date or time,
regardless of when the account was actually closed. This means you do not need to check
previously queried time frames.

Fetch the list of closed accounts once per day to keep your systems compliant and up to
date. When receiving account closure records, you must comply with applicable legal
requirements. Verify and delete received account closure records as soon as you determine
whether or not you are storing data relating to the closed accounts. If you are not storing
data in relation to an account closure record, do not retain that record.

SIE recommends that you keep a record of your queried dates.

# Reference Materials

This topic provides links to topics that relate to the Account Closure Web
API.

Refer to the following document for general topics such as call procedures for
PlayStation™Network APIs, including advance preparations (such as obtaining a base URL),
error handling, and call rate limits.

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

For details of the Account Closure Web API, refer to the following document:

* [Account Closure Web API Reference](../Account_Closure_WebAPI-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Account Closure Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Account_Closure_WebAPI-ReleaseNotes.html)