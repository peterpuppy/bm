# Title Cloud Storage Service Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS-Overview/notes-on-server-load-and-request-execution-rates.html

# Notes

This topic explains points to note when using the Title Cloud Storage service.

# Notes on Server Load and Request Execution Rates

There is a risk that an application with a high request execution rate could impose load on the server that is too much for it handle. Pay attention to the information provided below when designing the specifications for your application and when implementing it. (Consult with SIE if you are unsure about a decision regarding the design of specifications or implementation.)

Note that, if excessive access occurs, SIE may stop service for the corresponding application without notice. Take care, in particular, with large-scale applications - the larger, the greater the load.

## Send Information Collectively Whenever Possible

When using a TCS variable to record the number of defeated enemies, for example, do not communicate with the server every time an enemy is defeated. Instead, select an appropriate time, such as at the end of each stage, to send the information in collected batches to the server.

## Limit the Frequency with Which TCS Data and Variables Concerning the "anyone" User Are Updated

The TCS server is designed in such a way that the concentration of processing burden regarding "anyone" users cannot be avoided. Since it can easily cause excessive loads for servers, minimize access to the TCS data and variables - particularly update-related access - by the "anyone" user.

Additionally, there are cases in which an equivalent feature can be implemented by using the Leaderboards service or another service, instead of using the "anyone" user. Keep these points in consideration, along with all other points concerning server load.

## Prevent Continual Reloads and Votes

When implementing the reload feature, prevent a user interface where the user can repeat reloads. For example, do not adopt a specification where the continued pressing of a button means continued reloading. Also, avoid specifications that encourage the user to perform reloads - such as where the reference count is increased when the user downloads the same data repeatedly. Record the time lapse since the previous download in the save data, for example, and adopt a specification where unnecessary downloads cannot be repeated.

## Do Not Obtain Information until Needed

If at all possible, only obtain information that is displayed to the user in response to an operation by them after that operation has been performed. To the extent possible, please avoid designs where information that does not get displayed until the option menu is opened, or until the user scrolls down, is obtained before that operation.

## Directly Obtain Information of the Other Party by P2P Communication

Obtain the information of the party with which you are performing P2P communication directly from the other party wherever possible.

## Communication Frequency

The frequency of communication with the server should not exceed around once in 5 minutes. (Processing that transfers a single instance of TCS data divided among multiple downloads count as once.) Communication of the TCS variable 8 times is equivalent to communication of TCS data once. It is not a problem if the frequency is temporarily increased when a user performs engages in special behavior such as consecutive reloads; however, avoid a specification where the user is encouraged to act in such a way. For the API call rate limits for each API feature, refer to the call rate limits provided for them in [Title Cloud Storage Web API Reference](../TCS_WebAPI-Reference/__document_toc.html).

## Minimize the Number of Communication Processes to Execute at Once

When executing multiple communication processes at once, make sure that the number of processes does not exceed 8 by making good use of supplementary data for TCS data and API features that read multiple users/slots. An API related to friends is also provided for reading the TCS variables or supplementary data in a single process.

In a design where user operation is blocked until multiple processes end, an extremely long waiting time may occur, depending on the network state, rendering smooth operation impossible.

## Be Careful When Specifying Friends

The maximum number of friends is 2000. When specifying friends and reading slots, it will take an extremely long time if there are many friends, and the load will also increase.

Note that information of slots that haven't been configured or slots that have been deleted won't be included in the response. This means that when slot information can't be read, you won't be able to know if the read failed because the specified person is not a friend or if the slot is empty.

In this way, care is required when specifying friends. It may be possible to resolve the above problems if the friend list is obtained in advance and a slot is read by user specification.

## Handling "Currently Undergoing Maintenance"

If there is excessive accessing of TCS servers from an application, SIE may stop service provision for that application without notice. In that case, an error indicating that the TCS server is undergoing maintenance will be returned to the application. Please implement an appropriate way of handling this error.

Note that Private Support will contact the publisher after service has been stopped. Please be aware that you may be asked to rectify the excessive access frequency or to make alterations to application procedures upon the resumption of service.

# Notes on Security

## Data Security

The Title Cloud Storage service is not designed with privacy protection in mind. Do not store information such as users' credit card numbers, telephone numbers, addresses, or passwords for various services in title cloud storage.

Although it is unlikely that a server would be spoofed because server authentication is performed on the client side, data set to the server could be obtained using a spoofed PC, for example. Make sure data that should not be seen by the user is also not stored in title cloud storage.

# Other Notes

## Danger of a Deadlock

When a TCS variable is improperly used like in a semaphore, a deadlock may occur when the application hangs up, and it may be impossible to recover from this deadlock, even when the application is restarted. Design your application so that it can be continued even if the TCS variable or TCS data becomes invalid in terms of application specifications.

## Features That Cannot Be Used from the Title Cloud Storage Tool

The features provided below cannot be used from the Title Cloud Storage Tool. Use TCS Management features to use these features.

* Uploading data for distribution to a production server
* Uploading TCS data for the "anyone" user

## Limitations of the Title Cloud Storage Tool

The following features cannot currently be used by titles that have been migrated to the PlayStation® environments of the Sandbox network architecture:

* Operational history
* Publishing per slot