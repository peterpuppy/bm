# TCS Cross-Platform Data Sharing Demo Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/TCS_Cross_Data_Transfer_Demo-Overview/sample-program.html

# Overview

This chapter provides an overview of the TCS cross-platform data sharing demo.

# About This Document

This document introduces a demo sample program that uses the PlayStation™ Network Title Cloud Storage (TCS) service to share data between a PlayStation®4 title and a PlayStation®5 title. This document explains the frameworks that can be used as reference when sharing data, the examples of implementations using these frameworks, and the points to note at each stage of the process.

We anticipate the following use cases for using TCS from PlayStation®4 with the PlayStation®4 Cross-Generation SDK:

* Transferring user-generated content (UGC) created on PlayStation®4 to a PlayStation®5 title
* Sharing data between a PlayStation®5 title and a PlayStation®4 title

# Main Features

The main features of the sample program are as follows:

* A feature for saving and loading data to and from TCS
* A feature for verifying the identity of local data and data on TCS by comparing hash values
* A feature for obtaining update timestamps for data on TCS
* A feature for deleting data on TCS

In addition, some important guidelines and best practices are indicated below.

* When data is shared between a PlayStation®4 title and a PlayStation®5 title, conflicts may occur when uploading data, as both devices are able to access TCS at the same time.
* Data uploads must be atomic.

# Sample Program

The following is the demo sample program introduced in this document. For details about sample programs included in the SDK, refer to [Sample Program Overview](../Sample-Overview/__document_toc.html).

**sample\_code\playstation\_network\demo\_tcs\_cross\_data\_transfer**

This sample uses TCS to share data between a PlayStation®4 title and a PlayStation®5 title.

# Reference Materials

For an overall explanation of TCS, refer to the following document.

* [Title Cloud Storage Service Overview](../../../WebAPI/latest/TCS-Overview/__document_toc.html)