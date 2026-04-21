import random

# User decides how many dice to play with
num = int(input("How many dice would you like to roll? "))

# Keeps track of the number of rounds played
i = 0

'''
# Rolls two dice by default and displays the result
def game():
        global i
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        i += 1
        print(f"Round {i}: ({die1}, {die2})")
'''

# Rolls the dice and displays the result
def game():
    global i
    rolls = []
    for j in range(num):
        die = random.randint(1,6)
        rolls.append(die)
    i += 1
    print(f"Round {i}: {rolls}")
    
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