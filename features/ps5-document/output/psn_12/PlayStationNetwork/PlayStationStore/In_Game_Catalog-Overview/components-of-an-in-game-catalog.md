# In-Game Catalog Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/In_Game_Catalog-Overview/components-of-an-in-game-catalog.html

# In-Game Catalog Web API Overview

This chapter provides an overview of the In-Game Catalog Web API.

The PlayStation™Network (PSN) offers application developers the opportunity to create a *title store*, a store that is local to an application. Creating a title store allows you to offer *in-game* commerce opportunities to users. The title store can be either the PlayStation™Network system software store as well as a custom in-game store (also called an in-game catalog).

The PlayStation™Store includes regional and title stores. The PlayStation™Store that is accessed from the system software menu is implemented as a regional store that offers users a curated selection of products based on their country and region. The Content Pipeline application provides centralized access to product information. Information about the Content Pipeline application can be found in the documentation. See [Getting Started with Content Pipeline](https://learn.playstation.net/bundle/content-pipeline/page/Getting_Started.html) for more information.

The PlayStation™Store that is accessed from within an application is implemented as a title store. A title store offers users a selection of products based on their relevance to the application. A title store uses a subset of information from the Content Pipeline application to create select in-game opportunities for commerce.

The In-Game Catalog Web API provides REST resources and requests that allow applications to query information about store products and categories for use in a title store. The In-Game Catalog Web API does not allow applications to define or change information that is managed in the Content Pipeline application.

# Title Store

This topic provides information on the title store and catalog structure.

A title store is a store defined within the context of a PlayStation® application. Access to title stores is only through the application in which they are defined.

Your title store can offer users the opportunity to buy items that enhance game play from within the context of the application. A title store can also offer players a special membership as a "service".

The fundamental component of a title store is an in-game catalog.

## In-game Catalog

A title store uses an "in-game catalog" that contains a curated selection of products. The Content Pipeline application defines and manages the in-game catalog.

A PlayStation™Store catalog is structured as a hierarchical tree of categories and products. The in-game catalog is defined as a series of nested objects that represent the categories and products of this hierarchical tree.

A container is the basic component of an in-game catalog. Containers are represented by the `container` object. The `container` object is a JSON representation of a REST resource.

The `container` object is the sole resource that the In-Game Catalog Web API defines. There are two kinds of containers in an in-game catalog: products and categories. The `type` field of the `container` object identifies whether the container is a "product" or "category". The `container` objects that represent products and categories include all the information necessary for use in a title store.

Because products and categories are both derived from containers, they share some features, for example, the kinds of content they include, and how it is identified and displayed.

Subject to use restrictions, product and category information can be retrieved by using the `GET``Container` request. The `container` objects that the In-Game Catalog Web API retrieves are populated with information about categories and products by the Content Pipeline application. For detailed information about the `container` object and the `GET Container` operation, see the [In-Game Catalog Web API Reference](../In_Game_Catalog_WebAPI-Reference/__document_toc.html).

For more information about store catalogs, see the [PlayStation™Network Commerce Service Overview](../../../SDK/latest/PSN_Commerce_Service-Overview/__document_toc.html).

## Catalog Structure

Categories give a catalog its structure. The top-level container in a catalog encloses all the category and product content that the catalog contains. This root object is considered the root category. A title store is classified based on this *Root Category*.

Catalog Structure

Categories that are subordinate to the root category (subcategories) can contain containers of either product or category type.

# Components of an In-Game Catalog

This topic provides details on the components that make up catalog structure.

From a high-level view, an in-game catalog is a series of nested objects. As previously mentioned, the In-Game Catalog Web API provides the JSON-defined `container` object to represent these "containers".

A `container` can represent a category or a product. This topic describes components of categories and products that are basic to in-game commerce.

## Category

A category organizes the content of a title store. In addition to providing a title store with a hierarchical structure, a category represents a selection of items and their hierarchical position in a catalog.

A category includes information that identifies it and describes its content. The information that belongs to a category includes but is not limited to, a display name and an identifier called a category ID.

## Category ID

The category ID identifies a category in a catalog. The category ID is a concatenation of the service ID and a label, separated by a hyphen.

The label is an alphanumeric string limited to uppercase alphabetic characters and numbers (A-Z, 0-9). The figure below shows the category ID, consisting of a service ID and category label.

Note: Content Pipeline only uses the category label when referencing categories.

Category ID

The top-level category of a title store is identified by a *root category ID*. The root category ID is defined by the system. For example:

```
Root Category: IV0002-NPXS00004_00
```

The root category ID uses the same format as the service ID, but does not have a label. The labels of categories other than the root category ID are assigned by the content provider.

The service ID uniquely identifies a specific title such as a game or application. The service ID is composed of the service provider ID (SPID) and the NP title ID.

The service provider ID (SPID) is the first six digits of a content ID (category ID or product ID). The service provider ID uniquely identifies the application developer.

The NP title ID is provided to application developers through DevNet.

For more information about NP IDs, see [PlayStation™Network Overview - Reference Information](../../../SDK/latest/PSN-Overview/reference-information.html).

## Content

Containers that are products describe content items. A content product has attributes including *content descriptors*, *content ratings*, and *content type*.

The metadata attributes of content include but are not limited to the minimum age of the user, its search category, descriptive fields, display images, applicable restrictions and SKUs.

## Content Descriptor

A content descriptor provides information about the criteria that factors into a content rating. Depending on the content rating system, the criteria that contributes to the rating of a game could include the presence of descriptors such as "Blood and Gore", or "Intense Violence". Each of these provides a "reason" for a specific content rating.

A content descriptor is represented as an object that includes the name of the relevant criterion, the URL location of any associated image, and a description. Descriptors are contained in an array of content descriptor objects in the `contentDescriptors` field of the `container` object.

## Content Rating

A content rating represents the overall rating of the product. The content rating includes the rating and the rating system from which it is drawn. If the rating is represented by an image, the rating provides the URL location of the image.

Rating systems vary based on the region of the application. The table below lists a few of the ratings systems that are used in various countries/regions.

Rating Systems

| **Region** | **Rating System** |
| --- | --- |
| United States | ESRB |
| Japan | CERO |
| Europe | PEGI |

A content rating is represented by the `contentRating` object, a child object of the `container` object. For detailed information about the `contentRating` object, see [In-Game Catalog Web API Reference](../In_Game_Catalog_WebAPI-Reference/__document_toc.html).

## Image

Each product or category is associated with a *display image*.

An image is represented by the JSON `images` object. The `images` object is a child of the `media` object.

For detailed information about the `images` object, see [In-Game Catalog Web API Reference](../In_Game_Catalog_WebAPI-Reference/__document_toc.html).

## Label

The last segment of a category ID or a product ID is a *label*. A label is an alphanumeric string that becomes the last segment of the category or product identifier. A label uniquely identifies a category or product.

A *category label* identifies a specific category of products; a *product label* identifies a product unit.

The label is the last sixteen characters of the category ID or the product ID. For example:

**Root Category in a Store**

```
Example: IV0002-NPXS00004_00 (for the Root Category)
```

**Category label in the Category ID**

```
Example: IV0002-NPXS00004_00-CATG000011112222 (for all other categories; where "CATG000011112222" is the label)
```

**Product label in the Product ID**

```
Example: IV0002-NPXS00004_00-0000111122223333 (where "0000111122223333" is the label)
```

## Link

The link is a URL that specifies the location of the content in the PlayStation™Store.

## Product ID

A product represents digital data and services that belong to a given service ID. This could include additional data, or services with monthly charges.

The product ID is a combination of the service ID and a label, separated by a hyphen. The label is assigned by the content provider. The only characters allowed for the label are uppercase alphabetic characters and numbers (A-Z, 0-9). The figure below shows a product ID. Note that the other parts of the product ID (service ID, SPID, and NP title ID) are the same in the product ID as in the category ID shown in the previous figure.

Product ID

## SKU

A SKU is a unit of digital merchandise in a title store. A product is assigned a "default SKU" when it is created in the Content Pipeline application.

Typically, a product requires only one SKU. In the following cases, however, products can be most effectively managed through the assignment of multiple SKUs:

* For consumable items that are offered in different quantities, for example, in sets of 5, 10, or 50.
* For subscriptions that have different validity periods, for example, of one month, three months, or six months.
* For products that are offered at different prices, for example, to PlayStation®Plus members, or during a promotion.

Note:

Contact SIE when considering a product which is assigned to multiple SKUs.

In the In-Game Catalog Web API, the `skus` field of the `container` object represents SKUs and other attributes that apply to the display of product information in an in-game catalog.

For information about the use of SKUs to manage the products of the PlayStation™Store, see [PlayStation™Network Commerce Service Overview](../../../SDK/latest/PSN_Commerce_Service-Overview/__document_toc.html).

## Star Rating

A star rating is a five-star-based rating assigned to a product by its users. The `rating` object represents this five-star rating.

## Title

A title, usually a game application, is identified by its service ID. It is possible to set each title with information about the country/region where it is available, and the rating per country/region.

# Reference Materials

This topic provides links to other documents you may find useful when using the In-Game Catalog Web API.

For general information about the PlayStation™Network Web APIs:

* [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html)

For further information about the Commerce Service, NpCommerce, and NpCommerceDialog Libraries:

* [NpCommerce Library Overview](../../../SDK/latest/NpCommerce-Overview/__document_toc.html)
* [NpCommerce Library Reference](../../../SDK/latest/NpCommerce-Reference/__document_toc.html)
* [NpCommerceDialog Library Overview](../../../SDK/latest/NpCommerceDialog-Overview/__document_toc.html)
* [NpCommerceDialog Library Reference](../../../SDK/latest/NpCommerceDialog-Reference/__document_toc.html)
* [NpEntitlementAccess Library Overview](../../../SDK/latest/NpEntitlementAccess-Overview/__document_toc.html)
* [NpEntitlementAccess Library Reference](../../../SDK/latest/NpEntitlementAccess-Reference/__document_toc.html)

For information about the In-Game Catalog Web API and debugging:

* [In-Game Catalog Web API Reference](../In_Game_Catalog_WebAPI-Reference/__document_toc.html)
* [System Software Overview](../../../SDK/latest/System_Software-Overview/__document_toc.html)

For information about bugs, points to note, restrictions, and announcements, refer to the release notes below:

* [Release Notes - In-Game Catalog Web API](../../../SDK/latest/ReleaseNotes/PlayStation_Network-In_Game_Catalog_WebAPI-ReleaseNotes.html)