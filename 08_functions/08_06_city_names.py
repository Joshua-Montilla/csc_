def city_country(city, country):
    area = f"\n {city}, {country}"
    return area.title()

place1 = city_country("tampa", "united states")
print(place1)
place2 = city_country("puebla", "Mexico")
print(place2)
place3 = city_country("chennai", "India")
print(place3)