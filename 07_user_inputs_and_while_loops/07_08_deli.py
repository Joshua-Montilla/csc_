sandwich_orders = [
    "Ham Sandwich",
    "Bacon, Egg And Cheese Sandwich",
    "Grilled Cheese Sandwich",
    "Cuban Sandwich",
    "Turkey Sandwich",
    "Tuna Sandwich",
    "Pepperoni Sandwich"
 ]



finished_sandwiches = []

while sandwich_orders:
    made_orders = sandwich_orders.pop()

    print("\n Your " + made_orders +", is ready please enjoy.")
    finished_sandwiches.append(made_orders)

print("\n Here's all the sandwiches we have to offer:")
for sandwich in finished_sandwiches:
    print(sandwich)