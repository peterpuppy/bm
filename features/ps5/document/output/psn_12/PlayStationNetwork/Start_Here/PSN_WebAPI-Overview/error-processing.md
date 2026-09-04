# PlayStation™Network Web APIs Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_WebAPI-Overview/error-processing.html

# Usage

This topic provides general use cases for using PlayStation™Network Web
APIs.

This chapter explains general uses of PlayStation™Network Web APIs. Processing flow is as follows; however, there are detailed differences by platform, and there are sections that need not be considered on the application side because the library carries out the processing:

1. [Obtaining Access Tokens](obtaining-access-tokens.html "This topic provides information on how to obtain access tokens.").
2. [Constructing the Base URL](constructing-the-base-url.html "This topic provides information on how to construct base URLs for PlayStation™Network Web APIs.").
3. [Creating and Executing a Request](creating-and-executing-a-request.html "This topic provides information on how to create and execute a PlayStation™Network Web API request.").
4. [Handling the Response](handling-the-response.html "This topic provides information on how to handle PlayStation™Network Web API request responses.").
5. [Error Processing](error-processing.html "This topic provides information on how to handle PlayStation™Network Web API errors.").

# Preparation: Product Registration and Service Settings

This topic provides information on product registration and service
settings.

As preparation, the title and product information must be registered on the Developer Network website, and the services to be used must be requested.

For details on product registration, the services that can be used with each platform/product type, as well as request procedures, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

## Obtaining the Client ID

The Client ID is issued upon requesting the "Client ID" service. A Client Secret - to confirm ownership of the Client ID - is also issued.

Note: A Client Secret is secret information for guaranteeing that a developer is the owner of a Client ID. Take sufficient precautions to ensure that it is not leaked to third parties. For example, be sure to remove a Client Secret even when providing the source code/application package in order to receive support on the Developer Network website, etc.

## PlayStation®5 Applications

For PlayStation®5 applications, the NP Title ID serves as the Client ID. Thus, there is no need to obtain the Client ID.

## Application Server

The Client ID of an application server are sharable irrespective of the platform. For example, when setting a game server supporting both a PlayStation®5 and another platform application, it is sufficient to obtain a Client ID for only one of the platforms. However, because usable services vary depending on the platform, make sure to obtain the Client ID with the appropriate platform according to the services used by the game server.

## Back Office Servers

For back office servers, the server IP address is required upon a Client ID request. This is because Management Web APIs are only callable from an IP address registered in ACL.

Note: All ACL settings are sharable amongst Management Web APIs. If required, it is possible to use the ACL Management requests to change the settings.

## Application Servers (Client Credential)

Similar to back office servers, this application server type also requires an IP ACL to be registered in advance. However, in order to support servers dynamically allocated without a guaranteed static IP range, the IP ACL is only used during authentication to obtain an access token.

## IP Allowlisting Requirements

