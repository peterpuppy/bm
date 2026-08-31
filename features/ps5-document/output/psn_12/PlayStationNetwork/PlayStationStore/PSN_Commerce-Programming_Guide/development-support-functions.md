# PlayStation™Network Commerce Programming Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PSN_Commerce-Programming_Guide/development-support-functions.html

# Development Support Functions

You can test the commerce-related functions of your application for proper operation under a variety of conditions related to wallet charging, in-game commerce scenarios, title store previews, regional store previews and promotion codes, and unified entitlement validity periods.

# Wallet Charging

For checkout processing to complete, there must be at least the price of the content charged to the user's wallet.

Wallets can be charged in the checkout process.

In the development environment, charge wallets as necessary using the following credit card information or the following numbers of the prepaid cards for PlayStation®Store:

## Credit Card

* **Credit card number:** See the table below for an example credit card number.
* **Expiration date:** Any.
* **Address:**

  + All fields can be arbitrary (excluding US/CA).
  + Actual existing state and postal code must be entered. Other fields can be arbitrary (US/CA).
* **Name:** Any alphabetical letters (1 character or more).
* **Security code:** Any 3-digit number.

Sample Credit Card Numbers

| **Country/Region** | **Card Type** | **Card Number** |
| --- | --- | --- |
| SIEA countries/regions (excluding Brazil) | VISA | 4444 4444 4444 4448 |
| SIEE/SIEJA countries/regions (excluding Korea) | VISA | 4111 1111 1111 1111 |

Unless specially noted, use the above credit card numbers in the development environment only by an account in a country/region supported by the PlayStation®Store as described in the [PlayStation™Network Commerce Service Overview](../PSN_Commerce_Service-Overview/__document_toc.html). However, server support may be delayed for a newly added country/region.

Use the information in the table below for the input information required for credit card registration for Brazil.

Brazil Credit Card Registration

| **Item** | **Input Value** |
| --- | --- |
| Card Number | 4111 1111 1111 1111 |
| CPF Number | 37043292239 |
| Phone Number +55 | Any 10-digit number. |
| Street Address 1 | Any alphabetical letters (1 character or more). |
| City | Any alphabetical letters (1 character or more). |
| State/Province | Any of the pulldown menu selections. |
| Postal Code | Any 8-digit number. |

## Prepaid Card for PlayStation®Store

The table below contains prepaid card information.

Prepaid Card Information

