# Auth Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/http-status-and-error-codes.html

# Appendix

This chapter provides information on various different topics related to the Auth Web API, such as call rate limits,
language codes, and HTTP status and error codes.

# OAuth Grant Types, Scopes, and Life Cycles

This topic provides information on the authorization scopes and grant types given to different product types.

The product type of an OAuth client determines the grant type for obtaining a PlayStation™Network access token and the scope for the access token. OAuth clients must use the scopes assigned based on this product type. Refer to [PlayStation™Network Service Setup Guide - Registering Titles - Supported Product Types](../../../SDK/latest/PSN_Service_Setup-Guide/supported-product-types.html) for the differences between product types. Note that access tokens obtained using authorization code grant type are specific to a particular user and the current gameplay session and access tokens from client credentials are not.

An OAuth client may obtain OAuth authorization codes for the same user and the same scope concurrently across different consoles or web browsers used by the user. Each access, refresh, and ID token from each authorization code will have independent life cycles.

OAuth Grant Types and Scopes

| **Product type** | **Grant type** | **Scopes** |
| --- | --- | --- |
| Application server | `authorization_code` | `psn:s2s openid id_token:psn.basic_claims`   * Specify these scopes in the `SceNpAuthGetAuthorizationCodeParameterV3` object used to call the `sceNpAuthGetAuthorizationCodeV3` API. * The `openid` scope is used to obtain an ID token together with the access token. See [ID Tokens](id-token.html "This topic contains information on ID tokens and how to obtain them.") for details. * The `id_token:psn.basic_claims` scope is used to include `age`, `online_id`, and `device_type` claims in the ID token. |
| Authorized App server | `authorization_code` | `psn:s2s.authorizedApp openid id_token:psn.basic_claims`  * For authentication on websites, specify scopes in the `scope` query parameter in the [Authentication Features for Websites Reference - Sign-in Protocols - Redirect to the Sign-in Page](../Auth_for_Websites-Reference/redirect-to-the-sign-in-page.html) API. * For obtaining access on PlayStation®5 consoles, specify scopes in the `scope` parameter of the `SceNpAuthGetAuthorizedAppCodeParameter` object used to call the `sceNpAuthGetAuthorizedAppCode` API and in the `SceNpAuthAuthorizedAppDialogParam` object for requesting consent using the NpAuthAuthorizedAppDialog library. |
| Application server (client credentials) | `client_credentials` | `psn:s2s.service` This scope is used in the `scope` request parameter of the [Auth Web API Reference - Token Endpoint - getAccessTokenWithClientCredentials](../Auth_WebAPI-Reference/0004.html) API. |
| Back office server | `client_credentials` | `psn:backoffice` This scope is used in the `scope` request parameter of the [Auth Web API Reference - Token Endpoint - getAccessTokenWithClientCredentials](../Auth_WebAPI-Reference/0004.html) API. |

**Error Response for Invalid Scope or Grant Type**

When the scope submitted in an OAuth authorization or token request is invalid, malformed, or cannot be used by the client, an error response with `error=invalid_scope` is returned. When the client is not authorized to use the `authorization_code` or `client_credentials` grant types, an error response with `error=unauthorized_client` is returned. For more information, see [HTTP Status and Error Codes](http-status-and-error-codes.html "This topic provides the Auth Web API's HTTP status and error codes.").

# Call Rates to the Auth Web API

This topic provides information on how to stay within call rate limits when using the Auth Web API.

Clients must follow the guidelines below to control the call rate to the Auth Web API. Rate limits may be applied without notice.

Call Rates

