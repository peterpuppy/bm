# NpCommerceDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCommerceDialog-Overview/using-the-library.html

# Using the Library

# Preparation

To use the NpCommerceDialog library, call the `sceCommonDialogInitialize()` function to initialize the CommonDialog library upon program startup and to start a common dialog process.

This step is not necessary if it has already been called and is already running. If `sceCommonDialogInitialize()` is called when a common dialog process is already running, the function returns `SCE_COMMON_DIALOG_ERROR_ALREADY_SYSTEM_INITIALIZED`.

Note: Call `sceCommonDialogInitialize()` upon program startup, as it may take some time for a common dialog process to start. Further, since file reads, etc. occur when a common dialog process starts, the file load speed of the application process may be affected. Be sure to implement the application so that waiting time does not seem excessively long for the user.

For details on initializing the CommonDialog library, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) and the [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html).

# Basic Procedure

This topic explains the basic procedure for displaying the NP commerce
dialog.

Basic Procedure

Note: The examples in this section use `SceNpCommerceDialogParam2`, `sceNpCommerceDialogParamInitialize2()`, and `sceNpCommerceDialogOpen2()`, however, NpCommerceDialog Library still supports `sceNpCommerceDialogParam`. See [NpCommerce Library Reference](../NpCommerce-Reference/__document_toc.html) for more details.

## (1) Initialize the NP commerce dialog:

Call `sceNpCommerceDialogInitialize()` and initialize the NP commerce dialog:

```
if ( sceNpCommerceDialogInitialize() < 0 ) {
    // Error handling
}
```

## (2) Set parameters for the NP commerce dialog:

Prepare a `SceNpCommerceDialogParam2` type structure as call parameters for the NP commerce dialog and initialize the structure with `sceNpCommerceDialogParamInitialize2()`. Set the dialog display mode, the user ID of the user purchasing the products, and the parameters required for the set display mode:

```
SceNpCommerceDialogParam2 param;
sceNpCommerceDialogParamInitialize2( &param );
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY;
param.userId = user_id;
const char *category_label[] = { "CATEGORY00000000" };
param.targets = category_label;
param.numTargets = 1;
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
```

## (3) For each display mode and the parameters required for each mode, as well as other points to note, refer to the following sections:

* [Using the Browse Category Mode](using-the-browse-category-mode.html "This topic provides information on using NP commerce dialog in Browse Category mode.")
* [Using the Browse Product Mode](using-the-browse-product-mode.html "This topic provides information on using NP commerce dialog in Browse Product mode.")
* [Using the Redeem Promotion Code Mode](using-the-redeem-promotion-code-mode.html "This topic provides information on using NP commerce dialog in Redeem Promotion Code mode.")
* [Using the Checkout Mode](using-the-checkout-mode.html "This topic provides information on using NP commerce dialog in Checkout mode.")
* [Using the Download Mode](using-the-download-mode.html "This topic provides information on using NP commerce dialog in Download mode.")
* [Using the Join Premium Mode](using-the-join-premium-mode.html "This topic provides information on using NP commerce dialog in Join Premium mode.")

Note: The NP commerce dialog is displayed in the language corresponding to the country/region in which the user account is registered. Note the user ID specified as a parameter is unique to the console, and the display language may differ from the display language setting of the system software.

## (4) Display the NP commerce dialog:

Call `sceNpCommerceDialogOpen2()` with the dialog call parameters set above as the argument and display the dialog.

```
if ( sceNpCommerceDialogOpen2( &param ) < 0 ) {
    // Error handling
}
```

## (5) Monitor status of the NP commerce dialog:

Call `sceNpCommerceDialogUpdateStatus()` at regular intervals (such as at every rendering frame) to poll the operation status of the NP commerce dialog.

```
while(1) {
    stat = sceNpCommerceDialogUpdateStatus();
    if( stat == SCE_COMMON_DIALOG_STATUS_FINISHED ) {
        break;
    } else if( stat == SCE_COMMON_DIALOG_STATUS_RUNNING ) {
        if( need_close ) {
            sceNpCommerceDialogClose();
            break;
        }
    }
```

`SCE_COMMON_DIALOG_STATUS_RUNNING` returns for the operation status while the dialog is being displayed, therefore wait until the dialog is closed with a user operation, etc. and the operation status becomes `SCE_COMMON_DIALOG_STATUS_FINISHED`.

