# ID Mapper Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/ID_Mapper_WebAPI-Overview/using-the-online-id-change-list-on-servers.html

# Using the ID Mapper Web API

This chapter provides information on how to use the ID Mapper Web API.

# Mapping User IDs

This topic provides information on how to map user IDs.

You can map user IDs individually or in batches.

## Mapping Individual User IDs

Individual mapping functions provide the ability to map a single ID. Using the GET method, the URIs to convert IDs are:

* `sdkIdentityMapperBaseUrl/v3/users/map/onlineId2accountId/{online_id}`
* `sdkIdentityMapperBaseUrl/v3/users/map/accountId2onlineId/{account_id}`

Use the first URI to map an online ID to an account ID. The second maps an account ID to an online ID.

Additionally, when making the `onlineId2accountId` request, you can also specify the `asOf` query parameter. This parameter returns the account ID associated with the given online ID as of the time specified rather than the current time. Refer to [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) for correct format.

**Returned Data**

Because account IDs do not change, and online IDs can change, the data returned from these two calls are different. For online ID to account ID, the data returned is:

```
{
                   "accountId"  : String,
                   "isCurrent"  : Boolean,
                   "isRecycled" : Boolean,
                   "onlineId"   : String
}
```

For account ID to online ID, the data returned is:

```
{
                   "accountId" : String,
                   "onlineId"  : String
}
```

The following table describes the members of these objects:

|  |  |
| --- | --- |
| `accountId` | The account ID. |
| `isCurrent` | If the passed `onlineId` is currently associated with the `accountId`, `isCurrent=true`. If the association was active in the past, `isCurrent=false`. |
| `isRecycled` | If another account was associated with the online ID in the past, `isRecycled=true`. |
| `onlineId` | The online ID. Minimum length of 3 characters, maximum of 16. If the online ID cannot be mapped to an account ID, just the online ID is returned in the object with no other data. Regex pattern=*^[a-zA-Z][a-zA-Z0-9\_-]{2,15}$*. |

**Example**

This example shows a request to get an account ID, given an online ID and `asOf` query parameter. First, the request:

```
GET sdkIdentityMapperBaseUrl/v3/users/map/onlineId2accountId/HappyRobert?asOf=2017-11-02T12:34:12.398%2B0000
```

Note that the value for "`asOf`" parameter is URL encoded in the example above. Decoded value is 2017-11-02T12:34:12.398+0000.

And the response:

```
{
                   "accountId": "123456789",
                   "isCurrent": "true",
                   "onlineId": "HappyRobert"
}
```

## Mapping Multiple User IDs

Batch mapping allows you to map several IDs at one time. The URIs for batch mapping are:

* `sdkIdentityMapperBaseUrl/v3/users/map/edge/onlineId2accountId/batch`
* `sdkIdentityMapperBaseUrl/v3/users/map/edge/accountId2onlineId/batch`

Batch mapping uses query parameters to specify the ID's that need to be mapped. The response will contain a corresponding array of mapped IDs of the appropriate type. If an online ID is passed that does not have a corresponding account ID, the response contains only the passed in online ID.

For example, to map from online IDs to account IDs, you could pass the following array to map:

```
sdkIdentityMapperBaseUrl/v3/users/map/edge/onlineId2accountId/batch?id=slimJim&id=bigBill&id=tallJohn
```

To map account IDs to online IDs, you pass in an array of account IDs:

```
sdkIdentityMapperBaseUrl/v3/users/map/edge/accountId2onlineId/batch?id=571828457&id=512541255&id=254155135
```

**Returned Data**

The data for batch mapped IDs is the same as it is for individual IDs, except that they are in JSON arrays. For example, for mapping the above online IDs, and if "`tallJohn`" was not a valid online ID, the response body would be:

```
[
               {
                   "accountId": "123456789",
                   "isCurrent": "false",
                   "isRecycled": "true",
                   "onlineId": "slimJim"
               },
               {
                   "accountId": "987654321",
                   "isCurrent": "true",
                   "isRecycled": "false",
                   "onlineId": "bigBill"
               },
               {
                   "onlineId": "tallJohn"
               }
]
```

For further details, see [ID Mapper Web API Reference](../ID_Mapper_WebAPI-Reference/__document_toc.html).

# Using Cache Control

This topic provides information on how to use the cache control feature of the ID Mapper Web API.

In addition to providing the ability to map between online and account IDs, the ID Mapper Web API provides a guideline to determine when to map by providing a time-to-live caching value for online ID mappings.
The retention policy is based upon how an application receives a particular mapping from the PlayStation™Network API. Mappings received from the ID Mapper Web API can be reused for the period specified in the `cache-control` response header before they must be refreshed.

The `cache-control` header provides a time-to-live value you can use to refresh any IDs that have been cached. For example:

`Cache-Control:max-age=86400`

Note:

Mappings received in the responses from other Web API requests and SDK functions can be reused for up to four hours before they must be refreshed.

If you have a server application that has mappings cached for multiple accounts, you can avoid having to refresh each mapping individually by using the ID Mapper Web API Online ID Change List request. This request allows you to get a list of online IDs that have changed since a specified time. Making this call periodically and removing the changed online IDs from your cache will refresh the remaining items in the cache. Call it at least as often as the minimum of the time specified in the `cache-control` response header, or four hours, whichever is smaller.

Note:

Because applications can be suspended and resumed, time must be based on wall clock time and not elapsed game time. It is a best practice to use network time to determine if a mapping cache entry is stale.

# Using the Online ID Change List on Servers

This topic provides information on how to use the change list feature of the ID Mapper Web API.

The Online ID Change List request returns a list of all online IDs changed since a given date-time. The number of results returned are limited by the "limit" query parameter. Next set of results can be obtained by changing the value of the "since" query parameter to a later instant. This request uses the GET Method and the following method and URI:

```
GET sdkIdentityMapperBaseUrl/v3/users/onlineIdHistory
```

The request has the following query parameters:

* since: optional (string) default=(current date-time - 1 hour)

Date-time is the starting point for returning results. The request supports GMT time only. Refer to [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) for format.

* `limit: optional (string) minimum=1 maximum=1000 default=100`

The maximum number of results to be returned.

The response is an array of account IDs, the old online ID, the new online ID, and the date-time it changed. The following table describes the members of these objects:

|  |  |
| --- | --- |
| `accountId` | The account ID. |
| `dateChanged` | The date and time the online ID was changed. |
| `newOnlineId` | The current online ID. |
| `oldOnlineId` | The previous online ID. |

## Example

**Request**

```
GET sdkIdentityMapperBaseUrl/v2/accounts/onlineIdHistory?since=2013-11-07T11:03:00.000+0000&limit=100
```

**Response**

```
[
    {
        "accountId": "123456789",
        "dateChanged": "2013-11-07T11:03:20.000+0000",
        "newOnlineId": "SeriousAdult54",
        "oldOnlineId": "SillyKid42"
    },
    {
        "accountId": "123478907",
        "dateChanged": "2013-11-08T11:03:20.000+0000",
        "newOnlineId": "Mutton",
        "oldOnlineId": "LambChop"
    }
]
```

To avoid having to refresh each mapping individually, remove the changed online IDs from your cache, which keeps the remaining items in the cache current.