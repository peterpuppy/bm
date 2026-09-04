# ID Mapper Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/ID_Mapper_WebAPI-Overview/id-mapper-overview.html

# ID Mapper Web API Overview

This chapter provides an overview of the ID Mapper Web API.

The PlayStation™Network ID Mapper Web API provides the ability to map between online IDs and account IDs. The account ID represents a user in persistent storage, while the online ID is used for real-time display of a user's identity. The API also includes the ability to obtain a list of online IDs changed since a given date-time.

## Features

The ID Mapper Web API provides the following core features:

* Map an array of account IDs to their associated online IDs.
* Map an array of online IDs to their associated account IDs.
* Map an individual online ID to its associated account ID.
* Map an individual account ID to its currently associated online ID.
* Get a list of online IDs changed since a given date-time.

## Usage

Use this API when you:

* Have the account ID but need the online ID.
* Have the online ID but need the account ID.

You do not need to use this API when you:

* Are obtaining local user information in a game.
* Are obtaining user information on a network.

You can map IDs individually, or map them in batches. See [ID Mapper Web API Reference](../ID_Mapper_WebAPI-Reference/__document_toc.html) for example API requests.

## Reference Materials

The ID Mapper Web API is part of the PlayStation™Network Web APIs. Refer to the following documents for general topics such as call procedures for Web APIs, obtaining a base URL, error handling, call rate limits, and further details on ID mapping:

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - ID Mapper Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-ID_Mapper_WebAPI-ReleaseNotes.html)