| **Request** | **Rate** |
| --- | --- |
| `GetJwks` | Clients must cache the response according to the Cache-Control response header. Call this API only when needed to refresh the cache. |
| `GetAccessTokenWithAuthorizationCode` | Clients cannot use an authorization more than once. After an authorization code is used to get an access token, the same authorization code cannot be used anymore.  Therefore, to control the call rate, clients should control the rate of obtaining authorization codes by caching the access token obtained using the authorization code. Use the value of the `expires_in` parameter in the token response to determine how long the access token may be cached. Then, obtain a new authorization code only when the access token has been revoked, has expired or is about to expire and there is no refresh token to obtain a new access token. |
| `GetAccessTokenWithClientCredentials` | Clients must cache a client credentials access token according to the `expires_in` parameter in the token response.  Obtain a new access token only when the access token obtained earlier has been revoked, has expired or is about to expire. |
| `RefreshAccessToken` | Clients should cache access tokens according to the `expires_in` parameter in the token response.  Refresh access tokens only in the cases where the access token obtained earlier has been revoked, has expired or is about to expire at the time when the client needs an access token to call PlayStation™Network API. |
| `RevokeToken` | A client can revoke only access tokens issued to itself. When revocation is needed, only one call is required. |

# ID Token Claims

This topic provides information on ID token claims.

An ID token may also contain other additional claims. Any claims that the client does not understand must be ignored.

If a claim not listed in the table below is required, please contact us through DevNet.

List of ID token Claims

| **Claim Name** | **Claim Type** | **Description** |
| --- | --- | --- |
| `ver` | String | Version. |
| `iss` | String | Issuer. Identifier of ID token issuer. The value is always `"https://auth.account.sony.com"`. |
| `env_iss_id` | String | NP environment ID of the issuer.   * np: 256 * prod-qa: 8 * sp-int: 1 |
| `aud` | Array of String | Audience. Audience(s) that this ID token is intended for. It always contains the OAuth 2.0 client\_id of the application that requested the ID token.  In the future, this claim may contain other client ID(s) and in that case all client IDs in the claim must be known/trusted by the application that validates this ID token. |
| `iat` | Number | Issued at. UTC epoch seconds when the token is issued. |
| `exp` | Number | Expiration. UTC epoch second of token expiration. |
| `sub` | String | Subject identifier. Account ID of the end-user that has authenticated. |
| `legal_country` | String | Country/region of residence of the end-user. Value is the two-letter upper case country/region code as defined in ISO 3166-1 alpha-2. |
| `locale` | String | Account language of the end-user. See Language Codes for possible values. |
| `nonce` | String | A String value used to associate a client session with an ID token, and to mitigate replay attacks. The value is case sensitive and is the same as the value submitted in the authorization request. |
| `at_hash` | String | Access token hash. Value is case sensitive and generated in the following steps:  (1) Hash access\_token value with SHA-256.  (2) Take the left-most 128 bits.  (3) Base64url encode the value (without padding). |
| `age` | Number | Age of the end-user.  This claim requires an additional scope: `id_token:psn.basic_claims`. |
| `device_type` | String | Device type. One of the following:   * PlayStation®5: "PS5" * PlayStation®4: "PS4" * PlayStation®Vita: "PSVITA" * PlayStation®3: "PS3"   This claim requires an additional scope: `id_token:psn.basic_claims`.  ID tokens in authentication features for websites do not include this claim. |
| `online_id` | String | Online ID of the end-user.  This claim requires an additional scope: `id_token:psn.basic_claims`. |
| `duid` | String | Device Unique Identifier. Unique identifier of the device where the end-user has authenticated.  This claim requires an additional scope to obtain.  ID tokens in authentication features for websites do not include this claim. |
| `email` | String | Primary email address currently used as sign-in ID by the end-user.  This claim is available in ID tokens issued to Authorized App Servers. |
| `sbid` | String | Sandbox ID.  The unique identifier of the sandbox selected by the client application or the environment that runs the application when this ID token is created.  If the application or its environment has not selected a sandbox, this claim is omitted in the ID token. |

# Language Codes

This topic provides a list of valid language codes used in ID tokens.

List of Language Codes

