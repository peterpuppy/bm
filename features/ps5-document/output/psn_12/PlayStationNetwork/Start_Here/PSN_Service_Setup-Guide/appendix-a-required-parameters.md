# PlayStation™Network Service Setup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Service_Setup-Guide/appendix-a-required-parameters.html

# Appendix A: Required Parameters

This topic provides information on the parameters required to enable certain PlayStation™Network services.

The information required for PlayStation™Network service requests vary depending on the service. The following tables show the information and actions required for each service. Refer to them when making requests.

Information Required for Client ID (App Server) Service Requests

| Input Field | Information and Actions Required |
| --- | --- |
| Redirect URI | Enter the URI (the first part) for redirect backs for users who sign in from authentication features for websites.  Must be an https scheme URI that includes a FQDN but does not end with a FQDN.  Examples of acceptable URIs:   * https://example.com/signedin/ * https://example.com/signedin * https://example.com/   Example of unacceptable URIs:   * <https://example.com> |
| Refresh Token | Optionally, you can request a refresh token to be included in the response that provides an access token. For more information, see [Auth Web API Overview - Providing Access Privileges to an Application Server - Game Refresh Tokens](../../../WebAPI/latest/Auth_WebAPI-Overview/game-refresh-tokens.html) and the [Auth Web API Reference](../../../WebAPI/latest/Auth_WebAPI-Reference/__document_toc.html). |

Information Required for Client ID - App Server (client credential), Back Office Server - Service Requests

| Input Field | Information and Actions Required |
| --- | --- |
| Access source IP addresses | In order to call PlayStation™Network Web APIs from an App Server (client credential) or a Back Office Server, the calling source IP address must be registered on the ACL (access control list). Enter the IP addresses to register on the ACL.  Specify an IP range of /24 to /32 for IP addresses.  Note that private IPv4 addresses are not acceptable. (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) |