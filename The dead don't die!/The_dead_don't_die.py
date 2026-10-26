# A command line RPG game

import random

# Character sheet
Player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "attack": 10,
    "defense": 5,
    "cash": 0,
    "inventory": {
        "garri": 1,
        "water bottle": 2,
    },
    "equipment": {},
    "current_floor": 1,
    "current_room": 1,
    "cleared_rooms": 0
}
def location(player):
    """Displays players current location"""
    floor = Player['current_floor']
    room = Player['current_room']
    return f"Floor level: Floor{floor}, Room{room}\n"

def player_stats(player):
    """Prints player's status, inventory and location"""
    print(f"\nName: {Player['name']}")
    print(f"Health: {Player['health']}/{Player['max_health']}")
    print(f"Attack: {Player['attack']}")
    print(f"Defense: {Player['defense']}")
    print(f"Cash: {Player['cash']} CFA")

    # Adding seperator in inventory display
    print(f"Inventory: {', '.join([f'{item}: {qty}' for item, qty in Player['inventory'].items()]) if Player['inventory'] else 'Empty'}")

    # Adding seperator in equipment display
    print(f"Equipment: {', '.join([f'{item}: {details['attack']}' for item, details in Player['equipment'].items()]) if Player['equipment'] else 'None'}")

    # Printing floor and room level
    print(location(Player))

def generate_room():
    """Generates a random room with a chance of encountering an enemy or finding treasure or a merchant."""
    monster_room, treasure_room, merchant_room, empty_room = 55, 25, 10, 10    # room encounter chances
    random_room = random.randint(0, 100)
    if random_room <= monster_room:
        room_type = "monster"
    elif random_room <= monster_room + treasure_room:
        room_type = "treasure"
    elif random_room <= monster_room + treasure_room + merchant_room:
        room_type = "merchant"
    else:
        room_type = "empty"
    return room_type

def generate_monster(player):
    """Generates a random monster"""
    # Zombie database categorized by difficulty / floor tier
    MONSTER_POOL = {
        "tier_1": [
            # Canon fodder & agile basic enemies
            {"name": "Walker", "hp": 25, "attack": 6, "defense": 1, "xp": 10},
            {"name": "Crawler", "hp": 15, "attack": 4, "defense": 0, "xp": 8},
            {"name": "Runner", "hp": 20, "attack": 9, "defense": 1, "xp": 12},
        ],
        "tier_2": [
            # Disruptors, ranged threats, and stealth units
            {"name": "Stalker", "hp": 35, "attack": 12, "defense": 2, "xp": 20},
            {"name": "Spitter", "hp": 30, "attack": 15, "defense": 1, "xp": 22},
            {"name": "Screamer", "hp": 25, "attack": 5, "defense": 1, "xp": 18},
            {"name": "Grabber", "hp": 40, "attack": 10, "defense": 3, "xp": 25},
            {"name": "Fogger", "hp": 45, "attack": 8, "defense": 2, "xp": 24},
        ],
        "tier_3": [
            # Heavy tanks, hazardous units, and armored foes
            {"name": "Armored Zombie", "hp": 70, "attack": 14, "defense": 6, "xp": 40},
            {"name": "Bloater", "hp": 50, "attack": 18, "defense": 2, "xp": 35},
            {"name": "Brute", "hp": 90, "attack": 16, "defense": 5, "xp": 50},
        ],
        "boss": [
            # Major threats for boss floors
            {"name": "The Alpha Abomination", "hp": 200, "attack": 25, "defense": 8, "xp": 150}
        ]
    }
    # Determine the tier based on the player's current floor
    if Player["current_floor"] <= 2:
        tier = "tier_1"
    elif Player["current_floor"] <= 4:
        tier = "tier_2"
    else:
        tier = "tier_3"

    # Spawn boss on every 3rd floor
    if Player["current_floor"] % 3 == 0:
        tier = "boss"

    # Randomly select a monster from the appropriate tier and make a copy of it to avoid modifying the original monster data
    monster = random.choice(MONSTER_POOL[tier])
    monster = monster.copy()
    return monster

def battle(player, monster):
    """Handles the battle sequence between player and monster"""
    print(f"You encounter a {monster['name']}!")
    while player["health"] > 0 and monster["hp"] > 0:
        print(f"\nYour Health: {player['health']}")
        print(f"{monster['name']} Health: {monster['hp']}")

        action = input("Choose your action: [A]ttack or [R]un: ").lower()
        if action == "a":
            # Player attacks
            damage_to_monster = max(1, player["attack"] - monster["defense"])
            monster["hp"] -= damage_to_monster
            print(f"You dealt {damage_to_monster} damage to {monster['name']}!")

            if monster["hp"] <= 0:
                print(f"You defeated the {monster['name']}!")
                player["cash"] += monster["xp"] * 10  # Reward cash based on XP
                break

            # Monster attacks
            damage_to_player = max(1, monster["attack"] - player["defense"])
            player["health"] -= damage_to_player
            print(f"{monster['name']} dealt {damage_to_player} damage to you!")

            if player["health"] <= 0:
                print("\nYou have been defeated!")
                return "Game Over."
            

        elif action == "r":
            if random.random() < 0.50:
                print("You ran away safely!")
                break
            else:
                print("\nYour escape attempt failed! The monster attacks you!")
        else:
            print("\nInvalid action. Please choose again.")
            continue

    return "Victory"