Some PlayStation™Partners apps and services only allow access to allowlisted IP addresses. For more information, see [IP Allowlisting for PlayStation™Network Services](https://learn.playstation.net/csh?context=psp_IPallowlisting_gs).

# Obtaining Access Tokens

This topic provides information on how to obtain access tokens.

Depending on the authorization grant, the following types of access tokens exist for PlayStation™Network:

* Access tokens obtained using authorization codes (refer to OAuth 2.0 (RFC 6749)).
* Client credential access tokens (refer to OAuth 2.0 (RFC 6749)).

However, the type of access token to use is determined for each product type, therefore awareness of the access token is not required as long as obtaining is performed using the following methods.

## PlayStation®5 Applications

For PlayStation®5 applications (including test applications), there is no need to explicitly obtain an access token. Obtaining an access token is automatically processed by calling a PlayStation™Network Web API using the NpWebApi2 library.

## Application Servers (for PlayStation®5 Applications)

For application servers supporting a PlayStation®5 application, the application must obtain an authorization code using the NpAuth library/NP Auth utility and send it to the application server. The Client ID assigned to the application server must be specified at this time to obtain the authorization code for the application server.

The application server can use the Auth Web API to obtain the access token (access token obtained using an authorization code) from the sent authorization code and Client ID/Client Secret.

## Websites

For websites, an access token (access token obtained using an authorization code) can be obtained using authentication features for websites. For details, refer to the [Authentication Features for Websites Overview](../../../WebAPI/latest/Auth_for_Websites-Overview/__document_toc.html) and the [Authentication Features for Websites Reference](../../../WebAPI/latest/Auth_for_Websites-Reference/__document_toc.html).

## Back Office Servers and Application Servers (Client Credential)

For back office servers and application servers (Client Credential), an access token (client credential access token) can be obtained using the Auth Web API. For details, refer to [Auth Web API Overview - Providing Access Privilege to a Back Office Server](../../../WebAPI/latest/Auth_WebAPI-Overview/providing-access-privilege-to-a-back-office-server.html).

**Handling Dynamically Allocated Servers without a Static IP**

For application servers (Client Credential), authentication can be made from a pre-determined IP address range. In instances where cloud services are used to host game servers that cannot guarantee a static IP range, SIE recommends having a central service or egress server with a static IP address range perform authentication with PlayStation™Network and obtain an access token. Once an access token is obtained, pass that access token to the dynamically allocated game server for further API usage.

# Constructing the Base URL

This topic provides information on how to construct base URLs for PlayStation™Network
Web APIs.

A base URL is defined for each API group in the PlayStation™Network Web APIs.

## PlayStation®5 Applications

For PlayStation®5 applications (including test applications), there is no need to explicitly construct base URLs. Obtaining an appropriate base URL is automatically processed by calling a PlayStation™Network Web API using the NpWebApi2 library.

## Application Servers or Back Office Servers

For application servers or back office servers, base URLs should be constructed like below. Calling the `GET BaseUrl` request is no longer needed in PlayStation®5 generation.

```
https://s2s.sp-int.playstation.net/api/${apiGroup} (development/sp-int)
https://s2s.prod-qa.playstation.net/api/${apiGroup} (Certification environment/prod-qa)
https://s2s.np.playstation.net/api/${apiGroup} (production/np)
```

# Creating and Executing a Request

This topic provides information on how to create and execute a PlayStation™Network Web
API request.

For PlayStation®5 applications (including test applications), APIs required for creating and executing a request is provided by the NpWebApi2 library. Follow the procedure below and pass appropriate parameters to the appropriate API arguments to create and execute a request.

For application servers/back office servers, follow the procedure below and create an HTTP
request header and body with the appropriate method and issue the request with the HTTPS
protocol.

## (1) Set the HTTP request header.

Set an appropriate `Content-Type` HTTP header for when using PlayStation™Network Web APIs that require a request body. For requests with `Content-Type` specification, use one that is specified. For requests without `Content-Type` specification, JSON (RFC 4627) is used, so set "`application/json`" as in the following.

```
Content-Type: application/json; charset=utf-8
```

In requests with multilingual support, specify the languages with the `Accept-Language` HTTP header. For details, refer to the "[Accept-Language HTTP Header and Supported Languages](creating-and-executing-a-request.html#psn-web-apis-overview_2_4__psn-web-apis-overview_2_4_7)" item.

For application servers/back office servers, always set an `Authorization` HTTP header that includes an access token as in the following.

```
Authorization: Bearer AccessToken
```

## (2) Set the HTTP method and URI.

Use the base URL obtained earlier to set the HTTP method and URI according to the request. HTTPS is used for the protocol. The URI must always be percent-encoded (URL-encoded) based on RFC 3986.

Assign a query string to the URI as required. The available query parameters vary depending on the request. The following are the query parameters common to the PlayStation™Network Web APIs.

**fields**

For instance, you might use this query parameter for a `GET` operation and it is possible to decrease or increase the number of object members to obtain. By using this parameter appropriately, the processing time and network load can be reduced. When specifying multiple members, join the member names with commas. For details, refer to the documentation for each Web API for specific specifications.

Note that values with the prefix `@` are special values that indicate specific members.

Note: Do not include spaces before or after commas when specifying multiple members.

**offset**

Used when obtaining lists. For details, refer to the "[Pagination](creating-and-executing-a-request.html#psn-web-apis-overview_2_4__psn-web-apis-overview_2_4_5)" item.

**limit**

Used when obtaining lists. For details, refer to the "[Pagination](creating-and-executing-a-request.html#psn-web-apis-overview_2_4__psn-web-apis-overview_2_4_5)" item.

**sort**

Used when obtaining lists. For details, refer to the "[Sorting](creating-and-executing-a-request.html#psn-web-apis-overview_2_4__psn-web-apis-overview_2_4_6)" item.

## (3) Set the body.

Set a body that matches the `Content-Type` specified in the HTTP header for requests that require a request body.

If `Content-Type` is `application/json`, set data written in JSON format with UTF-8 encoded character strings. Note that there is a common restriction that `null` cannot be specified for JSON member values.

Example of a forbidden object including the null value:

```
{
  "example": null
}
```

## (4) Execute the request.

Execute the request.

## Pagination

Some requests that obtain list-type resources such as a request for obtaining a friend list provide a mechanism for pagination. For instance, you might use the following query parameters. For details, refer to the documentation for each Web API for specific specifications.

|  |  |
| --- | --- |
| `offset` | Offset for a list to obtain. |
| `limit` | Maximum number of elements for a list to obtain with one request. |

Requests compatible with pagination return an object that includes the following members as the response:

|  |  |
| --- | --- |
| `nextOffset` | Start offset for the next page. |
| `previousOffset` | End offset for the previous page. |

When a number that is equal to or greater than total counts is specified for `offset`, an empty array is returned.

Example of pagination with offset and limit parameters:

```
GET /v1/users/123456789012345689/friends?offset=4&limit=2
{
  "friends":[
    "1111111111111111111",
    "2222222222222222222"
  ],
  "nextOffset": 6,
  "previousOffset": 3
}
```

## Sorting

Requests that obtain list-type resources such as a request for obtaining a friend list may be able to obtain a list sorted with specific conditions by specifying sort conditions or a sort order. For instance, you might use the following query parameters. For details, refer to the documentation for each Web API for specific specifications.

The `sort` query parameter is used for specifying the sort conditions.

Multiple parameters for sorting can be specified as a comma-separated list, using a "`-`" (minus) prefix to indicate that the sort order should be descending (default is ascending sort order).

## Accept-Language HTTP Header and Supported Languages

When a PlayStation™Network Web API request or response contains localized resources, the API defines the Accept-Language HTTP request header to determine 1) the supported languages by the application and 2) the language to be selected in the response for localized resources.

