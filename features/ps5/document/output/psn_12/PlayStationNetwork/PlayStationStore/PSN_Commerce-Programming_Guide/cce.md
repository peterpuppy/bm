# PlayStation™Network Commerce Programming Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce-Programming_Guide/cce.html

# Commerce Services

There are two commerce services available to applications:

* PlayStation®Store Delivered Content
* Commerce Catalog and Entitlements

Both services allow applications to link other service ids via service label for the purpose of selling content in-game. However, there are some important differences between the two.

## PlayStation®Store Delivered Content Vs. Commerce Catalog and Entitlements

The following table shows some of the differences between the PlayStation®Store Delivered Content and Commerce Catalog and Entitlements services.

|  | PlayStation®Store Delivered Content | Commerce Catalog and Entitlements |
| --- | --- | --- |
| Number of links | Up to eight | No limit |
| PSAC check using NpEntitlementAccess after sale | Available | Not Available |
| Primary usage | Sell and distribute content accessible within the same game, such as additional content. | Sell and distribute other fully downloadable games for cross-promotion. |

# PlayStation®Store Delivered Content

The PlayStation®Store Delivered Content service is the primary service for linking, selling, and accessing content across shared services. This service uses all current features including selling content in game, checking entitlements through NpEntitlementAccess, and more. It is important to know that this service must be used if the products you want to sell, like additional content, are accessible in game. Only up to eight services can be linked to the original application using PlayStation®Store Delivered Content.

# Commerce Catalog and Entitlements

The Commerce Catalog and Entitlements service is another commerce service whose primary
function is to simply upsell content that does not need to be accessible in-game. It is
important to understand that DLC and Additional Content cannot be accessed in-game using
the Commerce Catalog and Entitlements service. If Additional Content is sold using the
Commerce Catalog and Entitlements service, it will not be accessible in game using
NpEntitlementAccess.

As an example, this service would be suitable to distribute full downloadable games as
well as subsets of full games like game demos. Additionally, it may be useful for
cross-promoting and selling games from additional franchises controlled by a
publisher.

# Reference Materials

For more information on these services, refer to the guide below:

* [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html)