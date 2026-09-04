# Entitlements Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Entitlements-Overview/procedure-for-consuming-entitlements.html

# Handling Consumable Entitlements

This chapter provides information on how to handle consumable entitlements.

Consumable entitlements are a product type sold in the PlayStation™Store, represented by the package types `PSVC` and `PSCONS`. The former is for virtual currency and the latter for other consumable items such as weapons, skins, and other special in-game items. For details, see the [Entitlements Web API Reference](../Entitlements_WebAPI-Reference/__document_toc.html).

The user purchases and consumes entitlements, after which the user has a certain number of rights in a game. The order in which an entitlement is consumed is crucial:

1. Retrieve entitlement eligibility.
2. Consume the entitlement.
3. Record on the game application or server that the item has been granted.
4. Grant the user the entitled items.

Note:

A game **MUST** successfully consume the PlayStation™Network entitlement prior to granting any associated in-game item to the player.

There are two restrictions on the use of `PSVC` entitlements.

* The consumption (`consumeEntitlement`) call must be made from a game server and not from a game application
* All available counts of an entitlement must be consumed from PlayStation™Network servers at once.

Note:

When receiving a 5xx error or getting a timeout on an [Entitlements Web API Reference - Entitlements - consumeEntitlement](../Entitlements_WebAPI-Reference/0004.html) request, you must resubmit the request using the same `transactionId` value. This ensures that the operation is idempotent. See [Ensuring Resiliency](procedure-for-consuming-entitlements.html#entitlements-overview_2_1__entitlements-overview_2_1_5) for more details.

Consuming entitlements in this order can prevent a user being given extra rights they should not have and allows your application to still provide the granted right if a network or other system failure occurs. If an error during this process does occur, a later crosscheck between a user's items and their rights can confirm if the items were properly given. The processing flow for providing an entitlement or other privilege appears in the diagram below.

Entitlements Web API Implementation Example

The above diagram shows the dataflow for two different entitlement implementations. In the first dataflow, the application uses the NpEntitlementAccess Library (1) to call the PlayStation™Network directly. The network responds with the requested entitlement data (2), which the application can then consume and internally process.

In the second implementation, the application calls a game server (A), and the game server uses the Entitlement Web API to request entitlement data (B). The PlayStation™Network returns the entitlement data to the server (C), finally consuming the entitlement (D) and passing the data to the application (E).

While managing consumable entitlements in a game server is more complex, it is **required** for virtual currency (`PSVC`) entitlements and is best practice for other consumable (`PSCONS`) entitlements. This architecture is more resilient and allows your server to keep track of consumable totals.

Note:

It is possible to consume `PSCONS` entitlements though NpEntitlementAccess library.

Attempting to consume any other entitlement is prohibited.

Communication between the game server and PlayStation™Network server require using the Auth Web API. For more information on authorization and authentication, see [Auth Web API Overview](../Auth_WebAPI-Overview/__document_toc.html) and [Auth Web API Reference](../Auth_WebAPI-Reference/__document_toc.html). However, the NpEntitlementAccess Library does not require the Auth Web API.

# Procedure for Consuming Entitlements

This topic provides an example of the procedure you would follow to handle a consumable entitlement.

Consumable entitlements are managed on the PlayStation™Network server using the Entitlements Web API through the `consumeEntitlement` request. The NpEntitlementAccess library can be used to consume `PSCONS` and PlayStation®4 service entitlements from the application, and it is recommended to consume these entitlements using the game server to take advantage of the idempotent API. See [Ensuring Resiliency](procedure-for-consuming-entitlements.html#entitlements-overview_2_1__entitlements-overview_2_1_5) for more details.

Only unified entitlements with package types `PSVC` and `PSCONS` are consumable. PlayStation®4 service entitlements that are shared via the PlayStation™Store Delivered Content (PSSDC) mechanism are consumable if this is specified in the entitlement definition setup. Attempting to use the `consumeEntitlement` request for a non-consumable entitlement results in an error.

The API consumes counts from an entitlement by updating the `useCount` element stored within the entitlement. When the entitlement is later retrieved, `useCount` and `useLimit` reflect the updated values.

In the following example, a user has a `PSCONS` entitlement `WEAPONSPAK` with a `useCount` of 0 and a `useLimit` of 3. A call is made to consume 2 of the 3 counts and the response shows that 1 unit remains.

## Request

```
PUT entitlementBaseUrl/v2/users/me/entitlements/WEAPONSPAK_00001

{
    "transactionId": "b1aef5fe-aec0-462a-9872-8e6e6fe2b1d4",
    "useCount": 2
{
```

## Response

```
{
      "useLimit": 1
      "amountConsumed": 2,
}
```

Consumption with a `PSVC` entitlement is slightly different in order to support the requirement that all available units of the entitlement must be consumed from at once. Specifically, the `useCount` property is omitted, however, the response contains the number of counts consumed. In the following example, a user has 100 counts of the entitlement BIGGAMEBUCKS. All 100 are consumed in the example request.

## Request

```
PUT entitlementBaseUrl/v2/users/me/entitlements/BIGGAMEBUCKS_100

{
    "transactionId": " 43b4177e-e707-4b95-85c7-6c198dd2108e"
{
```

## Response

```
{
      "useLimit": 0
      "amountConsumed": 100,
}
```

## Ensuring Resiliency

To ensure that the `consumeEntitlement` request is idempotent, a unique `transactionId` value is passed in the request body. This value should be generated by your client application or game server and must be unique within the given user and entitlement. If a request times out or returns an HTTP error in the 5xx range, it should be retried after a short (1-2 second) delay and with the same `transactionId`. This ensures that the consume request is not processed by the server more than once.

For the highest resiliency, it is recommended that you persist the unique `transactionId` so that you can ensure completion of the `consumeEntitlement` request and credit the user's account upon recovery from a failure of your application server, game application, or any network component.

Note:

Failed `consumeEntitlement` requests must be retried with the same `transactionId` under the following circumstances:

(1) You receive an http 5xx error code/timeout.

(2) You receive a valid API response with error codes:

* 303F02 internal\_error
* 303F03 service\_unavailable

The request should be retried after a short (1-2 second) interval, until a status code other than 5xx is received. If the problem persists, there could be an issue with the PlayStation™Network, so please retry with exponential backoff in mind.

# Tracking Entitlement Changes

This topic highlights how the `useCount` and `useLimit` properties are affected by grants, revocations, and uses.

Granting a user an entitlement means that the user has purchased or otherwise obtained entitlement counts. Revoking an entitlement can occur with a refund or other removal. The following table describes the events that have occurred, and the effect that they have on the associated values.

| **Step** | **User Event** | **useLimit** | **useCount** | **Sum of Values** |
| --- | --- | --- | --- | --- |
| 1 | Granted 10 counts | 10 | 0 | 10 |
| 2 | Consumed 2 counts | 8 | 2 | 10 |
| 3 | Consumed 1 count | 7 | 3 | 10 |
| 4 | Revoked 7 counts. | 0 | 3 | 3 |

In the above sequence of steps, the values indicate:

1. The user is granted 10 counts and has not consumed any yet.
2. The user consumes 2 counts. `useLimit` is decremented by 2 and `useCount` is incremented by 2.
3. The user consumes 1 count. `useLimit` is decremented by 1 and `useCount` is incremented by 1.
4. The remaining 7 units are revoked (e.g., due to a refund). In contrast to a consume, only `useLimit` is decremented.

Keeping track of these values gives you the ability to closely track entitlement usage, and whether a user is entitled to further items.