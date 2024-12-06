def make_car(maker, model, **car_info):
    car_info["manufacturer"] = maker
    car_info["car model"] = model
    return car_info

car = make_car("Lamborghini", "Temerario", color = "blue", elctric_vehicle = True)

print(car)