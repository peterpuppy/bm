# NpAuth Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuth-Overview/resources-used.html

# Basic Information about the NpAuth Library

This topic provides basic information you should know when using the NpAuth library, including the purpose and characteristics of the library, its main features, how to embed it into application programs, and sample programs provided by SIE.

# Purpose and Characteristics of the NpAuth Library

The NpAuth library provides a feature to obtain the authorization code required by the application server and Authorized Apps to access user information on the PlayStation™Network servers, and it provides a feature for obtaining an ID token.

The application server refers to a server set up by the licensee; a game server is a typical application server. Access privilege can be given to such an application server following the framework of OAuth 2.0 when it needs to access user information managed on PlayStation™Network, for example, to obtain a user's friend list or trophy collection. PlayStation®5 applications can use the NpAuth library to obtain the authorization code required to give access privileges to the application server. Transfer the obtained authorization code to the application server so that it can obtain an access token from the PlayStation™Network servers and access user information.

ID tokens can be used by applications servers to verify users. When the NpAuth library is used to obtain an ID token and then it is transferred to an application server, the application server will verify the token in order to verify the user.

Note:

In order to use Authorized App-related features, make an inquiry via the "Post new issue" page of Private Support (<https://game.develop.playstation.net/support/>). In addition, refer to the explanation for end users provided in "How to manage authorized apps" (<https://www.playstation.com/support/account/manage-authorized-apps/>) as necessary.

# Main Features of the NpAuth Library

The main feature provided by the NpAuth library is as follows.

* Feature for obtaining an authorization code from the server of PlayStation™Network
* Feature for obtaining an ID token from the server of PlayStation™Network
* Feature for obtaining an Authorized App authorization code from the PlayStation™Network servers

# Resources Consumed by the NpAuth Library

The NpAuth library consumes one mutex during the time between loading and unloading the PRX. In addition, one thread will be generated upon asynchronous processing request execution. The generated thread name is `SceNpAuthAsyncXXXXXXXX` (`XXXXXXXX` is a hexadecimal request ID), the stack of the generated thread will be 32 KiB, and the application can specify the priority and CPU affinity mask.

# Embedding the NpAuth Library into a Program

Include np.h in the source program. In addition, before calling any NpAuth library API features in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if (sceSysmoduleLoadModule(SCE_SYSMODULE_NP_AUTH) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceNpAuth\_stub\_weak.a.

# Sample Programs for the NpAuth Library

Sample programs using the NpAuth library are as follows.

## sample\_code/playstation\_network/api\_np\_auth/console

This sample program demonstrates basic usage of the NpAuth library. There is a program that obtains an authorization code for the sample application server, and a program that obtains an ID token with the specified parameters.

## sample\_code/playstation\_network/api\_np\_auth\_authorized\_app

This sample program obtains authorization codes for an Authorized App using the NpAuth library and NpAuthAuthorizedAppDialog library.

# Reference Materials for Using the NpAuth Library

Refer to the following documents regarding the Np library, which is a common requirement when using any PlayStation™Network feature.

* [Np Library Overview](../Np-Overview/__document_toc.html)
* [Np Library Reference](../Np-Reference/__document_toc.html)

Refer to the following document regarding the NP S2S (server to server) service and an overview of the PlayStation™Network Web API ("Web API" hereafter) required for accessing the PlayStation™Network servers from the application server and from an Authorized App.

* [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html)

Refer to the following document regarding how to use a Web API request for obtaining an access token for the application server and Authorized App.

* [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html)

For details about the NpAuthAuthorizedAppDialog library that is necessary for Authorized Apps and for obtaining authorization codes for Authorized Apps, refer to the following documents.

* [NpAuthAuthorizedAppDialog Library Overview](../NpAuthAuthorizedAppDialog-Overview/__document_toc.html)
* [NpAuthAuthorizedAppDialog Library Reference](../NpAuthAuthorizedAppDialog-Reference/__document_toc.html)

Refer to the following document regarding OAuth 2.0.

* "RFC6749 The OAuth 2.0 Authorization Framework" <http://tools.ietf.org/html/rfc6749>

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpAuth Library](../ReleaseNotes/PlayStation_Network-NpAuth-ReleaseNotes.html)