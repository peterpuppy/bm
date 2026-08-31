# PlayStation™Network Game Hub Preview Application Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Game_Hub_Preview_Application-Overview/preview-application.html

# Using the Preview Application

This chapter provides details on how to use the Game Hub Preview Application.

The DevKit provides a Preview Application that publishers can use to preview a product's game hub content as it appears in various stages of the game lifecycle. For information about the game lifecycle, see [Game and App Hub Overview](https://learn.playstation.net/bundle/content-pipeline/page/GameHub_Overview.html).

The following is the general workflow you would follow to preview a product's game hub content:

1. In Content Pipeline, [create a concept and a full-game or demo product group](https://learn.playstation.net/csh?context=CreatingGameConcept_CP). This step generates a concept ID, product ID, and an NP Title ID.
2. In Content Pipeline, [submit concept or product level metadata and assets](https://learn.playstation.net/csh?context=SubmittingMetadataAssetsProduct_CP) and publish to the sp-int development environment.
3. In DevNet, use the NP Title ID you generated earlier to register your title. For more information on title registration, see [PlayStation™Network Service Setup Guide - Registering Titles](../PSN_Service_Setup-Guide/registering-titles.html).
4. Create a package file (.pkg) for your game and upload it to PlayStation®5 GEMS. Once GEMS imports the package file, you will need to use Content Pipeline to configure the corresponding entitlement in sp-int. This step is only required for previewing the product launched phase. The package you upload to GEMS does not need to be final, you can always go back and replace it with the final version. For more information on package creation, see [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html).
5. Optional: Create a draft Terms of Sale in Content Pipeline, associate the entitlement to the product and publish it to the sp-int development environment. This is only required for previewing the product launched phase.
6. On the DevKit, enter the concept ID, product ID, or title ID you'd like to see in the Game Hub Preview Application.

The Preview Application shows what your game will look like on a product's game hub during the Concept-Announce phase, product launched phase, and the product sold phase.

Note:

This step requires an account on PlayStation™Network in the development environment with title privileges. For more details on how to assign these privileges, see [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html).

For more information on Content Pipeline, see [Getting Started with Content Pipeline](https://learn.playstation.net/bundle/content-pipeline).

# Previewing Game Hub Content

This topic provides details on how to preview a product's game hub content.

On the PlayStation®5 Development Kit, navigate to the Game Hub Preview Application and enter either concept ID, or product ID, or title ID to preview. Concept ID allows you to preview the announce phase, product ID is required to preview the product launched phase (examples: pre-order start, demo, full game launch etc.), and title ID is needed to preview the product sold phase.

Note:

If you find the on-screen keyboard cumbersome, you can plug in an external keyboard to speed up the ID entry process.

If the concept ID is valid and your development environment account on PlayStation™Network has title privileges to preview any NP Title ID within the requested concept ID, the preview application displays concept content that you are allowed to access; otherwise, it displays an error message. If you see an error message, click **Back** to return to the concept ID entry field.

Complete Publishing and Preview Workflow

For more information, see [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html).

## Previewing Concept-Announced Content

The Concept Announced stage drives players' anticipation for a product before it becomes available for sale. In support of this stage, you can submit to Content Pipeline the content that will populate the Cover Page, the Game Media Strand, the Game Highlights Strand, and the Game Info Page. Note that news stories and SIE merchandising cannot be previewed in the Game Hub Preview Application. For more information, see [Game and App Hub Overview](https://learn.playstation.net/bundle/content-pipeline/page/GameHub_Overview.html).

Previewable in the Concept-Announced Phase
Previewable Content at the Product Available Phase
Previewable Content at the Product Sold Phase

You cannot preview News Stories, SIE Merchandising, Activity, or user-generated content (UGC). If you want to preview News stories,
you must use the Consumer Activation Suite.

## Examples of a Product's Game Hub Display

The following figures provide examples of a product's game hub display in preview mode.

Product's Game Hub Cover
Game Media Strand
Game Highlights Page
Game Info Page

Certain metadata fields may not display all the text you enter on the Content Pipeline. For example, the sub-header field on the cover and the edition upsell features may not accommodate the maximum number of characters you could enter on the Content Pipeline. Be sure to check the Game Hub Preview Application for how your content renders before finalizing your concept/product set up on the Content Pipeline.

The latest Game Hub Preview Application includes UI updates. You can now verify your disc upgrade setup in the Product Available phase. The goal of enabling this functionality is to help you validate your disc upgrade offer setup. If you have a valid disc upgrade setup for a specific PlayStation®5 product, and you have the corresponding PlayStation®4 disc inserted, the cover page within the Product Available phase will display the disc upgrade call-to-action CTA as well as the text above the CTA.

Disc Upgrade

If you have a valid disc upgrade setup, but do not have the corresponding PlayStation®4 disc inserted, (for unreleased title, ISO disc or retail disc can be used) you will not see the disc upgrade CTA, instead, you will either see a 'Learn More' CTA or CTAs associated with other SKUs you have set up under the product. 'Learn More' will be shown if you only have a disc upgrade SKU under the product.

Disc Upgrade Without Corresponding Disc

If you do not have a valid disc upgrade product setup, you'll see the normal 'Placeholder' CTA.

Note:

You cannot click CTAs.

No Disc Upgrade

Note:

This feature can only be used once you have configured your product as explained in the following article: [Configuring a PS4 Disc to PS5 Digital Upgrade](https://learn.playstation.net/bundle/content-pipeline/page/Product_UpgradePS4DiscPS5Digital.html)

# Access Controls

This topic provides details on the title privileges required for a PlayStation™Partners account to preview game hub content.

A PlayStation™Partners account can upload assets and metadata to Content Pipeline, but previewing a product's game hub assets and metadata in the Preview Application requires an account on PlayStation™Network in the development environment that has title privileges for the specific NP Title ID being previewed.
After registering the NP Title ID on DevNet, a Title Collaborator with at least editor permission on DevNet can add title privileges to an existing account on PlayStation™Network in the development environment.
Ensure that you obtain the necessary title privileges for each title you intend to preview per region.

Access Control Based on Title Privileges

For more details on how to assign these privileges, see [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html).