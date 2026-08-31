# Authentication Features for Websites Reference – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_for_Websites-Reference/redirecting-to-sign-out.html

# Sign-out Protocols

# Redirecting to Sign-out

Start of sign-out

## Description

To sign a user out from PlayStation™Network, direct the user to the following URL with a link or redirect. After sign-out processing has been performed, redirect to the URI specified in `redirect_uri`.

## URL

## Production Environment for End Users

```
https://ca.account.sony.com/api/authn/v3/signOut?
client_id=xxxxx&redirect_uri=yyyyy
```

## Development Environment for Developers

```
https://ca.sp-int.account.sony.com/api/authn/v3/signOut?
client_id=xxxxx&redirect_uri=yyyyy
```

## Parameters

## Required Parameters

* `client_id`

  Specify the Client ID issued from the Developer Network website (<https://game.develop.playstation.net/>). A Client ID is an ID for identifying the authorization-target application or website with the PlayStation™Network Web APIs.
* `redirect_uri`

  Specify the URL of the page for the user to be redirected back to after sign-out.

  The scheme must be https. Moreover, the beginning of this URL must comprise the redirect URL registered to the Developer Network website.

## Response

If an invalid `client_id` or `redirect_uri` is specified, a response such as the following is returned without a redirect occurring.

```
{
    "error":"invalid_client",
    "error_description":"Invalid client",
    "error_code":4173,
    "docs":"http://docs.auth.api.ac.playstation.net/2.0/signout"
}
```

Each member of an error response has the following information:

* `error`

  Character string to identify the error. ASCII string with a maximum of 64 characters. Use it for determining errors. Refer to [Auth Web API Overview - Appendix - HTTP Status and Error Codes](../Auth_WebAPI-Overview/http-status-and-error-codes.html) for the definition of each error.
* `error_description`

  Comment describing the error. Use this for debugging, and so forth.
* `error_code`

  Error code. It may be useful for troubleshooting; however, don't use it for error handling.

The following errors can occur:

* `error: invalid_client`

  ```
  error: invalid_client
  error_description: Invalid client
  error_code: 4161
  ```

  + Cause/solution: Check the `client_id` with specified parameters.
* `error: redirect_uri_mismatch`

  ```
  error: redirect_uri_mismatch
  error_description: Redirect URI mismatch
  error_code: 4174
  ```

  + Cause/solution: Check the `redirect_uri` with specified parameters.

## Example

```
<a href = "https://ca.account.sony.com/api/authn/v3/signOut?client_id=2dcb1c90-29ed-11e2-81c1-0800200c9a66&redirect_uri=https%3%2F%2FAexample.com%2Fafter_signout">Sign-out</a>
```

# Redirecting Back from Sign-out

Sign-out success

## Description

After sign-out processing is performed, users are redirected back to the URL specified in `redirect_uri`. An error will not occur.

## URL

## When Sign-out Is Successful

```
<URL specified in redirect_uri>
```