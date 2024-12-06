def create_sandwich(*insides):
    print("\nAdding these to your food:")
    for item in insides:
        print(f"- {item}")

create_sandwich("Bacon", "Egg", "Chese")
create_sandwich("Tomato", "Lettuce", "Ham")
create_sandwich("Pepperoni", "Mayonnaise", "Ketchup", "Ham", "Cheese")