# Param.json File Specification – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Param_Json-Specification/list-of-language-codes.html

# Param File (param.json) Specifications

Param files are written in the JSON format. If you are creating the param file using a
generic text editor, make sure the param file conforms to the JSON format: in particular, make
sure that the param file does not contain the byte order mark (BOM) character and that the
character encoding is UTF-8.

Refer to RFC8259 for other JSON specifications. Note that words in italics such as
*member* and *object* in this chapter are words defined in JSON
specifications.

Warning: Software behavior, including the behavior of the
system software and the Publishing Tools, is not guaranteed for param files that do not
conform to the specifications described in this chapter. Create and use param files
according to the specifications described in this chapter unless you are instructed
otherwise by SIE.

# Param File Examples

This topic contains example param files for an application, for additional content, for disc creation, and for an application that supports PlayStation®5 Pro.

## Example of a Param File for an Application

```
{
  "applicationCategoryType": 0,
  "applicationDrmType": "standard",
  "contentId": "IV9999-PPSA99999_00-XXXXXXXXXXXXXXXX",
  "titleId": "PPSA99999",
  "conceptId": "12345",
  "masterVersion": "01.00",
  "contentVersion": "01.000.000",
  "localizedParameters": {
    "defaultLanguage": "en-US",
    "en-US": {
      "titleName": "Sample Shooting Game"
    },
    "ja-JP": {
      "titleName": "サンプルシューティングゲーム"
    }
  },
  "attribute": 0,
  "attribute2": 0,
  "attribute3": 0,
  "downloadDataSize": 1024,
  "ageLevel": {
    "default": 15,
    "US": 10,
    "JP": 15
  },
  "kernel": {
    "flexibleMemorySize": 402653184
  },
  "amm": {
    "attribute": 1
  },
  "share": {
    "overlay_position": "upper_left"
  },
  "savedata": {
    "titleIdForSharing": "PPSA99998",
    "titleIdForTransferring": [ "PPSA99997", "PPSA99996" ]
  },
  "gameIntent": {
    "permittedIntents": [
      {
        "intentType": "launchActivity"
      },
      {
        "intentType": "joinSession"
      }
    ]
  },
  "versionFileUri": "http://sample.dl.playstation.net/somewhere.xml",
  "contentBadgeType": 1,
  "userDefinedParam1": 1,
  "userDefinedParam2": 2,
  "userDefinedParam3": 3,
  "userDefinedParam4": 4
}
```

## Example of a Param File for Additional Content

```
{
  "contentId": "IV9999-PPSA99999_00-XXXXXXXXXXXXXXAC",
  "titleId": "PPSA99999",
  "conceptId": "12345",
  "masterVersion": "01.00",
  "contentVersion": "01.000.000",
  "localizedParameters": {
    "defaultLanguage": "en-US",
    "en-US": {
      "titleName": "Sample Shooting Game Additional Content"
    },
    "ja-JP": {
      "titleName": "サンプルシューティングゲーム追加コンテンツ"
    }
  },
  "versionFileUri": "http://sample.dl.playstation.net/somewhere.xml"
}
```

## Example of a Param File for Disc Creation

```
{
  "localizedParameters": {
    "defaultLanguage": "en-US",
    "en-US": {
      "titleName": "XYZ Games Collection"
    },
    "ja-JP": {
      "titleName": "XYZゲームコレクション"
    }
  }
}
```

## Example of a Param File for an Application Supporting PlayStation®5 Pro

