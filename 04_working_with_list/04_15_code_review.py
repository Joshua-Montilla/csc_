my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are;")
for m in my_foods:
    print(m)
print("\nMy friend's favorite foods are")
for f in friend_foods:
    print(f)

cubes = [value**3 for value in range(1,11)]
print(cubes)

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