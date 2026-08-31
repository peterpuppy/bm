# Commerce Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Commerce_Management_WebAPI-Overview/about-the-commerce-management-web-api.html

# About the Commerce Management Web API

This chapter provides basic information on the Commerce Management Web API.

The Commerce Management Web API lets you pull both revoke and reinstate reports, required data, and provides uniform standards that allow you to subscribe to near real-time PlayStation™Network data by event type. Event types include chargebacks, refunds, chargeback reversals and subscriptions. Event payloads are qualified by these event types, allowing SIE to produce new events on your behalf.

To assist with the revoking process, the Commerce Management Web API includes the `clientTransactionID` and `amountConsumed` data fields within the `additionalData` section of `getStreamEventsV2`. `clientTransactionID` provides an exact matching process for which entitlement consumption events are linked to the chargeback and refund events sent by the Commerce Management Web API. To support this new data field, store `clientTransactionID` on the client side when making consumption requests to PlayStation™Network for future reference. The `amountConsumed` data field indicates the amount of entitlement the player has consumed. You must enable `getStreamEventsV2` to incorporate these new data fields within the revoking process.

Pass `clientTransactionID` using `consumeEntitlement`. If you do not pass a `clientTransactionID` , SIE creates one on your behalf.

## Main Features

Back office servers (servers used mainly for development and operation support) can use the Commerce Management Web API to:

* Retrieve all streams
* Retrieve all events from a partner, title, or event level stream
* Create title streams
* List, create, and delete titles in a stream
* Configure title streams, register notification url and receive Subscription State Change events
* Report success and or failure of actions on consumed events to SIE

## Reference Materials

* For information on required permissions to use this API, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).
* For general information on the Commerce Management Web API, including required headers, query parameters, structures returned, and errors, see [Commerce Management Web API Reference](../Commerce_Management_WebAPI-Reference/__document_toc.html).
* For information on commerce and the PlayStation™Store, see [PlayStation™Network Commerce Service Overview](../../../SDK/latest/PSN_Commerce_Service-Overview/__document_toc.html).

## Release Notes

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - Commerce Management Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-Commerce_Management_WebAPI-ReleaseNotes.html)

## Contact Us

If you have any further questions, open a DevNet ticket.