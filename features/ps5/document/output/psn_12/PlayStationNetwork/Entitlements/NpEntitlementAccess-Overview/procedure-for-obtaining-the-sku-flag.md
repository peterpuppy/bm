# NpEntitlementAccess Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpEntitlementAccess-Overview/procedure-for-obtaining-the-sku-flag.html

# Using the Library: SKU Flags

This topic describes how to use the NpEntitlementAccess library to handle SKU flags. Features for testing are also described.

# Procedure for Obtaining the SKU Flag

The following procedure shows how to get the SKU flag that is set for each application.

Note:

Features related to the SKU flag are intended for use by applications with applicationDrmType in the parameter file (param.json) set so that the application can be upgraded. Other applications can also use these features, but the features won't be useful to them.

1. **Initialize the library**

   Use `sceNpEntitlementAccessInitialize()` to initialize the library as explained in "[Procedure to Initialize the NpEntitlementAccess Library](procedure-for-initializing-the-library.html)".
2. **Obtain the SKU flag**

   Use `sceNpEntitlementAccessGetSkuFlag()` to obtain the SKU flag.

   ```
   /* Obtain the SKU flag */
   SceNpEntitlementAccessSkuFlag  skuflag;
   ret = sceNpEntitlementAccessGetSkuFlag( &skuflag );
   ```

# SKU Flag Update Event

The SKU flag may change to "Full" while the application is running due to a user purchasing the product version application in the PlayStation™Store. The application will be notified of an update to the SKU flag as an event (`SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE`) from the SystemService library; thus, applications that use SKU flags can receive this event notification and re-check the SKU flag.

# Development Support Features for the SKU Flag

SKU flag values can be set in "★Debug Settings" > "PlayStation Network" > "Upgradable App Debug" as follows:

* Trial: Set `SCE_NP_ENTITLEMENT_ACCESS_SKU_FLAG_TRIAL`
* Full: Set `SCE_NP_ENTITLEMENT_ACCESS_SKU_FLAG_FULL`
* Off: Set the default value (`SCE_NP_ENTITLEMENT_ACCESS_SKU_FLAG_FULL`)

Use this feature for local testing. If the application is running, the set value will be immediately reflected in the SKU flag value (obtained with `sceNpEntitlementAccessGetSkuFlag()`), and the application will be notified of the `SCE_SYSTEM_SERVICE_EVENT_ENTITLEMENT_UPDATE` event from the SystemService library.