**PlayStation®5 Applications**

For PlayStation®5 applications (including test applications), language codes do not have to be explicitly specified. By using the NpWebApi2 library to call PlayStation™Network Web APIs, the language codes supported by the SDK is automatically set in the header.

**Application Servers and Websites**

For application servers, and websites, specify the language codes in the following format:

```
Accept-Language: List of language codes supported by the applications separated by commas, and with the language used in the UI for the current user placed first.
```

To determine the language to be selected in the response, only the highest prioritized language is treated as the language expected by the current user, if such language is not prepared by the resource the response will include the resource in the language prepared as default for each resource.

**Example:**

```
Accept-Language:ja-JP,en-US,fr-FR,es-ES,de-DE,it-IT,nl-NL,pt-PT,ru-RU,
ko-KR,zh-Hant,zh-Hans,fi-FI,sv-SE,da-DK,no-NO,pl-PL,pt-BR,en-GB,tr-TR,
es-419,ar-AE,fr-CA,cs-CZ,hu-HU,el-GR,ro-RO,th-TH,vi-VN,id-ID
```

With this example, ja-JP is considered as the UI language for the current user.

Note: Quality values (q=0.7, etc.) in the `Accept-Language` HTTP header is generally supported in the PlayStation™Network Web APIs, however, due to the language selection specification described above, use of quality values is not needed and not recommended.

**Back Office Servers**

For back office servers, specifying language codes is not required. All requests that can be called by back office servers return responses that are not dependent on a language.

# Handling the Response

This topic provides information on how to handle PlayStation™Network Web API request
responses.

