# NpBandwidthTest Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpBandwidthTest-Overview/reference-materials.html

# Library Overview

# Purpose and Features

The NpBandwidthTest library provides the application with a function for measuring the communication bandwidth between the client and the PlayStation™Network server.

# Used Resources

The NpBandwidthTest library uses one mutex upon loading the PRX. Moreover, it generates one thread upon measuring the bandwidth and allocates a work memory of 64 KiB. The stack of the generated thread is 32 KiB; the application can specify the priority of this thread and the CPU affinity mask.

# Embedding into a Program

Include np.h in the source program. In addition, before calling any NpBandwidthTest library APIs in the program, load the PRX module with the Sysmodule library API

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_UTILITY) != SCE_OK ) {
    // Error handling
}
```

Upon building the program, link libSceNpUtility\_stub\_weak.a.

# Sample Program

A sample program using the NpBandwidthTest library is as follows.

## samples/sample\_code/playstation\_network/api\_np\_bandwidth\_test

This sample shows the basic procedure for using the NpBandwidthTest library.

# Reference Materials

Refer to the following document for an overview of the PlayStation™Network functionalities.

* [PlayStation™Network Overview](../PSN-Overview/__document_toc.html)

Refer to the following documents regarding the Np library, which is commonly required when using the PlayStation™Network functionalities.

* [Np Library Overview](../Np-Overview/__document_toc.html)
* [Np Library Reference](../Np-Reference/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpBandwidthTest Library](../ReleaseNotes/PlayStation_Network-NpBandwidthTest-ReleaseNotes.html)