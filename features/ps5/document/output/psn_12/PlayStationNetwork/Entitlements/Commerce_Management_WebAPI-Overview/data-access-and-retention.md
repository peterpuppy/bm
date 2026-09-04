# Commerce Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Commerce_Management_WebAPI-Overview/data-access-and-retention.html

# Using the Commerce Management Web API

This chapter provides information on how to use the Commerce Management Web API.

The Commerce Management Web API lets you generate revoke and reinstate reports. By actively generating and reporting data, SIE can assist you with acting on chargebacks, refunds, and chargeback reversals to protect against cross-commerce, cross-progression, and shared wallet exploits.

## Prerequisites

Before using the Commerce Management Web API, you must obtain an access and ID token. For details, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

When requesting the OAuth token, ensure you are passing in the parameter `token_format=jwt`.

## Onboarding to Commerce Management Web API

To onboard to the Commerce Management Web API, contact your technical account manager to open a DevNet ticket to start the onboarding discussion. SIE presents a policy introduction, confirms your revoke and reinstate plan, and addresses any general questions you may have.

# Event Streams

This topic provides information on how to configure event streams, and how to release, consume, and report event stream data.

Event streams provide you with information on chargeback, refund, chargeback reversal and subscription events related to your application. You can consume these streams and report event data back to SIE, allowing SIE to assist you with acting on chargebacks, refunds, reversals and subscription events.

## Configuring Event Streams

