# Auth Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/revoking-consent.html

# Providing Access Privileges to an Authorized App Server

This chapter outlines how the Auth Web API provides access privileges to an Authorized App Server.

Authorized Apps enables account association between an account for PlayStation™Network and an account in a non-SIE account system. This allows an Authorized App server to access PlayStation™Network user information for the linked account.

An account for PlayStation™Network can only link to one non-SIE account per Authorized App Server. If the non-SIE account is already linked to an account for PlayStation™Network, the Authorized App Server must not re-initiate the account association flow.

The [Customer Data](https://learn.playstation.net/bundle/policies-and-business-model-guidelines/page/Customer_Data.html) document describes the policy in processing personal information of PlayStation® platform and product customers, as well as the requirements on *Account Association*.

The Authorized App Server must store the following information for consent:

* PlayStation™Network account ID. The value of [sub claim in ID token](id-token-claims.html "This topic provides information on ID token claims.").
* PlayStation™Network access token
* PlayStation™Network refresh token

Obtain the ID token, access token, and refresh token using the OAuth 2.0 authorization code flow.

The Authorized App account association flow requires the user to provide explicit consent to share user information from PlayStation™Network to the Authorized App Server of the non-SIE account system.

# Associating Accounts with Authorized App Servers

Use Authorized App Servers when creating an association between an account in a non-SIE system and an account for PlayStation™Network.

Authorized App Servers ensure that user consent is obtained before the system that manages the non-SIE account can access the account for PlayStation™Network and create an association between them. User consent may include permission to access the account from anywhere and anytime, enabling offline access.

PlayStation™Network users can remove their consent at anytime, resulting in the removal or inactivation of the account association.

When creating an association with a non-SIE server account and an account for PlayStation™Network:

* You can associate a non-SIE server account with only one account for PlayStation™Network at a time.
* You can associate only one non-SIE server account to a specific account for PlayStation™Network at a time.

Associating a non-SIE account with only one account for PlayStation™Network

When an account in the non-SIE account system is already associated with an account for PlayStation™Network, the user should not see another association flow.

In the unlikely event that an account in a non-SIE account system is found to have associations with multiple accounts for PlayStation™Network, keep only one association and remove the others. When removing an association, revoke any PlayStation™Network refresh tokens by calling the `revokeToken` API.

Associating only one non-SIE account with an account for PlayStation™Network

When adding an association to a specific account for PlayStation™Network, the non-SIE server must check that no other account in the non-SIE server is associated with the target account for PlayStation™Network. If an association already exists for a different non-SIE server account, you cannot add a new association until the other association is removed.

In the unlikely event that multiple accounts in the non-SIE server are found to be associated to the same account for PlayStation™Network, keep only one association and remove the other. When removing an association, discard the PlayStation™Network refresh tokens without calling the `revokeToken` API.

# Obtaining User Consent on Console

This topic provides information on how to grant an Authorized App Server access to PlayStation™Network user information from the PlayStation®5 console.

To grant an Authorized App Server access to PlayStation™Network user information from a PlayStation®5 console, users must first provide consent from within a PlayStation®5 application.

The following is an example of a typical authorization flow on the PlayStation®5 console:

* A PlayStation®5 application calls `sceNpAuthGetAuthorizedAppCode` to initiate authentication and check if the user has provided consent.
* If the user has provided consent, `sceNpAuthGetAuthorizedAppCode` returns an authorization code (hereafter Authorized App Code) that can be exchanged by the Authorized App Server for access, refresh, and ID tokens.
* If the user has not granted consent, a consent required error is returned to the PlayStation®5 application. The PlayStation®5 application must launch the Authorized App dialog after receiving the error to initiate the consent flow. See [NpAuthAuthorizedAppDialog Library Overview](https://game.develop.playstation.net/resources/documents/SDK/10.000/NpAuthAuthorizedAppDialog-Overview/__document_toc.html) for details. If the application flow can also continue without obtaining user consent, the application may defer the launch of the Authorized App dialog.
* Once the user grants consent, `sceNpAuthGetAuthorizedAppCode` can return an Authorized App Code.

SIE recommends that you obtain a new Authorized App Code each time a user launches the application.

Obtaining User Consent on Console

# Obtaining User Consent on Web

This topic provides information on how to grant an Authorized App Server access to PlayStation™Network user information from a web browser or mobile device.

To grant an Authorized App Server access to PlayStation™Network user information from a web browser or mobile device, users must first sign-in to PlayStation™Network and provide consent.

A user's consent is obtained and managed by PlayStation™Network and the user interaction is transparent to the client application.

If a user declines to provide consent or can't give consent due to age restriction, the PlayStation™Network authorization server returns a `consent_required` error to the Authorized App Server.

The following is an example browser redirection response to the Authorized App Server if a user declines to provide consent:

```
HTTP/1.1 302 Found
Location: (redirect_uri)?error=consent_required&…
```

Obtaining User Consent on Web

For more information on redirecting users to the sign-in page, see [Authentication Features for Websites Reference - Sign-in Protocols - Redirect to the Sign-in Page](../Auth_for_Websites-Reference/redirect-to-the-sign-in-page.html).

# User Consent Revocation

This topic provides information on how to handle user consent revocations.

## Revoking User Consent

When a user of a non-SIE account system removes the association with their account for PlayStation™Network, the Authorized App Server must perform the following clean up actions:

1. Call the [revokeToken](https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Reference/0008.html) API to revoke any access or refresh tokens. The token revocation also revokes the user consent in PlayStation™Network.
2. Discard the PlayStation™Network access and refresh tokens for that user.
3. Remove the account association with PlayStation™Network or mark it as inactive.
4. Remove all personal information shared from PlayStation™Network and remove the account association.

Revoking User Consent

For details on how to call the `revokeToken` API, see [Auth Web API Reference - Token Revocation Endpoint - revokeToken](../Auth_WebAPI-Reference/0006.html).

## Updating Account Association after a User Consent Revocation

Users may revoke consent anytime on PlayStation™Network.

When a user revokes consent, all access and refresh tokens for that user that are issued based on the consent are also revoked. The next time the Authorized App Server tries to get a new access token using the refresh token, it receives an `invalid_grant` error and must perform the following clean up actions:

1. Discard the PlayStation™Network access and refresh tokens for that user.
2. Remove the account association with PlayStation™Network or mark it as inactive.
3. Remove all personal information shared from PlayStation™Network and remove the account association.

# Authorized App Refresh Tokens

This topic provides information on the refresh token used by Authorized Apps.

When a non-SIE account is associated with an account for PlayStation™Network, Authorized App Servers use a long-lived refresh token to access user information from PlayStation™Network when the user is not online.

The default lifespan for the Authorized App refresh token is 60 days. It is used when the user is online on a non-PlayStation® system. While the user is online on the non-PlayStation® system, the refresh token is rotated before it expires, with a duration of up to five years.

To obtain a refresh token for Authorized App Servers, include the `access_type` request parameter.

See [Auth Web API Reference - Token Endpoint - refreshAccessToken](../Auth_WebAPI-Reference/0005.html) for the API specification to obtain a new access token using a refresh token. In the response, a new refresh token may also be returned. When a new refresh token is returned, discard the old one and store the new one for future use.

The token refresh may fail with an `invalid_grant`error that indicates the refresh token is no longer valid. To re-establish access to PlayStation™Network, you must obtain a new set of access and refresh tokens.

Obtaining a new access token for Authorized App Server