| **Country/Region** | **Card Number** | **Charged Price** |
| --- | --- | --- |
| Argentina | P25L-7TNE-FEH8 | 50.00 USD |
| Australia | 5L85-4HFF-3A9B | 80.00 AUD |
| Austria | D828-PEFE-L29H | 50.00 EUR |
| Belgium | RPQB-T7F5-NDG5 | 50.00 EUR |
| Bolivia | HHER-R2NG-6JG7 | 50.00 USD |
| Brazil | FPJQ-F7NA-RJ2Q | 85.00 BRL |
| Bulgaria | K2P5-TAN5-MD9M | 100.00 BGN |
| Canada | 7NE3-KHFR-TT63 | 50.00 CAD |
| Chile | HJDD-QKNK-44J6 | 50.00 USD |
| Costa Rica | H4Q2-TGNT-BQLA | 50.00 USD |
| Croatia | 5MBD-B2FK-LCBT | 350,00 HRK |
| Czech Republic | L45D-3NFM-DKRM | 1,500.00 CZK |
| Denmark | FPKN-5HFN-C7CB | 400.00 DKK |
| Ecuador | 5QEN-4KNQ-R96L | 50.00 USD |
| El Salvador | DCE6-87NF-G8QC | 50.00 USD |
| Finland | 3PGN-QDFF-Q2RJ | 50.00 EUR |
| France | Q5A3-2PF4-KPP4 | 50.00 EUR |
| Germany | R6PN-44FA-L4G9 | 50.00 EUR |
| Greece | P2PH-T8FM-R55N | 50.00 EUR |
| Guatemala | Q2HN-EGNP-T5KE | 50.00 USD |
| Honduras | JQQM-88NK-G4AC | 50.00 USD |
| Hong Kong | 5E2N-42FG-48NE | 160.00 HKD |
| Hungary | GRAK-6GN2-KC8B | 15000.00 HUF |
| India | 2T45-E6F2-JHLJ | 2,500 INR |
| Indonesia | GKD5-6NFA-7TG7 | 175,000 IDR |
| Ireland | AM8T-NMF8-8A39 | 50.00 EUR |
| Israel | 5KMA-6JN9-PF27 | 250.00 ILS |
| Italy | B676-EEFD-KQ6K | 50.00 EUR |
| Japan | M2LN-NHFM-66H9 | 10,000 JPY |
| Korea | BK7N-HCFE-EG92 | 50,000 KRW |
| Kuwait | 5HP5-GJNB-BK68 | 50.00 USD |
| Luxembourg | 77DP-66F5-F2JL | 50.00 EUR |
| Malaysia | EPCA-7GFF-EDGE | 60.00 MYR |
| Mexico | EHJP-44FF-CCAB | 50.00 USD |
| Netherlands | BQ77-98FP-CCQK | 50.00 EUR |
| New Zealand | 4M2P-6JFP-M4QG | 100.00 NZD |
| Nicaragua | EKC6-6MN5-7B4H | 50.00 USD |
| Norway | TQTD-QEFN-QNEJ | 400.00 NOK |
| Panama | GCC3-BGN5-TJ54 | 50.00 USD |
| Paraguay | 52NF-4TNM-584N | 50.00 USD |
| Poland | AGCF-FCF4-CPQT | 200.00 PLN |
| Portugal | F6BN-DJF7-R9E9 | 50.00 EUR |
| Qatar | GKBC-H8NF-3JP6 | 50.00 USD |
| Russia | 83NT-9QF2-QBQ6 | 1,500 RUB |
| Saudi Arabia | DP8B-85FK-P93A | 50.00 USD |
| Singapore | 4CAT-6MF6-KGND | 40.00 SGD |
| Slovenia | HC5A-J9FN-RA2D | 50.00 EUR |
| South Africa | RFP5-8NFA-NNPD | 500.00 ZAR |
| Spain | 6HC2-MEF9-77QE | 50.00 EUR |
| Sweden | 37GT-AGFQ-3QTJ | 400.00 SEK |
| Switzerland | 8LCJ-7CFA-333C | 80.00 CHF |
| Taiwan | 7DKD-5CF5-J7H2 | 600 TWD |
| Thailand | 25JK-GQF7-QBM9 | 1,000.00 THB |
| Turkey | P8KT-63FK-G33A | 100,00 TRY |
| UAE | E3TE-TLF8-ETNK | 50.00 USD |
| UK | QGFF-LMFL-5CE6 | 50.00 GBP |
| Ukraine | 3LPG-88NT-55DJ | 400.00 UAH |
| United States | 77R2-CLFC-7AK9 | 50.00 USD |
| Uruguay | ECJ5-PCNC-84M6 | 50.00 USD |

# PlayStation™Network - In-Game Commerce Debug

You can use the In-Game Commerce Debug feature to test the operation of an application that uses in-game browsing to browse and purchase products. This feature provides the following options:

* "Off"
* "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)"
* "[Empty Store](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_2)"
* "[Regular Discount](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_3)"
* "[Plus Discount for Plus](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_4)"
* "[Plus Discount for non-Plus](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_5)"
* "[Regular and Plus Bonus Discount for non-Plus](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_6)".

Of these options, the "[Regular Discount](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_3)", "[Plus Discount for Plus](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_4)", "[Plus Discount for non-Plus](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_5)", and "[Regular and Plus Bonus Discount for non-Plus](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_6)" are intended for use in tests of your application's ability to display various prices when discounts are set for an SKU. These options provide dummy values for the actual purchase price (`price`), the original price before a discount (`originalPrice`), and the discount price for PlayStation®Plus members (`plusUpsellPrice`).

Setting an option other than "Off" affects the values that an In-Game Catalog Web API request returns. For details on obtaining the various prices when discounts are set, see the [In-Game Catalog Web API Reference](../../../WebAPI/latest/In_Game_Catalog_WebAPI-Reference/__document_toc.html) document.

The remainder of this section provides additional detail about the effects of each option.

## Fake SKU and Metadata

The "Fake SKU and Metadata" option provides placeholder values for SKU labels, SKU prices and long descriptions. You can use the "Fake SKU and Metadata" option to ensure that your application's purchase-processing behavior requires the proper use of valid SKU labels.

**SKU Label**

You can use the "Fake SKU and Metadata" option to verify whether the application can display and use the correct SKU labels.

When the "Fake SKU and Metadata" option is set, all SKU labels obtained using the `GET container` request are changed to strings filled with the `Z` character.

The ability to proceed to purchase processing when "Fake SKU and Metadata" is set can be due to improper implementation, such as embedding a fixed SKU label in the application and using that hard-coded value instead of the invalid SKU that this option provides.

**SKU Price**

You can use the "Fake SKU and Metadata" option to verify the application's ability to display the correct SKU prices.

