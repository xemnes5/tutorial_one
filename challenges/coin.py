

import random 

print("\t\tsecond challenge".upper())
print("-"*55)
print("\t\tCOIN FLIP\n\n")

# TASK:
# Write a program that flips a coin 100 times and then tells you
# the number of heads and tails.


counter = 0 
heads = 0
tails = 0

while counter < 100:
    flip = random.randrange(2)

    if flip == 0:
        heads += 1
    else: tails +=1

    counter += 1

print("HEADS: ", heads)
print("TAILS: ", tails)

print("===================")



