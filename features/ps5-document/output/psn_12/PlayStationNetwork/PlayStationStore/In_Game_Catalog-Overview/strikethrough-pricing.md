# In-Game Catalog Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/In_Game_Catalog-Overview/strikethrough-pricing.html

# Discounts in the Title Store

This chapter provides information on discount attributes that you can apply to products in your store.

The price of a store product is defined by one or more attributes that are included in the product `container` object. These attributes are contained in the `skus` child object of the product container. In addition to having a default price that is represented by an attribute, a product could be assigned one or more attributes that represent discount prices.

You can use discount price attributes to display discount prices in your title store. Your in-game catalog can show the discount prices that are offered to users of the PlayStation™Store. Displaying discount pricing, as well as the discounts that are available to new PlayStation®Plus members, can increase sales. For purposes of this discussion, a "PSN user" is a PlayStation™Network account holder who does not subscribe to the PlayStation®Plus service.

The discount price attributes are optionally included in an element of the `skus` array as name-value pairs.

The table below describes discount price attributes. Applications reference the discount attributes to retrieve and display product pricing information in a title store. For detailed information about each attribute and how to obtain pricing information, see [In-Game Catalog Web API Reference](../In_Game_Catalog_WebAPI-Reference/__document_toc.html).

Discount Price Attributes

| **Attribute Name** | **Description** |
| --- | --- |
| `originalPrice` | The price of the product before the discount is applied. This price is an integer that does not include the currency code or symbol. |
| `displayOriginalPrice` | A character string rendering of the price of the product before the discount is applied. Its inclusion in the response body indicates that a discount was applied to the product. This display rendering of the original price includes the currency code or symbol.  The `displayOriginalPrice` attribute is returned with the `originalPrice` attribute. |
| `plusUpsellPrice` | The price of an upsell offer of a PlayStation®Plus discount to a user who does not have a PlayStation®Plus membership. This price is an integer that does not indicate the currency code or symbol. |
| `displayPlusUpsellPrice` | A character string rendering of the price of the product for a PlayStation®Plus discount to a user who does not have a PlayStation®Plus membership. This display rendering of the upsell price includes the currency code or symbol. The `plusUpsellPrice` attribute is returned with the `displayPlusUpsellPrice` attribute. |
| `isPlusPrice` | A boolean value that indicates whether the PlayStation®Plus discount was applied. |

# Strikethrough Pricing

This topic provides information on how strikethrough pricing is displayed in your store.

"Strikethrough pricing" is used to display discounts in the PlayStation™Store. This means that when a product is discounted, the original price and the discount price are *both* shown. The original price, however, is displayed in strikethrough text. This method of display makes it easy for users to identify discounts and can help to increase sales.

Title stores should display prices the same way the regional PlayStation™Store does. This includes the display of discount prices in strikethrough text, in the specified colors, and with the PlayStation®Plus icon, as appropriate.

# Discount Prices

This topic provides details on retrieving pricing information for discounts applied to your products.

The `GET Container` operation retrieves price information for those discounts that apply to the product. For example, the product `container` object that is the root object in a JSON response could include only three discount price attributes in the `skus` child object: `originalPrice`, `displayOriginalPrice`, and `isPlusPrice:`

```
{
  "skus": [
    {
      "displayOriginalPrice": "100.00USD",
      "displayPrice": "40.00USD",
      "endDate": "2019-05-30T01:00:00Z",
      "id": "IV0002-NPXS29017_00-PSTP000000000000-U009",
      "isPlusPrice": true,
      "isPurchaseable": true,
      "label": "U009",
      "name": "PSTP-IGC-SKU-FOR-TEST",
      "originalPrice": 10000,
      "price": 4000,
      "type": "standard",
      "useLimit": 0
    }
  ]
}
```

In this case, the `originalPrice` attribute represents the original price of a discounted product, the `displayOriginalPrice` attribute provides the discounted price for display, and the `isPlusPrice` attribute indicates that the discount applies to a PlayStation®Plus member.

For a product that has multiple discounts, the `skus` object in the product container could include all discount price attributes, including: `originalPrice`, `displayOriginalPrice`, `plusUpsellPrice`, `displayPlusUpsellPrice`, and `isPlusPrice`:

```
{
  "skus": [
    {
      "displayOriginalPrice": "100.00USD",
      "displayPlusUpsellPrice": "30.00USD",
      "displayPrice": "50.00USD",
      "endDate": "2019-05-30T01:00:00Z",
      "id": "IV0002-NPXS29017_00-PSTP000000000000-U009",
      "isPlusPrice": false,
      "isPurchaseable": true,
      "label": "U009",
      "name": "PSTP-IGC-SKU-FOR-TEST",
      "originalPrice": 10000,
      "plusUpsellPrice": 3000,
      "price": 5000, 
      "type": "standard",
      "useLimit": 0
    }
  ]
}
```