The PlayStation™Network Web APIs return an HTTP status code and body as responses. However, when the HTTP status code is 204, a body is not be returned. In addition, a JSON object with UTF-8 encoded character strings is returned as the body when an error occurs, but if an unexpected error occurs (when the URI is wrong, a timeout occurs upon using a proxy, etc.), there are cases where a non-JSON type body is returned and cases where a body is not returned.

Note: Due to specification changes in the PlayStation™Network Web API, it is possible for new elements and members to be included in the data obtained from a PlayStation™Network Web API. Implement your application so that when an element or member not described in the documentation is returned, it is ignored.

## (1) Determine request success/failure using the HTTP status code.

It is possible to use the HTTP status code to determine if the request was successful or failed.

The possible HTTP status codes returned by the PlayStation™Network Web APIs are as
listed in the table below. However, when an unexpected error occurs, there are cases
where an HTTP status code other than the following is returned.

HTTP Status Codes

| **Value** | **Message** | **Description** |
| --- | --- | --- |
| 200 | `OK` | Success. |
| 201 | `Created` | Success (new resource was created). |
| 204 | `No Content` | Success (without response body). |
| 304 | `Not Modified` | Resource not modified. |
| 400 | `Bad Request` | Incorrect request. |
| 401 | `Unauthorized` | No authentication information, etc. |
| 403 | `Forbidden` | Request was refused. |
| 404 | `Not Found` | Specified resource does not exist, etc. |
| 405 | `Method Not Allowed` | An attempt was made to use an unsupported method. |
| 409 | `Conflict` | An attempt was made to add an already added resource, etc. |
| 413 | `Request Entity Too Large` | Request body size is too big. |
| 414 | `Request-URI Too Long` | URI is too long. |
| 415 | `Unsupported Media Type` | Unsupported `Content-Type` was specified. |
| 429 | `Too Many Requests` | Rate limit was exceeded. |
| 500 | `Internal Server Error` | Unexpected internal server error. |
| 501 | `Not Implemented` | An attempt was made to use an unsupported protocol, etc. |
| 503 | `Service Unavailable` | Under maintenance, service has ended, etc. |

When the HTTP status code is 2xx, the request was successful. When the HTTP status code is 4xx or 5xx, it indicates that an error has occurred and the request has failed. When the application uses `sceNpWebApi2SendRequest()` in the NpWebApi2 library the functions convert HTTP Status Codes into error codes described in the following [Error Processing](error-processing.html "This topic provides information on how to handle PlayStation™Network Web API errors.") section, so there is no need to explicitly check HTTP Status Codes within the application.

Note: There is a possibility that HTTP status codes returned by the PlayStation™Network Web APIs might be added in the future. When HTTP status codes not listed above are returned from PlayStation™Network Web APIs, make sure that they are processed as errors, the application does not hang, and user operation does not become impossible.

## (2) Determine the Content-Type and obtain the body.

If a response body exists, obtain the `Content-Type` HTTP header value and appropriately process the body. For example, if `Content-Type` is `application/json`, a JSON object with UTF-8 encoded character strings is returned as the body, so parse and use it.

# Error Processing

This topic provides information on how to handle PlayStation™Network Web API
errors.

When an error occurs, the PlayStation™Network Web APIs returns a JSON object with UTF-8 encoded character strings that indicates the error content as the response body. However, when an unexpected error occurs, there are cases where a response body is not returned and cases where a non-JSON type response body is returned.

## (1) Obtain the error code.

When an error occurs, a root object that includes the following `error` object is returned as the response body.

error object

```
"error":{
  "code"          :Number,
  "message"       :String,
  "referenceId"   :String(uuid)
}
```

|  |  |
| --- | --- |
| `code` | Error code (0 to 12582911). |
| `message` | English error message for debugging (up to 128 ASCII characters).  Since this message is meant for developers, do not use this for error handling or display this for users. |
| `referenceId` | Reference number for error. Not all APIs provide this information. |

An error code is included as a `code` member value and HTTP status code is just a supplement to it, so use an error code for error handling. Be sure that processing can continue even if an error code not shown in each reference document occurs.

Note: The structure of the error objects that return upon errors for some Web APIs varies from the above structure.

## (2) Display error content to the user.

Display an error message to the user as required.

