# The Guessing Game
import random

print("Welcome to the Guessing Game!")
print("Choose your level!")
print("1. Easy (1-20)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

# User input for level selection
level = int(input("Enter the level number (1, 2, or 3): "))

# Setting the random number based on the selected level
if level == 1:
    print("You have selected Easy level.")
    random_number = random.randint(1, 20)
    max_range = 20
    number_of_guesses = 10  # Setting number guesses per level
elif level == 2:
    print("You have selected Medium level.")
    random_number = random.randint(1, 100)
    max_range = 100
    number_of_guesses = 7
else:
    print("You have selected Hard level.")
    random_number = random.randint(1, 500)
    max_range = 500
    number_of_guesses = 5

#initialize guess and count variables
guess = None
count = 0

# User input for guessing and feedback loop
while guess != random_number:
    guess = int(input("Guess my number: "))
    count += 1

    if guess < 1 or guess > max_range:
        print(f"Please enter a number between 1 and {max_range}.")

    # Check if the user has run out of guesses
    elif count >= number_of_guesses:
            print("Sorry, run out of guesses. The number was:", random_number)
            break
    elif guess < random_number:
        print("Your guess is too low.")
        print(f"You have {number_of_guesses - count} guesses left.")
    elif guess > random_number:
        print("Your guess is too high.")
        print(f"You have {number_of_guesses - count} guesses left.")
    else:
        print("Congratulations! You guessed the number!")
        print(f"You had it in {count} guesses.")