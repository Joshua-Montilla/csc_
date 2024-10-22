sandwich_orders = [
    "Ham Sandwich",
    "Bacon, Egg And Cheese Sandwich",
    "Grilled Cheese Sandwich",
    "Pastrami Sandwich",
    "Cuban Sandwich",
    "Turkey Sandwich",
    "Pastrami Sandwich",
    "Tuna Sandwich",
    "Pepperoni Sandwich",
    "Pastrami Sandwich"
 ]



finished_sandwiches = []

print("Unfortunately we have run out of Pastrami.")
while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")


while sandwich_orders:
    made_orders = sandwich_orders.pop()

    print("\n Your " + made_orders +", is ready please enjoy.")
    finished_sandwiches.append(made_orders)

print("\n Here's all the sandwiches we have to offer:")
for sandwich in finished_sandwiches:
    print(sandwich)