```
{
  "applicationCategoryType": 0,
  "applicationDrmType": "standard",
  "contentId": "IV9999-PPSA99999_00-XXXXXXXXXXXXXXXX",
  "titleId": "PPSA99999",
  "conceptId": "12345",
  "masterVersion": "01.00",
  "contentVersion": "01.000.000",
  "localizedParameters": {
    "defaultLanguage": "en-US",
    "en-US": {
      "titleName": "Sample Shooting Game"
    },
    "ja-JP": {
      "titleName": "サンプルシューティングゲーム"
    }
  },
  "attribute": 0,
  "attribute2": 0,
  "attribute3": 12582912,
  "downloadDataSize": 1024,
  "ageLevel": {
    "default": 15,
    "US": 10,
    "JP": 15
  },
  "kernel": {
    "flexibleMemorySize": 402653184
  },
  "amm": {
    "attribute": 1
  },
  "share": {
    "overlay_position": "upper_left"
  },
  "savedata": {
    "titleIdForSharing": "PPSA99998",
    "titleIdForTransferring": [ "PPSA99997", "PPSA99996" ]
  },
  "gameIntent": {
    "permittedIntents": [
      {
        "intentType": "launchActivity"
      },
      {
        "intentType": "joinSession"
      }
    ]
  },
  "versionFileUri": "http://sample.dl.playstation.net/somewhere.xml",
  "contentBadgeType": 1,
  "userDefinedParam1": 1,
  "userDefinedParam2": 2,
  "userDefinedParam3": 3,
  "userDefinedParam4": 4
}
```

# Parameter Definitions for Applications

This topic documents the parameters for applications, including their types, and their possible values.

## applicationCategoryType

Meaning: represents the application category

Required or optional: required

Parameter type: *number*

Parameter value: specify 0

## applicationDrmType

Meaning: represents the DRM type of the application

Required or optional: required

Parameter type: *string*

Parameter value: set "standard", "upgradable", or "demo". For details about these values, refer to [PlayStation™Store Content Guidelines - PlayStation™Store Content Guidelines Overview - Entitlements and Game Package Types](../PlayStation_Store_Content-Guidelines/entitlements-and-game-package-types.html).

## contentId

Meaning: represents the Content ID. Refer to the [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html) document for details on Content IDs.

Required or optional: required

Parameter type: *string*

## titleId

Meaning: represents the title ID, which is a part of the Content ID. Refer to the [Publishing Tools Overview](../Publishing_Tools-Overview/__document_toc.html) document for details on title IDs.

Required or optional: required

Parameter type: *string*

## conceptId

Meaning: represents the Concept ID. Concept IDs are issued by SIE.

Required or optional: required

Parameter type: *string*

Parameter value: specify the concept ID corresponding to the concept type in Content Pipeline.

Note: The value of this parameter is obtained from GEMS. Set the value obtained from GEMS without changing it. For details, refer to the [Parameters Obtained from GEMS](parameters-obtained-from-gems.html "Some parameter values are obtained from GEMS and must be copied into your param.json file. These values are included in the param_cp_values.json file, which is contained in npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS), and, as a general rule, copy the values found in the included JSON file (param_cp_values.json) into your param.json file without changing them.") section.

## masterVersion

Meaning: represents the version of an application or additional content to be submitted. The value must match the MDT Form Version. Refer to the [CertOps Submission Guide](https://learn.playstation.net/bundle/certops-guide/page/certops_submission_guide.html) for details.

Required or optional: required

Parameter type: *string*

Parameter value: specify "xx.xx" (where x is a numeric value from 0 to 9).

## contentVersion

Meaning: represents the version of an application or additional content to be updated. Refer to the [Content Packaging and Updating Guide](../Content_Packaging_and_Updating-Guide/__document_toc.html) document for details.

Required or optional: required

Parameter type: *string*

Parameter value: specify "xx.xxx.xxx" (where x is a numeric value from 0 to 9). Specify "01.000.000" for the initial release package and specify a value larger than "01.000.000" when updating a package after the initial release. The version value must be larger than the ones for previous updates.

## localizedParameters

Meaning: represents an *object* that stores parameters localized for each language

Required or optional: required

Parameter type: *object*

Parameters that can be stored in this *object*: "defaultLanguage", <language code>

## localizedParameters/defaultLanguage

Meaning: represents the language code of the default language. The default language will be used by the system software (for example) as a substitute when the user selects a language that isn't stored in localizedParameters.

Required or optional: required

Parameter type: *string*

Parameter value: set one of the language codes described in the [List of Language Codes](list-of-language-codes.html "Use the following language codes for the localizedParameters and <language code> parameters.") section. The set language code must be stored in localizedParameters.

## localizedParameters/<language code>

Meaning: represents an *object* that stores a parameter for the applicable language

Required or optional: required for <language code> specified for defaultLanguage and optional for other <language code>.

Parameter type: *object*

Parameter that can be stored in this *object*: "titleName"

## localizedParameters/<language code>/titleName

Meaning: represents the name of the content

Required or optional: required

Parameter type: *string*

## attribute

Meaning: represents configuration values

Required or optional: required

Parameter type: *number*

Parameter values: set according to the table below

| Item | Value |
| --- | --- |
| User Management | Represents whether or not the application supports login/logout of the user who started the application. Refer to the [User Management Overview](../User_Management-Overview/__document_toc.html) document for details.  When login/logout of the initial user is not supported (when the InitialUserAlwaysLoggedIn mode is enabled): +0  When login/logout of the initial user is supported (when the InitialUserAlwaysLoggedIn mode is disabled): +1 |
| HDR | Represents whether or not the application supports high dynamic range (HDR) rendering. Refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) document for details on HDR rendering.  When HDR rendering is not supported: +0  When HDR rendering is supported: +536870912 (0x20000000) |

