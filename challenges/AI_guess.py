

import random 

print("\t\tfourth challenge".upper())
print("-"*55)
print("\t\tAI-chan - GUESS A NUMBER\n\n")

# TASK:
# Here’s a bigger challenge. Write the pseudocode for a program
# where the player and the computer trade places in the number
# guessing game. That is, the player picks a random number
# between 1 and 100 that the computer has to guess. Before you
# start, think about how you guess. If all goes well, try coding the
# game.


guess = random.randint(1, 100)
print("Is it", guess, "?")
answer = str(input())

while answer != "yes":

    if answer == "high":
        guess = guess + guess/2
        print("Is it", guess, "?")

    elif answer == "low":
        guess = guess - guess/2
        print("Is it", guess, "?")
    
if answer == "yes":
    print("YATTA!!! THIS IS", guess)
