# Technical Requirements Checklist for PlayStation®5 – TRC 2026.07

Source: https://game.develop.playstation.net/resources/documents/TRC/2026.07/TRC/Requirement-Scope.html

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

DocumentsTechnical Requirements Checklist for PlayStation®5Requirement Scope
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
What’s TRC
Provided TRC Formats
Requirement Scope
Testing the combination of the application and additional content
Notes for Disc Release
User Handling
When displaying the name of the SIE controller during gameplay operation
Betas
About Each Version
Soundtrack and Digital Art Book
Publishing the Single Content/Entitlement in Multiple Countries/Regions
Notes on using the In-Game Commerce feature from an application server
Call rate limits
Test Case Overview
Important Materials for Certification Process
Changes from Version 2026.02 to Version 2026.07
PlayStation®5 Feature
PlayStation®VR2
Design
Intellectual Property
Parental Control and Content Restriction
Commerce
Premium Feature
PlayStation™Network
Compatibility & Security
PlayStation®4 Cross-Generation SDK
What’s TRC

The Technical Requirements Checklist for PlayStation®5 (hereinafter, referred to as TRC) is a collection of requirements that packages of titles for PlayStation®5 must adhere to prior to submission to Platform Certification & Operations (CertOps). All the requirements must be satisfied in order to release your application in the PlayStation®5 console format. Check the TRC throughout the planning stage, when creating the master, and upon master submission; make sure there are no violations.

In addition, CertOps may also report "Functionality" bugs. These are issues that are unrelated to the TRCs, and usually have a significant detrimental impact on the user experience. For more details, refer to the " CertOps User Guide - Bugs - Functionality Bug Reporting ".

TRC Version: 2026.07

Date of Issue

March 17, 2026

Date of Enforcement

July 1, 2026

Requirement Numbering Rule

New requirements have R53NN (N is numeric) as requirement numbers. Ported requirements from the TRC for PlayStation®4 have R50NN - R52NN (N is numeric) as requirement numbers. For ease of cross reference with the TRC for PlayStation®4, the lower three digits of requirement numbers are common with TRC for PlayStation®4. For example, the requirement about the initial chunk set (initial payload) for PlayGo is R4002 in the TRC for PlayStation®4 and TRC for PlayStation®5 is R5002.

Was this chapter helpful?  Yes  No
Provided TRC Formats
PDF and xml for TRC

Provided below:

https://game.develop.playstation.net/projects/publishing/#p36

TRC Versions Earlier Than the Latest Version

You can check the TRC version earlier than the latest version by checking the "Product" section in the online document on DevNet.

