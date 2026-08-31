# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/multi-lingual-support.html

# Creating Trophy Configuration Data

This topic describes the composition of trophy configuration data (trophy assets) and a summary of how to create this data, along with the specifications for the data. An example of what is displayed onscreen is provided in "[Reference: Displaying of Trophies by the System Software](reference-displaying-of-trophies-by-the-system-software.html "This topic describes how trophy sets are displayed in the UI of the system software.")" for you to refer to if necessary.

# Composition of Trophy Configuration Data

Trophy configuration data includes the information below. Using the UDS Management Tool, you can select items of this data and register image or text data prepared ahead of time to create trophy configuration files. For details about trophy configuration files, refer to "[Overview of Application Development](overview-of-application-development.html "This topic describes trophy-related processing you need to perform during the application development process.")".

## Information for the Trophy Set (Base Game Group)

* [Default Language](multi-lingual-support.html#trophy-system-overview_6_3__trophy-system-overview_6_3_1)
* [Trophy Set Still-image Icon](trophy-set-still-image-icon.html) (image with multi-lingual Support)
* [Trophy Set Name](trophy-set-name.html) (text with multi-lingual support)

## Information for the Trophy Group

* [Trophy Group Still-image Icon](trophy-group-still-image-icon.html) (image with multi-lingual Support)
* [Trophy Group Name](trophy-group-name.html) (text with multi-lingual support)

## Information for Each Trophy

* [Trophy Still-image Icon](trophy-still-image-icon.html) (image)
* [Trophy Name](trophy-name.html) (text with multi-lingual support)
* [Trophy Details](trophy-details.html) (text with multi-lingual support)
* [Names of Rewards Relating to Trophies](names-of-rewards-relating-to-trophies.html) (text with multi-lingual support)
* [Still-Image Icons for Rewards Relating to Trophies](still-image-icons-for-rewards-relating-to-trophies.html) (image)
* [Trophy grade](trophy-attributes.html#trophy-system-overview_2_2__trophy-system-overview_2_2_2)
* [Trophy show/hide attribute](trophy-attributes.html#trophy-system-overview_2_2__trophy-system-overview_2_2_3)
* [Trophy platinum link attribute](trophy-attributes.html)
* [Progressive trophy attribute](trophy-attributes.html#trophy-system-overview_2_2__trophy-system-overview_2_2_5)
* [Unlocking condition for the trophy](configuration-of-trophies.html)

# Summary of How to Create Trophy Configuration Data

Trophy configuration data is created using the UDS Management Tool. The created trophy configuration data will be included, as trophy00.ucp, in the package metadata file (npconfig.zip) that can be downloaded from GEMS. Refer to [Universal Data System Guide - Using the UDS Management Tool](../Universal_Data_System-Guide/using-the-uds-management-tool.html) for details regarding the operation of the UDS Management Tool.

Extract the downloaded package metadata file, and refer to the "[Placement of the Trophy Configuration and UDS Configuration Files](placement-of-the-trophy-configuration-and-uds-configuration.html)" section to save the extracted files to the specified directory.

The maximum size of trophy00.ucp is 1 GiB.

# Multi-lingual Support

The trophy set still-image icon, trophy set name, trophy group still-image icon, trophy group name, trophy names, trophy details, and reward names related to trophies support switching of languages by the system software. If these are made available in the applicable language, trophy data in the appropriate language, as specified in the system software language settings, will be selected.

The supported languages are as follows;

* Japanese
* English (United States)
* French
* Spanish
* German
* Italian
* Dutch
* Portuguese (Portugal)
* Russian
* Korean
* Chinese (Traditional)
* Chinese (Simplified)
* Finnish
* Swedish
* Danish
* Norwegian
* Polish
* Portuguese (Brazil)
* English (United Kingdom)
* Turkish
* Spanish (Latin America)
* Arabic
* French (Canada)
* Czech
* Hungarian
* Greek
* Romanian
* Thai
* Vietnamese
* Indonesian

## Default Language

Create trophy configuration data in at least one language, and choose one of those languages to be the default language. Because trophy configuration data cannot be modified later, it is recommended that the default language be set to English if a title might be put on sale in multiple territories.

# Trophy Set Still-image Icon

The trophy set still-image icon is an image that represents the trophy set.

In most cases, this image is the same as the still-image icon of the application.

The trophy set still-image icon can be provided in multiple languages to support switching by the system software. The icon must be provided in the default language; icons in all other languages are optional.

## Picture Size

512 x 512 pixels

## Image Format

PNG, 32 bit or 24 bit

Do not use interlaced format.

## File Size

There are no restrictions.

## Method of Creation

Use any commercially available, free, or open-source image manipulation tools.

# Trophy Set Name

The trophy set name is text data indicating the name of the trophy set.

In most cases, this is the same as the application title.

The trophy set name can be provided in multiple languages to support switching by the system software. The trophy set name must be provided in the default language and in all the languages supported by the application; the provision of the trophy set name in other languages is optional.

## Size

128 bytes

## Format

UTF-8

Up to 3 lines (up to 2 line feed codes). Use 0x0a for line feeds.

## Notes Regarding the Display

If the text does not fit in the width of the display area, line feed characters may be inserted automatically. Additionally, if the display area is only one line, any line feed characters may be replaced with spaces to display the text on a single line.

# Trophy Group Still-image Icon

The trophy group still-image icon is an image that represents the trophy group.

In most cases, the same image as the still image used to represent the additional content is used.

The trophy group still-image icon can be provided in multiple languages to support switching by the system software. The icon must be provided in the default language; icons in all other languages are optional.

## Picture Size

512 x 512 pixels

## Image Format

PNG, 32 bit or 24 bit

Do not use interlaced format.

## File Size

There are no restrictions.

## Method of Creation

Use any commercially available, free, or open-source image manipulation tools.

# Trophy Group Name

The trophy group name is text data indicating the name of the trophy group.

In most cases, this is the same as the name of the application's additional content.

Language-switching is supported. The default-language trophy group name is required; all other languages are optional.

## Size

128 bytes

## Format

UTF-8

Up to 3 lines (up to 2 line feed codes). Use 0x0a for line feeds.

## Notes Regarding the Display

If the text does not fit in the width of the display area, line feed characters may be inserted automatically. Additionally, if the display area is only one line, any line feed characters may be replaced with spaces to display the text on a single line.

# Trophy Still-image Icon

The trophy still-image icon is an image that represents a trophy and must be provided for each of the trophies in the trophy set. The same image can be used for multiple trophies. However, it is recommended that each trophy icon represents the characteristics of the trophy itself rather than using the same icon for all the trophies in a grade type, for example.

On the trophy collection screen of the system software, the still-image icon of a trophy will be displayed when it is unlocked (when the user earns the trophy).

Note:

Trophies that have not been unlocked are displayed in silhouette on the trophy collection screen. Because this silhouette image is automatically generated by the system software based on the trophy still-image icon, there is no need to create it beforehand.

Language-switching is not supported. The same images are used across all languages.

## Picture Size

512 x 512 pixels

## Image Format

PNG, 32 bit or 24 bit

Do not use interlaced format.

## File Size

There are no restrictions.

## Method of Creation

Use any commercially available, free, or open-source image manipulation tools.

# Trophy Name

The trophy name is text data indicating the name of a trophy.

The trophy name can be provided in multiple languages to support switching by the system software. It must be provided in the default language; all other languages are optional.

## Size

128 bytes

## Format

UTF-8

Up to 3 lines (up to 2 line feed codes). Use 0x0a for line feeds.

## Notes Regarding the Display

If the text does not fit in the width of the display area, line feed characters may be inserted automatically. Additionally, if the display area is only one line, any line feed characters may be replaced with spaces to display the text on a single line.

# Trophy Details

Trophy details are text data describing a trophy.

Language-switching is supported. Details must be provided in the default language; all other languages are optional.

## Size

1024 bytes

## Format

UTF-8

Supports as many line feed codes as necessary. Use 0x0a for line feeds.

## Notes Regarding the Display

If the text does not fit in the width of the display area, line feed codes will be inserted automatically. Additionally, if the display area is only one line, any line feed characters may be replaced with spaces to display the text on a single line.

# Names of Rewards Relating to Trophies

This is text data describing any in-game rewards that can be earned by unlocking the trophy. Only set a string value if there is a reward that the user can earn.

Language-switching is supported. The name of the reward in the default language is required, while its name in other languages is optional.

## Size

128 bytes

## Format

UTF-8

Up to 3 lines (up to 2 line feed codes). Use 0x0a for line feeds.

## Notes Regarding the Display

If the text does not fit in the width of the display area, line feed characters may be inserted automatically. Additionally, if the display area is only one line, any line feed characters may be replaced with spaces to display the text on a single line.

# Still-Image Icons for Rewards Relating to Trophies

These are images that represent in-game rewards that can be earned by unlocking trophies. Only set images if there are rewards that can be earned.

Language-switching is not supported. The same images are used across all languages.

## Picture Size

512 x 512 pixels

## Image Format

PNG, 32 bit or 24 bit

Do not use interlaced format.

## File Size

There are no restrictions.

## Method of Creation

Use any commercially available, free, or open-source image manipulation tools.