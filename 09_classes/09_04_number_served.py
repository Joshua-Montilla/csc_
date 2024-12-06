class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type
        self.number_served = 10 #0 
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, meals):
        self.number_served += meals

    def describe_restaurant(self):
        print(f"{self.name} only sells {self.food}")
        print("This restaurant is in support of no refunds")
    
    def open_restaurant(self):
        print(f"{self.name} is open")

restaurant = Restaurant("Jake's Steakout", "Steaks")
restaurant.set_number_served(50)
print(f"{restaurant.number_served} was made yesterday")
restaurant.increment_number_served(85)
print(f"{restaurant.number_served} was made today")