print("Hand over 2 numbers.")
num1 = input("First number: ")
num2 = input("Second number: ")
try:
    print(int(num1) + int(num2))
except ValueError:
    print("You can't add these.")