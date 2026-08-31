# PlayStation™Network Web APIs Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_WebAPI-Overview/api-group-strings.html

# Feature Overview

This chapter describes the features PlayStation™Network Web APIs provide.

# PlayStation™Network Web API Clients

This topic provides information on the available clients that PlayStation™Network Web
APIs support.

PlayStation™Network Web APIs are provided for the PlayStation®5 platform clients indicated below:

* PlayStation®5 applications.
* Application servers.
* Back office server.

The classifications of an application/application server/back office server for each platform are called "product types". For details regarding product types, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) document.

Note that an "application server" typically refers to servers such as game servers run for applications on PlayStation®5. "Website" refers to other servers. A "back office server" refers to a server used mainly for development and operation support.

# API Group Strings

This topic shows the relationship between API group names and API group
strings.

The strings representing API group names to be specified for using each API group are
listed in the table below.

API Group Strings

| **API Group** | **API Group String** |
| --- | --- |
| Account Closure Web API | `accountClosure` |
| Active Activities Web API | `activities` |
| Advanced Player Profile Management Web API | `advancedPlayerProfile` |
| Advanced Player Profile Web API | `advancedPlayerProfile` |
| Commerce Management Web API | `partnerEventService` |
| Communication Restriction Status Web API | `communicationRestrictionStatus` |
| Crash Reporting System Web API | `crashReport` |
| Entitlements Web API | `entitlement` |
| In-Game Catalog Web API | `inGameCatalog` |
| Leaderboards Management Web API | `leaderboards` |
| Leaderboards Web API | `leaderboards` |
| Matches Web API | `matches` |
| Matchmaking Web API | `matchmaking` |
| Package/Disc Management Web API | `gemsTool` |
| Profanity Filter Web API | `profanityFilter` |
| Session Manager Web API | `sessionManager` |
| Subscription Status Web API | `subscriptionsManager` |
| Title Cloud Storage Management Web API | `titleCloudStorage` |
| Title Cloud Storage Web API | `titleCloudStorage` |
| Universal Data System Configuration Web API | `universalDataSystem` |
| User Profile Web API | `userProfile` |

# Service Name in DevNet

This topic provides information on the relationship between API group names and DevNet
service names.

The names of the service that needs to be requested in DevNet are listed in the table
below.

Service Names in DevNet

| **API Group** | **DevNet Service Name** |
| --- | --- |
| Account Closure Web API | N/A |
| Active Activities Web API | Universal Data System |
| Advanced Player Profile Management Web API | Advanced Player Profile Management |
| Advanced Player Profile Web API | Advanced Player Profile |
| Commerce Management Web API | Commerce Management |
| Communication Restriction Status Web API | N/A |
| Crash Reporting System Web API | Crash Report |
| Entitlements Web API | PlayStation™Store Delivered Contents |
| In-Game Catalog Web API | PlayStation™Store Delivered Contents |
| Leaderboards Management Web API | Leaderboards Management |
| Leaderboards Web API | Leaderboards |
| Matches Web API | Universal Data System |
| Matchmaking Web API | Session Manager |
| Package/Disc Management Web API | Package/Disc Management |
| Profanity Filter Web API | Profanity Filter |
| Session Manager Web API | Session Manager |
| Subscription Status Web API | Subscription Status |
| Title Cloud Storage Management Web API | Title Cloud Storage Management |
| Title Cloud Storage Web API | Title Cloud Storage |
| Universal Data System Configuration Web API | Universal Data System Management |
| User Profile Web API | Presence 2  (in case retrieving Presence information) |

# PlayStation™Network Web API Usage Conditions

This topic provides information on PlayStation™Network Web API usage
requests.

## PlayStation™Network Web API Usage Requests

In order to use a Web API, a request must be made in advance for the service corresponding to the Web API. In other words, a Web API cannot be used if a request for its corresponding service is not accepted. For details on how to make service requests, refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) document.

Note: While most APIs require a request on the Developer Network website for usage, you can use the User Profile Web API with just an NP Title ID or Client ID. However, in the case of retrieving presence information with the User Profile Web API, a service setup is also required.

## Usable PlayStation™Network Web APIs

See the *Use Restrictions* section of each web API to check if a product type can use a PlayStation™Network Web API and [PlayStation™Network Service Setup Guide - Making Service Requests - Available Services](../PSN_Service_Setup-Guide/available-services.html) to check available services for a certain application type.

Note: API Support may vary for each API and request. Also, note that in many of the combinations where a Web API cannot be used, the use of an SDK library (for example) can achieve the equivalent functionality.

## Usage Restriction by User State

In order to use the PlayStation™Network Web APIs, the user must be signed into the PlayStation™Network. The usage of some requests such as, requests related to presence information, require the user to be in an online state.

# HTTP Method and URI Specifications

This topic provides details on the HTTP methods and URI specifications that
PlayStation™Network supports.

The PlayStation™Network Web APIs support HTTP/1.1 and HTTP/2.0.

Note: Supported HTTP version and other values may vary by API.

Each PlayStation™Network Web API is represented with the HTTP method and URI set as follows.

```
Method ApiGroupBaseUrl/ResourcePath[?QueryString]
```

## Method

The HTTP method. Four types are used: `GET`, `POST`, `PUT`, and `DELETE`.

## ApiGroupBaseUrl

Base URL defined for each API group. Includes the URI scheme, FQDN, and part of the path. For details, see [Usage](usage.html "This topic provides general use cases for using PlayStation™Network Web APIs.").

**Example:** `https://s2s.sp-int.playstation.net/api/userProfile`

## ResourcePath

The resource path. The resource path includes the version portion at the beginning. The version is represented with the prefix `v`.

**Example:** `/v1/users/user000/profile`

