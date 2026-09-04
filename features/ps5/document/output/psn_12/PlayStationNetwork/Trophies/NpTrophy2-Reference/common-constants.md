# NpTrophy2 Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Reference/common-constants.html

# Common Constants

# Data Sizes

Sizes of various data used in the NpTrophy2 library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_GAME_TITLE_MAX_SIZE` | 128 | The maximum size for the name of a trophy set (including the NULL terminator) |
| `SCE_NP_TROPHY2_GROUP_TITLE_MAX_SIZE` | 128 | The maximum size for the name of a trophy group (including the NULL terminator) |
| `SCE_NP_TROPHY2_NAME_MAX_SIZE` | 128 | The maximum size for the name of a trophy (including the NULL terminator) |
| `SCE_NP_TROPHY2_DESCR_MAX_SIZE` | 1024 | The maximum size for the description of a trophy (including the NULL terminator) |
| `SCE_NP_TROPHY2_REWARD_MAX_SIZE` | 128 | The maximum size for the reward related to a trophy (including the NULL terminator) |
| `SCE_NP_TROPHY2_NUM_MAX` | 1000 | The maximum number of trophies that can be defined |
| `SCE_NP_TROPHY2_GROUP_NUM_MAX` | 50 | The maximum number of groups that can be defined (including the base game group) |

## Description

These are size definitions of data used in the NpTrophy2 library.

# Return Codes

List of return codes returned by the NpTrophy2 library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_TROPHY2_ERROR_UNKNOWN` | 0x80553900 | Undefined error, not listed below |
| `SCE_NP_TROPHY2_ERROR_NOT_INITIALIZED` | 0x80553901 | Not initialized |
| `SCE_NP_TROPHY2_ERROR_ALREADY_INITIALIZED` | 0x80553902 | Already initialized |
| `SCE_NP_TROPHY2_ERROR_OUT_OF_MEMORY` | 0x80553903 | Not enough memory |
| `SCE_NP_TROPHY2_ERROR_INVALID_ARGUMENT` | 0x80553904 | Invalid argument |
| `SCE_NP_TROPHY2_ERROR_INSUFFICIENT_BUFFER` | 0x80553905 | Insufficient buffer to continue processing |
| `SCE_NP_TROPHY2_ERROR_EXCEEDS_MAX` | 0x80553906 | Exceeded the maximum value |
| `SCE_NP_TROPHY2_ERROR_ABORT` | 0x80553907 | Handle has been aborted  Processing has been aborted by `sceNpTrophy2AbortHandle()`. Delete the handle. |
| `SCE_NP_TROPHY2_ERROR_INVALID_HANDLE` | 0x80553908 | Invalid handle |
| `SCE_NP_TROPHY2_ERROR_INVALID_CONTEXT` | 0x80553909 | Invalid context |
| `SCE_NP_TROPHY2_ERROR_INVALID_TROPHY_ID` | 0x8055390a | Invalid trophy ID |
| `SCE_NP_TROPHY2_ERROR_INVALID_GROUP_ID` | 0x8055390b | Invalid group ID |
| `SCE_NP_TROPHY2_ERROR_NP_BIND_DAT_NOT_FOUND` | 0x8055390c | npbind.dat file cannot be found |
| `SCE_NP_TROPHY2_ERROR_ACCOUNTID_NOT_MATCH` | 0x8055390e | Account ID does not match |
| `SCE_NP_TROPHY2_ERROR_INSUFFICIENT_SPACE` | 0x8055390f | There is not enough free space in the console storage |
| `SCE_NP_TROPHY2_ERROR_CONTEXT_ALREADY_EXISTS` | 0x80553910 | Context already exists  There is a possibility that multiple contexts have been created for a single NP service label/user. |
| `SCE_NP_TROPHY2_ERROR_ICON_FILE_NOT_FOUND` | 0x80553911 | Icon file cannot be found |
| `SCE_NP_TROPHY2_ERROR_INVALID_TROPHY_CONF_FORMAT` | 0x80553914 | Invalid trophy configuration |
| `SCE_NP_TROPHY2_ERROR_UNSUPPORTED_TROPHY_CONF` | 0x80553915 | Unsupported trophy configuration |
| `SCE_NP_TROPHY2_ERROR_USER_NOT_FOUND` | 0x80553917 | User not found |
| `SCE_NP_TROPHY2_ERROR_USER_NOT_LOGGED_IN` | 0x80553918 | User is not logged in |
| `SCE_NP_TROPHY2_ERROR_CONTEXT_USER_LOGOUT` | 0x80553919 | Context is invalid due to user linked to context logging out |
| `SCE_NP_TROPHY2_ERROR_INVALID_NP_SERVICE_LABEL` | 0x8055391a | NP service label is invalid |
| `SCE_NP_TROPHY2_ERROR_CONTEXT_EXCEEDS_MAX` | 0x8055391b | Maximum number of contexts has been exceeded |
| `SCE_NP_TROPHY2_ERROR_HANDLE_EXCEEDS_MAX` | 0x8055391c | Maximum number of handles has been exceeded |
| `SCE_NP_TROPHY2_ERROR_INVALID_USER_ID` | 0x8055391d | User ID is invalid |
| `SCE_NP_TROPHY2_ERROR_TITLE_CONF_NOT_INSTALLED` | 0x8055391e | Trophy configuration data is not installed.  Confirm that the trophy configuration files are in the correct place. |
| `SCE_NP_TROPHY2_ERROR_INCONSISTENT_TITLE_CONF` | 0x8055391f | An attempt was made to install a trophy set that is inconsistent with already installed trophy configuration data |
| `SCE_NP_TROPHY2_ERROR_NOT_REGISTERED` | 0x80553920 | Context is not registered |
| `SCE_NP_TROPHY2_ERROR_ALREADY_REGISTERED` | 0x80553921 | Context is already registered |
| `SCE_NP_TROPHY2_ERROR_PARAM_FILE_NOT_FOUND` | 0x80553922 | param.json cannot be found |
| `SCE_NP_TROPHY2_ERROR_NOT_SUPPORTED_APP` | 0x80553923 | Called from an unsupported application |
| `SCE_NP_TROPHY2_ERROR_INVALID_NP_BIND` | 0x80553924 | npbind.dat file is invalid |
| `SCE_NP_TROPHY2_ERROR_NP_BIND_DAT_CORRUPTED` | 0x80553927 | The npbind.dat file is corrupted |
| `SCE_NP_TROPHY2_ERROR_NP_TITLE_DAT_CORRUPTED` | 0x80553928 | The nptitle.dat file is corrupted |
| `SCE_NP_TROPHY2_ERROR_BUSY` | 0x80553990 | The library is busy. |
| `SCE_NP_TROPHY2_ERROR_UCP_FILE_MODE_MISMATCH` | 0x805539cc | The Universal Data System Development Mode settings and the trophy configuration file format do not match.  Make sure that you have not renamed trophy00\_local.ucp to trophy00.ucp or vice versa. |