## (6) Get the result of calling the NP commerce dialog:

When the user closes the NP commerce dialog, the operation status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED`. Call `sceNpCommerceDialogGetResult()` to obtain the result of calling the dialog.

```
SceNpCommerceDialogResult result;
memset( &result, 0, sizeof(result) );
if( 0 > sceNpCommerceDialogGetResult( &result ) ) {
    // Error handling
}
```

To display the NP commerce dialog again after obtaining the call result, go back to [step 2](basic-procedure.html#_1_2___1_2_2) and start again from setting the parameters.

## (7) Terminate the NP commerce dialog:

After obtaining the call result, call `sceNpCommerceDialogTerminate()` to terminate the NP commerce dialog. This frees the resources allocated upon initialization and the operation status transitions to `SCE_COMMON_DIALOG_STATUS_NONE`.

Note: `sceNpCommerceDialogOpen()` can also be called when the operation status is `SCE_COMMON_DIALOG_STATUS_FINISHED`. Thus, it is possible to display the dialog again without executing `sceNpCommerceDialogTerminate()` and terminating the dialog first.

## (8) Close the NP Commerce Dialog by the Application:

Call `sceNpCommerceDialogClose()` to close the NP commerce dialog without user operation. When the call succeeds and `sceNpCommerceDialogUpdateStatus()` is periodically called thereafter, the dialog carries out processing to close the dialog display; the operation status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED` upon processing completion. When the dialog is closed with this function, the dialog call result that can be obtained with `sceNpCommerceDialogGetResult()` is `SCE_COMMON_DIALOG_RESULT_OK`.

## (9) Abort Processing:

To abort processing of the NP commerce dialog from the application side on an emergency basis, call `sceNpCommerceDialogTerminate()`. Processing can be aborted faster by calling this function rather than `sceNpCommerceDialogClose()`, and the operation status immediately transitions to `SCE_COMMON_DIALOG_STATUS_NONE`.

## (10) Handling of Unexpected Fatal Errors:

