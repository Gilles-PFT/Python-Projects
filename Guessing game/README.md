# The Guessing Game

A command-line number guessing game written in Python featuring three difficulty levels, proximity feedback ("hot/cold" hints), and high-score tracking across multiple rounds.

## Features

* **Three Difficulty Levels:**
  * **Easy:** Guess a number between `1` and `20` (10 guesses max, up to 100 points)
  * **Medium:** Guess a number between `1` and `100` (7 guesses max, up to 500 points)
  * **Hard:** Guess a number between `1` and `500` (5 guesses max, up to 1000 points)
* **Smart Proximity Hints:** Uses distance calculations to tell you if you are *boiling hot* (within 5), *hot* (within 10), or *cold*, alongside standard *too high / too low* guidance.
* **Dynamic Scoring System:** Your final score is calculated based on your chosen difficulty minus a 10-point penalty for each guess taken.
* **Input Validation:** Handles non-numeric inputs gracefully without crashing and warns when guesses fall outside the valid range.
* **Multi-Round High Score Tracker:** Tracks your scores across consecutive rounds and displays your highest score when you exit.

## Prerequisites

* Python 3.12+ (No external libraries required—uses only Python's built-in `random` module).

## How to Run

1. Clone or download this repository to your local machine.
```bash
git clone [https://github.com/Gilles-PFT/Python-Projects.git](https://github.com/Gilles-PFT/Python-Projects.git)
```

2. Open your terminal and navigate to the project directory.
```bash
cd Python-Projects/Guessing game
```

3. Run the script:
```bash
python The_Guessing_game.py
```
## How to play

1. Run the program and enter 1, 2, or 3 to select your difficulty level.

2. Enter your guesses one by one.

3. Use the proximity and high/low hints to narrow down the secret number before running out of attempts.

4. Type yes or no at the end of a round to play again or view your session's highest score.
