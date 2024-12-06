import album
artist1= album.make_album("Eminem","Encore", 4)
print(artist1)

import album as al
artist2 = al.make_album("Eminem","Relapse")
print(artist2)

from album import make_album
artist3 = make_album("Eminem","Get the guns", 4)
print(artist3)

from album import make_album as MAL
artist4 = MAL("Eminem","Kamikaze")
print(artist4)

from album import *
artist5 = make_album("Eminem","Infinite")
print(artist5)