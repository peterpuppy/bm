# NpBandwidthTest Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpBandwidthTest-Reference/constants.html

# Constants

# Return Codes

List of return codes returned by the NpBandwidthTest library

## Definition

| **Value** | **(Number)** | **Description** |
| --- | --- | --- |
| `SCE_NP_BANDWIDTH_TEST_ERROR_OUT_OF_MEMORY` | 0x80551f04 | Memory could not be allocated |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_ARGUMENT` | 0x80551f05 | Specified argument is invalid |
| `SCE_NP_BANDWIDTH_TEST_ERROR_INVALID_SIZE` | 0x80551f06 | Specified size is invalid |
| `SCE_NP_BANDWIDTH_TEST_ERROR_CONTEXT_NOT_AVAILABLE` | 0x80551f07 | Specified context cannot be used |
| `SCE_NP_BANDWIDTH_TEST_ERROR_ABORTED` | 0x80551f08 | Specified context was forced to terminate |
| `SCE_NP_BANDWIDTH_TEST_ERROR_TIMEOUT` | 0x80551f09 | Specified context timed out |

## Description

In addition to the above, error codes (negative value) of other libraries used internally by the kernel or the NpBandwidthTest library may be returned.