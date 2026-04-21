import random

# Rolls two dice and displays the result
def game():
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")

# Plays the game if user says 'y', terminates the game if user says 'n', and returns error message for any other input
while True:
    answer = input("Roll the dice? (y/n): ").lower()
    if answer == "y":
        game()
    elif answer == "n":
        print("Thank you for playing!")
        break
    else:
        print("That is not a valid input. Please try again.")