## attribute2

Meaning: represents configuration values

Required or optional: required

Parameter type: *number*

Parameter values: set according to the table below

| Item | Value |
| --- | --- |
| ContentSearch library | Represents whether or not the application uses the ContentSearch library. Refer to the [ContentSearch Library Overview](../ContentSearch-Overview/__document_toc.html) document for details on the ContentSearch library.  When the ContentSearch library is not used: +0  When the ContentSearch library is used: +4 |

## attribute3

Meaning: represents configuration values

Required or optional: required

Parameter type: *number*

Parameter values: set according to the table below

| Item | Value |
| --- | --- |
| Video-out Info | Represents whether or not output resolution information can be obtained. Refer to `SceVideoOutOutputResolution` and `SceVideoOutOutputStatus` for details.  When output resolution information is not obtained: +0  When output resolution information is obtained: +4 |
| Share library Capture API | Represents whether the application uses the Capture API of the Share library. For details about the Share library, refer to the [Share Library Overview](../Share-Overview/__document_toc.html) document.  When the Capture API of the Share library is not used: +0  When the Capture API of the Share is used: +16 |
| HFR | Represents whether or not the application supports HFR output. Refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) document for details on HFR output.  When HFR output is not supported: +0  When HFR output is supported: +64 |
| Scaling to the Display's Safe Area | Represents whether or not to disable scaling to the display's safe area by the system. Refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) for details.  To enable scaling: +0  To disable scaling: +128 |
| Beta | Represents whether the application is a beta version.  If not a beta version: +0  If a beta version: +256 |
| PlayStation®VR2 | Represents whether the application supports or requires PlayStation®VR2. Refer to the [Virtual Reality System Overview](../Virtual_Reality_System-Overview/__document_toc.html) document for details.  If the application does not support PlayStation®VR2: +0  If the application supports PlayStation®VR2: +1024  If the application requires PlayStation®VR2: +3072 |
| Display of Start-up Image | Represents whether the foreground image of the start-up image will be displayed quickly. Refer to [Content Information Specifications - Startup Image [Application Information]](../Content_Information-Specifications/startup-image-application-information.html) for details.  If not displayed quickly (pattern A): +0  If displayed quickly (pattern B): +4096 |
| PlayStation®VR2: Detailed Gaze Tracking Status | Represents whether or not Gaze Tracking Status can report additional details when `sceHmd2GazeGetResult()` and similar related APIs are called.  Refer to the [Virtual Reality System Overview](../Virtual_Reality_System-Overview/__document_toc.html) document for details.  If additional details are disabled: +0  If additional details are enabled: +8192 |
| UTC L1 Large Page Table Size | Represents whether the application uses enlarged page table size for UTC L1 (2MiB) or not (64KiB).  Refer to the [GPU Overview](../GPU-Overview/__document_toc.html) document for details.  UTC L1 Page Table Size 64KiB: +0  UTC L1 Page Table Size 2MiB: +16384 |
| PlayStation®VR2: Play Area | Represents Play Areas supported by the application.  Refer to the [Virtual Reality System Overview](../Virtual_Reality_System-Overview/__document_toc.html) document for details.  If the application supports both Stationary and Roomscale Play Area: +0  If the application supports Roomscale Play Area only: +65536  If the application supports Stationary Play Area only: +131072 |
| VRR | Represents the type of Variable Refresh Rate (VRR) that the application supports.  Refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) for details.  If the VRR setting of the application is determined by the system software: +0  If the application supports VRR Type A: +262144  If the application supports VRR Type B: +524288  If the application never supports VRR: +1835008 |
| PlayStation®5 Pro | Represents whether or not the application supports the Trinity mode.  When the Trinity mode is not supported: +0  When the Trinity mode is supported: +4194304 |
| 8K resolution | Represents whether or not the application supports 8K resolution output for PlayStation®5 Pro.  Refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) for details.  When 8K resolution output is not supported: +0  When 8K resolution out is supported: +8388608 |
| PlayStation®VR2: Camera SeeThrough | Represents whether or not the application uses Camera SeeThrough feature.  Refer to the [Hmd2 Library Overview](../Hmd2-Overview/__document_toc.html) document for details.  If the application does not use Camera SeeThrough feature: +0  If the application uses Camera SeeThrough feature: +16777216 |
| Overlay Port | Represents whether or not the application supports Overlay Port.  Refer to the [VideoOut Library Overview](../VideoOut-Overview/__document_toc.html) document for details.  If the application does not support Overlay Port: +0  If the application supports Overlay Port: +33554432 |
| PlayStation®VR2: Hand Tracking | Represents whether or not the application uses Hand Tracking feature.  Refer to the [VrHand Library Overview](../VrHand-Overview/__document_toc.html) document for details.  If the application does not use Hand Tracking feature: +0  If the application uses Hand Tracking feature: +67108864 |
| CPU and GPU frequency control | Represents the upper limit setting for the CPU frequency for PlayStation®5 Pro.  Refer to the [Kernel Overview](../Kernel-Overview/__document_toc.html) document for details.  When Standard is selected: +0  When High CPU Frequency is selected: +134217728 |
| PlayStation®VR2: MFSR | Represents whether or not the application uses MFSR in VR mode.  Refer to the [PlayStation®VR2 Design Guide](../Virtual_Reality_Design_Guide/__document_toc.html) and [PSML MFSR Overview](../PSML_MFSR-Overview/__document_toc.html) document for details.  If the application does not use MFSR in VR mode: +0  If the application uses MFSR in VR mode: +1073741824 |

