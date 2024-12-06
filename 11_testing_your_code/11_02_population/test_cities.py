from city_functions import city_country

def test_city_country():
    area = city_country("New York", "U.S.")
    assert area == "New York, U.S."

def test_city_country():
    area = city_country("New York", "U.S.", 200000)
    assert area == "New York, U.S. - population = 200000"