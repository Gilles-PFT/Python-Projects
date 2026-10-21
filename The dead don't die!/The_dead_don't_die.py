# A command line RPG game

# Character sheet
Player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "attack": 10,
    "defense": 5,
    "gold": 0,
    "inventory": [],
    "current_floor": 1,
    "current_room": 1,
    "cleared_rooms": 0
}
def Location(Player = Player):
    """Displays players current location"""
    floor = Player['current_floor']
    room = Player['current_room']
    print(f"Floor level: Floor{floor}, Room{room}\n")

def Player_stats(Player = Player):
    """Prints player's status, inventory and location"""
    print(f"\nName: {Player['name']}")
    print(f"Health: {Player['health']}/{Player['max_health']}")
    print(f"Attack: {Player['attack']}")
    print(f"Defense: {Player['defense']}")
    print(f"Gold: {Player['gold']}")

    # Adding seperator in inventory display
    print(f"Inventory: {', '.join(Player['inventory']) if Player['inventory'] else 'Empty'}")

    # Printing floor and room level
    Location()

def Generate_room():
    """Generates a random room with a chance of encountering an enemy or finding treasure or a merchant."""
    import random
    monster_room, treasure_room, merchant_room, empty_room = 55, 25, 10, 10    # room encounter chances
    random_room = random.randint(0, 100)
    if random_room <= monster_room:
        print("You encountered a monster!")
        room_type = "monster"
    elif random_room <= monster_room + treasure_room + merchant_room:
        print("You found a treasure chest!")
        room_type = "treasure"
    elif random_room <= monster_room + treasure_room + merchant_room + empty_room:
        print("You found a merchant!")
        room_type = "merchant"
    else:
        print("The room is empty.")
        room_type = "empty"

def Movement(Player = Player):
    """Handles player's moving sequence"""
    print("\nGo to previous floor(previous), next floor(next), or explore current floor(explore)?")
    choice = input("Enter your choice: ").lower()
    if choice == "previous":
        if Player["current_room"] == 1:
            Player["current_room"] -= 1
            print(f"You moved to room {Player['current_room']}.\n")
        else:
            print("You are already in the first room.\n")
    elif choice == "next":
        Player["current_room"] += 1
        print(f"You moved to room {Player['current_room']}.\n")
        if Player["current_room"] == 3:
            Player["current_floor"] += 1
            print(f"You moved to floor {Player['current_floor']}")
    elif choice == "explore":
        print(f"Your exploring floor {Player['current_floor']}.\n")
        Generate_room()
    else:
        print("Invalid choice. Please try again.")


# Main game loop
def main():
    print("===== Welcome to the Dead Don't Die! =====")
    Player["name"] = input("Enter your character's name: ").capitalize()
    print(f"\nWelcome {Player['name']}!\n")
    
    while True:
        print("1. Move")
        print("2. Check Status")
        print("3. Exit Game")
        
        choice = input("Select action to perform (1-3): ")
        
        if choice == "1":
            Movement()
        elif choice == "2":
            Player_stats()
            continue
        elif choice == "3":
            print("===== Thanks for playing! Goodbye! =====")
            break
        else:
            print("Invalid choice. Please try again.")

# Game launch
main()