## attribute4

Meaning: represents configuration values

Required or optional: optional

Parameter type: *number*

Parameter values: set according to the table below

| Item | Value |
| --- | --- |
| Low Energy Mode | Represents whether or not the application supports Low Energy Mode. When Low Energy Mode is not supported: +0  When Low Energy Mode is supported: +1 |

## attributePub

Meaning: represents configuration values

Required or optional: optional

Parameter type: *number*

Parameter values: set according to the table below

| Item | Value |
| --- | --- |
| Large Package Size support | Represents maximum size of application package.  A package for development that exceeds 154986MiB in size can be created by setting this value to 1.  To create a package for master submission that exceeds 154986MiB in size, SIE's approval and an ASA code is required as well as setting this value to 1.  Maximum package size 154986MiB: +0  Maximum package size 186804MiB: +1 |

## downloadDataSize

Meaning: represents the size of the download data area. Specify the required size in MiB if your application uses the download data area. Refer to the [AppContent Library Overview](../AppContent-Overview/__document_toc.html) and [Application Content Overview](../Application_Content-Overview/__document_toc.html) documents for details on the download data area.

The value of this parameter, and the size of the download data area, cannot be made smaller when the param file is updated.

Required or optional: optional

Parameter type: *number*

Parameter value: set 0, 256, 512, or 1024

## ageLevel

