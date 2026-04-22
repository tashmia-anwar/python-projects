# Dice Rolling Game

## What This Does
A simple command-line dice rolling game built in Python.

1. Asks the user how many dice they would like to roll
2. Rolls that number of dice each round, displaying the results
3. Keeps track of the round number
4. Accepts y to roll again or n to quit
5. Handles invalid input

## How To Run
```bash
python3 dice_rolling_game.py
```

## Example Output
```
How many dice would you like to roll? 3
Roll the dice? (y/n): y
Round 1: [5, 2, 3]
Roll the dice? (y/n): a
That is not a valid input. Please try again.
Roll the dice? (y/n): y
Round 2: [1, 5, 3]
Roll the dice? (y/n): y
Round 3: [4, 6, 2]
Roll the dice? (y/n): n
Thank you for playing!
```

## What I Learned
- Using Python's random module
- Functions and scope
- Loops and conditionals
- Lists and iteration
- User input handling and validation

## Next Steps
This project is the foundation for a larger learning arc. The plan is to wrap this logic in a Flask API, containerize it with Docker, and eventually deploy it to Kubernetes using Terraform. More on that in a separate repo.