# The Guessing Game
import random

def play_again():
    """Ask whether the user wants another round."""
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response in ("yes", "no"):
            return response == "yes"
        print("Please enter yes or no.")

print("Welcome to the Guessing Game!")
print("Choose your level!")
print("1. Easy (1-20)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

# User input for level selection
level = int(input("Enter the level number (1, 2, or 3): "))

# Setting the random number based on the selected level
if level == 1:
    print("You have selected Easy level. Try win the 100 points!")
    max_range = 20
    number_of_guesses = 10  # Setting number guesses per level
    max_score = 100    # Setting maximum score for each level
elif level == 2:
    print("You have selected Medium level. Try win the 500 points!")
    max_range = 100
    number_of_guesses = 7
    max_score = 500
elif level == 3:
    print("You have selected Hard level. Try win the 1000 points!")
    max_range = 500
    number_of_guesses = 5
    max_score = 1000

score_tracker = []  # Initialize score tracker list to keep track of scores for each round

while True:
    # Start a fresh round at the selected difficulty.
    if level == 1:
        random_number = random.randint(1, 20)
    elif level == 2:
        random_number = random.randint(1, 100)
    else:
        random_number = random.randint(1, 500)

    # Initialize count and score
    count = 0
    score = 0

    # Guessing loop for this round.
    while count < number_of_guesses:
        try:
            guess = int(input("Guess my number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        count += 1
        distance = abs(guess - random_number)    # Calculate the distance for user proximity feedback
        if distance <= 5:
            print("You are boiling hot!")
        elif distance <= 10:
            print("You are hot!")
        else:
            print("You are cold!")

        if guess < 1 or guess > max_range:
            print(f"Please enter a number between 1 and {max_range}.")
        elif guess == random_number:
            score = max_score - (count * 10)
            print("Congratulations! You guessed the number!")
            print(f"You had it in {count} guesses.")
            print(f"Your final score is: {score}")
            break
        elif count == number_of_guesses:
            print("Sorry, run out of guesses. The number was:", random_number)
            print("Your final score is 0.")
        elif guess < random_number:
            print("Your guess is too low.")
            print(f"You have {number_of_guesses - count} guesses left.")
        else:
            print("Your guess is too high.")
            print(f"You have {number_of_guesses - count} guesses left.")

    score_tracker.append(score)
    if not play_again():
        print("Thank you for playing the Guessing Game!")
        print(f"Your highest score was: {max(score_tracker)}")
        break