Meaning: represents the Age Level for Boot Restriction. Set the age at which users (with PlayStation™Network accounts) in the applicable country/region can launch the application to ageLevel/<country/region code>. Set this parameter for at least one country/region.

Required or optional: required

Parameter type: *object*

Parameters that can be stored in this *object*: "default", <country/region code>

Parameter value: set a value pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html).

Note: The value of this parameter is usually obtained from GEMS. It is recommended that the value obtained from GEMS be set without changing it. If the value obtained from GEMS is old, change it to an appropriate value or add a new value pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html). For details, refer to the [Parameters Obtained from GEMS](parameters-obtained-from-gems.html "Some parameter values are obtained from GEMS and must be copied into your param.json file. These values are included in the param_cp_values.json file, which is contained in npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS), and, as a general rule, copy the values found in the included JSON file (param_cp_values.json) into your param.json file without changing them.") section.

## ageLevel/default

Meaning: represents the age level that will be applied to users in a country/region where ageLevel/<country/region code> has not been set. This age level will also be applied to users for whom the country/region has not been set for the PlayStation™Network account in the system software.

Required or optional: required

Parameter type: *number*

Parameter value: set a value pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html).

Note: The value of this parameter is usually obtained from GEMS. It is recommended that the value obtained from GEMS be set without changing it. If the value obtained from GEMS is old, change it to an appropriate value or add a new value pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html). For details, refer to the [Parameters Obtained from GEMS](parameters-obtained-from-gems.html "Some parameter values are obtained from GEMS and must be copied into your param.json file. These values are included in the param_cp_values.json file, which is contained in npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS), and, as a general rule, copy the values found in the included JSON file (param_cp_values.json) into your param.json file without changing them.") section.

## ageLevel/<country/region code>

Meaning: represents the age level on a per-country/region basis. For <country/region code>, set one of the country/region codes listed in the [List of Country/Region Codes](list-of-country-region-codes.html "Use the following country/region codes for the <country/region code> parameter.") section.

Required or optional: It is a requirement to set at least one country/region. Setting two or more countries/regions is optional.

Parameter type: *number*

Parameter value: specify the age level (0 to 127).

Parameter value: set a value pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html).

Note: The value of this parameter is usually obtained from GEMS. It is recommended that the value obtained from GEMS be set without changing it. If the value obtained from GEMS is old, change it to an appropriate value or add a new value pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html). For details, refer to the [Parameters Obtained from GEMS](parameters-obtained-from-gems.html "Some parameter values are obtained from GEMS and must be copied into your param.json file. These values are included in the param_cp_values.json file, which is contained in npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS), and, as a general rule, copy the values found in the included JSON file (param_cp_values.json) into your param.json file without changing them.") section.

## kernel

Meaning: represents an *object* that stores parameters related to kernel features.

Required or optional: optional

Parameter type: *object*

## kernel/flexibleMemorySize

## kernel/cpuPageTableSize

## kernel/gpuPageTableSize

Meaning: represent parameters used with kernel features. For details, refer to the [Kernel Overview](../Kernel-Overview/__document_toc.html) document.

Required or optional: optional

Parameter type: *number*

## amm

Meaning: An *object* that stores parameters related to the AMM library.

Required or optional: optional

Parameter type: *object*

## amm/pagetableMemorySizeInMib

## amm/vaRangeInGib

## amm/multimapVaRangeInGib

Meaning: Represent parameters used with the AMM library. For details, refer to the [Kernel Overview](../Kernel-Overview/__document_toc.html) document.

Required or optional: optional

Parameter type: *number*

## share

Meaning: represents an *object* that stores parameters related to Share features.

Required or optional: optional

Parameter type: *object*

## share/overlay\_position

Meaning: represents the position of an overlay image. For details, refer to the [Share Library Overview](../Share-Overview/__document_toc.html) document.

Required or optional: optional

Parameter type: *string*

Parameter value: set "upper\_left", "upper\_right", "lower\_left", or "lower\_right"

## savedata

Meaning: represents an *object* that stores parameters related to save data

Required or optional: optional

Parameter type: *object*

## savedata/titleIdForSharing

