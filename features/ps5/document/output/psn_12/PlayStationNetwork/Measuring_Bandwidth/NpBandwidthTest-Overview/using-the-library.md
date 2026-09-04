# NpBandwidthTest Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpBandwidthTest-Overview/using-the-library.html

# Using the Library

# Bandwidth Measurement

1. **Start measurement**

   Call `sceNpBandwidthTestInitStartUpload()` or `sceNpBandwidthTestInitStartDownload()`. An internal thread for bandwidth measurement will be generated. Specify the priority and CPU affinity mask of the internal thread in the arguments.
2. **Wait for measurement completion**

   Poll `sceNpBandwidthTestGetStatus()` and wait until `SCE_NP_BANDWIDTH_TEST_STATUS_FINISHED` is returned to indicate measurement completion.
3. **End measurement and obtain results**

   Call `sceNpBandwidthTestShutdown()`. As an argument, pass the pointer to the `SceNpBandwidthTestResult` structure for obtaining measurement results. If the returned value of the `result` member of the structure is 0, measured bandwidth will be stored in `uploadBps` and `downloadBps`.

## Abort Measurement

To abort processing during bandwidth measurement, call `sceNpBandwidthTestAbort()` and then `sceNpBandwidthTestShutdown()`.