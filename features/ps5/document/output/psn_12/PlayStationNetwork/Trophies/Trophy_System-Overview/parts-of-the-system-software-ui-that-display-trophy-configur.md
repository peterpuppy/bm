# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/parts-of-the-system-software-ui-that-display-trophy-configur.html

# Reference: Displaying of Trophies by the System Software

This topic describes how trophy sets are displayed in the UI of the system software.

Trophy assets such as icons and descriptions are displayed on various screens of the system software. Refer also to the "[Creating Trophy Configuration Data](creating-trophy-configuration-data.html "This topic describes the composition of trophy configuration data (trophy assets) and a summary of how to create this data, along with the specifications for the data. An example of what is displayed onscreen is provided in \"Reference: Displaying of Trophies by the System Software\" for you to refer to if necessary.")" chapter, which describes the image sizes and formats of trophy assets. Note that the behavior of the system software, image designs, and text may change in the future and that these specifications are not guaranteed to remain the same indefinitely.

# Parts of the System Software UI That Display Trophy Configuration Information

Significant system software screens that display trophy sets include the following:

* Trophy Title List Screen
* Trophy Group List Screen
* Trophy List Screen
* Control Center Screen
* Trophy Details (Activity Card)

# Trophy Title List Screen

Game titles that the player has played are displayed on the trophy title list screen.

Trophy Title List

* 1. Trophy set still-image icon (base game group)
* 2. Trophy set name (base game group)

# Trophy Group List Screen

Trophy groups included in a selected title are displayed on the trophy group list screen. This screen is skipped if the title only has a base game group.

Trophy Group List

* 3. Trophy group still-image icon
* 4. Trophy group name

# Trophy List Screen

All trophies included in a selected trophy group are displayed on the trophy list screen.

Trophy List Screen

* 5. Trophy still-image icon (silhouette)
* 6. Trophy still-image icon
* 7. Progressive trophy (percentage display)
* 8. Trophy name
* 9. Trophy grade
* 10. Icon label indicating there are hints
* 11. Trophy details

# Control Center Screen

On the control center screen, trophies from games that the user is playing may be displayed as recommended activities.

Example of Trophies Being Displayed on the Control Center Screen

* 10. Icon label indicating there are hints

Example of Trophies Being Displayed on an Activity Card

* 8. Trophy name
* 9. Trophy grade
* 10. Icon label indicating there are hints
* 11. Trophy details
* 12. Trophy progress:

  When the value of the trophy unlocking condition has three digits, progress toward a trophy will be displayed as a fraction. If there are four or more digits, progress toward a trophy will be displayed as a percentage.
* 13. Still-image icon for reward relating to the trophy
* 14. Name of reward relating to the trophy

# Trophy Details (Activity Card)

The details of the selected trophy are displayed. On an activity card in the control center screen, detailed information is displayed to the right of the trophy list.

The [following figure](trophy-details-activity-card.html#trophy-system-overview_7_6__fd8f6960-e267-11ee-bd3d-0242ac120002) shows examples of a locked trophy (left image) and an unlocked trophy (middle and right images).

Trophy Details (Activity Card)

* 5. Trophy still-image icon (silhouette)
* 6. Trophy still-image icon
* 7. Progressive trophy (percentage display)
* 8. Trophy name
* 9. Trophy grade
* 10. Thumbnail of a hint video or a hint image
* 11. Trophy details
* 12. (Trophy unlocking status)
* 13. Still-image icon for reward relating to the trophy
* 14. Name of reward relating to the trophy
* 15. Trophy group still-image icon included in the trophy
* 16. Trophy group name included in the trophy