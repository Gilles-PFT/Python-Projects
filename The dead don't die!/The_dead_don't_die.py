# A command line RPG game

# Character sheet
Player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "attack": 10,
    "defense": 5,
    "cash": 0,
    "inventory": [],
    "current_floor": 1,
    "current_room": 1,
    "cleared_rooms": 0
}
def location(player):
    """Displays players current location"""
    floor = Player['current_floor']
    room = Player['current_room']
    print(f"Floor level: Floor{floor}, Room{room}\n")

def player_stats(player):
    """Prints player's status, inventory and location"""
    print(f"\nName: {Player['name']}")
    print(f"Health: {Player['health']}/{Player['max_health']}")
    print(f"Attack: {Player['attack']}")
    print(f"Defense: {Player['defense']}")
    print(f"Cash: {Player['cash']} CFA")

    # Adding seperator in inventory display
    print(f"Inventory: {', '.join(Player['inventory']) if Player['inventory'] else 'Empty'}")

    # Printing floor and room level
    location(Player)

def generate_room():
    """Generates a random room with a chance of encountering an enemy or finding treasure or a merchant."""
    import random
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
    

def room_event_handling(room_type, player):
    """Acts as the game event controller managing event based on generated room"""
    print(f"Event triggered: you encountered a/an {room_type} room")
    if room_type == "monster":
        print("... A zombie comes out to you !")

    elif room_type == "treasure":
        print("... A full wallet grabs your attention !")
        Player["cash"] += 5000

    elif room_type == "merchant":
        print("... A hiding bayam-sellam makes you a sign !")

    else:
        print("... The room is scarely silent. But nothing happens !")

def movement(player):
    """Handles player's moving sequence"""
    print("\nGo to previous or next room? [p/n]")
    choice = input("Enter your choice: ").lower()
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

    if Player["cleared_rooms"] == 3:
        Player["current_floor"] += 1
        Player["current_room"] = 1
        Player["cleared_rooms"] = 0
        print(f"\n===== Welcome to floor {Player['current_floor']} =====\n")


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
            movement(Player)
        elif choice == "2":
            player_stats(Player)
            continue
        elif choice == "3":
            print("===== Thanks for playing! Goodbye! =====")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Game launch
main()