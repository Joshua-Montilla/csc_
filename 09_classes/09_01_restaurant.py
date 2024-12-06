class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} only sells {self.food}")
        print("This restaurant is in support of no refunds")
    
    def open_restaurant(self):
        print(f"{self.name} is open")

restaurant = Restaurant("Jake's Steakout", "Steaks")

print(restaurant.name)
print(restaurant.food)

restaurant.describe_restaurant()

restaurant.open_restaurant()