

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
tries = 1

while tries < 5:
    if answer == "high":
        guess = guess + guess/2
        tries += 1
        print("Is it", guess, "?")
        answer = input()

    elif answer == "low":
        guess = guess - guess/2
        tries += 1
        print("Is it", guess, "?")
        answer = input() 
if answer == "yes":
    print("YATTA!!! THIS IS", guess)
