# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/sce-np-online-id.html

# Common Datatypes

# SceNpServiceLabel

NP service label

## Definition

```
#include <np/np_common.h>
typedef uint32_t SceNpServiceLabel;
#define SCE_NP_INVALID_SERVICE_LABEL (0xFFFFFFFF)
```

## Description

This integer indicates the NP service label.

An NP service label is an identifier that specifies when an NP title ID handles multiple service instances. NP service label values can be set when requesting usage of PlayStation™Network services. For the details of how to make a PlayStation™Network service request, refer to [PlayStation™Network Service Setup Guide - Making Service Requests - Service Request Overview](../PSN_Service_Setup-Guide/service-request-overview.html). For the ranges of values that can be specified for NP service labels, refer to [PlayStation™Network Service Setup Guide - Appendix B: Ranges of NP Service Labels That Can Be Specified](../PSN_Service_Setup-Guide/appendix-b-ranges-of-np-service-labels-tha.html).

# SceNpAccountId

Account ID

## Definition

```
#include <np/np_common.h>
typedef uint64_t SceNpAccountId;
```

## Description

This integer indicates the account ID. For details, refer to the "Basic Information for Accounts" section of the "Accounts" chapter of the [Np Library Overview](../Np-Overview/__document_toc.html) document.

# SceNpOnlineId

Online ID

## Definition

```
#define SCE_NP_ONLINEID_MIN_LENGTH		3
#define SCE_NP_ONLINEID_MAX_LENGTH		16
typedef struct SceNpOnlineId {
	char data[SCE_NP_ONLINEID_MAX_LENGTH];
	char term;
	char dummy[3];
} SceNpOnlineId;
```

## Members

|  |  |
| --- | --- |
| `data` | Online ID character string |
| `term` | Area for termination character for terminating `data` |
| `dummy` | (not used) |

## Description

This structure represents a user's Online ID. For details, refer to the "Basic Information for Accounts" section of the "Accounts" chapter of the [Np Library Overview](../Np-Overview/__document_toc.html) document.

# SceNpTitleId

NP Title ID

## Definition

```
#include <np/np_common.h>
#define SCE_NP_TITLE_ID_LEN          12
typedef struct SceNpTitleId {
	char id[SCE_NP_TITLE_ID_LEN + 1];
	uint8_t padding[3];
} SceNpTitleId;
```

## Members

|  |  |
| --- | --- |
| `id` | NP Title ID string  (specify the value issued by the PlayStation®5 Developer Network) |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the NP Title ID.

To have an NP Title ID issued, make a request through the PlayStation®5 Developer Network website.

# SceNpTitleSecret

NP Title Secret

## Definition

```
#include <np/np_common.h>
#define SCE_NP_TITLE_SECRET_SIZE          (128)
typedef struct SceNpTitleSecret {
	uint8_t data[SCE_NP_TITLE_SECRET_SIZE];
} SceNpTitleSecret;
```

## Members

|  |  |
| --- | --- |
| `data` | NP Title Secret data  (specify the value issued by the PlayStation®5 Developer Network) |

## Description

This structure represents the NP Title Secret.

To have an NP Title Secret issued, make a request through the PlayStation®5 Developer Network website.

# SceNpClientId

Client ID

## Definition

```
#include <np/np_common.h>
#define SCE_NP_CLIENT_ID_MAX_LEN          128
typedef struct SceNpClientId {
	char id[SCE_NP_CLIENT_ID_MAX_LEN + 1];
	uint8_t padding[7];
} SceNpClientId;
```

## Members

|  |  |
| --- | --- |
| `id` | Client ID string  (specify the value issued by the PlayStation®5 Developer Network) |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the client ID. It is used when using the NpAuth library to obtain an authorization code for use with an application server. For details, refer to the [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html) document.

# SceNpClientSecret

Client secret

## Definition

```
#include <np/np_common.h>
#define SCE_NP_CLIENT_SECRET_MAX_LEN	(256)
typedef struct SceNpClientSecret {
	char secret[SCE_NP_CLIENT_SECRET_MAX_LEN + 1];
	uint8_t padding[7];
} SceNpClientSecret;
```

## Members

|  |  |
| --- | --- |
| `secret` | Client secret string  (specify the value issued by the PlayStation®5 Developer Network) |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the client secret. It is used when using the NpAuth library to obtain an authorization code for use with an application server. For details, refer to the [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html) and [NpAuth Library Reference](../NpAuth-Reference/__document_toc.html) documents.

# SceNpAuthorizationCode

Authorization code

## Definition

```
#include <np/np_common.h>
#define SCE_NP_AUTHORIZATION_CODE_MAX_LEN          128
typedef struct SceNpAuthorizationCode {
	char code[SCE_NP_AUTHORIZATION_CODE_MAX_LEN + 1];
	uint8_t padding[7];
} SceNpAuthorizationCode;
```

## Members

|  |  |
| --- | --- |
| `code` | Authorization code string |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the authorization code.

For details about authorization codes, refer to the [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html) document.

# SceNpIdToken

ID token

## Definition

```
#include <np/np_common.h>
#define SCE_NP_ID_TOKEN_MAX_LEN			4096
typedef struct SceNpIdToken {
	char token[SCE_NP_ID_TOKEN_MAX_LEN + 1];
	uint8_t padding[7];
} SceNpIdToken;
```

## Members

|  |  |
| --- | --- |
| `token` | ID token string |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the ID token.

For details about ID tokens, refer to the [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html), [NpAuth Library Overview](../NpAuth-Overview/__document_toc.html), and [NpAuth Library Reference](../NpAuth-Reference/__document_toc.html) documents.

