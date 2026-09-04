# NpEntitlementAccess Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Overview/procedure-for-initializing-the-library.html

# Basic Information on the NpEntitlementAccess Library

This topic provides basic information you should know when using the NpEntitlementAccess library, including the purpose and characteristics of the library, its main features, how to embed it into application programs, and sample programs provided by SIE.

# NpEntitlementAccess Library Purpose and Characteristics

The NpEntitlementAccess library provides features for accessing additional content, consumable entitlements, and subscription entitlements. The library also provides a feature for determining whether an application is a product version or a trial version.

# Main Features of the NpEntitlementAccess Library

The main features provided by the NpEntitlementAccess library are as follows:

* Feature for accessing additional content
  + Obtaining a list of additional content for which the entitlement is valid
* Feature for accessing an entitlement
  + Obtaining a valid entitlement
  + Consuming a consumable entitlement
* Feature for determining whether an application is a product version or a trial version
  + Feature for obtaining the SKU flag
  + Feature for obtaining the GameTrials flag

# Embedding the NpEntitlementAccess Library into a Program

Include np\_entitlement\_access.h in the source program. In addition, before calling any NpEntitlementAccess library function in the program, load the PRX module with the relevant Sysmodule library function, as follows:

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_ENTITLEMENT_ACCESS) != SCE_OK ) {
    // Error handling
}
```

Link libSceNpEntitlementAccess\_stub\_weak.a upon building the program.

# Procedure to Initialize the NpEntitlementAccess Library

Prepare the `SceNpEntitlementAccessInitParam` and `SceNpEntitlementAccessBootParam` structures and clear each with 0's. Use `sceNpEntitlementAccessInitialize()` to initialize the NpEntitlementAccess library as follows:

```
/* Set parameters to be passed to sceNpEntitlementAccessInitialize() */
SceNpEntitlementAccessInitParam initParam;
SceNpEntitlementAccessBootParam bootParam;
memset(&initParam, 0, sizeof(SceNpEntitlementAccessInitParam));
memset(&bootParam, 0, sizeof(SceNpEntitlementAccessBootParam));

/* Perform library initialization processing */
ret = sceNpEntitlementAccessInitialize( &initParam, &bootParam );
```

# NpEntitlementAccess Library Sample Program

A sample program using the NpEntitlementAccess library is as follows:

## sample\_code/playstation\_network/api\_np\_entitlement\_access

This sample exemplifies basic usage of the NpEntitlementAccess library.

# Reference Materials for Using the NpEntitlementAccess Library

Refer to the following document for information about accessing data in additional content and about identifying additional content:

* [AppContent Library Overview](../AppContent-Overview/__document_toc.html)

Refer to the following documents for an overview of additional content and entitlements:

* [PlayStation™Network Commerce Service Overview](../PSN_Commerce_Service-Overview/__document_toc.html)
* [Entitlements Overview](../../../WebAPI/latest/Entitlements-Overview/__document_toc.html)

Refer to the following document for an overview of event notification obtainment regarding events that occur outside of the application:

* [SystemService Library Overview](../SystemService-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - NpEntitlementAccess Library](../ReleaseNotes/PlayStation_Network-NpEntitlementAccess-ReleaseNotes.html)