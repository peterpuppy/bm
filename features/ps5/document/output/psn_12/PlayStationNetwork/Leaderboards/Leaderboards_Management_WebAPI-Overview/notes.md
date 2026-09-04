# Leaderboards Management Web API Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Leaderboards_Management_WebAPI-Overview/notes.html

# Notes

This topic explains the points to note when using the Leaderboards Management Web API.

# Frequency Restrictions

With the Leaderboards Management Web API, access frequency is counted on both per-client ID and per-NP service label bases.

# Conditions for Use

The Leaderboards Management Web API is provided for the purpose of complementing the use of the Leaderboards service by the target application. Therefore, this API must be used within the scope of the target application's use of the Leaderboards service.

Read/write of ranking information that is not used by the target application and read/write of ranking information used by another application are prohibited.

# Processing Requiring User Consent

User consent must be obtained in advance to carry out the following operations using the Leaderboards Management Web API.

* Deleting a score with an abnormal value or a value set by illegal operation

# Responsibility for Results of Use

The licensee is fully responsible for the following results occurring due to the use of the Leaderboards Management Web API.

* Creation, change, and deletion of ranking information stored on the server and any effects these actions may have on the application
* Any effects on users using the target application (provide appropriate user support)

SIE shall not be responsible for any of the above, including the responsibility to restore ranking information stored on the server.

# Termination of Use

SIE may take any measures as it sees fit without prior notice, including terminating the use of the Leaderboards Management Web API, if the licensee acts as follows.

* Causes a server overload
* Violates any of the above points to note
* Is inappropriate/insufficient in providing user support regarding ranking information
* Is otherwise not using the Leaderboards Management Web API in an appropriate manner

In such a case, SIE may notify users that there is a problem with the ranking information of the target application.