def merchant_interaction(player):
    """Handles the interaction with the merchant"""
    while True:
        print("\nMerchant's Inventory:")
        print("1. garri (100 CFA)")
        print("2. water bottle (250 CFA)")
        print("3. body armor (2500 CFA)")
        print("4. knuckle (5000 CFA)")
        print("5. Exit Merchant")

        choice = input("Select an item to buy (1-5): ")
        if choice == "1":
            if Player["cash"] >= 100:
                Player["cash"] -= 100
                Player["inventory"]["garri"] = Player["inventory"].get("garri", 0) + 1
                print("You bought garri!")
            
            else:
                print("You don't have enough cash!")
        elif choice == "2":
            if Player["cash"] >= 250:
                Player["cash"] -= 250
                Player["inventory"]["water bottle"] = Player["inventory"].get("water bottle", 0) + 1
                print("You bought a water bottle!")
            else:
                print("You don't have enough cash!")
        elif choice == "3":
            if Player["cash"] >= 2500:
                Player["cash"] -= 2500
                Player["inventory"]["body armor"] = Player["inventory"].get("body armor", 0) + 1
                print("You bought body armor!")
            else:
                print("You don't have enough cash!")
        elif choice == "4":
            if Player["cash"] >= 5000:
                Player["cash"] -= 5000
                Player["inventory"]["knuckle"] = Player["inventory"].get("knuckle", 0) + 1
                print("You bought a knuckle!")
            else:
                print("You don't have enough cash!")
        elif choice == "5":
            print("You leave the merchant.")
            break
        else:
            print("Invalid choice. Please select again.")

def room_event_handling(room_type, player):
    """Acts as the game event controller managing event based on generated room"""
    print(f"Event triggered: you encountered a/an {room_type} room")
    # Handle the event based on the room type
    if room_type == "monster":
        print("... A zombie comes out to you !")
        monster = generate_monster(player)
        # Enter the battle sequence
        battle_result = battle(player, monster)
        if battle_result == "Game Over.":
            print("===== Game Over! You have been defeated! =====")
            exit()

    elif room_type == "treasure":
        print("... An open safe box grabs your attention !")
        weapon = random.choice([{"name": "Knife", "attack": 5}, {"name": "Baseball Bat", "attack": 8}, {"name": "Axe", "attack": 6}])
        reward = random.choice(["cash", "garri", weapon])
        if reward == "cash":
            Player["cash"] += 5000
            print("You found 5000 CFA!")
        elif reward == "garri":
            Player["health"] += 10
            if Player["health"] > Player["max_health"]:
                Player["health"] = Player["max_health"]
            print("You found some garri and restored your health!")
        else:
            Player["equipment"][weapon["name"]] = weapon # Add the weapon to the player's equipment
            Player["attack"] += weapon["attack"]
            print(f"You found {weapon['name']} and increased your attack!")
            
    elif room_type == "merchant":
        print("... A hiding bayam-sellam makes you a sign !")
        merchant_interaction(Player)
    else:
        print("... The room is scarely silent. But nothing happens !")

def use_inventory(player):
    """Handles the player's inventory usage"""
    if not player["inventory"]:
        print("Your inventory is empty.")
        return

    print("\nYour Inventory:")
    for index, (item, quantity) in enumerate(player["inventory"].items(), start=1):
        print(f"{index}. {item} (Quantity: {quantity})")

    choice = input("Enter the number of the item you want to use (or 'q' to cancel): ")
    if choice.lower() == 'q':
        return

    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(player["inventory"]):
            item_name = list(player["inventory"].keys())[choice_index]
            if item_name == "garri":
                player["health"] += 10
                if player["health"] > player["max_health"]:
                    player["health"] = player["max_health"]
                print("You used garri and restored your health!")
            elif item_name == "water bottle":
                player["health"] += 15
                if player["health"] > player["max_health"]:
                    player["health"] = player["max_health"]
                print("You drank water and restored some health!")
            else:
                print(f"You used {item_name}, but nothing happened.")

            # Decrease the quantity of the used item
            player["inventory"][item_name] -= 1
            if player["inventory"][item_name] <= 0:
                del player["inventory"][item_name]
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
def movement(player):
    """Handles player's moving sequence"""
    print("\nGo to previous or next room? [p/n]")
    choice = input("Enter your choice: ").lower()
    # Handle the movement based on the player's choice
    if choice == "p":
        if Player["current_room"] == 1:
            print("Your already in the first room.")
        else:
            Player["current_room"] -= 1
            print(f"\nYou moved to room {Player['current_room']}.")
    elif choice == "n":
        Player["current_room"] += 1
        Player["cleared_rooms"] += 1
        print(f"\nYou moved to room {Player['current_room']}.")
        # Rolling the room
        room_type = generate_room()

        # Handle the event
        room_event_handling(room_type, Player)
    else:
        print("Invalid choice. Please try again.")

    # Check if the player has cleared 5 rooms to move to the next floor
    if Player["cleared_rooms"] == 5:
        Player["current_floor"] += 1
        Player["current_room"] = 1
        Player["cleared_rooms"] = 0
        print(f"\n===== Welcome to floor {Player['current_floor']} =====\n")

    elif Player["current_floor"] == 6 and Player["cleared_rooms"] == 4:
        print("\n===== You found your junior brother! =====")
        print("You have successfully completed the game!")
        break

# Main game loop
def main():
    print("===== Welcome to the Dead Don't Die! =====")
    Player["name"] = input("Enter your character's name: ").capitalize()
    print(f"\nWelcome {Player['name']}!\n")
    
    while Player["health"] > 0:
        print("1. Move")
        print("2. Check Status")
        print("3. Use Item")
        print("4. Exit Game")
        
        choice = input("Select action to perform (1-4): ")
        
        if choice == "1":
            movement(Player)
        elif choice == "2":
            player_stats(Player)
            continue
        elif choice == "3":
            use_inventory(Player)
        elif choice == "4":
            print("===== Thanks for playing! Goodbye! =====")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Game launch
main()