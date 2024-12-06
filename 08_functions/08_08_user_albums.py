def make_album(name, album, songs=None):
    artist = {"Artist": name, "Album": album}
    if songs:
        artist["Number of Songs"] = songs
    return artist

while True:
    print("Please input an artist and album")
    print("(Enter 'quit' to quit)")

    musician = input("Artist: ")
    if musician == 'quit':
        break

    al = input("Album: ")
    if al == 'quit':
        break

musician1 = make_album(musician, al)
print(musician1)