| **Value** | **Description** |
| --- | --- |
| `ar-AE` | Arabic |
| `cs-CZ` | Czech |
| `da-DK` | Danish |
| `de-DE` | German |
| `el-GR` | Greek |
| `en-GB` | English (United Kingdom) |
| `en-US` | English (United States) |
| `es-419` | Spanish (Latin America) |
| `es-ES` | Spanish (Spain) |
| `fi-FI` | Finnish |
| `fr-CA` | French (Canada) |
| `fr-FR` | French (France) |
| `hu-HU` | Hungarian |
| `id-ID` | Indonesian |
| `it-IT` | Italian |
| `ja-JP` | Japanese |
| `ko-KR` | Korean |
| `nl-NL` | Dutch |
| `no-NO` | Norwegian |
| `pl-PL` | Polish |
| `pt-BR` | Portuguese (Brazil) |
| `pt-PT` | Portuguese (Portugal) |
| `ro-RO` | Romanian |
| `ru-RU` | Russian |
| `sv-SE` | Swedish |
| `th-TH` | Thai |
| `tr-TR` | Turkish |
| `uk-UA` | Ukrainian |
| `zh-Hans` | Chinese (Simplified) |
| `zh-Hant` | Chinese (Traditional) |

## Handling Unknown Language Codes

Applications must gracefully handle unsupported language codes without breaking user experience. Additionally, clients must assume that new language codes may be added in the future.

# HTTP Status and Error Codes

This topic provides the Auth Web API's HTTP status and error codes.

Authorization Endpoint

| `Status code` | `Error` | **Description** |
| --- | --- | --- |
| `302` | `interaction_required` | The authorization server requires end-user interaction of some form to proceed. |
| `302` | `login_required` | The authorization server requires end-user authentication. |
| `302` | `consent_required` | The authorization server requires user consent. |
| `302` | `server_error` | An unknown error has occurred. |
| `302` | `temporarily_unavailable` | The server is temporarily too busy. |
| `400` | `invalid_request` | The request is invalid. |
| `400` | `invalid_scope` | The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the resource owner. |
| `400` | `unauthorized_client` | The authenticated client is not authorized to use this authorization grant type. |

Jwks Endpoint

| `Status code` | `Error` | **Description** |
| --- | --- | --- |
| `429` | `temporarily_unavailable` | The request cannot be processed because of rate limit. |
| `500` | `server_error` | An unknown error has occurred. |
| `503` | `temporarily_unavailable` | The server is temporarily too busy. |

Token Endpoint

| `Status code` | `Error` | **Description** |
| --- | --- | --- |
| `400` | `invalid_grant` | The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client. |
| `400` | `invalid_request` | The request is invalid. |
| `400` | `invalid_scope` | The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the resource owner. |
| `400` | `unauthorized_client` | The authenticated client is not authorized to use this authorization grant type. |
| `401` | `invalid_client` | Bad client credentials. |
| `429` | `temporarily_unavailable` | The request cannot be processed because of rate limit. |
| `500` | `server_error` | An unknown error has occurred. |
| `503` | `temporarily_unavailable` | The server is temporarily too busy. |

Sign Out Endpoint

| `Status code` | `Error` | **Description** |
| --- | --- | --- |
| `302` | `server_error` | An unknown error has occurred. |
| `302` | `temporarily_unavailable` | The server is temporarily too busy. |
| `400` | `invalid_request` | The request is invalid. |

# Error Handling

This topic provides information on how to handle errors in the Auth Web API.

Clients must handle an error response from Auth Web API based on the HTTP status code and the value of the `error` response parameter:

* For HTTP status code = `500` (or `302` with `error=server_error`), log the error and then restart the user flow.
* For HTTP status code = `503` or `429` (or `302` with `error=temporarily_ unavailable`), log the error and retry after some wait time with exponential back off between retries.
* For HTTP status code = `400`, log the error and do not retry. The error response parameter describes more details on the error. If needed, handle the error based on this parameter.

  + When an authorization code or refresh token is invalid or has expired or been revoked `invalid_grant` error is returned. In this case, restart the user authentication flow to retrieve a new authorization code.
* Do not programmatically handle error based on `error_code`, though it should be logged. This `error_code` is the PlayStation™Network specific part of the implementation of the OAuth specification.

While an error response also includes `error_code` and `error_description` parameters, they are intended for simple troubleshooting only. Do not present them to users or use them to handle errors.