# SceNpPeerAddressA

Peer address

## Definition

```
#include <np/np_common.h>

typedef struct SceNpPeerAddressA {
	SceNpAccountId accountId;
	SceNpPlatformType platform;
	char padding[4];
} SceNpPeerAddressA;
```

## Members

|  |  |
| --- | --- |
| `accountId` | Account ID |
| `platform` | Platform type |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the peer address.

# SceNpLanguageCode2

Language code

## Definition

```
#include <np/np_common.h>
#define SCE_NP_LANGUAGE_CODE_2_MAX_LEN          (35)
typedef struct SceNpLanguageCode2{
	char code[SCE_NP_LANGUAGE_CODE_2_MAX_LEN + 1];
	uint8_t padding[12];
} SceNpLanguageCode2;
```

## Members

|  |  |
| --- | --- |
| `code` | Language code string |
| `padding` | Not used (clear with 0's) |

## Description

This structure represents the language code.

Check the [Auth Web API Overview](../../../WebAPI/latest/Auth_WebAPI-Overview/__document_toc.html) document for details about language codes and the corresponding languages supported by PlayStation™Network. Additions/corrections may be made as needed to the support status of language codes, regardless of SDK updates. Program applications so that application progress is possible even if a language code not listed is obtained.

# SceNpCountryCode

Country/region code

## Definition

```
#include <np/np_common.h>
#define SCE_NP_COUNTRY_CODE_LENGTH          2
typedef struct SceNpCountryCode {
	char data[SCE_NP_COUNTRY_CODE_LENGTH];
	char term;
	char padding[1];
} SceNpCountryCode;
```

## Members

|  |  |
| --- | --- |
| `data` | Country/region code (ISO 3166-1) |
| `term` | Area for termination character for terminating `data` |
| `padding` | Padding |

## Description

This structure indicates the country/region. `data` is a 2-byte ASCII code indicating the country/region code defined in ISO 3166-1.

The countries/regions currently supported by PlayStation™Network are as follows. The supported countries/regions may change or be corrected as needed independently from SDK updates. The application must not malfunction even if a country/region code other than those shown here is obtained.

| `data` | **Country/region** |
| --- | --- |
| `ae` | UAE |
| `ar` | Argentina |
| `at` | Austria |
| `au` | Australia |
| `be` | Belgium |
| `bg` | Bulgaria |
| `bh` | Bahrain |
| `bo` | Bolivia |
| `br` | Brazil |
| `ca` | Canada |
| `ch` | Switzerland |
| `cl` | Chile |
| `cn` | China |
| `co` | Colombia |
| `cr` | Costa Rica |
| `cy` | Cyprus |
| `cz` | Czech Republic |
| `de` | Germany |
| `dk` | Denmark |
| `ec` | Ecuador |
| `es` | Spain |
| `fi` | Finland |
| `fr` | France |
| `gb` | UK |
| `gr` | Greece |
| `gt` | Guatemala |
| `hk` | Hong Kong |
| `hn` | Honduras |
| `hr` | Croatia |
| `hu` | Hungary |
| `id` | Indonesia |
| `ie` | Ireland |
| `il` | Israel |
| `in` | India |
| `is` | Iceland |
| `it` | Italy |
| `jp` | Japan |
| `kr` | Korea |
| `kw` | Kuwait |
| `lb` | Lebanon |
| `lu` | Luxembourg |
| `mt` | Malta |
| `mx` | Mexico |
| `my` | Malaysia |
| `ni` | Nicaragua |
| `nl` | Netherlands |
| `no` | Norway |
| `nz` | New Zealand |
| `om` | Oman |
| `pa` | Panama |
| `pe` | Peru |
| `pl` | Poland |
| `pt` | Portugal |
| `py` | Paraguay |
| `qa` | Qatar |
| `ro` | Romania |
| `ru` | Russia |
| `sa` | Saudi Arabia |
| `se` | Sweden |
| `sg` | Singapore |
| `si` | Slovenia |
| `sk` | Slovakia |
| `sv` | El Salvador |
| `th` | Thailand |
| `tr` | Turkey |
| `tw` | Taiwan |
| `ua` | Ukraine |
| `us` | United States |
| `uy` | Uruguay |
| `za` | South Africa |

## See Also

`sceNpGetAccountCountryA()`

# SceNpUnifiedEntitlementLabel

Unified entitlement label

## Definition

```
#include <np/np_common.h>
#define SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE (17)

typedef struct SceNpUnifiedEntitlementLabel {
	char data[ SCE_NP_UNIFIED_ENTITLEMENT_LABEL_SIZE ];
	char padding[3];
} SceNpUnifiedEntitlementLabel;
```

## Members

|  |  |
| --- | --- |
| `data` | Entitlement label |
| `padding` | Padding area (pad with 0's) |

## Description

This structure represents the unified entitlement label that is used to identify additional content. It is used to specify the target additional content when `sceAppContentAddcontMount()` is used to mount additional content.

For more information about entitlement labels, refer to the [PlayStation™Network Overview](../PSN-Overview/__document_toc.html) document.

# SceNpServiceEntitlementLabel

Service entitlement label

## Definition

```
#include <np/np_common.h>
#define SCE_NP_SERVICE_ENTITLEMENT_LABEL_SIZE (7)

typedef struct SceNpServiceEntitlementLabel {
	char data[ SCE_NP_SERVICE_ENTITLEMENT_LABEL_SIZE ];
	char padding[13];
} SceNpServiceEntitlementLabel;
```

## Members

|  |  |
| --- | --- |
| `data` | Service entitlement label |
| `padding` | Padding area (pad with 0's) |

## Description

This structure represents the service entitlement label.