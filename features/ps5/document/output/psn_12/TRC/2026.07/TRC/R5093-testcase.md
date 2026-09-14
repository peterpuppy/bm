# Technical Requirements Checklist for PlayStation®5 – TRC 2026.07

Source: https://game.develop.playstation.net/resources/documents/TRC/2026.07/TRC/R5093-testcase.html

PlayStation®5 DevNet
10+
MY
Help Center
How satisfied are you with PlayStation Partners?
Ask Me Later
Home
Development
Support
Titles
Hardware
Admin
PS5

Development

DocumentsTechnical Requirements Checklist for PlayStation®5R5093 Test Case
Technical Requirements Checklist for PlayStation®5 – TRC 2026.07
Release Information
Getting Started
Audio/Video
Graphics
Input/Output Devices
Network
PlayStation™Network
Publishing
System
Target Management
Performance Optimization Guides
TRC and Guidelines
Guidelines
TRC
Technical Requirements Checklist for PlayStation®5
TRC Overview
Test Case Overview
Important Materials for Certification Process
Changes from Version 2026.02 to Version 2026.07
PlayStation®5 Feature
PlayStation®VR2
Design
Graphical User Interface
Termination of Application
R5093 Design - Termination of Application
R5093 Test Case
Enter Button
Peripheral Devices
Intellectual Property
Parental Control and Content Restriction
Commerce
Premium Feature
PlayStation™Network
Compatibility & Security
PlayStation®4 Cross-Generation SDK
R5030 Design - Display's Safe Area and Visibility

TEST | APP




Premise: -




Requirement:

Visibility

Visibility of essential items (see Description) and the visibility required for application usage and gameplay are maintained as follows:
Screen set to a resolution of 1080p or 2160p.
If 8K output is supported in Trinity mode, screen set to a resolution of 4320p.
If the application supports VR mode, video output to a VR headset.

Screen Adjustment

If the application disables the "Scaling to the Display's Safe Area", the screen is designed so that essential items are included within one of the following:
Approximately the center 90% of the vertical/horizontal measurements (90% x 90% of the area)
The display area that can be obtained with sceSystemServiceGetDisplaySafeAreaInfo().
Description

For applications running in VR mode and the social screen (TV side) setting is a separate mode, check that visibility on the TV side is also maintained.

Essential items

"Essential items" are as follows:

Error messages and warning messages defined by the TRC
Legal texts such as the EULA and other copyright notices
Online IDs used as the identifiers of users

In order to display long strings of characters the application can implement a scrolling feature; it is also acceptable to include features such as "See Details" to have the strings displayed in a separate screen.

In addition, when supporting VR mode within the application, refer to R5176 regarding the display of important information within VR mode.

Display Area

For details on setting the "Scaling to the Display's Safe Area", refer to Param.json File Specification.

If the application provides its own screen adjustment feature, ensure the options provided do not overlap with the "Display Area Adjustment" feature and instead provide new options such as:

Adjust UI parts or HUD elements
Change the aspect ratio of the screen
Related Requirements and Related Documents
R5176
R5197
Param.json File Specification
SystemService Library Overview
Was this chapter helpful?  Yes  No
R5030 Test Case
General Notes
If the "Scaling to the Display's Safe Area" is enabled, it is not necessary to perform R5030C and R5030D
R5030A
Expected results
The application can be started in all resolutions to be checked.
The visibility required to use the application and play the game is maintained throughout.
Procedures
Press the up button on the home screen.
Confirm that "Settings" > "Screen and Video" > "Video Output" > "Resolution" is set to one of the resolutions to check.
Go back to the home screen and select the Application.
Check throughout the entire application.
Notes
Check the resolution at both "1080p" and "2160p" in step (2). If the application supports 8K resolution on Trinity mode, please also check "4320p" with Trinity Testing Kit.
R5030B
Expected results

If the application supports the VR mode, visibility required to use the application and play the game is maintained on the VR headset screen.

