# NpSessionSignaling Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpSessionSignaling-Overview/exclusive-processing-in-the-callback-function.html

# Notes on Using the NpSessionSignaling Library

This topic provides explanations of mutexes in callback functions, limits on the number of connections, and the UDP port numbers used by the library; these matters require care when using the NpSessionSignaling library.

# Exclusive Processing in the Callback Function

When performing exclusive processing using a mutex in a callback function set by `sceNpSessionSignalingCreateContext2()`, do not allow other threads to call a function of the NpSessionSignaling library while the mutex is locked. Because mutexes are used within the NpSessionSignaling library, there is a risk of a deadlock occurring between the callback function thread and the thread that called the NpSessionSignaling library function. The same risk is posed by synchronous objects that use mutexes within the kernel; for example, the use of condition variables poses this risk.

# Limits on the Number of Connections

The maximum number of connections that the NpSessionSignaling library can handle at one time is 64. This is the total sum of connections in PENDING and ACTIVE states. The calling of `sceNpSessionSignalingActivateSession()` will never result in the establishment of connections in excess of this limit. Additionally, if `sceNpSessionSignalingActivateUser()` is used to attempt to establish a connection exceeding the limit, the error `SCE_NP_SESSION_SIGNALING_ERROR_TOO_MANY_CONN` will be returned.

# UDP Port Numbers Used by the NpSessionSignaling Library

The NpSessionSignaling library will first attempt to use port number 8571. If 8571 cannot be used, a port number in a range from 49152 to 65535 will be randomly used.