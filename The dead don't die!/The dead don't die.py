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
    "floor_level": 1
}

def player_status(Player = Player):
    print(f"Name: {Player['name']}")
    print(f"Health: {Player['health']}/{Player['max_health']}")
    print(f"Attack: {Player['attack']}")
    print(f"Defense: {Player['defense']}")
    print(f"Gold: {Player['gold']}")
    # Adding seperator in inventory display
    print(f"Inventory: {', '.join(Player['inventory']) if Player['inventory'] else 'Empty'}")
    print(f"Floor Level: {Player['floor_level']}")

def movement():
    print("Go to previous floor(previous), next floor(next), or explore current floor(explore)?")
    choice = input("Enter your choice: ").lower()
    if choice == "previous":
        if Player["floor_level"] > 1:
            Player["floor_level"] -= 1
            print(f"You moved to floor {Player['floor_level']}.")
        else:
            print("You are already on the first floor.")
    elif choice == "next":
        Player["floor_level"] += 1
        print(f"You moved to floor {Player['floor_level']}.")
    elif choice == "explore":
        print(f"Your exploring floor {Player['floor_level']}.")

        # Placeholder for exploration logic
        def generate_room():
            """Generates a random room with a chance of encountering an enemy or finding treasure or a merchant."""
            import random
            monster_room, treasure_room, merchant_room = 60, 25, 15    # room encounter chances
            random_room = random.randint(0, 100)
            if random_room <= monster_room:
                print("You encountered a monster!")
                room_type = "monster"
            elif random_room <= monster_room + treasure_room:
                print("You found a treasure chest!")
                room_type = "treasure"
            elif random_room <= monster_room + treasure_room + merchant_room:
                print("You found a merchant!")
                room_type = "merchant"
            else:
                print("The room is empty.")
                room_type = "empty"
    else:
        print("Invalid choice. Please try again.")


# Main game loop
def main():
    print("Welcome to the Dead Don't Die!")
    Player["name"] = input("Enter your character's name: ")
    
    while True:
        print("\n--- Player Status ---")
        player_status()
        print("\nWhat would you like to do?")
        print("1. Move")
        print("2. Check Status")
        print("3. Exit Game")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            movement()
        elif choice == "2":
            player_status()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")