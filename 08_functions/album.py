def make_album(name, album, songs=None):
    artist = {"Artist": name, "Album": album}
    if songs:
        artist["Number of Songs"] = songs
    return artist