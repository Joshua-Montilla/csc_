def make_album(name, album, songs=None):
    artist = {"Artist": name, "Album": album}
    if songs:
        artist["Number of Songs"] = songs
    return artist

musician1 = make_album("Eminem", "The Eminem Show", 38)
print(musician1)
musician2 = make_album("Siames", "HOME")
print(musician2)
musician3 = make_album("Cigarettes After Sex", "Cry")
print(musician3)