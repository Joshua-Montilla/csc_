from employee import Employee

def test_give_default_raise():
    person = Employee("Joshua", "Montilla", -250)
    person.give_raise()
    assert person.salary == 4750

def test_give_custom_raise():
    person = Employee("Joshua", "Montilla", -250)
    person.give_raise(2)
    assert person.salary == -248