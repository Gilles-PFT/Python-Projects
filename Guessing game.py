# The Guessing Game
import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

random_number = random.randint(1, 20)
guess = None
count = 0

# Random number generation and user input for guessing
while guess != random_number:
    guess = int(input("Guess my number: "))
    count += 1

    if guess < random_number:
        print("Your guess is too low.")
    elif guess > random_number:
        print("Your guess is too high.")

    # Ensuring range is respected
    elif guess < 1 or guess > 20:
        print("Please guess a number between 1 and 20.")
    else:
        print("Congratulations! You guessed the number!")
        print(f"You had it in {count} guesses.")