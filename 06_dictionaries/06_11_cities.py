cities = {
    "New_York":{
        "Country":"U.S.",
        "Population":"8.3 Million",
        "Fact":"Pizza is a huge deal!"
    },
    "Philadelphia":{
        "Country":"U.S.",
        "Population":"1.6 Million",
        "Fact":"Philadephia is the largest city in Pennsylvania."
    },
    "Tokyo":{
        "Country":"Japan",
        "Population":"14.18 Million",
        "Fact":"English is not widely spoken."
    }
}
for cities, info, in cities.items():
    print("City " + cities)
    details = ("\tLocated in: "+ info["Country"]) + ("\n\tPopulation: "+ info["Population"])+ ("\n\tOne fact: "+ info["Fact"])
    print(details)