Procedures
Confirm that the PlayStation®VR2 is connected to the PlayStation®5 console, and turn on the power of the PlayStation®VR2.
Select the Application on the home screen.
Proceed to a point that uses VR mode.
Check throughout all of VR mode.
Notes
When displaying different images on the VR headset screen and the television monitor, check that visibility is also maintained on the television monitor.
R5030C
Expected results

When keeping essential items within 90% of the horizontal and vertical dimensions of the screen.

The screen is designed so that essential items are displayed in the center 90% of the vertical/horizontal measurements (90% x 90% of the area).
When displaying long character strings, the display is scrolled or a feature, for example, "See details" displays the content on a separate screen.
Procedures
Select the Application on the home screen
Proceed to where an essential item is displayed
Notes
Check in all languages supported by the application.
R5030D
Expected results

When displaying essential items according to the display area settings set in the system software

Essential items are displayed within the display area set by "Adjust Display Area".
When displaying long character strings, the display is scrolled or a "See details" feature displays the content on a separate screen.
Procedures
Press the up button on the home screen.
Confirm that "Settings" > "Screen and Video" > "Video Output" > "Resolution" is set to one of the resolutions to check.
Go back to "Screen and Video" > "Screen" and set "Adjust Display Area" to an arbitrary value.
Go back to the home screen, then select the Application.
Proceed to where an essential item is displayed.
Close the Application.
Press the up button on the home screen.
Set "Settings" > "Screen and Video" > "Screen" > "Adjust Display Area" to a setting that differs from step (3).
Go back to the home screen, then select the Application.
Proceed to where the essential item confirmed in step (5) is displayed.
Notes
Check in all languages supported by the application.
Check the resolution at both "1080p" and "2160p". If the application supports 8K resolution on Trinity mode, please also check "4320p" with Trinity Testing Kit.
Was this chapter helpful?  Yes  No
R5149 Design - Error Codes

TEST | APP




Premise: -




Requirement: The application is implemented as follows:

The hexadecimal error codes (0x80000000 to 0x8FFFFFFF) returned by SDK library APIs are not displayed by the application.
The short error codes (examples: AB-12345-6, AB-123456-7, E-80000000, E2-80000000) displayed when an application is running are only the short error codes displayed using the display mode provided by the error dialog or the save data dialog. Short error codes are not displayed using the user specified message display mode of the message dialog or using an application proprietary message system.
An application proprietary error code format is not XY-YYYYY-Y or XY-YYYYYY-Y (where X is a letter, and Y is a letter or number).
Description

The hexadecimal error codes (0x80000000 to 0x8FFFFFFF) returned by SDK library APIs are in a format that is easy to process by programs, but the format is a long string of numbers that can be easily misread by users when viewed and conveyed verbally. In order to prevent such mistakes, the short error codes (examples: AB-12345-6, AB-123456-7, E-80000000, E2-80000000), are defined. This requirement is for standardizing the system error codes displayed for users into these short error codes.

Was this chapter helpful?  Yes  No
R5149 Test Case
General Notes
Examples of shortened error codes are AB-12345-6, AB-123456-7, E-80000000, E2-80000000
Generate various errors in the application, such as communication errors when using the network features and disconnecting devices at points where they are required, and check the messages displayed by the application.
R5149B
Expected results
When displaying a shortened error code, the following system message is displayed.
[T-008][Info]
ErrorDialog: 
ErrorCode - 
0x[hexadecimal error code set by application]
Procedures
Select the Application
Proceed to where a shortened error code is displayed
R5149C
Expected results

When the application uses a proprietary error code message system, it does not display the following.

Hexadecimal error codes (0x80000000 to 0x8FFFFFFF)
Error codes using the same format as shortened error codes
Error codes using the format XY-YYYYY-Y or XY-YYYYYY-Y (X is alphabetic characters and Y is alphanumeric characters)
Procedures
Select the Application on the home screen
Proceed to where the application displays a unique error code
Was this chapter helpful?  Yes  No
R5093 Design - Termination of Application

