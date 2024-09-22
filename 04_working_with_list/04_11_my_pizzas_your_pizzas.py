
my_pizza = ["Pepperoni", "Beef", "Bacon"]
friend_pizza = my_pizza[:]
my_pizza.append("Ham")
friend_pizza.append("alfredo")
message = "My favorite pizzas are;"
print(message)
for p in my_pizza:
    print(p)

message = "\nMy friend's favorite pizzas are;"
print(message)
for f in friend_pizza:
    print (f)