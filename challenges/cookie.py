

import random

print("\t\tfirst challenge".upper())
print("-"*55)
print("\t\tFORTUNE COOKIE CHALLENGE\n\n")

#TASK:
#Write a program that simulates a fortune cookie. The program
#should display one of five unique fortunes, at random, each
#time it’s run

#BANALITY:

cookie = random.randint(1, 5)

if cookie == 1:
    print("GOD LUCK. YOU'RE A GOD!")
elif cookie == 2:
    print("SUNNY ONE. IT WILL BE FINE.")
elif cookie == 3:
    print("RAINY ONE. SO'LL BE WET NOW.")
elif cookie == 4:
    print("DARK ONE. YOU CAN SEE BUT IT'S FADING.")
else:
    print("DEMON LUCK. YOU'RE OUT OF OPTIONS!")







