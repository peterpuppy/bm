# Auth Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/processing-flow-for-providing-access-privileges.html

# Providing Access Privileges to an Application Server

This chapter details how the Auth Web API provides access privileges to application servers.

# Processing Flow for Providing Access Privileges

This topic provides information on how the Auth Web API provides access privileges to
an application server.

An overview of PlayStation™Network providing access privileges to an application server
is shown in the figure below.

Example of Providing Access Privileges to an Application Server

The figure below illustrates the processing flow for providing access privileges to an
application server.

Example of the Processing Flow for Providing Access Privileges

## Application

Applications on PlayStation®5/PlayStation®4/PlayStation®Vita/PlayStation®3 use the
SDK library to obtain an authorization code from the PlayStation™Network. This
authorization code is then exchanged for an access token and an ID token. The access
token is used to access PlayStation™Network Web APIs. The authorization code is a
single use artifact with a limited time to live (TTL). Although the TTL of the
authorization code has been configured to allow for some delay or latency in use, it
is recommended that they are exchanged immediately.

## SDK Library

The NpAuth library is provided for
PlayStation®5/PlayStation®4/PlayStation®Vita/PlayStation®3 applications to obtain an
authorization code from the PlayStation™Network servers. An application must provide
the following information regarding the application server when obtaining the
authorization code:

* User identifier of the access target user ([User ID](https://ps4.siedev.net/resources/documents/SDK/7.000/UserService-Reference/0011.html) for
  PlayStation®5/PlayStation®4 or Online ID for PlayStation®Vita/PlayStation®3).
  Note that the user ID used in this library is not the same as the account ID
  used in PlayStation™Network Web APIs.
* Client ID of the application server. Specify the value issued by the Developer
  Network website.
* Scope of application server usage.

## Application Server

The application server (client program) obtains an access token using the
authorization code from the SDK library. In addition to the authorization code, the
following information is required to obtain an access token:

* Client ID and the corresponding Client Secret. Specify respective values issued
  by the Developer Network website for each.
* Redirect URL. Specify the value issued by the Developer Network website. For details, refer to the [PlayStation™Network Service Setup Guide](../../../SDK/latest/PSN_Service_Setup-Guide/__document_toc.html).

After obtaining an access token, it can be used to access user information from the
PlayStation™Network. For usable Web APIs, refer to the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

## PlayStation™Network Server

The PlayStation™Network server refers to the OAuth2.0 based
Authentication/Authorization server that manages authentication codes and access
tokens as well as resource servers that manage user information.

# Game Refresh Tokens

This topic provides information on how and when to use game refresh tokens.

When a user starts or resumes an online game, the game application obtains an authorization code to allow its game server to access PlayStation™Network APIs. The application passes the authorization code to its game server and the game server exchanges the authorization code for an access token, an ID token and optionally a game refresh token. The refresh token allows the game server to have continued access to PlayStation™Network APIs without obtaining a new authorization code from the game application.

A game refresh token must be used only when the user is still playing the game. At the end of the game, the game server must revoke the refresh token.

For security reasons, a refresh token may be revoked before its expiration. The game server must handle this by obtaining a new pair of access and refresh tokens.

To use refresh tokens for gameplay, the client must be configured accordingly on DevNet.

# Authentication on Websites

This topic provides information for authenticating PlayStation™Network API calls through websites.

Websites provide services using general web browsers and not applications on PlayStation®5/PlayStation®4/PlayStation®Vita/PlayStation®3. A typical website can obtain an authorization code from the PlayStation™Network authorization server. The website must then transfer that authorization code to its backend server, so that the backend server can exchange it for an access token in calling other PlayStation™Network Web APIs. However, the obtained access token cannot be passed to the web browser (or any other client). Make sure that PlayStation™Network Web APIs are always called from a backend server.

For processing flow and other details, see [Authentication Features for Websites Overview](../Auth_for_Websites-Overview/__document_toc.html) and [Authentication Features for Websites Reference](../Auth_for_Websites-Reference/__document_toc.html).