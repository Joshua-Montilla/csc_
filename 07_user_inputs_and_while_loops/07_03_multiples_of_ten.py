number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
    print("this number, " + str(number) + " is a multiple of 10")
else:
    print("This number is not a multiple of 10, please try again.")