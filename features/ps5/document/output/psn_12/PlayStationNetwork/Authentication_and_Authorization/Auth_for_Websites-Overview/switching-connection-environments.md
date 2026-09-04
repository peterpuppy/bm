# Authentication Features for Websites Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_for_Websites-Overview/switching-connection-environments.html

# Using the Features

# Preparation

## Obtain the Client ID and Client Secret

To use the authentication features for websites, you must first create a website-specific Authorized App Server product on the PlayStation®5 Developer Network website (<https://game.develop.playstation.net/>) and obtain a Client ID and Client Secret.

Because the Client ID and Client Secret are used to authenticate the website itself, this information must be managed with care and without risk of undesired disclosure.

## Register the Redirection URL

In addition to the above request, the URL to forward the user to after the sign-in screen must be registered. Details are given in the "[Obtain the authorization code by redirecting the user back](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_bz4_zf1_ycc)" step of the "[Basic Procedure](basic-procedure.html)" section.

# Basic Procedure

The procedure by which a website performs user authentication with the authentication features for websites and uses a Web API is as follows.

1. [Link or redirect the user to the sign-in page](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_ilp_yf1_ycc)
2. [Perform authentication on the sign-in page](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_hn3_zf1_ycc)
3. [Obtain the authorization code by redirecting the user back](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_bz4_zf1_ycc)
4. [Obtain the access token](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_p1w_zf1_ycc)
5. [Use a Web API](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_f2d_1g1_ycc)

Each step is explained in order below.

Authentication Features for Websites Processing (1) to (3)

1. **Link or redirect the user to the sign-in page**

   To perform user authentication with the authentication features for websites, first forward the user to the following URL by a link or redirection.

   After Production

   ```
   https://ca.account.sony.com/api/authz/v3/oauth/authorize
   ?service_entity=urn%3Aservice-entity%3Apsn
   &response_type=code
   &client_id=XXXXX
   &redirect_uri=YYYYY
   &scope=ZZZZZ
   ```

   During Development

   ```
   https://ca.sp-int.account.sony.com/api/authz/v3/oauth/authorize
   ?service_entity=urn%3Aservice-entity%3Apsn
   &response_type=code
   &client_id=XXXXX
   &redirect_uri=YYYYY
   &scope=ZZZZZ
   ```

   Be sure to apply the percent-encoding mechanism defined in RFC 3986 (<https://tools.ietf.org/html/rfc3986>) to each parameter.
2. **Perform authentication on the sign-in page**

   The PlayStation™Network sign-in screen will be displayed. Authentication will be carried out by the server of PlayStation™Network when the user follows the instructions on the sign-in screen and performs sign-in operation. If the user's permission is required to use the user's data, the user will also be prompted to give permission on the sign-in screen.

   Processing advances to the next step when the authentication is successful or when the user explicitly cancels the authentication process. All other authentication errors will be handled within the sign-in screen.
3. **Obtain the authorization code by redirecting the user back**

   When the authentication is successful, the user is redirected back to the URL specified in the `redirect_uri` parameter. The authorization code will be passed to the `code` parameter at this time. The authorization code will be a string such as qyp5EA.

   When the user cancels sign-in, the user will be redirected back to the URL specified in the `redirect_uri` parameter in the same manner as above; however, the `code` parameter will not be added. In other words, the existence or lack of the `code` parameter can be used to determine whether the user was authenticated or processing was canceled.

   Example: Redirection Destination When User is Authenticated

   ```
   https://example.com/after_signin/?code=qyp5EA
   ```

   Example: Redirection Destination When User Canceled

   ```
   https://example.com/after_signin/
   ```

   Authentication Features for Websites Processing (4) and (5)
4. **Obtain the access token**

   When authentication is successful and the user is redirected back, the passed authorization code can be transmitted by an appropriate protocol to the authorization server of PlayStation™Network to obtain that user's access token.

   In more specific terms, use the POST method to send a request to the following URL. The access token will be obtained upon normal termination of the method. The access token will be a string such as `84f325ad-010d-48bc-a948-10b2e1ee0d3d`.

   After Production

   ```
   https://s2s.np.playstation.net/api/authz/v3/oauth/token
   ```

   In Development

   ```
   https://s2s.sp-int.playstation.net/api/authz/v3/oauth/token
   ```

   Request Header

   * `Authorization`

     When the access token is obtained, basic HTTP authentication (basic authentication: RFC 2617) will be performed. Send the Client ID and the Client Secret to the server as the ID and password, respectively.
   * `Content-type`

     Specify `application/x-www-form-urlencoded` for `Content-type`.

   Request Body

   * `grant_type`

     Specify `authorization_code`.
   * `code`

     Specify the authorization code.
   * `redirect_uri`

     Specify the redirection destination URL specified when the authorization code was obtained. Redirection will not occur merely by using any redirect request for confirmation purposes. The specified `redirect_uri` must be an exact match for the `redirect_uri` specified when the authentication code was obtained.

   Example

   ```
   Request Header
   Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=
   Content-type: application/x-www-form-urlencoded

   Request Body
   grant_type=authorization_code&code=xxxxx&redirect_uri= https%3A%2F%2Ffoo.bar%2Fredirect
   ```

   For the details of the parameters to specify when obtaining an access token and the information that is returned, refer to "`getAccessTokenWithAuthorizationCode`" in the [Auth Web API Reference](../Auth_WebAPI-Reference/__document_toc.html) document.

   ID Token

   An ID token can be obtained from the response received upon obtaining the access token by specifying `openid` and an additional ID token scope as the `scope` parameters when obtaining the authentication code.

   This ID token contains user data authorized by the authentication server and is defined in OpenID Connect Core 1.0 (<https://openid.net/specs/openid-connect-core-1_0.html>), which was created as an extension to OAuth 2.0; the data is expressed in the form of a JSON Web Token (JWT) (<https://tools.ietf.org/html/rfc7519>). Basic information about the user, such as their account ID, can be obtained from JSON data extracted from the ID token using the JWT library or by employing another method.

   For details about the information that PlayStation™Network can provide with ID tokens and for the `scope` to specify, refer to the [Auth Web API Overview](../Auth_WebAPI-Overview/__document_toc.html) document.
5. **Use a Web API**

   After the access token is obtained successfully, it can be used to call a Web API to obtain various types of information. For actual use of Web APIs, refer to each applicable Web API document.

## Sign-out Procedure

To provide a sign-out feature in websites, call the following URL with a link/redirect to the sign-out page.

After Production

```
https://ca.account.sony.com/api/authn/v3/signOut
?client_id=xxxxx&redirect_uri=yyyyy
```

In Development

```
https://ca.sp-int.account.sony.com/api/authn/v3/signOut
?client_id=xxxxx&redirect_uri=yyyyy
```

The `redirect_uri` parameter conditions are the same as those for sign-in. Refer to ["Link or redirect the user to the sign-in page"](basic-procedure.html#authentication-features-for-websites-overview_1_2__li_ilp_yf1_ycc).

Example

```
<a href = "https://ca.account.sony.com/api/authn/v3/signOut?client_id=ae298edf-12c6-4d1c-ab3c-1230984842eab&redirect_uri=https%3A%2F%2Fexample.com%2Fafter_signout">Sign-out</a>
```

When sign-out processing is complete, a redirect back to the URL specified in `redirect_uri` will occur for the user.

# Switching Connection Environments

## When Obtaining the Authorization Code with the Authentication Features for Websites

The Issuer ID will not be returned from servers of PlayStation™Network with the authentication features for websites.

Switch the specified redirection destination for the authentication features for websites between the development application environment and the production application environment as required.