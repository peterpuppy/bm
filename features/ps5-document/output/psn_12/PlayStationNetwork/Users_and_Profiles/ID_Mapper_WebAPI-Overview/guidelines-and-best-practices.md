# ID Mapper Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/ID_Mapper_WebAPI-Overview/guidelines-and-best-practices.html

# Guidelines and Best Practices

This chapter provides guidelines and best practices to follow when using the ID Mapper Web API.

## ID Mapper Web API Guidelines

Game applications and servers must follow the following guidelines when working with account or online IDs:

* Online ID must be used only for user display and must not be kept persistent in a local game state, game servers, or in PlayStation™Network services such as Title User Storage (TUS) or Ranking.
* Online ID can be cached for display purposes, provided that you abide by the time-to-live (TTL) specified in the response header (or 4 hours if no header is specified). Alternatively, you may poll the ID Mapper Web API - Online ID Change List request every one to four hours to obtain a list of online IDs that have recently changed and purge only changed IDs from your cache.
* Account ID must be the only durable unique identifier for PlayStation™Network users. It is acceptable in game servers to keep your own user ID persistent as long as there is a mapping to the account ID.
* Game applications and servers must use account ID-based API requests to interact with PlayStation™Network services.
* Account ID must not be displayed to users.

## ID Mapper Web API Best Practices

With real-time requests:

* Always use the keyword `me` to refer to the current user in Web API URIs, if available.
* Always retrieve the current user's account ID from the token validation response, rather than using the ID Mapper Web API.
* You can optionally use batch mode for real-time access in running applications and game servers.

With background migration:

* When migrating multiple accounts, use the batch mode to map multiple IDs at a time in each call.

In both situations:

* Cache results in your game server to improve performance, but abide by the `cache-control` header values. If you cache mappings returned by other PlayStation™Network software, you must discard them after four hours.
* It is more efficient to concentrate first on rekeying your data stores from `onlineId` to `accountId` and secondly to take care of online ID references within the data.
* When migrating data that is keyed on online ID, discard any entries for which the API returns a value of "`isCurrent=false`". Until changing online ID becomes a user feature, these entries will correspond to users whose online IDs were administratively changed. In this instance, the data in question is inaccessible.