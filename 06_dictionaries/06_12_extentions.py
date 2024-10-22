people1 = {
    "first_name":"Jordan",
    "last_name":"Star",
    "age":"17",
    "city":"New York"
}
people2 = {
    "first_name":"Jason",
    "last_name":"Ichinose",
    "age":"20",
    "city":"Japan"
}
people3 = {
    "first_name":"Jaiden",
    "last_name":"Phillps",
    "age":"19",
    "city":"Florida"
}
people = [people1, people2, people3]

favorite_number = [1,7,8]
favorite_number2 = [2,10,15] 

for person in people:
    print("\n"+ person["first_name"])
    print(person["last_name"])
    print(person["age"])
    print(person["city"])

    if person["first_name"] == "Jordan":
        print("\nHis favorite numbers are: \n"+ str(favorite_number))
    elif person["first_name"] == "Jason":
        print("\nHis favorite numbers are: \n"+ str(favorite_number2))
    else:
        print("\n"+ person["first_name"]+ ", What are your favorite numbers?")


    