Meaning: represents the title ID for when save data is shared. Specify the title ID of the share target application if your application uses the save data sharing feature. Refer to the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document for details.

Required or optional: optional

Parameter type: *string*

## savedata/titleIdForTransferring

Meaning: represents the title ID(s) for when save data is transferred. Specify the title ID(s) of the transfer target application(s) in *array* if your application uses the save data transferring feature. Refer to the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document for details.

Required or optional: optional

Parameter type: *array*

## savedata/titleIdForTransferringPs4

Meaning: represents the title ID(s) for when save data is transferred from PlayStation®4 applications. Specify the title ID(s) of the transfer target application(s) in *array* if your application uses the save data transferring feature. Refer to the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document for details.

Required or optional: optional

Parameter type: *array*

## gameIntent

Meaning: represents an *object* that stores parameters related to game intent.

Required or optional: optional

Parameter type: *object*

## gameIntent/permittedIntents

Meaning: represents an *array* that stores the game intents that the application is permitted to receive. For details, refer to the [Game Intent System Overview](../Game_Intent_System-Overview/__document_toc.html) and [NpGameIntent Library Overview](../NpGameIntent-Overview/__document_toc.html) documents.

Required or optional: required if there exists a gameIntent parameter

Parameter type: *array*

## systemService

Meaning: represents an *object* that stores parameters related to the SystemService library.

Required or optional: optional

Parameter type: *object*

## systemService/noticeScreenVersion

Meaning: represents version number to manage whether notice screens can be skipped. For details, refer to the [SystemService Library Overview](../SystemService-Overview/__document_toc.html) document.

Required or optional: optional

Parameter type: *number*

## psml

Meaning: represents an object that stores parameters related to the Psml library.

Required or optional: optional

Parameter type: object

## psml/mfsrVersion

Meaning: represents a parameter used by the Psml library. For details, refer to the [PSML MFSR Overview](../PSML_MFSR-Overview/__document_toc.html) document.

Required or optional: optional

Parameter type: string

## versionFileUri

Meaning: indicates the URI used to obtain package updates.

Required or optional: required

Parameter type: *string*

Note: The value of this parameter is obtained from GEMS. Set the value obtained from GEMS without changing it. For details, refer to the [Parameters Obtained from GEMS](parameters-obtained-from-gems.html "Some parameter values are obtained from GEMS and must be copied into your param.json file. These values are included in the param_cp_values.json file, which is contained in npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS), and, as a general rule, copy the values found in the included JSON file (param_cp_values.json) into your param.json file without changing them.") section.

## contentBadgeType

Meaning: used to evaluate the application type (for classifying a game in a game hub, for example).

Required or optional: required

Parameter type: *number*

Parameter value: specify 1 if the source product in Content Pipeline for which the NP Title ID was issued is a "game" or "demo" and specify 2 if the product is an "application".

Note: The value of this parameter is obtained from GEMS. Set the value obtained from GEMS without changing it. For details, refer to the [Parameters Obtained from GEMS](parameters-obtained-from-gems.html "Some parameter values are obtained from GEMS and must be copied into your param.json file. These values are included in the param_cp_values.json file, which is contained in npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS), and, as a general rule, copy the values found in the included JSON file (param_cp_values.json) into your param.json file without changing them.") section.

## userDefinedParam1 to userDefinedParam4

Meaning: represents user defined parameters that can be arbitrarily defined by a developer and used in an application. Refer to the [AppContent Library Reference](../AppContent-Reference/__document_toc.html) document for details about user defined parameters.

Required or optional: optional

Parameter type: *number*

Parameter value: specify an integer value between 0 and 4294967295 (232- 1)

## asa

## asa/code

## asa/sign

Meaning: represent parameters (called ASA codes) that SIE issues for applications that use special features. For details about ASA codes, refer to the [ASA Codes](asa-codes.html "If an application uses a special feature, SIE may issue a parameter called an ASA code. ASA codes are in JSON object format and are issued on a per-content ID basis. If you have been issued an ASA code, store it unmodified in the param file for your application.") section.

Required or optional: optional

