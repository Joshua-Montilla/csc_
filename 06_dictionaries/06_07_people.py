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

for person in people:
    print(person["first_name"])
    print(person["last_name"])
    print(person["age"])
    print(person["city"])
    print("\n")