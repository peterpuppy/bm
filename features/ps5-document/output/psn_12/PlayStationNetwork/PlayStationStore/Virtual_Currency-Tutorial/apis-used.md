# Virtual Currency Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Virtual_Currency-Tutorial/apis-used.html

# Overview

This chapter provides an overview of the content within this tutorial, such as the APIs and services used.

This tutorial demonstrates the following aspects of virtual currency usage in a game:

* In-game store for virtual currency.

  + Creating an in-game store that sells virtual currency products.
  + Price rendering along with strike through and PlayStation®Plus discounted price.
  + Purchase of virtual currency in-game.
* Transfer of purchased virtual currency from PlayStation™Network to game server

  + User wallet tracking.

Consumption of virtual currency by the game player while in the game context is out of scope for this tutorial.

This tutorial is for Game developers who expect to sell virtual currency in their game. It is to be used in conjunction with the tutorial game code that is provided which demonstrates an end-to-end implementation of this feature. The tutorial provides you with assistance on how to implement and easily integrate this feature into your game titles.

# APIs Used

This topic provides a list and short description of the APIs used in this tutorial.

The main APIs needed to implement the various use cases for virtual currency are as follows:

## NpAuth

The NpAuth library provides methods to generate a user specific authorization code which can be provided to the PlayStation™Network game server to establish a session.

## Http2

The Http2 library provides methods to make http requests to the game server.

## Json2

The Json2 library is used to parse responses from the game server.

## NpCppWebAPI

The NpCppWebAPI library provides methods to access the In-Game Catalog Web API to retrieve catalog and product information along with pricing information from the PlayStation™Network.

## NpEntitlementAccess

The NpEntitlementAccess library provides methods to access entitlement information for the user along with supplementary methods to facilitate the request and response lifecycle with PlayStation™Network servers.

## NpCommerceDialog

The NpCommerceDialog library provides the mode `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` that launches a dialog used to complete an in-game purchase of a product, which in this tutorial's case is virtual currency.

## SystemService

The SystemService library provides methods required to handle entitlement update events triggered outside the game.