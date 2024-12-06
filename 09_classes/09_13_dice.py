# 4
from random import randint
class Die:
    def __init__(self, sides= 6):
        self.side = sides
    
    def roll_die(self):
        rolls = 0
        while rolls != 10:
            print(randint(1,self.side))
            rolls +=1


sixsided = Die()
sixsided.roll_die()

print("\n")
tensided = Die(10)
tensided.roll_die()

print("\n")
twentysided = Die(20)
twentysided.roll_die()

print("\n")
hundredsided = Die(100)
hundredsided.roll_die()