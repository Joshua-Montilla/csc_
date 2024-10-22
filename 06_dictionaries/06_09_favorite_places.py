favorite_place = {
    "Joshua":["New York, Tokyo"],
    "\nGabriel":["Florida, Philadephia"],
    "\nJadrian":["Boston, Canada"]
}
for name, place in favorite_place.items():
    print(name)
    for area in place:
        print(area)