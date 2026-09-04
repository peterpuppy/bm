# Advanced Player Profile Editor User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Advanced_Player_Profile_Editor-Users_Guide/bandwidth.html

# Editable Properties

The editor allows you to modify specific properties of an account on the PlayStation™Network. Property details are documented in the [Advanced Player Profile Overview - Properties Provided by Advanced Player Profile](../../../WebAPI/latest/Advanced_Player_Profile-Overview/properties-provided-by-advanced-player-profile.html).

# Bandwidth

This topic provides Information on how bandwidth values are formatted in the Advanced
Player Profile Management API.

Note that in the Advanced Player Profile Management Web API and the Advanced Player Profile Web API, the Average Bandwidth and Standard Deviation values are represented as bits per second (bps), but for convenience users can enter these values in Mbps in the Advanced Player Profile Editor.

For example, to represent a user having an average of a 50 Mbps, a user would enter 50 for Average Bandwidth, but in the APIs the value will be represented as 50000000.

The maximum value for Bandwidth Average and Standard Deviation is 2147, which would represent 2.147 Gbps.