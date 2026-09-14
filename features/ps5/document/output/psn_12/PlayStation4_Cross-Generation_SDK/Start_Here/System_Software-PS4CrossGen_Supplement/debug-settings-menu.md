# System Software Cross-Generation Supplement – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/System_Software-PS4CrossGen_Supplement/debug-settings-menu.html

# Additional Information for the Cross-Generation SDK

The PlayStation®4 Cross-Generation SDK ("Cross-Gen SDK") is an SDK for making some of the SDK features provided for PlayStation®5 usable on PlayStation®4. For more information about the Cross-Gen SDK as a whole, refer to the [Cross-Generation Overview](../Cross_Generation-Overview/__document_toc.html).

This document explains the differences between the system software included in the Cross-Gen SDK and the system software included in a standard PlayStation®4 SDK ("PlayStation®4 SDK").

# "★Debug Settings" Menu

## PlayStation™Network - WebTrace

Refer to the [Web API Tracer User's Guide](../Web_API_Tracer-Users_Guide/__document_toc.html) document for details.

## PlayStation™Network - Web API Force Rate Limit (version 2)

This setting is for checking application behavior when exceeding the call rate limit of PlayStation™Network Web APIs.

When this setting is set to "Enable", an error for when the call rate limit is exceeded will be returned for Web API calls that go through the NpWebApi2 and NpCppWebApi library.

Refer to the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document for details on the call rate limits of Web APIs.

## PlayStation™Network - Web API Force Rate Limit Target (version 2)

When "Web API Force Rate Limit (version 2)" is enabled, this setting allows you to check the behavior of an API group when the call rate limit for PlayStation™Network Web APIs is exceeded.

If you specify the name of an API group to this setting, an error for when the call rate limit is exceeded will be returned for that API group regarding Web API calls that go through the NpWebApi2 and NpCppWebApi library.

When this setting is not specified, an error for when the call rate limit is exceeded will be returned for the Web API calls of all API groups.

For example, when setting "Enable" to "Web API Force Rate Limit (version 2)" and "leaderboards" to "Web API Force Rate Limit Target (version 2)", an error for when the call rate limit is exceeded will only be returned for Leaderboards Web API calls. For the calls of other Web API groups, an error for when the call rate limit is exceeded will not be returned and the calls will be made as usual.