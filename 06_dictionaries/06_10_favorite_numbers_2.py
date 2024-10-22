favorite_number = {
    "Scarlet":["2 ,3, 20, 80"],
    "\nJason":["92, 27, 49, 50"],
    "\nEmil":["900, 203, 495, 22"],
    "\nJack":["1,303, 430, 706, 34"],
    "\nJoshua":["7, 2, 777, 1,403"]
}
for name, number in favorite_number.items():
    print(name + "'s favorite numbers are:")
    for word in number:
        print (word)


#print("\nScarlet's favorite numbers are " + favorite_number["Scarlet"])
#print("\nJason's favorite numbers are " + favorite_number["Jason"])
#print("\nEmil's favorite numbers are " + favorite_number["Emil"])
#print("\nJack's favorite numbers are " + favorite_number["Jack"])
#print("\nJoshua's favorite numbers are " + favorite_number["Joshua"])