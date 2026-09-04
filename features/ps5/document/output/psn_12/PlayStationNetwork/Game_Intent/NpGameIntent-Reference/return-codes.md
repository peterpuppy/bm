# NpGameIntent Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpGameIntent-Reference/return-codes.html

# Common Constants

# SCE\_NP\_GAME\_INTENT\_\*\_MAX\_SIZE

Maximum sizes of data used by the NpGameIntent library

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_GAME_INTENT_TYPE_MAX_SIZE` | 33 | Maximum size of the game intent event type string (includes the NULL terminator) |
| `SCE_NP_GAME_INTENT_DATA_MAX_SIZE` | 16385 | Maximum size of game intent data |

## Description

The above constants represent maximum sizes of data used by the NpGameIntent library.

# Return Codes

Return codes returned by the NpGameIntent library

## Definition

| **Value** | **Number** | **Description** |
| --- | --- | --- |
| `SCE_NP_GAME_INTENT_ERROR_UNKNOWN` | 0x80553800 | Undefined error that is not listed below |
| `SCE_NP_GAME_INTENT_ERROR_ALREADY_INITIALIZED` | 0x80553801 | Library is already initialized |
| `SCE_NP_GAME_INTENT_ERROR_NOT_INITIALIZED` | 0x80553802 | Library is not initialized |
| `SCE_NP_GAME_INTENT_ERROR_OUT_OF_MEMORY` | 0x80553803 | Insufficient memory |
| `SCE_NP_GAME_INTENT_ERROR_INVALID_ARGUMENT` | 0x80553804 | Specified parameter is invalid |
| `SCE_NP_GAME_INTENT_ERROR_INSUFFICIENT_BUFFER` | 0x80553805 | Insufficient buffer |
| `SCE_NP_GAME_INTENT_ERROR_INTENT_NOT_FOUND` | 0x80553806 | Game intent information does not exist |
| `SCE_NP_GAME_INTENT_ERROR_VALUE_NOT_FOUND` | 0x80553807 | Property value doesn't exist |