In this case, the `originalPrice` attribute represents the original price of a discounted product, the `displayOriginalPrice` attribute provides the discounted price for display, and the `isPlusPrice` attribute indicates that the discount applies to a PlayStation®Plus member. Additionally, the `plusUpsellPrice` attribute provides an integer that represents the discounted price of the product for a PlayStation™Network user, if the user becomes a PlayStation®Plus member. The `displayPlusUpsellPrice` attribute provides a string representation of the discounted price for display in the in-game catalog.

# Displaying Discount Prices

This topic provides information on how discount prices are displayed in your store.

Your application must implement the logic that is required to display discount prices from your in-game catalog.

Display the discount prices in accord with the following guidelines:

* Use strikethrough text to display the `displayOriginalPrice` value.
* Display the PlayStation®Plus icon to the left of the `displayPlusUpsell` value.

## Discount Price Examples

The following examples show five different ways you can display discount prices.

**Show the Best Price**

Display the best price that is available to PlayStation™Network users.

Only one price is shown. The in-game catalog does not show discount pricing.

**Show the Best Price and the Original Price**

Display the best price and the original price. There is no additional discount for PlayStation®Plus membership in the following display pattern.

Strikethrough pricing is applied to the original price. The two prices are shown in the same color. The original price should be displayed above or to the left of the best price.

**Show the Best Price and the Original Price for PlayStation™Network users and for PlayStation®Plus members**

Display the original price using strikethrough pricing and in a smaller font.

The best pricing for PlayStation™Network users is shown to the right of the strikethrough price and above the price for PlayStation®Plus members. The price that is available to PlayStation®Plus members is shown with the PlayStation®Plus icon and rendered in the hexadecimal color #FFCD00.

**Show the Best Price and the Original Price for PlayStation®Plus members**

Display the original price using strikethrough pricing.

The price that is available to PlayStation®Plus members is shown with the PlayStation®Plus icon and rendered in the hexadecimal color #FFCD00. The PlayStation®Plus membership price is shown below the strikethrough price.

**Show the Best Price for PlayStation™Network users and for PlayStation®Plus members**

Display the best price above the price that is available to PlayStation®Plus members.

The price that is available to PlayStation®Plus members is shown with the PlayStation®Plus icon and rendered in the hexadecimal color #FFCD00.

## Display Patterns

The five display cases fall into the following three patterns of logic. Your title store can implement any of these patterns to display discount pricing.

The following tables shows the different permutations of discount attributes that the `skus` object contains for each pattern.

Pattern 1: Display Case A

This pattern supports only Case A.

| **Discount Combination** | **Includes originalPrice SKU** | **Includes displayPlusUpsell SKU** | **Is Plus Price** | **Display** |
| --- | --- | --- | --- | --- |
| **Any discount or none** | N/A | N/A | N/A | Display the `displayPrice`. |

Pattern 2: Display Case A and Case B

This pattern supports Case A and Case B.

| **Discount Combination** | **Includes originalPrice attribute** | **Includes displayPlusUpsell attribute** | **Is Plus Price** | **Display** |
| --- | --- | --- | --- | --- |
| **Any discounts** | Yes | N/A | N/A | Display the `displayOriginalPrice` in strikethrough text.  Display the `displayPrice`. |
| **No discount** | No | N/A | N/A | Display the `displayPrice`. |

Pattern 3: Display Cases A through E

This pattern supports Case A through Case E.

| **Discount Type** | | **Included Attributes** | | **is\_plus\_price** | **Display value** |
| --- | --- | --- | --- | --- | --- |
|  | | `originalPrice` | `displayPlusUpsell` |  |  |
| **A** | **No discounts** | No | No | false | displayOriginalPrice |
| **B** | **Regular discount** | Yes | No | false | * `displayOriginalPrice` (strikethrough text) * `displayPrice` |
| **C** | **Plus discount** | Yes | No | true | * `displayOriginalPrice` (strikethrough text) * `displayPrice` (and PlayStation®Plus icon) |
| **D** | **Plus upsell price for PlayStation™Network users** | No | Yes | false | * `displayPrice` * `displayPlusUpsellPrice` (and PlayStation®Plus icon) |
| **E** | **Regular discount and bonus discount, for PlayStation™Network users** | Yes | Yes | false | * `displayOriginalPrice` (strikethrough text) * `displayPrice` * `displayPlusUpsellPrice` (and PlayStation®Plus icon) |

## Verifying Discount Price Display Configuration

You can use the debug settings that are provided in the PlayStation® system software to verify that discount prices are correctly displayed in your application.

Select from the following debug options:

* **Regular Discount**
* **Plus Discount for Plus account**
* **Plus Discount for non-Plus account**
* **Regular and Plus Bonus discount for non-Plus account**

For more information, see [System Software Overview](../../../SDK/latest/System_Software-Overview/__document_toc.html).