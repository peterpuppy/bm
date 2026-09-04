# Creating Data-Driven Experiences with UDS – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Creating_Data_Driven_Experiences_with_UDS/tournaments.html

# Data-Driven Experiences

Data-driven experiences are player-facing features such as activities, trophies, and game help that promote deeper game engagement and more fulfilling gameplay.

This continuous engagement can lead to higher play frequency, result in more playtime, and
keep the player coming back to the game over a longer period of time.

Consider the following examples:

* Activity cards that let players see their progress toward in-game goals.
* Game hints and tips that players can reference directly from the system while playing,
  which keeps them engaged with your game and playing longer.

There is a strong correlation between player usage of the data-driven experiences
on PlayStation®5 and higher per-game playtime, number of sessions, and gameplay tenure.

The following sections contain high-level overviews of the data-driven experiences
that you can provide on PlayStation®5. These overviews are meant to give you an idea
of the features and how they appear to players. Detailed information on implementing
them is available in the [UDS Workflow](uds-workflow.html "This section provides a workflow that you can follow for designing, configuring, and delivering data-driven experiences.") section. These experiences are all driven by the Universal Data System (UDS), which
is described after the experiences.

# Activities

This topic provides an overview of PlayStation™Network activities.

PlayStation™Network Activities integrate with UDS data to represent different gameplay elements and such as levels, chapters, missions, quests, and game modes. PlayStation™Network displays activities you've configured throughout the PlayStation®5 UI to inform players about what they're currently doing, what they could be doing, and what other players are doing in a specific game.

Activities encourage continued interaction and engagement with your game by enabling the following features and functionality:

* Game Help
* Playtime estimates
* Activity progress
* Game progress
* Challenge leaderboards and invites
* Tournaments

The image below shows an example of suggested activities that appear in the Game Hub.

Suggested Activities

# Tournaments

PlayStation®5 Tournaments are a special type of activity you can configure to enable a repeatable, bracket-based competition for players operated by the PlayStation®5 Tournaments service, without the need for manual administration.

Tournaments enhance the multiplayer experience by allowing players to challenge themselves
to beat a series of opponents in exchange for champion status. The PlayStation®5
Tournaments service only supports one-versus-one competitive modes.

The image below shows an example of a tournament activity card and a bracket:

Tournament Activity Card
Tournament Bracket

# Challenges

This topic provides an overview of challenges. Challenges are a special type of activity for repeatable sections of gameplay where results are sorted by time or score.

Challenges present leaderboards to enable players to compete asynchronously with friends
and other players for the best score or time. Players are informed directly through system
notifications when they have been beaten by friends even when they are outside of the game.
This type of asynchronous competition can encourage players to reinvest time in a game by
trying to get the highest score or fastest time.

The image below shows an example leaderboard.

Example of Activity Challenge Leaderboard

# Trophies

Trophies are a fundamental staple for player engagement with your game. The PlayStation™Network trophy system rewards users for completing various objectives in a game and keeps a record of these accomplishments.

The trophy collection is the system software's onscreen display of trophies earned by the
user, as well as the trophies yet to be earned. Such a system can reward the user with a
sense of accomplishment and motivate the user to continue playing.

There are two basic types of trophies: non-progressive and progressive.

* Non-progressive trophies give the player no indication of how close they are to unlocking
  a trophy. This type of trophy does not track progress towards a goal, but it can provide
  players with a sense of accomplishment upon completing a major objective. (Example:
  Complete level 1)
* Progressive trophies display each player's progress on any trophy that uses progress-based
  logic. By seeing the precise progress they've made toward unlocking a trophy, a player
  may be motivated to play further to unlock it. (Example: Win 10 races)

The image below shows an example of a progressive trophy that is displayed to a player.

Progress Tracking on Trophies

# Game Help

Game Help provides on-demand, short, spoiler-free help tips and videos to players based on their current progress within the game as defined by activities and trophies.

When players get stuck in a game, they often seek help on the Internet. Searching for help can take a significant amount of time, and the player risks encountering spoilers, such as information about the plot that spoils the surprise or suspense of the storyline for a first-time viewer.

By using the Game Help Tool, you can define tips and hints for players that they can easily access on the console during their gameplay session. This allows players to spend more of their console playtime on gameplay and minimizes their time spent looking for help. It also minimizes the player's risk of encountering spoilers, which can increase their game satisfaction.

Game Help content falls under two categories:

* Community Game Help - Content that is automatically generated for progress activities through player activity
* Custom Game Help - Custom content that you create

The image below shows an example of Game Help.

Spoiler-Free Game Help

# Spoiler Warning

Spoilers can ruin the gaming experience for players who do not wish to know details about the game that they have not yet experienced for themselves. With Spoiler Warning, you can flag Activities that contain spoilers, so that players are warned about content they have not seen yet in the game.

Players have control over the level of warnings
they would like to receive.

Avoiding Spoilers in Social Content