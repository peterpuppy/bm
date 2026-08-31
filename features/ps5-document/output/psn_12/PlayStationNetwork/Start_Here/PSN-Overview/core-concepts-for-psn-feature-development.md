# PlayStation™Network Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN-Overview/core-concepts-for-psn-feature-development.html

# Beginning Development

Before you begin development, [complete the required prerequisites](before-you-start.html "This topic covers prerequisites you'll need before developing PlayStation™Network features.") and familiarize yourself with
[core concepts unique to PlayStation™Network development](core-concepts-for-psn-feature-development.html "This topic provides an overview of concepts unique to PlayStation™Network development.").

# Before You Start

This topic covers prerequisites you'll need before developing PlayStation™Network
features.

Before you start development of PlayStation™Network features, you need the following resources:

## PlayStation®5 Development Kit, Connected to the Internet

To use the PlayStation™Network, the PlayStation®5 Development Kit must be connected to a network that can connect to the internet directly, without using a proxy.

To connect the PlayStation®5 Development Kit to the internet, the network settings must be set in advance.

**IP Address**

There is no need for the PlayStation®5 Development Kit to directly hold a global IP address. The internet can be accessed via a commercially-available NAT router. It is also possible to have multiple PlayStation®5 Development Kits connected to one NAT router.

Some PlayStation™Partners apps and services only allow access to allowlisted IP addresses. For more information, see [IP Allowlisting for PlayStation™Network Services](https://learn.playstation.net/csh?context=psp_IPallowlisting_gs).

Note: Depending on the combination of the router and NAT characteristics of the communication target, there may be problems in peer-to-peer (P2P) communication.

**Used Port Numbers**

When you use the PlayStation™Network functions, PlayStation™Network servers in the development environment are accessed from the PlayStation®5 Development Kit or Testing Kit.

The port numbers used to access PlayStation™Network servers in the development environment are:

```
TCP 80, 443, 3478, 3479, 3480, 5223
UDP 3478, 3479
```

These IP addresses and port numbers are subject to change. SIE will notify you of such changes.

Note: If the IP addresses and port numbers of the server used by the PlayStation™Network are blocked, for example by a firewall filter, correct operation is not possible.

Also, P2P communication in an online session using an arbitrary UDP port is used per session or per communication party. Problems in P2P communication may occur if some ports are unavailable due to firewall settings.

## Registered Product with Configured Services

To develop a product supporting the PlayStation™Network, register the title and product information to the PlayStation®5 Developer Network and set the services used. The term product here includes the following:

* Application on the console (PlayStation®5)
* Application on the console (PlayStation®4 Cross-Gen)
* Application Server
* Back Office Server

Regarding product registration, services that can be used for each product type, and how to request for services, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

## An Account for PlayStation™Network in the Development Environment

To develop an application that uses PlayStation™Network, you must have an account in the PlayStation™Network development environment. Accounts can only be used on one PlayStation®5 Development Kit accessing the PlayStation™Network at any one time. Accounts are not specific to the platform on which they were created, so the same account can be used to develop applications for PlayStation®5, PlayStation®4, PlayStation®3, and PlayStation®Vita. Accounts are specific to each NP environment, so you must create an account in the development environment even if you already have one in the production environment.

See [Creating an Account for Development](creating-an-account-for-development.html "This topic covers how to create an account for PlayStation™Network application development.") for detailed instructions.

# Core Concepts for PlayStation™Network Feature Development

This topic provides an overview of concepts unique to PlayStation™Network
development.

## Web APIs

The PlayStation™Network Web APIs are REST APIs that are used by PlayStation®5 and PlayStation®4 applications, and the application servers and websites that work with these applications. For details, refer to the following document:

* [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html)

## NpCppWebApi Library

The NpCppWebApi library is used by applications to access the Web APIs. It provides a native C/C++ wrapper for each function in the PlayStation™Network Web APIs. For details, refer to the following documents:

* [NpCppWebApi Library Overview](../NpCppWebApi-Overview/__document_toc.html)
* [NpCppWebApi Library Reference](../NpCppWebApi-Reference/__document_toc.html)

## NpWebApi2 Library

The NpWebApi2 library is used by applications to access the Web APIs. It provides a generic, C/C++ native interface to the PlayStation™Network Web APIs from the console. Unlike the NpCppWebApi, which provides wrapper functions for Web API endpoints, NpWebApi2 provides a generic way to interface with an arbitrary Web API.

It also provides interfaces for receiving push events and order-guaranteed push events. For details, refer to the following documents:

* [NpWebApi2 Library Overview](../NpWebApi2-Overview/__document_toc.html)
* [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html)

## Np Library

The NP library is the base library for applications using the PlayStation™Network. It provides functions for retrieving the account for PlayStation™Network ID for users signed into the console. In addition to functionalities related to user accounts, the Np library provides functionalities required for using other libraries related to PlayStation™Network. For details, refer to the following documents:

* [Np Library Overview](../Np-Overview/__document_toc.html)
* [Np Library Reference](../Np-Reference/__document_toc.html)