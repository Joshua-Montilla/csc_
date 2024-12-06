from one_user import User

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