# Commerce Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Commerce_Management_WebAPI-Overview/faq.html

# Frequently Asked Questions

This chapter includes frequently asked questions you may encounter when implementing the Commerce Management Web API.

## Can I increase the 10 times per five minute rate limit for our service?

The documentation states a recommended call rate for the stream. Rate limits are configurable; however, this is subject to change.

## Can the Commerce Management Web API only be used from a PlayStation®5 Back Office Server product type?

The back office server product can be created using either PlayStation®4 or PlayStation®5 DevNet accounts. The API works based on the `clientId`/`clientSecret` defined in DevNet, so the server only requires a valid API authorization and IP allowlisting to make the call.

## Can I add new Title IDs to Commerce Management Web API streams after completing the onboarding process?

Yes, to add new Title IDs to existing streams, open a DevNet ticket with SIE to verify the Title IDs before they are added.

## Does the Commerce Management Web API provide a testing environment during the onboarding process?

The data listed in the development environment (sp-int) is manufactured data that can't be linked to any accounts for PlayStation™Network on the Partner's side.

The purpose of the development environment is to make sure that streams are formatted correctly with the titles and event data you request. You can test revoke and reinstate actions on data listed within streams in your production environment (NP).

## How are event streams configured?

After the onboarding process, you can create your streams and add game Title IDs to the streams per your requirements. For example, if the requirement is to process data for a specific game title, you can create a title stream for the individual game title and add the relevant game Title IDs to the stream. This newly created stream contains data only for the added game Title IDs. You must create the stream and add the game Title IDs to the stream to consume the data.

## How do I obtain my Partner Name?

SIE creates and provides your partner name during the onboarding process.

## How should I construct base URL paths?

The Partner should always use "s2s" endpoint at the URL path's start. If the Partner uses other endpoints such as the "ps5" endpoint, their connection attempts to access the Commerce Management Web API will be denied.

## How do I handle 50X series or any network-related errors while reacting to event data or sending back postEventFeedback data to SIE?

If you encounter an error for more than two hours, open a DevNet ticket with a summary of the error you're experiencing, along with the error message.

## Should my partner name be in all caps or lower case?

After SIE provides you with your partner name, ensure it is in all upper case when adding URL paths, for example, `PARTNER_NAME`.

## Once the streams are configured, can I update the access to use a different clientId?

Yes, provide SIE with the new `clientId` to update your configuration.

## With the bearer token/clientId secret, am I able to get event streams across different titles?

Yes, SIE can configure your access with the `clientId` across multiple streams, as well as limit the access per stream/title.

## What is the cadence in which we should be calling the Commerce Management Web API?

The cadence to call the Commerce Management Web API should be daily, which entails the Partner retrieving, processing, and sending back their postEventFeedback event data to SIE. The Partner should be pulling their event data once a day and sending their postEventFeedback reporting data at the end of the same day that the event data was pulled. If the Partner cannot follow the advised cadence, they should inform the SIE onboarding team to agree upon a decided cadence that works for both parties.

## Can I populate my root stream with event data using addTitle and getstreamEventsV2 for new game titles after the onboarding process is completed?

No. Commerce Management Web API onboarding support teams link `titleIds` for new games to your root stream for your team to reference.

## Can I populate auto-generated event streams such as refunds, chargebacks, and chargeback reversals, with additional game titleIds once created?

No, you cannot add additional game `titleIds` to refund, chargeback, or chargeback reversal streams directly.

Use `addTitleId` to add `titleIds` to streams created using `createStream`. Additional `titleIds` you add to streams are reflected in refund, chargeback, and chargeback reversal streams automatically.

## What does it mean when Client\_Transaction\_Id (CTID) starts with a "PSN:" prefix?

CTIDs are prefixed with "PSN:" when you send consumption requests without a CTID.