# PlayStation™Network Cloud Streaming Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Cloud_Streaming-Overview/getting-started-with-streaming.html

# Before You Begin

This chapter provides an overview of the prerequisites you'll need before you can stream your PlayStation®5 applications from cloud streaming servers in development environments.

## Intended Audience

This document is intended for developers that want to stream PlayStation®5 applications on cloud streaming servers before submitting them for certification.

Review the prerequisites below before you begin streaming your PlayStation®5 applications.

## Prerequisites

Before you can begin streaming your PlayStation®5 applications, you must have the following:

* A TestKit or DevKit with system software 11.00 or higher
* Package files that can run on a PlayStation®5 Base TestKit set to *Release Mode*
* An account in the PlayStation™Network development environment

# Getting Started With Streaming

This topic provides an overview of the streaming process and streaming compatibility requirements for certification.

## Compatibility Requirements for Streaming PlayStation®5 Applications on SIE Cloud Streaming Servers

For the certification process, follow the requirements defined in [TRC R5017](https://game.develop.playstation.net/resources/documents/TRC/latest/TRC/R5017.html).

If unexpected issues occur only when streaming from cloud streaming servers, reach out to [DevNet private support](https://game.develop.playstation.net/support). Include the session log information to help investigate the issue. For more information, see [Troubleshooting](troubleshooting.html "This topic provides information and resolution steps for issues you may encounter while using the Cloud Streaming Preview application.").

## Streaming Process Overview

You can use the Cloud Streaming Preview application to stream PlayStation®5 applications on cloud streaming servers before submitting them for certification. This helps you identify any potential streaming related issues to ensure your game is ready for users to download and stream at launch.

The general workflow for streaming from cloud streaming servers is as follows:

1. Upload your application package (PSGD) and any additional content packages (PSAC) to the Package/Disc Management Tool (GEMS).
2. From GEMS, deploy the package to the cloud streaming server in the development environment.
3. Configure **Title Dev/Admin** roles for the accounts in the PlayStation™Network development environment.
4. On your DevKit or TestKit, start the game stream using the Cloud Streaming Preview application.

Cloud Streaming Workflow

For a more detailed explanation of these steps, see [Streaming Applications in Development Environments](testing-streaming-compatability.html "This topic describes the procedure for streaming applications on cloud streaming servers in development environments, including features, options, and settings that are available during streaming.").

## Reference Materials

The following links may assist you when streaming from cloud streaming servers:

* [GEMS tool](https://tools.partners.playstation.net/gems-tool)
* [Development Accounts tool](https://tools.partners.playstation.net/accntls/)
* [DevNet private support](https://game.develop.playstation.net/support)
* [Policies and Business Model Guidelines](https://learn.playstation.net/bundle/policies-and-business-model-guidelines/page/Publishing_Formats.html)
* [Package/Disc Management Tool (GEMS) Overview - Manage Cloud Streaming](../Package_Disc_Management_Tool_GEMS-Overview/streaming-management.html)
* [Development Accounts User's Guide](../Development_Accounts-Users_Guide/__document_toc.html)

## Related Information

In addition to this document, SIE also provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements. You can refer to the following release notes:

* [Release Notes - PlayStation™Network Cloud Streaming](../ReleaseNotes/PlayStation_Network-Cloud_Streaming-ReleaseNotes.html)

# Technical Specifications

This topic provides information on certain technical specifications required to use the Cloud Streaming Preview application.

## Application Operation Mode and Runtime Mode

The operation on cloud streaming servers is equivalent to that of a PlayStation®5 Base TestKit set to **Release Mode**. Thus, applications operate in **Base Mode** and run in **PS5 Base Mode**.

Additionally, you can enable low energy mode from **★Debug Settings** > **Game** > **Enable Low Energy Mode**. Applications that support low energy mode run in that mode on cloud streaming servers when you enable this setting.

For more information on application operation and runtime modes, see [Programming Startup Guide - Basic Information on Application Execution Environments](../Programming-Startup_Guide/ps5-basic-information-on-application-execution-environments.html).

## File Access

**Download Data Area**

The download data area is available for use in cloud streaming servers and sessions. You can delete downloaded data on the server side by using the *Delete Download Data* function of the Cloud Streaming Preview application.

For more information, see [AppContent Library Overview - Using the Library: Download Data Area](../AppContent-Overview/using-the-library-download-data-area.html).

**Temporary Data Area**

The temporary data area is available for use in cloud streaming servers. The temporary data area is lost between cloud streaming sessions.

For more information, see [AppContent Library Overview - Using the Library: Temporary Data Area](../AppContent-Overview/using-the-library-temporary-data-area.html).

**ContentSearch Library**

The ContentSearch Library allows you to search for images and videos captured during streaming. You can capture images and videos using the *Create* button, the ContentExport library, or the Share library.

All methods of image and video capturing have the following limitations on the number of files that can be saved:

* Still images: ten files
* Videos: one file

If you save more files than the limits above, the oldest file is deleted and the latest image/video is saved. Additionally, it is not possible to access data saved during different streaming sessions as data is stored in the volatile area of the cloud streaming server.

For related development support features, see [ContentSearch Library Overview - Reference Information - Development Support Features](../ContentSearch-Overview/ps5-development-support-features.html).

## Application State Transitions

The hardware resources available for PlayStation®5 applications on cloud streaming servers are equivalent to the retail units which run in *Base mode*.

For more information, see [Programming Startup Guide - Resources That Can Be Used by Applications](../Programming-Startup_Guide/resources-that-can-be-used-by-applications.html).

**Application states when streaming:**

Cloud streaming supports the following application states:

* Foreground execution
* Background execution

For more information, see [Programming Startup Guide - Application State Transitions](../Programming-Startup_Guide/application-state-transitions.html).

## Networking

If you would like your game servers to detect whether the application is running from cloud streaming servers, file a ticket with [DevNet private support](https://game.develop.playstation.net/support).

## Limitations on Cloud Streaming Servers

The following features are not supported during cloud streaming:

* PlayStation®VR2
* Camera
* Keyboard
* Mouse
* PlayStation®5 Wi-Fi AP (NetCtlAp Library)
* Remote Play
* Share Play
* Share Screen
* Importing PlayStation®4 save data
* Broadcast

## Network Latency and Global Availability

SIE operates cloud streaming servers across Japan, North America, and Europe to support low-latency, high-quality cloud gaming. For consumer-facing cloud gaming, SIE supports network latency up to 80ms RTT. With SIE's investments in streaming technology and data centers, the overwhelming majority of cloud gaming sessions have minimal network latency.

Compatibility and functional game testing focuses on the game rather than the cloud gaming experience. These tests can tolerate network latency up to 140ms RTT, enabling developers outside Japan, North America, and Europe to validate game functionality. However, if the game contains latency-sensitive elements, an upper bound of 80ms RTT should be used for those tests to ensure functionality is accurately validated.

Average RTTs from various cities to SIE data centers are listed below; however, your actual latency may vary. For the best results, use a wired landline connection (DSL, cable, or fiber). Cellular, 5G, or satellite internet connections may work but typically have higher latency.

|  |  |  |  |
| --- | --- | --- | --- |
| **Continent** | **Country/Region** | **City** | **RTT (ms)** |
| Africa | Algeria | Algiers | 31 |
| Africa | Egypt | Cairo | 52 |
| Africa | Ghana | Accra | 96 |
| Africa | Kenya | Nairobi | 164 |
| Africa | Morocco | Fez | 52 |
| Africa | Nigeria | Lagos | 97 |
| Africa | South Africa | Cape Town | 143 |
| Africa | South Africa | Johannesburg | 157 |
| Africa | Tanzania | Dares Salaam | 125 |
| Africa | Tunisia | Tunis | 29 |
| Asia | Bangladesh | Dhaka | 114 |
| Asia | Cambodia | Phnom Penh | 86 |
| Asia | China | Shanghai | 47 |
| Asia | China | Shenzhen | 162 |
| Asia | Cyprus | Limassol | 59 |
| Asia | Georgia | Tbilisi | 60 |
| Asia | Hong Kong | Hong Kong | 48 |
| Asia | India | Bangalore | 138 |
| Asia | India | Chennai | 103 |
| Asia | India | New Delhi | 140 |
| Asia | India | Pune | 124 |
| Asia | Indonesia | Jakarta | 78 |
| Asia | Kazakhstan | Karaganda | 91 |
| Asia | Lebanon | Beirut | 54 |
| Asia | Malaysia | Malaysia | 79 |
| Asia | Pakistan | Lahore | 124 |
| Asia | Philippines | Manila | 70 |
| Asia | Saudi Arabia | Riyadh | 72 |
| Asia | Singapore | Singapore | 75 |
| Asia | South Korea | Seoul | 33 |
| Asia | Taiwan | Taipei | 33 |
| Asia | Thailand | Bangkok | 99 |
| Asia | Turkey | Ankara | 49 |
| Asia | Turkey | Istanbul | 35 |
| Asia | United Arab Emirates | Dubai | 103 |
| Asia | Vietnam | Hanoi | 110 |
| Asia | Vietnam | Ho Chi Minh City | 76 |
| Oceania | Australia | Adelaide | 211 |
| Oceania | Australia | Brisbane | 130 |
| Oceania | Australia | Canberra | 182 |
| Oceania | Australia | Melbourne | 144 |
| Oceania | Australia | Perth | 128 |
| Oceania | Australia | Sydney | 114 |
| Oceania | New Zealand | Auckland | 190 |
| South America | Argentina | Buenos Aires | 141 |
| South America | Brazil | Sao Paulo | 120 |
| South America | Chile | Santiago | 134 |
| South America | Colombia | Bogota | 77 |
| South America | Ecuador | Quito | 80 |
| South America | Peru | Lima | 89 |
| South America | Suriname | Paramaribo | 86 |
| South America | Uruguay | Montevideo | 144 |
| South America | Venezuela | Caracas | 70 |