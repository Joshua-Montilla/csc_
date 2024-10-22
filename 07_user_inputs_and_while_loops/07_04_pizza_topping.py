prompt = "\n Please enter a pizza topping you'd like on your pizza:"
prompt += "\n (Enter 'quit' once you're finished.)"

while True:
    Topping = input(prompt)

    if Topping == 'quit':
        break
    else:
        print(f"I'd love some {Topping.title()} on my pizza!")