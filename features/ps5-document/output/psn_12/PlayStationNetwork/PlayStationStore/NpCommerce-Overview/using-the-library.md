# NpCommerce Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCommerce-Overview/using-the-library.html

# Using the NpCommerce Library

## Embedding into a Program

Include `np.h` in the source program. An additional number of headers are automatically included.

In addition, before calling the NpCommerce library, load the PRX module with the Sysmodule library API as follows.

```
if ( sceSysmoduleLoadModule(SCE_SYSMODULE_NP_COMMERCE) != SCE_OK ) {
                //Error handling
                }
```

Upon building the program, link `libSceNpCommerce_stub_weak.a`.

## Sample Programs

The Sample program using the NpCommerce library is:

**samples/sample\_code/playstation\_network/api\_np/np\_commerce/**

This is an integrated sample for NpCommerce.

# Showing a PlayStation™Store Icon

You can use the NpCommerce library to display the PlayStation™Store icon for in-game stores.

Call `sceNpCommerceShowPsStoreIcon()` to display the PlayStation™Store icon. Call `sceNpCommerceHidePsStoreIcon()` to hide it.

For more information on available endpoints, see [NpCommerce Library Reference](../NpCommerce-Reference/__document_toc.html).

## Setting the Display Position

Because the PlayStation™Store icon is overlaid on the screen displayed by the application, select its display position so that it does not overlap with important display items of the application. The display position can be selected from three options - screen lower left, screen lower center, and screen lower right - with the argument of `sceNpCommerceShowPsStoreIcon()`. By calling `sceNpCommerceSetPsStoreIconLayout()` in advance, a selection can be made to fix the layout area to the entire screen (100%), to change the layout area pursuant to the display safe area (90% to 100%), or to fix the layout area to 90% of the entire screen (the layout area is fixed to 100% by default). The display positions and size for each are as follows:

PlayStation™Store Icon Size
PlayStation™Store Icon Display Position

## Limitations for VR Output

There are limitations when the video output mode is VR output:

* The display position cannot be specified during 3D VR (3D display in the VR output mode). The display position and layout specified with the API is ignored and the PlayStation™Store icon is always displayed at the lower center of the overlay area of the system screen.
* In the separate mode, the PlayStation™Store icon is not displayed on the social screen. In the mirroring mode, the PlayStation™Store icon may be displayed on the social screen depending on the viewpoint of the user wearing the VR headset.

## API Summary

Functions for Showing/Hiding the PlayStation™Store Icon

| **API** | **Description** |
| --- | --- |
| `sceNpCommerceShowPsStoreIcon()` | Shows the PlayStation™Store icon |
| `sceNpCommerceHidePsStoreIcon()` | Hides the PlayStation™Store icon |
| `sceNpCommerceSetPsStoreIconLayout()` | Sets the layout area of the PlayStation™Store icon |