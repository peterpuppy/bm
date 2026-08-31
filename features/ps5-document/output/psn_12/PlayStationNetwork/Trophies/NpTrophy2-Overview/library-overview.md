# NpTrophy2 Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Overview/library-overview.html

# Basic Information of the NpTrophy2 Library

This topic provides basic information that you need to know when using the NpTrophy2 library, including the purpose and characteristics of the library, the main features of the library, how to embed the library into your application program, the sample program provided by SIE, and reference materials.

## Purpose and Characteristics

The NpTrophy2 library provides API features for applications to obtain information, such as trophy configuration data and trophy records, from the trophy system. Because trophies are unlocked via the Universal Data System, the NpTrophy2 library does not provide any API features for unlocking trophies. For information on how to unlock trophies, refer to [Trophy System Overview - Game Play and the Trophy System - Unlocking Trophies](../Trophy_System-Overview/unlocking-trophies.html).

## Main Features

The main features provided by the NpTrophy2 library are as follows.

* Obtaining trophy configuration data
* Obtaining trophy unlock states

## Embedding into a Program

Include np.h in the source program. In addition, before calling any NpTrophy2 library API features in the program, load the PRX module with the relevant Sysmodule library function, as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_TROPHY2) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceNpTrophy2\_stub\_weak.a.

## Sample Program

The following sample program uses the NpTrophy2 library. Refer to [Sample Program Overview](../Sample-Overview/__document_toc.html) for basic information (such as the directory configuration) that is common to the sample programs provided in the SDK.

**sample\_code/playstation\_network/api\_np\_trophy2**

This sample exemplifies the basic usage of the NpTrophy2 library. The sample also includes unlocking trophies using the NpUniversalDataSystem library.

## Reference Materials

Refer to the following document for an overall look at the features of the PlayStation™Network:

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)

Refer to the following documents regarding the Np library, which is commonly required when using the PlayStation™Network functionalities.

* [Np Library Overview](../Np-Overview/__document_toc.html)
* [Np Library Reference](../Np-Reference/__document_toc.html)

Refer to the following document to gain an overall sense of how the trophy system works.

* [Trophy System Overview](../Trophy_System-Overview/__document_toc.html)

The Universal Data System is the basis for the trophy system. Refer to the following document for an overview of the Universal Data System and for the procedure for developing applications that use it:

* [Universal Data System Guide](../Universal_Data_System-Guide/__document_toc.html)

Refer to the following documents for information about the NpUniversalDataSystem library, which is required to unlock trophies.

* [NpUniversalDataSystem Library Overview](../NpUniversalDataSystem-Overview/__document_toc.html)
* [NpUniversalDataSystem Library Reference](../NpUniversalDataSystem-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpTrophy2 Library](../ReleaseNotes/PlayStation_Network-NpTrophy2-ReleaseNotes.html)