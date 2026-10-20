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
    print("You have selected Easy level. Try win the 100 points!")
    random_number = random.randint(1, 20)
    max_range = 20
    number_of_guesses = 10  # Setting number guesses per level
    max_score = 100    # Setting maximum score for each level
elif level == 2:
    print("You have selected Medium level. Try win the 500 points!")
    random_number = random.randint(1, 100)
    max_range = 100
    number_of_guesses = 7
    max_score = 500
elif level == 3:
    print("You have selected Hard level. Try win the 1000 points!")
    random_number = random.randint(1, 500)
    max_range = 500
    number_of_guesses = 5
    max_score = 1000

#initialize guess and count variables
guess = None
count = 0
score = 0  # Initialize score based on number of guesses
Round = 1  # Initialize round variable
score_tracker = []  # Initialize score tracker list to keep track of scores for each round

# User input for guessing and feedback loop
while guess != random_number:
    # Error handling for invalid input
    try:
        guess = int(input("Guess my number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    count += 1
    score = max_score-(count * 10)  # Decrease score based on number of guesses

    if guess < 1 or guess > max_range:
        print(f"Please enter a number between 1 and {max_range}.")

    # Check if the user has run out of guesses
    elif count >= number_of_guesses:
            print("Sorry, run out of guesses. The number was:", random_number)
            print(f"Your final score is 0.")
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
        print(f"Your final score is: {score}")
        score_tracker.append(score)  # Add score to tracker
        print(f"You have completed round {Round}.")

        # Play again option
        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again == "yes":
            Round += 1
            count = 0
            score = 0
            # Reset the random number based on the selected level
            if level == 1:
                random_number = random.randint(1, 20)
            elif level == 2:
                random_number = random.randint(1, 100)
            elif level == 3:
                random_number = random.randint(1, 500)

            score_tracker.append(score)  # Add score to tracker
        else:
            print("Thank you for playing the Guessing Game!")
            # Display the highest score from the score tracker
            for scores in enumerate(score_tracker):
                max_score = score_tracker[0]
                if scores[1] > max_score:
                    max_score = scores[1]
            print(f"Your highest score was: {max_score}")
            break
    
