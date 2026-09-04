# NpWebApi2 Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpWebApi2-Overview/how-to-specify-the-request-header-for-debugging-purposes.html

# Reference Information

# How to specify the request header for debugging purposes

The following request headers can be used for debugging purposes during development. To use them, specify them in the system software "★ Debug Settings" menu.

* `X-PSN-Fake-Rate-Limit-Enabled`
  + Refer to the "Rate Limit" section of the [PlayStation™Network Web APIs Overview](../PSN_WebAPI-Overview/__document_toc.html) document for details.
* `X-Psn-WebTrace-Enabled`
  + Refer to the [Web API Tracer User's Guide](../Web_API_Tracer-Users_Guide/__document_toc.html) document for details.

The library will ignore attempts to set these request headers using `sceNpWebApi2AddHttpRequestHeader()`.