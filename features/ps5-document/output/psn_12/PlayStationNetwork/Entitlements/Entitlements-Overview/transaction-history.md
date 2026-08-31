# Entitlements Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Entitlements-Overview/transaction-history.html

# Transaction History

This chapter provides information on how to retrieve and use the transaction history a user's entitlements.

The Entitlements Web API provides the ability to retrieve the history of consume operations for a given user and entitlement. This is useful to help investigate user complaints surrounding consumable entitlements. Use the Transaction History API by back-office customer support systems and not for real-time handling of consumables. For details, see the [Entitlements Web API Reference](../Entitlements_WebAPI-Reference/__document_toc.html).

PlayStation™Network reserves the right to prune transaction records that are more than two years old.

# Retrieving a User's Transaction History

You can retrieve the consumption history of a user's entitlement, or a single transaction for a given entitlement.

## Retrieving the Transaction History for a User's Consumable Entitlement

To retrieve a set of entitlements held by the current user, use [Entitlements Web API Reference - Entitlements - listEntitlements](../Entitlements_WebAPI-Reference/0002.html).

**Example: Obtaining Transaction History**

In this example, we retrieve consumption history for the user with `accountId` 1234's `WEAPONSPAK_00001` entitlement.

The response document lists the four transactions associated with this entitlement in reverse chronological order, so read them bottom-up. The transactions in this example are the same as the ones in the example in the previous section, [Tracking Entitlement Changes](tracking-entitlement-changes.html "This topic highlights how the useCount and useLimit properties are affected by grants, revocations, and uses.").

**Request**

```
GET entitlementBaseUrl/v2/users/1234/entitlements/WEAPONSPAK_00001/transactions
```

**Response**

```
{
              "transactions": [ {
              "date" : "2019-03-01T11:04:22.000+00:00",
              "count" : 7,
              "useCount" : 3,
              "useLimit" : 0,
              "operation" : "REVOKE",
              "transactionId" : "0c809765-8f80-4ab3-ba04-a3c3fb5a60af"
              
              },
              "date" : "2019-02-25T10:07:02.000+00:00",
              "count" : 1,
              "useCount" : 3,
              "useLimit" : 7,
              "operation" : "CONSUME",
              "transactionId" : "f3b2fcf2-c443-4a01-b4bc-21edb7751ad0"
              
              },
              "date" : "2019-02-25T09:22:01.000+00:00",
              "count" : 2,
              "useCount" : 2,
              "useLimit" : 8,
              "operation" : "CONSUME",
              "transactionId" : "40764532-ebda-437d-965c-6ef984725c25"
              }, {
              "date" : "2019-02-23T04:56:07.000+00:00",
              "count" : 10,
              "useCount" : 0,
              "useLimit" : 10,
              "operation" : "GRANT",
              "transactionId" : "0e06137b-f1aa-45ed-85f8-f18ec36eb108"
              } ]
}
```

## Paging and Limit

The caller may limit the number of responses received at one time by setting the `limit` query parameter. By default, its value is 100. If more than `limit` transactions are available, only the most recent `limit` is returned in the response and added to the response body is a property, `previous`, that contains a value that can be passed to the next call as the query parameter, `before`.

Note that we use the names ***previous*** and ***before*** since we are paging backwards in time.

## Retrieving the Result of a Single Transaction

In this example, we request only a specific transaction for the `WEAPONSPAK_00001` entitlement. It correlates with the third transaction (in time order) in the example above.

**Request**

```
GET entitlementBaseUrl/v2/users/1234/entitlements/WEAPONSPAK_00001/transactions/f3b2fcf2-c443-4a01-b4bc-21edb7751ad0"
```

**Response**

```
{
                  "date" : "2019-02-25T10:07:02.000+00:00",
                  "count" : 1,
                  "useCount" : 3,
                  "useLimit" : 7,
                  "operation" : "CONSUME",
                  "transactionId" : "f3b2fcf2-c443-4a01-b4bc-21edb7751ad0"
}
```