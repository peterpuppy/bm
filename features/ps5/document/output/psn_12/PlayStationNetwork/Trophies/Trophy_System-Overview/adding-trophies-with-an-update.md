# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/adding-trophies-with-an-update.html

# Trophy Set Configuration

This topic describes the set of trophies prepared for a single title, as well as the multilingual support for each trophy's attributes and text information.

# Trophy Sets

A trophy set is a group of trophies provided in a title.

A trophy set is identified by its NP Title ID and NP service label and does not necessarily correspond to a single title. When games are distributed in multiple territories, the version released in each territory is considered to be a separate title with its own NP Title ID, but it is recommended that you have these titles share the same trophy set worldwide. A still-image icon and name can be configured for a trophy set.

## Multi-lingual Support

The trophy system supports multiple languages. The text information included in a trophy set - the trophy set name, trophy names, and details - can be set in the languages that have been selected. Any set of languages among the available languages can be selected. However, please make sure to use a common language set worldwide. Even when a single title is being launched in multiple license territories, do not change the language set by territory. It is possible to add a language to the language set by upgrading the trophy set.

# Trophy Attributes

Each trophy has the following attributes:

* Trophy ID: The ID that identifies the trophy within the trophy set
* Name/details: The name and description of the trophy. This attribute has multi-lingual support.
* Grade: Bronze, silver, gold, or platinum. For details, refer to the "[Grades](trophy-attributes.html#trophy-system-overview_2_2__trophy-system-overview_2_2_2)" chapter.
* Hidden flag: This flag determines whether to display the details of the trophy in the system software's trophy collection if the user has not yet earned the trophy. When set to hidden, the trophy's name, details, grade, reward information, and progress are hidden while the trophy is locked. When set to be displayed, the name of, and details about, the trophy will be displayed even while it is locked. It is not possible to set a platinum trophy as a hidden trophy.
* Platinum link: This link indicates whether or not the trophy is linked to the platinum trophy. When the trophy is "Linked", its obtainment is one of the conditions for earning the platinum trophy.
* Reward information: This is the name of any in-game rewards that are earned when the trophy is earned. This attribute has multi-lingual support. This information is displayed in the trophy collection of the system software.
* Progressive flag: This flag indicates whether the trophy is progressive. For details, refer to the "[Progressive Flag](trophy-attributes.html#trophy-system-overview_2_2__trophy-system-overview_2_2_5)" chapter.
* Target value: The target value that is used in the condition for a progressive trophy to be unlocked

## Trophy Details

Unlocking conditions for trophies are described here. You may represent these conditions in a manner that fits in with the feel of your game's world, but make sure that unlocking conditions will not be misunderstood by the game's users.

## Grades

There are four trophy grades, and points are allocated according to the grade.

* Bronze (15 points)
* Silver (30 points)
* Gold (90 points)
* Platinum

Assign bronze trophies to relatively easy missions. In particular, it is recommended that a bronze trophy be assigned to the first mission in the game.

Assign silver and gold trophies to increasingly difficult missions.

The platinum trophy is not linked to a particular mission and indicates that the user has earned all the trophies in the game. Only one platinum trophy is allowed in a normal game.

## Hidden Flag

If there is a risk that the name, details, reward information, or other items pertaining to a trophy would spoil the game's story, trophy information can be hidden by setting the hidden flag. However, it is recommended that the setting of the hidden flag be limited to as few trophies as possible.

The system software's trophy collection provides users with the ability to individually reveal hidden trophy information on the Trophy Details screen. Also, selecting "Reveal All" from the options menu of the trophy set list automatically displays information for all hidden trophies in that trophy set.

## Reward Information

It is possible to display information about in-game rewards that are earned when a trophy is earned. This information is displayed in the trophy collection of the system software. Displaying reward information helps to motivate players to unlock the trophy.

## Progressive Flag

Depending on the trophy unlocking condition, you can configure each trophy so that the progress toward earning the trophy is displayed in the trophy collection of the system software. By displaying this progress, you can make users aware of trophies they are close to unlocking, motivating them to play the game.

However, the unlocking condition for a progressive trophy must be "a given integer-type UDS Stat is equal to or larger than the target value". It is not possible to display progress toward a trophy that references a UDS Stat of a non-integer type or whose unlocking condition is "equal to the target value" or "equal to or smaller than the target value".

## Trophy Groups

In the trophy collection of the system software, trophies can be displayed in groups for each piece of additional content. A still-image icon and name can be configured for the trophy group of each piece of additional content.

## Quantity Restriction

The number of trophies that can be included in any one trophy set is limited to 1,000 trophies total for all grades. Up to 50 trophy groups can be configured including the base game group. The base game group is the trophy group of the main game and is not related to any piece of additional content.

# Adding Trophies with an Update

Trophies can be added by including a new trophy set in an update. The trophy set in an update must also include all the trophies of the main game.

When releasing the main game and additional content for a title, trophy sets can be configured using one of the following methods:

* Including a trophy set that also contains all the trophies to be used with additional content in the first master package
* Including a trophy set that only contains the trophies to be used with the main game in the first master package. Creating a new version of the trophy set with trophies to be used with additional content and including this new trophy set in the update package for distribution

Refer to the "[Upgrading the Trophy Set](upgrading-the-trophy-set.html)" section for information about updating the trophy set.