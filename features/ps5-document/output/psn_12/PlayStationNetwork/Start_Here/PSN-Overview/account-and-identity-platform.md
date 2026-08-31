# PlayStation™Network Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN-Overview/account-and-identity-platform.html

# Account and Identity Platform

The Account and Identity Platform encompasses authentication and authorization, data privacy, account security, and account management on the PlayStation™Network.

It can be used to implement secure entry points for PlayStation® customers to purchase and
access games and services, play games online, and socialize online with other gamers.

The Account Platform also enables partners to access authorized platform and user account data to develop enhanced experiences within games and applications both on and off-console.

# SignIn and Auth

SignIn and Auth provide functionality that allows applications, websites and application servers to identify users and access account information.

The PlayStation™Network offers the following Web API and libraries:

## SigninDialog Library

The SigninDialog library is used by applications to provide a sign-in screen that allows users to sign in to the PlayStation™Network. For details, refer to the following documents:

* [SigninDialog Library Overview](../SigninDialog-Overview/__document_toc.html)
* [SigninDialog Library Reference](../SigninDialog-Reference/__document_toc.html)

## Auth Web API

The Auth Web API is used by licensee application servers, websites, and back office websites to access user information that is held on PlayStation™Network servers. It is an OAuth 2.0 framework implementation provides and verifies access tokens, and can also provide ID tokens that contain basic user and authentication information. For details, refer to the following documents:

* [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html)
* [Auth Web API Reference](../../../WebAPI/latest/Auth_WebAPI-Reference/__document_toc.html)

## NpAuth Library

The NpAuth library provides a C/C++ native interface to the Auth Web API. It is used for authenticating an account on a specialized server, and for supporting server-to-server use of the Web APIs. For details, refer to the following documents:

* [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html)
* [NpAuth Library Reference](../NpAuth-Reference/__document_toc.html)

## Authentication of Websites

This feature allows websites that target general browsers to use accounts for PlayStation™Network for user authentication. "General browsers" refers to off-console browsers such as PC and smartphone browsers. For details, refer to the following documents:

* [Authentication Features for Websites Overview](../../../WebAPI/latest/Auth_for_Websites-Overview/__document_toc.html)
* [Authentication Features for Websites Reference](../../../WebAPI/latest/Auth_for_Websites-Reference/__document_toc.html)

# Identity and Account Management

This topic links to resources for learning more about the Account Closure Web
API.

## Account Closure Web API

Account Closure allows customers who no longer want to have a relationship with the PlayStation™Network to close their account. The Account Closure Web API allows partners to retrieve information about account closures so they can comply with legal and development issues. For details, refer to the following documents:

* [Account Closure Overview](../../../WebAPI/latest/Account_Closure-Overview/__document_toc.html)
* [Account Closure Web API Reference](../../../WebAPI/latest/Account_Closure_WebAPI-Reference/__document_toc.html)