# SystemService Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SystemService-Reference/ps5-sce-system-service-param-id.html

# Obtaining System Parameters

# SceSystemServiceParamId

System parameter ID

## Definition

```
#include <system_service.h>
typedef int32_t SceSystemServiceParamId;
```

## Description

These are the system parameter IDs to specify for the 1st argument `paramId` of the function `sceSystemServiceParamGetInt()` and `sceSystemServiceParamGetString()`, for obtaining a system parameter.

The integer-type system parameter IDs used in `sceSystemServiceParamGetInt()` and values that can be obtained are as follows.

| **Value** | **(Number)** | **Obtainable Value** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_PARAM_ID_LANG` | 1 | Language settings (value of `SceSystemParamLang`) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_DATE_FORMAT` | 2 | Date display format (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_TIME_FORMAT` | 3 | Time display format (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_TIME_ZONE` | 4 | Time zone offset (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_SUMMERTIME` | 5 | Daylight savings time (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_ENABLE` | 100 | Display closed captions (0: Disable, 1: Enable) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CONTENT_SPECIFIED` | 101 | Display closed captions as specified by the content (0: Disable, 1: Enable) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_FONT_TYPE` | 102 | Characters - Font type (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_SIZE` | 103 | Characters - Size (%) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_COLOR` | 104 | Characters - Color (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_EDGE` | 105 | Characters - Outline (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_EDGE_COLOR` | 106 | Characters - Outline color (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_OPACITY` | 107 | Characters - Opacity (%) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_BG_COLOR` | 108 | Captions - Background color (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CHAR_BG_OPACITY` | 109 | Captions - Background opacity (%) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_WINDOW_COLOR` | 110 | Captions - Window color (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CC_WINDOW_OPACITY` | 111 | Captions - Window opacity (%) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_TEXT_SIZE` | 201 | Text size (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_BOLD_TEXT` | 202 | Bold text (0: Disable, 1: Enable) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_HIGH_CONTRAST_TEXT` | 203 | High contrast text (0: Disable, 1: Enable) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_AUTO_SCROLL_SPEED` | 204 | Auto-scroll speed (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_INVERT_COLORS` | 205 | Invert colors (0: Disable, 1: Enable) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_COLOR_FILTER` | 206 | Color filter (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_COLOR_FILTER_INTENSITY` | 207 | Color filter intensity (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_SCREEN_READER` | 208 | Screen reader (0: Disable, 1: Enable) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_SCREEN_READER_SPEED` | 209 | Screen reader speech speed (integer value: -10 to 10) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_SCREEN_READER_VOLUME` | 210 | Screen reader voice value (integer value: 1 to 100) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_SCREEN_READER_VOICE_TYPE` | 211 | Screen reader voice type (details below) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_REDUCE_MOTION` | 212 | Reduce motion (0: Disabled, 1: Enabled) |
| `SCE_SYSTEM_SERVICE_PARAM_ID_CLEARLY_SHOW_SWITCH` | 213 | Display setting of the on/off switch for the system settings menu (0: normal, 1: display more clearly) |

The string-type system parameter ID used in `sceSystemServiceParamGetString()` and the value that can be obtained are as follows

| **Value** | **(Number)** | **Obtainable Value** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_PARAM_ID_SYSTEM_NAME` | 6 | System name |

The following constant is defined regarding the length of the system name.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_MAX_SYSTEM_NAME_LENGTH` | 65 | Maximum system name length |

The date display formats are indicated by the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_DATE_FORMAT_YYYYMMDD` | 0 | Year/Month/Day |
| `SCE_SYSTEM_PARAM_DATE_FORMAT_DDMMYYYY` | 1 | Day/Month/Year |
| `SCE_SYSTEM_PARAM_DATE_FORMAT_MMDDYYYY` | 2 | Month/Day/Year |

The time display formats are indicated by the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_TIME_FORMAT_12HOUR` | 0 | 12 hour |
| `SCE_SYSTEM_PARAM_TIME_FORMAT_24HOUR` | 1 | 24 hour |

The time zone offset is represented as the difference in minutes between local time and Greenwich Mean Time. Examples are as follows:

* GMT+09:00 → +540
* GMT-04:00 → -240

Daylight savings time is indicated by an integer value of 1 or 0. The value will be 1 if the set time zone is currently in daylight savings time and will be 0 if it is not in daylight savings time.

For closed captions, when the value obtained with `SCE_SYSTEM_SERVICE_PARAM_ID_CC_ENABLE` is 0, further parameters will have no meaning. Similarly, when the value obtained with `SCE_SYSTEM_SERVICE_PARAM_ID_CC_CONTENT_SPECIFIED` is 1, further parameters will have no meaning.

The character font types are indicated by the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_MONOSPACED_WITH_SERIFS` | 0 | Type 3 (monospaced font with serifs) |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_PROPORTIONALLY_SPACED_WITH_SERIFS` | 1 | Type 4 (proportional font with serifs) |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_MONOSPACED_WITHOUT_SERIFS` | 2 | Type 1 (monospaced font without serifs) |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_PROPORTIONALLY_SPACED_WITHOUT_SERIFS` | 3 | Type 2 (proportional font without serifs) |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_CASUAL` | 4 | Type 5 (casual) |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_CURSIVE` | 5 | Type 6 (cursive) |
| `SCE_SYSTEM_PARAM_CC_FONT_TYPE_SMALL_CAPITALS` | 6 | Type 7 (small capitals) |

The colors for characters/character outlines/caption backgrounds/caption windows are indicated by the following hexadecimal values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_CC_COLOR_BLACK` | 0x00000000 | Black |
| `SCE_SYSTEM_PARAM_CC_COLOR_BLUE` | 0x00000002 | Blue |
| `SCE_SYSTEM_PARAM_CC_COLOR_GREEN` | 0x00000200 | Green |
| `SCE_SYSTEM_PARAM_CC_COLOR_CYAN` | 0x00000202 | Cyan |
| `SCE_SYSTEM_PARAM_CC_COLOR_RED` | 0x00020000 | Red |
| `SCE_SYSTEM_PARAM_CC_COLOR_MAGENTA` | 0x00020002 | Magenta |
| `SCE_SYSTEM_PARAM_CC_COLOR_YELLOW` | 0x00020200 | Yellow |
| `SCE_SYSTEM_PARAM_CC_COLOR_WHITE` | 0x00020202 | White |

The character outlines are indicated by the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_CC_EDGE_TYPE_NO_EDGE_ATTRIBUTE` | 0 | No outline |
| `SCE_SYSTEM_PARAM_CC_EDGE_TYPE_RAISED_EDGES` | 1 | Raised |
| `SCE_SYSTEM_PARAM_CC_EDGE_TYPE_DEPRESSED_EDGES` | 2 | Depressed |
| `SCE_SYSTEM_PARAM_CC_EDGE_TYPE_UNIFORM_EDGES` | 3 | Uniform |
| `SCE_SYSTEM_PARAM_CC_EDGE_TYPE_DROP_SHADOWED_EDGES` | 4 | Shadowed |

Text size is indicated by one of the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_TEXT_SIZE_SMALL` | -1 | Small |
| `SCE_SYSTEM_PARAM_TEXT_SIZE_NORMAL` | 0 | Normal |
| `SCE_SYSTEM_PARAM_TEXT_SIZE_LARGE` | 1 | Large |
| `SCE_SYSTEM_PARAM_TEXT_SIZE_VERY_LARGE` | 2 | Very large |

Auto-scroll speed is indicated by one of the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_AUTO_SCROLL_SPEED_VERY_SLOW` | -2 | Very slow |
| `SCE_SYSTEM_PARAM_AUTO_SCROLL_SPEED_SLOW` | -1 | Slow |
| `SCE_SYSTEM_PARAM_AUTO_SCROLL_SPEED_NORMAL` | 0 | Normal |
| `SCE_SYSTEM_PARAM_AUTO_SCROLL_SPEED_FAST` | 1 | Fast |

The color filter is indicated by one of the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_COLOR_FILTER_DISABLED` | 0 | Disabled |
| `SCE_SYSTEM_PARAM_COLOR_FILTER_GRAYSCALE` | 1 | Grayscale |
| `SCE_SYSTEM_PARAM_COLOR_FILTER_PROTANOPIA` | 2 | Red/Green (Protanopia) |
| `SCE_SYSTEM_PARAM_COLOR_FILTER_DEUTERANOPIA` | 3 | Green/Red (Deuteranopia) |
| `SCE_SYSTEM_PARAM_COLOR_FILTER_TRITANOPIA` | 4 | Blue/Yellow (Tritanopia) |

The intensity of the color filter is represented by an integer value of 0 to 100, but this value is meaningful only when the color filter value is `SCE_SYSTEM_PARAM_COLOR_FILTER_PROTANOPIA`, `SCE_SYSTEM_PARAM_COLOR_FILTER_DEUTERANOPIA`, or `SCE_SYSTEM_PARAM_COLOR_FILTER_TRITANOPIA`.

The screen reader voice type is represented by one of the following integer values.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_VOICE_TYPE_FEMALE` | 0 | Female |
| `SCE_SYSTEM_PARAM_VOICE_TYPE_MALE` | 1 | Male |

# SceSystemParamLang

Language code type

## Definition

```
#include <system_param.h>
typedef int32_t SceSystemParamLang;
```

## Description

These types indicate the language setting value that can be obtained by specifying `SCE_SYSTEM_SERVICE_PARAM_ID_LANG` for the 1st argument of `sceSystemServiceParamGetInt()`.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_PARAM_LANG_JAPANESE` | 0 | Japanese |
| `SCE_SYSTEM_PARAM_LANG_ENGLISH_US` | 1 | English (United States) |
| `SCE_SYSTEM_PARAM_LANG_FRENCH` | 2 | French (France) |
| `SCE_SYSTEM_PARAM_LANG_SPANISH` | 3 | Spanish (Spain) |
| `SCE_SYSTEM_PARAM_LANG_GERMAN` | 4 | German |
| `SCE_SYSTEM_PARAM_LANG_ITALIAN` | 5 | Italian |
| `SCE_SYSTEM_PARAM_LANG_DUTCH` | 6 | Dutch |
| `SCE_SYSTEM_PARAM_LANG_PORTUGUESE_PT` | 7 | Portuguese (Portugal) |
| `SCE_SYSTEM_PARAM_LANG_RUSSIAN` | 8 | Russian |
| `SCE_SYSTEM_PARAM_LANG_KOREAN` | 9 | Korean |
| `SCE_SYSTEM_PARAM_LANG_CHINESE_T` | 10 | Chinese (traditional) |
| `SCE_SYSTEM_PARAM_LANG_CHINESE_S` | 11 | Chinese (simplified) |
| `SCE_SYSTEM_PARAM_LANG_FINNISH` | 12 | Finnish |
| `SCE_SYSTEM_PARAM_LANG_SWEDISH` | 13 | Swedish |
| `SCE_SYSTEM_PARAM_LANG_DANISH` | 14 | Danish |
| `SCE_SYSTEM_PARAM_LANG_NORWEGIAN` | 15 | Norwegian |
| `SCE_SYSTEM_PARAM_LANG_POLISH` | 16 | Polish |
| `SCE_SYSTEM_PARAM_LANG_PORTUGUESE_BR` | 17 | Portuguese (Brazil) |
| `SCE_SYSTEM_PARAM_LANG_ENGLISH_GB` | 18 | English (United Kingdom) |
| `SCE_SYSTEM_PARAM_LANG_TURKISH` | 19 | Turkish |
| `SCE_SYSTEM_PARAM_LANG_SPANISH_LA` | 20 | Spanish (Latin America) |
| `SCE_SYSTEM_PARAM_LANG_ARABIC` | 21 | Arabic |
| `SCE_SYSTEM_PARAM_LANG_FRENCH_CA` | 22 | French (Canada) |
| `SCE_SYSTEM_PARAM_LANG_CZECH` | 23 | Czech |
| `SCE_SYSTEM_PARAM_LANG_HUNGARIAN` | 24 | Hungarian |
| `SCE_SYSTEM_PARAM_LANG_GREEK` | 25 | Greek |
| `SCE_SYSTEM_PARAM_LANG_ROMANIAN` | 26 | Romanian |
| `SCE_SYSTEM_PARAM_LANG_THAI` | 27 | Thai |
| `SCE_SYSTEM_PARAM_LANG_VIETNAMESE` | 28 | Vietnamese |
| `SCE_SYSTEM_PARAM_LANG_INDONESIAN` | 29 | Indonesian |
| `SCE_SYSTEM_PARAM_LANG_UKRAINIAN` | 30 | Ukrainian |

# sceSystemServiceParamGetInt

Get system parameter (integer value)

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceParamGetInt(
	SceSystemServiceParamId paramId,
	int32_t *value
);
```

## Arguments

|  |  |
| --- | --- |
| `paramId` | System parameter ID |
| `value` | Destination to store the obtained value |

## Return Values

Stores the obtained value in `*value` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | The `paramId` value is invalid, or `value` is NULL |
| Other errors | Negative value | Fatal error |

## Description

This function obtains the current system parameter value (integer value) set for the system software.

For `paramId`, specify the `SceSystemServiceParamId` value.

The meaning of the value stored in `*value` changes depending on the value specified for `paramId`. Refer to the Description for `SceSystemServiceParamId`.

## Examples

```
/* Obtain the language settings set to the system software */
int32_t language;

ret = sceSystemServiceParamGetInt( SCE_SYSTEM_SERVICE_PARAM_ID_LANG, &language );
```

## Notes

* This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, the library may not operate as expected afterward. Make sure to program the application so that this function is not called at the same time by multiple threads.
* Do not poll this function. Obtaining a value when the application starts and after resuming from a suspension is sufficient for following changed settings.

# sceSystemServiceParamGetString

Get system parameter (string)

## Definition

```
#include <system_service.h>
int32_t sceSystemServiceParamGetString(
	SceSystemServiceParamId paramId,
	char *buf,
	size_t bufSize
);
```

## Arguments

|  |  |
| --- | --- |
| `paramId` | System parameter ID |
| `buf` | Destination to store the obtained string |
| `bufSize` | Size of the buffer pointed to by `buf` |

## Return Values

Stores the obtained string in `*buf` and returns `SCE_OK` (=0) for normal termination.

Returns one of the following error codes (a negative value) for an error.

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_SYSTEM_SERVICE_ERROR_PARAMETER` | 0x80A10003 | The `paramId` value is invalid, or `buf` is NULL, or the buffer size specified in `bufSize` is insufficient |
| Other errors | Negative value | Fatal error |

## Description

This function obtains the current system parameter value (string) set for the system software.

For `paramId`, specify the `SceSystemServiceParamId` value.

The meaning of the value stored in `*buf` changes depending on the value specified for `paramId`. Refer to the Description for `SceSystemServiceParamId`.

## Examples

```
/* Retrieve system name set to the system software */
char buf[SCE_SYSTEM_SERVICE_MAX_SYSTEM_NAME_LENGTH];

ret = sceSystemServiceParamGetString(SCE_SYSTEM_SERVICE_PARAM_ID_SYSTEM_NAME, buf, SCE_SYSTEM_SERVICE_MAX_SYSTEM_NAME_LENGTH);
```

## Notes

* This function is not multithread safe. Although this function may reach normal termination when it is called by multiple threads at the same time, the library may not operate as expected afterward. Make sure to program the application so that this function is not called at the same time by multiple threads.
* Do not poll this function. Obtaining a value when the application starts and after resuming from a suspension is sufficient for following changed settings.