# NpCommerceDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCommerceDialog-Reference/sce-np-commerce-dialog-param2.html

# Initialization/Termination

# SceNpCommerceDialogMode

NP commerce dialog display modes.

## Definition

```
#include <np_commerce_dialog.h>
typedef int32_t SceNpCommerceDialogMode;
```

## Description

These constants represent the NP commerce dialog display modes.

Specify the display mode in the `mode` member of the [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.") or [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.") structures, which is passed as an argument when displaying the dialog with [sceNpCommerceDialogOpen()](sce-np-commerce-dialog-open.html "Displays the NP commerce dialog.") and [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog.") respectively.

| **Value** | **Description** |
| --- | --- |
| `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY` | Browse category mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT` | Browse product mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE` | Redeem promotion code mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` | Checkout mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST` | Download mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM` | Join premium mode. |

**Browse Category Mode**

Displays one category specified first as a parameter onscreen. The user can select a product or category within this category and display its contents.

**Browse Product Mode**

Displays a product detail screen for one product specified first as a parameter. The user can purchase products from this screen.

**Redeem Promotion Code Mode**

Displays a screen for redeeming a promotion code. If one promotion code is specified first as a parameter, the screen for redeeming that promotion code is displayed. If a promotion code is not specified, a screen prompting the user to enter the promotion code to redeem is displayed.

**Checkout Mode**

Displays one or multiple products specified as a parameter on the "Purchase Confirmation" screen. Purchase processing is carried out when the user clicks on the "Buy" button and download processing is automatically started when purchase processing completes.

An error occurs if there is a product among the products specified that has already been purchased or a product that cannot be purchased.

**Download Mode**

Displays one or multiple products specified as a parameter on the "My Downloads" screen. The user can select a product from the list to download.

If a product that cannot be downloaded (because it has not been purchased, for example) exists among the products specified upon startup, that product is not included on the "My Downloads" screen.

**Join Premium Mode**

Displays a screen to purchase entitlement to join PlayStation®Plus. The user can proceed from this screen to processing to join PlayStation®Plus.

## See Also

[sceNpCommerceDialogOpen()](sce-np-commerce-dialog-open.html "Displays the NP commerce dialog."), [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters."), [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog."), [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.")

# SceNpServiceName

NP commerce service names.

## Definition

```
#include <np_commerce_dialog.h>
typedef int32_t SceNpServiceName;
```

## Description

These constants represent the PlayStation™Network services that can be provisioned to a title for content linking.

Specify the service name in the `serviceName` member of the [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.") structure, which is passed as an argument when displaying the dialog with [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog.").

| **Value** | **Description** |
| --- | --- |
| `SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS` | PlayStation™Store Delivered Contents |
| `SCE_NP_SERVICE_COMMERCE_CATALOG_AND_ENTITLEMENTS` | Commerce Catalog and Entitlements service. |

**PlayStation™Store Delivered Contents**

Refers to the PlayStation™Store Delivered Contents service that can be provisioned for the title. When using this service name, the configured service label assumes it is in reference to this PlayStation™Network service. This service is supported by the Browse Category, Browse Product, Checkout, and Download modes.

**Commerce Catalog and Entitlements**

Refers to the Commerce Catalog and Entitlements service that can be provisioned for the title. When using this service name, the configured service label assumes it is in reference to this PlayStation™Network service. This service is supported by the Browse Category, Browse Product, Checkout, and Download modes.

## See Also

[sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog."), [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.")

# SceNpCommerceDialogParam2

NP commerce dialog parameters.

## Definition

```
#include <np_commerce_dialog.h>
typedef struct SceNpCommerceDialogParam2 {
    SceCommonDialogBaseParam baseParam;
    int32_t size;
    SceUserServiceUserIduserId;
    SceNpCommerceDialogModemode;
    SceNpServiceLabelserviceLabel;
    SceNpServiceName serviceName;
    const char * const *targets;
    uint32_t numTargets;
    int : 32;
    uint64_t features;
    void *userData;
    uint8_t reserved[32];
} SceNpCommerceDialogParam2;
```

## Members

|  |  |
| --- | --- |
| `baseParam` | Parameters common to the common dialog. |
| `size` | Size of this structure. |
| `userId` | User ID. |
| `mode` | Display mode of the NP commerce dialog. |
| `serviceLabel`  `serviceName` | Service label.  Service Name of the PlayStation™Network service to be used for Service Label lookup. |
| `targets` | Array of display target strings, or NULL. |
| `numTargets` | Total display targets, or 0. |
| `features` | Premium feature type. |
| `userData` | Application defined argument. |
| `reserved` | Reserved area (fill with 0's). |

## Description

This structure is used for specifying dialog parameters when displaying the NP commerce dialog with [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog.").

Use this structure after initializing it with [sceNpCommerceDialogParamInitialize2()](sce-np-commerce-dialog-param-initialize2.html "Initializes parameters for the NP commerce dialog.").

For `userId`, specify the user ID of the user calling the dialog. Product purchase is carried out by the NP account of the user corresponding to this value. This member is required for all display modes.

For `mode`, specify the display mode of the NP commerce dialog. Specify one of the following values:

| **Value** | **Description** |
| --- | --- |
| `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY` | Browse Category mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT` | Browse Product mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE` | Redeem promotion code mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` | Checkout mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST` | Download mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM` | Join premium mode. |

For details on the dialog display mode, refer to [SceNpCommerceDialogMode](sce-np-commerce-dialog-mode.html "NP commerce dialog display modes.").

For `serviceLabel`, specify applicable values when making specifications with a service label. This is valid when the display mode is `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY`, `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT`, `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT`, or `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST`.

For details on the service label, refer to the [PlayStation™Network Overview](../PSN-Overview/__document_toc.html).

For `serviceName`, specify applicable values when making specifications with a service name. This is valid when the display mode is `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY`, `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT`, `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT`, or `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST`.

Values to set for `targets` and `numTargets` differ by the display mode:

* **SCE\_NP\_COMMERCE\_DIALOG\_MODE\_CATEGORY:** Set `targets` as an array with the label name of the category to browse as the only element and `numTargets` to one. Setting `targets` to NULL and `numTargets` to zero allows you to open the top category of the In-Game catalog that belongs to the service label specified in `serviceLabel`.
* **SCE\_NP\_COMMERCE\_DIALOG\_MODE\_PRODUCT:** Set `targets` as an array with the label name of the category to browse as the only element and `numTargets` to one.
* **SCE\_NP\_COMMERCE\_DIALOG\_MODE\_PRODUCT\_CODE:** Set `targets` as an array with the promotion code to redeem as the only element and `numTargets` to one. Setting `targets` to NULL and `numTargets` to zero allows the user to enter the promotion code to redeem.
* **SCE\_NP\_COMMERCE\_DIALOG\_MODE\_CHECKOUT:** Set `targets` as
  an array of product labels, for example, PRODUCT000000001, to purchase or as an array
  where each element is a product label and a SKU label connected by a hyphen (-), for
  example, PRODUCT000000001-J001. Set `numTargets` as the number
  of elements in the array. The maximum value for `numTargets` is
  `SCE_NP_COMMERCE_DIALOG_NUM_TARGETS_MAX`, or ten. When
  `targets` is set as an array with product labels as
  elements, the products must have a purchasable SKU. Including a product with two or
  more SKUs in the array results in an error and the purchase processing terminates.
  When `targets` is set as an array with product labels and SKU
  labels connected by hyphens (-) as elements, you can specify products with different
  service labels by connecting a service label and a colon (:) at the beginning of the
  string for each element, for example, 1:PRODUCT000000001-J001. Elements without
  service labels use the value from `serviceLabel` as their
  service label.
* **SCE\_NP\_COMMERCE\_DIALOG\_MODE\_DOWNLOADLIST:** Specify an array in `targets` where each element is a product label and a SKU label connected by a hyphen (-) for example, PRODUCT000000001-J001. Set `numTargets` as the number of elements in the array. Set `targets` to NULL and `numTargets` to zero to target all products belonging to the service label specified in `serviceLabel` that the user specified in `userId` can download.
* **SCE\_NP\_COMMERCE\_DIALOG\_MODE\_PREMIUM:** Set `targets` to NULL and `numTargets` to zero.

Set `features` as the premium feature type. Specify `SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY`.

This parameter specification is only valid when the display mode is `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM`. Specify zero for modes other than `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM`.

You can set `userData` as an arbitrary pointer that is stored as the `userData` member of the [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.") structure when obtaining the dialog call result with [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog.").

Although parameters common to the common dialog must be specified in `baseParam` and the size of this structure in `size`, appropriate values for them are stored automatically with [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog."). It is not necessary to explicitly specify them in the program.

`reserved` is a reserved area. This area must be filled with 0's; however, it is automatically filled with 0's by [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog.").

## Examples

```
SceNpCommerceDialogParam2 param;
sceNpCommerceDialogParamInitialize2( &param );
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT;
const char *category_label[] = { "CATEGORY00000000" };
param.targets = category_label;
param.numTargets = 1;
param.serviceName = SCE_NP_SERVICE_COMMERCE_CATALOG_AND_ENTITLEMENTS;
```

## See Also

[SceNpCommerceDialogMode](sce-np-commerce-dialog-mode.html "NP commerce dialog display modes."), [sceNpCommerceDialogParamInitialize2()](sce-np-commerce-dialog-param-initialize2.html "Initializes parameters for the NP commerce dialog."), [sceNpCommerceDialogOpen2()](sce-np-commerce-dialog-open2.html "Displays the NP commerce dialog."), [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog."), [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.")

# SceNpCommerceDialogParam

NP commerce dialog parameters.

## Definition

```
#include <np_commerce_dialog.h>
typedef struct SceNpCommerceDialogParam {
    SceCommonDialogBaseParam baseParam;
    int32_t size;
    SceUserServiceUserIduserId;
    SceNpCommerceDialogModemode;
    SceNpServiceLabelserviceLabel;
    const char * const *targets;
    uint32_t numTargets;
    int : 32;
    uint64_t features;
    void *userData;
    uint8_t reserved[32];
} SceNpCommerceDialogParam;
```

## Members

|  |  |
| --- | --- |
| `baseParam` | Parameters common to the common dialog. |
| `size` | Size of this structure. |
| `userId` | User ID. |
| `mode` | Display mode of the NP commerce dialog. |
| `serviceLabel` | Service label. |
| `targets` | Array of display target strings, or NULL. |
| `numTargets` | Total display targets, or 0. |
| `features` | Premium feature type. |
| `userData` | Application defined argument. |
| `reserved` | Reserved area (fill with 0's). |

## Description

This structure is used for specifying dialog parameters when displaying the NP commerce dialog with [sceNpCommerceDialogOpen()](sce-np-commerce-dialog-open.html "Displays the NP commerce dialog.").

Use this structure after initializing it in advance with [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog.").

For `userId`, specify the user ID of the user calling the dialog. Product purchase is carried out by the NP account of the user corresponding to this value. This member is required for all display modes.

For `mode`, specify the display mode of the NP commerce dialog. Specify one of the following values.

| **Value** | **Description** |
| --- | --- |
| `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY` | Browse category mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT` | Browse product mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE` | Redeem promotion code mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` | Checkout mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST` | Download mode. |
| `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM` | Join premium mode. |

For details on the dialog display mode, refer to [SceNpCommerceDialogMode](sce-np-commerce-dialog-mode.html "NP commerce dialog display modes.").

For `serviceLabel`, specify applicable values when making specification with a service label. This is valid when the display mode is `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY`, `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT`, `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT`, or `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST`.

For details on the service label, refer to the [PlayStation™Network Overview](../PSN-Overview/__document_toc.html).

Values to specify to `targets` (array representing display targets) and `numTargets` (total number of display targets) differ by the display mode.

* When `mode` is `SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY`

Specify an array with the label name of the category to browse as the only element for `targets`, and specify 1 for `numTargets`. However, by specifying NULL in `targets` and 0 in `numTargets`, it is possible to open the top category of the In-Game catalog that belongs to the service label specified in `serviceLabel`.

* When `mode` is `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT`

Specify an array with the label name of the product to browse as the only element for `targets`, and specify 1 for `numTargets`.

* When `mode` is `SCE_NP_COMMERCE_DIALOG_MODE_PRODUCT_CODE`

Specify an array with the promotion code to redeem as the only element for `targets`, and specify 1 for `numTargets`. However, by specifying NULL in `targets` and 0 for `numTargets`, it is possible to let the user enter the promotion code to redeem.

* When `mode` is
  `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT`, for
  `targets`, specify an array of product labels (example:
  PRODUCT000000001) to purchase or specify an array where each element is a product
  label and a SKU label connected by a hyphen (-) (example: PRODUCT000000001-J001), and
  for `numTargets`, specify the number of elements in the array.
  The maximum value for `numTargets` is
  `SCE_NP_COMMERCE_DIALOG_NUM_TARGETS_MAX` (=10). When an array with
  product labels as elements is specified to `targets`, the
  specified products must all have a purchasable SKU. If a product with two or more
  SKUs is specified, an error dialog is displayed and the purchase processing
  terminates.

When an array with product labels and SKU labels connected by hyphens (-) as elements is specified in `targets`, it is possible to specify products with different service labels by connecting a service label and a colon (:) at the beginning of the string for each element (example: 1:PRODUCT000000001-J001). Elements without service labels specified are considered to be products with service labels set to `serviceLabel`.

* When `mode` is `SCE_NP_COMMERCE_DIALOG_MODE_DOWNLOADLIST`

Specify an array in `targets` where each element is a product label and a SKU label connected by a hyphen (-) (example: PRODUCT000000001-J001), and specify the number of elements in `numTargets`. However, by specifying NULL for `targets` and 0 for `numTargets`, it is possible to target all products belonging to the service label specified in `serviceLabel` that are downloadable by the user specified in `userId`.

* When `mode` is `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM`, specify NULL for `targets` and 0 for `numTargets`.

For `features`, specify the premium feature type. Specify `SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY`.

This parameter specification is only valid when the display mode is `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM`. Specify 0 for modes other than `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM`.

An arbitrary pointer can be specified for `userData`. The pointer specified here is stored as is in the `userData` member of the [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.") structure when obtaining the dialog call result with [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog.").

Although parameters common to the common dialog must be specified in `baseParam` and the size of this structure in `size`; appropriate values for them are stored automatically with [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog."). It is not necessary to explicitly specify them in the program.

`reserved` is a reserved area. This area must be filled with 0's; however, it is automatically filled with 0's by [sceNpCommerceDialogParamInitialize()](sce-np-commerce-dialog-param-initialize.html "Initializes parameters for the NP commerce dialog.").

## Examples

```
SceNpCommerceDialogParam2 param;
sceNpCommerceDialogParamInitialize2( &param );
param.userId = user_id;
param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY;
const char *category_label[] = { "CATEGORY00000000" };
param.targets = category_label;
param.numTargets = 1;
```

## See Also

[SceNpCommerceDialogMode](sce-np-commerce-dialog-mode.html "NP commerce dialog display modes."), [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog."), [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.")

# sceNpCommerceDialogInitialize

Initializes the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
int32_t sceNpCommerceDialogInitialize()
```

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Value** | **Description** |
| --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_SYSTEM_INITIALIZED` | Common dialog process is not started. |
| `SCE_COMMON_DIALOG_ERROR_ALREADY_INITIALIZED` | NP commerce dialog is already initialized. |
| `SCE_COMMON_DIALOG_ERROR_BUSY` | Another common dialog is running. |
| `SCE_COMMON_DIALOG_ERROR_OUT_OF_MEMORY` | Insufficient memory. |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | Unexpected fatal error occurred. |

## Description

This function initializes the NP commerce dialog.

This function can only be called when no common dialog - including the NP commerce dialog itself - is being executed. `SCE_COMMON_DIALOG_ERROR_BUSY` returns if the function is called while another common dialog is running.

When the function call succeeds, the operation status immediately transitions from `SCE_COMMON_DIALOG_STATUS_NONE` to `SCE_COMMON_DIALOG_STATUS_INITIALIZED`.

For details on the operation status, see the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## Examples

```
if ( sceNpCommerceDialogInitialize() < 0 ) {
    // Error handling
}
```

## See Also

[sceNpCommerceDialogTerminate()](sce-np-commerce-dialog-terminate.html "Terminates the NP commerce dialog.")

# sceNpCommerceDialogParamInitialize2

Initializes parameters for the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
static inline
void sceNpCommerceDialogParamInitialize2(SceNpCommerceDialogParam2 *param)
{
    memset( param, 0x0, sizeof(SceNpCommerceDialogParam2) );

    _sceCommonDialogBaseParamInit( &param->baseParam );
    param->size = sizeof(SceNpCommerceDialogParam2);
}
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters to initialize. |

## Return Values

None

## Description

This function initializes the parameters for the NP commerce dialog.

Before setting the various parameters, make sure to initialize the parameters with this function.

Calling this function sets appropriate default values to each member of `param`. The application is not required to explicitly set values for members that are not used, for example, reserved area.

For details of each parameter, see [SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.").

## Examples

```
SceNpCommerceDialogParam2 param;
sceNpCommerceDialogParamInitialize2( &param );

param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY;
const char *category_label[] = { "CATEGORY00000000" };
param.target = category_label;
param.numTargets = 1;
param.serviceName = SCE_NP_SERVICE_PLAYSTATION_STORE_DELIVERED_CONTENTS;
if ( sceNpCommerceDialogOpen2( &param ) < 0 ) {
    // Error handling
```

## See Also

[SceNpCommerceDialogParam2](sce-np-commerce-dialog-param2.html "NP commerce dialog parameters.")

# sceNpCommerceDialogParamInitialize

Initializes parameters for the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
static inline
void sceNpCommerceDialogParamInitialize(SceNpCommerceDialogParam *param)
{
    memset( param, 0x0, sizeof(SceNpCommerceDialogParam) );

    _sceCommonDialogBaseParamInit( &param->baseParam );
    param->size = sizeof(SceNpCommerceDialogParam);
}
```

## Arguments

|  |  |
| --- | --- |
| `param` | Parameters to initialize. |

## Return Values

None

## Description

This function initializes the parameters for the NP commerce dialog.

Before setting the various parameters, make sure to initialize the parameters with this function.

Appropriate default values are set to each member of `*param` by calling this function; the application is not required to explicitly set values for members that are not used (reserved area, for example).

For details of each parameter, see [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.").

## Examples

```
SceNpCommerceDialogParam param;
sceNpCommerceDialogParamInitialize( &param );

param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CATEGORY;
const char *category_label[] = { "CATEGORY00000000" };
param.target = category_label;
param.numTargets = 1;
if ( sceNpCommerceDialogOpen( &param ) < 0 ) {
    // Error handling
```

## See Also

[SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.")

# sceNpCommerceDialogTerminate

Terminates the NP commerce dialog.

## Definition

```
#include <np_commerce_dialog.h>
int32_t sceNpCommerceDialogTerminate()
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for errors.

| **Error Code** | **Value** | **Description** |
| --- | --- | --- |
| `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` | `0x80B80003` | NP commerce dialog is not initialized. |
| `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL` | `0x80B8000E` | Unexpected fatal error occurred. |

## Description

This function terminates the NP commerce dialog.

After calling the NP commerce dialog with [sceNpCommerceDialogInitialize()](sce-np-commerce-dialog-initialize.html "Initializes the NP commerce dialog."), this function must ultimately be called to terminate the dialog.

To quickly abort dialog processing by the application, display can be terminated faster by calling this function rather than [sceNpCommerceDialogClose()](sce-np-commerce-dialog-close.html "Closes the NP commerce dialog.").

This function can be called regardless of the dialog's operation status as long as it is after the NP commerce dialog has been initialized with [sceNpCommerceDialogInitialize()](sce-np-commerce-dialog-initialize.html "Initializes the NP commerce dialog."). `SCE_COMMON_DIALOG_ERROR_NOT_INITIALIZED` returns if the NP commerce dialog is not initialized.

When the call of this function succeeds, the operation status immediately transitions to `SCE_COMMON_DIALOG_STATUS_NONE`.

For details on the operation status, see the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html).

## Examples

```
SceCommonDialogStatus stat = sceNpCommerceDialogUpdateStatus();
if( stat != SCE_COMMON_DIALOG_STATUS_NONE ) {
    sceNpCommerceDialogTerminate();
    break;
}
```

## See Also

[sceNpCommerceDialogInitialize()](sce-np-commerce-dialog-initialize.html "Initializes the NP commerce dialog."), [sceNpCommerceDialogUpdateStatus()](sce-np-commerce-dialog-update-status.html "Updates and gets operation status of the NP commerce dialog.")