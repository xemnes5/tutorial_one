

import random 

print("\t\tthird challenge".upper())
print("-"*55)
print("\t\tGUESS A NUMBER\n\n")

# TASK:
# Modify the Guess My Number game so that the player has a
# limited number of guesses. If the player fails to guess in time,
# the program should display an appropriately chastising message.


number = random.randint(1, 100)
guess = int(input("Try to guess: "))
tries = 1

while guess != number:
    if guess > number:
        print("Lower, yo")
        tries += 1
    else:
        print("Higher, epty")
        tries += 1

    if tries == 8:
        break 
    
    guess = int(input("Try to guess: "))

if guess == number:
    print("\nYOU GUESSED RIGHT! IT'S", number, "\nand you only needed", tries, "tries to do it")
else:
    print("\nZannen. You suck.")
