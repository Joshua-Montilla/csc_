prompt = "\n Welcome to the movie theater how old are you?:"
prompt += "\n (Enter 'quit' once you're finished.)"

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