TEST | APP




Premise: -




Requirement: The application does not perform processing to terminate itself.

Description

This requirement is in place in order to make the system software the standard way of terminating the application. For example implementations that use a button to terminate the application are prohibited.

Exception cases

sceSystemServiceReportAbnormalTermination() can be called for the purpose of reporting a problem to the SIE-managed Recap server only if processing that should succeed fails, and advancement is no longer possible as the application cannot be restored. Examples of this are:

When a required file is missing
When calling a function for a library essential to advancement returns an internal error

Under these circumstances, it is permitted to display a message asking the user to terminate the application (without explaining how to do so).

For the handling of recoverable errors such as a network disconnection, calling sceSystemServiceReportAbnormalTermination() is not permitted and appropriate error handling must be carried out instead.

Handling during CertOps submission

Calling sceSystemServiceReportAbnormalTermination() force terminates the application generating a core dump. The forced termination will be handled in CertOps as equivalent to the application crashing, therefore such occurrences should be avoided within the usual scope of application gameplay.

Related Requirements and Related Documents
Programming Startup Guide - Basic Information on Programming Environments - Self-Termination of an Application
SystemService Library Overview
Was this chapter helpful?  Yes  No
R5093 Test Case
R5093A
Expected results

Except for calling sceSystemServiceReportAbnormalTermination(), the application does not execute a core dump when it has performed processing to voluntarily terminate a program.

Procedures
Select the Application
Proceed to where users are prompted to exit the application
The user performs the prompt action
Notes

"Users are prompted to exit the application" in step (2) refers to content such as "Press the circle button to exit the application". If a core dump is executed when the circle button is pressed at this time, the application will have performed voluntary termination processing and will be in violation of this requirement.

Was this chapter helpful?  Yes  No
R5207 Design - Enter Button

TEST | APP




Premise: If the application package was built using SDK 9.00 or later




Requirement: The cross button is assigned to the Enter button in the application.

Description

This requirement aims to maintain consistent usage of the Enter button between the system software and application. The Enter button of the system software, on-screen keyboards (OSK) that can be used in application, and Common Dialogs (especially NpCommerceDialog andSaveDataDialog) are all assigned to the cross button regardless of the license territory. Due to this, the Enter button must also be assigned to the cross button within the application regardless of the license territory. If not, users may accidentally select options from the OSK and Common Dialogs.

When assigning buttons for transitioning scenes forward/backward, we recommend that you assign the cross button for forward operations and the circle button for backward operations.

Cases exempted from this requirement

This requirement does not apply while the user is operating the application using the PlayStation VR2 Sense™ controller while in VR mode. During that time, it is acceptable to assign the Enter button to the button (for example, the L2/R2 buttons) used for selecting/confirming pointer operation.

When updating an application package created with an SDK less than 9.00, compliance with this requirement is not mandatory, but it is strongly recommended.

Related Requirements and Related Documents
Programming Startup Guide - Application Specification Guidelines - Assignment of the Enter Button
Was this chapter helpful?  Yes  No
R5207 Test Case
R5207A
Expected results

The cross button is assigned as the Enter Button in the application.

Procedures
Select the application on the home screen.
Check throughout the entire application.
Was this chapter helpful?  Yes  No
R5071 Safety Use of Wireless Controller

TEST | APP




Premise: -




Requirement: The application does not instruct or ask the user to vigorously shake the controller with one hand.

Was this chapter helpful?  Yes  No
R5071 Test Case
R5071A
Expected results

Users are not requested or instructed to vigorously shake the DualSense™ wireless controller with one hand.

Procedures
Select the Application on the home screen
Check throughout the entire application
Notes

Pay particular attention when motion sensor features are being used.

Was this chapter helpful?  Yes  No
<
Previous
PlayStation®VR2
Next
Intellectual Property
>
English
日本語 (Japanese)
한국말 (Korean)
© 2026 Sony Interactive EntertainmentAbout UsTerms of UsePrivacy