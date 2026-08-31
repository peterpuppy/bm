# NpAuth Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Overview/support-for-np-environment-switching.html

# Providing Access Privilege to the Application Server

This topic explains the mechanism that grants privileges to access user information managed by PlayStation™Network. The granting of access privileges to an Authorized App uses almost the same mechanism.

# Overview of Providing Access Privileges

To provide access privileges to the application server, PlayStation™Network supports OAuth 2.0.

With OAuth 2.0, unique services coordinated with PlayStation™Network can be provided so that the application server set up by the game developer can access user information on the server of PlayStation™Network.

An overview of PlayStation™Network providing access privileges to an application server is provided below.

Providing Access Privilege to the Application Server

Note: A simple use case is presented here to illustrate the processing flow. However it would also be possible, for example, for a single user to use multiple authorization codes on multiple consoles simultaneously. Refer to [Auth Web API Overview - Appendix - OAuth Grant Types, Scopes, and Life Cycles](../../../WebAPI/latest/Auth_WebAPI-Overview/oauth-grant-types-and-scopes.html).

# Processing Flow for Providing Access Privilege

The processing flow for providing access privilege to the application server is as follows.

Note: To provide access privileges to an Authorized App, rather than an application server, follow the processing flow described here and use `sceNpAuthGetAuthorizedAppCode()` instead of `sceNpAuthGetAuthorizationCodeV3()`. An applications on PlayStation®4 can use `sceNpAuthGetAuthorizedAppCode()` provided by the NpAuth library for PlayStation®5 via the PlayStation®4 Cross-Generation SDK.

Processing Flow for Providing Access Privilege

## Application on PlayStation®5

An application on PlayStation®5 uses the NpAuth library to obtain an authorization code from the PlayStation™Network servers. The authorization code is provisional data with a short validity period; transfer it to the application server immediately.

## NpAuth Library

The NpAuth library carries out communication for obtaining the authorization code from the server of PlayStation™Network. An application should set the following information regarding the application server to obtain the authorization code.

* Online ID of the access-target user
* Client ID of the application server. Specify the value issued by the PlayStation®5 Developer Network.
* Scope of user information to access

## Application Server

The application server (client program) obtains an access token from the authorization code using an Auth Web API. In addition to the authorization code, the following information is required to obtain an access token.

* Client ID and the corresponding client secret. Specify respective values issued by the PlayStation®5 Developer Network for each
* Redirect URL. Specify the value issued by the PlayStation®5 Developer Network.

After obtaining the access token, use the Web API to access user information.

## Server of PlayStation™Network

The PlayStation™Network servers provide features (issuing authorization codes and issuing access tokens) equivalent to the Authorization server and a feature (managing user information) equivalent to the Resource server of OAuth 2.0.

# Support for NP Environment Switching

Applications that use the PlayStation™Network services are required to support the three NP environments: the development environment (sp-int), the certification environment (prod-qa), and the production environment (np). The accounts for each NP environment cannot be used interchangeably, therefore it is important to manage separate accounts for each environment.

Since environment switching is designed to be performed just by changing [NP Environment] in [★Debug Settings] in the system software, normally there is no need to change the program code in applications on PlayStation®5. However, program code in application servers is required to support environment switching.

In order for application servers to identify environments, use the issuer ID returned when obtaining the authorization code with `sceNpAuthGetAuthorizationCodeV3()`. The issuer ID will be a fixed value that returns according to the environment as follows.

Issuer IDs for Each Environment

| **NP Environment** | **Issuer ID** |
| --- | --- |
| np | 256 (0x100) |
| prod-qa | 8 (0x8) |
| sp-int | 1 (0x1) |

Application servers are required to use the issuer ID returned with authorization codes to identify NP environments and appropriately switch NP environments when calling Web API requests.

Refer to each Web API reference for details on the URLs of Web APIs.

Various implementations are possible for application servers that perform environment switching, but having independent server environments for each environment is recommended. One such method is for the game client to send an authorization code and issuer ID to an end point on the application server, and then the application server redirects clients to independent server environments corresponding to respective PlayStation™Network environments based on the issuer ID. With this method, it will be possible for developers to change the independent server environments to be used by just changing the redirect logic. When not using this method, it is also possible to use a method where game clients select independent server environments based on the issuer ID.

## Notes on Using the Certification Environment

Notes for supporting the certification environment in independent application servers are as follows.

**Registering Certification Environment IP Addresses**

For security purposes, the certification environment (prod-qa) server has access restrictions using IP address whitelists. In order to use the certification environment for testing environment switching support in independent application servers, make a request for an IP address range for clients and independent application servers. For details, refer to "IP Allowlisting For PlayStation™Network Services" in PlayStation™Partners Help Center (<https://learn.playstation.net/csh?context=psp_IPallowlisting_gs>).

**Creating Accounts for the Certification Environment**

It is not possible to use development environment accounts in the certification environment. Create new accounts for the certification environment. On PlayStation®5, switch the environment name in [Settings]->[Debug Settings]->[PlayStation Network]->[NP Environment] in the system software to "prod-qa", and then create a new local user and perform sign-up.

**Purpose of the Certification Environment**

The certification environment is normally used by SIE to carry out the certification process. Independent application servers must support the certification environment, but development and testing are in principle performed in the development environment. Use of the certification environment should be limited to performing simple operation checks such as authorization checks for application servers and environment switching processing checks. In particular, in order to prevent negative effects on the work done by SIE, make sure that the certification environment is not accessed after master submission.