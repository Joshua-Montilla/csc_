class User:
    def __init__(self, first_name, last_name, age, place):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.place = place
    
    def describe_user(self):
        print(f"{self.fname} likes to go places")
    
    def greet_user(self):
        print(f"Greetings, I'm {self.fname} {self.lname}, nice to meet you.")

person1 = User("MK", "Pig", 24, "Lego")

print(person1.fname + "\n" + person1.lname + "\n" + str(person1.age) + "\n" + person1.place)
person1.describe_user()

person1.greet_user()
print("\n")

person2 = User("Mae", "Sakano", 18, "EU")

print(person2.fname + "\n" + person2.lname + "\n" + str(person2.age) + "\n" + person2.place)
person2.describe_user()

person2.greet_user()
print("\n")

person3 = User("Luigi", "Mario", 25, "Mushroom Kingdom")

print(person3.fname + "\n" + person3.lname + "\n" + str(person3.age) + "\n" + person3.place)
person3.describe_user()

person3.greet_user()