Games = ["Infamous", "Cod3", "Roblox", "Minecraft"]
print(Games)

Games.sort()
print(Games)

Games.insert(2,"Limbus Company")
print(Games)
print(len(Games))
print(Games)

del Games[0]
print(Games)

print(sorted(Games,reverse=True))

Games.append("GangBeast")
print(Games)

print("My favorite game is " + Games[1])

print("I don't play " + Games[4] +  " as much as I play other games")
Games.pop(4)
print(Games)

Games.sort(reverse=True)
Games.sort()
print(len(Games))

#print("This is the list of my favorite games" (Games)) The error here is missing a + on the space between the quotation and the ( with games. This also wouldn't work because I cannot print the whole list within that sentence but can choose one of the things within the list to use for that sentence. I'd have to print my list after writing down that sentence.
print("This is the list of my favorite games.")
print(Games)