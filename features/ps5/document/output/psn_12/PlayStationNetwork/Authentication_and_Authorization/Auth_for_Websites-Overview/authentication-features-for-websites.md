# Authentication Features for Websites Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Auth_for_Websites-Overview/authentication-features-for-websites.html

# Authentication Features for Websites

# Purpose and Characteristics

Authentication features for websites are for performing user authentication using accounts for PlayStation™Network and are provided targeting general browsers, such as those on PCs/smartphones.

By using the authentication features for websites, the following can be performed on customized websites.

* User authentication
* Obtaining user age, parental control, country/region of residence, language used, etc.
* Obtaining information of privileges owned by the user, including entitlements purchased on PlayStation™Store
* (By also using S2S communication service APIs:) obtaining profile information such as the online name and self introduction in PlayStation™Network, and obtaining friend list

A summary of the procedure for authenticating a user using the authentication features for websites is as follows.

1. Forward the user to the designated URL by a link or redirection. As the URL query parameter, specify the URL to return the user back to after sign-in processing.
2. The sign-in screen is displayed, and the user enters their PlayStation™Network sign-in ID and password.
3. After sign-in, the user is returned to the specified URL and the authorization code issued by the authentication features for websites is returned as the query parameter.
4. Transmit the authorization code, along with the Client ID and Client Secret issued to the website, to the authentication server. The access token indicating that the user has been authorized will be returned.
5. The returned access token can be used to obtain user information. The access token can also be transmitted when using the S2S API and used for obtaining user authorization.

The authentication features for websites do not demand specific technologies from websites. As long as the authentication features for websites are accessed following the specifications indicated in this document, it does not matter which technologies are used to configure websites.

# Passkey Integration in Mobile Apps

To allow passkey-based sign in from passwordless accounts, all mobile apps and websites that use PlayStation™Network sign in must support WebAuthn. If a mobile app does not support WebAuthn, the user will be unable to access that mobile app using PlayStation™Network sign in even if they have enabled their account's passkey.

For details, refer to "Passkey Integration in Mobile Apps" (<https://game.develop.playstation.net/projects/sdk/dl/dl/71/6497/Passkey_integration_in_Mobile_Apps_for_Partners_v1.0_j.pdf>) on the Developer Network website.

# OAuth 2.0

The authentication features for websites that are the subject of this document are implemented pursuant to RFC 6749 "The OAuth 2.0 Authorization Framework" (<http://tools.ietf.org/html/rfc6749>). Refer separately to RFC information, for example, as necessary.

## Other Reference Materials

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Authentication Features for Websites](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Auth_for_Websites-ReleaseNotes.html)