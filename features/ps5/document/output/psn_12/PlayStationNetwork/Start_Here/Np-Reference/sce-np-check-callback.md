# Np Library Reference – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Reference/sce-np-check-callback.html

# Checking Callbacks

# sceNpCheckCallback

Checks callbacks

## Definition

```
#include <np/np_common.h>
int sceNpCheckCallback(
	void
);
```

## Arguments

None

## Return Values

Returns `SCE_OK` (=0) for normal termination.

Returns an error code (a negative value) for an error. (Refer to "[Return Codes](return-codes.html)" for details.)

## Description

This function checks whether any of the callback functions, the event handlers, or the callbacks for receiving the result of asynchronous functions, registered using the Np library or other libraries related to PlayStation™Network, are in a state in which they should be called. If so - in other words, if an applicable event has been generated or if processing within an asynchronous function has completed and its result is ready to be returned to the application - the appropriate callback function (for example) will be called in the context of the thread that called this function.

Design the application so that this function is called regularly.

## Notes

This function is not multithread safe; operation is not guaranteed when called simultaneously from multiple threads.