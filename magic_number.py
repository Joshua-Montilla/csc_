#I wanted to do this for fun while it was on screen but didn't get it all :(

import random

magicNumber = random.random () * 1000
print (magicNumber)
magicNumber = int(magicNumber)
print(magicNumber)
numTries = 0
while True:
    answer = input ("Please guess the number:")
    answer = int(answer)
    numTries = numTries + 1
    if answer > magicNumber:
        print("Too High")
    elif answer < magicNumber:
        print("Too Low")
    else:
        print("You got it!")
        break
print ("You took" + str(numTries))