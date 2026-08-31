# Auth Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/user-authentication-using-an-id-token.html

# User Authentication Using an ID Token

This chapter provides information on user authentication using ID tokens.

# ID Tokens

This topic contains information on ID tokens and how to obtain them.

An [ID token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) is an OpenID Connect compliant security token that is used to authenticate a user. An ID token is a JWT token and it contains the following information:

* The authentication of an end-user (when an end-user is authenticated, on which device, and the account identifier of the end-user).
* Claims about the end-user (age, country/region, language preference, etc.).

All clients can obtain an ID token. You can get an ID token using the Auth Web API or the NpAuth library. For more information, see [Processing Flow for Providing Access Privileges](processing-flow-for-providing-access-privileges.html "This topic provides information on how the Auth Web API provides access privileges to an application server.") and [Authentication Using an ID Token From NpAuth Library](authentication-using-an-id-token-from-np-auth-library.html "This topic provides information on obtaining ID tokens using the NpAuth library.").

To obtain an ID token, clients must include "openid" in the scope request parameter when requesting an authorization code. This is either when calling the [sceNpAuthGetAuthorizationCodeV3](../../../SDK/latest/NpAuth-Reference/sce-np-auth-get-authorization-codev3.html) method of the NpAuth library or when redirecting to the authorization endpoint in Authentication for Websites. In addition to the "openid" scope, the client must also include "id\_token:psn.basic\_claims" in the scope request parameter to obtain the following information in the ID token:

* online\_id
* age
* device\_type

See [ID Token Claims](id-token-claims.html "This topic provides information on ID token claims.") for the list of claims in an ID token. An ID token may also contain other additional claims. Any claims that the client does not understand must be ignored.

To authenticate a user using an ID token, clients must validate the ID token issued according to the steps defined at [https://openid.net/specs/openid-connect-core-1\_0.html\_IDTokenValidation](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation). Additionally, clients must also validate the value of the `env_iss_id` claim to match current environment.

An ID token is always signed. Reject an ID token with `alg = none` in its header. The public key for validating the signature of an ID token can be obtained from the `GetJwks` Auth Web API.

# Authentication Using an ID Token From NpAuth Library

This topic provides information on obtaining ID tokens using the NpAuth library.

In addition to using the Auth Web API, a PlayStation®5/PlayStation®4 application may also obtain an ID token using the NpAuth library. In this case, the application must send the ID token to the application server and the application server must validate the token before using it to authenticate the user.

When using NpAuth library to obtain an ID token, the client ID to use is that of the application server. For details, refer to the [NpAuth Library Overview](../../../SDK/latest/NpAuth-Overview/__document_toc.html).

Example of User Authentication on an Application Server Using an ID Token

The validation of an ID token only requires the public key that is obtained from Auth Web API and cached in the application server. Different from using an authorization code, user authentication can be carried out without the application server making a call to the Auth Web API.

On the other hand, it is not possible for the application server to access the PlayStation™Network APIs with an ID token.

An ID token should only be used to authenticate a user on the application server-side or to obtain limited user information included in the ID token.

Note:

PlayStation™Network ID tokens contain personally identifiable information and are not encrypted. Always send tokens over secure communication/transport and store them in secured storage.