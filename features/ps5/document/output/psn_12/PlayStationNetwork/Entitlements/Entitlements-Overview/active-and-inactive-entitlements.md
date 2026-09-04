# Entitlements Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Entitlements-Overview/active-and-inactive-entitlements.html

# Using the Entitlements Web API

This chapter provides details on how to use the Entitlements Web API.

Entitlement retrieval requests return information in an entitlement object. For a description of the elements in the response bodies of these requests, see [Entitlements Web API Reference](../Entitlements_WebAPI-Reference/__document_toc.html).

# Retrieving Entitlement Data

This topic provides details on what types of information the Entitlements Web API can retrieve.

The Entitlements Web API can retrieve the following types of information:

* All entitlements held by the current user.
* A specific entitlement held by the current user.

## Retrieving a Set of Entitlements

To retrieve a set of entitlements held by the current user, use [Entitlements Web API Reference - Entitlements - listEntitlements](../Entitlements_WebAPI-Reference/0002.html):

```
GET entitlementBaseUrl/v2/users/me/entitlements
```

The above example gets all entitlements held by a user. To get a certain set of entitlements, use the id query parameter (up to 100), and add the entitlement labels as necessary separated by commas:

```
GET entitlementBaseUrl/v2/users/me/entitlements?id=ENTITLEMENT00001,ENTITLEMENT00002
```

When using the `id` parameter, `entitlementType` becomes optional.

Note that there is no request body.

Upon normal termination, the response consists of an HTTP status code of 200 and the `entitlements` object, which contains an array of `entitlement` objects.

**Example: Obtaining Entitlement Information**

In this example, the request asks for all entitlements of the current user, sorted ascending by active date. The response contains an `entitlements` object containing an array of user entitlements. Note that the first entitlement returned is not consumable, but the second one is. Because we have specified `id`, `entitlementType` is not necessary.

**Request**

```
GET entitlementBaseUrl/v2/users/me/entitlements?sort=activeDate&direction=asc&id=ENTITLEMENT00001,ENTITLEMENT00002
```

**Response**

```
{
                "entitlements" : [ {
                "inactiveDate" : "2000-01-23T04:56:07.000+00:00",
                "activeDate" : "2000-01-23T04:56:07.000+00:00",
                "id" : " ENTITLEMENT00001",
                "useCount" : 1,
                "useLimit" : 5,
                "entitlementType" : "UNIFIED",
                "packageType" : "PSCONS",
                "activeFlag" : true
                }, {
                "inactiveDate" : "2000-01-23T04:56:07.000+00:00",
                "activeDate" : "2000-01-23T04:56:07.000+00:00",
                "id" : " ENTITLEMENT00002",
                "entitlementType" : "UNIFIED",
                "packageType" : "PSAL",
                "activeFlag" : true
                } ],
                "previousOffset" : 6,
                "nextOffset" : 0
                }
```

## Retrieving a Specific Entitlement

To retrieve a specific entitlement that belongs to a user, use [Entitlements Web API Reference - Entitlements - getEntitlement](../Entitlements_WebAPI-Reference/0003.html):

```
GET entitlementBaseUrl/v2/users/me/entitlements/entitlementLabel
```

Where `entitlementlabel` is the label for the entitlement information to obtain.

Note that there is no request body.

Upon normal termination, the response consists of an HTTP status code of 200 and the `entitlement`object. If the user does not have the entitlement, the request returns a 404 "Entitlement not found." error.

**Example: Obtaining Information for an Entitlement**

In this example, information is requested for an entitlement labeled as `CALLINGALLCARS01.`

**Request**

```
GET entitlementBaseUrl/v2/users/me/entitlements/CALLINGALLCARS01
```

**Response**

```
{
                "inactiveDate" : "2000-01-23T04:56:07.000+00:00",
                "activeDate" : "2000-01-23T04:56:07.000+00:00",
                "id" : " CALLINGALLCARS01",
                "entitlementType" : "UNIFIED",
                "packageType" : "PSAL",
                "activeFlag" : true
                }
```

# Active and Inactive Entitlements

This topic highlights the conditions that make an entitlement active or inactive.

In addition to having a permanent entitlement, an application can limit an entitlement by a number of uses (is consumable) or by date. This limit can be one type or the other, but not be both. Limiting entitlements by date provides the ability to have application features such as:

* Limited time betas or demos.
* In game sales for a specific period.
* Subscriptions or other short-term items.

Date-limited entitlements have an `activeDate` and an `inactiveDate`. Within those dates, the entitlement is active. To check if an entitlement is active, you can use the `activeFlag` for the `getEntitlement` and `listEntitlements` requests. This field is true if the entitlement is active, false if it is not. Use `activeFlag` for both subscription and non-subscription entitlements.

Further, do not check entitlement eligibility based on the validity period, and specifically do not use `inactiveDate` to determine eligibility, as some entitlements can trigger mismatches in units of minutes depending on the timing of update processing. For example, in actions such as auto-renewal and eligibility rule check.

This functionality is intentional. In case of a server issue however, there is a possibility that the mismatch occurs for a longer time-period due to a delay in processing updates. In this case, using `inactiveDate` in-game results in an issue where a user cannot use the entitlement in game or purchase a new one in the PlayStation™Store when there is an eligibility rule to prevent duplicated purchases. This is because the PlayStation™Store uses `activeFlag` for entitlement eligibility check, as designed. In general, use `activeDate` and `inactiveDate` fields to present to the user information about an entitlement start date or end date. You can inform the user of such things as:

* Remaining days for an event.
* The date when a special in-game event ends.
* A subscription validity period.

When displaying validity periods of a subscription, note that since there is no method to obtain the status of auto-renew of an entitlement within a game, it is best to display dates as "validity period" rather than "next scheduled date of renewal."

Note:

Permanent entitlements do not have an `inactiveDate` field, unless a refund on the entitlement occurs. When an item is refunded, the date the item was refunded appears in the field indicating it is no longer active. Inactive entitlements remain in the user's entitlement list.