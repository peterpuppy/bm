# Title Cloud Storage Service Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/TCS-Overview/reference-information.html

# Reference Information

This topic explains the differences between Title Cloud Storage and the legacy storage service.

The main differences between the Title Cloud Storage service versus the old Title User Storage (TUS) service and the Title Small Storage (TSS) service are as follows:

* The standard NpWebApi2/NpCppWebApi libraries and the Title Cloud Storage Web API can now be used, instead of the dedicated NpTus/NpTss libraries
* The Title User Storage service and the Title Small Storage service have been integrated into one service: the Title Cloud Storage service
* As a result of this integration, tools, management APIs, and other features have also been integrated
* The virtual user concept of the TUS has been revised into the concept of "anyone" users

Note that the storage used by the Title Cloud Storage service, the Title User Storage service, and the Title Small Storage service is independent. Be aware that it is not possible to inherit saved data from the older services or to share saved data among the services.