As a general rule, please comply with the latest version of the TRC. If it is difficult to comply with the latest version of the requirements, please contact Private Support via the PlayStation®5 Developer Network website ( https://game.develop.playstation.net ) for each requirement. If the Acceptable Versions for Submission > Exceptions apply to your application and you wish to use an expired version of the TRC, also contact Private Support via the PlayStation®5 Developer Network website ( https://game.develop.playstation.net ). Once the application is released using the current version of the TRC at the time of its submission to CertOps, SIE does not need to be contacted when updating that application.

Was this chapter helpful?  Yes  No
Requirement Scope

"APP" and/or "ADD-ON" will be mentioned in each requirement, and they indicate whether the requirement is applicable to each type of content.

APP: application package
ADD-ON: additional content, consumable items, virtual currency, and so on.

Only the requirements which have "TEST" are tested in CertOps. Even for requirements which do not have "TEST", make sure to confirm them during development.

Was this chapter helpful?  Yes  No
Testing the combination of the application and additional content

Before submitting the package, ensure that it works correctly in combination with the related application and additional content. It is not necessary to test it with applications or additional content other than the latest versions.

Example 1: When submitting new additional content
Test using a combination of the latest version of the application and the additional content being submitted.
Example 2: When submitting a patch for the application
Test using a combination of the submitted application, the submitted patch, and the valid additional content.
Example 3: When submitting a patch for existing additional content
Test using a combination of the latest version of the application and the patch for the additional content being submitted.
Was this chapter helpful?  Yes  No
Notes for Disc Release

For Blu-ray Disc games on the PlayStation®5 console, ISO files are not uploaded to GEMS. Additionally, as Blu-ray Disc games are only read after installation, there is no need to burn Blu-ray Discs for testing during development. For further details please refer to Content Packaging and Updating Guide - Overview of Discs.

Was this chapter helpful?  Yes  No
User Handling

A "user" referred to in each requirement is limited to "a user who is permitted to participate in the application". If either or both of the following conditions are met, it will be deemed that participation of that user has been permitted by the application.

Texts and/or images referring to that user are displayed
Device inputs from that user such as controller inputs are accepted

For example, if an application specifies that the user who starts the application is the only one who is permitted to participate, then there is no need to implement measures to satisfy each requirement for other users who are not permitted to participate.

Although this interpretation of a "user" is applicable to all requirements, make special note of it for R5061, R5063 and R5064.

Was this chapter helpful?  Yes  No
When displaying the name of the SIE controller during gameplay operation

When specifying SCE_PAD_PORT_TYPE_STANDARD for the port type of the controller, use the term "DualSense™ wireless controller". There is no way to determine the controller of this port type (e.g. the Access™ controller, the DualSense Edge™ wireless controller, etc). For details, refer to Pad Library Overview - Basic Usage of the Pad Library.

In addition, if an application displays the product image of a controller to explain gameplay operation in accordance with R5038, display the product image of the DualSense™ wireless controller.

Was this chapter helpful?  Yes  No
Betas

For Betas, applicable TRC requirements will be determined during the beta application process. Please refer to the Betas (found at Help Center > Documentation). Also, set the following:

Content Pipeline: Register "Product Types" as "Full Game" and "Storefront Classification" as "Beta"
Param.json: Add "+256" to "attribute3"

Contact Private Support via the PlayStation®5 Developer Network website ( https://game.develop.playstation.net/ ) in advance with any questions about the above.

Was this chapter helpful?  Yes  No
About Each Version

This is an explanation of each of the following versions related to master submission.

Master version (masterVersion)
Application version (contentVersion)
Master Version (masterVersion)

Represents the version of an application or additional content to be submitted. The Master Version in the param.json(s) of the package submitted to CertOps must match the MDT form Version (01.00, 01.01, and so on). For details, refer to CertOps guidelines - MDT Submissions and Param.json File Specification - Param File (param.json) Specifications - Parameter Definitions for Applications.

Application version (contentVersion)

Represents the version of an application or additional content to be updated. For details, refer to Param.json File Specification - Param File (param.json) Specifications - Parameter Definitions for Applications and Content Packaging and Updating Guide - Overview of Updates.

Was this chapter helpful?  Yes  No
Soundtrack and Digital Art Book

If the application does not contain game elements (for example, soundtrack or digital art book), set as follows:

Register the "Concept Type" as a "Game" in Content Pipeline
If there is a related game concept, create a "Product Group" under it
Register the "Product Types" as an "Application" in Content Pipeline
Set the value of the "contentBadgeType" to "2" and the "applicationDrmType" to "standard" in the param.json for each product in the package. For details, refer to the Param.json File Specification document

Please follow the table below in regards to handling of requirements for these types of applications:

Category

	

Requirement

	

Expected handling




PlayGo

	
R5002
R5158
	

Not required

All files in the package can be included in chunk #0.



Trophy

	
R5013
	

This feature must not be used




Share & Remote Play

	
R5076
	

If it is difficult to comply for copyright or other reasons, please create a waiver request thread




Parental Control and Content Restriction

	
R5005
	

Set the same "Age Level for Boot Restriction" as the related game




Premium Feature

	
R5063
R5064
	

This feature must not be used




Design

	
R5045
	

If user accounts are managed on an application server, contact Private Support through the PlayStation®5 Developer Network website ( https://game.develop.playstation.net/ ) in advance.




Session/Invitation/Game Intent

	
R5112
R5303
R5307
	

This feature must not be used




Activity

	
R5301
R5302
	

This feature must not be used

Was this chapter helpful?  Yes  No
Publishing the Single Content/Entitlement in Multiple Countries/Regions

If you release the same content/entitlement in multiple countries/regions (including using the global publishing feature), you should pay particular attention to the following requirements:

R5005
Follow the requirement and set age level according to the rating for each applicable country/region. If additional countries/regions are added, it is acceptable to update the age level via patch.
R5207
Assign the cross button as the enter button according to the requirement.
R5158
Check R5158A in all supported languages.

Refer to Content Pipeline User Guide - Selling Products Globally for how to sell the same content/entitlement in multiple countries/regions.

Was this chapter helpful?  Yes  No
Notes on using the In-Game Commerce feature from an application server
In-Game Commerce debug features can be used to test applications that use In-Game Browsing to browse and purchase products. When this feature is enabled, the value returned from the In-Game Catalog Web API request will be replaced with dummy data. When calling the In-Game Catalog Web API (hereafter Web API) from an application of PlayStation®5, use "★Debug Settings" > "PlayStation Network" > "In-Game Commerce Debug". However, this setting is only valid when calling Web API from an application of PlayStation®5. The response will not be replaced with dummy data when the application server calls Web API. Therefore, use the In-Game Commerce debug header when calling the Web API from the application server. For details on the In-Game Commerce debug header, refer to In-Game Catalog Overview.
When using an application server, please use the In-Game Commerce debug header to perform test cases for R5051.
The In-Game Commerce debug header can be used for testing purposes in the development environment (sp-int). In the CertOps certification process, CertOps does not test using this header. Therefore, if an application server is used, please test it thoroughly and raise a waiver request with the below:
"TRC numbers requesting waiver": R5051
"Reason why waiver is needed": Because an application server is being used, it is not possible to execute R5051B, R5051C, R5051D, and R5051E using the "In-Game Commerce Debug" feature.
Was this chapter helpful?  Yes  No
Call rate limits
PlayStation™Network Web API
When PlayStation™Network Web APIs are called frequently enough to exceed the rate limit, an error code indicating that the rate limit has been exceeded is returned. It is important to implement handling in the application to not immediately retry when these errors are returned. For more details, refer to PlayStation™Network Web APIs Overview - Feature Overview - Rate Limit.
If the call rate limit is exceeded, a system message will be displayed. The system message includes the API group name and a message indicating that the call rate limit has been exceeded. For example, if the User Profile Web API call rate limit is exceeded, the following system message will be displayed:
[T-027][Warning]
userProfile:
Rate limit exceeded.
The system message does not include the API name. When different APIs are called within the same API group, the same system message will be displayed. Therefore, even if the same system message is displayed twice in a row, it is no problem as long as you can confirm these are made by separate API calls and not the result of retry processing.
NpUniversalDataSystem Library
When the number of UDS events an application sends exceeds the rate limit, the system will stop receiving the event for a while. For more details, refer to Universal Data System Guide - About the Universal Data System (UDS) - Data Reliability and NpUniversalDataSystem Library Overview - Using the Library - Debug Support Through the System Software.
When UDS events are sent that exceed the rate limit, the following system message will be displayed.
Debug:
sceNpUniversalDataSystemPostEvent: Over 300 events in 5 minutes.
Was this chapter helpful?  Yes  No
Next
Test Case Overview
>
English
日本語 (Japanese)
한국말 (Korean)
© 2026 Sony Interactive EntertainmentAbout UsTerms of UsePrivacy