# Virtual Currency Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Virtual_Currency-Tutorial/files.html

# Setting Up Your Development Environment

This chapter provides guidance on how to set up your development environment before attempting this tutorial.

This tutorial uses the SampleUtil framework as a foundation to build the tutorial application. For more information on setting up a Development environment for PlayStation®5, refer to the [Development Kit Setup Guide](../DevKit-Setup_Guide/__document_toc.html).

This tutorial assumes you are generally familiar with the development environment for PlayStation®5 and have already downloaded the latest system software and set the environment variables needed to compile the application.

# Setting Up the Game Server

This topic provides information on how to set up the game server that's included in this tutorial.

Before running the tutorial game, you will need to build and run the included game server. This game server handles all required s2s communication with the PlayStation™Network.

For setup details, see the included readme file found in `sdk\target\samples\sample_code\playstation_network\tutorial_virtual_currency\`.

The figure below shows the entire flow and interaction between the Game, Game Server, Session Cache service (provided as part of the game server demo code), Auth Service and Entitlements Service (PlayStation™Network services).

Game Server Setup

# Anatomy of the Tutorial Game

This topic provides information on the different screens that are available in the tutorial game application.

## Screens

The tutorial game has the following screens.

**Main Menu:** This is the first screen displayed on launching the tutorial game and provides the entry point into the virtual currency in-game store.

Main Menu

**Store:** This screen displays the in-game store that displays product information for virtual currency sold in the game. It also provides information on the user wallet that holds information on the count of virtual currency the user has purchased from the PlayStation™Network.

Store

# Tutorial Application Files

This topic provides information on the files used within the tutorial game application.

The following are the main files of the application along with a brief description of what each file does.

## Virtual Currency Logic Files

* **main.cpp** This file takes care of all the initialization logic of the main modules used by the tutorial application. It also contains logic for screen registration and rendering of the first screen.
* **player\_wallet.cpp** This file includes logic for the sub-thread job item that maintains state of the count of virtual currency that the user has purchased.
* **screen\_store.cpp** This file contains all the logic to create the in-game store along with displaying the catalog, product and player wallet information and invoking the commerce dialog in the checkout mode for making a purchase.
* **screen\_menu.cpp** This file provides the entry point into the in-game store.
* **store\_catalog.cpp** This file includes logic for the sub thread job item that is used to get the catalog and product data needed for the in-game store.
* **store\_product.cpp** This file includes logic for displaying the product information and price including the logic for rendering an image and adhering to the pricing rules of the PlayStation™Network including strike through pricing.

## UI Files

In addition to the above primary files, the project also contains some UI specific files: ui\_button.cpp, ui\_panel.cpp, ui\_cursor.cpp, ui\_screen.cpp, ui\_label.cpp, and ui\_image.cpp.

These files contain layout code for the screens for the tutorial game and do not demonstrate any virtual currency use cases. Details of these files are not discussed in this tutorial, but you can always view the details in the source code.