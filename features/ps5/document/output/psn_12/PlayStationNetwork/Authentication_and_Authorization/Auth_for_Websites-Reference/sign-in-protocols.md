# Authentication Features for Websites Reference – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_for_Websites-Reference/sign-in-protocols.html

# Sign-in Protocols

# Redirect to the Sign-in Page

Start of user authentication

## Description

To perform user authentication with the authentication features for websites, forward the user to the sign-in page below using a link or redirection.

## URL

## Production Environment for End Users

```
https://ca.account.sony.com/api/authz/v3/oauth/authorize
?service_entity=urn%3Aservice-entity%3Apsn
&response_type=code
&client_id=XXXXX
&redirect_uri=YYYYY
&scope=ZZZZZ
```

## Development Environment for Developers

```
https://ca.sp-int.account.sony.com/api/authz/v3/oauth/authorize
?service_entity=urn%3Aservice-entity%3Apsn
&response_type=code
&client_id=XXXXX
&redirect_uri=YYYYY
&scope=ZZZZZ
```

## Parameters

Be sure to apply the percent-encoding mechanism defined in RFC 3986 (<http://tools.ietf.org/html/rfc3986>) to each parameter.

## Required Parameters

* `service_entity`

  Always specify `urn:service-entity:psn`.
* `response_type`

  Always specify `code`.
* `client_id`

  Specify the Client ID issued from the Developer Network website (<https://game.develop.playstation.net/>). A Client ID is an ID for identifying the authorization-target application or website with the PlayStation™Network Web APIs.
* `redirect_uri`

  Specify the URL of the page for the user to be redirected back to after sign-in.

  The scheme must be https. Moreover, the beginning of this URL must comprise the redirect URL registered to the Developer Network website.
* `scope`

  Specify the privilege required for the access token.

  Specify `psn:s2s.authorizedApp` when using a Client ID of the Authorized App Server product type.

  Specify `psn:s2s` when using a Client ID issued before the implementation of the Authorized App Server product type. However, the use of a newly issued Client ID of the Authorized App Server product type is recommended instead of an earlier Client ID.

  Additionally, if basic information about the user is required, refer to the [Auth Web API Overview](../Auth_WebAPI-Overview/__document_toc.html) document, and specify an `openid` and an additional ID token scope. (Separate with blank spaces if specifying multiple scopes.) The ID token can be obtained along with the access token.

Example of Obtaining an ID Token

```
psn:s2s.authorizedApp openid id_token:psn.basic_claims
```

## Option Parameters

* `request_locale`

  The language used on the sign-in page can be specified. The language codes that PlayStation™Network supports are based on BCP47 (<https://tools.ietf.org/html/bcp47>); on PlayStation™Network, any one of the codes in the table below can be specified.

  Behavior if a code not found in the following table is specified is undefined (a language assumed to be appropriate will be picked, but there is no guarantee that it will actually be).

  If the `request_locale` parameter is not specified or if one of the above combinations is not specified, the sign-in page is set in accordance with the language setting of the browser.

| **Language** | **Language Code** |
| --- | --- |
| Arabic | ar-AE |
| Czech | cs-CZ |
| Danish | da-DK |
| German | de-DE |
| Greek | el-GR |
| English (United Kingdom) | en-GB |
| English (United States) | en-US |
| Spanish (Latin America) | es-419 |
| Spanish (Spain) | es-ES |
| Finnish | fi-FI |
| French (Canada) | fr-CA |
| French (France) | fr-FR |
| Hungarian | hu-HU |
| Indonesian | id-ID |
| Italian | it-IT |
| Japanese | ja-JP |
| Korean | ko-KR |
| Dutch | nl-NL |
| Norwegian | no-NO |
| Polish | pl-PL |
| Portuguese (Brazil) | pt-BR |
| Portuguese (Portugal) | pt-PT |
| Romanian | ro-RO |
| Russian | ru-RU |
| Swedish | sv-SE |
| Thai | th-TH |
| Turkish | tr-TR |
| Vietnamese | vi-VN |
| Chinese (Simplified) | zh-Hans |
| Chinese (Traditional) | zh-Hant |

* `access_type`

  Specify the access type. Specify `access_type=offline` when using a Client ID of the Authorized App Server product type for offline access.
* `state`

  Specify an arbitrary value.

  The value specified for `state` will be returned when redirecting the user back. Compare and verify the specified value against the returned value and use the result for Cross-Site Request Forgery (CSRF) protection on the page to which the user is redirected back.

  Refer to RFC6749 (<http://tools.ietf.org/html/rfc6749>) for information about CSRF protection.

## Example

```
<a href = "https://ca.account.sony.com/api/authz/v3/oauth/authorize?service_entity=urn%3Aservice-entity%3Apsn&response_type=code&client_id=2dcb1c90-29ed-11e2-81c1-0800200c9a66&redirect_uri=https%3%2F%2FAexample.com%2F after_signin%2F &scope=psn%3As2s%20id_token%3Alegal_country%20id_token%3Alocale%20id_token%3Aonline_id&request_locale=ja-JP">to members area</a>
```

# Redirecting Back from the Sign-in Page

Evaluate sign-in success and obtain authorization code

## Description

When sign-in is successful or when the user selects to cancel on the sign-in screen, the user is redirected to the URL specified in `redirect_uri`.

The authorization code is passed as the query parameter when sign-in is successful; an error code is passed as the query parameter when an error occurs or when the user cancels sign-in.

## URL

## When Sign-in Is Successful

```
<URL specified in redirect_uri>?code=authcode
```

## When the User Cancels

```
<URL specified in redirect_uri>?error=XXX&error_description=YYY&error_code=ZZZ
```

## Parameters

## When Sign-in Is Successful

* `code`

  The authorization code issued by the authentication features for websites. The authorization code is a string such as "qzzm2W".

## When the User Cancels

* `error`

  Character string to identify the error. ASCII string with a maximum of 64 characters. Use it for determining errors. Refer to [Auth Web API Overview - Appendix - HTTP Status and Error Codes](../Auth_WebAPI-Overview/http-status-and-error-codes.html) for the definition of each error.

```
Example: error=login_required
```

* `error_description`

  Comment describing the error. Use this for debugging, and so forth.

```
Example: error_description=User+is+not+authenticated
```

* `error_code`

  Error code. It may be useful for troubleshooting; however, don't use it for error handling.

```
Example: error_code=4165
```

## Option

* `state`

  When the user is redirected to the sign-in page, the value specified in `state` will be returned if it has been specified.

## Notes

To call a PlayStation™Network Web API, the authorization code must be sent to the authentication server to obtain an access token. For details on how to obtain the access token, refer to the [Auth Web API Overview](../Auth_WebAPI-Overview/__document_toc.html) document.