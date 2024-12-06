print("Hand over 2 numbers. (put 'q' to stop)")

while True:
    num1 = input("First number: ")
    if num1 == 'q':
        break

    num2 = input("Second number: ")
    if num2 == 'q':
        break

    try:
        print(int(num1) + int(num2))
    except ValueError:
        print("You can't add these.")