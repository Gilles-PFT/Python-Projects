# The Dead Don't Die - Text-Based RPG
A survival horror text-based RPG where you climb a zombie-infested building in Douala to find your kidnapped junior brother.

**Play demo[https://demo-delta-rose-90.vercel.app/]**

## What is this project?

**The Dead Don't Die** is a command-line RPG built with **basic Python only** (no pygame, no external libraries). The goal is simple but tense: you start on Floor 1 and you must clear 5 rooms per floor to go up. Each room is randomly generated as a monster fight, treasure, merchant, or empty room.

I built it for my non-traditional game idea: instead of an open world, the player is forced to search every room of a building. Your brother is somewhere at the top, so you have to survive, loot, and manage your inventory.

## How I built it:
- The player is a single Python `dict` storing health, attack, defense, cash, inventory, equipment, and position (current floor/room).
- I used two dicts to separate logic: `inventory = {item: quantity}` for consumables like garri and water, and `equipment = {slot: weapon}` for weapons that give permanent ATK.
- Rooms are generated with weighted probabilities (55% monster, 25% treasure, 10% merchant, 10% empty) using `random.randint`.
- Monsters are scaled by floor tier (Tier 1 on floors 1-2, Tier 2 on floors 3-4, Tier 3 after, and a Boss on every 3rd floor).
- The whole game runs in a `while` loop in `main()` with functions for `movement()`, `battle()`, `merchant_interaction()`, and `room_event_handling()`.
  ![](Screenshots/p2.png)
  
- The game ends when the junior is found or the player is defeated
  ![](Screenshots/p7.png)
  
- The player can use inventory items and check status before any movement through out the game
  ![](Screenshots/p3.png)
  
## Why building it?
This project was a fun way for me to put alltogether what i've learned so far with python and a prove i can actually build something 
concrete with what i already konw, learn and apply new things while developing.

## How to run / play
 1. Requirements
- Python 3.7+ installed

 2. Install and Run

### Clone the repo
```bash
git clone https://github.com/Gilles-PFT/Python-Projects.git
cd The dead don't die!
```
### Run the game
The_dead_don't_die.py