There is a possibility that the following functions might return `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL`. In such cases, call `sceNpCommerceDialogTerminate()`. Afterward, re-execute the processes starting with [step 1](basic-procedure.html#_1_2___1_2_1).

* `sceNpCommerceDialogInitialize()`
* `sceNpCommerceDialogOpen2()`
* `sceNpCommerceDialogGetResult()`

## API Summary

The functions used in basic processing to display the NP commerce dialog are shown in the table below.

APIs Used in Basic Processing

| **Function** | **Description** |
| --- | --- |
| `sceNpCommerceDialogInitialize()` | Initializes the NP commerce dialog. |
| `SceNpCommerceDialogParam` | Parameter structure for the dialog. |
| `SceNpCommerceDialogParam2` | Parameter structure for the dialog. |
| `sceNpCommerceDialogParamInitialize()` | Initializes the parameter structure. |
| `sceNpCommerceDialogParamInitialize2()` | Initializes the parameter structure. |
| `sceNpCommerceDialogOpen()` | Displays the dialog. |
| `sceNpCommerceDialogOpen2()` | Displays the dialog. |
| `sceNpCommerceDialogUpdateStatus()` | Updates and obtains the dialog's operation status. |
| `sceNpCommerceDialogClose()` | Closes the dialog. |
| `SceNpCommerceDialogResult` | Structure storing the result of calling the dialog. |
| `sceNpCommerceDialogGetResult()` | Gets the result of calling the dialog. |
| `sceNpCommerceDialogTerminate()` | Terminates the NP commerce dialog. |

# Using the Browse Category Mode

This topic provides information on using NP commerce dialog in Browse Category mode.

When the NP commerce dialog is launched in the Browse Category mode, one category specified by the application is displayed onscreen. The user can select a product within that category to display product details and to purchase the product by pressing the **Buy** button on the product detail screen.

## Parameters of the Browse Category Mode

Specify `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY` for `mode` in the `SceNpCommerceDialogParam2` structure. For `targets`, specify an array with the category label string of the category to display as the only element, and specify 1 for `numTargets`. When specifying a top category, however, specify NULL for `targets` and 0 for `numTargets`.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY;
const char *category_label[] = { "CATEGORY00000000" };
param.targets = category_label;
param.numTargets = 1;
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
```

If the category to display belongs to a service label other than the default (=0), specify that service label for `serviceLabel`.

The Browse Category mode supports both designated `serviceName` values. Configure this parameter based on whether the content you want to access was linked by the PlayStation™Store Delivered Contents service or the Commerce Catalog and Entitlements service.

Category labels can be found in the Content Pipeline tool under **Store Structures**
> **In-Game Catalog** for your concept, for example, `WEAPONSEU`.

Category Label in Content Pipeline

# Using the Browse Product Mode

This topic provides information on using NP commerce dialog in Browse Product mode.

When the NP commerce dialog is launched in the browse product mode, the product detail screen of one product specified by the application is displayed. The user can purchase the product by pressing the **Buy** button.

## Parameters of the Browse Product Mode

Specify `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT` for `mode` in the `SceNpCommerceDialogParam2` structure. For `targets`, specify an array with the product label string of the product to display as the only element, and specify 1 for `numTargets`.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT;
const char *product_label[] = { "PRODUCT000000000" };
param.targets = product_label;
param.numTargets = 1;
param.serviceName = SCE_NP_SERVICE_COMMERCE_CATALOG_AND_ENTITLEMENTS;
```

If the product to display belongs to a service label other than the default (0), specify that service label for `serviceLabel`.

Product Mode supports both designated `serviceName` values. Configure this parameter based on whether the content you want to access was linked by the PlayStation™Store Delivered Contents service or the Commerce Catalog and Entitlements service.

Product labels can be found in the Content Pipeline tool under **Product Groups** for
your concept, for example, `2880310005072815`.

Product Label in Content Pipeline

# Using the Redeem Promotion Code Mode

This topic provides information on using NP commerce dialog in Redeem Promotion Code mode.

When the NP commerce dialog is launched in the redeem promotion code mode, the user can obtain a product in exchange for its promotion code.

There are two methods by which the NP commerce dialog can be launched in this mode: the application specifies the promotion code to redeem upon dialog launch, or the dialog is launched without specifying the promotion code and the user is asked to enter it.

## Parameters for When the Application Specifies the Promotion Code to Redeem

Specify `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE` for `mode` in the `SceNpCommerceDialogParam` structure. Also specify an array with only the promotion code as its element for `targets` and 1 for `numTargets`.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE;
const char *product_label[] = { "AAAA-A111-111A" };
param.targets = product_label;
param.numTargets = 1;
```

## Parameters for When the User Is Asked to Enter the Promotion Code

Specify `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE` for `mode` in the `SceNpCommerceDialogParam` structure. Also specify NULL for `targets` and 0 for `numTargets`.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE;
param.targets = NULL;
param.numTargets = 0;
```

# Using the Checkout Mode

This topic provides information on using NP commerce dialog in Checkout
mode.

When the NP commerce dialog is launched in checkout mode, the user can be guided to product purchase processing.

One or more specified products are displayed on the **Purchase Confirmation** screen and purchase processing is carried out when the user presses the **Buy** button. An **Add Funds** button is also displayed on the **Purchase Confirmation** screen and the user can select to add funds to his/her wallet.

Products to purchase can either be specified using product labels or using product labels and SKU labels. An error occurs if even one already-purchased product or product that cannot be purchased is specified.

## Parameters for When Products Are Specified Using the Product Label

If all the products to display in the dialog are products with one SKU registered per product, products can be specified using product labels.

In this case, specify `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` for `mode` in the `SceNpCommerceDialogParam` structure. For `targets`, specify an array with the product label of the product(s) to display, and specify the number of products (the number of elements in `targets`) for `numTargets`.

If there is even one product specified that has two or more SKUs registered, an error occurs.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT;
const char *sku_ids[] = {
    "PRODUCT000000000",
    "PRODUCT000000001" };
param.targets = sku_ids;
param.numTargets = 2;
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
```

If all the products to display belong to the same service label other than the default (=0), specify that service label in `serviceLabel`. If some products belong to a different service label, make the specification by placing that service label and a colon in front of the product label (for example, `"1:PRODUCT000000001"`).

Checkout mode supports both designated `serviceName` values. Configure this parameter based on whether the content you want to access was linked by the PlayStation™Store Delivered Contents service or the Commerce Catalog and Entitlements service.

## Parameters for When Products Are Specified Using Product Labels and SKU Labels

If a product with multiple SKUs registered is included in the products to display in the dialog, products must be specified using product labels and SKU labels.

In this case, specify `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` for `mode` in the `SceNpCommerceDialogParam` structure, specify an array of character strings consisting of each product label and SKU label for the products to display connected by a hyphen for `targets`, specify the number of products (the number of elements in `targets`) for `numTargets`. Note that SKU labels are issued by SIE and therefore cannot be fixed within the program; SKU labels must be obtained using the In-Game Catalog Web API.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT;
param.targets = sku_ids; /* ex: {"PRODUCT000000000-J001", "PRODUCT000000001-J001" } */
param.numTargets = 2;
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
```

If all the products to display belong to the same service label other than the default (=0), specify that service label in `serviceLabel`. If some products belong to a different service label, make the specification by placing that service label and a colon in front of the product label (for example, `"1:PRODUCT000000001-J001"`).

## Adding Funds to Wallet

When the NP commerce dialog is launched in a mode that entails payment (e.g. checkout mode), an **Add Funds** button is displayed onscreen and funds can be added to the user's wallet. A selection can be made for adding funds from the following two methods (may differ according to the country/region in which the user account is registered):

* Credit card.
* Prepaid card for PlayStation™Store.

If a credit card is selected for adding funds and a credit card is not registered, the credit card information screen is displayed and the user is able to register his/her credit card.

# Using the Download Mode

This topic provides information on using NP commerce dialog in Download mode.

When the NP commerce dialog is launched in the download mode, one or more products specified by the application is displayed on the **My Downloads** screen (unpurchased products and entitlement products is not displayed).

You can select products to download from this list. Use this mode to provide a feature by which the user can re-download purchased products.

There are two methods for specifying products to download: individually specifying products using the product label and SKU label or specifying products in a batch using the service label.

## Parameters for When Products Are Specified Using the Product Labels and SKU Labels

Specify `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST` for `mode` in the `SceNpCommerceDialogParam` structure. Also specify an array with the character strings consisting of a product label and SKU label connected by a hyphen of the products to download for `targets`, and specify the number of products (the number of elements in `targets`) in `numTargets`. Of the specified products, those that can be downloaded by the user are displayed in the dialog.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST;
param.targets = sku_ids; /* ex: {"PRODUCT000000000-J001", "PRODUCT000000001-J001" } */
param.numTargets = 2;
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
```

Note that SKU labels are issued by SIE and therefore cannot be fixed within the program; SKU labels must be obtained using the In-Game Catalog Web API.

If all the products to display belong to the same service label other than the default (0), specify that service label to `serviceLabel`. If some products belong to a different service label, make specification by placing that service label and a colon in front of the product label (for example, `"1:PRODUCT000000001-J001"`).

Download mode supports both designated `serviceName` values. Configure this parameter based on whether the content you want to access was linked by the PlayStation™Store Delivered Contents service or the Commerce Catalog and Entitlements service.

## Parameters for When Products Are Specified in a Batch Using the Service Label

Specify `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST` for `mode` in the `SceNpCommerceDialogParam` structure. Specify NULL for `targets` and 0 for `numTargets`. In addition, if the products to display belong to the same service label other than the default (=0), specify that service label in `serviceLabel`.

Of the products belonging to the specified service label, those that can be downloaded by the user are displayed in the dialog.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST;
param.targets = NULL;
param.numTargets = 0;
param.serviceLabel = a_service_label; // Specify the service label
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
```

# Using the Join Premium Mode

This topic provides information on using NP commerce dialog in Join Premium mode.

When the NP commerce dialog is launched in the Join Premium mode, the screen for purchasing PlayStation®Plus entitlements is displayed.

## Join Premium Mode Parameters

Specify `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM` for `mode` in the `SceNpCommerceDialogParam` structure. Also specify NULL for `targets`, 0 for `numTargets`, and the premium feature type for `features`.

```
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM;
param.targets = NULL;
param.numTargets = 0;
param.features = applying_features; // Specify premium feature type 
                                    // to apply for
```