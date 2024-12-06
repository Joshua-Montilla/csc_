class Employee:
    def __init__(self, first_name, last_name, annual_salary=0):
        self.fname = first_name
        self.lname = last_name
        self.salary = annual_salary

    def give_raise(self, money=5000):
        self.money = money
        self.salary += self.money