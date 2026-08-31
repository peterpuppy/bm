# Communication Restriction Status Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Communication_Restriction_Status_WebAPI-Overview/reference-materials.html

# About the Communication Restriction Status Web API

This chapter provides basic information about the Communication Restriction Status Web API.

The ability to engage in communication (social) activities on the PlayStation™Network is a major feature of the platform. For example, posting or viewing user-generated content, such as texts, images, audio and video clips, and broadcasts.

There are times when it is necessary for the platform and any games running on the platform to prevent a user from engaging in such features. The Communication Restriction Status Web API tells an application whether the social features are allowable for a particular user, identified by an account ID. This check needs to occur for all the accounts, and is not limited to children accounts.

A user can become restricted through the following situations:

* Parental Controls. Family Managers and Guardians can block a child's social features via the Communication and User Generated Content Parental Control. Valid values are "Allow" or "Block".
* Communication Suspension. For various reasons, primarily malicious social activity, the PlayStation™Network may determine that a user has violated its terms of service and can therefore go into a short or prolonged suspension of all social features. Non-social features, such as game play and game purchase should be unaffected by this however.

Note: If the API returns a Communication Restriction Status of "true", a caller of this API will not have the ability to understand which of these criteria a user meets.

# Using the Communication Restriction Status Web API

This topic provides information on when you should use the Communication Restriction Status Web API.

When your application has features such as posting or viewing of user generated content (text, image, audio, video clip, broadcasting, etc.), communication using text, audio, video etc., use this API to determine if the user with a given account ID can use such features.

If your application does not have such features, you do not need to use this API.

# Reference Materials

This topic provides links to documents relevant to the Communication Restriction Status Web API.

* For general topics such as call procedures for APIs that include advance preparations (such as obtaining a base URL), error handling, and call rate limits, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

* For details of the Communication Restriction Status Web API, see [Communication Restriction Status Web API Reference](../Communication_Restriction_Status_WebAPI-Reference/__document_toc.html).

* For information about bugs, points to note, restrictions, and announcements, see [Release Notes - Communication Restriction Status Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Communication_Restriction_Status_WebAPI-ReleaseNotes.html).