On a PlayStation®5 application, the appropriate error message can be displayed by using the ErrorDialog library APIs (rate limit errors that occur as a result of excessive user operation are also supported). For the error code to pass as a parameter to an ErrorDialog library API, use the 32-bit integer value returned by `sceNpWebApi2SendRequest()` instead of the `code` member value.

## Handling of Undefined Errors That Start With 0x82

The PlayStation®5 SDK libraries may return undefined error codes starting with 0x82. These are represented as errors of PlayStation™Network Web APIs called in libraries, therefore the error details can be confirmed by converting them to Web API error codes (`code` member values) as follows.

**When the SDK library error code is 0x82000000 to 0x82BFFFFF**

1. Convert to a 24-bit integer value without 0x82 (example: 0x82202001 → 0x202001).
2. Convert the 24-bit integer value to decimal notation (example: 0x202001 → 2105345).
3. The obtained decimal number is a Web API error code. The error code range is determined by API group, so look up the API group for the error using the table below, then refer to the corresponding Web API reference document.

**When the SDK library error code is 0x82E00000 to 0x82E0FFFF**

These are authentication server errors. For details on these errors, contact SIE.

1. Convert to a 16-bit integer value without 0x82E0 (example: 0x82E00064 → 0x0064).
2. Convert the 16-bit integer value to decimal notation (example: 0x0064 → 100).
3. The obtained decimal number is an Auth Web API error code. For details on errors, refer to the [Auth Web API Reference](../../../WebAPI/latest/Auth_WebAPI-Reference/__document_toc.html) document.

**When the SDK library error code is 0x82E10000 to 0x82EFFFFF**

These are authentication server errors that indicate that an error code could not be obtained. For details on these errors, contact SIE.

**When the SDK library error code is 0x82F00000 to 0x82FFFFFF**

Indicates that a Web API error code could not be obtained. For details on these errors, contact SIE.

## Error Code Ranges For Each API Group

The error code ranges for each API group in the PlayStation™Network Web APIs are listed
in the table below.

Note: The Crash Reporting System Web API has a different set of error codes, as described in the [Crash Reporting System Web API Reference](../Crash_Reporting_System_WebAPI-Reference/__document_toc.html).

Error Code Ranges

| **API Group** | **Error Range (Decimal)** | **Error Range (24-bit Hexadecimal)** |
| --- | --- | --- |
| Account Closure Web API | 1048576 to 1052671  1069056 to 1073151 | 0x100000 to 0x100FFF  0x105000 to 0x105FFF |
| Communication Restriction Status Web API | 1048576 to 1060863 | 0x100000 to 0x102FFF |
| Entitlements Web API | 3158016 to 3162111 | 0x303000 to 0x303FFF |
| In-Game Catalog Web API | 3162112 to 3166207 | 0x304000 to 0x304FFF |
| Leaderboards Management Web API | 2297856 to 2301951 | 0x231000 to 0x231FFF |
| Leaderboards Web API | 2289664 to 2293759 | 0x22F000 to 0x22FFFF |
| Matches Web API | 2269184 to 2273279 | 0x22A000 to 0x22AFFF |
| Matchmaking Web API | 2273280 to 2277375 | 0x22B000 to 0x22BFFF |
| Package/Disc Management Web API | 2260992 to 2265087 | 0x228000 to 0x228fff |
| Profanity Filter Web API | 3350528 to 3354623 | 0x332000 to 0x332FFF |
| Session Manager Web API | 2232320 to 2236415 | 0x221000 to 0x221FFF |
| Subscription Status Web API | 1572995 to 1093762 | 0x180083 to 0x10B082 |
| Title Cloud Storage Management Web API | 2301952 to 2306047 | 0x232000 to 0x232FFF |
| Title Cloud Storage Web API | 2293760 to 2297855 | 0x230000 to 0x230FFF |
| Universal Data System Configuration Web API | 2306048 to 2310143 | 0x233000 to 0x233FFF |
| User Profile Web API | 2281472 to 2285567 | 0x22D000 to 0x22DFFF |

# Post Processing

This topic provides information on PlayStation™Network Web API post
processing.

Termination processing is not required for the PlayStation™Network Web APIs.