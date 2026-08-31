# Web API Tracer User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Web_API_Tracer-Users_Guide/how-to-enable-disable-the-api-logging-of-web-api-calls-ps4-p.html

# Using the Web API Tracer Tool

This chapter provides information on how to use the Web API Tracer tool.

## Accessing the Tool

The Web API Tracer is accessed through a link provided in DevNet. The following conditions are required to launch the Web API Tracer from DevNet:

* A service targeted for the Web API Tracer is successfully provisioned to a NP Title ID with a NP Communication ID.
* The user is a "Viewer", "Owner", or "Editor" title collaborator for the NP Title ID.

DevNet displays a link to launch the Web API Tracer in the product detail page for the title. Refer to the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) for details on how to configure permissions and provision services. Contact your developer support representative to receive access to DevNet.

# Enabling and Disabling the API logging of Web API calls [PlayStation®4/PlayStation®5/S2S]

This topic describes the process of enabling or disabling the logging of Web API calls.

When using a PlayStation®4 or PlayStation®5, a debug setting is provided to enable or disable the API logging of Web API calls. Refer to the [Reference Materials](overview.html#web-api-tracer-users-guide_0__section_exq_jc2_22c) for the appropriate documents regarding debug settings.

When not using a PlayStation® system, the following HTTP header can enable API logging to be viewed in Web API Tracer for server to server use:

`X-Psn-WebTrace-Enabled: true`

If this header is not present, API logging is disabled.

Logs that are provided in the Web API Tracer are only taken in the sp-int (Development) environment. Logs expire and are deleted after one hour.

# Enabling and Disabling Web Trace Tags [PlayStation®4/PlayStation®5/S2S]

This topic describes the process of enabling and disabling web trace tags.

When using a PlayStation®4 or PlayStation®5, a debug setting is provided to attach an optional tag to Web API calls to assist in detailed debugging efforts. A developer can filter and fine tune the log results. Please refer to the following documents for the Web Trace Tags in detail:

* [NpWebApi2 Library Reference](../NpWebApi2-Reference/__document_toc.html)
* [NpCppWebApi Library Reference](../NpCppWebApi-Reference/__document_toc.html)

When not using a PlayStation® system, an optional tracing tag can be attached to Web API calls. Add the following HTTP header to apply the tag to a specific API call for server to server use:

`X-Psn-WebTrace-Tag: YOUR_TAG`

If the header is missing or the value is blank, Web Trace tags shows "None" in the tool. Note that you cannot use double quote characters (") in a tag. Tags have a limit of 64 characters.

Main Page

## Log Summary Section

A summary of logged information appears at the top of the tool including "Total Calls in Last Hour", "Calls/Per Second", "Errors in Last Hour" and "Unique Online IDs". Filters can be applied to show only data from a specific service, and general information about the PlayStation™Network status are shown at the top.

Filter

## File Exporting

Use the Download Logs dropdown menu to export logs as a file. The file can be exported in json or csv format. When exporting, you can apply filters to export specific data. The file is downloaded as a zip file. The filename is named with UTC time. For example, web-trace-logs-YYYY-MM-DD-hh-mm-ss.zip. Note that only the logs from the last one hour can be downloaded.

## API Group Tracker Section

The group tracker shows details about the number of calls made, call rate, and error rate seen during the debugging session. The section also shows a visual representation of usage to better understand how the game uses the PlayStation™Network Web API calls. These charts are based on the service filter selected at the top.

API Group Tracker

## Event Logs Section

Detailed logs showing individual Web API requests and responses are shown in the bottom area of the tool. Developers can create filters to better investigate detailed logs based on the following:

* Request Time (both UTC time and local time)
* API Group Name
* Source IP (client making API Calls)
* Online ID
* Source
* NP Title ID
* Web Trace Tags.

Individual API calls can be expanded to show more details.

Logs in Detail