Parameter type: *object* (asa, asa/code), *array* (asa/sign)

Parameter value: Specify the value issued by SIE without modification.

# Parameter Definitions for Additional Content

The following are defined as parameters for additional content. Store only the
parameters defined here in param files for additional content.

* `contentId`
* `titleId`
* `conceptId`
* `masterVersion`
* `contentVersion`
* `localizedParameters`
* `localizedParameters/defaultLanguage`
* `localizedParameters/` <language code>
* `localizedParameters/`<language code>`/titleName`
* `versionFileUri`

The meaning of each parameter for additional content is the same as that for the parameter for an application; therefore, refer to the [Parameter Definitions for Applications](parameter-definitions-for-applications.html "This topic documents the parameters for applications, including their types, and their possible values.") section.

# Parameter Definitions for Additional Content Without Extra Data (PSAL)

The following are defined as parameters for additional content without extra data
(PSAL). Store only the parameters defined here in param files for additional content without
extra data (PSAL).

* `contentId`
* `titleId`
* `conceptId`
* `masterVersion`
* `localizedParameters`
* `localizedParameters/defaultLanguage`
* `localizedParameters/` <language code>
* `localizedParameters/`<language code>`/titleName`

The meaning of each parameter for additional content without extra data (PSAL) is the same as that for the parameter for an application; therefore, refer to the [Parameter Definitions for Applications](parameter-definitions-for-applications.html "This topic documents the parameters for applications, including their types, and their possible values.") section.

# Parameter Definitions for Disc Creation

Param files for disc creation are used to specify the disc title name when creating a
compilation disc. The specification of the disc title name includes localized values. The
following are defined as parameters for disc creation. Store only the parameters defined here
in param files for disc creation.

* `localizedParameters`
* `localizedParameters/defaultLanguage`
* `localizedParameters/`<language code>
* `localizedParameters/`<language code>`/titleName`

For more information on creating compilation discs, refer to the [Content Packaging and
Updating Guide](../Content_Packaging_and_Updating-Guide/__document_toc.html) and [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) documents.

# Parameters Obtained from GEMS

Some parameter values are obtained from GEMS and must be copied into your param.json
file. These values are included in the param\_cp\_values.json file, which is contained in
npconfig.zip. Download the npconfig.zip file from the Package/Disc Management Tool (GEMS),
and, as a general rule, copy the values found in the included JSON file (param\_cp\_values.json)
into your param.json file without changing them.

Of the following parameters, regarding `conceptId` and `contentBadgeType`, verification on GEMS will result in an error if there is discrepancy with the values in Content Pipeline. For `ageLevel`, a value discrepancy will be handled as a warning instead of an error because it's possible that rating information hasn't been set in Content Pipeline. Upon release of the product, however, make sure there is no discrepancy with the obtained rating pursuant to TRC [R5005](../../../TRC/latest/TRC/R5005.html).

## Parameters for Applications

* `conceptId`
* `ageLevel (including ageLevel/default, etc.)`
* `versionFileUri`
* `contentBadgeType`

## Parameters for Additional Content

There is one npconfig.zip file per title, so for additional content, set values that are shared with the application.

* `conceptId`
* `versionFileUri`

## Parameters for Additional Content Without Extra Data (PSAL)

There is one npconfig.zip file per title, so for additional content without extra data (PSAL), set values that are shared with the application.

* `conceptId`

For GEMS and npconfig.zip files, refer to the [Package/Disc Management Tool (GEMS)
Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) document.

# List of Language Codes

Use the following language codes for the localizedParameters and <language code>
parameters.

