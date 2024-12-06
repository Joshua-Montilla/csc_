# 7 pretty difficult
from random import choice
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "E", "G", "Z", "X"]
chosen=0
winning_card= []
while chosen!=4:
    digit= (choice(digits))
    chosen+=1
    winning_card.append(digit)
print(f"IF your ticket lands the following:({winning_card}), you win!!!!!!!!!!!\n")