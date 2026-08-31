# Auth Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_WebAPI-Overview/api-overview.html

# Auth Web API Overview

This topic provides an overview of the Auth Web API.

The Auth Web API is an OAuth 2.0 framework implementation that licensee application servers, websites, and back office servers utilize to access user information (such as friends lists or trophies) managed on PlayStation™Network servers. The API provides access tokens for accessing PlayStation™Network Web APIs and ID tokens for user authentication.

Note:

"Application servers" typically refer to proprietary licensee servers, such as game servers, that communicate with applications on PlayStation®5/PlayStation®4/PlayStation®Vita/PlayStation®3. "Websites" typically refer to licensee servers for users such as, fan-site servers, which do not function as application servers used for gameplay. "Back office servers" typically refer to licensee servers for application development support and operational support.

In this document where a distinction is not required, applications on PlayStation®5/PlayStation®4/PlayStation®Vita/PlayStation®3 are collectively referred to as "applications" and the libraries used by such applications to access PlayStation™Network servers are referred to as "SDK libraries". The developer network website for PlayStation®5/PlayStation®4/PlayStation®Vita/PlayStation®3 are collectively referred to as the "Developer Network website", or [DevNet](https://siedev.net/).

# Main Features

This topic highlights the main features of the Auth Web API.

The main features provided by the Auth Web API are:

* Issuing access tokens for accessing PlayStation™Network Web APIs.
* Issuing ID tokens for user authentication. ID tokens provide user information, such as age, country/region of the account and account language.

# Reference Materials

This topic provides links to documents that are relevant when using the Auth Web API.

Refer to the following documents for OAuth2.0 specification standards on which Auth Web API is based.

* [RFC6749 The OAuth 2.0 Authorization Framework](http://tools.ietf.org/html/rfc6749)

* For information about bugs, points to note, restrictions, and announcements, see [Release Notes - Auth Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Auth_WebAPI-ReleaseNotes.html).