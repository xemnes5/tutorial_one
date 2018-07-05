

import random

print("\t\tfirst challenge".upper())
print("-"*55)
print("\t\tFORTUNE COOKIE CHALLENGE\n\n")

#TASK:
#Write a program that simulates a fortune cookie. The program
#should display one of five unique fortunes, at random, each
#time it’s run

#WITH LIST:
a = "GOD LUCK. YOU'RE A GOD!" 
b = "SUNNY ONE. IT WILL BE FINE." 
c = "RAINY ONE. SO'LL BE WET NOW."
e = "DARK ONE. YOU CAN SEE BUT IT'S FADING."
d = "DEMON LUCK. YOU'RE OUT OF OPTIONS!"

pechenki = [a, b, c, d, e]

i = random.randrange(5)
print(pechenki[i])



