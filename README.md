# Civil War Game
A Civil War game based off of the [DOS Civil War Strategy](https://classicreload.com/civil-war-strategy.html) game

**How to play:**
1. **Start the server:** Run the `server.py` script.
2. **Connect clients:** Run the `client.py` script on two different machines or terminals.
3. **Play the game:** Players take turns entering their moves. The first player to meet a win condition wins the game.

**Technologies used:**
* Python
* PyGame
* Sockets

**Additional resources:**
* [Python Docs](https://docs.python.org/3/)
* [Pygame Docs](https://www.pygame.org/docs/)
* [Sockets](https://docs.python.org/3/howto/sockets.html)

# Proof of Concept

I made a quick mockup of the simple setup/UI of the game, with imported JSON data for cities and their locations, all in PyGame, to prove the concept of the game and show how it will be realistically developed and expanded upon. Graphical quality is not a high priority, and we settle for the minimum viable product. If in later stages development time allows, I would love to go back through and expand on the quality of life of this project.

The screenshot below shows the mockup, which was made in just an hour or so to bring the concept to life and show it off.

![Capture](/Resources/Capture.PNG)



# SOW

## Project Title
Civil War Game

## Team
Chris Pierce

## Project Objective
The goal is to recreate the DOS Civil War Strategy game with modern technology. It is a simple and fun game to play, but is limited by the original technology it was created with, and has potential for expansion.

## Scope
**Inclusions:**
* A set start state of the map
* Simultaneous turns of play
* Groups of units that can move between cities, conducting battle and capturing them
* Income based on cities controlled
* Some kind of semi-random battle outcomes
* Generals with stats
* Requirement for armies to have supply
* Navy ships including raiding and invasion abilities
* Longer-form of play than the original game
* Free assignment of generals to armies
* Ability to split and merge armies at will for both sides
* Railroad Units
* Various win conditions
* Original Keyboard and new mouse functionality for menu options
* Server-based game data management

**Exclusions:**
* Random events as done in the first game
* Random starting scenarios
* Ability to create/build forts
* Ability to move capital
* Exclusion of actions for certain sides
* AI and Difficulty Settings

## Deliverables
* Civil War Game Client 
* Civil War Game Server
* Game Documentation / Manual

## Timeline
**Key Milestones:**
* Create Full Client Prototype - Oct 11th
* Create Full Server Prototype - Nov 1st
* Finalize all TCP/Multiplayer Connections - Nov 30th

**Task Breakdown:**
* Client:
  * Finish Map (Citiy Placements, Connections, Population and Income Values) - 1 hour
  * Create working UI with functioning actions - 3 hours
  * Add Armies, with General assignments, and setup starting positions - 3 hours
  * Add Navies - 3 hours
  * Create Win Conditions and checks for them - 2 hours
  * Create some kind of info menu as existed in first game - 2 hours
  * Railroad ability and pathfinding check - 2 hours
  * (QOL) Add resolution options, as well as audio and sound effects - 2 hours
* Server:
  * Create sudo-game client to store game-data for clients - 5 hours
  * Create connection system for clients to connect to server - 6 hours
  * Run game turns, and facilitate data transfer between clients - 4 hours
  * (QOL) Create a save game system? - 8 hours

## Technical Requirements
**Hardware:**
* Hardware limitations should be pretty bare bones. Likely two devices needed. One host machine could run server and a local client and the other can be the second client/player.

**Software:**
* VSCode is being used as the programming IDE for this project
* Python 3.12.2 is being used
* Socket, Threading, and PyGame are all being used
* Everything will be coded and tested on Windows

## Assumptions
* Stable Network Connection - It will be assumed that both clients and server will have stable connections and will not drop out or be lost during gameplay.
* Synchronized Game State - It will be assumed that no client is trying to manipulate the game state, and that everything the client sends to the server is legitimate for the sake of keeping the game state syncronized
* Security - Again it will be assumed that each client is acting with good intent with the server, and thus there will be minimal security measures taken
 
## Roles and Responsibilities 
Chris: Everything :)

## Communication Plan
Its all in my head

## Additional Notes
*Thoughtfully written additional notes*



