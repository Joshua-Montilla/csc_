prompts = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    prompt = input(name + ", if you could go anywhere you've ever wanted in the world, where would you go? ")

    prompts[name] = prompt

    repeat = input("Do you wish to respond again? y/n ")
    if repeat == "n":
        polling_active = False

print ("results: ")
for name, prompt in prompts.items():
    print(name + " Would want to go to " + prompt)