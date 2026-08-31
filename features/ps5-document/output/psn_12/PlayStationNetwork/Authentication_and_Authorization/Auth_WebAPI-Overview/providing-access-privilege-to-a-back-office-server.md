# Auth Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/providing-access-privilege-to-a-back-office-server.html

# Providing Access Privilege to a Back Office Server

This chapter details how the Auth Web API provides access privileges to back office servers.

# Client Credential Access Token

This topic provides information on client credential access tokens and how to use them.

A client credential access token is an access token for S2S (Server to Server) usage by back office servers that can be obtained by client authentication alone, without user authentication. The client ID and client secret are required to obtain a client credential access token. Because of this, user interaction is not required for obtaining a client credential access token and it is not associated with any user context. See [Auth Web API Reference - Token Endpoint - getAccessTokenWithClientCredentials](../Auth_WebAPI-Reference/0004.html) for the API specification to obtain a new client credentials access token.

Back Office Server Authentication Using a Client Credential Access Token

## Using the Client Credential Access Token

Web APIs that can be accessed using the credential client access token are limited.
For usable Web APIs and the method for requesting usage, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).