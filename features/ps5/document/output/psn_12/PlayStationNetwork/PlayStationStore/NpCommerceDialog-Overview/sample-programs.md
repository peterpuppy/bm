# NpCommerceDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCommerceDialog-Overview/sample-programs.html

# Library Overview

# Purpose and Characteristics

The NpCommerceDialog library provides features to purchase, download, and install products provided from the PlayStation™Store Title Store.

The NpCommerceDialog library is provided as a library including user interface display. When the NpCommerceDialog library is called, the product list and product details obtained from the PlayStation™Network servers using the In-Game Catalog Web API are proposed to the user in a dialog format, and purchase/download processing is carried out pursuant to user response.

A feature is also provided to only carry out download processing (for already-purchased products). It is also possible to purchase and download multiple products at the same time. Further, a feature to add funds to the user's wallet is also provided within purchase processing.

# Main Features

This topic lists the main features provided by the NpCommerceDialog library.

The main features provided by the NpCommerceDialog library are:

* Lists products of a category specified by the user.
* Displays details of a product specified by the user.
* Redeem promotion codes.
* Purchases and downloads products specified by the user.
* Adds funds to the user's wallet.
* Displays a screen to encourage the user to join PlayStation®Plus.
* Allows users to browse and purchase content from either PlayStation™Store Delivered Content or Commerce Catalog and Entitlements services.

# Embedding into a Program

This section shows you how to embed required libraries in your program to enable use of the NPCommerceDialog library.

1. Include `np_commerce_dialog.h` in the source program.
2. Before calling any NpCommerceDialog library APIs in the program, load the PRX module with the relevant Sysmodule library API, as follows:

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_COMMERCE) != SCE_OK ) {
    // Error handling
}
```

1. Upon building the program, link `libSceNpCommerce_stub_weak.a`.
2. Embed the CommonDialog library to use the NpCommerceDialog library. See [CommonDialog Library Overview - Library Overview - Embedding into a Program](../CommonDialog-Overview/embedding-into-a-program.html).

It is not necessary to explicitly include the `common_dialog.h` header file of the CommonDialog library since it is automatically included when including `np_commerce_dialog.h` in the source program.

# Sample Programs

The sample program using the NpCommerceDialog library is:

## sample\_code/playstation\_network/api\_np\_commerce

This is a comprehensive sample of NP commerce. It uses features of the NpCommerceDialog library.

# Reference Materials

This topic provides links to additional sources of information for the CommonDialog libraries.

For more information regarding specifications, restrictions, etc., see:

* [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html)
* [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html)

For information on NP commerce, as well as terms such as category/product/service label used for displaying products in the PlayStation™Store, refer to:

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)
* [PlayStation™Network Commerce Service Overview](../PSN_Commerce_Service-Overview/__document_toc.html)

# Related Information

This topic includes links to information related to NpCommerceDialog libraries.

In addition to this document, SIE also provides important release note information that could affect application development. This information includes bugs, points to note, restrictions, and announcements. You can refer to the release notes below:

* [Release Notes - NpCommerceDialog Library](../ReleaseNotes/PlayStation_Network-NpCommerceDialog-ReleaseNotes.html)