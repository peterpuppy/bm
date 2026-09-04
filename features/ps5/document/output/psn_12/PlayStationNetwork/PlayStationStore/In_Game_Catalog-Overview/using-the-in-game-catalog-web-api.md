# In-Game Catalog Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/In_Game_Catalog-Overview/using-the-in-game-catalog-web-api.html

# Using the In-Game Catalog Web API

This chapter provides information on how to use the In-Game Catalog Web API.

## Prerequisites

Obtain the access token and base URL for accessing the PlayStation™Network Web APIs. For more information, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

For information about obtaining the permissions that are required to use the In-Game Catalog Web API, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

## Commerce Base URL

The base URL of the In-Game Catalog Web API is `CommerceBaseUrl`. To learn how to obtain and use `CommerceBaseUrl`, see [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html).

## Required Headers

For requests from an application server or website:

```
Authorization: Bearer AccessToken
```

Specify an access token obtained as described in the [PlayStation™Network Web APIs Overview - Usage - Obtaining Access Tokens](../../../SDK/latest/PSN_WebAPI-Overview/obtaining-access-tokens.html).

Specify a list of language codes.

```
Accept-Language: A comma-separated list of language codes
```

## In-Game Commerce Debug Headers

If the In-Game Catalog Web API is called from the application server rather than the PlayStation®5 application, In-Game Commerce debug settings do not work.

Instead, use the In-Game Commerce Debug header `X-Psn-Trc-Check-IGC` to test various conditions and cases relating to TRC.

```
X-Psn-Trc-Check-IGC: TRC Check Setting
```

For more information on the In-Game Commerce debug feature, see [PlayStation™Network Commerce Programming Guide - Development Support Functions - PlayStation™Network - In-Game Commerce Debug](../../../SDK/latest/PSN_Commerce-Programming_Guide/psn-in-game-commerce-debug.html).

For a full list of `X-Psn-Trc-Check-IGC` options, see [In-Game Catalog Web API Reference - Containers - getContainer](../In_Game_Catalog_WebAPI-Reference/0002.html).

## Status Codes

The In-Game Catalog Web API returns a set of standard HTTP status codes with descriptions. Use these status codes and messages to debug your application; do not display them to users.

The application is responsible for handling errors without interruption to processing.

For detailed information about the status codes that are most commonly returned, see [In-Game Catalog Web API Reference](../In_Game_Catalog_WebAPI-Reference/__document_toc.html).

# Retrieving a Root Container

This topic provides information on how to retrieve an In-Game Catalog's root container.

The following example shows the request and response for a root container identified by the NP service label 0.

## Request

```
GET  CommerceBaseUrl/v5/container?serviceLabel=0
```

## Response

```
[
   {
      "id": "IV0002-NPXS45006_00",
      "label": "",
      "ageLimit": 0,
      "displayName": "TITLEID_SIE_NP_COMMERCE_SAMPLE",
      "type": "category",
      "children": [
         {
            "id": "IV0002-NPXS45006_00-PSALCATEGORY",
            "label": "PSALCATEGORY",
            "ageLimit": 0,
            "displayName": "PSAL Category",
            "publisher": {},
            "type": "category",
            "skus": []
         },
         {
            "id": "IV0002-NPXS45006_00-PSVCCATEGORY",
            "label": "PSVCCATEGORY",
            "type": "category",
            "skus": []
         },
         {
            "id": "IV0002-NPXS45006_00-PSCONSCATEGORY",
            "label": "PSCONSCATEGORY",
            "ageLimit": 0,
            "type": "category",
            "skus": []
         }
      ],
      "totalItemCount": 3
    }
]
```

# Retrieving Multiple In-Game Catalog Containers

This topic provides information on how to retrieve multiple In-Game Catalog containers.

The following example shows a request and response for containers identified by the containerID labels `PSALCATEGORY` and `PSVCCATEGORY`. ContainerID labels can point to either category or product labels.

## Request with Category List

```
GET CommerceBaseUrl/v5/container?serviceLabel=0&containerIds=PSALCATEGORY:PSVCCATEGORY
```

## Response

```
[
   {
      "id": "IV0002-NPXS45006_00-PSALCATEGORY",
      "label": "PSALCATEGORY",
      "ageLimit": 0,
      "displayName": "PSAL Category",
      "type": "category",
      "children": [
         {
            "id": "IV0002-NPXS45006_00-PSAL000000000002",
            "label": "PSAL000000000002",
            "contentType": "GAME",
            "type": "product",
            "skus": [
               {
                  "id": "IV0002-NPXS45006_00-PSAL000000000002-U001",
                  "label": "U001",
                  "type": "standard",
                  "price": 100,
                  "displayPrice": "1.00USD",
                  "useLimit": 0,
                  "annotationName": "NONE"
               },
                  ...
            ]
         }
      ],
         "totalItemCount": 1
      },
      {
         "id": "IV0002-NPXS45006_00-PSVCCATEGORY",
         "label": "PSVCCATEGORY",
         "ageLimit": 0,
         "displayName": "PSVC Category",
         "type": "category",
         "children": [
            {
               "id": "IV0002-NPXS45006_00-PSVC000000000001",
               "label": "PSVC000000000001",
               "ageLimit": 0,
               "displayName": "PSVC Test Product #1",
               "contentType": "GAME",
               "publisher": {
                  "name": "SIE: for public sample"
            },
            "type": "product",
            "skus": [
               {
                  "id": "IV0002-NPXS45006_00-PSVC000000000001-U001",
                  "label": "U001",
                  "type": "standard",
                  "price": 0,
                  "displayPrice": "0.00USD",
                  "useLimit": 1,
                  "annotationName": "NONE"
               }
            ]
         },
              ...
       ],
       "totalItemCount": 2
    }
]
```