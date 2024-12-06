def city_country(city, country, population=None):
    if population:
        place = f"{city}, {country} - population = {str(population)}"
    else:
        place = f"{city}, {country}"
    return place