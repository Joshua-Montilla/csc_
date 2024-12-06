class User:
    def __init__(self, first_name, last_name, age, place):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.place = place
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.fname} likes to go places")
    
    def greet_user(self):
        print(f"Greetings, I'm {self.fname} {self.lname}, nice to meet you.")

person1 = User("MK", "Pig", 24, "Lego")

print(person1.login_attempts)
person1.increment_login_attempts()
print(person1.login_attempts)
person1.increment_login_attempts()
print(person1.login_attempts)
person1.increment_login_attempts()
print(person1.login_attempts)
person1.reset_login_attempts()
print(person1.login_attempts)