When the "Fake SKU and Metadata" option is set, all prices (`price`) obtained using the `GET container` request are changed to `9999999`. In the same manner, the display price (`displayPrice`) is also changed to "`$99999.99`".

If the displayed price does not change when "Fake SKU and Metadata" is set, it can be due to an improper implementation, such as embedding a fixed price in the application and displaying the hard-coded value instead of the `9999999` that this option provides.

**Size of Product Details (Long Description)**

You can use the "Fake SKU and Metadata" option to verify the application's ability to display the entire `description` value.

When the "Fake SKU and Metadata" option is set, the descriptive text (`description`) obtained using the `GET container` request is filled with a 4000-byte string. The last seven characters in the 4000-byte string are `----END`, and the other positions in the string are filled with "Z" or a string that may be displayed on PlayStation®Store.

## Empty Store

The "Empty Store" option allows you to simulate the availability of no items in the PlayStation®Store. You can use this option to verify that your application processes this condition correctly.

**Number of Store Items**

When the "Empty Store" option is set, the `GET container` request returns root category information only, and the number of items in the root category (`totalItemCount`) is `0`.

Set the "Empty Store" option to verify that the application handles the "no deliverables" use case correctly; for example, your application might notify the user of this condition, throw an exception, and disallow purchase processing.

## Regular Discount

The "Regular Discount" option provides placeholder values for SKU labels, SKU prices and long descriptions. You can use this option to determine whether your application displays regular discounts correctly.

**SKU Label**

The "Regular Discount" option provides the same SKU labels that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**Size of Product Details (Long Description)**

The "Regular Discount" option provides the same long descriptions that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**SKU Price**

When the "Regular Discount" option is set, all prices (`price`) obtained using the `GET container` request are changed to the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" price with a 50% regular discount applied; that is, the prices are changed to `4999999`. The display price (`displayPrice`) also changes accordingly; for example, from `"$99999.99"` to `"$49999.99"`.

If the displayed price does not change or if the discount is not displayed when "Regular Discount" is set in an application that supports the display of discounts, it can be due to inappropriate implementation, such as embedding a fixed price in the application and displaying the hard-coded price instead of the value that this option provides.

## Plus Discount for Plus Account

The "Plus Discount for Plus account" option provides placeholder values for SKU labels, SKU prices and long descriptions. You can use this option to check the display of a PlayStation®Plus discount for PlayStation®Plus members.

**SKU Label**

The "Plus Discount for Plus account" option provides the same SKU labels that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**Size of Product Details (Long Description)**

The "Plus Discount for Plus account" option provides the same long descriptions that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**SKU Price**

When the "Plus Discount for Plus account" option is set, all prices (`price`) obtained using the `GET container` request are changed to the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" SKU price with a 75% discount for PlayStation®Plus members applied; that is, the prices are changed to `2499999`. The display price (`displayPrice`) also changes accordingly; for example, from `"$99999.99"` to `"$24999.99"`. In addition, the `isPlusPrice` flag is set to `"true"`, which indicates that the PlayStation®Plus member discount is applied.

If a displayed price does not change when "Plus Discount for Plus account" is set, or if the discount is not displayed appropriately in an application that supports the display of PlayStation®Plus member discounts, it is possible that the application contains an inappropriate implementation, such as embedding a fixed price in the application and displaying the hard-coded value instead of the one that this option provides.

## Plus Discount for non-Plus Account

The "Plus Discount for non-Plus account" option provides placeholder values for SKU labels, SKU prices and long descriptions. You can use this option to check the display of a PlayStation®Plus discount for non-PlayStation®Plus members.

**SKU Label**

The "Plus Discount for non-Plus account" option provides the same SKU labels that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**Size of Product Details (Long Description)**

The "Plus Discount for non-Plus account" option provides the same long descriptions that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**SKU Price**

When the "Plus Discount for non-Plus account" option is set, all prices (`price`) obtained using the `GET container` request are changed to the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" SKU price; that is, the prices are changed to `9999999`. The display price (`displayPrice`) also changes accordingly; for example, to `"$99999.99"`. In addition, the discount price that can be applied when a non-PlayStation®Plus member becomes a PlayStation®Plus member (`plusUpsellPrice`) is 75% off; for example, the `plusUpsellPrice` price is `2499999`. The display price (`displayPlusUpsellPrice`) also changes accordingly; for example, to `"$24999.99"`.

If a displayed price does not change when "Plus Discount for non-Plus account" is set or if the discount is not displayed appropriately in an application that supports the display of PlayStation®Plus member discounts, it is possible that the application contains an inappropriate implementation, such as embedding a fixed price in the application and displaying the hard-coded value instead of the values that this option provides.

## Regular and Plus Bonus Discount for non-Plus Account