| Language | Language Code |
| --- | --- |
| Arabic | ar-AE |
| Czech | cs-CZ |
| Danish | da-DK |
| German | de-DE |
| Greek | el-GR |
| English (United Kingdom) | en-GB |
| English (United States) | en-US |
| Spanish (Latin America) | es-419 |
| Spanish (Spain) | es-ES |
| Finnish | fi-FI |
| French (Canada) | fr-CA |
| French (France) | fr-FR |
| Hungarian | hu-HU |
| Indonesian | id-ID |
| Italian | it-IT |
| Japanese | ja-JP |
| Korean | ko-KR |
| Dutch | nl-NL |
| Norwegian | no-NO |
| Polish | pl-PL |
| Portuguese (Brazil) | pt-BR |
| Portuguese (Portugal) | pt-PT |
| Romanian | ro-RO |
| Russian | ru-RU |
| Swedish | sv-SE |
| Thai | th-TH |
| Turkish | tr-TR |
| Vietnamese | vi-VN |
| Chinese (Simplified) | zh-Hans |
| Chinese (Traditional) | zh-Hant |
| Ukrainian | uk-UA |

# List of Country/Region Codes

Use the following country/region codes for the <country/region code>
parameter.

| Country/Region Name | Country/Region Code |
| --- | --- |
| United States | US |
| Canada | CA |
| Mexico | MX |
| Chile | CL |
| Argentina | AR |
| Brazil | BR |
| Peru | PE |
| Colombia | CO |
| Panama | PA |
| Costa Rica | CR |
| Ecuador | EC |
| Guatemala | GT |
| El Salvador | SV |
| Paraguay | PY |
| Honduras | HN |
| Bolivia | BO |
| Uruguay | UY |
| Nicaragua | NI |
| UK | GB |
| Ireland | IE |
| Belgium | BE |
| Luxembourg | LU |
| Netherlands | NL |
| France | FR |
| Germany | DE |
| Austria | AT |
| Switzerland | CH |
| Italy | IT |
| Portugal | PT |
| Denmark | DK |
| Finland | FI |
| Norway | NO |
| Sweden | SE |
| Australia | AU |
| New Zealand | NZ |
| Spain | ES |
| Russia | RU |
| UAE | AE |
| South Africa | ZA |
| Poland | PL |
| Greece | GR |
| Saudi Arabia | SA |
| Czech Republic | CZ |
| Turkey | TR |
| India | IN |
| Croatia | HR |
| Slovenia | SI |
| Kuwait | KW |
| Israel | IL |
| Ukraine | UA |
| Bulgaria | BG |
| Hungary | HU |
| Qatar | QA |
| Romania | RO |
| Bahrain | BH |
| Lebanon | LB |
| Oman | OM |
| Malta | MT |
| Cyprus | CY |
| Slovakia | SK |
| Iceland | IS |
| Hong Kong | HK |
| Taiwan | TW |
| Singapore | SG |
| Malaysia | MY |
| Indonesia | ID |
| Thailand | TH |
| China | CN |
| Korea | KR |
| Japan | JP |

# ASA Codes

If an application uses a special feature, SIE may issue a parameter called an ASA code.
ASA codes are in JSON *object* format and are issued on a per-content ID basis. If you have
been issued an ASA code, store it unmodified in the param file for your application.

## Example of an ASA Code

```
"asa": {
    "code": {
      "asa01": "1"
    },
    "sign": [
      "EgjBqv+XAeSUzw8FRtgHoJ4ZwOfqUaJi0vj1gM/4Sv8j85Oi/SAnep9hVeuiltYU",
      (Omitted)
      "0jRlHwP+yYoqXCeUuzHLFMvV89i1UhKiHsE5W550mejN5YXkm/wQcbc1uH9HjrKa"
    ]
  }
```

## Example of a Param File with an Embedded ASA Code

```
{
  "applicationCategoryType": 0,
  "applicationDrmType": "standard",
  "contentId": "IV9999-PPSA99999_00-0000000000000000",
  "titleId": "PPSA99999",
  (Omitted)
  "attribute": 0,
  "attribute2": 0,
  "attribute3": 0,
  "asa": {
    "code": {
      "asa01": "1"
    },
    "sign": [
      "EgjBqv+XAeSUzw8FRtgHoJ4ZwOfqUaJi0vj1gM/4Sv8j85Oi/SAnep9hVeuiltYU",
      (Omitted)
      "0jRlHwP+yYoqXCeUuzHLFMvV89i1UhKiHsE5W550mejN5YXkm/wQcbc1uH9HjrKa"
    ]
  }
}
```