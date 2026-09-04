# User Profile Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/User_Profile-Overview/service-request.html

# Presence Information

# About Presence Information

Presence information indicates how individual users are currently accessing PlayStation™Network, as follows.

* Whether a user is online or not
* Whether the current user and the target user are playing the same application

Note:

Whether a user is online indicates whether that user is accessing PlayStation™Network from a PlayStation®5 or PlayStation®4 console. Access from a PlayStation®Vita unit or a PlayStation®3 console has no effect here.

# Obtaining Presence Information

`GetBasicPresences` can be used to obtain presence information of the user with the specified account ID. However, whether the information will be successfully obtained depends on the "Presence Information Privacy Settings" set by the target user.

In addition, presence information changes can be obtained when using Push events. Refer to the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html) document for information on how to use Push events and refer to the [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html) document for details on Push events that can be used.

# Service Request

Refer to the [PlayStation™Network Service Setup Guide](../../../SDK/latest/PSN_Service_Setup-Guide/__document_toc.html) document for making a service request.

In addition, the following will be enabled by making a request to use the Presence 2 service. (Refer to the [User Profile Web API Reference](../User_Profile_WebAPI-Reference/__document_toc.html) document for details on the Presence 2 service.)

* An object called `inContext` will be included in the response of the `GetBasicPresences` request
* The presence inContext information update event (Push event) will be sent

# Presence Information Privacy Settings

Users can select one of the following settings for the scope of disclosure of their presence information.

* Disclose to all users
* Disclose only to friends and friends of friends
* Disclose only to friends

# Feature to Hide Presence (Appear Offline Feature)

## Appear Offline Setting

The system software for PlayStation®5 and that for PlayStation®4 provide a feature to hide the user's presence for occasions when the user does not want to disclose their online status - or information regarding games being played - to friends (Appear Offline feature). The user can change the Appear Offline setting any time from the system software's Control Center, for example.

When the user enables the Appear Offline setting, the user's online status will be displayed as offline regardless of the actual status.

## Effects on the Application

The enabling/disabling of the Appear Offline setting may affect some request operations. For details regarding the behavior of each Web API when the Appear Offline setting is enabled, refer to the documentation for each Web API.

## Application-side Support

Even when the Appear Offline setting is enabled, the application must be implemented so that all types of gameplay including online multiplayer gameplay are possible. Be careful so that gameplay does not become drastically limited when the Appear Offline setting is enabled.

Moreover, when enabling online multiplayer gameplay, the user with the Appear Offline setting enabled will still be visible as playing the game online to others playing the same game. This may seem contradictory but is not a problem.