# NpCommerceDialog Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpCommerceDialog-Reference/parameter-error-codes.html

# Constants

# Parameter Error Codes

Code output when the parameter content specified to the NP commerce dialog is invalid.

## Definition

| **Value** | **Description** |
| --- | --- |
| `1` | [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.") is NULL. |
| `2` | [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.") `.reserved` is invalid. |
| `3` | [SceNpCommerceDialogParam](sce-np-commerce-dialog-param.html "NP commerce dialog parameters.") `.mode` is invalid. |
| `100` | [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.") is NULL. |
| `101` | [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.") `.reserved` is invalid. |

## Description

When the content of the parameter structure specified in each function of the NpCommerceDialog library is invalid, `SCE_COMMON_DIALOG_ERROR_PARAM_INVALID` is stored in [SceNpCommerceDialogResult](sce-np-commerce-dialog-result.html "Result of calling the NP commerce dialog.")`.result` that can be obtained by calling [sceNpCommerceDialogGetResult()](sce-np-commerce-dialog-get-result.html "Gets result of calling the NP commerce dialog.").

Furthermore, detailed position of the parameter error occurrence is output to the console in the following format.

```
****** SceNpCommerceDialog Parameter Error : XX ******
(XX stands for one of the values in the definitions above)
```

A parameter error is a coding mistake in the application that must be fixed before release.