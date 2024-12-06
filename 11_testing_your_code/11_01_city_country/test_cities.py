from city_funcitons import city_country

def test_city_country():
    area = city_country("New York", "U.S.")
    assert area == "New York, U.S."