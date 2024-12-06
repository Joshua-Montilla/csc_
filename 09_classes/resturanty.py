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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = ["Chocolate", "Vanilla", "Cookies and cream", "Chocolate with fudge"]
    
    def describe_flavors(self):
        print(f"{self.name} has many different flavors, such as:")
        for yum in self.flavor:
            print(f"- {yum}")