Note: Please note that for specific versions, usage may be restricted after notice is given for a certain time period.

## QueryString

The query string.

# Rate Limit

This topic provides information on PlayStation™Network Web API rate
limits.

A "rate limit" is placed on the frequency of many PlayStation™Network Web API calls to only permit a certain number of calls within a certain time period as excessive accesses affect Web API server performance. Although the limit on the number of calls is set high enough so that there should be no inconvenience in general use cases, access frequency may increase if the user performs the same operation repeatedly; there is also a possibility that the limit on the number of calls will be lowered in the future. Even if the limit is not reached, as a general rule, keep the access frequency as low as possible; prevent unneeded accesses by caching obtained data and using Push events. For details on the recommended frequencies by which to call requests, refer to each Web API reference document.

As a general rule, the access frequency is counted per client application identifier (e.g. Np Title Id, Auth Client Id, etc.) and per user. Moreover, the time unit and the limit on the number of calls set as the rate limit differ per request. Multiple requests share access counts in some cases (`PUT` and `DELETE` for example).

When a PlayStation™Network Web API is called exceeding the rate limit, an error code indicating that the rate limit has been exceeded returns in the response body along with the following HTTP response header. For an error code, please refer to each Web API reference document.

```
Retry-After: delay-seconds
```

Web APIs return how long the client application ought to wait before making a follow-up request with the Retry-After HTTP response header. As a general rule, the value of the header is a number of seconds to delay after the response is received. If the client application receives the rate limit error, it must wait to send a follow-up request.

## Temporarily Receiving the Rate Limit

To make it easier to test processing that handles rate limit errors, a feature that temporarily returns the rate limit error set for a request is provided. Set the following HTTP request header and execute the request:

```
X-PSN-Fake-Rate-Limit-Enabled: true
```

For PlayStation®5 applications, use the debug settings on the console instead of setting HTTP request header. For details of the debug settings, refer to the 'PlayStation™Network − Web API Force Rate Limit' section in the [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html).

In addition, a feature that temporarily returns the rate limit error is available for specified API groups. You can specify multiple comma separated API group strings without spaces:

```
X-PSN-Fake-Rate-Limit-Targets: <Comma separated API group strings without spaces>
```

For PlayStation®5 applications, use the debug settings on the console instead of setting HTTP request header. For details of the debug settings, refer to the 'PlayStation™Network − Web API Force Rate Limit Target' section in the [System Software User's Guide (Settings)](../System_Software-Users_Guide_for_Settings/__document_toc.html).

These headers are supported only on the development/sp-int and Certification environment/prod-qa environments.

# Supported Languages and Language Codes

This topic lists supported languages and their associated language codes.

The PlayStation™Network Web APIs have multilingual support. With requests that include text information for users in responses, it is possible to receive text in the language specified upon a request.

The languages that can be used with the PlayStation™Network Web APIs and the corresponding language codes are as follows. PlayStation™Network Language Code supported on PlayStation®5 has been updated since the PlayStation®4 generation.

Supported Languages and Language Codes

| **Language Name** | **PlayStation™Network Language Code** | **PlayStation®4 Language Code** |
| --- | --- | --- |
| Arabic | ar-AE | ar |
| Czech | cs-CZ | cs |
| Danish | da-DK | da |
| German | de-DE | de |
| Greek | el-GR | el |
| English (United Kingdom) | en-GB | en-GB |
| English (United States) | en-US | en |
| Spanish (Latin America) | es-419 | es-MX |
| Spanish (Spain) | es-ES | es |
| Finnish | fi-FI | fi |
| French (Canada) | fr-CA | fr-CA |
| French (France) | fr-FR | fr |
| Hungarian | hu-HU | hu |
| Indonesian | id-ID | id |
| Italian | it-IT | it |
| Japanese | ja-JP | ja |
| Korean | ko-KR | ko |
| Dutch | nl-NL | nl |
| Norwegian | no-NO | no |
| Polish | pl-PL | pl |
| Portuguese (Brazil) | pt-BR | pt-BR |
| Portuguese (Portugal) | pt-PT | pt |
| Romanian | ro-RO | ro |
| Russian | ru-RU | ru |
| Swedish | sv-SE | sv |
| Thai | th-TH | th |
| Turkish | tr-TR | tr |
| Vietnamese | vi-VN | vi |
| Chinese (Simplified) | zh-Hans | zh-CN |
| Chinese (Traditional) | zh-Hant | zh-TW |

Note: Supported languages might be added in the future. In addition, the supported languages may vary depending on the API group.

# Push Events

This topic provides information on how and when to use push events.

Push events are features that can receive notifications when resources have changed. They can detect resource updates in real time, such as changes in a friend's online status. Since processing that detects resource updates with polling can cause excessive strain on servers, push events can be more efficient when used properly.

When using push events, note the following:

* To receive push events, the user must be in the online status.
* Push events may not arrive when unexpected errors such as network errors occur.
* The order by which events occur on the server may differ from the order by which push events arrive.

Push events are defined for each data type. Push events can include the following content, and from among these, the data type and recipient information are always included.

* Data type:

  + Indicates what resource changed.
* Sender:

  + Includes the Online ID, account ID, and platform information of the sender.
* Recipient:

  + Includes the Online ID and account ID of the recipient.
* Data:

  + Arbitrary data represented in JSON with UTF-8 encoded character strings. Up to 1024 bytes.
* Extended data:

  + Extended data represented in JSON with UTF-8 encoded character strings. It is possible to specify an extended data key and obtain the value that corresponds to the key. A value that corresponds to a single extended data key can be up to 1024 bytes.

Note: For details on receiving push events with PlayStation®5, refer to the NpWebApi2 library documents.