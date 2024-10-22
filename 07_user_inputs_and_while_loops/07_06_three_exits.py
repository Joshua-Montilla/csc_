prompt = "\n Welcome to the movie theater how old are you?:"
prompt += "\n (Enter 'quit' once you're finished.)"

letter = 1
while letter <= 60:
    print(letter)
    letter += 1


active = True
while active:
    message = input("Don't you ever question your life choices and how you got here? y/n")
    if message == "n":
        print("Oh... That sucks.")
        active = False
    else:
        message = print("Ah.. Me too man, me too...")
        active = False

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            age = str(age)
            print("If you are " + age + " years old, the tickets are free!")
        elif age < 13:
            age = str(age)
            print("If you are " + age + " years old, the tickets are 10$!")
        else:
            age = str(age)
            print("If you are " + age + " years old, the tickets are 15$!")