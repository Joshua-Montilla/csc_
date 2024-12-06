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

class Privileges:
    def __init__(self, privileges=["Ban users", "IP Ban", "Remove content", "Send private posts", "Create/Adjust rules"]):
        self.privileges = privileges

    def show_privileges(self):
        print("As an Admin you can:")
        for access in self.privileges:
            print(f"- {access}")

class Admin(User):
    def __init__(self, first_name, last_name, age, place):
        super().__init__(first_name, last_name, age, place)
        self.privilege = Privileges()
    
man = Admin("Jaque", "Maeyson", 45, "N/A")
man.privilege.show_privileges()