After SIE [confirms your revoke and reinstate plan and approves your event stream data](using-the-commerce-management-web-api.html#commerce-management-web-api-overview_1__commerce-management-web-api-overview_1_2), you can configure streams in your development environment (sp-int).

To configure your event streams in your development environment:

1. Configure the back office server product. SIE confirms your IP addresses and client ID allowlisting specifications.
2. Confirm allowlisting of the notification URL with SIE. See [Event Push](event-push.html "This topic provides information on how to configure Event Push for subscription events and verify signed delivery from SIE.") for more information.
3. Confirm Title IDs with SIE.
4. Create title streams and add titles. SIE works with you to validate event data and ensure the integration functions as expected.

An example list of available streams after configuration:

Available Streams Example

This configuration has three levels of streams with event data:

* **Partner level --** Event data for all titles and event types. For example: "/partner-events/PARTNER1/PARTNER1"
* **Title level --** Event data for all event types. For example: "/partner-events/PARTNER1/TITLE\_STREAM"
* **Event type level --** Event data per event type. For example: "/partner-events/PARTNER1/REFUND-PARTNER1-TITLE\_STREAM"

## Releasing to a Production Environment

When you are satisfied with your event stream integration, you can release it to a production environment (NP).

To release your integration to production:

1. Create your production environment (NP).
2. Create title streams and add titles.
3. Confirm a go-live date with SIE to populate your production environment. SIE populates your production environment with production data on the agreed date and works with you to troubleshoot access or data issues.

## Consuming Events from a Stream

Use `startPosition` and `fetchSize` to consume events from a stream.

* `startPosition` - Required parameter indicating the starting position to read from within the stream. If a downstream system crashes while consuming data or loses the database requiring a recovery from data loss, it is possible to restart at an earlier `startPosition`.
* `fetchSize` - Optional parameter indicating the number of events to read from the stream. There is a maximum of 500 events in a single fetch.

You can start consuming events from anywhere in the stream and go back in time up to a retention period of three years.

For events that cannot be handled or return an error, you can either stop the process to fix it and then resume consumption, or you can store them on a server for later review.

## Reporting Event Data

After your stream integration is live, create a `postEventFeedback` reporting loop to send event data back to SIE.

To set up the `postEventFeedback` reporting loop:

1. Connect the `postEventFeedback` reporting loop using the Commerce Management Web API.
2. Report your matching and actioning of event data.
3. Confirm a go-live date with SIE for the `postEventFeedback` reporting loop.

SIE recommends that you pull your event data once a day and report the success and failures for each event type using `postEventFeedback`. Include reasons for event failures to help identify solutions.

# Data Access and Retention

This topic provides information on SIE's data access and retention policy with data gathered from the Commerce Management Web API.

The Commerce Management Web API data that is initially available pertains to refunds, chargebacks, and chargeback reversals for the purpose of entitlement alignment. Any future events determined on a partner-by-partner basis are subject to additional review for proper data sharing agreement compliance.

SIE retains API data for three years and one day based on the `timestamp` field for the purpose of entitlement alignment. After three years and one day, event data is removed from your event streams. If you wish to review event data that has been removed from an event stream, you must open a DevNet ticket requesting assistance with the following information:

* The date-range of the event data pull request
* Game title
* `titleId`(s)
* A reason for the request.

Once you create the DevNet ticket, a Commerce Management Web API support team member provides the requested data in a password-protected Microsoft Excel file. This retainment period is subject to change with sufficient notice and is determined by SIE's observation of partner needs.

# Event Push

This topic provides information on how to configure Event Push for subscription events and verify signed delivery from SIE.

Event Push enables you to receive push notifications for user subscription state change events, for example, when a user renews or cancels their subscription, or when a subscription is in dunning.

Note: Currently, Event Push only supports the `SUBSCRIPTION` event type.

## Configuring Event Push

Before configuring Event Push, [ensure that you have on-boarded to the Commerce Management Web API](using-the-commerce-management-web-api.html#commerce-management-web-api-overview_1__commerce-management-web-api-overview_1_2) and received your partner name and OAuth credentials for API access.

To configure and use Event Push, do the following:

1. Create a title stream using [Commerce Management Web API Reference - Streams - createStream](../Commerce_Management_WebAPI-Reference/0008.html).
2. Register the notification URL where subscription events will be delivered using [Commerce Management Web API Reference - Titles - registerNotificationUrl](../Commerce_Management_WebAPI-Reference/0010.html). For example, `https://some.subdomain.partnerdomain.com/notify`. Events are based on the `subscription` event type. To receive subscription events, SIE must allowlist the domain of the notification URL. For example, `.partnerdomain.com` in the example above.
3. Associate one or more title IDs to the stream using [Commerce Management Web API Reference - Titles - addTitle](../Commerce_Management_WebAPI-Reference/0012.html).

Once configured, [SIE delivers subscription state change events to your registered notification URL as signed requests](event-push.html#event-push__section_cwx_2gy_q3c). For payload specification, see [Commerce Management Web API Reference](../Commerce_Management_WebAPI-Reference/__document_toc.html).

## Standardized Secure Web-hook Delivery

SIE has created a secure delivery environment to ensure a standard verification process for all partners.

SIE posts JSON over HTTPS to your registered notification URL, signing the `Host`, `X-Psn-Event-Id`, `X-Psn-Timestamp`, and `Digest` headers using an SIE private key. Once received, your endpoint should verify the signature, timestamp, and event ID using an SIE public key and return an HTTP 2xx if successful. Reject `X-Psn-Timestamp` if it is older than five minutes and reject `X-Psn-Event-Id` if it has already been processed. If the same ID is received again (for example, due to a retry), ignore it.

Failure to deliver the 2xx response triggers a retry. If retries are exhausted, the event is sent to Dead Letter Queue (DLQ).

**Example Signed Request**

```
POST /partner/webhook HTTP/1.1
Host: partner.example.com
Content-Type: application/json
X-Psn-Event-Id: 169856dd-6aa3-4c00-a043-4157647b1c98
X-Psn-Timestamp: 2025-11-12T21:17:26.777Z
Digest: SHA-256=U9b+5dm9xP02wxZrJ0X72kGc5CZXChpO0LrThR5T2Jk=
X-Psn-Alg: rsa-pss-sha256
X-Psn-Key-Id: kid-001
X-Psn-Signature: MEYCIQDv4DxM...<base64 signature>...
```

**Example Body**

```
{
  "id": "169856dd-6aa3-4c00-a043-4157647b1c98",
  "eventVersion": 1,
  "eventSource": "NP_EVENTS_DATA_FEED",
  "eventType": "SUBSCRIPTION",
  "eventDomain": "SUBSCRIPTION",
  "timestamp": "2025-11-12 21:17:26.777000",
  "body": {
    ...
  }
}
```

Signing Workflow

**Event Redelivery Support**

SIE can redeliver failed events if requested. Only events less than 14 days old are eligible for redelivery.

If events are older than 14 days, you can reconcile using the event retrieval API and filtering to the appropriate date range. For more information, see [Commerce Management Web API Reference - Stream Events - getStreamEventsV2](../Commerce_Management_WebAPI-Reference/0003.html).