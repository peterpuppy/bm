# NpWebApi2 Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Overview/feature-for-receiving-push-events.html

# Feature Description

This library mainly provides the following two features:

* Feature for calling PlayStation™Network Web APIs
* Feature for receiving Push events

# Feature for Calling PlayStation™Network Web APIs

To use PlayStation™Network Web APIs, you must obtain an access token. By having the NpWebApi2 library carry out the process of obtaining the access token within the library, applications that use the NpWebApi2 library are able to concentrate on using the features of Web APIs without needing to explicitly handle the access token.

When using the NpWebApi2 library to call Web APIs, instead of specifying the entire URL that points to the Web API endpoint, specify strings called "API groups" that identify the service, and the resource path (and query string), which is part of the URL, as parameters. The NpWebApi2 library determines the URL to call based on the specifications described in the "HTTP Methods and URI Specifications" section of the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) Document.

In addition, the NpWebApi2 library will automatically generate the necessary request headers for Web APIs that require them, or they can be specified by the application.

Information about the API groups that the application should specify when calling the Web APIs can be found in the "API Group Strings" section of the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document. In addition, information about resource paths, request headers, and other parameters that should be specified for each API can be found in the reference documentation for each Web API.

In the event that an error occurs on the server after calling the Web API, the NpWebApi2 library also provides a feature for mapping the server error code (decimal number) in the Json object returned by the server to an error code (hexadecimal number starting with 0x82) that adheres to the same error code system as other SDK libraries. The error code will be returned as a return value of `sceNpWebApi2SendRequest()`.

Web APIs called by the NpWebApi2 library only support synchronous calls.

# Feature for Receiving Push Events

The feature for receiving Push events receives event notifications originating from the PlayStation™Network Web API server.

Types of Push events are identified by their data type.

Whether the Push event is a normal Push event or an "order-guaranteed Push event" is determined for each data type. The function that prepares to receive the Push event and the method of reception differ between a normal Push event and an "order-guaranteed Push event". For details, refer to the "Using the Library" chapter. Information about which data type and method to use can be found in the "Order Guaranteed" section of the reference documentation for each Web API. If the Order Guaranteed section states "No", it is a normal Push event. If the Order Guaranteed section states "Yes", it is an "order-guaranteed Push event".

"Order-guaranteed Push events" provide order guarantees to Push events that would otherwise lack this feature. The order information is added to the push event by the Web API server and received by the NpWebApi2 library via management structures called "Push contexts". If the order of a Push event ends up being switched as it passes over the network, the Push context returns it to the correct order and notifies the application. Additionally, if some Push events are lost while traveling over the network, the detection of lacking Push events is notified to the application so that the application can respond to it. The level at which order management is performed and how the application responds to the lack of an event differs depending on the Web API. The details are described in the documentation for each relevant Web API.

Depending on the data type, an NP service name or NP service label may need to be specified. Push events for data types that require an NP service name to be specified are Push events for titles that are grouped by title. For service names that should be specified, refer to the "NP Service Name Required for Receiving" section in the reference for each Web API. Specify an NP service label in order to separately use multiple contexts with the same NP service. Specify the NP service label that was set up upon submitting the request for PlayStation™Network service usage.