The "Regular and Plus Bonus Discount for non-Plus account" option provides placeholder values for SKU labels, SKU prices and long descriptions. You can use this option to check the display of a regular discount and a PlayStation®Plus discount for non-PlayStation®Plus members.

**SKU Label**

The "Regular and Plus Bonus Discount for non-Plus account" option provides the same SKU labels that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**Size of Product Details (Long Description)**

The "Regular and Plus Bonus Discount for non-Plus account" option provides the same long descriptions that the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" option provides.

**SKU Price**

When the "Regular and Plus Bonus Discount for non-Plus account" option is set, all prices (`price`) obtained using the `GET container` request are changed to the "[Fake SKU and Metadata](psn-in-game-commerce-debug.html#psn-commerce-programming-guide_3_2__psn-commerce-programming-guide_3_2_1)" SKU price with a 50% regular discount applied; that is, the prices are changed to `4999999`. The display price (`displayPrice`) also changes accordingly; for example, to `"$49999.99"`. Further, when a non-PlayStation®Plus member becomes a PlayStation®Plus member, the discount prices (`plusUpsellPrice`) are an additional 25% lower, for a total discount of 75% off the regular price; for example, the `plusUpsellPrice` is `2499999`. The display price (`displayPlusUpsellPrice`) also changes accordingly; for example, to `"$24999.99"`.

If a displayed price does not change when "Regular and Plus Bonus Discount for non-Plus account" is set, or if the discount is not displayed appropriately in an application that supports display of PlayStation®Plus member discounts, it is possible that the application contains an inappropriate implementation, such as embedding a fixed price in the application and displaying the hardcoded value instead of the value that this option provides.

# Title Store/Regional Store Previews and Promotion Code Redemption

On the Development Kit, the system software provides features for previewing the In-Game Catalog for a Title Store and the Global Catalog for a Regional Store, in addition to features for redeeming promotion codes.

To activate these features, do the following steps:

## (1) Sign in.

Sign in with an account for PlayStation™Network that has Title Admin or Title Dev account privileges set in DevNet. Title Admin/Title Dev requires Title privileges for an account on PlayStation™Network. For more details on how to assign these privileges, see [PlayStation™Network Overview - Reference Information - Features Restricted by Title Dev/Title Admin Roles During Development](../PSN-Overview/features-restricted-by-title-dev-title-admin-roles-during-de.html).

## (2) Display the feature selection screen.

Select **★Store Preview** in the function area of the system software's home screen to display a feature selection screen.

## (3) Select feature to use.

Select the feature to use from the pull-down menu:

* Title Store Preview - Previews the In-Game Catalog for the Title Store.
* Regional Store Preview - Previews the product which has been published through Content Pipeline using Product Preview.
* Voucher Redemption - Redeems promotion codes.

## (4) Set the Network Platform Title ID and NP Service Label.

Set the Network Platform Title ID (example: NPXS00004\_00) to **Network Platform Title
ID** and the NP service label to **Service Label** of the menu.

Input is not necessary when **Voucher Redemption** is selected in step [(3)](title-store-regional-store-previews-and-promotion-code-redem.html#psn-commerce-programming-guide_3_3__psn-commerce-programming-guide_3_3_3). Input is automatically prohibited.

## (5) Start up the screen for the selected feature.

The screen for the feature selected in step [(3)](title-store-regional-store-previews-and-promotion-code-redem.html#psn-commerce-programming-guide_3_3__psn-commerce-programming-guide_3_3_3) is displayed when selecting the **Open** button.

# Operation Test upon Expiration of the Validity Period

The system software of Development Kits provides a feature for testing the operation of
applications that use unified entitlements with a validity period set.

Typically, the validity period is evaluated against the internal clock, which is set over
the network. However, when setting **★Debug Settings** - **System** - **Debug
NPDRM Clock** to "On" in a state when **★Debug Settings** -
**PlayStation™Network** - **Require purchased license** is set to "On", the
validity period is evaluated against the time set on the displayed date/time-setting
screen.

Make sure that your application runs as expected when setting a date/time before or after
the expiration of the validity period.

In addition, the date/time set after setting **Debug NPDRM Clock** to "On" is also
used to determine whether to display the PlayStation®Plus icon on the system-software
screen. The icon is displayed on-screen if the date/time is within the validity period
of the user's entitlement.

Using the [Development Account - Commerce Editor tool](https://p.siedev.net/resources/documents/SDK/latest/Development_Accounts-Users_Guide/0005.html#__document_toc_00000016)
allows developers to test unified entitlement consumables such as PSVC/PSCONS, where
aging accounts can be done to expire entitlements. Revocation tests can be done here as
well.