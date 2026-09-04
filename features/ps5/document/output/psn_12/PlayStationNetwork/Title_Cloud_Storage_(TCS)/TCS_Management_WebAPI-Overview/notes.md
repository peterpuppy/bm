# Title Cloud Storage Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS_Management_WebAPI-Overview/notes.html

# Notes

This topic explains points to note when using the Title Cloud Storage Management Web API.

## Rate Limits

For the Title Cloud Storage Management Web API, each Client ID and each NP Service Label will count toward the access rate.

## Conditions for Use

The Title Cloud Storage Management Web API is provided for the purpose of complementing the use of the title cloud storage service by the target application. Use the Web API within the same scope that the target application uses the title cloud storage system.

**Prohibitions**

Avoid using the Title Cloud Storage Management API for the following purposes in particular:

* Reading and writing of data not used by the target application
* Reading and writing of data for use by other applications
* Saving of personally identifying information, such as users' credit card numbers, telephone numbers, and addresses
* Saving of passwords and secret keys for various services
* Transferring or exchanging paid-for content.

## Processing Requiring User Consent

User consent must be obtained in advance to carry out the following processing using the Title Cloud Storage Management Web API:

* Correcting TCS variable/TCS data with an abnormal value or a value set by an illegal operation

## Responsibility for Results of Use

The licensee is fully responsible in the event that any of the following results occur due to the use of the Title Cloud Storage Management Web API:

* Creation, change, and deletion of data stored on the server and any effects these actions may have on the application
* Any effects on users using the target application (provide appropriate user support)

SIE shall not be responsible for any of the above, including the responsibility to restore data stored on the server.

## Termination of Use

SIE may take any measures, as it sees fit without prior notice, including terminating the use of the Title Cloud Storage Management Web API, if the licensee acts as follows:

* Causes a server overload
* Violates any of the above conditions, prohibitions, requirements, or responsibilities
* Is inappropriate/insufficient in providing user support regarding the title cloud storage
* Is otherwise not using the Title Cloud Storage Management Web API in an appropriate manner

In such a case, SIE may notify users that there is a problem with the title cloud storage of the target application.